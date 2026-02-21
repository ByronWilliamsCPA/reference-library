---
stage: 1
agent: grammar-composition-editor
source: ../../before/03-expense-policy-memo.md
timestamp: 2026-02-20T23:14:17Z
---

## Grammar Report

```text
Grammar Errors:       7
Composition Issues:   2
Plain Language Flags: 2
AI-Mechanical Flags:  2
Non-Prose Issues:     4
Total:               17
```

**Status**: FAIL

Six or more grammar errors require the document to return to the author for revision before
proceeding to Stage 2. However, all errors are mechanical and correctable. The corrected
document below applies all fixes. If the author accepts the corrected text, Stage 2 may
proceed from the corrected version without a resubmission cycle.

---

## Issue Log

| # | Location | Category | Severity | Current Text | Issue | Suggested Fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Background, sentence 1 | Grammar | Error | "the firm's last comprehensive policy refresh was 2018" | Missing preposition before the year. "Was 2018" is ungrammatical; a date requires a linking preposition. | "was in 2018" |
| 2 | Background, sentence 2 | Grammar | Error | "travel patterns have changed, remote work increased, and our audit/compliance expectations have evolved" | Tense inconsistency in a parallel series. The first and third clauses use present-perfect ("have changed," "have evolved"); the second uses simple past ("increased"). | "remote work has increased" |
| 3 | Background, sentence 3 | Composition | Warning | "We received feedback from finance, clients, and employees indicating confusion about what's covered..." | Misplaced modifier. "Indicating" attaches grammatically to the nearest noun "employees," but the intended referent is "feedback." Restructure to put "indicating" next to "feedback." | "We received feedback indicating confusion about what's covered — from finance, clients, and employees alike." Or: "Feedback from finance, clients, and employees indicated confusion about what's covered..." |
| 4 | Analysis, bullet 4 | Composition | Warning | "A centralized, accessible policy improves fairness and improves client billing and cost allocation." | Redundant verb. "Improves" appears twice in the same clause. The second instance adds no new meaning; fold the objects into one series. | "A centralized, accessible policy improves fairness, client billing, and cost allocation." |
| 5 | Proposed key elements, Tax compliance bullet | Grammar | Error | "taxable benefits treated as wages" | Sentence fragment. The clause lacks a finite verb. In a formal memo, an independent clause requires a verb. | "taxable benefits are treated as wages" |
| 6 | Proposed key elements, Authorization levels bullet | Grammar | Error | "CFO waiver for out-of-policy exceptions" | Broken parallel structure. The first three items use subject-verb pairs ("Employees submit," "Manager approves," "Finance enforces caps"). The fourth item is a noun phrase, breaking the pattern. | "CFO approves waivers for out-of-policy exceptions" |
| 7 | Proposed key elements, Expense capture bullet | Grammar | Error | "Company issued corporate card preferred" | Missing hyphen in compound modifier. "Company-issued" modifies "corporate card" and requires a hyphen as a compound adjective preceding the noun. | "Company-issued corporate card preferred" |
| 8 | Proposed key elements, Gifts bullet | Grammar | Error | "Gifts/gifts:" | Repeated word — "gifts" appears twice in the label. Likely a drafting typo. | "Gifts:" |
| 9 | Proposed key elements, Client billing bullet | AI-Mechanical | Warning | "Client-related expenses flagged for possible bill-through or approval by engagement partner, ensuring compliance with client policy and firm gross margin targets." | Gerund phrase padding. The trailing participial phrase ", ensuring compliance with client policy and firm gross margin targets" is appended to a passive main clause and restates the implied purpose of flagging expenses rather than adding specifics. Also, no actor is stated for "flagged." | Rewrite to active voice and remove the padding: "The engagement partner flags client-related expenses for bill-through approval, per client policy and firm gross margin targets." |
| 10 | Analysis, bullet 1 | AI-Mechanical | Note | "reimbursements risk classification as taxable income" | Nominalization. "Classification" converts the verb "classify" into a noun, hiding the action. The verb form is clearer. | "reimbursements risk being classified as taxable income" |
| 11 | Implementation Steps, Establish ownership bullet | Grammar | Error | "Finance will lead policy drafting; HR ensures compliance with employment law; IT for integrations; Engagement Partners for client approvals." | Two errors: (a) tense inconsistency — "Finance will lead" (future) followed by "HR ensures" (present); (b) broken parallel structure — the first two items are subject-verb pairs, but "IT for integrations" and "Engagement Partners for client approvals" are noun phrases. | "Finance will lead policy drafting; HR will ensure compliance with employment law; IT will manage system integrations; Engagement Partners will handle client approvals." |
| 12 | Proposed key elements, BYOD bullet | Plain Language | Warning | "BYOD stipend $50/month..." | Acronym undefined. BYOD (Bring Your Own Device) is not expanded on first use in this document. Define it. | "Bring Your Own Device (BYOD) stipend..." |
| 13 | Implementation Steps, Measure and improve sub-bullet | Plain Language | Warning | "Track KPIs: reimbursement cycle time..." | Acronym undefined. KPI (Key Performance Indicator) is not expanded on first use. | "Track key performance indicators (KPIs): reimbursement cycle time..." |
| 14 | All section headers | Non-Prose | Error | "Executive Summary", "Background", "Analysis", "Recommendation", "Proposed key elements", "Implementation Steps" | Heading hierarchy absent. All section headers are plain bold text, not markdown headings. The document has no H1 and no heading-level markup. This breaks screen-reader accessibility (WCAG 1.3.1) and makes heading hierarchy unverifiable. Convert to markdown headings. | Use `#` for document title (Subject line context), `##` for major sections (Executive Summary, Background, Analysis, Recommendation, Implementation Steps), and `###` for subsections (Proposed key elements). |
| 15 | Proposed key elements header | Non-Prose | Error | "Proposed key elements" | Inconsistent capitalization and heading level. All other section headers capitalize both major words ("Executive Summary," "Implementation Steps"). This header uses lowercase "key elements" and follows the Recommendation section without a clear hierarchical relationship. | Either promote to a parallel `##` heading as "Proposed Key Elements" or demote explicitly to `###` as a subsection of Recommendation. Capitalize to match other headers. |
| 16 | Recommendation, numbered list | Non-Prose | Note | "1) Clear and transparent guidelines..." | Non-standard list numbering. Uses parenthesis-suffix style (1) 2) 3) 4)) rather than standard markdown ordered list notation (1. 2. 3. 4.). This may not render as an ordered list in all markdown processors. | "1. Clear and transparent guidelines" |
| 17 | Background, sentence 3 (full) | Non-Prose | Note | "We received feedback from finance, clients, and employees indicating confusion about what's covered, weak controls over high-risk categories (e.g., ride-share, event fees, training), and slow or uneven reimbursements." | Sentence carries three distinct types of feedback in one clause, making it difficult to scan. Advisory: consider a short list. Stage 3 may retain for voice reasons. | Split into: "We received feedback indicating: (1) confusion about covered expenses, (2) weak controls over high-risk categories (e.g., ride-share, event fees, training), and (3) slow or uneven reimbursements." |

---

## Corrected Document

> All changes from the issue log are applied inline. Changed text is not marked; the
> corrected document is the clean handoff version for Stage 2. See the issue log above
> for the location and rationale of each change.

---

To: All Employees
From: HR Director
Date: September 28, 2025
Subject: Update the Firm's Employee Expense Reimbursement Policy

## Executive Summary

Our current expense reimbursement policy is outdated and inconsistently applied, creating tax
compliance risk, reimbursement delays, and morale issues. Updating the policy will clarify
allowable expenses, align with IRS and state rules, improve process transparency, and support
better budget management. I recommend we adopt a modern, business-friendly policy emphasizing
clear documentation, timely approvals, and responsible spend.

## Background

The firm's last comprehensive policy refresh was in 2018. Since then, the firm has grown to
approximately 200 employees, travel patterns have changed, remote work has increased, and our
audit/compliance expectations have evolved. Feedback from finance, clients, and employees
indicated confusion about what's covered, weak controls over high-risk categories (e.g.,
ride-share, event fees, training), and slow or uneven reimbursements. State and federal rules
on accountable plans and substantiation have not materially changed, but enforcement has.

## Analysis

- Tax and compliance risk: Without clear guidance on substantiation (when, where, amount,
  business purpose, attendees), reimbursements risk being classified as taxable income. This
  increases the firm's liability and can lead to penalties. A clear accountable plan statement
  is essential.
- Process and timeliness: Delays often result from ambiguous categories, unclear caps, and
  manual approvals. Standardizing thresholds and enabling electronic capture will shorten
  cycle time.
- Budget and spend controls: Without category-specific limits, costs spike in
  meals/entertainment and ad-hoc software/tooling. Clear caps, per diem rates, and mandatory
  cost-benefit checks will manage spend and client expectations.
- Equity and transparency: Inconsistent rules across teams lead to perceptions of unfair
  treatment. A centralized, accessible policy improves fairness, client billing, and cost
  allocation.

## Recommendation

Adopt a modern expense policy built around four pillars:

1. Clear and transparent guidelines
2. Robust substantiation and approvals
3. Reasonable category-specific limits
4. Fair and timely reimbursements

### Proposed Key Elements

- Authorization levels: Employees submit; Manager approves; Finance enforces caps; CFO
  approves waivers for out-of-policy exceptions.
- Documentation: Business purpose, date, amount, attendees, and location are required for all
  expenses over $25, and encouraged for all. Receipts required for single items over $75;
  detailed itemized receipts for hotels and airfare.
- Tax compliance: Non-taxable reimbursements must meet accountable plan requirements; taxable
  benefits are treated as wages.
- Limits and rates:
  - Travel: Economy airfare; hotel within reasonable local rate (e.g., $200/night typical,
    with market-adjusted exceptions; corporate negotiated rates when available). Ride-share
    pre-approval required for long-distance trips. Rail where feasible.
  - Meals: Day trip per diem $50; Overnight per diem $80; Entertainment/meals with clients:
    $80 per person; 50% business allocation required for billable client events where allowable.
  - Phone/internet: Employer-provided or employer-approved reimbursement. Bring Your Own
    Device (BYOD) stipend $50/month if device and plan are primarily personal.
  - Office/equipment: Mandatory approval for all equipment purchases >$500; standard IT list
    with approved vendors to avoid duplicate or incompatible purchases.
  - Training/certification: Pre-approval for courses or exams not on the approved list;
    reimbursement upon proof of completion.
  - Parking/tolls: Reimburse with receipts when practical.
  - Mileage: IRS standard rate annually (2025: 67.0 cents/mile) when a personal vehicle is
    used; parking and tolls separate; require route and business purpose.
  - Alcohol: Policy allows one drink with meals or events within the meal per diem; alcohol
    alone not reimbursable.
  - Gifts: No cash gifts; client gifts limited to $100 with written justification.
- Reimbursement windows: Employees submit within 30 days; Managers review within 7 days;
  Finance processes within 5 business days.
- Expense capture: Company-issued corporate card preferred; use mobile app or scan-and-submit;
  include required fields in one workflow.
- Client billing: The engagement partner flags client-related expenses for bill-through
  approval, per client policy and firm gross margin targets.
- Prohibited: Personal travel tagged as business, duplicate claims, gifts intended to
  improperly influence, and luxury upgrades absent prior approval.
- Exceptions: All exceptions require CFO or designated policy owner sign-off.

## Implementation Steps

- Establish ownership: Finance will lead policy drafting; HR will ensure compliance with
  employment law; IT will manage system integrations; Engagement Partners will handle client
  approvals.
- Communicate and train:
  - Publish the full policy on the intranet with FAQs, quick reference cards, and examples.
  - Host mandatory 60-minute policy training for managers; provide asynchronous micro-learning
    for all staff.
  - Update onboarding materials to include expense policy orientation.
- Technology and tools:
  - Configure the expense system to align with category codes, per diem limits, and workflow
    requirements.
  - Integrate corporate card feeds to streamline reconciliation.
  - Ensure mobile capture and real-time feedback for missing documentation.
- Approvals and enforcement:
  - Define approval thresholds and escalation paths; implement system checks for out-of-policy
    spend.
  - Run a 90-day pilot with three departments to refine processes.
  - Introduce quarterly audits by Finance/Compliance with red-flag alerts for anomalies.
- Measure and improve:
  - Track key performance indicators (KPIs): reimbursement cycle time, rejection rate, policy
    violations, and client cost recovery ratio.
  - Conduct annual policy review and quarterly adjustments as needed.
  - Maintain a policy ownership calendar (e.g., quarterly updates; annual full review).

By updating and enforcing a clear, fair policy, we will reduce compliance risk, speed
reimbursements, support client work, and promote responsible spending across the firm.

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
      All errors are mechanical and correctable. Corrected document is provided
      above and may be used as the Stage 2 input if the author accepts the changes,
      avoiding a resubmission cycle. Primary error types: missing preposition,
      tense inconsistency, sentence fragment, repeated word typo, missing hyphen
      in compound modifier, broken parallel structure (two instances). Non-prose
      issues include absent heading hierarchy throughout. No pervasive AI-mechanical
      pattern accumulation detected; two isolated flags (gerund padding, one
      nominalization).

  stage_2_validation:
    status: PENDING

  stage_3_style:
    status: PENDING
```
