from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Any

import requests

from .models import DraftRecord

W3C_SPECIFICATIONS_URL = "https://api.w3.org/specifications"


def fetch_recent_w3c_specs(session: requests.Session, *, since_days: int) -> tuple[list[DraftRecord], list[str]]:
    try:
        response = session.get(W3C_SPECIFICATIONS_URL, timeout=30)
        response.raise_for_status()
        payload: Any = response.json()
    except Exception as exc:
        return [], [f"w3c specifications fetch failed: {exc}"]

    cutoff = date.today() - timedelta(days=since_days)
    records = extract_w3c_specifications(payload, cutoff=cutoff)
    return records, []


def extract_w3c_specifications(payload: Any, *, cutoff: date | None = None) -> list[DraftRecord]:
    records: dict[str, DraftRecord] = {}
    for item in _collect_spec_items(payload):
        shortname = _pick_first_string(item, ["shortname", "shortName", "name", "slug", "id"])
        if not shortname:
            continue

        normalized_shortname = _slugify(shortname)
        if not normalized_shortname:
            continue

        updated_at = _pick_first_string(
            item,
            [
                "updated",
                "modified",
                "lastModified",
                "date",
                "published",
                "created",
            ],
        )
        parsed_updated = _parse_date(updated_at)
        if cutoff is not None and parsed_updated and parsed_updated < cutoff:
            continue

        version = int(parsed_updated.strftime("%Y%m%d")) if parsed_updated else 0
        version_suffix = parsed_updated.strftime("%Y%m%d") if parsed_updated else "latest"
        base_name = f"w3c-{normalized_shortname}"
        versioned_name = f"{base_name}-{version_suffix}"
        url = _pick_first_string(
            item,
            [
                "uri",
                "url",
                "href",
                "edDraft",
                "editorDraft",
                "shortlink",
            ],
        ) or f"https://www.w3.org/TR/{normalized_shortname}/"
        title = _pick_first_string(item, ["title", "shortTitle", "shorttitle", "name"]) or shortname
        abstract = _pick_first_string(item, ["abstract", "description", "summary"])
        group_name = _pick_first_string(item, ["group", "publisher", "organization", "wg"])

        records[versioned_name] = DraftRecord(
            versioned_name=versioned_name,
            base_name=base_name,
            version=version,
            datatracker_url=url,
            title=title,
            abstract=abstract,
            group_name=group_name,
            source_updated_at=updated_at,
        )

    return sorted(records.values(), key=lambda record: record.versioned_name)


def _collect_spec_items(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, dict):
        if isinstance(payload, list):
            queue: list[Any] = [payload]
        else:
            return []
    else:
        queue = [payload]

    candidates: list[dict[str, Any]] = []
    while queue:
        current = queue.pop(0)
        if isinstance(current, list):
            queue.extend(current)
            continue
        if not isinstance(current, dict):
            continue
        if _looks_like_spec(current):
            candidates.append(current)
        for value in current.values():
            if isinstance(value, (list, dict)):
                queue.append(value)
    return candidates


def _looks_like_spec(item: dict[str, Any]) -> bool:
    has_name = any(key in item for key in ("shortname", "shortName", "name", "title"))
    has_link = any(key in item for key in ("uri", "url", "href", "shortlink"))
    return has_name and has_link


def _pick_first_string(payload: dict[str, Any], paths: list[str]) -> str:
    for path in paths:
        value = payload.get(path)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, dict):
            for nested_key in ["title", "name", "value", "uri", "href"]:
                nested = value.get(nested_key)
                if isinstance(nested, str) and nested.strip():
                    return nested.strip()
    return ""


def _slugify(value: str) -> str:
    chars = []
    for char in value.lower().strip():
        if char.isalnum():
            chars.append(char)
        elif chars and chars[-1] != "-":
            chars.append("-")
    return "".join(chars).strip("-")


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
