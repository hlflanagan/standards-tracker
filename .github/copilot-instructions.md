# Copilot instructions for this repository

This repository monitors the IETF Datatracker for Internet-Drafts relevant to digital identity, authorization, credentials, privacy-preserving identity, trust infrastructure, AI agents, and AI governance.

## Project principles

- Keep the tool small and maintainable.
- Prefer deterministic behavior over opaque automation.
- The LLM classifier is optional and must never be required for the tool to run.
- Do not over-classify drafts as relevant.
- Treat generic AI/network-optimization drafts as low relevance unless they address identity, authorization, credentials, trust, provenance, governance, privacy, or agent authority.
- Preserve human review. The tool produces a triage report; it does not decide final relevance.

## Expected commands

Run tests:

```bash
pytest
