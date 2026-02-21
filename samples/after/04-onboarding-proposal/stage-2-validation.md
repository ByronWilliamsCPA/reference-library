---
stage: 2
agent: document-validator
source: ../stage-1-grammar.md (Corrected Document section)
timestamp: 2026-02-20T23:55:00Z
---

## Validation Summary

```text
Document: Internal Proposal — Restructured New-Hire Onboarding Program
Total Claims Analyzed: 22
─────────────────────────────
Verified:        0  (0%)
Expert Judgment: 7  (32%)
Assumptions:     4  (18%)
Unverified:      11 (50%)
Suspect:         0  (0%)
─────────────────────────────
Reasoning Errors: 5
Universal Quantifiers: 1 flagged ("typically" — soft universal)
Overall Status: CONDITIONAL
```

**Rationale**: Verified + Expert Judgment = 32%, well below the 75% Conditional threshold.
However, the document contains zero Suspect claims and no fabricated entities. The low verified
percentage reflects that every benefit claim is unsourced, not that claims are false. The
document is internally consistent and the program elements are professionally plausible. The
Conditional verdict is appropriate: the factual deficiencies are concentrated in the Benefits
section and the metrics list, and all are correctable without restructuring. A FAIL verdict
would require either Suspect claims or evidence of unmitigated Confirmation Bias or Optimism
Bias. Both are present but mitigable with targeted revisions.

---

## Issue Log

| # | Section | Claim | Tag | Issue | Recommendation |
| --- | --- | --- | --- | --- | --- |
| 1 | Benefits, sentence 1 | "Associates typically reach billable levels earlier" | UNVERIFIED | Comparative without a baseline ("earlier than what?"), causal without evidence (why would this program cause it?), and "typically" functions as a soft universal that implies consistent replication across associates. No firm data, pilot result, or external study cited. | Add baseline: "In our current cohort, associates reach full billable capacity at approximately [X] weeks. The structured 90-day path targets [Y] weeks." Or hedge explicitly: "We expect associates to reach billable proficiency faster, though the magnitude will be confirmed through pilot measurement." |
| 2 | Benefits, sentence 2 | "Fewer errors and less rework improve the firm's risk profile and reputation with clients" | UNVERIFIED | Two unsupported causal links: (1) the program will reduce errors and rework; (2) reduced errors will improve both risk profile and client reputation. Neither link is sourced. The causal chain is plausible but stated as fact. | Break the chain into testable pieces. State which program elements are expected to reduce errors (supervised real-file work, the competency matrix) and flag that error-rate improvement will be confirmed through pilot chargeback and defect tracking. |
| 3 | Benefits, sentence 3 | "Buddies develop supervisory capability, building the firm's pool of qualified managers" | UNVERIFIED | Assumed developmental outcome for buddies with no evidence base. The claim implies that serving as a buddy produces measurable supervisory skill gain. No study, pilot, or professional judgment basis is stated. | Qualify as a design intent: "The buddy role is structured to give senior associates early supervisory experience, supporting their development toward manager roles." Or cite peer-reviewed literature on structured mentoring and skill transfer if available. |
| 4 | Benefits, sentence 4 | "Clear role expectations and a predictable support schedule enhance engagement and reduce first-year attrition" | UNVERIFIED | Dual causal claim with no evidence. Both links (role clarity drives engagement; engagement reduces attrition) have research support in general organizational behavior literature, but no source is cited and no firm baseline attrition figure is provided, making the claim unmeasurable. | Cite a credible source (e.g., SHRM, Gallup, or AICPA workforce research) or qualify as a hypothesis to be tested: "We anticipate that role clarity and consistent support will reduce disengagement-driven attrition; the pilot will establish a first-year retention baseline for comparison." |
| 5 | Benefits, sentence 5 | "Knowledge captured in the playbook standardizes quality and makes training scalable across offices" | UNVERIFIED | Two assumed benefits of the playbook format: quality standardization and scalability. Both are reasonable design goals but are stated as outcomes rather than intentions. No evidence that playbook adoption achieves these results at this firm or in comparable firms. | Reframe as design objectives: "The digital playbook is designed to standardize role-based competencies and reduce reliance on individual-office variation, enabling firmwide rollout." |
| 6 | Problem, sentence 3 | "delays chargeable hours, burdens senior staff with repetitive questions, and increases turnover" | UNVERIFIED | Three claimed consequences of the current onboarding gap. Plausible and likely observed, but presented as established facts. No measurement is provided (e.g., average delay in weeks, hours lost per quarter, turnover rate). | Add at least one anchor figure drawn from firm records: "First-year attrition has averaged [X]% over the past [N] years" or "Partners estimate [X] hours per month spent on repeated onboarding questions." If firm data is unavailable, reframe as observed patterns: "Partners report delays in chargeable hours, high rates of repeated questions to senior staff, and elevated first-year turnover." |
| 7 | Problem, sentence 4 | "Partners report uneven expectations among client teams, while associates frequently cite unclear advancement benchmarks" | EXPERT JUDGMENT | Sourced to internal observation ("Partners report," "associates frequently cite"). Not externally verified, but appropriate as an internal diagnosis. Acceptable if this reflects actual partner and associate feedback gathered through a defined process. | If these observations come from a formal survey or structured interviews, note the process briefly: "Exit interviews and partner feedback sessions consistently identify..." This lifts the claim from anecdote to evidence. |
| 8 | Solution, sentence 1 | Two-day integration summit covering firm values, compliance, client service standards, and timekeeping basics | EXPERT JUDGMENT | Program design elements are professional judgments, not factual claims requiring external citation. The structure is plausible and consistent with standard onboarding practice. | No action required. |
| 9 | Solution | Week-one module list (tax and audit methodologies, document review workflows, tools) | EXPERT JUDGMENT | Content selection is a professional design judgment appropriate for an internal proposal. | No action required. |
| 10 | Solution | Day 45 proficiency check; day 90 skills audit and client-readiness review | EXPERT JUDGMENT | Milestone structure is a design decision. The specific timing is stated as a plan, not a factual claim about outcomes. | No action required. |
| 11 | Solution | Twelve-week buddy pairing; buddy is a senior associate or manager | EXPERT JUDGMENT | Program structure elements are design decisions. Twelve weeks is a defined parameter, not an empirical claim. | No action required. |
| 12 | Solution | Pilot with next two cohorts, milestones at 30, 45, and 90 days | EXPERT JUDGMENT | Pilot design is a professional judgment. Tracking at three milestones is standard practice. | No action required. |
| 13 | Implementation | "Training spaces and virtual tools will be configured within four weeks" | ASSUMPTION | States a delivery timeline as fact. The four-week figure implies that IT capacity, tool licensing, and space scheduling are already assessed. No basis is given. | Flag as an assumed timeline: "IT and facilities estimate four weeks for configuration, pending confirmation of tool licensing and space availability." |
| 14 | Metrics | "shortened time to billable proficiency" | UNVERIFIED | Metric is named but has no baseline, no target, and no measurement method. "Shortened" implies a comparison point that does not appear in the document. | State the current baseline and target: "Current time to full chargeable capacity: [X] weeks. Target: [Y] weeks by end of pilot cohort." |
| 15 | Metrics | "reduced first-year turnover" | UNVERIFIED | Metric is named but has no baseline figure, no target reduction percentage, and no measurement window. | State: "Current first-year attrition: [X]%. Target: reduce to [Y]% within [Z] cohorts." |
| 16 | Metrics | "fewer defects and chargebacks" | UNVERIFIED | Metric is named but has no current rate, no measurement definition, and no target. "Defects" is undefined — does it mean client-reported errors, internal review failures, or chargeback disputes? | Define the metric, state the current rate, and set a target. "Chargeback rate per associate in months 1–3: [X per quarter]. Target: reduce by [Y]%." |
| 17 | Metrics | "improved manager workload balance" | UNVERIFIED | This metric has no definition, no current measurement, and no target. "Workload balance" is not a standard accounting metric and would require a bespoke survey instrument or time-tracking analysis. | Either define the measurement instrument ("we will track manager hours spent on new-hire support questions using time entries coded to [category]") or remove this metric and replace it with a more tractable measure such as manager satisfaction score from a structured survey. |
| 18 | Metrics | "increased client satisfaction" | UNVERIFIED | Client satisfaction is a standard metric, but no baseline, measurement instrument, or attribution method is specified. Client satisfaction scores fluctuate for many reasons; attribution to the onboarding program requires a defined comparison period and controlled comparison. | Specify the instrument and baseline: "Net Promoter Score (or equivalent) for engagements staffed by first-year associates: current baseline [X]. Target: [Y] by [quarter]." |
| 19 | Implementation | "quarterly audits by the partners" | EXPERT JUDGMENT | Governance mechanism is a design decision. Quarterly audit cadence is standard professional practice. | No action required. |
| 20 | Problem, sentence 1 | "new hires often feel adrift during the first quarter" | UNVERIFIED | Experiential claim stated as a general fact. Plausible and likely based on informal observation, but "often" is a frequency claim with no basis given. | Tie to a source: exit survey data, informal partner feedback, or associate check-in observations. If anecdotal, qualify: "Feedback from recent associates describes..." |
| 21 | Opening | "compress ramp time, reduce risk, and strengthen the culture" | EXPERT JUDGMENT | These are stated program goals, not factual claims. Appropriate as proposal framing. | No action required. |
| 22 | Problem | "These patterns reflect a fragmented approach rather than a deliberate learning journey" | EXPERT JUDGMENT | Interpretive conclusion drawn from observed patterns. Appropriate for a proposal; this is the author's diagnosis, not a factual assertion requiring citation. | No action required. |

---

## Assumption Register

| # | Assumption | Stated? | Type | Risk if Invalid | Recommendation |
| --- | --- | --- | --- | --- | --- |
| 1 | Firm data on current ramp time, attrition, and error rates exists and will be available to measure against | No | Resource | All five success metrics become unmeasurable; the pilot produces no comparable results | State explicitly: "Pilot measurement requires baseline data from HR and billing systems. Data availability will be confirmed before pilot launch." |
| 2 | The two pilot cohorts are large enough and representative enough to produce valid measurements | No | Technical | Pilot results do not generalize to firmwide rollout; program scaled prematurely | State cohort size and address representativeness: "The two pilot cohorts include [N] associates across [office locations and service lines], selected to reflect firmwide diversity." |
| 3 | IT capacity and tool licensing can be completed within four weeks | No | Resource | Implementation timeline slips; program cannot launch on schedule | State explicitly and add contingency: "IT configuration and licensing are estimated at four weeks, contingent on [vendor/IT confirmation]. A six-week buffer is built into the pilot launch date." |
| 4 | Senior associates and managers who serve as buddies and coaches have sufficient capacity alongside their billable obligations | No | Organizational | Buddy and coach roles go unfilled or are nominal; program quality degrades | Address explicitly: "Buddy and coach participation is voluntary and limited to associates and managers at [utilization threshold] or below, ensuring participation does not create overload." |
| 5 | Buddy and coach roles require training to function as designed | Partial | Organizational | Untrained buddies and coaches deliver inconsistent or counterproductive guidance | The document references "trained buddy" in the solution section, implying training exists. The training design and duration are not described. State what "trained" means: "Buddies complete a [X-hour] preparation session covering feedback skills, confidentiality, and escalation protocols." |
| 6 | The curriculum, digital playbook, and competency matrix can be drafted by the task force within the four-week configuration window | No | Temporal | Content is not ready when training spaces are; launch delays or program launches with incomplete materials | Decouple the content-development timeline from the IT-configuration timeline. State separate milestones for curriculum completion and tool readiness. |
| 7 | Partner buy-in exists for quarterly audit participation | No | Organizational | Governance mechanism is nominal; audit findings are not acted upon | Note whether partner participation has been secured: "The managing partner has confirmed partner participation in quarterly audits as a standing agenda item." |

---

## Reasoning Error Log

| # | Section | Error Type | Claim | Issue | Fix |
| --- | --- | --- | --- | --- | --- |
| 1 | Benefits, sentence 1 | False Causation | "Associates typically reach billable levels earlier" | The program is described; it is then asserted that associates reach billable levels earlier. No mechanism connecting the program elements to the speed outcome is stated. The word "typically" implies this is an observed pattern, but no observation basis is given. This conflates the program as designed with the program as delivering results. | State the causal mechanism explicitly: "Because associates complete core methodology modules in week one and receive supervised real-file work from month one, we expect them to reach chargeable proficiency [X] weeks earlier than the current average." Then confirm through pilot measurement. |
| 2 | Benefits, sentence 4 | False Causation | "Clear role expectations and a predictable support schedule enhance engagement and reduce first-year attrition" | Two causal steps are asserted as fact: (1) the program will produce clear role expectations and predictable support; (2) those conditions will enhance engagement and reduce attrition. Step one is a design intention, not a delivered outcome. Step two is a behavioral claim with research support in organizational behavior literature but no citation here. | Separate the design intent from the expected outcome and cite supporting evidence. "Structured role expectations and consistent check-in schedules are associated with higher engagement and lower attrition in professional-services contexts (cite source). The program is designed to provide both." |
| 3 | Benefits, entire paragraph | Cherry-Picking (Confirmation Bias) | Benefits paragraph presents five positive outcomes with no risks, implementation challenges, or failure modes acknowledged | The document lists only the expected positive outcomes of the program. There is no acknowledgment of what could go wrong: buddy relationships that do not work, associates who do not respond to structured programs, partner disengagement from governance, or cohort-to-cohort variation that distorts pilot results. This is a structurally one-sided argument. | Add a brief risk paragraph or a "Risks and Mitigations" section. At minimum, acknowledge two or three realistic failure modes and how the program design addresses them. This also improves credibility with skeptical partners. |
| 4 | Benefits, entire paragraph | Optimism Bias | All five projected outcomes are stated as expected positives; no conservative or baseline scenario is presented | Every projected outcome is framed as an improvement. There is no acknowledgment that some metrics may not improve in the pilot, that the improvement may take longer than one cohort to manifest, or that early results may be mixed. This is consistent with AI-generated benefit language that defaults to positive projection. | Add a calibration sentence: "Initial pilot results may be mixed as facilitators build experience with the program. We will use the first cohort to refine delivery and set realistic targets for the second." |
| 5 | Metrics, sentence 1 | Non Sequitur (incomplete argument) | "Success will be measured by shortened time to billable proficiency, reduced first-year turnover, fewer defects and chargebacks, improved manager workload balance, and increased client satisfaction" | Listing metrics does not constitute a measurement plan. The sentence implies that success is defined and measurable, but without baselines, targets, measurement instruments, and attribution methodology, the metrics are labels, not measures. The conclusion ("this is a measurement plan") does not follow from the premise ("here are five category names"). | Complete each metric: state the current baseline, the target, the measurement instrument, and the measurement window. For client satisfaction, specify the attribution methodology — how will the firm distinguish program effects from engagement quality effects? |

---

## Bias Assessment

| Bias Type | Present? | Evidence | Mitigation |
| --- | --- | --- | --- |
| Confirmation Bias | Yes | The Benefits paragraph presents five positive outcomes with no counterexamples, failure modes, or conditions under which the program would not achieve the stated results. Evidence that could weaken the case (e.g., research showing structured programs fail when buddy quality is inconsistent, or that attrition in accounting is driven by compensation rather than onboarding) is absent. | Add a Risks and Mitigations section. Acknowledge at least two failure modes and the program design elements that address them. |
| Optimism Bias | Yes | All projections are framed as improvements with no acknowledgment of magnitude uncertainty, timeline variation, or mixed early results. The metrics section names five improvements without any conservative scenario. | Add a calibration statement in the benefits section. Present at least one conservative scenario: "If pilot results are mixed, we will extend the pilot to a third cohort before firmwide rollout." |
| Survivorship Bias | Possible | The implicit framing is that structured onboarding programs succeed. The document does not acknowledge that similar programs at other firms may have failed or produced smaller gains than projected, nor does it discuss conditions necessary for success. | If citing general industry practice in a revision, acknowledge that implementation quality drives outcomes: "Programs of this type have produced varying results; the primary risk factors are buddy-training quality and partner engagement in governance." |
| Vendor/Solution Bias | No | No external vendor is named or favored. The proposal is for an internally developed program. | No action required. |
| Sunk Cost | No | No prior investment in onboarding infrastructure is cited as justification for this proposal. | No action required. |
| Authority Bias | Minimal | The proposal relies on partner and associate observations as its diagnostic basis. These are appropriate internal sources for an internal proposal, though they are stated without a defined collection process. | If partner and associate feedback was gathered through a structured process (survey, interviews), name it to strengthen the evidence base. |

---

## Validated Document

The corrected document from Stage 1 is reproduced below with inline claim tags applied to key
factual assertions. Tags appear in brackets immediately after the claim they classify. Advisory
Stage 3 markers from Stage 1 are preserved.

---

## Internal Proposal: Restructured New-Hire Onboarding Program

We propose a [S3: "revitalized"] onboarding program designed to compress ramp time, reduce
risk, and strengthen the culture of a regional accounting firm. [EXPERT JUDGMENT: program
goals stated as intentions, not factual claims] The plan focuses on a structured 90-day path
that begins with firm foundations and rapidly builds toward job-ready proficiency under close
coaching and shared learning.

The current onboarding experience varies across offices and service lines, and new hires often
feel adrift during the first quarter. [UNVERIFIED: "often" is a frequency claim without a
measurement basis; tie to exit survey or check-in data] New accountants receive inconsistent
guidance on basic standards, unfamiliar clients, and firm policies, which delays chargeable
hours, burdens senior staff with repetitive questions, and increases turnover. [UNVERIFIED:
three claimed consequences stated as facts; no measurement provided for any of them — add at
least one anchor figure from firm records] Partners report uneven expectations among client
teams, while associates frequently cite unclear advancement benchmarks. [EXPERT JUDGMENT:
attributed to internal observation; acceptable if based on formal feedback process — note the
collection method] These patterns reflect a fragmented approach rather than a deliberate
learning journey. [EXPERT JUDGMENT: interpretive conclusion, appropriate as proposal diagnosis]

Our solution introduces a phased, outcomes-focused program that starts with a two-day
integration summit covering firm values, compliance, client service standards, and timekeeping
basics. [EXPERT JUDGMENT: design decision] In week one, associates complete core modules on
tax and audit methodologies, document review workflows, and tools such as firm knowledge bases
and practice management systems. [EXPERT JUDGMENT: design decision] A digital playbook
establishes role-based competencies and checklists mapped to typical tasks. [EXPERT JUDGMENT:
design decision] Within the first month, each new hire is paired with a trained buddy for
twelve weeks [ASSUMPTION: "trained" implies a preparation program whose design and duration
are not described — specify what buddy training entails] and assigned a coach who is a senior
associate or manager. [ASSUMPTION: assumes these staff have sufficient capacity alongside
billable obligations — address capacity constraints explicitly] The training manager holds
weekly office hours to address issues, share quick wins, and reinforce best practices.
[EXPERT JUDGMENT: design decision] Chargeable training hours are scheduled and monitored;
associates receive supervised learning on real files without overburdening clients.
[EXPERT JUDGMENT: design decision] By day 45, associates should demonstrate proficiency in a
subset of standard procedures; by day 90, they complete a skills audit and a client-readiness
review with their manager, identifying any gaps that require targeted support or mentorship.
[EXPERT JUDGMENT: milestone design decisions]

We expect early and measurable benefits from this plan. Associates typically reach billable
levels earlier, [UNVERIFIED: comparative without baseline; causal without mechanism; "typically"
implies observed pattern with no observation basis cited — add baseline figure and causal
mechanism, or reframe as hypothesis to be confirmed through pilot] increasing utilization and
reducing early-stage losses associated with low chargeable time. [Advisory: Stage 3 may revise
the gerund chain in the preceding sentence.] Fewer errors and less rework improve the firm's
risk profile and reputation with clients. [UNVERIFIED: two unsupported causal links; plausible
but stated as fact — name which program elements are expected to reduce errors and flag for
pilot confirmation] Buddies develop supervisory capability, building the firm's pool of
qualified managers. [UNVERIFIED: assumed developmental outcome with no evidence base — reframe
as design intent or cite supporting literature] Clear role expectations and a predictable
support schedule enhance engagement and reduce first-year attrition. [UNVERIFIED: dual causal
claim without source; organizational behavior literature supports the general principle but no
citation is provided and no attrition baseline exists — cite a source or qualify as hypothesis]
Knowledge captured in the playbook standardizes quality and makes training scalable across
offices. [UNVERIFIED: assumed playbook benefit stated as outcome rather than design intent —
reframe as objective]

Implementation begins with a cross-functional task force (HR, learning and development (L&D),
IT, practice leaders, and three coaches) tasked with drafting the curriculum, digital playbook,
and competency matrix. [EXPERT JUDGMENT: implementation structure] Training spaces and virtual
tools will be configured within four weeks. [ASSUMPTION: timeline stated as fact; assumes IT
capacity, tool licensing, and space scheduling are already assessed — add contingency and
confirm with IT] We will pilot the program with the next two cohorts, [ASSUMPTION: two cohorts
may be insufficient sample for reliable measurement; state cohort size and representativeness]
tracking milestones at 30, 45, and 90 days and gathering feedback through pulse surveys and
retrospective sessions. [EXPERT JUDGMENT: evaluation design decision] Success will be measured
by shortened time to billable proficiency, [UNVERIFIED: no baseline, no target, no measurement
method] reduced first-year turnover, [UNVERIFIED: no baseline attrition figure, no target, no
measurement window] fewer defects and chargebacks, [UNVERIFIED: "defects" undefined; no
current rate, no target] improved manager workload balance, [UNVERIFIED: metric undefined;
no measurement instrument specified] and increased client satisfaction. [UNVERIFIED: no
instrument, no baseline, no attribution methodology] [Advisory: Stage 3 may restructure the
preceding sentence for clarity.] After refinements from the pilot, the program rolls out
firmwide by the following quarter, [ASSUMPTION: assumes pilot will produce sufficient data
within one quarter to support confident firmwide rollout; no trigger criteria for rollout
decision are specified] with ongoing governance by L&D and quarterly audits by the partners.
[EXPERT JUDGMENT: governance design; ASSUMPTION: partner participation in audits assumed but
not confirmed]

---

## Pipeline Status Block

```yaml
pipeline:
  document: 04-onboarding-proposal.md
  format: proposal

  stage_1_grammar:
    status: NEEDS_WORK
    errors: 5
    warnings: 9
    notes: 4
    categories:
      grammar: 6
      composition: 5
      plain_language: 1
      ai_mechanical: 6
    fixes_applied: true
    advisory_items_deferred_to_stage_3: 2
    reviewer: grammar-composition-editor
    timestamp: 2026-02-20T23:30:00Z

  stage_2_validation:
    status: CONDITIONAL
    claims_analyzed: 22
    verified_pct: 0%
    expert_judgment_pct: 32%
    unverified_count: 11
    suspect_claims: 0
    assumptions_found: 7
    reasoning_errors: 5
    bias_patterns_found: 2
    bias_patterns_unmitigated: 2
    reviewer: document-validator
    timestamp: 2026-02-20T23:55:00Z
    notes: >
      All deficiencies concentrated in Benefits paragraph and Metrics list.
      Zero suspect claims. No fabricated entities, statistics, or regulatory
      references. Correctable without restructuring. Two unmitigated bias
      patterns (Confirmation, Optimism) require a Risks and Mitigations
      addition before PASS is achievable.

  stage_3_style_editor:
    status: PENDING
```

---

## Final Recommendation

**CONDITIONAL**

The document has significant factual deficiencies but no fabricated claims or suspect
assertions. Every problem is correctable without restructuring the document. The program
elements themselves are professionally sound; the failure is in how the expected benefits
are stated — as facts rather than hypotheses to be confirmed through the pilot.

**Required fixes before Stage 3 proceeds** (address these before passing to the writing-style
editor, because Stage 3 may rewrite sentences in the Benefits and Metrics sections, and those
rewrites must carry accurate claim framing):

1. **Benefits paragraph — add baselines and reframe as hypotheses.** Each of the five benefit
   claims must either (a) cite a source or firm data point, or (b) be explicitly reframed as
   a pilot hypothesis. The current framing states projected outcomes as established facts,
   which they are not.

2. **Metrics — complete each metric.** For all five named metrics, provide: current baseline
   value, target value, measurement instrument, and measurement window. "Manager workload
   balance" requires either a defined instrument or replacement with a measurable proxy.

3. **Add a Risks and Mitigations section.** At minimum, name two or three realistic failure
   modes and how the program design addresses them. This resolves both the Confirmation Bias
   and Optimism Bias findings and substantially improves credibility with a skeptical partner
   audience.

4. **Problem section — anchor at least one consequence claim.** The three claimed consequences
   of current onboarding gaps (delayed chargeable hours, senior-staff burden, elevated
   turnover) need at least one figure from firm records. If records are unavailable, reframe
   the claims as observed patterns rather than established facts.

5. **State the rollout trigger criteria.** The document moves from pilot to firmwide rollout
   "after refinements" with no stated decision criteria. Add a sentence specifying what
   results would trigger or delay firmwide rollout: "Firmwide rollout proceeds if the pilot
   cohorts demonstrate [X]% improvement in time to billable proficiency and first-year
   attrition holds at or below [Y]%."

**Recommended additions (strengthen the proposal materially):**

- Note the collection method for partner and associate feedback (survey, interviews, exit
  data) in the Problem section.
- Specify what "trained buddy" means — duration and content of buddy preparation.
- Add a capacity-constraint acknowledgment for buddies and coaches.
- State cohort size and composition for the pilot.

**Handoff note to Stage 3**: The Benefits paragraph and the Metrics sentence carry the heaviest
cluster of factual issues. When Stage 3 revises these sections for voice, any rewritten
sentences that introduce new claim language must return through Stage 2 for a targeted check.
The Advisory items deferred from Stage 1 (gerund chain in Benefits sentence 1; metrics sentence
structure) overlap with Stage 2 findings — coordinate the rewrites so that factual framing
corrections and voice adjustments are applied in the same pass rather than sequentially.
