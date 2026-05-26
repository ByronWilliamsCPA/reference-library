# Reference Library

> **Purpose**: Base reference files and agents, general, reusable across personal, CPA, and investment
> projects
> **Version**: 1.1.0
> **Last Updated**: 2026-05-16

A centralized reference library for authoritative style, drafting, and writing standards. This repository
contains no project-specific content. Individual project repositories extend what they need.

**API reference**: Not applicable. This is a documentation-only repository with no programmatic interface
or callable library.

---

## What's Here

### `legal-style/`: Oregon Legal Style and Drafting

Reference files extracted from three authoritative Oregon sources:

| Source | Governs |
| --- | --- |
| Oregon Appellate Courts Style Manual (2002) | Court filings, briefs, opinions |
| Oregon Legislative Counsel Drafting Manual | Bill drafting, statutory language |
| Oregon LC Form and Style Manual | ORS citations, bill formatting, grammar |

Start with [`legal-style/QUICK-START.md`](legal-style/QUICK-START.md) for the most common daily lookups.

### `writing-style/`: Writing Style Reference

Quantified writing style profile and AI pattern detection reference. Not project-specific; applies to any
professional document context.

- [`writing-style/style-profile.md`](writing-style/style-profile.md): sentence metrics, rhythm targets, stylometry (shipped default; per-person calibration lives locally under `config/profiles/`)
- [`writing-style/ai-detection.md`](writing-style/ai-detection.md): blacklisted terms, structural tells,
  rewrite examples
- [`writing-style/punctuation-preferences.md`](writing-style/punctuation-preferences.md): catalog of person-configurable Tier 3 overrides (em-dash, etc.)

### `config/`: Person × Style Profiles

A V2 layer that lets agents be parameterized by **person** (the maintainer, a colleague, you)
and **style context** (work email, client memo, statutory drafting, court brief, etc.).

- [`config/profiles.example.toml`](config/profiles.example.toml): shipped default profile plus
  six starter styles (general, work-email, internal-memo, client-memo, statutory-drafting,
  court-brief). Committed to the repo.
- `config/profiles.toml`: your local active config. Gitignored. Created from the example by
  `scripts/setup.sh` on first run; edit it to add people, styles, or cross-scoped overrides.
- `config/profiles/{person}/{style}.md`: per-person calibration data written by the
  `style-analyzer` agent. Gitignored.

The resolver script (`scripts/profile_resolver.py`) merges base defaults → person → style →
cross-scoped overrides → call-time arguments and emits the active profile as JSON. Agents
call it at invocation time. See [`CLAUDE.md`](CLAUDE.md) for resolution rules.

### `agents/`: Base Agent Definitions

General-purpose Claude agents with no project-specific content baked in. Install them globally
with `scripts/setup.sh`; no per-project setup required.

| Agent | Pipeline Position | Purpose |
| --- | --- | --- |
| `style-analyzer` | Pre-pipeline (calibration) | Analyze writing samples, compute stylometry, calibrate voice profile |
| `document-drafter` | Pre-pipeline (generation) | Voice-calibrated first drafts from outlines, bullets, or prompts |
| `tone-rewriter` | Pre-pipeline (generation) | Transform register for a different audience, preserve factual content |
| `grammar-composition-editor` | Stage 1 (editing) | Grammar, composition, plain language, AI-mechanical patterns |
| `document-validator` | Stage 2 (editing) | Factual accuracy, assumptions, hallucinations, bias, reasoning errors |
| `writing-style-editor` | Stage 3 (editing) | Voice alignment, AI pattern detection, stylometry |
| `audience-reaction-analyzer` | Post-pipeline (analysis) | Predict audience comprehension, persuasion, emotional response |

New users should run the `style-analyzer` agent first to calibrate the style profile before
using the generators or editing pipeline.

---

## How to Use Across Projects

### Install the agents (one-time setup)

```bash
git clone https://github.com/ByronWilliamsCPA/reference-library.git
cd reference-library
bash scripts/setup.sh
```

This installs all seven agents to `~/.claude/agents/`, making them available in every Claude
Code project without touching any project files. If you move or reclone the repository,
re-run `setup.sh` to update the installed paths.

### Reference files in prompts or agents

After installation, point to library files using the path where you cloned:

```text
See /path/to/reference-library/legal-style/QUICK-START.md for citation rules.
See /path/to/reference-library/writing-style/style-profile.md for style targets.
```

### Extending agents for a specific project

To add project-specific rules on top of a base agent, create a `.claude/agents/` file in your
project with the additional rules. The base agent's globally installed version handles the
standard pipeline; your project file adds the domain-specific layer.

```text
# In project/.claude/agents/writing-style-editor-legal.md
# Extends the base writing-style-editor with Oregon legal style rules.

## Oregon Legal Style Additions
[project-specific legal style rules]
```

---

## Source PDFs

The three Oregon legal PDFs are stored locally in `legal-style/source-pdfs/` but excluded from git
(see `.gitignore`). To re-download:

```bash
cd legal-style/source-pdfs
curl -O "https://www.courts.oregon.gov/publications/Documents/UpdatedStyleManual2002.pdf"
curl -O "https://www.oregonlegislature.gov/lc/PDFs/draftingmanual.pdf"
curl -O "https://www.oregonlegislature.gov/lc/PDFs/form-stylemanual.pdf"
```

To re-extract text from the PDFs:

```bash
python scripts/extract_legal_pdfs.py
```

---

## Structure

```text
reference-library/
├── README.md
├── agents/                        # Agent templates; installed globally by setup.sh
│   ├── style-analyzer.md
│   ├── document-drafter.md
│   ├── tone-rewriter.md
│   ├── grammar-composition-editor.md
│   ├── document-validator.md
│   ├── writing-style-editor.md
│   └── audience-reaction-analyzer.md
├── config/                          # V2 person × style profiles
│   ├── profiles.example.toml        # Shipped default (committed)
│   ├── profiles.toml                # Active local config (gitignored)
│   └── profiles/                    # Per-person calibration data (gitignored)
├── legal-style/
│   ├── README.md
│   ├── QUICK-START.md
│   ├── cross-reference.md
│   ├── appellate-style-manual/
│   ├── lc-drafting-manual/
│   └── lc-form-style-manual/
├── writing-style/
│   ├── README.md
│   ├── style-profile.md
│   ├── ai-detection.md
│   ├── tone-voice.md
│   ├── structural-formatting.md
│   ├── plain-language-guide.md
│   ├── logical-fallacies-guide.md
│   ├── transition-words-reference.md
│   ├── punctuation-preferences.md   # Tier 3 override catalog
│   └── grammar-style/
├── samples/
│   ├── before/                   # AI-generated before-state samples for pipeline testing
│   └── after/                    # Post-pipeline output: per-stage transcripts plus recaps
├── docs/
│   ├── architecture/             # ADRs
│   ├── compliance-reports/       # Generated audit reports (git-ignored)
│   ├── superpowers/              # Local working directory (git-ignored)
│   ├── known-vulnerabilities.md  # CVE log and accepted Scorecard exceptions
│   └── reusable-workflow-jobs.yaml
├── LICENSES/                     # REUSE 3.0 licenses (FOUND-025)
└── scripts/
    ├── setup.sh                   # Install agents; bootstrap config/profiles.toml
    ├── profile_resolver.py        # Resolve a person × style profile (V2)
    ├── extract_legal_pdfs.py
    └── generate_before_samples.py
```
