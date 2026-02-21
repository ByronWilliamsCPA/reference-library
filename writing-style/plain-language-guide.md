# Plain Language Guide

> **Purpose**: Write clearly for the reader, not the writer
> **Source**: Federal Plain Language Guidelines (plainlanguage.gov), Plain Writing Act of 2010,
> Zinsser's *On Writing Well* principles
> **Scope**: All professional documents — business cases, strategy memos, policy briefs, governance proposals

---

## Core Principles

Plain language is not dumbed-down language. It is clear, concise writing that lets the reader
understand the message the first time they read it. Complex ideas can be expressed plainly;
jargon and unnecessary complexity cannot.

### 1. Write for Your Reader

Identify the audience before drafting. Ask:

- Who will read this?
- What do they already know?
- What do they need to do after reading it?
- What decisions will this document inform?

Structure the document so the most important information comes first (inverted pyramid). Executive
readers scan; put the conclusion before the evidence.

### 2. Organize for Understanding

- Lead with the main point — don't bury it
- Group related information together
- Use headings that tell the reader what each section contains
- Place conditions before actions: "If the data fails validation, reject the record" (not "Reject
  the record if the data fails validation")

### 3. Use Everyday Words

Replace complex words with simpler alternatives when meaning is preserved. Technical terms are
acceptable when the audience expects them — but define each on first use.

| Complex | Plain | Notes |
| --- | --- | --- |
| utilize | use | Always |
| facilitate | help, support | Always |
| commence | start, begin | Always |
| terminate | end, stop | Always |
| subsequent | next, later | Always |
| prior to | before | Always |
| in the event that | if | Always |
| in order to | to | Always |
| with respect to | about, on | Always |
| notwithstanding | despite, even though | Always |
| pursuant to | under, following | Legal contexts may retain |
| promulgate | issue, publish | Legal contexts may retain |
| effectuate | carry out, implement | Always |
| hereinafter | (omit — use the short form directly) | Always |
| aforementioned | (omit — name the specific thing) | Always |
| methodology | method | Unless distinguishing from method |
| functionality | function, feature | Always |
| implementation | setup, launch, rollout | Context-dependent |
| operationalize | put into practice | Always |
| paradigm | model, framework | Unless quoting a source |
| stakeholder | (name the actual group) | When possible |

### 4. Keep Sentences Focused

One idea per sentence. One topic per paragraph. When a sentence tries to do two things, split it.

**Before**: "The committee reviewed the proposal and after considerable discussion decided to
table it until the next meeting because several members had questions about the cost estimates
that had not been addressed in the supporting documentation."

**After**: "The committee reviewed the proposal. Several members raised unanswered questions about
the cost estimates. The committee tabled the decision until the next meeting."

### 5. Eliminate Clutter

Zinsser's core principle: every word that serves no function, every long word that could be short,
every adverb that carries the same meaning as the verb, every construction that circles back on
itself — strip them all out.

| Cluttered | Clean |
| --- | --- |
| at this point in time | now |
| in light of the fact that | because |
| is in a position to | can |
| it is important to note that | (delete — state the point) |
| the reason for this is that | because |
| it should be pointed out that | (delete) |
| a number of | several, many |
| the vast majority of | most |
| on the order of | about |
| in close proximity to | near |
| has the ability to | can |
| is indicative of | indicates, shows |
| take into consideration | consider |
| make a determination | determine, decide |
| conduct an investigation | investigate |
| give consideration to | consider |
| make an adjustment to | adjust |
| is dependent on | depends on |

### 6. Address the Reader Directly

Use "you" and "we" when appropriate. Passive constructions hide who acts and who is responsible.

**Passive**: "It has been determined that the policy will be revised."

**Direct**: "We will revise the policy."

This does not apply to all contexts. Formal governance documents, legal instruments, and standards
may require impersonal construction. Match the tone palette in use (see `tone-voice.md`).

---

## Readability Targets

Use these as guidelines, not rigid rules. Voice and persona requirements (see `style-profile.md`)
take precedence when they conflict with simplification targets.

| Metric | Professional/Executive | Technical | General Audience |
| --- | --- | --- | --- |
| Flesch-Kincaid Grade Level | 10–14 | 12–16 | 8–10 |
| Flesch Reading Ease | 40–60 | 30–50 | 60–70 |

**Interpretation**:

- Grade Level 10–14 means a college-educated reader can follow without rereading
- Reading Ease 40–60 is typical for business and policy documents
- Lower grade levels are better for documents reaching broad audiences
- Technical documents serving specialist audiences can run higher

**Measurement note**: LLMs cannot reliably compute Flesch-Kincaid scores from text alone.
When a computation environment is available, use it. Otherwise, apply the qualitative checks:
Can you read each paragraph aloud without stumbling? Would a colleague outside your specialty
follow the argument?

---

## Accessibility Considerations

Plain language is an accessibility practice, not just a style preference.

- Define acronyms on first use (treat executive summary and body as separate scopes)
- Provide text equivalents for any visual content (tables, diagrams)
- Use logical heading hierarchy for screen reader navigation (see `structural-formatting.md`)
- Avoid idioms that don't translate across cultures when the audience is international
- For documents that will be converted to HTML or PDF, maintain structural markup (headings,
  lists, tables) that assistive technology can parse

Cross-reference: `structural-formatting.md` for WCAG 2.2 and Section 508 requirements.

---

## Inclusive Language

Write so every reader feels addressed, not excluded.

### Person-First Language

Refer to people before their characteristics.

| Avoid | Prefer |
| --- | --- |
| the disabled | people with disabilities |
| the elderly | older adults |
| diabetics | people with diabetes |
| the homeless | people experiencing homelessness |

### Gender-Neutral Defaults

Use gender-neutral language unless referring to a specific person whose pronouns are known.

- Use "they/them" as a singular pronoun (CMS §5.256 endorses this)
- Use role titles: "the analyst," "the officer," "the reviewer"
- Avoid "he/she" or "s/he" constructions — rewrite or use "they"

### Ableist Metaphor Alternatives

These metaphors are common in business writing. Replace them when the literal meaning creates
exclusion.

| Metaphor | Alternative |
| --- | --- |
| blind spot | gap, oversight, unexamined area |
| crippling | severe, debilitating, damaging |
| tone-deaf | unaware, insensitive, out of touch |
| falling on deaf ears | being ignored, going unheard |
| lame | weak, unconvincing, inadequate |
| sanity check | confidence check, logic check, validation |
| grandfathered in | exempt, pre-existing, legacy |

### Culturally Neutral Idioms

When writing for international or cross-cultural audiences, avoid idioms that assume shared
cultural context.

| Culture-Specific | Neutral Alternative |
| --- | --- |
| hit a home run | succeeded, delivered strong results |
| move the goalposts | change the criteria |
| boil the ocean | attempt too much, overscope |
| low-hanging fruit | quick wins, easy improvements |
| drink the Kool-Aid | accept uncritically |
| come to Jesus moment | decisive turning point |

---

## Relationship to Other References

- **Grammar rules**: See `grammar-style/QUICK-START.md` — plain language doesn't override grammar
- **Voice and tone**: See `style-profile.md` and `tone-voice.md` — voice requirements take
  precedence over simplification when they conflict. A formal scholarly tone may use Latinate
  vocabulary that plain language guidelines would flag. The tone palette governs.
- **Structural formatting**: See `structural-formatting.md` — heading hierarchy and accessibility
  requirements complement plain language
- **AI detection**: See `ai-detection.md` — many AI patterns (buzzwords, filler phrases) violate
  plain language principles. The grammar-composition-editor flags both simultaneously.
- **Transition overuse**: See `transition-words-reference.md` — reflexive use of "Additionally,"
  "Furthermore," and "Moreover" is both a plain language violation (clutter) and an AI pattern.
  That reference provides usage rules and detection heuristics for all transition categories.
