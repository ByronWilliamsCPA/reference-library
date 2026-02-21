# Tone and Voice Reference

> **Source**: Derived from PromptCraft Pro C.R.E.A.T.E. Framework, 06 Tone-and-Format.md §1.3
> (May 2025). Not copyrighted reference material — internal PromptCraft Pro framework defaults.

## Authority

Tone and voice selection is a pre-writing decision. Choose a style palette first; then apply the
grammar rules from `grammar-style/` within that voice.

When combining palettes, use a **Tone Hierarchy** directive to resolve conflicts:
`"Maintain formal tone; allow conversational analogies only."`

## Style Palettes

| Palette | Domain | Characteristic Signals | Activation Trigger |
| --- | --- | --- | --- |
| Formal/Scholarly | Legal, academic | Latinate vocabulary; passive voice acceptable; footnotes or endnotes; no contractions | "Use a formal scholarly tone with citations." |
| Warm/Conversational | Client letters, explainers | Contractions; second-person ("you"); plain language; analogies | "Explain in plain English, suitable for clients." |
| RFC-style | IT documentation | Numbered MUST/SHOULD/MAY; requirement language; defined terms in ALL-CAPS | "Respond in RFC-style prose with MUST/SHOULD." |
| Authoritative Practitioner | Tax, compliance, regulatory | Inline statute/regulation citations; directive language; present-tense rules | "Write as an authoritative practitioner." |
| C-Suite Neutral | Fiscal analysis, policy briefs | Executive summary up front; bullet lists; no jargon; metrics over prose | "Provide a C-suite brief with key bullets." |
| Exam-Style Q&A | Tax, compliance, bar prep | Question headers; statutory citations (IRC §, ORS §); concise answers; no preamble | "Answer in exam-style, cite IRC Section 61(a)(1)." |
| Plain-Language | Public policy, general audience | Minimal jargon; analogies for complex concepts; simple sentence structure | "Use plain-language suitable for non-technical readers." |
| Peer-Code-Review | Software development | Inline comment tags; style-guide references; specific line citations; suggestions not demands | "Provide peer-code-review comments per Google standard." |

## PromptCraft Pro Defaults (Applied Unless Overridden)

These defaults apply to all palettes unless a specific palette or user instruction overrides:

- **Contractions**: Permitted ("it's," "don't," "we'll")
- **Em-dashes**: **Banned.** Use commas, colons, semicolons, or parentheses instead
- **Lists**: Use only when the user explicitly requests steps or a list; otherwise use narrative prose
- **Commas**: For asides and parenthetical insertions
- **Colons**: For expansion, elaboration, and introducing examples
- **Semicolons**: For linking closely related independent clauses

## Rhetorical Devices

Apply one or two for subtle effect; combining more than two becomes noise.

| Device | Effect | Trigger |
| --- | --- | --- |
| Analogies for lay readers | Clear metaphors connecting complex concepts to familiar ideas | "Incorporate analogies for non-technical readers." |
| Rhetorical questions | Socratic hooks that engage the reader | "Use rhetorical questions to prompt reflection." |
| Sentence-length burstiness | Varied cadence mixing short and long sentences | "Encourage sentence-length burstiness (12–24 words avg)." |
| Dry wit/mild humor | Light humor without informal tone | "Add a touch of dry wit, no more than one quip per section." |
| Negative constraints | Suppress unwanted patterns | "Avoid bigrams and limit exclamation marks." |
| Voice perspective | Switch first/second/third person | "Write in second person, addressing the reader as 'you.'" |

## Stylometry Targets (PromptCraft Pro Defaults)

For measurable targets, see `style-profile.md`. Summary:

- Avg sentence length: 17–22 words; σ ≥ 8
- Short sentences (< 8 words): ≥ 15%
- Long sentences (> 30 words): ≥ 15%
- Lexical diversity (TTR): ≥ 0.40; no content word > 2% of tokens
- Hedge density: 5–10% of sentences
- Paragraph mix: alternate short (2–3 sentences) and long (4–6 sentences)
