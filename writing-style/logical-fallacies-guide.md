# Logical Fallacies in Professional Documents

> **Purpose**: Detect reasoning errors in business cases, strategy documents, and policy proposals
> **Use**: Loaded by the `document-validator` agent during factual review
> **Scope**: Common fallacies that appear in professional and analytical writing

---

## How to Use This Reference

For each claim or argument in the document, check whether the reasoning holds. A factually
accurate claim can still rest on a logical fallacy. The document-validator flags the reasoning
error; the author decides whether to strengthen the argument or qualify the conclusion.

---

## Fallacies

### 1. Appeal to Authority Without Evidence

**Pattern**: Citing a person, organization, or vague consensus as proof rather than presenting
the underlying evidence.

**Example**: "Industry leaders agree that cloud migration reduces costs."

**Detection question**: Is the conclusion supported by evidence, or only by who said it?

**Fix**: Name the specific source and present their evidence. "A 2024 Gartner survey of 500
mid-market firms found average infrastructure cost reductions of 18–25% within 24 months of
cloud migration."

### 2. False Causation

**Pattern**: Presenting a correlation or sequence as a cause-and-effect relationship without
establishing the causal mechanism.

**Example**: "After implementing the new platform, data quality improved by 15%. The platform
caused the improvement."

**Detection question**: Could something else explain the change? Was there a controlled comparison?

**Fix**: State the correlation explicitly and qualify the causal claim. "Data quality improved
by 15% in the six months following platform implementation. Contributing factors may include the
concurrent training program and revised data entry procedures."

### 3. Cherry-Picking (Confirmation Bias)

**Pattern**: Selecting only evidence that supports the preferred conclusion while ignoring
contradictory data.

**Example**: A vendor comparison that highlights the recommended vendor's strengths and
competitors' weaknesses without comparing the same criteria across all options.

**Detection question**: Is there evidence that would weaken this conclusion? Was it considered?

**Fix**: Present a balanced comparison using consistent evaluation criteria. Acknowledge where
the recommended option is weaker than alternatives.

### 4. False Precision

**Pattern**: Stating a number with more specificity than the underlying data supports, creating
an illusion of rigor.

**Example**: "This initiative will save $127,432 annually."

**Detection question**: What is the basis for this exact figure? What assumptions produce it?
What is the confidence interval?

**Fix**: Use ranges or round numbers with stated assumptions. "Estimated annual savings of
$100K–$150K, assuming current staffing levels and vendor pricing from Q3 2025 quotes."

### 5. Non Sequitur

**Pattern**: Drawing a conclusion that does not follow from the stated premises.

**Example**: "Our competitors are adopting AI tools. Therefore, we need a $2M analytics platform."

**Detection question**: Does the conclusion actually follow from the premise? Is there a missing
step in the reasoning?

**Fix**: Connect the premises to the conclusion explicitly. "Competitors' AI adoption is shifting
client expectations for reporting speed. To meet revised SLAs, we need real-time analytics
capability. The proposed platform addresses this specific gap."

### 6. Straw Man

**Pattern**: Misrepresenting an alternative to make the preferred option look better by comparison.

**Example**: "The alternative is to continue with our current manual process, which is error-prone
and unsustainable." (When the actual alternative includes targeted automation improvements.)

**Detection question**: Does the description of each alternative reflect what that option would
actually involve? Would a proponent of the alternative recognize this description?

**Fix**: Describe each alternative as its proponent would present it, then compare on the merits.
Include the strongest version of each option, not the weakest.

### 7. Sunk Cost Fallacy

**Pattern**: Justifying continued investment because of what has already been spent rather than
on the basis of expected future value.

**Example**: "We've already invested $500K in the current platform. Switching now would waste
that investment."

**Detection question**: Would we start this investment today if we hadn't already spent the money?
Is future value driving the decision, or past cost?

**Fix**: Evaluate the go-forward decision independently. "Continuing with the current platform
requires an additional $200K over two years. Switching costs $350K but reduces annual operating
costs by $150K. The switching option has a positive ROI within 30 months regardless of prior
investment."

### 8. Bandwagon / Appeal to Popularity

**Pattern**: Arguing that something is correct or advisable because many others are doing it.

**Example**: "73% of peer organizations have adopted this framework."

**Detection question**: Does adoption by others prove this is right for our specific situation?
Are our constraints and objectives the same?

**Fix**: Evaluate fit for the specific context. "Of the 12 peer organizations that adopted this
framework, the 4 with similar portfolio complexity report [specific outcomes]. Our constraints
differ in [ways], which suggests [tailored conclusion]."

### 9. False Dilemma

**Pattern**: Presenting only two options when more exist, typically framing the choice as "our
proposal or disaster."

**Example**: "We either adopt this platform or accept continued data quality failures."

**Detection question**: Are there really only two options? What about partial measures,
alternative vendors, or phased approaches?

**Fix**: Acknowledge the full range of options. The alternatives section should include at
minimum: status quo, proposed solution, at least one competing approach, and internal build
(if applicable).

### 10. Hasty Generalization

**Pattern**: Drawing a broad conclusion from too few examples or too small a sample.

**Example**: "The pilot with two teams showed productivity gains. This will work across all
200 teams."

**Detection question**: Is the sample representative? Are there reasons the pilot results might
not generalize?

**Fix**: State the scope of the evidence and qualify the projection. "The two-team pilot showed
12% productivity gains over three months. Broader rollout results will depend on team size,
existing tooling, and change management support."

---

## Quick Scan Checklist

Run this over any recommendation or cost-benefit analysis:

- [ ] Are conclusions supported by evidence, not just authority?
- [ ] Are causal claims distinguished from correlations?
- [ ] Does the evidence include data that might weaken the conclusion?
- [ ] Are numbers stated with appropriate precision (ranges, not false precision)?
- [ ] Does each conclusion follow logically from its premises?
- [ ] Are alternatives described fairly, not as straw men?
- [ ] Are forward-looking decisions based on expected value, not sunk costs?
- [ ] Are popularity claims backed by relevance to this specific context?
- [ ] Are all reasonable options presented, not just two?
- [ ] Do generalizations reflect adequate sample size and representativeness?

---

## Relationship to Other References

- **Factual claim classification**: The `document-validator` agent classifies claims as
  VERIFIED / EXPERT JUDGMENT / ASSUMPTION / UNVERIFIED / SUSPECT. Logical fallacies can
  appear in any category — a verified statistic can still be used in a cherry-picked argument.
- **False precision overlap**: False precision appears both here and in the validator's
  hallucination detection. The validator checks whether the number exists; this guide checks
  whether the precision is warranted.
- **AI detection overlap**: AI-generated text frequently contains appeal-to-authority and
  bandwagon arguments. See `ai-detection.md` for AI-specific patterns.
