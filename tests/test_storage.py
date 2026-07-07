from datetime import date
from pathlib import Path

from ietf_watch.models import DraftRecord
from ietf_watch.storage import WatchStore


def test_sqlite_deduplicates_seen_versions(tmp_path: Path) -> None:
    store = WatchStore(tmp_path / "watch.db")
    record = DraftRecord(
        versioned_name="draft-ietf-oauth-sample-00",
        base_name="draft-ietf-oauth-sample",
        version=0,
        datatracker_url="https://example.test",
        title="OAuth Sample",
        date_seen=date(2026, 7, 7),
        status="new-draft",
        category="authorization",
        bucket="monitor",
        relevance_score=5,
        rationale="test",
    )
    store.save(record)
    assert store.has_seen_version("draft-ietf-oauth-sample-00") is True
    assert store.has_seen_base("draft-ietf-oauth-sample") is True
    store.close()
