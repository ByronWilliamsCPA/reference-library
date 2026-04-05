# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

A centralized reference library: authoritative style, drafting, and writing standards shared across
personal, CPA, and investment projects. No project-specific content lives here. Individual project
repositories extend what they need.

## Repository Structure

```text
reference-library/
├── legal-style/           # Oregon legal style and drafting rules
│   ├── QUICK-START.md     # 80% of daily lookups — start here
│   ├── cross-reference.md # Where the three sources diverge (read this before drafting)
│   ├── appellate-style-manual/   # Oregon Appellate Courts Style Manual (2002)
│   ├── lc-drafting-manual/       # Oregon Legislative Counsel Drafting Manual
│   └── lc-form-style-manual/     # Oregon LC Form and Style Manual
├── writing-style/
│   ├── style-profile.md          # Quantified stylometry targets and voice characteristics
│   ├── ai-detection.md           # Blacklisted AI terms and rewrite examples
│   ├── tone-voice.md             # 8 style palettes with triggers and signals
│   ├── structural-formatting.md  # Markdown rules, heading hierarchy, WCAG notes
│   ├── plain-language-guide.md   # Federal plain language principles, readability, inclusive language
│   ├── logical-fallacies-guide.md    # Common reasoning errors in professional documents
│   ├── transition-words-reference.md # Transition categories, usage rules, AI overuse detection
│   └── grammar-style/            # EoS + CMS grammar reference (14 files)
│       ├── QUICK-START.md        # 80% of grammar questions — start here
│       ├── cross-reference.md    # 21 EoS/CMS/PCP divergences with resolution
│       ├── index.md              # Concept-to-file routing map
│       ├── elements-of-style/    # EoS base rules (Tier 1, drafting baseline)
│       └── chicago-manual/       # CMS rules (Tier 2, editing authority)
├── agents/
│   ├── grammar-composition-editor.md  # Stage 1: Grammar, composition, plain language
│   ├── document-validator.md          # Stage 2: Factual accuracy, assumptions, bias
│   ├── writing-style-editor.md        # Stage 3: Voice, AI detection, stylometry
│   ├── style-analyzer.md             # Pre-pipeline: Analyze samples, calibrate profile
│   ├── document-drafter.md           # Pre-pipeline: Voice-calibrated first-draft generation
│   ├── audience-reaction-analyzer.md # Post-pipeline: Predict audience comprehension and response
│   └── tone-rewriter.md             # Pre-pipeline: Transform register for different audiences
└── scripts/
    └── extract_legal_pdfs.py     # PDF → raw text extraction (pdftotext → pymupdf fallback)
```

## Architecture: Grammar-Style Three-Tier System

The `writing-style/grammar-style/` content uses a three-tier authority hierarchy. The tier
governs based on which operation you are performing:

| Operation | Authority |
| --- | --- |
| Drafting (writing first draft) | Elements of Style (Tier 1 baseline) |
| Editing (reviewing any draft) | Chicago Manual of Style, 17th ed. (Tier 2; overrides EoS) |
| User-confirmed preference deviations | PromptCraft Pro defaults (Tier 3; overrides CMS) |

**One confirmed Tier 3 override**: no em-dashes. CMS §6.85–6.87 permits them; the user
follows the PromptCraft Pro default banning them. Use commas, colons, semicolons, or
parentheses instead. See `writing-style/grammar-style/cross-reference.md` #21.

**Agent file-loading strategy**: Load `grammar-style/QUICK-START.md` first. For conflicts,
load `cross-reference.md`. For deeper rules, load only the specific source file. Never
load all grammar-style files at once (full set exceeds 12,000 tokens).

---

## Architecture: Three-Source Oregon Legal System

The `legal-style/` content comes from three distinct sources with **different and sometimes
conflicting rules**. The source governs based on what you are *writing*, not what you are reading:

| Document type | Governing source |
| --- | --- |
| Court opinions and briefs | Appellate Courts Style Manual |
| Bills and session law | LC Form & Style Manual |
| Statutory language (meaning, construction) | LC Drafting Manual |

**Critical divergences** (see `legal-style/cross-reference.md` for the full list):

- **Serial comma**: LC omits it (`A, B and C`); Appellate uses it (`A, B, and C`)
- **Quotation mark punctuation**: LC puts punctuation outside; Appellate puts it inside
- **ORS ranges**: LC always uses "to"; Appellate uses " - " (hyphen with spaces) in citation form
- **Ellipsis**: Appellate uses `* * *`; LC uses `...`
- **Tense**: LC uses present tense throughout; Appellate uses past for facts, present for legal rules

## Agent Architecture: Writing Quality Pipeline

The seven agents in `agents/` include pre-pipeline generators, a calibration agent,
a sequential three-stage editing pipeline, and a post-pipeline analyzer. No project-specific
content lives in any agent.

### Style Analyzer (Pre-Pipeline Calibration)

| Agent | Scope | Analogy |
| --- | --- | --- |
| `style-analyzer` | Collect writing samples, compute stylometry, characterize voice, update profile | Tune the instrument |

Run the style analyzer **once** when a new user adopts the library, or when the user's
writing style has evolved. It analyzes the user's real writing samples and generates
updated targets for `style-profile.md` plus adjustment notes for the three pipeline agents.
This replaces the repository author's default style profile with one calibrated to the
new user's voice.

**Workflow**: Provide 3–5 writing samples (2,000+ words total) → analyzer computes
stylometry and characterizes voice → review and approve recommendations → updated
profile drives all future pipeline runs.

### Pre-Pipeline Generators

These agents produce text that feeds into the editing pipeline. Both apply `style-profile.md`
targets and `ai-detection.md` constraints during generation to minimize downstream corrections.

| Agent | Scope | Analogy |
| --- | --- | --- |
| `document-drafter` | Generate first drafts from outlines, bullet points, or contextual prompts, calibrated to the author's voice | Write the first draft |
| `tone-rewriter` | Transform a document's register for a different audience while preserving all factual content | Same message, new audience |

**Document drafter** accepts outlines, bullet points, prior documents, contextual prompts,
emails with reply direction, or topic-plus-audience descriptions. It produces a complete first
draft that already sounds like the author, reducing the remediation cycles Stage 3 needs to run.

**Tone rewriter** takes a finished document and transforms it for a different audience or
formality level. A formal tax analysis becomes a client-friendly summary. An internal memo
becomes an executive brief. Factual content must survive the transformation; Stage 2
re-verifies semantic preservation after every rewrite.

Both agents tag their output with `ai_generated: true` metadata, which signals Stage 3 to
apply heightened AI pattern scrutiny.

**Generator flow**: Input → Generator Agent → Stage 1 → Stage 2 → Stage 3 → Submission

### Editing Pipeline (Stages 1–3)

Run the three editing agents in order: Stage 1 → Stage 2 → Stage 3.

| Stage | Agent | Scope | Analogy |
| --- | --- | --- | --- |
| 1 | `grammar-composition-editor` | Grammar, composition, plain language, AI-mechanical patterns | Fix the bones |
| 2 | `document-validator` | Factual accuracy, assumptions, bias, reasoning errors | Verify the truth |
| 3 | `writing-style-editor` | Voice, persona fidelity, AI pattern detection, stylometry | Tune the voice |

**Pipeline flow**: Draft → Stage 1 (grammar) → Stage 2 (facts) → Stage 3 (voice) → Submission

**Why this order**: Grammar fixes are mechanical and objective. Factual errors are highest-stakes
for credibility. Style and persona are final polish on clean, verified text.

**Remediation**: If Stage 3 rewrites text for voice, those sections flow back through Stage 1
then Stage 2 to verify grammar and semantic preservation. Max 3 remediation cycles before
human review.

### Audience Reaction Analyzer (Post-Pipeline)

| Agent | Scope | Analogy |
| --- | --- | --- |
| `audience-reaction-analyzer` | Predict audience comprehension, persuasion effectiveness, emotional response, and action clarity | Will this land? |

Run the audience reaction analyzer **after** the editing pipeline passes. It reads the
finished document from the perspective of a specified target audience and reports what they
will understand, misunderstand, feel, and do.

**Workflow**: Provide the finished document plus a target audience description and desired
outcome → analyzer predicts comprehension gaps, persuasion weaknesses, emotional trajectory,
and action clarity → revision recommendations ranked by impact on the desired outcome.

The analyzer does not edit text. If its findings require revision, the document-drafter or
tone-rewriter agents can generate updated content, which then re-enters the editing pipeline.

**Full workflow**: Input → Generator → Stage 1 → Stage 2 → Stage 3 → Audience Analyzer → (revision if needed)

**Installing agents**: Run `bash scripts/setup.sh` from the repository root. This installs
all agents to `~/.claude/agents/` with the correct absolute paths substituted. Agents
become globally available across all Claude Code projects with no per-project configuration.
Re-run after moving or recloning the repository.

**Extending agents**: To add project-specific rules, create a `.claude/agents/` file in the
target project with the additional content. The globally installed base agents handle the
standard pipeline; the project file adds domain-specific rules on top.

## Re-Extracting PDF Source Material

The three source PDFs are stored in `legal-style/source-pdfs/` (git-ignored). Raw text
intermediates in `legal-style/source-pdfs/raw-text/` are also git-ignored (reproducible).

To download the source PDFs:

```bash
cd legal-style/source-pdfs
curl -O "https://www.courts.oregon.gov/publications/Documents/UpdatedStyleManual2002.pdf"
curl -O "https://www.oregonlegislature.gov/lc/PDFs/draftingmanual.pdf"
curl -O "https://www.oregonlegislature.gov/lc/PDFs/form-stylemanual.pdf"
```

To re-extract text (tries `pdftotext` first, falls back to `pymupdf`):

```bash
python scripts/extract_legal_pdfs.py
```

If a PDF is image-based (low character yield), the script instructs you to use the Claude Code
`Read` tool in 20-page increments as an OCR fallback.

## How Other Projects Reference This Library

### Agents (automatic after setup)

After running `bash scripts/setup.sh`, all seven agents (style analyzer, two generators,
three pipeline stages, and the audience analyzer) are globally available in all Claude Code
projects. No per-project configuration is required. New users should run the `style-analyzer`
agent first to calibrate the style profile before using the generators or editing pipeline.

### Reference files in prompts or agents

Point directly to files using the path where you cloned the library. For example, if cloned
to `~/dev/reference-library`:

```text
See ~/dev/reference-library/legal-style/QUICK-START.md for citation rules.
See ~/dev/reference-library/writing-style/style-profile.md for style targets.
See ~/dev/reference-library/writing-style/grammar-style/QUICK-START.md for grammar rules.
```

The library is designed to be referenced in-place, not copied. The installed agents already
resolve these paths automatically at setup time.
