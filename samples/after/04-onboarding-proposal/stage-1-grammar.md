---
stage: 1
agent: grammar-composition-editor
source: ../../before/04-onboarding-proposal.md
timestamp: 2026-02-20T23:30:00Z
---

## Grammar Report

```text
Grammar Errors:       5
Composition Issues:   4
Plain Language Flags: 1
AI-Mechanical Flags:  6
Non-Prose Issues:     2
Total:                18
```

**Status**: NEEDS WORK

Rationale: Five grammar errors exceed the PASS threshold of zero. No single category reaches
the FAIL threshold. The document is structurally sound and coherent; all errors are correctable
without restructuring.

---

## Issue Log

| # | Location | Category | Severity | Current Text | Issue | Suggested Fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Para 5, sentence 1 | Grammar | Error | "task force—HR, learning and development, IT, practice leaders, and three coaches—tasked" | Two em-dashes used as parenthetical delimiters. PCP Tier 3 override bans em-dashes entirely. | Replace both with parentheses: "task force (HR, learning and development, IT, practice leaders, and three coaches) tasked" |
| 2 | Para 3, sentence 5 | Grammar | Error | "assigned a coach from a senior associate or manager" | Preposition "from" implies the coach is sourced from that person, creating ambiguity. The intended meaning is that the coach is a senior associate or manager. | "assigned a coach who is a senior associate or manager" |
| 3 | Para 3, sentence 6 | Grammar | Error | "Chargeable training hours are scheduled and monitored to avoid overburdening clients while providing supervised learning on real files." | Dangling modifier: "while providing supervised learning" has no clear grammatical subject. "Hours" cannot provide learning. | Rewrite to name the actor: "Chargeable training hours are scheduled and monitored; associates receive supervised learning on real files without overburdening clients." |
| 4 | Para 4, sentence 2 | Grammar | Error | "Fewer errors and rework improve the firm's risk profile" | "Fewer" applies to countable nouns; "rework" is a mass noun requiring "less." | "Fewer errors and less rework improve the firm's risk profile" |
| 5 | Para 3, sentence 4 | Grammar | Error | "paired with a trained buddy for 12 weeks" | CMS §9.2–9.3 requires spelling out one through one hundred in running text. "12" is within that range. | "paired with a trained buddy for twelve weeks" |
| 6 | Para 2, sentence 3 | Grammar | Warning | "uneven expectations between client teams" | "Between" is standard for two parties; "among" is correct when three or more groups are implied. Client teams at a regional firm would be plural groups. | "uneven expectations among client teams" [ExpertJudgment: if exactly two teams are meant, "between" is correct — verify with author] |
| 7 | Para 3, sentence 5 | Composition | Warning | "Weekly office hours are held by the training manager to address issues, share quick-wins, and reinforce best practices." | Passive voice when the actor (the training manager) is known and named. Active voice preferred. Also: "quick-wins" is hyphenated incorrectly; as a plural noun it does not take a hyphen. | "The training manager holds weekly office hours to address issues, share quick wins, and reinforce best practices." |
| 8 | Para 3, sentence 9 | Composition | Warning | "a client-ready readiness review" | Redundant compound: "ready" and "readiness" express the same idea. | "a client-readiness review" |
| 9 | Para 4, sentence 1 | Composition | Warning | "increasing utilization and reducing early-stage losses associated with low chargeable time" | Sentence-final participial chain adds two -ing forms without specifying the mechanism or metric. Advisory: Stage 3 may retain for voice reasons. | Consider: "This raises utilization rates and cuts early-stage losses from low chargeable time." |
| 10 | Para 4, sentence 4 | Composition | Warning | "The clarity of role expectations and a predictable cadence of support enhance engagement" | Two nominalizations in one subject ("clarity of role expectations," "cadence of support") hide the actors and actions. | "Clear role expectations and a predictable support schedule enhance engagement" |
| 11 | Para 5, sentence 4 | Plain Language | Warning | "Success will be measured by shortened time to billable proficiency, reduced first-year turnover, fewer defects and chargebacks, improved manager workload balance, and increased client satisfaction." | Passive construction buries the measuring agent. The sentence is dense with five parallel noun phrases. Advisory; Stage 3 may retain for voice reasons. | "We will measure success by: time to billable proficiency, first-year turnover rate, defect and chargeback counts, manager workload balance, and client satisfaction scores." |
| 12 | Para 4, sentence 3 | AI-Mechanical | Warning | "Buddies develop supervisory capability, strengthening the bench of future managers." | Sentence-final gerund padding: "strengthening the bench of future managers" adds no information beyond what "develop supervisory capability" already states. The sports idiom "bench" is also a Stage 3 note. | Remove or specify: "Buddies develop supervisory capability, building the firm's pool of qualified managers." |
| 13 | Para 4, sentence 1 | AI-Mechanical | Warning | "Associates typically reach billable levels earlier, increasing utilization and reducing early-stage losses associated with low chargeable time." | Two sentence-final gerund phrases (",  increasing utilization and reducing early-stage losses") state effects without quantifying or specifying mechanism. Classic gerund padding pattern. | Rewrite with finite verbs and specifics, or flag for Stage 3 to supply the mechanism. |
| 14 | Para 5, sentence 5 | AI-Mechanical | Warning | "with ongoing governance by L&D and quarterly audits by the partners to ensure effectiveness and alignment with our standards" | Sentence-final gerund phrase "to ensure effectiveness and alignment" is vague padding; it states a purpose that is self-evident from the activity described. | Remove "to ensure effectiveness and alignment with our standards" or replace with the specific standard being audited. |
| 15 | Para 3, sentence 3 | AI-Mechanical | Note | "Chargeable training hours are scheduled and monitored to avoid overburdening clients while providing supervised learning on real files." | In addition to the dangling modifier (Issue 3), this sentence contains three -ing forms ("overburdening," "providing," "learning"), exceeding the three-form detection threshold for present participle overuse. The rewrite resolving Issue 3 will also resolve this pattern. | See Issue 3 fix. |
| 16 | Para 1, sentence 1 | AI-Mechanical | Note | "revitalized onboarding program" | "Revitalized" is a common AI-generated evaluative adjective. Flagged for Stage 3 voice review; not a grammar error. | Stage 3 decision. |
| 17 | Para 5, sentence 1 | Non-Prose | Error | "L&D" | Acronym used without prior expansion in the document body. First use must define it: "Learning and Development (L&D)." | Expand on first use, then use "L&D" for subsequent references. Note: if "learning and development" appears earlier in the same sentence, restructure so the parenthetical expansion follows the first occurrence. |
| 18 | Document title | Non-Prose | Note | "## Internal Proposal: Restructured New-Hire Onboarding Program" | Document uses H2 as its title with no H1. In a standalone proposal document this is acceptable if no parent document exists. If this document will be embedded in a larger file, an H1 is required. | Verify document context; add H1 if embedded. Advisory only. |

---

## Corrected Document

The corrected text below applies all Error-severity fixes and all Warning-severity fixes except
those marked "Advisory; Stage 3 may retain for voice reasons." Notes and Stage 3 items are
flagged inline with [S3] but not changed.

---

## Internal Proposal: Restructured New-Hire Onboarding Program

We propose a [S3: "revitalized"] onboarding program designed to compress ramp time, reduce
risk, and strengthen the culture of a regional accounting firm. The plan focuses on a structured
90-day path that begins with firm foundations and rapidly builds toward job-ready proficiency
under close coaching and shared learning.

The current onboarding experience varies across offices and service lines, and new hires often
feel adrift during the first quarter. New accountants receive inconsistent guidance on basic
standards, unfamiliar clients, and firm policies, which delays chargeable hours, burdens senior
staff with repetitive questions, and increases turnover. Partners report uneven expectations
among client teams, while associates frequently cite unclear advancement benchmarks. These
patterns reflect a fragmented approach rather than a deliberate learning journey.

Our solution introduces a phased, outcomes-focused program that starts with a two-day integration
summit covering firm values, compliance, client service standards, and timekeeping basics. In
week one, associates complete core modules on tax and audit methodologies, document review
workflows, and tools such as firm knowledge bases and practice management systems. A digital
playbook establishes role-based competencies and checklists mapped to typical tasks. Within the
first month, each new hire is paired with a trained buddy for twelve weeks and assigned a coach
who is a senior associate or manager. The training manager holds weekly office hours to address
issues, share quick wins, and reinforce best practices. Chargeable training hours are scheduled
and monitored; associates receive supervised learning on real files without overburdening clients.
By day 45, associates should demonstrate proficiency in a subset of standard procedures; by day
90, they complete a skills audit and a client-readiness review with their manager, identifying
any gaps that require targeted support or mentorship.

We expect early and measurable benefits from this plan. Associates typically reach billable
levels earlier, increasing utilization and reducing early-stage losses associated with low
chargeable time. [Advisory: Stage 3 may revise the gerund chain in the preceding sentence.]
Fewer errors and less rework improve the firm's risk profile and reputation with clients.
Buddies develop supervisory capability, building the firm's pool of qualified managers. Clear
role expectations and a predictable support schedule enhance engagement and reduce first-year
attrition. Knowledge captured in the playbook standardizes quality and makes training scalable
across offices.

Implementation begins with a cross-functional task force (HR, learning and development (L&D),
IT, practice leaders, and three coaches) tasked with drafting the curriculum, digital playbook,
and competency matrix. Training spaces and virtual tools will be configured within four weeks.
We will pilot the program with the next two cohorts, tracking milestones at 30, 45, and 90 days
and gathering feedback through pulse surveys and retrospective sessions. Success will be measured
by shortened time to billable proficiency, reduced first-year turnover, fewer defects and
chargebacks, improved manager workload balance, and increased client satisfaction. [Advisory:
Stage 3 may restructure the preceding sentence for clarity.] After refinements from the pilot,
the program rolls out firmwide by the following quarter, with ongoing governance by L&D and
quarterly audits by the partners.

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

  stage_2_validator:
    status: PENDING

  stage_3_style_editor:
    status: PENDING
```

---

## Handoff Note to Stage 2

The corrected document above is mechanically clean at the Error level. Five grammar errors have
been resolved. Nine composition and plain language warnings have been addressed except where
marked Advisory (two items deferred to Stage 3).

Stage 2 should note the following items that fall within its scope but were observed during
Stage 1 review:

- Para 4 states that associates "typically reach billable levels earlier" — verify that this
  causal claim is supported by firm data or is appropriately hedged as a projection.
- Para 5 states success will be measured by five metrics — verify that measurement methods
  exist for each metric, particularly "client satisfaction" and "manager workload balance."
- The document does not quantify ramp-time targets or turnover baseline figures. Stage 2 should
  assess whether the absence of baselines constitutes an unsupported assumption.
