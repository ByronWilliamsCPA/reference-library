# Reference Library

> **Purpose**: Base reference files and agents — general, reusable across personal, CPA, and investment
> projects
> **Version**: 1.0.0
> **Last Updated**: 2026-03-15

A centralized reference library for authoritative style, drafting, and writing standards. This repository
contains no project-specific content. Individual project repositories extend what they need.

---

## What's Here

### `legal-style/` — Oregon Legal Style and Drafting

Reference files extracted from three authoritative Oregon sources:

| Source | Governs |
| --- | --- |
| Oregon Appellate Courts Style Manual (2002) | Court filings, briefs, opinions |
| Oregon Legislative Counsel Drafting Manual | Bill drafting, statutory language |
| Oregon LC Form and Style Manual | ORS citations, bill formatting, grammar |

Start with [`legal-style/QUICK-START.md`](legal-style/QUICK-START.md) for the most common daily lookups.

### `writing-style/` — Writing Style Reference

Quantified writing style profile and AI pattern detection reference. Not project-specific — applies to any
professional document context.

- [`writing-style/style-profile.md`](writing-style/style-profile.md) — sentence metrics, rhythm targets, stylometry
- [`writing-style/ai-detection.md`](writing-style/ai-detection.md) — blacklisted terms, structural tells,
  rewrite examples

### `agents/` — Base Agent Definitions

General-purpose Claude agents with no project-specific content baked in. Install them globally
with `scripts/setup.sh` — no per-project setup required.

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
├── agents/                        # Agent templates — installed globally by setup.sh
│   ├── style-analyzer.md
│   ├── document-drafter.md
│   ├── tone-rewriter.md
│   ├── grammar-composition-editor.md
│   ├── document-validator.md
│   ├── writing-style-editor.md
│   └── audience-reaction-analyzer.md
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
│   └── grammar-style/
└── scripts/
    ├── setup.sh                   # Install agents to ~/.claude/agents/
    └── extract_legal_pdfs.py
```
