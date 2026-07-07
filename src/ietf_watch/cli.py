from __future__ import annotations

import argparse
import logging
from datetime import date
from pathlib import Path

import requests

from .classify import classify_record, maybe_apply_llm
from .config import DEFAULT_CONFIG_PATH, load_config
from .datatracker import fetch_recent_drafts
from .reporting import write_reports
from .storage import WatchStore

LOGGER = logging.getLogger(__name__)
DEFAULT_DB_PATH = Path(".data/ietf_watch.db")
DEFAULT_REPORTS_PATH = Path("reports")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Monitor recent IETF drafts relevant to identity and AI trust.")
    parser.add_argument("--use-llm", action="store_true", help="Use OPENAI_API_KEY-backed classification refinement.")
    parser.add_argument("--since-days", type=int, default=7, help="Recent window to inspect from Datatracker.")
    parser.add_argument("--min-relevance", type=int, default=None, help="Override minimum reporting threshold.")
    parser.add_argument("--dry-run", action="store_true", help="Generate reports without persisting reviewed drafts.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="Path to YAML configuration.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    config = load_config(args.config)
    if args.min_relevance is not None:
        config.minimum_reporting_threshold = args.min_relevance

    session = requests.Session()
    store = WatchStore(DEFAULT_DB_PATH)
    today = date.today()
    try:
        records, errors = fetch_recent_drafts(session, since_days=args.since_days)
        report_records = []
        for record in records:
            if store.has_seen_version(record.versioned_name):
                LOGGER.info("Skipping already reviewed version %s", record.versioned_name)
                continue
            record.date_seen = today
            record.status = "new-version" if store.has_seen_base(record.base_name) else "new-draft"
            deterministic = classify_record(record, config)
            classification = maybe_apply_llm(
                record,
                deterministic,
                config,
                enabled=args.use_llm,
            )
            record.category = classification.category
            record.bucket = classification.bucket
            record.relevance_score = classification.relevance_score
            record.rationale = classification.rationale
            record.matched_keywords = classification.matched_keywords
            report_records.append(record)

        markdown_path, csv_path = write_reports(report_records, errors, config, today, DEFAULT_REPORTS_PATH)
        LOGGER.info("Wrote reports to %s and %s", markdown_path, csv_path)

        if not args.dry_run:
            for record in report_records:
                store.save(record)
        return 0
    finally:
        session.close()
        store.close()


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
