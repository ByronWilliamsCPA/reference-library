# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-05-16

### Added

- CONTRIBUTING.md with docs-only contribution guidelines
- CHANGELOG.md (this file)
- .github/CODEOWNERS assigning @ByronWilliamsCPA as default owner
- AGENTS.md documenting the seven-agent writing quality pipeline
- GEMINI.md for Gemini CLI support
- docs/architecture/adr-001-writing-authority-hierarchy.md documenting the
  three-tier grammar authority system and three-source Oregon legal system
- docs/known-vulnerabilities.md (no known vulnerabilities at this time)

### Changed

- Bumped `actions/dependency-review-action` from v4.9.0 to v5.0.0. The new
  release upgrades the action runtime from Node 20 to Node 24, which requires
  Actions Runner v2.327.1 or newer. GitHub-hosted runners (`ubuntu-latest`)
  meet this requirement automatically; self-hosted runners may need to update.
- README.md version metadata refreshed to 1.1.0 / 2026-05-16 to reflect the
  CONTRIBUTING, CHANGELOG, AGENTS, GEMINI, ADR-001, and known-vulnerabilities
  additions made since the initial 1.0.0 release.
- REUSE.toml `SPDX-FileCopyrightText` year updated from 2025 to 2026 to match
  `LICENSES/MIT.txt`.
- `docs/known-vulnerabilities.md` reassessment policy tightened from 90 days to
  60 days to align with the global `~/.claude/CLAUDE.md` standard.
- `SECURITY.md` Secret Rotation Policy now states that `SONAR_TOKEN` and
  `QLTY_COVERAGE_TOKEN` are fine-grained service-issued credentials scoped to
  the minimum permissions required by each service (SonarCloud project-scoped
  tokens and Qlty repo-scoped tokens); classic GitHub PATs are not used as
  repository or organization secrets.
- `GEMINI.md` em-dash rule scope clarified to cover commit messages, code
  comments, and PR descriptions in addition to documentation.
- `.pre-commit-config.yaml` no-em-dash exclude block annotated to distinguish
  permanent exclusions (transcribed authority text) from scoped cleanup paths
  with a 2026-12-31 target (PC-014).
- Project `CLAUDE.md` cross-references corrected from `~/.claude/.claude/rules/`
  to `~/.claude/rules/` (three "See Also" links and one Model Selection link).
- `CLAUDE.md` and `README.md` repository structure trees now include the
  `docs/` directory for ADR and known-vulnerabilities findability.
- `.claude/compliance-overrides.md` expanded with documented exceptions for
  CI-001, CI-035, CI-042, CI-046, OSSF-011, SCORECARD:publish_results,
  SCORECARD:Fuzzing, FOUND-024 (em-dash tracking), and FOUND-025 (REUSE 3.0
  in lieu of root LICENSE).
- `.gitignore` extended with `.ruff_cache/` and `docs/superpowers/`.

### Fixed

- Two em-dashes in `samples/README.md` (lines 95-96) surfaced by the narrower
  `samples/before/|samples/after/` exclude pattern in `.pre-commit-config.yaml`.
  The previous `samples/` exclude was hiding repo-authored content that the
  global no-em-dash rule should cover.

## [1.0.0] - 2026-03-15

### Added

- Initial release of the reference library
- Oregon legal style reference files extracted from three authoritative sources:
  Appellate Courts Style Manual (2002), LC Drafting Manual, and LC Form and Style Manual
- Writing style reference: style profile, AI pattern detection, tone and voice palettes,
  structural formatting rules, plain language guide, logical fallacies guide,
  and transition words reference
- Grammar-style three-tier authority system with Elements of Style (Tier 1),
  Chicago Manual of Style 17th ed. (Tier 2), and PromptCraft Pro overrides (Tier 3)
- Seven Claude agent definitions installed globally via `scripts/setup.sh`:
  style-analyzer, document-drafter, tone-rewriter, grammar-composition-editor,
  document-validator, writing-style-editor, audience-reaction-analyzer
- PDF extraction utility script (`scripts/extract_legal_pdfs.py`)
- Cross-reference files documenting divergences between the three Oregon legal sources
  and 21 EoS/CMS/PromptCraft Pro conflicts

[Unreleased]: https://github.com/ByronWilliamsCPA/reference-library/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/ByronWilliamsCPA/reference-library/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ByronWilliamsCPA/reference-library/releases/tag/v1.0.0
