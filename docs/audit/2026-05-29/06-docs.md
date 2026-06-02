# Documentation and Developer Experience Audit: reference-library

Audit date: 2026-05-29 (UTC). HEAD: 60e1cda. Scope: README accuracy vs actual setup, broken links, stale content, onboarding friction, ADR coverage. Read-only. ~23,000 lines of markdown across 86 files.

## Summary

Documentation quality is high: every internal markdown link resolves, the README setup steps match `setup.sh` and the real paths, and the routing files in `legal-style/` and `writing-style/grammar-style/` point to files that exist. The gaps are governance-level: only one ADR exists despite several architecture decisions visible in the code, the CHANGELOG `[Unreleased]` section is empty while post-1.1.0 commits exist, and a contributor must reconcile four assistant-instruction files (tracked in detail as ARCH-01).

## Findings

### DOC-01: Only one ADR exists; major decisions are undocumented

- Severity: Low
- Effort: M (write 3 to 4 short ADRs; a few days)
- Affected files: `docs/architecture/` (contains only `adr-001-writing-authority-hierarchy.md`)
- Evidence: The repo has exactly one ADR. Decisions plainly present in the code and config have none: the V2 person x style profile resolver and its merge/override semantics, the adoption of org reusable workflows pinned to `main`, and the 11-workflow security/CI design. CLAUDE.md describes these as settled architecture, but there is no record of why each was chosen, so future maintainers cannot recover the rationale.
- Recommendation: Add short ADRs for the V2 profile architecture and the CI/reusable-workflow strategy; one page each is enough to capture the decision and alternatives.

### DOC-02: CHANGELOG `[Unreleased]` is empty despite post-1.1.0 changes

- Severity: Low
- Effort: S
- Affected files: `CHANGELOG.md:8-10`
- Evidence: `CHANGELOG.md` shows `## [Unreleased]` immediately followed by `## [1.1.0] - 2026-05-16` with no entries between them, yet files dated 2026-05-29 have changed since 1.1.0 (CLAUDE.md, AGENTS.md, README.md per the working tree timestamps and the current audit branch). Changes are landing without changelog entries.
- Recommendation: Record post-1.1.0 changes under `[Unreleased]` as they land, or enforce it (commitizen is already a pre-commit hook and can drive changelog generation).

## Clean areas

- Internal links: zero broken. Every relative markdown link was resolved against its own file's directory; all targets exist (the `legal-style/` and `writing-style/grammar-style/` routing maps included).
- README setup accuracy: the documented flow (`bash scripts/setup.sh`, the example-to-active config copy, the curl PDF downloads, `python scripts/extract_legal_pdfs.py`) matches `setup.sh`, which installs all 7 agents with the `{{LIBRARY_PATH}}` substitution and bootstraps `config/profiles.toml` from the example with `chmod 600`. Referenced paths exist.
- Machine-local references: markdown link targets pointing at `~/...` home-dir paths: zero (the `~/.claude/rules/*` mentions are prose pointers to global rules, not broken links).
- CONTRIBUTING vs tooling: CONTRIBUTING.md describes the conventional-commit and pre-commit expectations that the actual hooks enforce.
- Instruction-file count: a contributor must read CLAUDE.md, AGENTS.md, GEMINI.md, and `.github/copilot-instructions.md`. The onboarding cost of reconciling four overlapping files is real but is owned as an architecture finding (ARCH-01) to avoid duplication.
