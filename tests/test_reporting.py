from datetime import date
from pathlib import Path

from ietf_watch.config import WatchConfig
from ietf_watch.models import DraftRecord
from ietf_watch.reporting import render_markdown, write_reports


def test_markdown_report_generation(tmp_path: Path) -> None:
    config = WatchConfig(
        report_title="Watch Report",
        minimum_reporting_threshold=4,
        keywords=[],
        wg_boosts=[],
        categories={},
    )
    record = DraftRecord(
        versioned_name="draft-ietf-oauth-sample-01",
        base_name="draft-ietf-oauth-sample",
        version=1,
        datatracker_url="https://example.test",
        title="OAuth Sample",
        abstract="Sample abstract",
        group_name="oauth",
        date_seen=date(2026, 7, 7),
        status="new-version",
        category="authorization",
        bucket="read_now",
        relevance_score=8,
        rationale="test",
    )
    markdown = render_markdown([record], ["metadata fetch failed"], config, date(2026, 7, 7))
    assert "## Read now" in markdown
    assert "draft-ietf-oauth-sample-01" in markdown
    assert "## Errors / fetch failures" in markdown

    markdown_path, csv_path = write_reports([record], [], config, date(2026, 7, 7), tmp_path)
    assert markdown_path.exists()
    assert csv_path.exists()
