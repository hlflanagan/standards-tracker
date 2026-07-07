from __future__ import annotations

import sqlite3
from pathlib import Path

from .models import DraftRecord


class WatchStore:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self._initialize()

    def _initialize(self) -> None:
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS drafts_seen (
                versioned_name TEXT PRIMARY KEY,
                base_name TEXT NOT NULL,
                version INTEGER NOT NULL,
                datatracker_url TEXT NOT NULL,
                title TEXT,
                abstract TEXT,
                group_name TEXT,
                date_seen TEXT NOT NULL,
                status TEXT NOT NULL,
                category TEXT NOT NULL,
                bucket TEXT NOT NULL,
                relevance_score INTEGER NOT NULL,
                rationale TEXT NOT NULL
            )
            """
        )
        self.connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_drafts_seen_base_name ON drafts_seen(base_name)"
        )
        self.connection.commit()

    def has_seen_version(self, versioned_name: str) -> bool:
        row = self.connection.execute(
            "SELECT 1 FROM drafts_seen WHERE versioned_name = ?",
            (versioned_name,),
        ).fetchone()
        return row is not None

    def has_seen_base(self, base_name: str) -> bool:
        row = self.connection.execute(
            "SELECT 1 FROM drafts_seen WHERE base_name = ? LIMIT 1",
            (base_name,),
        ).fetchone()
        return row is not None

    def save(self, record: DraftRecord) -> None:
        self.connection.execute(
            """
            INSERT OR REPLACE INTO drafts_seen (
                versioned_name, base_name, version, datatracker_url, title, abstract,
                group_name, date_seen, status, category, bucket, relevance_score, rationale
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.versioned_name,
                record.base_name,
                record.version,
                record.datatracker_url,
                record.title,
                record.abstract,
                record.group_name,
                record.date_seen.isoformat() if record.date_seen else "",
                record.status,
                record.category,
                record.bucket,
                record.relevance_score,
                record.rationale,
            ),
        )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
