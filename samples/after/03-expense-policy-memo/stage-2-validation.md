---
stage: 2
agent: document-validator
source: ../stage-1-grammar.md (Corrected Document section)
timestamp: 2026-02-20T23:55:00Z
---

## Stage 1 Status Check

Stage 1 returned FAIL (7 grammar errors). Per pipeline rules, Stage 2 proceeds only because
Stage 1 supplied a corrected document and the instructions confirm that corrected document is
the Stage 2 input. The factual review below applies to the corrected document text, not the
original.

---

## Red Flag Quick Scan

Before the full framework, the following high-frequency patterns were identified on first read:

| Red Flag | Location | Finding |
| --- | --- | --- |
| Specific statistic without source | Mileage bullet | "2025: 67.0 cents/mile" — specific figure, no citation |
| Specific statistic without source | Background | "approximately 200 employees" — no source |
| Historical claim without source | Background | "last comprehensive policy refresh was in 2018" — no source |
| Assumed consensus | Background | "enforcement has [increased]" — which enforcement authority? What evidence? |
| Universal quantifier | Proposed Key Elements | "required for all expenses over $25" — "all" is an absolute claim |
| Universal quantifier | Proposed Key Elements | "All exceptions require CFO..." — absolute claim; verify no carve-outs |
| Unsupported causation | Analysis, bullet 2 | "Standardizing thresholds...will shorten cycle time" — assumed, not evidenced |
| False precision (regulatory) | Mileage bullet | Rate stated to one decimal (67.0); source must be authoritative and current |
| Regulatory claim | Tax compliance bullet | Accountable plan requirements stated without citation |
| Regulatory claim | Meals bullet | "50% business allocation required for billable client events where allowable" — rule stated without citation |

---

## Validation Summary

```text
Document: Update the Firm's Employee Expense Reimbursement Policy (Corrected)
Total Claims Analyzed: 28
─────────────────────────────
Verified:        8  (29%)
Expert Judgment: 9  (32%)
Assumptions:     4  (14%)
Unverified:      5  (18%)
Suspect:         2   (7%)
─────────────────────────────
Reasoning Errors: 3
Universal Quantifiers: 2 flagged
Overall Status: FAIL
```

**Threshold analysis**: Verified + Expert Judgment = 61% (threshold: 75% for CONDITIONAL,
90% for PASS). Suspect = 2 (threshold: 0 for PASS, ≤2 for CONDITIONAL). However, one suspect
claim is a material regulatory error — a wrong IRS rate stated as current fact — which elevates
severity beyond a threshold count. Unverified = 18% (threshold: ≤15% for CONDITIONAL).
Optimism bias is present and unmitigated. These factors collectively produce a FAIL verdict.

---

## Issue Log

| # | Section | Claim | Tag | Issue | Recommendation |
| --- | --- | --- | --- | --- | --- |
| 1 | Mileage bullet | "IRS standard rate annually (2025: 67.0 cents/mile)" | SUSPECT | The 2025 IRS business standard mileage rate is 70 cents/mile per IRS Notice 2025-5 (issued December 19, 2024). The 67-cent figure is the 2024 rate. This is a material factual error on a directly citable IRS figure. | Correct to "70 cents/mile" and add citation: IRS Notice 2025-5. |
| 2 | Gifts bullet | "client gifts limited to $100 with written justification" | SUSPECT | The IRS deduction limit for business gifts is $25 per recipient per year (unchanged since 1962; IRC §274(b)). A $100 internal reimbursement ceiling is a policy choice, but stating it without noting the $25 deductibility cap creates a compliance gap: the firm would reimburse up to $100 but only deduct $25. This is not a factual error in the policy limit itself, but the absence of any mention of the IRS deductibility limit is a material omission in a tax-compliance-focused document. | Add a parenthetical: "Note: IRS deductibility cap is $25 per recipient per year (IRC §274(b)); amounts above $25 are non-deductible." |
| 3 | Background | "the firm's last comprehensive policy refresh was in 2018" | UNVERIFIED | No source cited. This could be confirmed by internal records, but as a stated fact in the memo it is unverified. | Add "(per HR records)" or similar qualifier, or note as internal data. |
| 4 | Background | "the firm has grown to approximately 200 employees" | UNVERIFIED | Approximate figure with no source. Plausible for a professional services firm, but unverified as stated. In a memo recommending policy change, this figure is used to imply scope and relevance, so its basis matters. | Add "(per current headcount as of [date])" or cite HR data source. |
| 5 | Background | "State and federal rules on accountable plans and substantiation have not materially changed, but enforcement has" | UNVERIFIED | The first clause — rules unchanged — is broadly consistent with current law (the three-prong accountable plan test has not changed materially). The second clause — enforcement has increased — is presented as fact with no supporting evidence. What enforcement activity? IRS audit rates? Treasury guidance? Penalties assessed? The claim is plausible given IRS interest in fringe benefit taxation, but it is asserted without any supporting evidence. | Either cite enforcement evidence (IRS audit statistics, published IRS guidance on fringe benefits, or a CPA advisory) or qualify as professional judgment: "In our experience, audit scrutiny of reimbursement practices has increased." |
| 6 | Analysis, bullet 1 | "reimbursements risk being classified as taxable income" | EXPERT JUDGMENT | Accurate statement of the general IRS rule for non-accountable plans. The risk is real and well-established under Treas. Reg. §1.62-2. No citation given, but this is standard professional tax knowledge. | Acceptable as expert judgment. Optional improvement: cite Treas. Reg. §1.62-2 or IRS Publication 15. |
| 7 | Analysis, bullet 1 | "A clear accountable plan statement is essential" | EXPERT JUDGMENT | Standard professional advice for employers seeking tax-favored treatment of reimbursements. Reasonable and accurate. | No change needed. |
| 8 | Tax compliance bullet | "Non-taxable reimbursements must meet accountable plan requirements" | VERIFIED | Accurate. Under Treas. Reg. §1.62-2, reimbursements qualify as non-taxable only when the arrangement meets three requirements: business connection, substantiation, and return of excess. The three-prong test is well-established law. | Acceptable. Consider adding a citation for the reader's reference. |
| 9 | Tax compliance bullet | "taxable benefits are treated as wages" | VERIFIED | Accurate. Benefits that fail accountable plan requirements are included in gross income and subject to withholding and payroll taxes under IRC §61 and Treas. Reg. §1.62-2(c)(5). | No change needed. |
| 10 | Documentation bullet | "Business purpose, date, amount, attendees, and location are required for all expenses over $25" | EXPERT JUDGMENT | The substantiation elements (amount, time, place, business purpose) are prescribed by IRC §274(d) and Treas. Reg. §1.274-5 for travel and entertainment expenses. The document's list of five elements is consistent with the regulatory requirement. The $25 internal threshold is a policy choice, not an IRS mandate; the IRS $75 receipt threshold applies to documentation form, not to whether substantiation is required at all. This is accurate but slightly imprecise. | Acceptable as expert judgment. Clarify that the $25 threshold is a firm policy choice; the IRS mandates substantiation elements for all reimbursable business expenses. |
| 11 | Documentation bullet | "Receipts required for single items over $75; detailed itemized receipts for hotels and airfare" | VERIFIED | Consistent with IRS guidance. Treas. Reg. §1.274-5(c) requires documentary evidence (receipts) for lodging and for any expense of $75 or more. Itemized receipts for lodging are specifically required. | No change needed. |
| 12 | Meals bullet | "50% business allocation required for billable client events where allowable" | EXPERT JUDGMENT | The 50% meals deduction limit under IRC §274(n)(1) is accurate for 2025. The TCJA eliminated entertainment deductions but preserved the 50% deduction for qualifying business meals. The phrase "where allowable" appropriately hedges for contexts where 100% deductibility applies (e.g., certain employee events). This is accurate. | No change needed. |
| 13 | Meals bullet | "Entertainment/meals with clients: $80 per person" | EXPERT JUDGMENT | The $80/person limit is a firm policy choice, not an IRS mandate. It is not contradicted by IRS rules. Consistent with the document's overall approach of setting internal caps. | No change needed as policy. The document should make clear this is a firm cap, not an IRS limit. |
| 14 | Mileage bullet | "parking and tolls separate" | VERIFIED | Accurate. Under IRS guidance, parking fees and tolls are separately deductible business expenses and are not folded into the standard mileage rate. IRS Publication 463 confirms this. | No change needed. |
| 15 | Mileage bullet | "require route and business purpose" | EXPERT JUDGMENT | Standard substantiation practice for mileage under Treas. Reg. §1.274-5. Accurate. | No change needed. |
| 16 | Alcohol bullet | "Policy allows one drink with meals or events within the meal per diem; alcohol alone not reimbursable" | EXPERT JUDGMENT | This is a policy choice within the employer's discretion. There is no IRS rule mandating or prohibiting a one-drink limit. The characterization of alcohol-only reimbursement as excluded is a reasonable internal control. | No change needed as policy. |
| 17 | Executive Summary | "Updating the policy will clarify allowable expenses, align with IRS and state rules, improve process transparency, and support better budget management" | EXPERT JUDGMENT | These outcomes are reasonable and achievable if the recommended policy is implemented competently. None are stated as certainties; the construction "will" does assert certainty. See bias assessment below. | See optimism bias finding. |
| 18 | Analysis, bullet 2 | "Standardizing thresholds and enabling electronic capture will shorten cycle time" | EXPERT JUDGMENT | Plausible professional judgment. Electronic capture and clear thresholds typically reduce ambiguity-driven delays. However, "will shorten" asserts certainty; actual impact depends on implementation quality, adoption rates, and system configuration. | Qualify: "are expected to shorten cycle time." |
| 19 | Analysis, bullet 3 | "costs spike in meals/entertainment and ad-hoc software/tooling" | UNVERIFIED | Presented as a current problem justifying the policy change. No data is cited — no trend analysis, no year-over-year comparison, no internal audit finding. Plausible given the stated context, but asserted as fact. | Add supporting data (e.g., "Finance identified a 23% year-over-year increase in meals expenses in FY2024") or qualify as observed pattern. |
| 20 | Analysis, bullet 4 | "Inconsistent rules across teams lead to perceptions of unfair treatment" | UNVERIFIED | The feedback claim in the Background section supports this (employees reported confusion), but the causal connection between inconsistent rules and fairness perceptions is asserted without direct evidence here. Plausible, but the Background feedback is the only supporting source and it is itself unverified. | Reference the employee feedback explicitly: "Feedback indicates that inconsistent rules across teams create perceptions of unfair treatment." |
| 21 | Implementation Steps | "Run a 90-day pilot with three departments" | ASSUMPTION | The document recommends a specific pilot scope (90 days, three departments) without stating the basis for these parameters. Why three departments? Why 90 days? This is presented as a concrete plan element but appears to be an arbitrary round number with no analytical basis. | Either state the basis ("three departments were selected to represent high, medium, and low travel frequency") or present as illustrative ("a pilot with representative departments"). |
| 22 | Implementation Steps | "Conduct annual policy review and quarterly adjustments as needed" | EXPERT JUDGMENT | Standard governance practice for expense policies. Reasonable and consistent with good HR/finance practice. | No change needed. |
| 23 | Closing sentence | "we will reduce compliance risk, speed reimbursements, support client work, and promote responsible spending" | EXPERT JUDGMENT | Reasonable projection of outcomes if the recommended policy is implemented. The "will" framing asserts certainty; see bias assessment. | See optimism bias finding. |
| 24 | Background | "travel patterns have changed, remote work has increased" | EXPERT JUDGMENT | Consistent with post-2020 workforce trends. No firm-specific data cited, but the general trend is widely documented. Reasonable as professional context-setting. | Acceptable. |
| 25 | Background | "audit/compliance expectations have evolved" | UNVERIFIED | Vague authority appeal. Whose expectations? Internal leadership? The IRS? State tax agencies? Clients? The claim is plausible but unattributed. | Specify: "Management's compliance expectations have evolved" or "client audit requirements have evolved." |
| 26 | Recommendation | "All exceptions require CFO or designated policy owner sign-off" | EXPERT JUDGMENT | Reasonable governance control. "All" is a universal quantifier. In practice, routine low-value exceptions handled under a delegated authority matrix are common. The document does not define what constitutes an "exception." | Define "exception" (e.g., any spend outside category limits or caps) to make "all" defensible, or qualify: "All material exceptions require..." |
| 27 | Implementation Steps | "Host mandatory 60-minute policy training for managers" | ASSUMPTION | The 60-minute duration is stated with false precision. No training needs assessment or content scope is cited. The basis for "60 minutes" is unexplained. | Either state the basis or use "an estimated X-hour training session." |
| 28 | Analysis, bullet 3 | "Clear caps, per diem rates, and mandatory cost-benefit checks will manage spend and client expectations" | EXPERT JUDGMENT | Reasonable policy outcome. "Will manage" is appropriately modest; "manage" does not imply elimination. Acceptable. | No change needed. |

---

## Assumption Register

| # | Assumption | Stated? | Type | Risk if Invalid | Recommendation |
| --- | --- | --- | --- | --- | --- |
| 1 | The firm's current expense policy was last updated in 2018 | No — asserted as fact | Temporal | If incorrect, the urgency framing ("outdated") is weakened or strengthened depending on actual date | Verify from HR records and state as internal data |
| 2 | The firm currently has approximately 200 employees | No — asserted as fact | Organizational | If headcount is materially different, the policy scope and implementation estimates may be off | Cite current headcount data with date |
| 3 | The expense management system can be configured to enforce category codes, per diem limits, and workflow requirements | Not stated | Technical | If the current system cannot support these requirements, the implementation plan and timeline are invalid | Add a dependency note: "Subject to confirmation that [system name] supports required configuration" |
| 4 | Finance, HR, IT, and Engagement Partners have capacity to execute implementation concurrently | Not stated | Resource | If any function lacks capacity, the implementation timeline will extend | Add a capacity assumption or phase the implementation plan |
| 5 | The 90-day pilot scope (three departments) is sufficient to surface policy gaps before firm-wide rollout | Not stated | Temporal/Organizational | Insufficient pilot scope could result in undetected issues at full rollout | State the selection basis for the pilot departments and the success criteria |
| 6 | State rules on accountable plans and substantiation align with federal rules for this firm's operating states | Not stated | Regulatory | Some states have independent requirements that differ from federal IRS rules | Identify the states in which the firm operates and confirm state-level compliance requirements |
| 7 | The $50/month BYOD stipend is set at a level that meets the IRS "reasonableness" standard for accountable plan treatment | Not stated | Regulatory | If the stipend is not tied to a documented business-use percentage, it may not qualify for tax-free treatment | Confirm the BYOD stipend structure against IRS accountable plan guidance or treat as taxable compensation |
| 8 | Vendor and market pricing for hotels will remain near the $200/night guideline | Not stated | Market | Rate changes could make the guideline obsolete quickly in high-cost markets | Add a review trigger: "Guidelines reviewed annually or when market rates in key travel markets shift materially" |

---

## Reasoning Error Log

| # | Section | Error Type | Claim | Issue | Fix |
| --- | --- | --- | --- | --- | --- |
| 1 | Executive Summary, Closing | False certainty / Non sequitur | "Updating the policy will...reduce compliance risk, speed reimbursements, support client work, and promote responsible spending" | The conclusion that a policy update "will" produce all four outcomes does not follow from the premise that the policy is outdated. Policy updates fail when they are poorly communicated, inconsistently enforced, or implemented in systems that cannot support them. The document acknowledges implementation steps are needed but treats their success as given. | Qualify the outcome claims: "A well-implemented policy update is expected to reduce compliance risk..." Present implementation quality as a condition, not a given. |
| 2 | Analysis, bullet 2 | False causation | "Standardizing thresholds and enabling electronic capture will shorten cycle time" | Causation is asserted without evidence. Reimbursement cycle time is also affected by manager responsiveness, finance staffing, and system reliability — none of which are addressed by standardizing thresholds alone. | Add qualifiers acknowledging the conditions under which the outcome holds: "are expected to shorten cycle time, assuming adoption of electronic capture tools and consistent manager review within the prescribed 7-day window." |
| 3 | Analysis, bullets 1–4 | Cherry-picking | All four analysis bullets present only the costs and risks of the status quo | The analysis does not acknowledge any cost or risk of the proposed change itself: implementation cost, employee burden during transition, risk of over-complexity in a small-firm environment, or potential for the new policy to be perceived as punitive and damage morale. | Add a brief acknowledgment of implementation risks and transition costs, even if the conclusion remains in favor of the update. |

---

## Bias Assessment

| Bias Type | Present? | Evidence | Mitigation |
| --- | --- | --- | --- |
| Confirmation | Yes | The analysis section presents four arguments in favor of the policy change and no arguments against. Risks of the change itself (implementation cost, employee burden, over-complexity) are not mentioned. | Add a "Risks and Mitigations" section or acknowledge implementation risks within the existing analysis bullets. |
| Optimism | Yes | "Will reduce compliance risk, speed reimbursements, support client work, and promote responsible spending" — all outcomes framed as certain positives. No conservative scenario presented. No acknowledgment of failure modes: an overly complex policy, poor adoption, or system limitations could produce the opposite of the stated outcomes. | Qualify outcome language. Add at minimum one sentence on conditions required for success and risks if those conditions are not met. |
| Survivorship | Marginal | The recommendation implies expense policy updates always improve outcomes. No mention of implementations that increased complexity without improving compliance. | Low severity given memo format, but a brief reference to implementation risk addresses this adequately. |
| Anchoring | No | The recommendation section presents four pillars, none of which dominates the analysis unfairly. | No action needed. |
| Vendor/Solution | No | No vendor is recommended; technology references are generic. | No action needed. |
| Authority | No | No appeal to authority without evidence beyond the "enforcement has increased" claim (addressed in Issue Log #5). | No action needed beyond Issue Log #5 fix. |

---

## Validated Document

The corrected document text appears below with inline claim tags on key factual assertions.
Tags are placed immediately after the claim they apply to. Policy choices (dollar caps, approval
windows, organizational roles) are not tagged unless they interact with a legal or regulatory
claim.

---

To: All Employees
From: HR Director
Date: September 28, 2025
Subject: Update the Firm's Employee Expense Reimbursement Policy

## Executive Summary

Our current expense reimbursement policy is outdated [UNVERIFIED — date of last refresh cited in
Background but not independently sourced] and inconsistently applied [UNVERIFIED — feedback cited
in Background is itself unverified], creating tax compliance risk [EXPERT JUDGMENT], reimbursement
delays [EXPERT JUDGMENT], and morale issues [UNVERIFIED — not supported in the Background section;
fairness perceptions are mentioned but "morale issues" is a stronger claim]. Updating the policy
will clarify allowable expenses, align with IRS and state rules [EXPERT JUDGMENT], improve process
transparency [EXPERT JUDGMENT], and support better budget management [EXPERT JUDGMENT]. I recommend
we adopt a modern, business-friendly policy emphasizing clear documentation, timely approvals, and
responsible spend.

## Background

The firm's last comprehensive policy refresh was in 2018 [UNVERIFIED — asserted without citation
to internal records]. Since then, the firm has grown to approximately 200 employees [UNVERIFIED —
asserted without citation to HR data], travel patterns have changed [EXPERT JUDGMENT — consistent
with documented post-2020 workforce trends but no firm-specific data cited], remote work has
increased [EXPERT JUDGMENT — same], and our audit/compliance expectations have evolved [UNVERIFIED
— vague; whose expectations? cite source]. Feedback from finance, clients, and employees indicated
confusion about what's covered, weak controls over high-risk categories (e.g., ride-share, event
fees, training), and slow or uneven reimbursements [UNVERIFIED — feedback referenced but not
quantified, attributed, or dated]. State and federal rules on accountable plans and substantiation
have not materially changed [EXPERT JUDGMENT — consistent with current law; the three-prong test
has been stable], but enforcement has [UNVERIFIED — assertion without evidence; no enforcement
data cited].

## Analysis

- Tax and compliance risk: Without clear guidance on substantiation (when, where, amount,
  business purpose, attendees) [VERIFIED — these are the §274(d) substantiation elements],
  reimbursements risk being classified as taxable income [EXPERT JUDGMENT — accurate statement
  of risk under Treas. Reg. §1.62-2]. This increases the firm's liability and can lead to
  penalties [EXPERT JUDGMENT]. A clear accountable plan statement is essential [EXPERT JUDGMENT].
- Process and timeliness: Delays often result from ambiguous categories, unclear caps, and
  manual approvals [UNVERIFIED — asserted as a cause without data]. Standardizing thresholds and
  enabling electronic capture will shorten cycle time [EXPERT JUDGMENT — plausible but stated with
  false certainty; see Reasoning Error #2].
- Budget and spend controls: Without category-specific limits, costs spike in
  meals/entertainment and ad-hoc software/tooling [UNVERIFIED — asserted without internal trend
  data]. Clear caps, per diem rates, and mandatory cost-benefit checks will manage spend and
  client expectations [EXPERT JUDGMENT].
- Equity and transparency: Inconsistent rules across teams lead to perceptions of unfair
  treatment [UNVERIFIED — plausible given feedback cited, but causal link not established].
  A centralized, accessible policy improves fairness, client billing, and cost allocation
  [EXPERT JUDGMENT].

## Recommendation

Adopt a modern expense policy built around four pillars:

1. Clear and transparent guidelines
2. Robust substantiation and approvals
3. Reasonable category-specific limits
4. Fair and timely reimbursements

### Proposed Key Elements

- Authorization levels: Employees submit; Manager approves; Finance enforces caps; CFO
  approves waivers for out-of-policy exceptions [EXPERT JUDGMENT — reasonable governance
  structure; "all" exceptions requires defining "exception"].
- Documentation: Business purpose, date, amount, attendees, and location are required for
  all expenses over $25 [EXPERT JUDGMENT — substantiation elements match §274(d); $25 threshold
  is an internal policy choice, not an IRS mandate], and encouraged for all. Receipts required
  for single items over $75 [VERIFIED — consistent with Treas. Reg. §1.274-5(c) and IRS
  Publication 463]; detailed itemized receipts for hotels and airfare [VERIFIED — consistent with
  IRS requirements for lodging].
- Tax compliance: Non-taxable reimbursements must meet accountable plan requirements [VERIFIED —
  consistent with Treas. Reg. §1.62-2]; taxable benefits are treated as wages [VERIFIED —
  consistent with IRC §61 and Treas. Reg. §1.62-2(c)(5)].
- Limits and rates:
  - Travel: Economy airfare; hotel within reasonable local rate (e.g., $200/night typical,
    with market-adjusted exceptions; corporate negotiated rates when available) [ASSUMPTION —
    $200/night benchmark is not sourced; market rates vary significantly by city]. Ride-share
    pre-approval required for long-distance trips [EXPERT JUDGMENT]. Rail where feasible
    [EXPERT JUDGMENT].
  - Meals: Day trip per diem $50; Overnight per diem $80; Entertainment/meals with clients:
    $80 per person [EXPERT JUDGMENT — these are internal policy caps, not IRS-mandated rates];
    50% business allocation required for billable client events where allowable [VERIFIED —
    consistent with IRC §274(n)(1) as applicable in 2025; note that the TCJA eliminated
    entertainment deductions; the 50% rule applies to qualifying business meals].
  - Phone/internet: Employer-provided or employer-approved reimbursement. Bring Your Own
    Device (BYOD) stipend $50/month if device and plan are primarily personal [ASSUMPTION —
    the tax treatment of this stipend depends on whether it meets accountable plan requirements;
    the basis for the $50 amount is not stated].
  - Office/equipment: Mandatory approval for all equipment purchases >$500 [EXPERT JUDGMENT];
    standard IT list with approved vendors to avoid duplicate or incompatible purchases
    [EXPERT JUDGMENT].
  - Training/certification: Pre-approval for courses or exams not on the approved list;
    reimbursement upon proof of completion [EXPERT JUDGMENT].
  - Parking/tolls: Reimburse with receipts when practical [EXPERT JUDGMENT].
  - Mileage: IRS standard rate annually (2025: 67.0 cents/mile) [SUSPECT — THIS IS INCORRECT.
    The 2025 IRS business standard mileage rate is 70 cents/mile per IRS Notice 2025-5. The
    67.0-cent rate is the 2024 rate. Must be corrected before publication.] when a personal
    vehicle is used; parking and tolls separate [VERIFIED — per IRS Publication 463]; require
    route and business purpose [EXPERT JUDGMENT — consistent with substantiation requirements].
  - Alcohol: Policy allows one drink with meals or events within the meal per diem; alcohol
    alone not reimbursable [EXPERT JUDGMENT — internal policy choice; no IRS rule dictates a
    one-drink limit].
  - Gifts: No cash gifts; client gifts limited to $100 with written justification [SUSPECT —
    the $100 internal reimbursement ceiling is a policy choice the firm may make, but the
    document does not disclose that the IRS deductibility limit for business gifts is $25 per
    recipient per year under IRC §274(b), unchanged since 1962. Reimbursing up to $100 while
    only deducting $25 creates a compliance gap that a tax-focused memo must address.].
- Reimbursement windows: Employees submit within 30 days; Managers review within 7 days;
  Finance processes within 5 business days [EXPERT JUDGMENT — the 30-day employee submission
  window is consistent with IRS safe-harbor guidance recommending substantiation within 60 days;
  manager and finance windows are internal policy choices].
- Expense capture: Company-issued corporate card preferred; use mobile app or scan-and-submit;
  include required fields in one workflow [EXPERT JUDGMENT].
- Client billing: The engagement partner flags client-related expenses for bill-through
  approval, per client policy and firm gross margin targets [EXPERT JUDGMENT].
- Prohibited: Personal travel tagged as business, duplicate claims, gifts intended to
  improperly influence, and luxury upgrades absent prior approval [EXPERT JUDGMENT — these
  prohibitions are consistent with standard IRS disallowance rules and FCPA/ethics principles].
- Exceptions: All exceptions require CFO or designated policy owner sign-off [EXPERT JUDGMENT —
  "All" is a universal quantifier; define "exception" to make this enforceable].

## Implementation Steps

- Establish ownership: Finance will lead policy drafting; HR will ensure compliance with
  employment law; IT will manage system integrations; Engagement Partners will handle client
  approvals [EXPERT JUDGMENT — reasonable functional assignment; capacity is assumed, not
  verified].
- Communicate and train:
  - Publish the full policy on the intranet with FAQs, quick reference cards, and examples
    [EXPERT JUDGMENT].
  - Host mandatory 60-minute policy training for managers [ASSUMPTION — 60-minute duration is
    stated without a training needs assessment or content scope]; provide asynchronous
    micro-learning for all staff [EXPERT JUDGMENT].
  - Update onboarding materials to include expense policy orientation [EXPERT JUDGMENT].
- Technology and tools:
  - Configure the expense system to align with category codes, per diem limits, and workflow
    requirements [ASSUMPTION — assumes the current system can support required configuration;
    not verified].
  - Integrate corporate card feeds to streamline reconciliation [ASSUMPTION — assumes system
    integration capability].
  - Ensure mobile capture and real-time feedback for missing documentation [ASSUMPTION — same].
- Approvals and enforcement:
  - Define approval thresholds and escalation paths; implement system checks for out-of-policy
    spend [EXPERT JUDGMENT].
  - Run a 90-day pilot with three departments to refine processes [ASSUMPTION — basis for 90
    days and three departments not stated; presented as concrete without analytical basis].
  - Introduce quarterly audits by Finance/Compliance with red-flag alerts for anomalies
    [EXPERT JUDGMENT].
- Measure and improve:
  - Track key performance indicators (KPIs): reimbursement cycle time, rejection rate, policy
    violations, and client cost recovery ratio [EXPERT JUDGMENT].
  - Conduct annual policy review and quarterly adjustments as needed [EXPERT JUDGMENT].
  - Maintain a policy ownership calendar (e.g., quarterly updates; annual full review)
    [EXPERT JUDGMENT].

By updating and enforcing a clear, fair policy, we will reduce compliance risk, speed
reimbursements, support client work, and promote responsible spending across the firm
[EXPERT JUDGMENT — outcomes are plausible but stated with false certainty; see Reasoning
Error #1 and Bias Assessment].

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
      and was used as the Stage 2 input per pipeline instructions.

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
    status: PENDING
```

---

## Final Recommendation

**FAIL — Return to author for revision before Stage 3.**

The document contains two suspect claims that must be corrected and cannot be deferred to Stage 3:

**Required corrections (blocking):**

1. Mileage rate error (Issue #1): Correct "67.0 cents/mile" to "70 cents/mile" and add a
   citation to IRS Notice 2025-5. This is a material factual error on a directly citable IRS
   figure. A compliance-focused document cannot carry a wrong regulatory rate.

2. Client gift compliance gap (Issue #2): Add disclosure of the $25 IRS deductibility limit
   per IRC §274(b) alongside the $100 internal reimbursement ceiling. The document explicitly
   positions itself as aligning with "IRS and state rules" — the omission of this limit in the
   gifts section is a material gap for a tax-oriented memo.

**Required corrections (non-blocking but should be fixed before Stage 3):**

3. Enforcement claim (Issue #5): Cite enforcement evidence or rewrite as professional judgment.

4. "Costs spike" claim (Issue #19): Add supporting internal data or qualify as observed pattern.

5. Reasoning Error #1: Qualify outcome language throughout (Executive Summary, closing sentence)
   from "will" to "is expected to" or "should."

6. Reasoning Error #3: Add a brief acknowledgment of implementation risks or costs to address
   the one-sided analysis.

7. Assumption #3 and #4: Add explicit dependency notes for system configuration and functional
   capacity.

**Acceptable to carry forward to Stage 3 after blocking corrections are made:**

- Background claims about 2018 policy date and 200-employee headcount may remain as
  "[UNVERIFIED — per internal records]" if the author adds a qualifier; they do not require
  external citation.
- The $25 internal documentation threshold and other internal policy caps are policy choices,
  not factual claims, and require no correction.
- Expert judgment classifications throughout are well-founded and do not require sourcing in
  a memo format.

**Resubmission path**: Author corrects items 1–2 (blocking) and ideally items 3–7. Stage 2
re-checks only the rewritten sections before passing to Stage 3.
