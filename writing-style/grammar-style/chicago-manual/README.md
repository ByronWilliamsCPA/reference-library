# Chicago Manual of Style Reference

> **Source**: *The Chicago Manual of Style*, 17th edition (2017). University of Chicago Press.
> Copyright retained by the publisher.
>
> **Copyright compliance**: Rules are paraphrased in the user's own words. CMS section
> references (§X.XX) are provided so you can look up the original text. No verbatim
> reproduction of CMS prose appears in these files. The underlying facts and rules — ideas
> and principles — are not copyrightable; only the specific expression is.
>
> **Paraphrase standard**: Every rule states the condition and result — "If X, then Y" — not
> just a section pointer. An LLM needs the logic.
>
> **Edition tag**: When a rule changes in a future CMS edition, mark the update
> `[CMS 18th ed. change]`.

## Files in This Directory

| File | CMS Chapter(s) | Contents |
| --- | --- | --- |
| `grammar-usage.md` | Ch. 5 | Parts of speech edge cases, agreement, voice, mood, parallel structure |
| `punctuation.md` | Ch. 6, 7 (partial) | Comma, semicolon, colon, en dash, quotation marks, apostrophe |
| `numbers.md` | Ch. 9 | Spell out vs. numeral, dates, percentages, measurements, ordinals |
| `capitalization.md` | Ch. 8 | Titles, proper nouns, titles of people, common lowercase exceptions |
| `citations-documentation.md` | Ch. 14–15 | Notes-bibliography system; author-date system; bibliography formats |
| `common-errors.md` | Various | Most-looked-up rules in one quick-answer file |

## How CMS Fits the Authority Hierarchy

CMS is the **Tier 2 editing authority**. When EoS and CMS conflict, CMS governs. When neither
addresses a question, prefer plain-English usage.

One user-confirmed Tier 3 override supersedes CMS: **no em-dashes** (PromptCraft Pro default).
See `../cross-reference.md` #21.

## Note on File Size

Each file targets approximately 2,000 tokens. `punctuation.md` and `grammar-usage.md` cover
large CMS chapters and may approach the limit. If a file grows past 3,000 tokens, split it
at a logical section boundary and update `../index.md` routing.
