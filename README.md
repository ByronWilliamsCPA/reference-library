# Reference Library

> **Purpose**: Base reference files and agents — general, reusable across personal, CPA, and investment projects
> **Version**: 1.0.0
> **Last Updated**: 2026-02-20

A centralized reference library for authoritative style, drafting, and writing standards. This repository contains no project-specific content. Individual project repositories extend what they need.

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

Quantified writing style profile and AI pattern detection reference. Not project-specific — applies to any professional document context.

- [`writing-style/style-profile.md`](writing-style/style-profile.md) — sentence metrics, rhythm targets, stylometry
- [`writing-style/ai-detection.md`](writing-style/ai-detection.md) — blacklisted terms, structural tells, rewrite examples

### `.claude/agents/` — Base Agent Definitions

General-purpose Claude agents with no project-specific content baked in:

- `writing-style-editor` — voice alignment, AI pattern detection, grammar review
- `document-validator` — factual verification, assumption audit, bias detection

---

## How to Use Across Projects

### Reference files

Point agents or prompts directly to files in this repo:

```text
See /home/byron/dev/reference-library/legal-style/QUICK-START.md for citation rules.
See /home/byron/dev/reference-library/writing-style/style-profile.md for style targets.
```

### Extending agents

Copy a base agent into your project's `.claude/agents/` and add project-specific content:

```text
# In project/.claude/agents/writing-style-editor.md

# Inherits base behavior from reference-library
# Project-specific additions below:

## Domain Terminology
[project-specific terms and standards]
```

---

## Source PDFs

The three Oregon legal PDFs are stored locally in `legal-style/source-pdfs/` but excluded from git (see `.gitignore`). To re-download:

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
├── .claude/
│   └── agents/
│       ├── writing-style-editor.md
│       └── document-validator.md
├── legal-style/
│   ├── README.md
│   ├── QUICK-START.md
│   ├── appellate-style-manual/
│   ├── lc-drafting-manual/
│   ├── lc-form-style-manual/
│   └── cross-reference.md
├── writing-style/
│   ├── README.md
│   ├── style-profile.md
│   └── ai-detection.md
└── scripts/
    └── extract_legal_pdfs.py
```
