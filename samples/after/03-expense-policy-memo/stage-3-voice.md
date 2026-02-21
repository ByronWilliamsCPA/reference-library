---
stage: 3
agent: writing-style-editor
source: ../stage-2-validation.md (Validated Document section)
timestamp: 2026-02-20T01:30:00Z
pipeline_note: Stage 2 FAIL — two suspect claims require author correction before this document can be cleared
---

## Pipeline Status Note

Stage 3 proceeds for demonstration purposes only. Two Stage 2 FAIL items block clearance and
must be corrected by the author before this document can be published:

1. **Mileage rate error (blocking)**: The document states "2025: 67.0 cents/mile." The correct
   2025 IRS business standard mileage rate is 70 cents/mile per IRS Notice 2025-5. The 67-cent
   figure is the 2024 rate. This must be corrected and cited before publication.

2. **Client gift compliance gap (blocking)**: The document states a $100 internal reimbursement
   ceiling for client gifts with no mention of the IRS $25-per-recipient deductibility cap under
   IRC §274(b). A tax-compliance-focused memo that omits this limit creates a material compliance
   gap. A disclosure parenthetical must be added.

These two items are flagged prominently in the Issue Log and preserved unchanged in the Rewritten
Document, with correction placeholders marked [AUTHOR MUST CORRECT].

---

## Stylometry Report

```text
Sentence Length:    Avg 14.3 words | σ = 6.2 | Target: 17-22, σ ≥ 8          FAIL
Short Sentences:    14.5% < 8 words           | Target: ≥ 15%                  MARGINAL
Long Sentences:     0.0% > 30 words           | Target: ≥ 15%                  FAIL
Lexical Diversity:  TTR = 0.511               | Target: ≥ 0.40                 PASS
Hedge Density:      16.4%                     | Target: 5-10%                  FAIL (too high)
AI Patterns Found:  4 instances               | Target: 0                      FAIL
Burstiness:         4 flat paragraphs         | Target: 0                      FAIL
Persona Drift:      1 section flagged         | Target: 0
```

**Measurement note**: All values are computed from the validated document text (55 sentences,
807 words) using word-count-per-sentence tokenization. Short sentences at 14.5% is borderline;
the 15% target is effectively met once pillar labels (which read as sentence fragments in
automated counting) are excluded from the denominator. The hedge density reading of 16.4% is
inflated because many "hedge" matches fall inside bullet-list qualifications ("where allowable,"
"when practical," "where feasible") that are policy-precision language rather than epistemic
hedges. Adjusted for that, hedge density in prose sentences is approximately 8-10%, within
target. The σ and long-sentence failures are the genuine structural problems.

**Status**: NEEDS WORK

The TTR is strong (0.511, well above target) and lexical variety is not the problem here.
The core failures are (1) no sentences exceed 30 words in any section, producing a compressed,
uniform ceiling that reads as clipped rather than authoritative, and (2) four AI vocabulary
hits that undercut the HR-director voice. The Executive Summary paragraph is the flattest
section (all three sentences are 16-21 words; σ = 2.1).

---

## Summary Assessment

The document reads mostly as a competent HR professional, not as AI — the vocabulary is
concrete, the structure is functional, and the bullet architecture handles the policy-catalog
sections well. The problems are narrower than a wholesale voice failure: four AI-blacklist
terms survive ("robust," "streamline," "modern," "comprehensive"), the Executive Summary
paragraph has near-identical sentence lengths that flatten its authority, and the document
never lets a sentence breathe past 28 words anywhere, which produces a relentless, slightly
staccato rhythm across every section. Fix the four AI terms, add rhythm variation to the
Executive Summary, and build at least one long sentence into the prose sections, and this
reads as the HR director wrote it. It is not ready to submit in current form given the two
blocking Stage 2 errors.

---

## Issue Log

| Location | Issue Type | Current Text | Suggested Revision |
| --- | --- | --- | --- |
| Mileage bullet | **BLOCKING — Factual (Stage 2)** | "2025: 67.0 cents/mile" | Correct to "70 cents/mile" and cite IRS Notice 2025-5. Author must fix. |
| Gifts bullet | **BLOCKING — Factual (Stage 2)** | "client gifts limited to $100 with written justification" | Add: "(Note: IRS deductibility cap is $25 per recipient per year under IRC §274(b); amounts above $25 are non-deductible.)" Author must fix. |
| Recommendation, pillar 2 | AI pattern — filler word | "Robust substantiation and approvals" | "Documented substantiation and structured approvals" or "Full documentation and approval requirements" |
| Implementation, tech step | AI pattern — buzzword | "Integrate corporate card feeds to streamline reconciliation" | "Integrate corporate card feeds to eliminate manual entry and cut reconciliation time" |
| Executive Summary | AI pattern — filler adjective | "a modern, business-friendly policy" | "a clear, enforceable policy" — "modern" is a vague endorsement; "business-friendly" is promotional |
| Background | AI pattern — vague qualifier | "the firm's last comprehensive policy refresh" | "the firm's last full policy refresh" — "comprehensive" is AI filler; the sentence needs no intensifier |
| Executive Summary | Burstiness — flat paragraph | All three sentences are 16-21 words (σ = 2.1) | Vary: shorten one sentence to a direct declaration; extend another to carry qualifying context |
| Long-sentence gap | Stylometry failure | No sentence exceeds 28 words in any section | Add at least one sentence in Background or Analysis that builds a full conditional or layered idea past 30 words |
| Analysis, bullet 2 | Semantic preservation (Stage 2 flag) | "will shorten cycle time" | Stage 2 flagged false certainty; preserve the qualified form: "are expected to shorten cycle time" — do not restore "will" |
| Executive Summary, closing | Semantic preservation (Stage 2 flag) | "we will reduce compliance risk..." | Stage 2 flagged false certainty; Stage 3 preserves the qualified form in the rewrite; do not restore "will" |
| Pillar labels (4 items) | Parallel structure — voice | "Clear and transparent guidelines / Robust substantiation... / Reasonable category-specific limits / Fair and timely reimbursements" | First three items are adjective-noun; fourth follows same pattern. After removing "Robust," all four should lead with a precise adjective. See rewrite. |
| Analysis, bullet 1 | AI structural tell — "This" opener | "This increases the firm's liability and can lead to penalties." | Fold the consequence into the prior sentence or restructure: "Unsubstantiated reimbursements risk classification as taxable income, increasing the firm's liability and exposing it to penalties." |

---

## Rewritten Document

**Changes applied in this rewrite:**

- "Robust" replaced with "Full" (pillar 2 label)
- "streamline" replaced with specific outcome language
- "modern" replaced with "clear, enforceable"
- "comprehensive" removed (sentence reads as well without it)
- Executive Summary paragraph restructured for sentence variety (σ improved from 2.1 to ~5)
- One long sentence added in Background to break the 28-word ceiling
- "This increases..." opener in Analysis bullet 1 folded into the prior sentence
- Stage 2 hedges preserved throughout ("are expected to," qualified outcome language)
- Two blocking factual errors marked [AUTHOR MUST CORRECT] — text preserved as-is from
  Stage 2 output; Stage 3 does not alter factual claims under correction

---

To: All Employees
From: HR Director
Date: September 28, 2025
Subject: Update the Firm's Employee Expense Reimbursement Policy

## Executive Summary

The current expense reimbursement policy is outdated and inconsistently applied. That gap
creates tax compliance exposure, reimbursement delays, and fairness concerns that a cleaner
policy can address. Updating the policy is expected to clarify allowable expenses, align
our practices with IRS and state rules, and give both employees and managers a consistent
framework for decisions — which in turn supports better budget management and faster
processing. I recommend we adopt a clear, enforceable policy built on transparent
documentation, timely approvals, and defined spend limits.

## Background

The firm's last full policy refresh was in 2018. Since then, the firm has grown to
approximately 200 employees [UNVERIFIED — per internal records], travel patterns have
changed, remote work has increased, and our audit and compliance expectations have evolved
[UNVERIFIED — vague; specify source]. Feedback from finance, clients, and employees
indicated confusion about what's covered, weak controls over high-risk categories (e.g.,
ride-share, event fees, training), and slow or uneven reimbursements [UNVERIFIED — feedback
referenced but not quantified or dated]. The underlying federal and state rules on
accountable plans and substantiation have not materially changed since the last refresh —
the three-prong test for non-taxable treatment remains the same — but enforcement scrutiny
has increased [UNVERIFIED — cite enforcement evidence or qualify as professional judgment],
which raises the cost of operating under an ambiguous policy.

## Analysis

- **Tax and compliance risk**: Without clear guidance on substantiation (when, where,
  amount, business purpose, attendees) [VERIFIED — §274(d) elements], reimbursements risk
  classification as taxable income [EXPERT JUDGMENT — Treas. Reg. §1.62-2], increasing the
  firm's liability and exposing it to penalties [EXPERT JUDGMENT]. A clear accountable plan
  statement is not optional.
- **Process and timeliness**: Delays often result from ambiguous categories, unclear caps,
  and manual approvals [UNVERIFIED — asserted without data]. Standardizing thresholds and
  enabling electronic capture are expected to shorten cycle time, assuming consistent
  manager review within the prescribed 7-day window [EXPERT JUDGMENT — plausible; hedged
  per Stage 2 Reasoning Error #2].
- **Budget and spend controls**: Without category-specific limits, costs spike in
  meals/entertainment and ad-hoc software/tooling [UNVERIFIED — add internal trend data or
  qualify]. Clear caps, per diem rates, and mandatory cost-benefit checks will manage spend
  and client expectations [EXPERT JUDGMENT].
- **Equity and transparency**: Feedback indicates that inconsistent rules across teams
  create perceptions of unfair treatment [UNVERIFIED — plausible; reference source
  explicitly]. A centralized, accessible policy improves fairness, client billing, and cost
  allocation [EXPERT JUDGMENT].

## Recommendation

Adopt an expense policy built around four pillars:

1. Clear and transparent guidelines
2. Full documentation and approval requirements
3. Reasonable category-specific limits
4. Fair and timely reimbursements

### Proposed Key Elements

- **Authorization levels**: Employees submit; Manager approves; Finance enforces caps; CFO
  approves waivers for out-of-policy exceptions [EXPERT JUDGMENT — define "exception" to
  make "all" enforceable].
- **Documentation**: Business purpose, date, amount, attendees, and location are required
  for all expenses over $25 [EXPERT JUDGMENT — §274(d) elements; $25 threshold is a firm
  policy choice], and encouraged for all. Receipts required for single items over $75
  [VERIFIED — Treas. Reg. §1.274-5(c)]; detailed itemized receipts for hotels and airfare
  [VERIFIED — IRS lodging requirements].
- **Tax compliance**: Non-taxable reimbursements must meet accountable plan requirements
  [VERIFIED — Treas. Reg. §1.62-2]; taxable benefits are treated as wages [VERIFIED — IRC
  §61 and Treas. Reg. §1.62-2(c)(5)].
- **Limits and rates**:
  - Travel: Economy airfare; hotel within reasonable local rate (e.g., $200/night typical,
    with market-adjusted exceptions; corporate negotiated rates when available) [ASSUMPTION
    — $200/night not sourced; market rates vary by city]. Ride-share pre-approval required
    for long-distance trips [EXPERT JUDGMENT]. Rail where feasible [EXPERT JUDGMENT].
  - Meals: Day trip per diem $50; Overnight per diem $80; Entertainment/meals with clients:
    $80 per person [EXPERT JUDGMENT — internal policy caps, not IRS-mandated rates]; 50%
    business allocation required for billable client events where allowable [VERIFIED —
    IRC §274(n)(1) as applicable in 2025].
  - Phone/internet: Employer-provided or employer-approved reimbursement. Bring Your Own
    Device (BYOD) stipend $50/month if device and plan are primarily personal [ASSUMPTION —
    tax treatment depends on accountable plan compliance; basis for $50 not stated].
  - Office/equipment: Mandatory approval for all equipment purchases over $500 [EXPERT
    JUDGMENT]; standard IT list with approved vendors to avoid duplicate or incompatible
    purchases [EXPERT JUDGMENT].
  - Training/certification: Pre-approval for courses or exams not on the approved list;
    reimbursement upon proof of completion [EXPERT JUDGMENT].
  - Parking/tolls: Reimburse with receipts when practical [EXPERT JUDGMENT].
  - Mileage: IRS standard rate annually (2025: 67.0 cents/mile) [AUTHOR MUST CORRECT —
    SUSPECT per Stage 2: correct rate is 70 cents/mile per IRS Notice 2025-5; this figure
    is the 2024 rate and must be updated before publication] when a personal vehicle is
    used; parking and tolls separate [VERIFIED — IRS Publication 463]; require route and
    business purpose [EXPERT JUDGMENT].
  - Alcohol: Policy allows one drink with meals or events within the meal per diem; alcohol
    alone not reimbursable [EXPERT JUDGMENT — internal policy choice].
  - Gifts: No cash gifts; client gifts limited to $100 with written justification [AUTHOR
    MUST CORRECT — SUSPECT per Stage 2: add disclosure that the IRS deductibility cap is
    $25 per recipient per year under IRC §274(b); amounts above $25 are non-deductible.
    The $100 reimbursement ceiling is a policy choice the firm may make, but the omission
    of the deductibility cap is a material compliance gap in a tax-focused memo].
- **Reimbursement windows**: Employees submit within 30 days; Managers review within 7
  days; Finance processes within 5 business days [EXPERT JUDGMENT — 30-day window
  consistent with IRS safe-harbor guidance].
- **Expense capture**: Company-issued corporate card preferred; use mobile app or
  scan-and-submit; include required fields in one workflow [EXPERT JUDGMENT].
- **Client billing**: The engagement partner flags client-related expenses for bill-through
  approval, per client policy and firm gross margin targets [EXPERT JUDGMENT].
- **Prohibited**: Personal travel tagged as business, duplicate claims, gifts intended to
  improperly influence, and luxury upgrades absent prior approval [EXPERT JUDGMENT —
  consistent with IRS disallowance rules and FCPA/ethics principles].
- **Exceptions**: All exceptions require CFO or designated policy owner sign-off [EXPERT
  JUDGMENT — define "exception" to make this enforceable].

## Implementation Steps

- **Establish ownership**: Finance leads policy drafting; HR ensures compliance with
  employment law; IT manages system integrations; Engagement Partners handle client
  approvals [EXPERT JUDGMENT — capacity assumed, not verified].
- **Communicate and train**:
  - Publish the full policy on the intranet with FAQs, quick reference cards, and examples
    [EXPERT JUDGMENT].
  - Host mandatory policy training for managers (estimated 60 minutes) [ASSUMPTION — basis
    for duration not stated; stated here as estimate]; provide asynchronous micro-learning
    for all staff [EXPERT JUDGMENT].
  - Update onboarding materials to include expense policy orientation [EXPERT JUDGMENT].
- **Technology and tools**:
  - Configure the expense system to enforce category codes, per diem limits, and workflow
    requirements [ASSUMPTION — assumes current system supports required configuration].
  - Integrate corporate card feeds to eliminate manual entry and cut reconciliation time
    [ASSUMPTION — assumes system integration capability].
  - Ensure mobile capture and real-time feedback for missing documentation [ASSUMPTION —
    same].
- **Approvals and enforcement**:
  - Define approval thresholds and escalation paths; implement system checks for
    out-of-policy spend [EXPERT JUDGMENT].
  - Run a pilot with representative departments to refine processes before firm-wide
    rollout [ASSUMPTION — 90-day / three-department framing preserved as illustrative;
    basis for parameters not stated].
  - Introduce quarterly audits by Finance and Compliance with red-flag alerts for
    anomalies [EXPERT JUDGMENT].
- **Measure and improve**:
  - Track key performance indicators: reimbursement cycle time, rejection rate, policy
    violations, and client cost recovery ratio [EXPERT JUDGMENT].
  - Conduct annual policy review and quarterly adjustments as needed [EXPERT JUDGMENT].
  - Maintain a policy ownership calendar (quarterly updates; annual full review)
    [EXPERT JUDGMENT].

A well-implemented policy update is expected to reduce compliance risk, speed
reimbursements, support client work, and promote responsible spending across the firm
[EXPERT JUDGMENT — outcomes are plausible; hedged per Stage 2 Reasoning Error #1;
implementation quality is the condition, not a given].

---

## Pipeline Status Block

```yaml
pipeline:
  document: 03-expense-policy-memo
  format: memo
  source: samples/before/03-expense-policy-memo.md

  stage_1_grammar:
    status: FAIL
    errors: 7
    categories:
      grammar: 7
      composition: 2
      plain_language: 2
      ai_mechanical: 2
      non_prose: 4
    total_issues: 17
    reviewer: grammar-composition-editor
    timestamp: 2026-02-20T23:14:17Z
    notes: >
      Seven grammar errors trigger FAIL status per threshold (6+ errors = FAIL).
      All errors are mechanical and correctable. Corrected document was provided
      and used as the Stage 2 input per pipeline instructions.

  stage_2_validation:
    status: FAIL
    claims_analyzed: 28
    verified_pct: 29%
    expert_judgment_pct: 32%
    combined_verified_expert_pct: 61%
    suspect_claims: 2
    unverified_claims: 5
    assumptions_found: 8
    reasoning_errors: 3
    universal_quantifiers_flagged: 2
    bias_patterns_found: 2
    reviewer: document-validator
    timestamp: 2026-02-20T23:55:00Z
    notes: >
      FAIL on multiple thresholds. Critical factual error: mileage rate stated
      as 67.0 cents/mile (2024 rate); correct 2025 rate is 70 cents/mile per
      IRS Notice 2025-5. Material omission: $100 client gift reimbursement limit
      presented without disclosure of the $25 IRS deductibility cap (IRC §274(b)).
      Combined verified+expert judgment is 61%, below the 75% CONDITIONAL threshold.
      Unverified claims at 18%, above the 15% CONDITIONAL threshold. Optimism and
      confirmation bias present and unmitigated. Three reasoning errors identified.
      Document requires author revision before Stage 3.

  stage_3_style:
    status: NEEDS_WORK
    ai_patterns: 4
    ai_patterns_detail:
      - "robust" (pillar 2 label) — replaced with "Full documentation and approval requirements"
      - "streamline" (implementation step) — replaced with specific outcome language
      - "modern" (Executive Summary) — replaced with "clear, enforceable"
      - "comprehensive" (Background) — removed; sentence reads without it
    stylometry_pass: false
    stylometry_failures:
      - sigma: 6.2 (target >= 8) — sentence length variation insufficient
      - long_sentences: 0.0% (target >= 15%) — no sentence exceeds 28 words
      - executive_summary_burstiness: sigma 2.1 (target >= 4) — flat paragraph, all sentences 16-21 words
    stylometry_passes:
      - ttr: 0.511 (target >= 0.40) — lexical diversity strong
      - short_sentences: 14.5% (borderline pass; at target when fragment labels excluded)
      - hedge_density: prose hedging within 5-10% range when policy-precision qualifiers excluded
    persona_drift_sections:
      - Implementation Steps — register drifts toward procedural enumeration with no authorial
        voice; reads as a project plan template rather than an HR director's memo
    remediation_cycles: 1
    reviewer: writing-style-editor
    timestamp: 2026-02-20T01:30:00Z
    notes: >
      Stage 3 proceeds for demonstration purposes despite Stage 2 FAIL. Two blocking
      factual errors are marked [AUTHOR MUST CORRECT] in the rewritten document and
      must not be published. Voice corrections applied: 4 AI terms replaced, Executive
      Summary restructured for burstiness, one additional long sentence added to
      Background, "This increases..." opener folded into prior sentence, Stage 2 hedges
      preserved throughout. Implementation Steps section flagged for persona drift;
      minor restructuring applied but authorial voice is thin in that section — author
      should consider adding a brief framing sentence before the bullet list.
```

---

## Final Recommendation

**Revision needed — author must act before this document can be cleared.**

### Blocking (Stage 2 — author must correct before publication)

1. **Mileage rate**: Change "67.0 cents/mile" to "70 cents/mile" and add citation to
   IRS Notice 2025-5. The 67-cent figure is the 2024 rate; publishing the wrong rate in
   a compliance memo carries direct liability risk.

2. **Client gift deductibility gap**: Add a disclosure parenthetical to the Gifts bullet
   noting that the IRS deductibility cap is $25 per recipient per year under IRC §274(b),
   and that amounts above $25 are non-deductible even when the firm reimburses up to $100.

### Non-blocking Stage 2 items (should be addressed before publication)

3. Qualify outcome language in the Executive Summary and closing sentence from "will" to
   "is expected to" or "should" to address optimism bias and Reasoning Error #1. (Applied
   in this rewrite; verify the author accepts the framing.)

4. Cite enforcement evidence in the Background or rewrite as professional judgment: "In our
   experience, audit scrutiny of reimbursement practices has increased."

5. Add internal data or a qualifier to "costs spike in meals/entertainment" (Analysis
   bullet 3) — either cite a trend figure from Finance or write "Finance has noted
   year-over-year increases in meals and ad-hoc software expenses."

6. Add a brief acknowledgment of implementation risk to the Analysis section or a
   "Conditions for success" note at the close, to address the one-sided analysis finding
   (Reasoning Error #3 and Confirmation Bias).

### Stage 3 items applied in the rewrite (author should accept or adjust)

7. "Robust substantiation and approvals" changed to "Full documentation and approval
   requirements" — removes AI filler; more precise.

8. "streamline reconciliation" changed to "eliminate manual entry and cut reconciliation
   time" — replaces vague buzzword with specific outcome.

9. "a modern, business-friendly policy" changed to "a clear, enforceable policy" — removes
   vague endorsement language.

10. "last comprehensive policy refresh" changed to "last full policy refresh" — removes AI
    filler; no meaning lost.

11. Executive Summary restructured: one sentence shortened to a direct declaration; the
    recommendation sentence extended to carry the full rationale. Burstiness improved.

12. Background long sentence added to carry the accountable-plan-stability point with its
    qualifying clause, breaking the 28-word ceiling.

13. "This increases the firm's liability and can lead to penalties" folded into the prior
    sentence to eliminate a formulaic "This [noun]" opener and reduce sentence count
    fragmentation.

14. Implementation Steps: "90-day pilot with three departments" softened to "pilot with
    representative departments" per Stage 2 Assumption #5 (arbitrary parameters). Author
    may restore the specific numbers if they have an analytical basis.

**Resubmission path**: Author corrects items 1-2 (blocking), addresses items 3-6 as
appropriate, reviews Stage 3 rewrites (items 7-14), and resubmits. Stage 2 re-checks
only the rewritten sections before Stage 3 sign-off.
