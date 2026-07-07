from __future__ import annotations

import logging
import re
from datetime import date, datetime, timedelta
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .models import DraftRecord

LOGGER = logging.getLogger(__name__)
RECENT_URL = "https://datatracker.ietf.org/doc/recent"
DOC_JSON_TEMPLATE = "https://datatracker.ietf.org/doc/{base_name}/doc.json"
DRAFT_NAME_RE = re.compile(r"\b(draft-[a-z0-9-]+)-(\d{2})\b", re.IGNORECASE)


def parse_draft_name(value: str) -> tuple[str, str, int]:
    normalized = value.strip().lower()
    match = DRAFT_NAME_RE.fullmatch(normalized)
    if not match:
        raise ValueError(f"Invalid draft name: {value}")
    base_name = match.group(1)
    version = int(match.group(2))
    return normalized, base_name, version


def extract_recent_draft_names(html: str) -> list[DraftRecord]:
    soup = BeautifulSoup(html, "html.parser")
    records: dict[str, DraftRecord] = {}

    for anchor in soup.find_all("a", href=True):
        candidate_text = " ".join(filter(None, [anchor.get_text(" ", strip=True), anchor["href"]]))
        for match in DRAFT_NAME_RE.finditer(candidate_text.lower()):
            versioned_name, base_name, version = parse_draft_name(match.group(0))
            if versioned_name in records:
                continue
            href = anchor["href"]
            datatracker_url = href if href.startswith("http") else urljoin(RECENT_URL, href)
            title = anchor.get_text(" ", strip=True)
            if title.lower() == versioned_name:
                title = _extract_context_title(anchor, versioned_name)
            records[versioned_name] = DraftRecord(
                versioned_name=versioned_name,
                base_name=base_name,
                version=version,
                datatracker_url=datatracker_url,
                title=title,
            )
    return sorted(records.values(), key=lambda record: record.versioned_name)


def _extract_context_title(anchor: Any, versioned_name: str) -> str:
    container = anchor.find_parent(["tr", "li", "article", "div"])
    if not container:
        return ""
    parts = [part.strip() for part in container.stripped_strings if part.strip()]
    cleaned = [part for part in parts if part.lower() != versioned_name.lower()]
    return cleaned[0] if cleaned else ""


def fetch_recent_drafts(session: requests.Session, *, since_days: int) -> tuple[list[DraftRecord], list[str]]:
    errors: list[str] = []
    try:
        response = session.get(RECENT_URL, timeout=30)
        response.raise_for_status()
    except Exception as exc:
        return [], [f"recent drafts fetch failed: {exc}"]

    records = extract_recent_draft_names(response.text)
    cutoff = date.today() - timedelta(days=since_days)
    filtered: list[DraftRecord] = []
    for record in records:
        try:
            include_record = enrich_record_from_metadata(session, record, cutoff=cutoff)
        except Exception as exc:  # pragma: no cover - defensive failure capture
            record.error = str(exc)
            errors.append(f"{record.base_name}: metadata fetch failed: {exc}")
            filtered.append(record)
            continue
        if include_record:
            filtered.append(record)
    return filtered, errors


def enrich_record_from_metadata(
    session: requests.Session,
    record: DraftRecord,
    *,
    cutoff: date | None = None,
) -> bool:
    response = session.get(DOC_JSON_TEMPLATE.format(base_name=record.base_name), timeout=30)
    response.raise_for_status()
    payload: dict[str, Any] = response.json()

    record.title = _pick_first_string(payload, ["title", "name"]) or record.title
    record.abstract = _pick_first_string(payload, ["abstract"])
    record.group_name = _extract_group_name(payload)
    record.source_updated_at = _pick_first_string(
        payload,
        ["rev", "time", "updated", "created", "expires"],
    )

    if cutoff is not None:
        parsed_date = _parse_date(record.source_updated_at)
        if parsed_date and parsed_date < cutoff:
            LOGGER.info("Skipping %s because metadata date %s is older than cutoff %s", record.versioned_name, parsed_date, cutoff)
            return False
    return True


def _pick_first_string(payload: dict[str, Any], paths: list[str]) -> str:
    for path in paths:
        value = payload.get(path)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip():
                    return item.strip()
                if isinstance(item, dict):
                    for nested in item.values():
                        if isinstance(nested, str) and nested.strip():
                            return nested.strip()
        if isinstance(value, dict):
            for nested_key in ["title", "name", "value", "slug", "acronym", "rev"]:
                nested = value.get(nested_key)
                if isinstance(nested, str) and nested.strip():
                    return nested.strip()
    return ""


def _extract_group_name(payload: dict[str, Any]) -> str:
    for key in ["group", "wg", "working_group", "stream"]:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, dict):
            for nested_key in ["acronym", "name", "slug"]:
                nested = value.get(nested_key)
                if isinstance(nested, str) and nested.strip():
                    return nested.strip()
    return ""


def _parse_date(value: str) -> date | None:
    if not value:
        return None
    normalized = value.strip().replace("Z", "+00:00")
    for pattern in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.strptime(normalized, pattern).date()
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(normalized).date()
    except ValueError:
        return None
