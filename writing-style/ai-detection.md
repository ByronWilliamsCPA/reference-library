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

## Detector Landscape Notes (2026)

Context that shapes how the rules above should be weighted. The detection market has moved
past "perplexity plus burstiness catches generic ChatGPT prose." Some once-useful defenses
have decayed; a few have reversed into liabilities.

### How Modern Detectors Score Text

Commercial tools (GPTZero, Turnitin, Copyleaks, Originality, Pangram, Winston, Sapling)
now combine several signals rather than relying on perplexity alone:

- Document-level, section-level, and sentence-level classification
- Mixed-authorship categories (human, AI, AI-paraphrased, mixed)
- Continuous-regression / edit-extent scoring (EditLens-family): detection framed as
  "how much of this was AI-assisted" rather than a binary yes/no label
- Retrieval matching against proprietary corpora of previously-scored AI output
  (Copyleaks AI Source Match and similar approaches)
- Explicit handling of humanizer and bypasser tool outputs
- Broad model coverage: GPT-4o/5, Claude 3.5 and 4.x, Gemini 2.x/3.x, DeepSeek, Llama,
  Qwen, and open-weight fine-tunes

Implication: a "low-perplexity, generic ChatGPT" profile is no longer the only profile
that detectors flag. Claude, Gemini, and open-weight outputs are actively scored by
current commercial stacks. Editing an AI draft for voice can reduce binary "looks like
AI" scores while leaving edit-extent scores largely intact; a regression-style detector
can still report "heavily AI-assisted" even after Stage 3 passes.

Operational note on institutional thresholds: some platforms suppress low scores as
statistically unreliable (Turnitin marks scores below 20% with an asterisk and hides the
numeric value). Chasing a 5% versus 15% delta in that band is noise. Reviewers see the
score above 20%; that is the threshold that matters.

### Template and Structural Repetition

Retrieval-based detectors fingerprint structural repetition across documents, not just
surface vocabulary. If the same scaffolding appears across multiple documents generated
from a fixed prompt template (identical heading sequences, same bullet counts, the same
opening gambit, the same closing line), that repeated structure is itself a retrieval
signal independent of the prose.

Operational rule: rotate scaffolding between documents that will cross the same
institutional detector. Avoid reusing identical header sequences, bullet counts, or
formulaic opening and closing lines in two documents headed for the same review pipeline.
The pipeline's own recap and stage-file templates are acceptable because they are
internal artifacts; the submitted document should not inherit their scaffolding.

### Over-Engineering Caveat

Stylometric adjustments that look too deliberate can register as text optimized against
a detector rather than as human prose. Specific failure modes:

- Sentence-length oscillation pushed well beyond the σ ≥ 8 floor, producing mechanical
  alternation rather than natural rhythm
- Punctuation cadences that repeat identically across paragraphs
- Rare synonyms or lexical oddities clustered in predictable positions
- Opener variety so complete that every sentence starts differently in an engineered way

Hit the `style-profile.md` targets. Do not exceed them for theatrical effect. Authentic
voice is more durable than optimized voice, because modern detectors are increasingly
trained against humanizer-style revisions and will flag artifacts of that optimization.

### Paraphrase and Humanizer Detection

Turnitin, QuillBot, and Winston now flag paraphrase passes and humanizer-tool output as a
distinct category, separate from "AI-generated." Running an AI draft through a humanizer
or a second paraphrase pass to scrub patterns can introduce its own detection signature.

Operational rule: rewrite at the sentence and paragraph level by hand (the Stage 3 loop).
Do not route drafts through automated paraphrase or humanizer utilities.

### Non-Native and Constrained-Register Bias

Detectors that lean on low perplexity and reduced lexical variety historically flagged
formal, technical, and non-native-English prose at elevated rates. Liang et al. (Patterns,
2023) reported ~61% false-positive rates across seven detectors on TOEFL essays. Some
vendors claim remediation; independent peer-reviewed replication lags the claims.

Registers common to this library (tax analysis, statutory drafting, regulatory memos,
bar-style exam prose) sit in the risk zone because they are formal, lexically constrained,
and rely on stable defined terminology. Substituting synonyms for variety's sake would
violate both the relevant Oregon style guides and the semantic-preservation rules in the
pipeline.

Operational guidance: when register legitimately constrains vocabulary (defined statutory
terms, elements of a tax test, fixed citation forms), accept a narrower TTR. Let the
register justify the constraint in a Stage 3 rewrite note when the document is likely to
be screened.

### Provenance Signals

Text generated inside Google Gemini surfaces carries SynthID watermarking that survives
light editing and does not get stripped by stylistic rewriting. OpenAI and Anthropic have
not shipped text watermarks in production as of April 2026, though both have disclosed
research work.

Implication: for documents that may enter a watermark-checking workflow, process evidence
(drafting history, revision timeline, source materials) matters more than surface
stylometry. The three-stage pipeline already produces that evidence as a byproduct; keep
stage files rather than only the final rewrite.

Edit-versus-regenerate distinction: paraphrasing or Stage-3 rewriting a watermarked
draft preserves most of the original token sequence, which preserves the watermark.
Regenerating the idea from scratch in a non-watermarked model produces a fully new
token sequence and strips the signal. If a document started inside a watermarked
surface and its provenance must reflect your own process, re-draft from the source
prompt in Claude or another non-watermarked model rather than running the watermarked
output through paraphrase or voice editing.

### What Has Decayed as a Defense

- Burstiness modulation as the primary shield. Still required per `style-profile.md`; no
  longer sufficient on its own.
- Automated paraphrase passes as a cleaning step. Now actively targeted by commercial
  detectors.
- The assumption that Claude output is harder to detect than ChatGPT output. Partially
  true for some tools; no longer safe to rely on.
- Score suppression as the whole strategy. Defensible authorship evidence plus a clean
  draft beats an optimized score under institutional review.

---

## Quick Scan Checklist

Run this before finalizing any document:

- [ ] No terms from the Cliché Blacklist
- [ ] No vague qualifiers without accompanying numbers
- [ ] Sentence length standard deviation ≥ 8 (and not artificially inflated past ~15)
- [ ] Short sentences (< 8 words) ≥ 15% of total
- [ ] Long sentences (> 30 words) ≥ 15% of total
- [ ] Sentence variation reads as natural, not as engineered alternation
- [ ] No repetitive paragraph openers
- [ ] Transition words used sparingly
- [ ] No automated paraphrase or humanizer pass on the final draft
- [ ] Every statistic has a source or is labeled as an estimate
- [ ] Assumptions stated explicitly, not embedded
- [ ] Stage files retained alongside the final rewrite (drafting evidence)
- [ ] Scaffolding (heading sequence, bullet counts, opener/closer lines) is not reused
      verbatim from a prior document heading into the same review pipeline
