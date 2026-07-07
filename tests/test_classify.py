from datetime import date

from ietf_watch.classify import classify_record, score_keywords
from ietf_watch.config import WatchConfig
from ietf_watch.models import DraftRecord


TEST_CONFIG = WatchConfig(
    report_title="Test",
    minimum_reporting_threshold=4,
    keywords=["oauth", "identity", "ai", "trust", "attestation"],
    wg_boosts=["oauth", "rats"],
    categories={
        "authorization": ["oauth", "authorization", "agent authority"],
        "trust_infrastructure": ["attestation", "trust"],
        "adjacent_watchlist": ["model"],
    },
)


def test_keyword_scoring_counts_unique_matches() -> None:
    score, matches = score_keywords("OAuth identity trust", TEST_CONFIG.keywords)
    assert score == 6
    assert matches == ["identity", "oauth", "trust"]


def test_keyword_scoring_avoids_partial_word_matches() -> None:
    score, matches = score_keywords("The chair said the mail arrived.", TEST_CONFIG.keywords)
    assert score == 0
    assert matches == []


def test_deterministic_category_assignment_prefers_strongest_match() -> None:
    record = DraftRecord(
        versioned_name="draft-ietf-oauth-sample-00",
        base_name="draft-ietf-oauth-sample",
        version=0,
        datatracker_url="https://example.test",
        title="OAuth Attestation for Agent Authority",
        abstract="Defines authorization signals and attestation for AI agents.",
        group_name="oauth",
        date_seen=date(2026, 7, 7),
    )
    result = classify_record(record, TEST_CONFIG)
    assert result.category == "authorization"
    assert result.bucket in {"read_now", "monitor"}
    assert result.relevance_score >= 7
