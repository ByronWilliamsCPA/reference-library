# AI Pattern Detection Reference

> **Purpose**: Identify and eliminate AI-generated language patterns in professional documents
> **Use**: Review documents before submission; flag anything on these lists for revision

---

## Cliché Blacklist

Instant flags — these terms appear so frequently in AI output that their presence strongly suggests unrevised AI-generated content.

### Vague Qualifiers

Replace with specific metrics or remove entirely.

| Term | Problem | Fix |
| --- | --- | --- |
| significantly | Vague — how much? | Use a number or remove |
| substantially | Same problem | Use a number or remove |
| considerably | Same problem | Use a number or remove |
| greatly | Same problem | Use a number or remove |
| highly | Same problem | Be specific about what makes it "high" |
| markedly | Same problem | Quantify or remove |

### Corporate Buzzwords

These carry no information. Replace with what you actually mean.

| Term | Problem | Fix |
| --- | --- | --- |
| leverage | Overused business speak | Use "use," "apply," "draw on" |
| synergies | Hollow | Name what actually combines |
| optimize | Vague | Say what you're improving and how |
| streamline | Vague | Describe what's eliminated or automated |
| empower | Patronizing and vague | Say what capability is being added |
| enable | Often used as filler | State the specific action |

### Hype Words

Suggest marketing copy, not analysis.

| Term | Problem | Fix |
| --- | --- | --- |
| best-in-class | Asserted, not demonstrated | Name the specific capability |
| cutting-edge | Marketing speak | Name the specific technology or approach |
| game-changer | Hyperbole | Quantify the actual impact |
| innovative | Self-awarded | Describe what's new specifically |
| revolutionary | Same problem | Same fix |
| transformative | Same problem | Same fix |
| state-of-the-art | Vague and dated quickly | Be specific |

### AI Filler Phrases

These add no information and signal AI authorship.

| Phrase | Problem | Fix |
| --- | --- | --- |
| delve into | AI tell | "Examine," "review," or just remove |
| crucial | Overused | "Required," "necessary," or state the consequence |
| robust | Vague qualifier | Describe what makes it robust |
| seamless | Promises something; means nothing | Describe the actual integration |
| holistic | Vague | Name the specific components |
| comprehensive | Vague | List what's included |
| it's important to note | Filler — everything in the document is important | Delete; state the point directly |
| in conclusion | Structural tell | Delete; let the conclusion speak |
| in summary | Same problem | Delete |
| to summarize | Same problem | Delete |
| moving forward | Corporate filler | State what happens next and when |
| in today's landscape | Padding | Delete entirely |
| at the end of the day | Cliché | Delete |

---

## Phrase-Level Patterns

More nuanced than single terms — these are common AI constructions.

| AI Pattern | Problem | Revision Strategy |
| --- | --- | --- |
| "Significantly improve [X]" | Vague qualifier + vague outcome | Quantify: "Reduce [X] from Y to Z" |
| "Leverage [tool] to streamline [process]" | Two buzzwords | "Use [tool] to eliminate [specific step]" |
| "Best-in-class solution that meets [need]" | Marketing | "Meets requirements: [A], [B], [C]" |
| "Create synergies between [A] and [B]" | Hollow | "Combine [A] and [B] to achieve [specific outcome]" |
| "Robust framework for [X]" | Vague | Describe what makes the framework adequate |
| "Seamless integration with [system]" | Promise without substance | Describe the actual integration mechanism |
| "Key stakeholders" | Generic | Name them |
| "It's worth noting that..." | Filler | Delete the preamble; state the point |
| "This innovative approach..." | Self-congratulatory | Describe what it does |
| "Cutting-edge technology" | Vague | Name the technology |

---

## Sentence Structure Tells

These patterns appear in AI output but rarely in natural human writing.

### Monotonous Length

**Tell**: All sentences are 18–22 words. Standard deviation < 5.

**Fix**: Vary deliberately. Add short punches. Let complex ideas build across longer sentences.

### Repetitive Openers

**Tell**: Multiple consecutive sentences starting with "This," "The," or "Additionally."

**Fix**: Restructure. Open sentences differently. Lead with the idea, not the subject.

### Transition Stacking

**Tell**: "Additionally," "Furthermore," "Moreover" used multiple times per page.

**Fix**: Use transitions only when needed. Often the connection is clear without them.

### Subject-Verb-Object Monotony

**Tell**: Every sentence follows the same S-V-O pattern with no variation.

**Fix**: Invert occasionally. Lead with the condition, the consequence, or the modifier.

---

## Structural Tells

AI tends to produce documents with unnatural symmetry. Human writers don't.

| Tell | Why It's a Problem | Fix |
| --- | --- | --- |
| Every section exactly the same length | Looks templated | Let content determine length |
| Bullet points always in groups of 3 | Suspiciously neat | List what's actually there |
| Overly symmetrical organization | Mechanical | Let the argument determine structure |
| Every paragraph same number of sentences | Robotic | Vary — short paragraphs for emphasis, longer for development |
| Every bullet point same length | AI pattern | Match length to content |

---

## Rewrite Examples

### Converting AI-Speak to Human Voice

**Before (AI-generated)**:

> "This innovative solution will significantly improve operational efficiency by leveraging cutting-edge technology to streamline workflows and create synergies across the organization."

**After**:

> "The proposed platform reduces manual reconciliation from 60 to 6 hours per month. It connects three currently siloed systems — portfolio management, accounting, and risk — through a shared data layer."

---

**Before**:

> "Improve data quality across the organization."

**After**:

> "Increase trade data accuracy from 92% to 99.5% by implementing automated validation at ingestion."

---

### Breaking AI Rhythm

**Before (monotonous)**:

> "The system provides real-time data access. The system enables better decision-making. The system reduces operational risk. The system improves compliance."

**After (varied rhythm)**:

> "Real-time data access changes how decisions get made. Instead of waiting three days for reconciliation, analysts can rebalance same-day when conditions shift. Risk visibility improves. Compliance becomes proactive rather than reactive."

---

### Fixing Over-Hedging

**Before**:

> "This approach could potentially help to somewhat reduce costs in certain situations."

**After**:

> "This approach typically reduces costs by 20–30% in organizations with similar data volumes."

---

## Quick Scan Checklist

Run this before finalizing any document:

- [ ] No terms from the Cliché Blacklist
- [ ] No vague qualifiers without accompanying numbers
- [ ] Sentence length standard deviation ≥ 8
- [ ] Short sentences (< 8 words) ≥ 15% of total
- [ ] Long sentences (> 30 words) ≥ 15% of total
- [ ] No repetitive paragraph openers
- [ ] Transition words used sparingly
- [ ] Every statistic has a source or is labeled as an estimate
- [ ] Assumptions stated explicitly, not embedded
