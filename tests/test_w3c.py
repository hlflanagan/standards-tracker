from __future__ import annotations

from datetime import date

from ietf_watch.w3c import extract_w3c_specifications, fetch_recent_w3c_specs


class _FakeResponse:
    def __init__(self, payload: object) -> None:
        self._payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> object:
        return self._payload


class _FakeSession:
    def __init__(self, payload: object) -> None:
        self.payload = payload

    def get(self, *_: object, **__: object) -> _FakeResponse:
        return _FakeResponse(self.payload)


def test_extract_w3c_specifications_parses_nested_payload() -> None:
    payload = {
        "items": [
            {
                "shortname": "vc-data-model",
                "title": "Verifiable Credentials Data Model",
                "uri": "https://www.w3.org/TR/vc-data-model/",
                "description": "Credential data model",
                "updated": "2026-07-07",
                "group": "vcwg",
            }
        ]
    }

    records = extract_w3c_specifications(payload)

    assert len(records) == 1
    record = records[0]
    assert record.base_name == "w3c-vc-data-model"
    assert record.versioned_name == "w3c-vc-data-model-20260707"
    assert record.version == 20260707
    assert record.datatracker_url == "https://www.w3.org/TR/vc-data-model/"
    assert record.abstract == "Credential data model"
    assert record.group_name == "vcwg"


def test_extract_w3c_specifications_honors_cutoff() -> None:
    payload = {
        "items": [
            {
                "shortname": "did-core",
                "uri": "https://www.w3.org/TR/did-core/",
                "updated": "2024-01-01",
            }
        ]
    }

    records = extract_w3c_specifications(payload, cutoff=date(2026, 1, 1))

    assert records == []


def test_extract_w3c_specifications_includes_record_on_cutoff_boundary() -> None:
    payload = {
        "items": [
            {
                "shortname": "did-core",
                "uri": "https://www.w3.org/TR/did-core/",
                "updated": "2026-01-01",
            }
        ]
    }

    records = extract_w3c_specifications(payload, cutoff=date(2026, 1, 1))

    assert len(records) == 1


def test_fetch_recent_w3c_specs_returns_records_without_errors() -> None:
    session = _FakeSession(
        {
            "items": [
                {
                    "shortname": "vc-jose-cose",
                    "title": "VC JOSE COSE",
                    "uri": "https://www.w3.org/TR/vc-jose-cose/",
                    "updated": "2026-07-08",
                }
            ]
        }
    )

    records, errors = fetch_recent_w3c_specs(session, since_days=30)

    assert len(records) == 1
    assert errors == []


class _FailingSession:
    def get(self, *_: object, **__: object) -> _FakeResponse:
        raise RuntimeError("network down")


def test_fetch_recent_w3c_specs_returns_error_on_fetch_failure() -> None:
    records, errors = fetch_recent_w3c_specs(_FailingSession(), since_days=30)

    assert records == []
    assert len(errors) == 1
    assert errors[0].startswith("w3c specifications fetch failed:")
