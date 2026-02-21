# Writing Style Profile

> **Purpose**: Quantified targets for authentic, human-sounding professional prose
> **Scope**: General — applies across personal, CPA, legal, and investment contexts

---

## Stylometry Targets

These are measurable, checkable metrics. Apply to any document before submission.

| Metric | Target | How to Measure |
| --- | --- | --- |
| **Sentence Length** | Avg 17–22 words; σ ≥ 8 | Count words per sentence, calculate mean and standard deviation |
| **Short Sentences** | ≥ 15% under 8 words | Sentences < 8 words ÷ total sentences |
| **Long Sentences** | ≥ 15% over 30 words | Sentences > 30 words ÷ total sentences |
| **Lexical Diversity** | TTR ≥ 0.40 | Unique words ÷ total words (Type-Token Ratio) |
| **Word Repetition** | No content word > 2% of tokens | Check most frequent nouns, verbs, adjectives |
| **Hedge Density** | 5–10% of sentences | Count sentences with hedges ("typically," "often," "suggests") |
| **Paragraph Mix** | Alternating short (2–3 sentences) and long (4–6 sentences) | Scan paragraph lengths — uniform lengths are a tell |

### Measurement Accuracy

LLMs cannot reliably compute precise statistical values (standard deviation, TTR, burstiness)
from text alone. The quantified targets above remain the authoritative specification for two
reasons: they are verifiable when a computation environment is available, and they anchor the
qualitative proxies below.

**Qualitative proxies** (use when computation is not available):

| Metric | Proxy |
| --- | --- |
| Sentence length σ | Read the text aloud. If the rhythm feels monotonous and predictable, σ is likely too low. Natural writing stumbles, pauses, and accelerates. |
| TTR | Scan each paragraph for content words (nouns, verbs, adjectives) appearing 3 or more times. Frequent repetition within a paragraph signals low diversity. |
| Short sentences (< 8 words) | Spot-check: every page should contain at least one punchy, declarative short sentence. If none exist, the text lacks emphasis. |
| Long sentences (> 30 words) | Spot-check: every page should contain at least one sentence that layers an idea with qualifications or multiple clauses. If none exist, the text is choppy. |
| Burstiness (per-paragraph σ) | Compare any paragraph that "feels flat" against one that reads naturally. Flat paragraphs have uniform sentence lengths; natural ones vary. |

**When to compute**: If a Python environment, shell script, or similar tool is available, always
prefer actual measurement over qualitative proxies. The `writing-style-editor` agent should
request computation when the environment supports it.

---

## Sentence Rhythm

### Length Distribution

Natural prose varies. No single length dominates.

- **Primary range**: 12–24 words — most sentences fall here
- **Short punches**: Under 8 words — used for emphasis, transitions, conclusions
- **Complex builds**: Over 30 words — used when layering interconnected ideas, conditions, or qualifications

A document where every sentence is 18–22 words reads as robotic, even if technically correct.

### Rhythm Patterns

Good: short → medium → long → short (variation throughout)

Bad: medium → medium → medium → medium (monotonous)

---

## Voice Characteristics

| Attribute | Description |
| --- | --- |
| **Precision** | Methodical, technically rigorous — specific over vague |
| **Tone** | Professional yet approachable, analytical but human |
| **Confidence** | Assertive with appropriate hedging — never overselling |
| **Structure** | Clear hierarchy, systems-thinking orientation |
| **Thinking style** | Connects specifics to broader frameworks; explicit tradeoff acknowledgment |

---

## Hedging: The Right Amount

Hedging shows intellectual honesty. Too little sounds overconfident; too much sounds weak.

**Appropriate hedges**:

- "This approach typically..."
- "Evidence suggests..."
- "In most cases..."
- "Based on current data..."

**Over-hedged** (weak):

> "This approach could potentially help to somewhat reduce costs in certain situations."

**Appropriately hedged** (confident):

> "This approach typically reduces costs by 20–30% in organizations with similar data volumes."

**No hedge needed** (factual statement):

> "The process currently takes 40 hours per month."

---

## Analogies and Thinking Patterns

When analogies help, draw from these domains:

- **Libraries and information architecture** — filing systems, catalogues, classification
- **Engineering and construction** — foundations, load-bearing structures, specifications
- **Natural systems and ecosystems** — interdependencies, feedback loops, carrying capacity

Connect individual decisions to broader strategy, risk, standards, or governance implications.
If a choice has implications beyond the immediate problem, state them.

---

## Quantification Over Vagueness

State measurable outcomes when possible. If you can't measure it, say so explicitly rather than using a vague qualifier.

| Vague | Better |
| --- | --- |
| "Significantly improve efficiency" | "Reduce processing time from 40 to 5 hours per month" |
| "Better data quality" | "Increase accuracy from 85% to 99%" |
| "Lower costs" | "Eliminate $50K in annual manual workaround costs" |
| "Faster turnaround" | "Cut report delivery from 3 days to same-day" |

When you genuinely don't have a number, use ranges or state the basis:

- "$125K ±$75K (range: $50K–$200K based on scope)"
- "Estimated 20–30% reduction based on comparable implementations"

---

## Tradeoff Transparency

Good analysis acknowledges constraints. Explicitly flag:

- What this approach doesn't do
- What conditions it depends on
- Where uncertainty exists
- What the alternatives cost

Glossing over limitations reduces credibility. Naming them increases it.

---

## Factual Integrity

When generating documents with AI assistance, classify each factual claim:

| Type | Definition | How to Present |
| --- | --- | --- |
| **Sourced Fact** | Directly from cited document or data | Cite explicitly: "Per [source], ..." |
| **Expert Judgment** | Professional inference, not directly sourced | Tag: "Based on experience..." or estimate note |
| **Assumption** | Unstated premise the argument depends on | State explicitly: "This assumes..." |
| **Projection** | Future-oriented claim | Label: "We project..." or "Expected..." |

Do not present assumptions as facts. If the document depends on staffing levels, pricing, or
approval decisions remaining constant, say so.

---

## Relationship to Other References

- **AI pattern detection**: See `ai-detection.md` — the vocabulary and structural patterns that
  produce AI-sounding prose are the same ones that depress stylometry scores. Stylometry
  violations (σ < 8, TTR < 0.40) and AI blacklist terms describe the same underlying problem.
- **Voice and tone**: See `tone-voice.md` — stylometry targets apply within any tone palette.
  A formal scholarly tone can still meet σ ≥ 8; palette choice affects vocabulary, not rhythm.
- **Document-validator integration**: The factual integrity categories (Sourced Fact, Expert
  Judgment, Assumption, Projection) map directly to the `document-validator` claim tags
  (VERIFIED, EXPERT JUDGMENT, ASSUMPTION, UNVERIFIED).
