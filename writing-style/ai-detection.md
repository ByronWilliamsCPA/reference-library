# AI Pattern Detection Reference

> **Purpose**: Identify and eliminate AI-generated language patterns in professional documents
> **Use**: Review documents before submission; flag anything on these lists for revision

---

## Cliché Blacklist

Instant flags — these terms appear so frequently in AI output that their presence strongly suggests
unrevised AI-generated content.

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

### Additional AI Puffery Terms

Single words that inflate tone without adding meaning.

| Term | Problem | Fix |
| --- | --- | --- |
| pivotal | Overstatement; every AI event is "pivotal" | State what actually changed as a result |
| vital | Same problem as *crucial* | State the consequence of not doing it |
| groundbreaking | Self-awarded; marketing | Describe what is specifically new |
| testament | "A testament to X" — filler construction | State the evidence directly |
| enduring legacy | Vague praise | Describe the specific lasting effect |
| transformative | Same problem as *revolutionary* | Quantify or name the specific change |
| unwavering | Praise word with no content | Remove or describe the specific commitment |
| unparalleled | Absolute claim; rarely defensible | Name what makes it superior or remove |
| exemplary | Praise word | Name the specific quality |

### Empty Gerund Phrases

These constructions appear constantly in AI-generated text. The gerund promises action but
delivers nothing specific.

| Pattern | Problem | Fix |
| --- | --- | --- |
| "ensuring reliability" | What reliability? What makes it reliable? | State the specific measure |
| "showcasing features" | Vague | List which features and why they matter |
| "fostering collaboration" | How? Between whom? | Name the mechanism |
| "driving growth" | How much growth? By what means? | Quantify or specify |
| "enhancing performance" | What performance metric? | State the before/after |
| "delivering value" | To whom? What value? | Be specific |
| "enabling success" | Vague cause-effect | State what the system actually does |

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

**Quantified targets**: The authoritative stylometry targets (σ ≥ 8, TTR ≥ 0.40, hedge density
5–10%) are in `style-profile.md`. The same violations that produce AI-sounding prose also
depress these stylometry scores — the patterns and the metrics describe the same underlying
problem from two angles.

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
| Bullet overuse (analytical prose converted to bullets) | Fragments reasoning; disconnects evidence from conclusion | Rewrite as prose; bullets only for genuinely enumerable, parallel items |
| Overly symmetrical organization | Mechanical | Let the argument determine structure |
| Every paragraph same number of sentences | Robotic | Vary — short paragraphs for emphasis, longer for development |
| Every bullet point same length | AI pattern | Match length to content |
| Excessive bolding (multiple phrases bolded per paragraph, or entire sentences bolded) | Substitutes formatting for prose structure; signals AI-generated emphasis | Bold only critical terms or key distinctions; one instance per section at most |
| Emoji used as formatting decorators in professional documents | Signals unrevised AI output; undermines professional register | Remove entirely; use prose or structural elements for emphasis |

---

## Rewrite Examples

### Converting AI-Speak to Human Voice

**Before (AI-generated)**:

> "This innovative solution will significantly improve operational efficiency by leveraging
> cutting-edge technology to streamline workflows and create synergies across the organization."

**After**:

> "The proposed platform reduces manual reconciliation from 60 to 6 hours per month. It connects
> three currently siloed systems — portfolio management, accounting, and risk — through a shared
> data layer."

---

**Before**:

> "Improve data quality across the organization."

**After**:

> "Increase trade data accuracy from 92% to 99.5% by implementing automated validation at ingestion."

---

### Breaking AI Rhythm

**Before (monotonous)**:

> "The system provides real-time data access. The system enables better decision-making. The system
> reduces operational risk. The system improves compliance."

**After (varied rhythm)**:

> "Real-time data access changes how decisions get made. Instead of waiting three days for
> reconciliation, analysts can rebalance same-day when conditions shift. Risk visibility improves.
> Compliance becomes proactive rather than reactive."

---

### Fixing Over-Hedging

**Before**:

> "This approach could potentially help to somewhat reduce costs in certain situations."

**After**:

> "This approach typically reduces costs by 20–30% in organizations with similar data volumes."

---

## Em-Dash Formulaic Patterns

> **Note**: The PCP override (see `grammar-style/cross-reference.md` #21) bans em-dashes entirely.
> This section aids detection of unrevised AI-generated text, not style enforcement.

AI uses em-dashes in a single repeating pattern: parenthetical insertion between two parts of
a sentence ("X — insertion — Y"). Human writers use em-dashes for several distinct purposes
(amplification, attribution, abrupt break). When AI text contains em-dashes, they almost always
follow the same parenthetical structure.

**Detection signals**:

- More than 2 em-dash pairs per page
- Every em-dash use follows the same "X — insertion — Y" pattern
- Em-dashes appear in multiple consecutive paragraphs

**Cross-reference**: The `grammar-composition-editor` agent detects additional AI-mechanical
patterns (nominalizations, gerund padding, downtoner accumulation) that frequently co-occur
with em-dash overuse.

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
