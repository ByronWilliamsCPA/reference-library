# Code Quality, Maintainability, and Legacy Patterns Audit: reference-library

Audit date: 2026-05-29 (UTC). HEAD: 60e1cda. Scope: the 4-file Python surface in `scripts/` plus `tests/test_profile_resolver.py` (1434 LOC total). Read-only. Tools available: ruff, pytest, mypy. Missing: basedpyright (the configured strict checker), pytest-cov.

## Summary

The in-scope code is clean: `ruff check scripts/ tests/` passes with zero findings, 44 tests pass with 77 assertions, no skips or xfails, no `TODO`/`FIXME`/`HACK`/`XXX`, no broad `except`, modern typing throughout (PEP 585/604, no `typing.List`, no `os.path`, no `%`-formatting). The debt is concentrated where the config looks away: two scripts are excluded from both ruff and coverage and carry 22 lint errors, the core resolver leans on `dict[str, Any]` so its "strict" type gate proves little, and two of the three runtime-relevant scripts have zero test coverage.

## Findings

### CQ-01: Two scripts excluded from ruff and coverage hide 22 lint errors

- Severity: Medium
- Effort: S (auto-fixable plus manual line wraps; under a day)
- Affected files: `scripts/extract_legal_pdfs.py`, `scripts/generate_before_samples.py`, `pyproject.toml:44-47,21-25`
- Evidence: `pyproject.toml` `extend-exclude` removes both files from ruff and `coverage omit` drops them from coverage. Running ruff directly on them: `ruff check --no-cache scripts/extract_legal_pdfs.py scripts/generate_before_samples.py` reports `Found 22 errors` (21 E501 line-too-long, 1 UP017 `datetime.timezone.utc` where `datetime.UTC` is available, `generate_before_samples.py:234`). One is auto-fixable.
- Recommendation: Run `ruff check --fix` on the two files, wrap the long lines, then remove the `extend-exclude` so the lint gate covers all of `scripts/`. The exclusion converts a one-hour cleanup into permanent hidden debt.

### CQ-02: `dict[str, Any]` pervades the resolver, so the "strict" type gate proves little

- Severity: Medium
- Effort: M (introduce TypedDicts/dataclasses for the profile shape; a few days)
- Affected files: `scripts/profile_resolver.py`
- Evidence: `basedpyright` is configured `typeCheckingMode = "standard"` (not strict, despite the pyproject comment calling it the strict entry point) scoped to `profile_resolver.py` and `tests/` (`pyproject.toml:56-60`). The file imports `Any` (`profile_resolver.py:47`) and 28 signatures/locals are typed `dict[str, Any]`, `list[Any]`, or `Any` (for example `_merge`, `_merge_lists`, `_resolve_overlays`, `_format_text` at lines 145, 133, 211, 383). Every profile field flows through `Any`, so the checker cannot catch a misspelled key or wrong value type, which is the exact class of bug a config resolver risks.
- Recommendation: Model the profile and config sections as `TypedDict`s or dataclasses and set `typeCheckingMode = "strict"`, so the resolver's merge logic is actually type-checked rather than nominally so.

### CQ-03: Coverage measures one of three runtime scripts; two are untested

- Severity: Medium
- Effort: M (add tests for extraction and sample-generation paths; a few days)
- Affected files: `scripts/extract_legal_pdfs.py`, `scripts/generate_before_samples.py`, `tests/`
- Evidence: `tests/` contains one file, `test_profile_resolver.py`. `pyproject.toml:24-27` omits the other two scripts from coverage entirely, so the reported coverage figure describes only `profile_resolver.py`. The exact repo-wide coverage number could not be produced in this environment (`pytest-cov` is not installed: `pytest --cov` returns "unrecognized arguments"). Effective test coverage of `extract_legal_pdfs.py` and `generate_before_samples.py` is zero.
- Recommendation: Add at least smoke/parse tests for the two untested scripts (PDF-yield threshold logic, `.env` key parsing, request payload assembly) and remove them from `coverage omit`, or state explicitly in the report config that they are intentionally uncovered operational utilities.

### CQ-04: `tomli` fallback import is untyped and unresolved by the type checker

- Severity: Low
- Effort: S
- Affected files: `scripts/profile_resolver.py:51-53`
- Evidence: `mypy scripts/profile_resolver.py` reports one error: `Cannot find implementation or library stub for module named "tomli" [import-not-found]` at line 53, and notes the existing `# type: ignore[no-redef]` does not cover that code. The fallback exists for Python <3.11, but `requires-python` is `>=3.11`, so the branch is unreachable on every supported interpreter.
- Recommendation: Given the 3.11 floor, `tomllib` is always present; drop the `tomli` fallback (and its `# type: ignore`), or guard the import so the type checker resolves cleanly.

## Clean areas

- In-scope lint: `ruff check scripts/ tests/` reports "All checks passed!" against the selected rule set (E, F, W, I, B, C4, SIM, UP).
- Tests: 44 passed in 0.14s, 77 `assert` statements, zero skips, zero xfails, no assertion-free tests observed.
- Debt markers: zero `TODO`/`FIXME`/`HACK`/`XXX` across `scripts/` and `tests/`.
- Legacy idioms: none. No `typing.List/Dict/Optional` (PEP 585/604 generics used), no `os.path` (pathlib throughout), no `%`-formatting or `.format()` for interpolation, no bare or broad `except`.
- Complexity: no function in the in-scope set trips an obvious complexity ceiling; the resolver is decomposed into small single-purpose helpers (`_merge`, `_resolve_overlays`, `_format_text`).
