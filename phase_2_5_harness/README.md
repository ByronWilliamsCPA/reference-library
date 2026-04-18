# Phase 2.5 AI-Detector Evaluation Harness

Submits curated writing samples to multiple AI-content detectors, records
normalized scores and raw vendor responses, and produces an analysis-ready
Markdown report. Input is the `phase_2_5_samples.md` package committed to the
`reference-library` research branch.

## Status

Phase 0 scaffold. Module files beyond `detectors/__init__.py` land in later
phases per the task plan:

| Phase | Scope                                                     |
| ----- | --------------------------------------------------------- |
| 0     | Project layout, tooling, credentials template (this step) |
| 1     | `parse_samples.py` plus round-trip test                   |
| 2     | `config.py`, `schema.py`, `base.py`                       |
| 3     | Detector adapters (GPTZero, Sapling, Originality, ZeroGPT, local stubs) |
| 4     | `runner.py` CLI with resume, rate-limit, checkpointing    |
| 5     | `report.py` — matrix, FP analysis, efficacy, disagreement |
| 6     | Execute end-to-end                                        |

## Quick start

```bash
poetry install
cp .env.example .env   # fill in keys for detectors you want to exercise
poetry run parse-samples ../phase_2_5_samples.md
poetry run run-harness --detectors auto
poetry run build-report data/results/run_<timestamp>.json
```

## Conventions

- Python 3.11, full type annotations, Google-style docstrings.
- Ruff, Mypy (strict), Bandit, pytest configured in `pyproject.toml`.
- Credentials via `.env` only. `detect-secrets` baseline tracks accidental leaks.
- Results are streamed to disk per row so a crash mid-run does not lose work.
- Adapters strip long echoed text from `raw_response` before persistence to
  keep result JSON small and to avoid sample-content duplication.

## Guardrails

- Missing credentials silently skip a detector in `auto` mode (never fail the run).
- HTTP 429 backs off exponentially up to three retries, then records an error.
- Every sample submission is logged to the vendor; samples were PII-scrubbed in
  the upstream Phase 2.5 packaging step.
