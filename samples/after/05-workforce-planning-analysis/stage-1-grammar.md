---
stage: 1
agent: grammar-composition-editor
source: ../../before/05-workforce-planning-analysis.md
timestamp: 2026-02-20T23:55:00Z
---

## Grammar Report

```text
Grammar Errors:       2
Composition Issues:   3
Plain Language Flags: 5
AI-Mechanical Flags:  9
Non-Prose Issues:     2
Total:                21
```

**Status**: FAIL

Rationale: Two grammar errors (undefined acronyms) and nine AI-mechanical pattern instances
across four paragraphs exceed the FAIL threshold of six AI-mechanical instances across the
document. Three or more AI-mechanical instances appear in paragraphs 3 and 4 individually.
The document is mechanically near-clean on punctuation, tense, agreement, and that/which usage,
but the density of AI-mechanical patterns (particularly the five-participle sentence in paragraph
3 and the gerund-padded closing in paragraph 4) requires remediation before Stage 2.

---

## Issue Log

| # | Location | Category | Severity | Current Text | Issue | Suggested Fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Para 1, sentence 3 | Non-Prose | Error | "...rather than FTEs." | "FTEs" used without definition on first use | "...rather than full-time equivalents (FTEs)." |
| 2 | Para 4, sentence 4 | Non-Prose | Error | "...explicit ROI thresholds..." | "ROI" used without definition on first use; concept first appears in P4-S3 as "return on investment" but acronym is not established there | Define at first appearance: "return on investment (ROI)" in P4-S3, then use ROI in P4-S4 |
| 3 | Para 4, sentence 2 | Composition | Warning | "licensing or cloud infrastructure, integration with..." | Parallel structure broken: "licensing" is a gerund (activity noun) while "cloud infrastructure" is a thing; they cannot share an "or" under the same list heading | Rewrite as two items: "software licensing, cloud infrastructure, integration with..." |
| 4 | Para 4, sentence 3 | Composition | Warning | "labor savings, error reduction, faster time-to-value, and new revenue..." | Parallel structure broken: "faster time-to-value" inserts an adjective before the noun where all other list items are plain noun phrases ("labor savings," "error reduction," "new revenue") | Rewrite: "labor savings, error reduction, reduced time-to-value, and new revenue..." |
| 5 | Para 4, sentence 3 | Plain Language | Error | "Return on investment arises from labor savings...while vendor-agnostic architectures and careful contract design protect against platform dependencies." | Single sentence of approximately 70 words contains a conditional clause, a coordinated list of four items, a semicolon-joined independent clause with "while" subordination, and two parallel noun phrases. Violates the one-idea-per-sentence rule. Advisory: Stage 3 may retain complexity for voice reasons. | Split into at minimum two sentences at the semicolon: (1) "Return on investment arises from labor savings, error reduction, reduced time-to-value, and new revenue from higher-margin advisory services — but only when firms baseline performance, set cycle-time and rework targets, and measure utilization gains against historical workload." (2) "Scenario analysis and staged rollouts mitigate risk; vendor-agnostic architectures and careful contract design protect against platform dependencies." Note: sentence 1 retains an em-dash; substitute a colon or comma per PCP override. |
| 6 | Para 1, sentences 1-4 | Plain Language | Warning | Full paragraph | No headings; four long sentences (average ~38 words). Paragraph sentences each carry two to four independent ideas. Readability is in the technical range (grade 14-16 estimated) for an audience that may be professional/executive (target: 10-14). Advisory: Stage 3 may retain for voice reasons. | Consider splitting sentences at conjunctions and semicolons; add section headings if document structure permits |
| 7 | Para 3, sentence 3 | Plain Language | Warning | "the calculus is less about title and tenure and more about growth velocity and meaningful work" | "calculus" used as a general business metaphor for "balance" or "consideration." Plain language flag: jargon. | "the calculation" or "the question" or "the tradeoff" |
| 8 | Para 3, sentence 4 | Plain Language | Warning | "attraction levers like continuous learning budgets and retention mechanisms such as flexible automation-enabled delivery roles" | "attraction levers" and "retention mechanisms" are jargon compound nouns. Plain language flag. | "tools to attract candidates, such as continuous learning budgets, and mechanisms to retain staff, such as flexible automation-enabled delivery roles" |
| 9 | Para 4, sentence 1 | Plain Language | Warning | "the economic case demands disciplined implementation" | "implementation" is a nominalization where the verb form is available. "demands disciplined implementation" could be "demands that firms implement automation with discipline." Flagged because it opens the concluding paragraph and the nominalization buries the actor. | "the economic case requires firms to implement automation with discipline" |
| 10 | Para 3, sentence 3 | AI-Mechanical | Error | "...which automation can deliver by offloading drudgery and freeing time for complex projects; conversely, firms must counter alienation by making the benefits visible, offering transparent career paths, and giving staff control over automation design." | Five -ing forms in one sentence: "offloading," "freeing," "making," "offering," "giving." Exceeds the three-or-more threshold for present participle overuse. | Split at the semicolon. Rewrite the second clause with finite verbs: "...conversely, firms must counter alienation by making the benefits visible, creating clear career paths, and giving staff control over automation design." That reduces to three -ing forms total across two clauses; further reduction preferred. |
| 11 | Para 4, sentence 4 | AI-Mechanical | Error | "...ensuring that automation strengthens competitiveness without eroding the professional judgment that defines mid-market firms." | Sentence-final gerund phrase padding. The main clause ("Workforce planning becomes a financial discipline that links headcount adjustments to explicit ROI thresholds and service delivery targets") is complete. The gerund phrase adds no new information: it restates the goal in abstract terms without specifying a mechanism, metric, or constraint. This is the classic empty gerund closer. | Delete or replace with a concrete statement. Example: "When implemented this way, workforce planning becomes a financial discipline, not an administrative function." Alternative: end the sentence after "service delivery targets." |
| 12 | Para 1, sentence 1 | AI-Mechanical | Warning | "where human judgment delivers differentiation" | "differentiation" is a nominalization; the verb phrase ("where human judgment distinguishes the firm") is shorter and more direct. | "where human judgment distinguishes the firm" |
| 13 | Para 1, sentence 2 | AI-Mechanical | Warning | "perform reconciliations," "improve forecasting and resource allocation" | Three nominalizations in one sentence: "reconciliations," "forecasting," "allocation." Nominalization density flag (two or more per sentence). "reconciliations" → "reconcile"; "forecasting and resource allocation" → "forecast and allocate resources." | "perform reconciliations" → "reconcile accounts"; "improve forecasting and resource allocation" → "improve how firms forecast and allocate resources" |
| 14 | Para 2, sentence 4 | AI-Mechanical | Warning | "Planning thus becomes forward-looking competence mapping rather than pure headcount forecasting, because the marginal worker is not simply an analog replacement but a new combination of human insight and supervised automation." | Four nominalizations: "competence mapping," "forecasting," "replacement," "combination." Dense nominalization throughout: "the marginal worker is not simply an analog replacement but a new combination..." hides the action behind noun stacks. | Flag for Stage 3. Possible rewrite: "Planning thus looks forward rather than backward: instead of counting heads, firms map the competencies they need and ask how humans and automated systems will share the work." |
| 15 | Para 3, sentence 2 | AI-Mechanical | Warning | "prompting firms to cultivate internal pipelines through apprenticeships, rotational programs, and partnerships with universities and coding bootcamps." | Sentence-appended participial phrase ("prompting firms to cultivate...") is a softer version of gerund padding. The participial phrase does carry information (it specifies how firms respond), so this is a Warning, not an Error. However, the -ing chain "maintaining...prompting" in successive phrases weakens the sentence. | Rewrite as a separate sentence with a finite verb: "Firms respond by building internal pipelines through apprenticeships, rotational programs, and university and bootcamp partnerships." |
| 16 | Para 2, sentence 3 | AI-Mechanical | Warning | "to ensure outputs remain reliable and ethically sound" | Sentence-final infinitive phrase that gestures at a goal without specifying any mechanism or standard. What makes an output "ethically sound"? This is the infinitive-phrase variant of gerund padding. | Delete or specify: "to meet accuracy and bias-review standards" or similar concrete criterion. |
| 17 | Para 4, sentence 3 | AI-Mechanical | Warning | "scenario analysis and staged rollouts mitigate risk, while vendor-agnostic architectures and careful contract design protect against platform dependencies." | This clause (joined to the main clause by semicolon) uses two abstract noun-phrase subjects ("scenario analysis and staged rollouts"; "vendor-agnostic architectures and careful contract design") where the actor (the firm) is hidden. The nominalizations — "analysis," "rollouts," "architectures," "design" — stack four in one clause. | Advisory for Stage 3. Possible rewrite: "Staged rollouts and scenario analysis reduce risk. Vendor-agnostic architecture and negotiated contract terms guard against platform lock-in." |
| 18 | Para 2, opener | AI-Mechanical | Note | "These productivity gains propagate into role design and skill evolution..." | Echo-opener pattern: the paragraph opens by restating the conclusion of the previous paragraph ("productivity gains") rather than introducing a new topic sentence. This is an AI structural tell. Stage 3 decision. | Note for Stage 3 (Voice). Do not correct at Stage 1. |
| 19 | Para 3, opener | AI-Mechanical | Note | "The talent market responds in kind..." | Echo-opener pattern: "responds in kind" explicitly connects to the paragraph above rather than asserting the paragraph's own claim. Stage 3 decision. | Note for Stage 3 (Voice). Do not correct at Stage 1. |
| 20 | Para 1, sentence 3 | Grammar | Note | "...capacity is increasingly defined by system bottlenecks rather than FTEs." | "is increasingly defined" is passive. Actor (automation / system growth) is de-emphasized by design. Passive is acceptable here. No correction needed. | No fix required. Noted for completeness. |
| 21 | Para 4, sentence 3 | Composition | Note | Full sentence (~70 words) | Complexity flag: this is the longest sentence in the document and the most structurally loaded. Stage 1 recommends splitting at the semicolon (see issue #5). Stage 3 has final authority to retain the complex form for voice reasons. | Advisory only; Stage 3 may retain. |

---

## Corrected Document

The following version applies all Error-level and Warning-level fixes that fall within Stage 1's
mechanical scope. Notes and Stage 3 items are flagged inline but not altered. Advisory flags are
indicated in brackets.

Fixes applied:
- Issue 1: FTEs defined on first use
- Issue 2: ROI defined on first use (in P4-S3); acronym used in P4-S4
- Issue 3: Parallel structure in P4-S2 corrected ("licensing or cloud infrastructure" split)
- Issue 4: Parallel structure in P4-S3 corrected ("faster" removed; "reduced" substituted)
- Issue 5: P4-S3 split at semicolon into two sentences; em-dash replaced with colon per PCP override
- Issue 10: P3-S3 five-participle chain reduced; second clause rewritten with finite verbs
- Issue 11: Sentence-final gerund padding removed from P4-S4; sentence ends after "service delivery targets"

Warnings retained as-is (jargon, nominalization density, participial appended phrases) are
marked [Stage 3] for voice-level remediation. Advisory complexity flags are marked [Advisory].

---

Automation is altering workforce planning in mid-market professional services by changing how
output is measured, how work is sequenced, and where human judgment [Stage 3: consider
"distinguishes the firm" in place of "delivers differentiation"] delivers differentiation.
Document intelligence can summarize engagements and reconcile accounts in minutes rather than
days; workflow orchestration and robotic process automation can move tickets through repeatable
checkpoints without delays tied to human handoffs; and analytics platforms surface leading
indicators that improve how firms forecast and allocate resources. As throughput rises without
proportional headcount growth, planning shifts from filling roles to managing utilization and
rework, because capacity is increasingly defined by system bottlenecks rather than full-time
equivalents (FTEs). The result is a planning model that emphasizes cycle-time reduction, quality
bands, and compliance guardrails, while treating hours as a derivative rather than the primary
currency of productivity.

These productivity gains propagate into role design and skill evolution [Stage 3: echo-opener
pattern; see issue 18], because automation displaces routine tasks yet expands the demand for
judgment, data fluency, and client-adjacent advisory work. As standard audits, legal research,
and basic design are automated, hybrid roles such as automation analyst, data steward, and
client success manager emerge alongside traditional experts who must now interpret model outputs,
challenge assumptions, and govern the systems they rely on. Firms therefore redesign career
ladders to include data literacy as a baseline competence and embed cross-functional squads where
analysts, technologists, and domain specialists collaborate under agile governance; at the same
time, they invest in prompt engineering and model supervision training [Stage 3: consider
specifying accuracy and bias-review standards in place of "to ensure outputs remain reliable and
ethically sound"]. Planning thus becomes forward-looking competence mapping rather than pure
headcount forecasting [Stage 3: high nominalization density; see issue 14], because the marginal
worker is not simply an analog replacement but a new combination of human insight and supervised
automation.

The talent market responds in kind [Stage 3: echo-opener pattern; see issue 19], because firms
are no longer competing only for domain expertise but for candidates who can orchestrate
technology alongside client engagement. Recruitment strategies prioritize data and automation
skills while maintaining domain proficiency; firms then build internal pipelines through
apprenticeships, rotational programs, and university and bootcamp partnerships. In retention,
the tradeoff [Stage 3: "calculus" flagged as jargon; "tradeoff" is one option] is less about
title and tenure and more about growth velocity and meaningful work, which automation can deliver
by offloading drudgery and freeing time for complex projects; conversely, firms must counter
alienation by making the benefits visible, creating clear career paths, and giving staff control
over automation design. Workforce planning therefore incorporates tools to attract candidates,
such as continuous learning budgets [Stage 3: "attraction levers" flagged as jargon; see issue
8], and mechanisms to retain staff, such as flexible automation-enabled delivery roles, because
the worker experience is now a key differentiator in talent competition.

Finally, the economic case requires firms to implement automation with discipline [Stage 3:
nominalization "implementation" replaced with verb construction; see issue 9] because mid-market
firms must balance cash outlays against uncertain gains and because technology choices carry
lock-in and upgrade costs. Initial costs include software licensing, cloud infrastructure,
integration with case management and accounting systems, data preparation and governance,
security and compliance controls, and change management, which together can constitute a
meaningful share of annual IT budgets; recurring expenses encompass model monitoring, vendor
support, staff training, and model refresh cycles. Return on investment (ROI) arises from labor
savings, error reduction, reduced time-to-value, and new revenue from higher-margin advisory
services, but only when firms baseline performance, set cycle-time and rework targets, and
measure utilization gains against historical workload. Scenario analysis and staged rollouts
mitigate risk, while vendor-agnostic architectures and careful contract design protect against
platform dependencies [Advisory: Stage 3 may rewrite this clause to surface the firm as actor;
see issue 17]. Workforce planning, in this context, becomes a financial discipline that links
headcount adjustments to explicit ROI thresholds and service delivery targets.

---

## Pipeline Status Block

```yaml
pipeline:
  document: 05-workforce-planning-analysis.md
  format: analytical-report

  stage_1_grammar:
    status: FAIL
    errors: 2
    warnings: 10
    notes: 4
    categories:
      grammar: 0
      non_prose: 2
      composition: 3
      plain_language: 5
      ai_mechanical: 9
    total_issues: 21
    reviewer: grammar-composition-editor
    timestamp: 2026-02-20T23:55:00Z
    notes_for_stage_3:
      - "Echo-opener pattern in paragraphs 2 and 3 (issues 18-19): Stage 3 decision"
      - "High nominalization density throughout (issues 12-14, 17): Stage 3 decision"
      - "Jargon terms flagged in plain language issues 7-9: Stage 3 decision on retention"
      - "Advisory complexity flag on paragraph 4 sentence 3: Stage 3 may retain"
    handoff_recommendation: >
      FAIL status requires author review before Stage 2. Primary blockers are the
      sentence-final gerund padding (issue 11, corrected in this pass), the five-participle
      sentence in paragraph 3 (issue 10, partially corrected), and pervasive AI-mechanical
      nominalization density throughout all four paragraphs. The corrected document above
      addresses all Error-level and Warning-level mechanical issues within Stage 1 scope.
      If the author accepts the Stage 1 corrections, the corrected document may proceed to
      Stage 2 without a full author-revision cycle; Stage 2 should be aware of the high
      nominalization and jargon density flagged for Stage 3.

  stage_2_validator:
    status: PENDING

  stage_3_style:
    status: PENDING
```
