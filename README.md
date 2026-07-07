# standards-tracker

A small Python tool that watches recent IETF Internet-Drafts for digital identity, authorization, credentials, privacy-preserving identity, trust infrastructure, and AI governance relevance.

## Project layout

- `src/ietf_watch/` - fetching, classification, persistence, and reporting
- `tests/` - focused unit tests
- `config/default.yaml` - relevance rules and reporting settings
- `reports/` - generated Markdown and CSV reports
- `.data/ietf_watch.db` - local SQLite review state created at runtime

## Local setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]
```

Python 3.11+ is required.

## Local run instructions

Run tests:

```bash
pytest
```

Run the monitor with the default deterministic classifier:

```bash
python -m ietf_watch.cli --config config/default.yaml --since-days 7
```

Useful options:

- `--use-llm` - enable optional OpenAI-backed classification refinement
- `--since-days` - recent draft window to inspect
- `--min-relevance` - override the configured reporting threshold
- `--dry-run` - write reports without updating the SQLite review state
- `--config` - choose a different YAML config file

Generated reports are written as:

- `reports/YYYY-MM-DD-ietf-identity-ai-watch.md`
- `reports/YYYY-MM-DD-ietf-identity-ai-watch.csv`

## GitHub Actions setup

The workflow in `.github/workflows/daily-ietf-watch.yml`:

- runs every day at `14:00 UTC`
- installs dependencies
- runs tests
- runs the monitor
- commits updated reports back to the repository when the `reports/` directory changes

You can also run it manually with **Actions -> Daily IETF Watch -> Run workflow**.

## OPENAI_API_KEY GitHub secret

If you want optional LLM refinement in your own runs, add `OPENAI_API_KEY` as a repository secret:

1. Open **Settings** -> **Secrets and variables** -> **Actions**
2. Create a new repository secret named `OPENAI_API_KEY`
3. Provide the key value
4. Run locally or update the workflow command to include `--use-llm`

The tool still works without the key and defaults to deterministic classification.

## Tuning relevance rules

Edit `config/default.yaml` to adjust:

- global relevance keywords
- working-group boost values
- per-category keyword definitions
- minimum reporting threshold
- report title

The classifier intentionally avoids treating every AI-related draft as high relevance; AI drafts focused only on networking or telemetry should fall to weaker buckets unless they also involve identity, authority, credentials, provenance, governance, trust, or privacy.

## Known limitations

- The Datatracker HTML is parsed heuristically, so layout changes may require parser updates.
- Metadata JSON fields vary across drafts, so group and update-date extraction is best effort.
- Optional LLM classification uses the OpenAI Chat Completions API and falls back to deterministic scoring on any failure.
- Previously seen versions are skipped once stored in SQLite; deleting `.data/ietf_watch.db` resets local review state.
