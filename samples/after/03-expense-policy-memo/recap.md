---
document: 03-expense-policy-memo
stage: recap
timestamp: 2026-02-20
---

# Pipeline Recap: 03 — Expense Policy Memo

## Document Overview

| Field | Value |
| --- | --- |
| Format | memo |
| Topic | Employee expense reimbursement policy update recommendation |
| Word count (before) | ~807 words (validated document; original is comparable) |
| System prompt | sme-role (HR director) |
| Model | minimax/minimax-m2 |

## Before State

The document is a standard HR memo recommending a comprehensive overhaul of the firm's expense
reimbursement policy. The structure — Executive Summary, Background, Analysis, Recommendation,
Implementation Steps — is logical and the content is substantively correct in most areas, but
the draft contains seven grammar errors, no markdown heading hierarchy, and several AI-mechanical
patterns. Representative phrases illustrate the problems: the Recommendation section lists "Robust
substantiation and approvals" (AI filler adjective) and the Executive Summary promotes "a modern,
business-friendly policy" (vague endorsement language with no substantive content). The Background
section opens with "The firm's last comprehensive policy refresh was 2018" — missing the preposition
"in" and using "comprehensive" as empty filler. Underneath the surface errors sits a more serious
problem the grammar stage cannot catch: the mileage rate is wrong.

## Stage 1 — Grammar and Composition

**Status**: FAIL

**What was found** (counts):
- Grammar errors: 7
- Composition issues: 2
- Plain language flags: 2
- AI-mechanical flags: 2
- Non-prose issues: 4
- Total: 17

**Key fixes applied**:

- Missing preposition: "was 2018" → "was in 2018"
- Tense inconsistency in parallel series: "remote work increased" → "remote work has increased"
  (to match "have changed" and "have evolved" in the same clause)
- Sentence fragment: "taxable benefits treated as wages" → "taxable benefits are treated as wages"
- Broken parallel structure in Authorization levels: "CFO waiver for out-of-policy exceptions"
  → "CFO approves waivers for out-of-policy exceptions" (matching "Employees submit," "Manager
  approves," "Finance enforces caps")
- Repeated word typo: "Gifts/gifts:" → "Gifts:"
- Missing hyphen in compound modifier: "Company issued corporate card" → "Company-issued
  corporate card"
- Tense inconsistency + broken parallel in Establish ownership bullet: "Finance will lead
  policy drafting; HR ensures compliance with employment law; IT for integrations; Engagement
  Partners for client approvals" → "Finance will lead policy drafting; HR will ensure compliance
  with employment law; IT will manage system integrations; Engagement Partners will handle client
  approvals"
- Acronyms defined on first use: "BYOD" → "Bring Your Own Device (BYOD)"; "KPIs" → "key
  performance indicators (KPIs)"
- Heading hierarchy added throughout (all section headers converted from bold text to markdown
  `##` and `###` headings); numbered list converted from `1)` to `1.` notation
- Misplaced modifier restructured: "employees indicating confusion" → "Feedback from finance,
  clients, and employees indicated confusion..." (so "indicated" attaches to "Feedback")
- Redundant verb collapsed: "improves fairness and improves client billing" → "improves
  fairness, client billing, and cost allocation"
- AI-mechanical passive rewritten: "Client-related expenses flagged for possible bill-through
  or approval by engagement partner, ensuring compliance..." → "The engagement partner flags
  client-related expenses for bill-through approval, per client policy and firm gross margin
  targets"
- Nominalization softened: "reimbursements risk classification as taxable income" →
  "reimbursements risk being classified as taxable income"

**Note**: This is the only Stage 1 FAIL in the sample set. Seven grammar errors exceeded the
six-error FAIL threshold. All errors were mechanical and correctable; the stage supplied a clean
corrected document rather than requiring a resubmission cycle.

**Deferred to later stages**:

The stage flagged the Background sentence carrying three types of feedback as a non-prose
readability note (Issue #17), with an advisory to consider splitting it into a short list.
Stage 3 was noted as the authority to retain it for voice reasons. The factual accuracy of
all policy figures — including the mileage rate — was out of scope for Stage 1 and deferred
to Stage 2.

## Stage 2 — Factual Validation

**Status**: FAIL

**What was found** (counts):
- Claims analyzed: 28 (Verified: 8 / 29%, Expert Judgment: 9 / 32%, Assumptions: 4 / 14%,
  Unverified: 5 / 18%, Suspect: 2 / 7%)
- Reasoning errors: 3
- Hidden assumptions (assumption register): 8
- Universal quantifiers flagged: 2
- Bias patterns: 2 (confirmation bias, optimism bias)

**Key findings** (the two SUSPECT/blocking items lead):

- **IRS mileage rate error (SUSPECT — blocking)**: The document states "2025: 67.0 cents/mile."
  The correct 2025 IRS business standard mileage rate is 70 cents/mile per IRS Notice 2025-5,
  issued December 19, 2024. The 67-cent figure is the 2024 rate. This is a material factual
  error on a directly citable IRS figure in a compliance-focused memo.

- **Missing IRC §274(b) gift deductibility limit (SUSPECT — blocking)**: The document states
  "client gifts limited to $100 with written justification" with no mention of the IRS
  deductibility cap of $25 per recipient per year under IRC §274(b), unchanged since 1962. A
  memo explicitly positioned as aligning with "IRS and state rules" cannot omit this limit in
  the gifts section. The firm would reimburse up to $100 but only deduct $25 — a compliance gap
  the document creates without disclosing.

- **Unverified claims**: "The firm's last comprehensive policy refresh was in 2018" (no citation
  to internal records); "the firm has grown to approximately 200 employees" (no HR data source);
  "costs spike in meals/entertainment and ad-hoc software/tooling" (no internal trend data cited);
  "audit/compliance expectations have evolved" (vague — whose expectations?); "Inconsistent rules
  across teams lead to perceptions of unfair treatment" (plausible but causal link unestablished).

- **Reasoning errors**: (1) False certainty — "Updating the policy will reduce compliance risk,
  speed reimbursements..." treats successful implementation as a given; (2) False causation —
  "Standardizing thresholds...will shorten cycle time" ignores manager responsiveness and
  system reliability as co-factors; (3) Cherry-picking — all four analysis bullets present
  status-quo costs only; implementation risks, transition costs, and failure modes are absent.

- **Assumption register**: Eight hidden assumptions surfaced, including that the current expense
  system can be configured to support required workflows (not verified), that Finance/HR/IT/
  Engagement Partners have capacity to execute concurrently (not stated), that the $200/night
  hotel guideline tracks current market rates, and that the $50/month BYOD stipend meets IRS
  accountable plan requirements for tax-free treatment.

**Why this sample is important**:

This is the only sample in the set with a Stage 2 FAIL, and it caught a verifiable factual
error — a wrong IRS rate stated as current fact — that only Stage 2 could identify; Stage 1
has no mechanism to detect it, and Stage 3 would have passed it through to publication.

## Stage 3 — Voice and Style

**Status**: NEEDS WORK

**Pipeline note**: Stage 2 FAIL — the two blocking items are preserved as [AUTHOR MUST CORRECT]
markers in the rewritten document; Stage 3 proceeded for demonstration purposes only.

**Stylometry** (before → after):

- Sentence length σ: 6.2 → ~8+ (target ≥ 8; improved by Executive Summary restructure and
  added long sentence in Background)
- Short sentences: 14.5% → borderline pass (target ≥ 15%; effectively met when pillar fragment
  labels are excluded from the denominator)
- Long sentences: 0.0% → above 0% (target ≥ 15%; at least one sentence added past 30 words)
- AI patterns: 4 → 0 remaining

**Key fixes applied**:

- "Robust substantiation and approvals" → "Full documentation and approval requirements"
  (removes AI filler adjective; more precise about what the pillar actually requires)

- "a modern, business-friendly policy" → "a clear, enforceable policy" ("modern" is a vague
  endorsement; "business-friendly" is promotional language with no policy content)

- "the firm's last comprehensive policy refresh" → "the firm's last full policy refresh"
  ("comprehensive" is AI filler; the sentence carries no additional meaning with it)

- "Integrate corporate card feeds to streamline reconciliation" → "Integrate corporate card
  feeds to eliminate manual entry and cut reconciliation time" ("streamline" replaced with
  specific outcome language)

- Executive Summary restructured for burstiness: the original three sentences were all 16-21
  words (σ = 2.1); the rewrite shortens one to a direct declaration and extends the
  recommendation sentence to carry the full rationale, improving σ to approximately 5.

- One long sentence added to Background to break the 28-word ceiling: "The underlying federal
  and state rules on accountable plans and substantiation have not materially changed since the
  last refresh — the three-prong test for non-taxable treatment remains the same — but
  enforcement scrutiny has increased..."

- "This increases the firm's liability and can lead to penalties" folded into the prior sentence:
  "reimbursements risk classification as taxable income, increasing the firm's liability and
  exposing it to penalties" (eliminates formulaic "This [noun]" opener)

- Stage 2 hedges preserved: "will reduce compliance risk" → "A well-implemented policy update
  is expected to reduce compliance risk..."; "will shorten cycle time" → "are expected to shorten
  cycle time, assuming consistent manager review within the prescribed 7-day window"

## Final State

After all three stages, the document is structurally clean (heading hierarchy, parallel
construction throughout, no grammar errors), factually tagged with claim-level confidence
ratings, and voiced as a competent HR director rather than an AI model — the four blacklisted
AI terms have been replaced and the Executive Summary reads with appropriate sentence variety.
The Implementation Steps section was flagged for persona drift (procedural enumeration with no
authorial voice), a minor remaining weakness. Two items block final clearance and require author
action: the mileage rate must be corrected from 67.0 cents/mile to 70 cents/mile with a citation
to IRS Notice 2025-5, and the gifts bullet must add a disclosure of the $25 IRC §274(b)
deductibility cap before the document can be published.

## What This Sample Demonstrates

- **Stage 1 FAIL threshold in action**: Seven grammar errors cross the six-error FAIL threshold,
  making this the only sample in the set to fail Stage 1. The stage shows how to handle a FAIL
  gracefully — by supplying a corrected document that lets Stage 2 proceed without a full
  resubmission cycle.

- **Stage 2 FAIL on a verifiable factual error**: The 67.0 cents/mile mileage figure is the
  clearest example in the sample set of a specific, citable, wrong number. Stage 2 is the only
  stage that can catch this; Stage 1 and Stage 3 have no mechanism to verify regulatory figures.

- **Material omission as a SUSPECT claim**: The gift deductibility gap illustrates that Stage 2
  catches not just wrong facts but missing required disclosures — the $100 policy ceiling is not
  wrong on its face, but the omission of the §274(b) cap makes the section materially incomplete
  in context.

- **Pipeline continuation under FAIL**: Stage 3 proceeding "for demonstration purposes only"
  with [AUTHOR MUST CORRECT] markers preserved shows how the pipeline handles a blocking FAIL
  without discarding downstream work — the voice corrections are complete and ready to accept
  once the author fixes the two blocking items.

- **Confirmation bias and optimism bias as pipeline catches**: The one-sided analysis
  (no implementation risks discussed) and the "will reduce compliance risk" false certainty are
  reasoning-level problems that Stage 2 surfaces even when the prose is grammatically clean.
  Neither Stage 1 nor Stage 3 is designed to catch them.
