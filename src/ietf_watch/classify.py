from __future__ import annotations

import json
import logging
import os
import re
from collections import Counter
from typing import Any

import requests

from .config import WatchConfig
from .models import ClassificationResult, DraftRecord

LOGGER = logging.getLogger(__name__)
NETWORK_AI_HINTS = {"telemetry", "traffic engineering", "network optimization", "routing"}
CORE_AI_TRUST_HINTS = {"identity", "credential", "authorization", "auth", "trust", "provenance", "governance", "privacy", "attestation"}


def score_keywords(text: str, keywords: list[str]) -> tuple[int, list[str]]:
    lowered = text.lower()
    matches = [keyword for keyword in keywords if contains_keyword(lowered, keyword)]
    return len(matches) * 2, sorted(set(matches))


def classify_record(record: DraftRecord, config: WatchConfig) -> ClassificationResult:
    text = " ".join(part for part in [record.title, record.abstract] if part).lower()
    score, matched_keywords = score_keywords(text, config.keywords)

    if record.group_name and record.group_name.lower() in {item.lower() for item in config.wg_boosts}:
        score += 3
        matched_keywords.append(f"wg:{record.group_name.lower()}")

    category_hits: Counter[str] = Counter()
    for category, category_keywords in config.categories.items():
        for keyword in category_keywords:
            if contains_keyword(text, keyword):
                score += 1
                category_hits[category] += 1

    if contains_keyword(text, "ai") and not any(contains_keyword(text, hint) for hint in CORE_AI_TRUST_HINTS):
        if any(contains_keyword(text, hint) for hint in NETWORK_AI_HINTS):
            score = max(0, score - 3)

    if category_hits:
        category = category_hits.most_common(1)[0][0]
    elif score >= max(1, config.minimum_reporting_threshold - 1):
        category = "adjacent_watchlist"
    else:
        category = "ignored_after_review"

    bucket = assign_bucket(score, config.minimum_reporting_threshold, category)
    rationale = (
        f"score={score}; category={category}; matched={', '.join(sorted(set(matched_keywords))) or 'none'}"
    )
    return ClassificationResult(
        category=category,
        bucket=bucket,
        relevance_score=score,
        rationale=rationale,
        matched_keywords=sorted(set(matched_keywords)),
    )


def assign_bucket(score: int, threshold: int, category: str) -> str:
    if score >= threshold + 3:
        return "read_now"
    if score >= threshold:
        return "monitor"
    if score > 0 or category == "adjacent_watchlist":
        return "adjacent_watchlist"
    return "ignored_after_review"


def contains_keyword(text: str, keyword: str) -> bool:
    normalized = keyword.lower().strip()
    if not normalized:
        return False
    pattern = re.compile(rf"(?<![a-z0-9]){re.escape(normalized)}(?![a-z0-9])")
    return bool(pattern.search(text.lower()))


def maybe_apply_llm(
    record: DraftRecord,
    deterministic: ClassificationResult,
    config: WatchConfig,
    *,
    enabled: bool,
    timeout: int = 30,
) -> ClassificationResult:
    if not enabled:
        return deterministic

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        LOGGER.warning("--use-llm requested but OPENAI_API_KEY is not set; using deterministic classification")
        return deterministic

    prompt = {
        "title": record.title,
        "abstract": record.abstract,
        "group": record.group_name,
        "deterministic_category": deterministic.category,
        "deterministic_bucket": deterministic.bucket,
        "deterministic_score": deterministic.relevance_score,
        "allowed_categories": list(config.categories.keys()) + ["ignored_after_review"],
        "allowed_buckets": ["read_now", "monitor", "adjacent_watchlist", "ignored_after_review"],
        "guidance": "Do not treat generic AI/network optimization drafts as relevant unless they address identity, authority, credentials, provenance, governance, privacy, or trust.",
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload: dict[str, Any] = {
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "temperature": 0,
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": "Return strict JSON with category, bucket, relevance_score, and rationale.",
            },
            {"role": "user", "content": json.dumps(prompt)},
        ],
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=timeout,
        )
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        category = str(parsed.get("category", deterministic.category))
        bucket = str(parsed.get("bucket", deterministic.bucket))
        if category not in prompt["allowed_categories"] or bucket not in prompt["allowed_buckets"]:
            return deterministic
        return ClassificationResult(
            category=category,
            bucket=bucket,
            relevance_score=int(parsed.get("relevance_score", deterministic.relevance_score)),
            rationale=str(parsed.get("rationale", deterministic.rationale)),
            matched_keywords=deterministic.matched_keywords,
        )
    except Exception as exc:  # pragma: no cover - defensive network failure handling
        LOGGER.warning("LLM classification failed for %s: %s", record.versioned_name, exc)
        return deterministic
