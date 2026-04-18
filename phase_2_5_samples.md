# Phase 2.5 Sample Package

Generated: 2026-04-18
Source repo: ByronWilliamsCPA/reference-library
Commit SHA: 1bfd7ea

## Inventory Summary

- Total candidates scouted: 15 prose files under `samples/` (5 `before/*.md`, 5 `after/*/stage-3-voice.md`, 5 `after/*/recap.md`); all other Markdown in the repo is reference-rule or agent-definition material, not prose.
- Samples selected: 8 (H=0, S=4, U=4, X=0)
- Total selected word count: 4177
- Excluded for confidentiality: 0
- Excluded for size or scope:
  - `samples/before/01-paragraph-summary.md and its stage-3 companion` — 163-word and 209-word bodies fall below the 300-word floor specified in the Phase 2.5 guardrails. Most free-tier detectors also require 250+ words.

### Classification Note

The repo contains no human-authored (pre-AI) baseline prose. The samples/ directory is built exclusively from minimax/minimax-m2 outputs to expose AI patterns for the editing pipeline to catch. That design choice is documented in samples/README.md. The package therefore ships with zero bucket-H samples; the external detector study must source human baselines from outside this repo if false-positive testing is required. Buckets S and U carry shared topics so the external tool can compare pre-edit versus post-edit scores on matched text.

### Confidentiality Pre-Screen

All eight selected samples are from samples/before and samples/after in the reference-library repo. They were generated via the committed scripts/generate_before_samples.py against an OpenRouter model with generic topic prompts. None contains real client names, employee names, taxpayer identifiers, account details, dollar figures tied to real engagements, or OST-internal codenames. The expense-memo sample references 'the firm' generically. The client-status email uses 'Key Sponsor' as a placeholder and a bracketed [Your Name] closing block. No PII redaction needed.

---

## Sample 01 — Client Status Email — Unedited AI Output
- **Classification:** U
- **Source path:** samples/before/02-client-status-email.md
- **Word count:** 315
- **Domain / register:** Business correspondence (management-consulting status email to a manufacturing client, SME role prompt)
- **Excerpt note:** Full body

Subject: Project Status Update – Operational Efficiency Review (Month 4 of 6)

Dear Team,

We are pleased to report significant progress on our 6-month Operational Efficiency Review, now in month 4. We have completed the diagnostic phase, including value stream mapping for our main product families, baseline OEE and throughput metrics across assembly and machining lines, and initial root-cause analysis of cycle time variability and waste pockets. We executed two targeted kaizen events that delivered quick wins in line balancing and changeover time reduction. Results from the automation pilot on Line 3 show an estimated 18% throughput improvement with stable quality; these learnings will inform the scale-up approach.

While overall trajectory is strong, we are managing three risks. Data reliability from legacy ERP systems may delay final baseline validation; we are implementing an end-of-month audit of data sources and a backup extraction process. Cross-functional resource availability remains tight for rapid pilot scaling; we are formalizing commitments through a capacity matrix reviewed at our steering meeting. Organizational change readiness is moderate and requires stronger sponsorship communication; we will align a one-paged operating model and change narrative with your leaders to ensure sustainable adoption.

Next steps for the next four weeks include finalizing the prioritized list of efficiency opportunities (ROI and payback per initiative), running two additional pilots in Packaging and Receiving to expand the automation scope, and hosting the executive steering meeting in Month 5 Week 2 with recommended investment options and timeline. We will also conduct change workshops for frontline teams and operations supervisors to support adoption and to embed performance routines around takt time adherence, preventive maintenance, and WIP reduction.

Please confirm Key Sponsor availability for the steering meeting and let us know any additional items to include. Thank you for your continued collaboration; we remain confident the final recommendations will deliver measurable operational gains.

Best regards,

[Your Name]
[Your Title]
[Company Name]
[Contact Information]

---

## Sample 02 — Client Status Email — System-Edited Rewrite
- **Classification:** S
- **Source path:** samples/after/02-client-status-email/stage-3-voice.md
- **Word count:** 379
- **Domain / register:** Business correspondence (same topic and register as the unedited companion, run through the three-stage editing pipeline)
- **Excerpt note:** Full body

Subject: Project Status Update: Operational Efficiency Review (Month 4 of 6)

Dear Team,

Month four is on schedule. We completed the diagnostic phase -- value stream mapping across
the main product families, OEE and throughput baselines across assembly and machining, and
root-cause analysis of cycle time variability and waste pockets. Two kaizen events produced
[AUTHOR: quantify if data available, e.g., "a 12-minute reduction in changeover time on
Line 2" -- if not available, retain directional: "early improvements in line balancing and
changeover time"]. The Line 3 automation pilot shows [AUTHOR: if measured, replace
"an estimated" with "a measured"] 18% throughput improvement with no quality degradation
[AUTHOR: confirm "stable quality" definition and measurement period per Stage 2 Issue Log #1];
those results will shape the validation approach for the next two pilots.

Three risks are in active management. Data reliability from the legacy ERP systems may push
final baseline validation past the current schedule; we are running an end-of-month source
audit with a backup extraction process standing by. Resource availability is the tighter
constraint -- cross-functional capacity for rapid pilot scaling remains limited, and we are
formalizing commitments through a capacity matrix before the steering meeting. Change
readiness [AUTHOR: add basis per Stage 2 Issue Log #2, e.g., "assessed through facilitator
observation during kaizen events"] is moderate; we will work with your operations leaders
on a one-page operating model and change narrative to build the foundation before the
workshops begin.

Over the next four weeks we will finalize the prioritized opportunity list with ROI and
payback estimates per initiative, run pilots in Packaging and Receiving to test whether
the Line 3 results generalize to those line configurations [per Stage 2 Reasoning Error #2
-- reframed as validation, not expansion], and bring recommended investment options and a
timeline to the Month 5 Week 2 steering meeting. Frontline change workshops and supervisor
sessions will run in parallel to embed takt time adherence, preventive maintenance, and
WIP reduction routines.

Please confirm Key Sponsor [AUTHOR: confirm capitalization against engagement contract per
Stage 2 Issue Log #5] availability for the steering meeting and flag any agenda items you
want added. The next four weeks are the pivot from diagnosis to decisions; we will have the
analysis ready.

Best regards,

[Your Name]
[Your Title]
[Company Name]
[Contact Information]

---

## Sample 03 — Expense Policy Memo — Unedited AI Output
- **Classification:** U
- **Source path:** samples/before/03-expense-policy-memo.md
- **Word count:** 637
- **Domain / register:** Policy memo (HR, tax compliance, reimbursement rules; SME role prompt)
- **Excerpt note:** Excerpted: leading paragraphs only, full paragraphs kept intact

To: All Employees  
From: HR Director  
Date: September 28, 2025  
Subject: Update the Firm’s Employee Expense Reimbursement Policy

Executive Summary
Our current expense reimbursement policy is outdated and inconsistently applied, creating tax compliance risk, reimbursement delays, and morale issues. Updating the policy will clarify allowable expenses, align with IRS and state rules, improve process transparency, and support better budget management. I recommend we adopt a modern, business-friendly policy emphasizing clear documentation, timely approvals, and responsible spend.

Background
The firm’s last comprehensive policy refresh was 2018. Since then, the firm has grown to approximately 200 employees, travel patterns have changed, remote work increased, and our audit/compliance expectations have evolved. We received feedback from finance, clients, and employees indicating confusion about what’s covered, weak controls over high-risk categories (e.g., ride-share, event fees, training), and slow or uneven reimbursements. State and federal rules on accountable plans and substantiation have not materially changed, but enforcement has.

Analysis
- Tax and compliance risk: Without clear guidance on substantiation (when, where, amount, business purpose, attendees), reimbursements risk classification as taxable income. This increases the firm’s liability and can lead to penalties. A clear accountable plan statement is essential.
- Process and timeliness: Delays often result from ambiguous categories, unclear caps, and manual approvals. Standardizing thresholds and enabling electronic capture will shorten cycle time.
- Budget and spend controls: Without category-specific limits, costs spike in meals/entertainment and ad-hoc software/tooling. Clear caps, per diem rates, and mandatory cost-benefit checks will manage spend and client expectations.
- Equity and transparency: Inconsistent rules across teams lead to perceptions of unfair treatment. A centralized, accessible policy improves fairness and improves client billing and cost allocation.

Recommendation
Adopt a modern expense policy built around four pillars:
1) Clear and transparent guidelines  
2) Robust substantiation and approvals  
3) Reasonable category-specific limits  
4) Fair and timely reimbursements

Proposed key elements
- Authorization levels: Employees submit; Manager approves; Finance enforces caps; CFO waiver for out-of-policy exceptions.
- Documentation: Business purpose, date, amount, attendees, and location are required for all expenses over $25, and encouraged for all. Receipts required for single items over $75; detailed itemized receipts for hotels and airfare.
- Tax compliance: Non-taxable reimbursements must meet accountable plan requirements; taxable benefits treated as wages.
- Limits and rates:
  - Travel: Economy airfare; hotel within reasonable local rate (e.g., $200/night typical, with market-adjusted exceptions; corporate negotiated rates when available). Ride-share pre-approval required for long-distance trips. Rail where feasible.
  - Meals: Day trip per diem $50; Overnight per diem $80; Entertainment/meals with clients: $80 per person; 50% business allocation required for billable client events where allowable.
  - Phone/internet: Employer-provided or employer-approved reimbursement. BYOD stipend $50/month if device and plan are primarily personal.
  - Office/equipment: Mandatory approval for all equipment purchases >$500; standard IT list with approved vendors to avoid duplicate or incompatible purchases.
  - Training/certification: Pre-approval for courses or exams not on the approved list; reimbursement upon proof of completion.
  - Parking/tolls: Reimburse with receipts when practical.
  - Mileage: IRS standard rate annually (2025: 67.0 cents/mile) when a personal vehicle is used; parking and tolls separate; require route and business purpose.
  - Alcohol: Policy allows one drink with meals or events within the meal per diem; alcohol alone not reimbursable.
  - Gifts/gifts: No cash gifts; client gifts limited to $100 with written justification.
- Reimbursement windows: Employees submit within 30 days; Managers review within 7 days; Finance processes within 5 business days.
- Expense capture: Company issued corporate card preferred; use mobile app or scan-and-submit; include required fields in one workflow.
- Client billing: Client-related expenses flagged for possible bill-through or approval by engagement partner, ensuring compliance with client policy and firm gross margin targets.
- Prohibited: Personal travel tagged as business, duplicate claims, gifts intended to improperly influence, and luxury upgrades absent prior approval.
- Exceptions: All exceptions require CFO or designated policy owner sign-off.

---

## Sample 04 — Expense Policy Memo — System-Edited Rewrite
- **Classification:** S
- **Source path:** samples/after/03-expense-policy-memo/stage-3-voice.md
- **Word count:** 439
- **Domain / register:** Policy memo (same topic, post-pipeline; retains two [AUTHOR MUST CORRECT] flags on mileage rate and gift-cap disclosure as residual factual items)
- **Excerpt note:** Excerpted: leading paragraphs only, full paragraphs kept intact

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

---

## Sample 05 — Onboarding Proposal — Unedited AI Output
- **Classification:** U
- **Source path:** samples/before/04-onboarding-proposal.md
- **Word count:** 503
- **Domain / register:** Internal proposal (regional accounting firm new-hire program, no system prompt)
- **Excerpt note:** Full body

## Internal Proposal: Restructured New‑Hire Onboarding Program

We propose a revitalized onboarding program designed to compress ramp time, reduce risk, and strengthen the culture of a regional accounting firm. The plan focuses on a structured 90‑day path that begins with firm foundations and rapidly builds toward job‑ready proficiency under close coaching and shared learning.

The current onboarding experience varies across offices and service lines, and new hires often feel adrift during the first quarter. New accountants receive inconsistent guidance on basic standards, unfamiliar clients, and firm policies, which delays chargeable hours, burdens senior staff with repetitive questions, and increases turnover. Partners report uneven expectations between client teams, while associates frequently cite unclear advancement benchmarks. These patterns reflect a fragmented approach rather than a deliberate learning journey.

Our solution introduces a phased, outcomes‑focused program that starts with a two‑day integration summit covering firm values, compliance, client service standards, and timekeeping basics. In week one, associates complete core modules on tax and audit methodologies, document review workflows, and tools such as firm knowledge bases and practice management systems. A digital playbook establishes role‑based competencies and checklists mapped to typical tasks. Within the first month, each new hire is paired with a trained buddy for 12 weeks and assigned a coach from a senior associate or manager. Weekly office hours are held by the training manager to address issues, share quick‑wins, and reinforce best practices. Chargeable training hours are scheduled and monitored to avoid overburdening clients while providing supervised learning on real files. By day 45, associates should demonstrate proficiency in a subset of standard procedures; by day 90, they complete a skills audit and a client‑ready readiness review with their manager, identifying any gaps that require targeted support or mentorship.

We expect early and measurable benefits from this plan. Associates typically reach billable levels earlier, increasing utilization and reducing early‑stage losses associated with low chargeable time. Fewer errors and rework improve the firm’s risk profile and reputation with clients. Buddies develop supervisory capability, strengthening the bench of future managers. The clarity of role expectations and a predictable cadence of support enhance engagement and reduce first‑year attrition. Knowledge captured in the playbook standardizes quality and makes training scalable across offices.

Implementation begins with a cross‑functional task force—HR, learning and development, IT, practice leaders, and three coaches—tasked with drafting the curriculum, digital playbook, and competency matrix. Training spaces and virtual tools will be configured within four weeks. We will pilot the program with the next two cohorts, tracking milestones at 30, 45, and 90 days and gathering feedback through pulse surveys and retrospective sessions. Success will be measured by shortened time to billable proficiency, reduced first‑year turnover, fewer defects and chargebacks, improved manager workload balance, and increased client satisfaction. After refinements from the pilot, the program rolls out firmwide by the following quarter, with ongoing governance by L&D and quarterly audits by the partners to ensure effectiveness and alignment with our standards.

---

## Sample 06 — Onboarding Proposal — System-Edited Rewrite
- **Classification:** S
- **Source path:** samples/after/04-onboarding-proposal/stage-3-voice.md
- **Word count:** 683
- **Domain / register:** Internal proposal (same topic, post-pipeline; contains one explicit [AUTHOR TO COMPLETE] placeholder block preserved as the repo committed it)
- **Excerpt note:** Excerpted: leading paragraphs only, full paragraphs kept intact

## Internal Proposal: Restructured New-Hire Onboarding Program

We propose a new onboarding program for the firm, structured around a 90-day path that begins
with firm foundations and builds toward job-ready proficiency under close coaching and shared
learning. The goals are concrete: compress ramp time, reduce risk, and strengthen the culture
of a regional accounting firm where talent development has lagged program design.

The current experience varies across offices and service lines. New hires often feel adrift
during the first quarter, and the pattern is consistent enough that it shows up in exit
interviews and partner feedback alike. New accountants receive inconsistent guidance on basic
standards, unfamiliar clients, and firm policies, which delays chargeable hours, burdens senior
staff with repetitive questions, and drives turnover that the firm has not yet measured but
clearly bears. Partners report uneven expectations among client teams, while associates
frequently cite unclear advancement benchmarks. These patterns reflect a fragmented approach
rather than a deliberate learning journey.

The proposed program is phased around three proficiency milestones at days 30, 45, and 90.
It opens with a two-day integration summit covering firm values, compliance, client service
standards, and timekeeping basics. In week one, associates complete core modules on tax and
audit methodologies, document review workflows, and tools such as firm knowledge bases and
practice management systems. A digital playbook establishes role-based competencies and
checklists mapped to typical tasks. Within the first month, each new hire is paired with a
trained buddy for twelve weeks and assigned a coach who is a senior associate or manager; buddy
preparation includes a defined orientation session covering feedback skills, confidentiality,
and escalation protocols. The training manager holds weekly office hours to address issues,
share quick wins, and reinforce best practices. Chargeable training hours are scheduled and
monitored; associates receive supervised learning on real files without overburdening clients.
By day 45, associates should demonstrate proficiency in a subset of standard procedures. By
day 90, they complete a skills audit and a client-readiness review with their manager,
identifying any gaps that require targeted support or mentorship.

We expect the program to produce measurable improvements across several dimensions, though
specific magnitudes will depend on pilot results. The most direct benefit we anticipate is
faster time to billable proficiency: associates who complete core methodology modules in week
one and supervised real-file work from month one are expected to reach chargeable capacity
earlier than the current average, though the pilot will establish the baseline needed to
quantify the gap. Supervised work and competency-based checkpoints are also designed to reduce
the errors and rework that generate chargebacks and client friction, though error-rate
improvement will be confirmed through pilot tracking before being stated as a program outcome.
The buddy structure serves a secondary purpose: senior associates who take on the role gain
early supervisory experience, and the program is designed with that development arc in mind,
not just associate integration. Whether that translates into a measurable contribution to
manager readiness will be one of the pilot's secondary questions. On retention, the
organizational behavior literature consistently links role clarity and structured support to
lower first-year attrition in professional services; this program is designed to provide both,
and the pilot will let us test whether that holds at our firm. The digital playbook is a
design choice with a specific intent: to reduce reliance on individual-office variation and
make firmwide rollout feasible, not just replication of the pilot.

**Risk acknowledgment**: The program depends on assumptions that could affect outcomes.
Buddy and coach participation works only if those staff have sufficient capacity alongside
their billable obligations; participation should be limited to associates and managers below a
defined utilization threshold. Partner engagement in quarterly governance audits is planned but
not yet confirmed as a standing commitment. And pilot results from two cohorts may be
directionally useful but not statistically conclusive, particularly if the cohorts are small
or drawn from a single office or service line; cohort size and composition should be stated
before launch. If early results are mixed, the program design should be refined before a third
cohort rather than rolled out firmwide on a fixed timeline.

---

## Sample 07 — Workforce Planning Analysis — Unedited AI Output
- **Classification:** U
- **Source path:** samples/before/05-workforce-planning-analysis.md
- **Word count:** 572
- **Domain / register:** Analytical essay (automation and mid-market professional-services workforce planning, no system prompt)
- **Excerpt note:** Full body

Automation is altering workforce planning in mid-market professional services by changing how output is measured, how work is sequenced, and where human judgment delivers differentiation. Document intelligence can summarize engagements and perform reconciliations in minutes rather than days; workflow orchestration and robotic process automation can move tickets through repeatable checkpoints without delays tied to human handoffs; and analytics platforms surface leading indicators that improve forecasting and resource allocation. As throughput rises without proportional headcount growth, planning shifts from filling roles to managing utilization and rework, because capacity is increasingly defined by system bottlenecks rather than FTEs. The result is a planning model that emphasizes cycle-time reduction, quality bands, and compliance guardrails, while treating hours as a derivative rather than the primary currency of productivity.

These productivity gains propagate into role design and skill evolution, because automation displaces routine tasks yet expands the demand for judgment, data fluency, and client-adjacent advisory work. As standard audits, legal research, and basic design are automated, hybrid roles such as automation analyst, data steward, and client success manager emerge alongside traditional experts who must now interpret model outputs, challenge assumptions, and govern the systems they rely on. Firms therefore redesign career ladders to include data literacy as a baseline competence and embed cross-functional squads where analysts, technologists, and domain specialists collaborate under agile governance; at the same time, they invest in prompt engineering and model supervision training to ensure outputs remain reliable and ethically sound. Planning thus becomes forward-looking competence mapping rather than pure headcount forecasting, because the marginal worker is not simply an analog replacement but a new combination of human insight and supervised automation.

The talent market responds in kind, because firms are no longer competing only for domain expertise but for candidates who can orchestrate technology alongside client engagement. Recruitment strategies prioritize data and automation skills while maintaining domain proficiency, prompting firms to cultivate internal pipelines through apprenticeships, rotational programs, and partnerships with universities and coding bootcamps. In retention, the calculus is less about title and tenure and more about growth velocity and meaningful work, which automation can deliver by offloading drudgery and freeing time for complex projects; conversely, firms must counter alienation by making the benefits visible, offering transparent career paths, and giving staff control over automation design. Workforce planning therefore incorporates attraction levers like continuous learning budgets and retention mechanisms such as flexible automation-enabled delivery roles, because the worker experience is now a key differentiator in talent competition.

Finally, the economic case demands disciplined implementation because mid-market firms must balance cash outlays against uncertain gains and because technology choices carry lock-in and upgrade costs. Initial costs include licensing or cloud infrastructure, integration with case management and accounting systems, data preparation and governance, security and compliance controls, and change management, which together can constitute a meaningful share of annual IT budgets; recurring expenses encompass model monitoring, vendor support, staff training, and model refresh cycles. Return on investment arises from labor savings, error reduction, faster time-to-value, and new revenue from higher-margin advisory services, but only when firms baseline performance, set cycle-time and rework targets, and measure utilization gains against historical workload; scenario analysis and staged rollouts mitigate risk, while vendor-agnostic architectures and careful contract design protect against platform dependencies. Workforce planning, in this context, becomes a financial discipline that links headcount adjustments to explicit ROI thresholds and service delivery targets, ensuring that automation strengthens competitiveness without eroding the professional judgment that defines mid-market firms.

---

## Sample 08 — Workforce Planning Analysis — System-Edited Rewrite
- **Classification:** S
- **Source path:** samples/after/05-workforce-planning-analysis/stage-3-voice.md
- **Word count:** 649
- **Domain / register:** Analytical essay (same topic, post-pipeline)
- **Excerpt note:** Full body

Automation has changed how mid-market professional services firms plan their workforces. Not
incrementally -- in the mechanics of how output is measured, how work is sequenced, and
where human judgment still matters. Document intelligence can summarize routine engagements
and reconcile accounts in hours or minutes rather than days, though complex multi-entity
work takes longer; workflow orchestration and robotic process automation move tickets through
repeatable checkpoints without delays tied to human handoffs; and analytics platforms surface
leading indicators that improve how firms forecast and allocate resources. As throughput rises
without proportional headcount growth, planning shifts from filling seats to managing
utilization and rework, because capacity is increasingly defined by system bottlenecks rather
than headcount. The result is a planning model built around cycle-time reduction, quality
bands, and compliance guardrails -- one that treats hours billed as a derivative of output
rather than the primary unit of productivity.

Automation displaces routine tasks and simultaneously expands demand for judgment, data
fluency, and advisory work that requires direct client contact. As AI tools increasingly
automate routine audit procedures, legal research tasks, and basic design work, hybrid roles
such as automation analyst, data steward, and client success manager are beginning to appear
alongside traditional experts who must interpret model outputs, challenge assumptions, and
govern the systems they rely on. Firms redesign career ladders accordingly -- data literacy
becomes a baseline expectation, not a specialty -- and embed cross-functional squads where
analysts, technologists, and domain specialists work together under agile governance while
investing in prompt engineering and model supervision training. Planning shifts from pure
headcount forecasting toward mapping the competencies the firm will need in two to three years.
These outcomes are not automatic. Firms that underinvest in change management, deploy tools
before their workflows are sufficiently standardized, or operate in practice areas subject to
regulatory constraints on automated professional work may find that automation increases
oversight costs before reducing them.

Competing for talent looks different when the job description has changed. Firms now recruit
for candidates who can combine domain expertise with the ability to orchestrate automation
tools alongside direct client engagement -- a narrower target than either skill alone.
Recruitment strategies prioritize data and automation proficiency while maintaining domain
depth; firms build internal pipelines through apprenticeships, rotational programs, and
university and bootcamp partnerships. In retention, the calculus has shifted: title and
tenure matter less than rate of career advancement and access to work that requires real
judgment, which automation can deliver by eliminating repetitive tasks and freeing time for
complex projects. Conversely, firms must counter alienation by making the productivity gains
visible, creating legible career paths, and giving staff genuine control over automation
design. Worker experience has become an increasingly important differentiator in professional
services talent competition, as candidates with automation skills have more options than
their predecessors did.

The economic case is real but not guaranteed. Mid-market firms must balance cash outlays
against uncertain returns, and technology choices carry lock-in and upgrade costs that extend
well beyond initial deployment. Initial costs include software licensing, cloud infrastructure,
integration with case management and accounting systems, data preparation and governance,
security and compliance controls, and change management -- together representing, for most
mid-market firms, somewhere between 15 and 30 percent of annual IT budgets, depending on
scope and vendor pricing, though firms with more complex legacy environments will fall toward
the higher end of that range. Recurring expenses add model monitoring, vendor support, staff
training, and model refresh cycles. When firms baseline performance before deployment, set
explicit cycle-time and rework targets, and measure utilization gains against historical
workload, automation can generate ROI through labor savings, error reduction, reduced
time-to-value, and new revenue from higher-margin advisory services. Scenario analysis and
staged rollouts reduce implementation risk; vendor-agnostic architectures and careful contract
terms reduce platform dependency. Workforce planning, under this discipline, becomes a
financial function -- one that ties headcount decisions directly to ROI thresholds and
service delivery targets rather than to historical staffing ratios.

---
