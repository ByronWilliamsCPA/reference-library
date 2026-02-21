# Writing Pipeline Sample Documents

Before/after examples demonstrating the three-stage writing quality pipeline. Each pair shows
what the pipeline catches and fixes across grammar, factual accuracy, and voice.

## Directory Structure

```text
samples/
├── before/    # Raw AI output with natural AI-mechanical patterns
│   ├── 01-paragraph-summary.md
│   ├── 02-client-status-email.md
│   ├── 03-expense-policy-memo.md
│   ├── 04-onboarding-proposal.md
│   └── 05-workforce-planning-analysis.md
└── after/     # Post-pipeline output with stage files and recap
    ├── 01-paragraph-summary/
    │   ├── stage-1-grammar.md
    │   ├── stage-2-validation.md
    │   ├── stage-3-voice.md
    │   └── recap.md           # Quick-reference summary of all three stages
    ├── 02-client-status-email/
    │   └── ...
    └── ...
```

## Sample Inventory

| File | Format | Word range | System prompt | Best demonstrates |
| --- | --- | --- | --- | --- |
| `01-paragraph-summary.md` | 1-paragraph summary | 120-180 words | None (raw baseline) | Sentence-length monotony (σ 3.9 → 12.0), AI patterns |
| `02-client-status-email.md` | 3-5 paragraph email | 250-400 words | SME: management consultant | False precision on statistics, structural AI tells |
| `03-expense-policy-memo.md` | 1-2 page memo | 500-800 words | SME: HR director | Stage 1 FAIL + Stage 2 FAIL with verifiable factual error |
| `04-onboarding-proposal.md` | Short proposal | 350-500 words | None (raw baseline) | Unsourced benefit claims, false causation chains |
| `05-workforce-planning-analysis.md` | Analytical report | 400-550 words | None (raw baseline) | Echo-opener AI tells, nominalization density, regulatory assumptions |

**System prompt strategy**: Three samples use no system prompt (raw baseline showing default AI
output). Two use an SME role to simulate the realistic case where a user frames domain expertise
but no writing quality guidance. "Professional writer" is intentionally excluded because it
suppresses the AI-mechanical patterns the pipeline is designed to catch.

**Model**: `minimax/minimax-m2` via OpenRouter. No house-style tuning; reliably produces the
natural AI patterns listed below.

## Recap Documents

Each `after/` subdirectory contains a `recap.md` that synthesizes all three stages into a single
reference document. Use the recap when you want to understand:

- What the before document contained and why it was problematic
- What each stage caught and changed, with before → after examples
- What the final document looks like after all three stages
- Which pipeline capabilities the sample best illustrates

For the full stage-by-stage detail, read the individual `stage-N-*.md` files.

## What the Before Samples Contain

Each before sample is unmodified model output and should exhibit:

**Stage 1 targets (grammar and composition)**

- Nominalization overuse: verb concepts recast as nouns ("the implementation of," "the
  optimization of")
- Gerund phrase padding: sentence-final -ing clauses that promise but don't specify ("ensuring
  reliability," "driving growth," "enabling success")
- Present participle stacking: three or more -ing forms chained without clear referents
- Downtoner accumulation: two or more hedges per clause ("somewhat generally considered to be
  relatively effective")
- Deadwood phrasing: "in order to," "owing to the fact that," "at this point in time"

**Stage 2 targets (factual validation)**

- Vague statistics without sources ("studies show," "research indicates")
- Universal quantifiers overstating claims ("all," "never," "always")
- Assumed consensus ("industry best practice is")
- Hidden assumptions stated as facts
- Unsupported causal claims ("X led to Y" with no evidence)
- Verifiable factual errors (sample 03: wrong IRS mileage rate)

**Stage 3 targets (voice and style)**

- AI cliche vocabulary: "leverage," "synergies," "streamline," "robust," "seamless,"
  "holistic," "cutting-edge," "transformative"
- Vague quantifiers: "significantly," "substantially," "considerably," "markedly"
- Filler phrases: "it's important to note," "in conclusion," "moving forward,"
  "in today's landscape"
- Monotonous sentence length (standard deviation below 8 words)
- AI structural tells: echo-openers that summarize the previous paragraph
  ("These productivity gains propagate...," "The talent market responds in kind...")
- All sentences following the same Subject-Verb-Object structure

**Note on transition overuse**: The "Additionally/Furthermore/Moreover" overuse pattern
(listed as a Stage 1 and Stage 3 target in the agent definitions) does not appear in these
samples because the document formats — paragraph summaries, emails, memos, proposals, and
analytical reports — produce different AI transition strategies. The minimax model used
sophisticated echo-openers and causal connectors instead of explicit additive transitions.
The transition-words-reference.md guide still applies when the pattern appears in other documents.

## Pipeline Flow

Run the three stages in sequence on any before sample:

```text
before sample
    -> Stage 1: grammar-composition-editor  (fixes mechanics, flags AI-mechanical patterns)
    -> Stage 2: document-validator          (verifies facts, audits assumptions, checks reasoning)
    -> Stage 3: writing-style-editor        (eliminates AI voice, aligns stylometry targets)
    -> after/   (save each stage output + recap separately to show the progression)
```

If Stage 3 rewrites text in a way that changes meaning, those sections loop back through Stage 1
then Stage 2. Maximum three remediation cycles before human review.

## Actual Pipeline Results (Summary)

| Sample | Stage 1 | Stage 2 | Stage 3 |
| --- | --- | --- | --- |
| 01-paragraph-summary | NEEDS WORK | CONDITIONAL | FAIL → rewritten (σ 3.9 → 12.0, 6 AI patterns removed) |
| 02-client-status-email | NEEDS WORK | CONDITIONAL | FAIL → rewritten (6 AI patterns, 0% → 17% short sentences) |
| 03-expense-policy-memo | FAIL (corrected) | FAIL (IRS rate error, gift limit gap) | NEEDS WORK (2 author corrections required) |
| 04-onboarding-proposal | NEEDS WORK | CONDITIONAL | FAIL → rewritten (3 AI patterns, benefits reframed) |
| 05-workforce-planning-analysis | FAIL (corrected) | CONDITIONAL | NEEDS WORK (echo-openers, nominalization density) |

## Regenerating the Before Samples

The before samples are committed to the repository. If you need to regenerate them (to test a
different model or prompt), run:

```bash
python3 scripts/generate_before_samples.py
```

To regenerate a single sample:

```bash
python3 scripts/generate_before_samples.py --only 05-workforce-planning-analysis.md
```

Requires `OPENROUTER_API_KEY` in the `.env` file at the repository root. The script overwrites
existing files in `samples/before/`.

## File Format

Each before sample file uses YAML frontmatter followed by the raw model output:

```yaml
---
format: [email | memo | paragraph-summary | proposal | analytical-report]
topic:  [one-line topic description]
model:  minimax/minimax-m2
system_prompt: [none | sme-role]
generated: [ISO 8601 UTC timestamp]
stage: before
---
```

Each after stage file uses:

```yaml
---
stage: [1 | 2 | 3]
agent: [grammar-composition-editor | document-validator | writing-style-editor]
source: [relative path to input file]
timestamp: [ISO 8601 UTC]
---
```
