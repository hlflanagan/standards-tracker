from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

from .config import WatchConfig
from .models import DraftRecord

SECTION_TITLES = {
    "read_now": "Read now",
    "monitor": "Monitor",
    "adjacent_watchlist": "Adjacent / watchlist",
    "ignored_after_review": "Ignored after review",
}


def write_reports(
    records: list[DraftRecord],
    errors: list[str],
    config: WatchConfig,
    report_date: date,
    output_dir: Path,
) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{report_date.isoformat()}-ietf-identity-ai-watch"
    markdown_path = output_dir / f"{stem}.md"
    csv_path = output_dir / f"{stem}.csv"
    markdown_path.write_text(render_markdown(records, errors, config, report_date), encoding="utf-8")
    write_csv(records, errors, csv_path)
    return markdown_path, csv_path


def render_markdown(
    records: list[DraftRecord],
    errors: list[str],
    config: WatchConfig,
    report_date: date,
) -> str:
    grouped = {key: [] for key in SECTION_TITLES}
    for record in records:
        grouped.setdefault(record.bucket, []).append(record)

    lines = [f"# {config.report_title}", "", f"Date: {report_date.isoformat()}", ""]
    for key, title in SECTION_TITLES.items():
        lines.append(f"## {title}")
        lines.append("")
        section_records = grouped.get(key, [])
        if not section_records:
            lines.append("_None._")
            lines.append("")
            continue
        for record in sorted(section_records, key=lambda item: (-item.relevance_score, item.versioned_name)):
            summary = f"- **{record.versioned_name}** ({record.status}, score {record.relevance_score}, {record.category})"
            if record.group_name:
                summary += f" [{record.group_name}]"
            summary += f": [{record.title or record.base_name}]({record.datatracker_url})"
            if record.abstract:
                summary += f" — {record.abstract}"
            lines.append(summary)
        lines.append("")

    lines.append("## Errors / fetch failures")
    lines.append("")
    if not errors:
        lines.append("_None._")
    else:
        for error in errors:
            lines.append(f"- {error}")
    lines.append("")
    return "\n".join(lines)


def write_csv(records: list[DraftRecord], errors: list[str], destination: Path) -> None:
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "versioned_name",
                "base_name",
                "version",
                "status",
                "bucket",
                "category",
                "relevance_score",
                "group_name",
                "title",
                "abstract",
                "datatracker_url",
                "date_seen",
                "error",
            ],
        )
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "versioned_name": record.versioned_name,
                    "base_name": record.base_name,
                    "version": record.version,
                    "status": record.status,
                    "bucket": record.bucket,
                    "category": record.category,
                    "relevance_score": record.relevance_score,
                    "group_name": record.group_name,
                    "title": record.title,
                    "abstract": record.abstract,
                    "datatracker_url": record.datatracker_url,
                    "date_seen": record.date_seen.isoformat() if record.date_seen else "",
                    "error": record.error,
                }
            )
        for error in errors:
            writer.writerow({"error": error})
