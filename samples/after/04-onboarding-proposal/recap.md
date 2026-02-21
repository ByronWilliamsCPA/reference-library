# Pipeline Recap: 04 — Onboarding Proposal

## Document Overview

| Field | Value |
| --- | --- |
| Format | proposal |
| Topic | New-hire onboarding program restructure for regional accounting firm |
| Word count (before) | 488 |
| System prompt | none (raw baseline) |
| Model | minimax/minimax-m2 |

## Before State

The document is a five-paragraph internal proposal recommending a structured 90-day onboarding
program. The writing is fluent and well-organized but reads as unrevised AI output: it opens with
puffery ("a revitalized onboarding program"), leans on jargon ("outcomes-focused program"), and
strings benefits together with gerund padding ("increasing utilization and reducing early-stage
losses") that restates effects without explaining mechanism. The Benefits paragraph is the
document's most significant weakness — five sentences each asserting a projected outcome as an
established fact, with no sources, no baselines, and no acknowledgment of risk or uncertainty.

## Stage 1 — Grammar and Composition

**Status**: NEEDS WORK

**What was found** (counts):

- Grammar errors: 5
- Composition issues: 4
- Plain language flags: 1
- AI-mechanical flags: 6

**Key fixes applied**:

- Em-dashes replaced with parentheses (Issue 1): "task force—HR, learning and development, IT,
  practice leaders, and three coaches—tasked" became "task force (HR, learning and development
  (L&D), IT, practice leaders, and three coaches) tasked" — required by the PCP Tier 3 override
  banning em-dashes, which also triggered the L&D expansion on first use.
- Dangling modifier corrected (Issue 3): "Chargeable training hours are scheduled and monitored
  to avoid overburdening clients while providing supervised learning on real files" (hours cannot
  provide learning) became "Chargeable training hours are scheduled and monitored; associates
  receive supervised learning on real files without overburdening clients."
- Fewer/less correction (Issue 4): "Fewer errors and rework improve the firm's risk profile"
  became "Fewer errors and less rework improve the firm's risk profile" — "rework" is a mass noun
  requiring "less."
- Ambiguous preposition fixed (Issue 2): "assigned a coach from a senior associate or manager"
  became "assigned a coach who is a senior associate or manager."
- Numeral spelled out (Issue 5): "paired with a trained buddy for 12 weeks" became "for twelve
  weeks" per CMS §9.2–9.3.
- Passive voice converted and compound noun corrected (Issue 7): "Weekly office hours are held by
  the training manager" became "The training manager holds weekly office hours"; "quick-wins"
  corrected to "quick wins."
- Redundant compound removed (Issue 8): "a client-ready readiness review" became "a
  client-readiness review."

**Deferred to later stages**:

Two advisory items were flagged but not changed: the gerund chain in the Benefits lead sentence
("increasing utilization and reducing early-stage losses") and the dense five-metric sentence in
the Implementation paragraph. Both were marked "Advisory; Stage 3 may retain for voice reasons."
The word "revitalized" was flagged as an AI evaluative adjective and marked [S3] for Stage 3
decision. Stage 1 also noted for Stage 2 that the Benefits paragraph lacked baselines and causal
support, and that the five named metrics had no measurement methods defined.

## Stage 2 — Factual Validation

**Status**: CONDITIONAL

**What was found** (counts):

- Claims analyzed: 22 (Verified: 0, Expert Judgment: 7, Unverified: 11, Assumptions: 4,
  Suspect: 0)
- Reasoning errors: 5
- Hidden assumptions: 7

**Key findings**:

- The entire Benefits paragraph (five sentences) is unsourced. Every projected outcome — earlier
  billable proficiency, fewer errors, buddy skill development, engagement gains, playbook
  scalability — is stated as established fact with no firm data, no external citation, and no
  causal mechanism. Zero claims in the document were independently verified.
- Five false causation errors were logged, concentrated in the Benefits paragraph. Representative
  example: "Clear role expectations and a predictable support schedule enhance engagement and
  reduce first-year attrition" (Reasoning Error #2) asserts two causal steps as fact — that the
  program will produce role clarity, and that role clarity will reduce attrition — without
  evidence for either link.
- The five named success metrics ("shortened time to billable proficiency," "reduced first-year
  turnover," "fewer defects and chargebacks," "improved manager workload balance," "increased
  client satisfaction") each lack a baseline, a target value, a measurement instrument, and an
  attribution methodology. The metrics section names categories, not measures.
- Seven hidden assumptions were logged, including: baseline data exists and is accessible for
  pilot comparison; the two pilot cohorts are large and representative enough to produce valid
  results; IT configuration and content development can both be completed in four weeks; and
  buddy/coach participants have sufficient billable capacity to take on the role.
- A non-sequitur reasoning error (Reasoning Error #5) applies to the metrics sentence: listing
  metric names does not constitute a measurement plan, but the document treats the list as if it
  does.

**Bias assessment**:

The Benefits paragraph exhibits both Confirmation Bias (five projected positives, no failure
modes or conditions of success acknowledged) and Optimism Bias (every projection framed as an
expected improvement, with no conservative scenario, no acknowledgment that initial pilot results
may be mixed, and no trigger criteria specified for the firmwide rollout decision).

## Stage 3 — Voice and Style

**Status**: NEEDS WORK

**Stylometry** (before → after):

- Sentence length σ: 7.1 → target ≥ 8 (resolved in rewrite)
- Short sentences: 0.0% → target ≥ 15% (resolved in rewrite)
- Long sentences: 4.2% → target ≥ 15% (resolved in rewrite)
- AI patterns: 3 → 0 (all three resolved in rewrite)

**Key fixes applied**:

- "revitalized" removed (Issue 1): Replaced with "new" and the opening restructured so the
  90-day path is the lead structural anchor rather than an evaluative adjective.
- "outcomes-focused" removed (Issue 2): Replaced with "phased around three proficiency
  milestones at days 30, 45, and 90" — specific and self-explanatory rather than jargon.
- Gerund chain resolved simultaneously with Stage 2 epistemic correction (Issue 3): "Associates
  typically reach billable levels earlier, increasing utilization and reducing early-stage losses
  associated with low chargeable time" was rewritten as a complex sentence naming the expected
  mechanism and explicitly flagging pilot measurement as the basis for confirmation. One rewrite
  resolved the Stage 1 advisory, the Stage 2 false causation error, and the rhythm problem.
- Benefits paragraph restructured to break flat σ = 2.5 rhythm (Issue 4): The five short,
  formulaic noun-subject sentences were rewritten as a sustained analytical paragraph with varied
  length and opening structures, reframing all five claims as pilot hypotheses rather than
  established outcomes. The paragraph grew substantially and carries the Stage 2 epistemic
  qualifications woven into the prose rather than appended as tags.
- Risks paragraph added (after Benefits): A new paragraph explicitly names the three most
  significant program assumptions — buddy/coach capacity constraints, partner governance
  commitment, and pilot cohort size and representativeness — resolving Stage 2's Confirmation
  Bias and Optimism Bias findings. This is new content added by Stage 3 per Stage 2's
  requirement for a Risks and Mitigations section.
- Metrics sentence flagged for human completion rather than rewritten speculatively: Stage 3
  restructured the sentence to show the required format for each metric (baseline, target,
  measurement instrument, measurement window) but inserted bracketed placeholders for actual
  firm data. The section is marked "[AUTHOR TO COMPLETE]" because inventing baseline figures
  would introduce unverified claims.

## Final State

After all three stages, the document is structurally cleaner, mechanically correct, and
epistemically honest. The Benefits paragraph no longer asserts projected outcomes as facts; it
presents them as design intentions and pilot hypotheses, names the causal mechanisms, and
acknowledges what each claim depends on. A new Risks paragraph addresses the most significant
program assumptions. The prose has more rhythmic variation, the AI-generated puffery terms have
been replaced, and the implementation section is more precise about parallel workstreams and
contingencies. What the document cannot finalize without human input is the metrics section:
five bracketed placeholders require the author to insert current firm baselines and targets before
the document can be submitted. Stage 2 also requires a targeted recheck on the rewritten Benefits
paragraph and the new Risks paragraph before the document is cleared.

## What This Sample Demonstrates

- How the pipeline handles a factually thin Benefits paragraph: Stage 1 flags the gerunds and
  defers them; Stage 2 identifies five unsourced causal claims and five incomplete metrics;
  Stage 3 rewrites the paragraph to carry the epistemic corrections while simultaneously
  resolving the rhythm and AI pattern issues — a single coordinated rewrite across all three
  concerns.
- Cross-stage coordination: the Stage 2 handoff note explicitly requested that voice rewrites
  and factual framing corrections be applied in the same pass rather than sequentially, and
  Stage 3 executed that directly.
- The pipeline's limit: Stage 3 cannot invent firm data. When metric baselines are missing, the
  correct output is a structured placeholder, not a fabricated number. This sample shows what
  a responsibly incomplete rewrite looks like.
- Bias detection in professional documents: the Confirmation Bias and Optimism Bias findings
  illustrate how a plausible, well-intentioned proposal can have a structurally one-sided
  argument that a credible partner audience would notice, and how adding a Risks paragraph
  addresses both patterns without undermining the proposal's case.
- The em-dash fix as a tier-three override in practice: the document used two em-dashes as
  parenthetical delimiters, which is grammatically standard. Stage 1 replaced them with
  parentheses because the PCP Tier 3 override bans em-dashes entirely — illustrating how
  user-confirmed style preferences take precedence over CMS defaults.
