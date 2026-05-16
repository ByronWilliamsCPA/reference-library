# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/ByronWilliamsCPA/reference-library/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ByronWilliamsCPA/reference-library/releases/tag/v1.0.0
