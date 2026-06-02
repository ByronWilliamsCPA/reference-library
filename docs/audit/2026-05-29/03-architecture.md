# Architecture and Structure Audit: reference-library

Audit date: 2026-05-29 (UTC). HEAD: 60e1cda. Scope: V2 person x style profile system (`scripts/profile_resolver.py`), the 7-agent pipeline, the grammar/legal authority hierarchies, and drift between the code and the repo's stated conventions. Read-only.

## Summary

The V2 architecture documented in CLAUDE.md is implemented in the resolver, and the agents reference profile fields consistently. The structural weakness is documentation governance, not code: four separate AI-assistant instruction files restate the same architecture and must be hand-synced, and one house rule (`no-em-dash`) is documented as a per-profile Tier-3 override while being hardcoded into repo infrastructure, contradicting the design's own "never hardcode Tier 3" rule.

## Findings

### ARCH-01: Four overlapping assistant-instruction files duplicate the architecture and will drift

- Severity: High
- Effort: M (designate one source of truth and reduce the others to pointers; a few days)
- Affected files: `CLAUDE.md` (323 lines), `AGENTS.md` (121), `GEMINI.md` (33), `.github/copilot-instructions.md` (22)
- Evidence: All four describe the same agent pipeline and conventions. `AGENTS.md` headings (`Invocation: Person x Style`, `Agent Overview`, `Editing Pipeline: Stages 1 to 3`, `Installation`) restate CLAUDE.md sections verbatim in places. The seven-agent pipeline, the SHA-pin rule, and the no-em-dash rule each appear in three or four of these files. There is no single source of truth, so any architecture change requires editing up to four files in lockstep. The churn data already shows CLAUDE.md edited 9 times and these files moving independently.
- Recommendation: Make CLAUDE.md canonical and reduce AGENTS.md, GEMINI.md, and copilot-instructions.md to short tool-specific pointers ("see CLAUDE.md for architecture; this file adds X"), so the architecture is stated once.

### ARCH-02: `no-em-dash` is documented as a per-profile Tier-3 override but hardcoded repo-wide

- Severity: Low
- Effort: S
- Affected files: `CLAUDE.md` (Grammar-Style Three-Tier section), `.pre-commit-config.yaml:104-106`, `.github/copilot-instructions.md:16`, `AGENTS.md`, `GEMINI.md`
- Evidence: CLAUDE.md states Tier 3 is "profile-driven," that "other profiles may omit it," and "Never hardcode a Tier 3 rule into agents or reference content." The resolver honors this: `tier_3_overrides` is read from config (`profile_resolver.py:314,330`; `config/profiles.example.toml:50`) and the agents apply it dynamically (`agents/document-drafter.md:158,207`). But the same rule is hardcoded as a repo-wide gate: a `no-em-dash` local pre-commit hook (`.pre-commit-config.yaml:104-106`), a flat assertion in `copilot-instructions.md:16` ("No em-dashes in any output"), and equivalents in AGENTS.md/GEMINI.md. A profile that omits `no-em-dash` (which the design explicitly permits) could not produce em-dash content without failing CI.
- Recommendation: Decide whether no-em-dash is a universal house rule or a per-profile override and align the docs with the enforcement; if it is universal, stop framing it as a configurable Tier-3 example.

### ARCH-03: Model Selection table references a superseded model generation

- Severity: Low
- Effort: S
- Affected files: `CLAUDE.md:151-153`
- Evidence: The Model Selection table names "Opus 4.7", "Sonnet 4.6", "Haiku 4.5" as current choices. Opus 4.8 is the current top model, so the table's top tier is one generation stale. Minor, but it is normative guidance the repo tells contributors to follow.
- Recommendation: Update the table to the current model generation, or replace specific version numbers with role labels ("most capable", "balanced", "fast") so the table does not require a commit each model release.

## Clean areas

- V2 resolution is implemented as documented: base -> person -> style -> overrides with last-writer-wins scalars and concat-and-dedupe lists (`profile_resolver.py` `_merge`, `_merge_lists`, `_resolve_overlays`), and `tier_3_overrides` is person-scoped only (`profile_resolver.py:22`). Domain gating with a dedicated exit code is present.
- Agent consistency: all 7 agent files carry the `{{LIBRARY_PATH}}` placeholder substituted by `setup.sh`, and all reference `tier_3_overrides` and the profile flags the same way; none hardcode a Tier-3 rule into the agent body.
- Module structure in `scripts/`: the resolver is decomposed into small single-responsibility helpers; no circular imports (the scripts do not import each other); each script is a standalone entry point.
- Documented directory tree in CLAUDE.md matches the actual tree (`git ls-files` confirms the `agents/`, `scripts/`, `config/`, `legal-style/`, `writing-style/` contents as described, including the gitignored paths it annotates as local-only).
