# Grammar-Style Index

> Concept-to-file routing map for agent use. Load `QUICK-START.md` first for common questions.
> Load a specific file only when the quick-start answer is insufficient.

## Quick Navigation

**For 80% of questions**: `QUICK-START.md`

**When EoS and CMS conflict**: `cross-reference.md`

---

## Topic-to-File Map

### Punctuation

| Topic | Best File |
| --- | --- |
| Serial comma, Oxford comma | `QUICK-START.md` #1, or `chicago-manual/punctuation.md` |
| Comma in compound sentences | `QUICK-START.md` #2, or `chicago-manual/punctuation.md` |
| Comma after introductory phrase | `QUICK-START.md` #9, or `chicago-manual/punctuation.md` |
| Comma for nonrestrictive clauses | `chicago-manual/punctuation.md` |
| Semicolon uses | `QUICK-START.md` #11, or `chicago-manual/punctuation.md` |
| Colon uses | `QUICK-START.md` #11, or `chicago-manual/punctuation.md` |
| Em-dash (banned by PCP) | `cross-reference.md` #15 and #21 |
| En dash | `QUICK-START.md` #10, or `chicago-manual/punctuation.md` |
| Quotation mark punctuation placement | `QUICK-START.md` #19, or `chicago-manual/punctuation.md` |
| Apostrophe and possessives | `QUICK-START.md` #12–13, or `chicago-manual/punctuation.md` |
| Ellipsis | `cross-reference.md` #19 |

### Grammar

| Topic | Best File |
| --- | --- |
| Active vs. passive voice | `QUICK-START.md` #4, `cross-reference.md` #2 |
| *That* vs. *which* | `QUICK-START.md` #3, `cross-reference.md` #10 |
| *Who* vs. *whom* | `QUICK-START.md` #14 |
| *None*: singular or plural | `QUICK-START.md` #15, `cross-reference.md` #5 |
| Split infinitives | `QUICK-START.md` #6, `cross-reference.md` #4 |
| Dangling modifiers | `QUICK-START.md` #17 |
| Sentence fragments | `QUICK-START.md` #5, `cross-reference.md` #3 |
| Prepositions at end of sentence | `QUICK-START.md` #7 |
| Subject-verb agreement | `chicago-manual/grammar-usage.md` |
| Collective nouns | `chicago-manual/grammar-usage.md` |
| Parallel structure | `chicago-manual/grammar-usage.md` |
| Pronoun agreement | `chicago-manual/grammar-usage.md` |
| Subjunctive mood (*if I were*) | `chicago-manual/grammar-usage.md` |
| *Shall* vs. *will* | `cross-reference.md` #17 |
| *Due to* vs. *because of* | `QUICK-START.md` #20, `cross-reference.md` #8 |

### Numbers

| Topic | Best File |
| --- | --- |
| Spell out vs. numeral | `QUICK-START.md` #8, or `chicago-manual/numbers.md` |
| Dates | `chicago-manual/numbers.md` |
| Percentages | `chicago-manual/numbers.md` |
| Currency and measurements | `chicago-manual/numbers.md` |
| Ordinal numbers | `chicago-manual/numbers.md` |
| Large round numbers | `chicago-manual/numbers.md` |

### Capitalization

| Topic | Best File |
| --- | --- |
| Titles of works | `QUICK-START.md` #18, `chicago-manual/capitalization.md` |
| Proper nouns | `chicago-manual/capitalization.md` |
| Titles of people | `chicago-manual/capitalization.md` |
| Seasons, directions, other common nouns | `chicago-manual/capitalization.md` |

### Word Usage

| Topic | Best File |
| --- | --- |
| Commonly misused word pairs | `elements-of-style/words-expressions.md` |
| *Affect* vs. *effect* | `elements-of-style/words-expressions.md` |
| *Less* vs. *fewer* | `elements-of-style/words-expressions.md` |
| *Comprise* vs. *compose* | `elements-of-style/words-expressions.md` |
| *Imply* vs. *infer* | `elements-of-style/words-expressions.md` |

### Composition Principles

| Topic | Best File |
| --- | --- |
| Omit needless words | `elements-of-style/principles-composition.md` |
| Paragraph structure | `elements-of-style/principles-composition.md`, `cross-reference.md` #6 |
| Positive vs. negative constructions | `elements-of-style/principles-composition.md` |
| Sentence rhythm | `../style-profile.md` |

### Citations and Documentation

| Topic | Best File |
| --- | --- |
| Footnotes and endnotes | `chicago-manual/citations-documentation.md` |
| Notes-bibliography system | `chicago-manual/citations-documentation.md` |
| Author-date system | `chicago-manual/citations-documentation.md` |
| Bibliography entries | `chicago-manual/citations-documentation.md` |
| Short-form citations | `chicago-manual/citations-documentation.md` |
| *Ibid.* usage | `chicago-manual/citations-documentation.md` |

### Tone and Formatting

| Topic | Best File |
| --- | --- |
| Style palettes (Formal, Conversational, etc.) | `../tone-voice.md` |
| PromptCraft Pro defaults | `../tone-voice.md` |
| Markdown structure | `../structural-formatting.md` |
| Heading hierarchy | `../structural-formatting.md` |
| AI patterns to avoid | `../ai-detection.md` |
| Stylometry targets | `../style-profile.md` |

---

## Agent Loading Strategy

Load files selectively by topic rather than loading the entire grammar-style directory.
Typical workflow:

1. Check `QUICK-START.md` — answers 80% of questions in one table.
2. If `QUICK-START.md` points to a conflict, load `cross-reference.md`.
3. If deeper detail is needed, load the specific source file (e.g., `chicago-manual/punctuation.md`).
4. Never load all files at once; the full set exceeds 12,000 tokens.

**Uncertainty tags** (from PromptCraft Pro evaluation protocol):

- `[ExpertJudgment]` — advice is professional inference; reasonable but not directly sourced here
- `[Confidence:Low]` — the rule depends on context, document type, or edition differences
- `[NeedsHumanReview]` — the question exceeds what this reference can resolve; consult the source directly
