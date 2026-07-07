from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(slots=True)
class WatchConfig:
    report_title: str
    minimum_reporting_threshold: int
    keywords: list[str]
    wg_boosts: list[str]
    categories: dict[str, list[str]]


DEFAULT_CONFIG_PATH = Path("config/default.yaml")


def _normalize_list(values: list[str]) -> list[str]:
    return [value.strip() for value in values if value and value.strip()]


def load_config(path: str | Path | None = None) -> WatchConfig:
    config_path = Path(path) if path else DEFAULT_CONFIG_PATH
    with config_path.open("r", encoding="utf-8") as handle:
        raw: dict[str, Any] = yaml.safe_load(handle) or {}
    return WatchConfig(
        report_title=raw.get("report_title", "IETF Identity + AI Standards Watch"),
        minimum_reporting_threshold=int(raw.get("minimum_reporting_threshold", 4)),
        keywords=_normalize_list(list(raw.get("keywords", []))),
        wg_boosts=_normalize_list(list(raw.get("wg_boosts", []))),
        categories={
            key: _normalize_list(list(values))
            for key, values in dict(raw.get("categories", {})).items()
        },
    )
