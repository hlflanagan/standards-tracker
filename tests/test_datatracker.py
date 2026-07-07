from ietf_watch.datatracker import extract_recent_draft_names, parse_draft_name


def test_parse_draft_name_extracts_base_and_version() -> None:
    versioned, base_name, version = parse_draft_name("draft-ietf-oauth-example-02")
    assert versioned == "draft-ietf-oauth-example-02"
    assert base_name == "draft-ietf-oauth-example"
    assert version == 2


def test_parse_draft_name_normalizes_case() -> None:
    versioned, base_name, version = parse_draft_name("DRAFT-IETF-OAUTH-EXAMPLE-09")
    assert versioned == "draft-ietf-oauth-example-09"
    assert base_name == "draft-ietf-oauth-example"
    assert version == 9


def test_extract_recent_draft_names_deduplicates_versions() -> None:
    html = """
    <table>
      <tr><td><a href="/doc/draft-ietf-oauth-example-00/">draft-ietf-oauth-example-00</a></td><td>OAuth Example</td></tr>
      <tr><td><a href="/doc/draft-ietf-oauth-example-00/">duplicate</a></td></tr>
      <tr><td><a href="/doc/draft-ietf-rats-attestation-01/">draft-ietf-rats-attestation-01</a></td><td>RATS Attestation</td></tr>
    </table>
    """
    drafts = extract_recent_draft_names(html)
    assert [draft.versioned_name for draft in drafts] == [
        "draft-ietf-oauth-example-00",
        "draft-ietf-rats-attestation-01",
    ]
    assert drafts[0].base_name == "draft-ietf-oauth-example"
    assert drafts[0].version == 0
