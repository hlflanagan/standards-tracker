from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass(slots=True)
class DraftRecord:
    versioned_name: str
    base_name: str
    version: int
    datatracker_url: str
    title: str = ""
    abstract: str = ""
    group_name: str = ""
    date_seen: date | None = None
    status: str = "new-draft"
    category: str = "ignored_after_review"
    bucket: str = "ignored_after_review"
    relevance_score: int = 0
    rationale: str = ""
    source_updated_at: str = ""
    error: str = ""
    matched_keywords: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ClassificationResult:
    category: str
    bucket: str
    relevance_score: int
    rationale: str
    matched_keywords: list[str]
