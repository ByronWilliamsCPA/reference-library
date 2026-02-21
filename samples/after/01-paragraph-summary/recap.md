---
document: 01-paragraph-summary
stage: recap
generated: 2026-02-20
---

# Pipeline Recap: 01 — Paragraph Summary

## Document Overview

| Field | Value |
| --- | --- |
| Format | paragraph-summary |
| Topic | Remote work long-term effects on productivity and culture |
| Word count (before) | ~150 words (3 sentences) |
| System prompt | none (raw baseline) |
| Model | minimax/minimax-m2 |

## Before State

The original document is a single three-sentence paragraph averaging 49 words per sentence
(sigma = 3.9) — a wall of text with almost no rhythmic variation. Every sentence chains two
or three independent ideas through semicolons, producing compound structures that read as
compressed outlines rather than prose. The writing carries the signature patterns of unrevised
AI output: vague authority appeals ("Most longitudinal studies report"), abstract noun clusters
("outcome-driven trust," "central levers for sustainable performance and culture"), gerund-phrase
list endings ("unless replaced by intentional rituals, knowledge platforms, and synchronous
collaboration windows"), and nominalizations hiding simple verbs ("lower effectiveness,"
"performance clarity").

## Stage 1 — Grammar and Composition

**Status**: NEEDS WORK

**What was found** (counts):

- Grammar errors: 0
- Composition issues: 4
- Plain language flags: 2
- AI-mechanical flags: 4

**Key fixes applied**:

- Nominalization repair (Issue 7): "lower effectiveness" replaced with "become less effective"
  — restoring the verb that was buried in the noun form.
- Nominalization repair (Issue 8): "performance clarity" replaced with "the clarity of
  performance expectations" — a partial repair; full restructuring deferred to Stage 3.
- Participial phrase attachment repair (Issue 9): the trailing clause ", requiring stronger
  work-life boundaries and more disciplined project management" replaced with a finite clause:
  "so organizations need stronger work-life boundaries and more disciplined project management."
  Before the fix, the gerund phrase attached loosely to the second independent clause of a
  semicolon-joined sentence; after, the causal connection is explicit.
- All four composition warnings (sentence overloading, 60-word average, weak sentence-final
  positions, lack of a unifying topic sentence) were flagged as Advisory and deferred to
  Stage 3, which has final authority over voice and structure.

**Deferred to later stages**:

All seven advisory issues — including the three-topic paragraph structure, the 60-word sentence
lengths, the weak sentence-final positions ("and culture," "across locations"), the abstract
close ("sustainable performance and culture"), and the plain language flags — were held for
Stage 3. Stage 1 corrected only what was mechanical and unambiguous.

## Stage 2 — Factual Validation

**Status**: CONDITIONAL

**What was found** (counts):

- Claims analyzed: 12 (Verified: 0, Expert Judgment: 7 — 58%, Unverified: 5 — 42%, Suspect: 0)
- Reasoning errors: 2
- Hidden assumptions: 3

**Key findings**:

- Authority appeal without evidence (Issue 1, Reasoning Error 1): "Most longitudinal studies
  report" invokes unnamed research as collective proof. No studies are named; "most" cannot
  be supported in a summary. Fix: replace with "Research generally shows" — the finding's
  direction is sound; the authority frame is not warranted.
- Overclaimed empirical rigor (Issue 3): "measurable declines in informal learning" implies
  quantification has been done. The phenomenon is real, but the word "measurable" imports
  precision the document does not provide. Fix: delete "measurable."
- False causation (Issue 4, Reasoning Error 2): "ties that weaken innovation unless replaced
  by intentional rituals, knowledge platforms, and synchronous collaboration windows" presents
  the three interventions as causally sufficient to restore innovation. The causal mechanism
  is not established, and the interventions are not defined. Fix: qualify as associative —
  "which research links to reduced innovation capacity."
- Undefined comparison (Issue 5): "hybrid or flexible models preserve cultural cohesion better"
  lacks a comparison baseline. Better than what? Fix: add "than fully remote arrangements."
- Conflated equity claim with mixed evidence (Issue 6): the sentence treats caregivers and
  underrepresented groups as a single category with uniform positive outcomes. Evidence on
  remote work and underrepresented groups is mixed — some research documents promotion
  disadvantage and visibility gaps. Fix: split into two claims with appropriate hedging on
  the underrepresented groups finding.

**Bias assessment**:

Two bias patterns were found: mild confirmation bias in leading with the productivity-positive
finding while relegating coordination friction to a subordinate clause, and moderate
cherry-picking on the equity claims by presenting only the positive attrition finding and
omitting the counter-evidence on promotion disadvantage for underrepresented groups.

## Stage 3 — Voice and Style

**Status**: PASS (input failed on 5 of 8 measures; rewrite passes all)

**Stylometry** (before → after):

- Sentence length sigma: 3.9 → 12.0 (target >= 8)
- Short sentences (< 8 words): 0% → 27% (target >= 15%)
- Long sentences (> 30 words): 100% → 18% (target >= 15%)
- AI patterns: 6 → 0

**Key fixes applied**:

- Sentence decomposition: the three 49-word mega-sentences were broken into 11 sentences
  across three paragraphs, introducing deliberate length variation and burstiness. The
  before/after contrast is sharpest in Paragraph 2: the original's 53-word compound sentence
  becomes a five-word topic sentence ("Cultural cohesion is harder to sustain.") followed by
  specific elaboration.
- Abstract noun cluster elimination: "outcome-driven trust" replaced with a concrete
  description of the mechanism — "a reliance on trust built through outputs rather than
  presence." "Central levers for sustainable performance and culture" replaced with "the
  practical levers for cultures that hold."
- List-as-remedy construction removed: "unless replaced by intentional rituals, knowledge
  platforms, and synchronous collaboration windows" replaced with "research links their decline
  to reduced innovation capacity" — resolving Stage 2's false causation flag simultaneously.
- All six Stage 2 required fixes incorporated directly into the rewrite. The author does not
  need to apply them separately.
- Two author judgment calls flagged but not blocking: (1) "than most expect going in" in
  Paragraph 1 adds grounding warmth and can be cut for a crisper close; (2) "for cultures
  that hold" in Paragraph 3 is compressed and idiomatic — the author may substitute "for
  organizations that want distributed models to hold" if the audience calls for more literal
  phrasing.

## Final State

The output is three focused paragraphs — productivity, culture, equity — each anchored by a
short topic sentence and developed through specific, varied-length sentences with no AI
signature patterns remaining. The claims are appropriately hedged where Stage 2 required it
("Research generally shows," "tend to," "appear to hold") without over-hedging throughout,
and the equity section now accurately represents the state of evidence by distinguishing the
well-supported caregiver finding from the more mixed underrepresented groups finding. The
author has two minor judgment calls to make on phrasing but no substantive corrections to
apply.

## What This Sample Demonstrates

- How AI-generated prose fails on stylometry even when it is factually directional and
  grammatically correct: three sentences of nearly identical length (51 / 53 / 44 words) is
  the single most reliable signal Stage 3 uses to identify unrevised AI output, and this
  sample illustrates it clearly.
- The difference between a Stage 1 repair (mechanical, objective, applied immediately) and
  a Stage 3 advisory (structural and voice-related, held for final authority): Stage 1 fixed
  three issues and deferred seven, which is the correct behavior for a NEEDS WORK document
  with no grammar errors.
- How the pipeline handles overclaimed authority: the "Most longitudinal studies" framing
  survived Stage 1 (not a grammar issue) but was caught by Stage 2 as an authority appeal
  without evidence and then eliminated by Stage 3 in the rewrite — a cross-stage resolution
  path.
- How Stage 2 and Stage 3 interact: Stage 2 issued six required fixes as author-directed
  instructions; Stage 3 incorporated all six directly into the rewrite rather than waiting
  for the author, with notes explaining which rewrite decision satisfied which Stage 2 issue.
- The distinction between hedging as a style problem and hedging as a semantic preservation
  constraint: the rewrite's 27% hedge density exceeds the 5-10% target, but Stage 3
  documented it as a required preservation of Stage 2 UNVERIFIED tags rather than flagging
  it as over-hedging — illustrating how pipeline stages respect each other's authority within
  defined limits.
