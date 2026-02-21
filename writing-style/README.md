# Writing Style Reference

> **Purpose**: Quantified writing style profile, AI pattern detection, grammar and composition
> reference — not project-specific, applies across all contexts
> **Scope**: Professional documents, legal writing, technical and general prose

## Files

| File | Purpose |
| --- | --- |
| [`style-profile.md`](style-profile.md) | Sentence metrics, rhythm targets, lexical diversity, hedge density |
| [`ai-detection.md`](ai-detection.md) | Blacklisted terms, structural tells, rewrite strategies |
| [`tone-voice.md`](tone-voice.md) | 8 PromptCraft Pro style palettes with domain mapping and triggers |
| [`structural-formatting.md`](structural-formatting.md) | Markdown rules, heading hierarchy, WCAG accessibility notes |
| [`plain-language-guide.md`](plain-language-guide.md) | Federal plain language principles, readability targets, inclusive language |
| [`logical-fallacies-guide.md`](logical-fallacies-guide.md) | 10 fallacies with detection questions and fixes; Stage 2 reference |
| [`transition-words-reference.md`](transition-words-reference.md) | Transition categories, usage rules, AI overuse detection |

## Grammar and Style Reference (`grammar-style/`)

A modular grammar and composition reference based on a three-tier authority hierarchy:

| Tier | Source | Applies When |
| --- | --- | --- |
| 1 (base) | **Elements of Style** (EoS) | Drafting baseline; applies when CMS is silent |
| 2 (editing authority) | **Chicago Manual of Style**, 17th ed. (CMS) | Final answer on grammar, punctuation, numbers |
| 3 (user-confirmed overrides) | **PromptCraft Pro** defaults | Specific cases where user preference overrides CMS |

**One confirmed Tier 3 override**: no em-dashes. CMS §6.85–6.87 permits them; PCP bans them.
Use commas, colons, semicolons, or parentheses instead. See `grammar-style/cross-reference.md` #21.

### Navigation

**Start here for most questions**: [`grammar-style/QUICK-START.md`](grammar-style/QUICK-START.md)

**EoS/CMS conflicts**: [`grammar-style/cross-reference.md`](grammar-style/cross-reference.md)

**Topic lookup**: [`grammar-style/index.md`](grammar-style/index.md)

### Grammar-Style Directory Map

| File | Contents |
| --- | --- |
| `grammar-style/QUICK-START.md` | 20 high-frequency rules; start here for 80% of questions |
| `grammar-style/cross-reference.md` | 21 EoS/CMS/PCP divergences with resolution |
| `grammar-style/index.md` | Concept-to-file routing map for agents |
| `grammar-style/elements-of-style/rules-of-usage.md` | Strunk's 8 elementary rules (public domain) |
| `grammar-style/elements-of-style/principles-composition.md` | 11 composition principles |
| `grammar-style/elements-of-style/words-expressions.md` | Commonly misused word pairs |
| `grammar-style/chicago-manual/grammar-usage.md` | CMS Ch. 5: agreement, voice, mood, parallel structure |
| `grammar-style/chicago-manual/punctuation.md` | CMS Ch. 6: comma, semicolon, colon, en dash, quotation marks |
| `grammar-style/chicago-manual/numbers.md` | CMS Ch. 9: spell-out vs. numeral rules |
| `grammar-style/chicago-manual/capitalization.md` | CMS Ch. 8: titles, proper nouns, government terms |
| `grammar-style/chicago-manual/citations-documentation.md` | CMS Ch. 14–15: notes-bibliography + author-date |
| `grammar-style/chicago-manual/common-errors.md` | 20 most-looked-up rules in one quick-answer file |

## How These Are Used

The `writing-style-editor` agent uses these files to evaluate documents against quantified
targets, check grammar and style rules, and flag AI-generated patterns. Load files selectively
by topic; never load the full grammar-style directory at once (exceeds 12,000 tokens).

**Agent loading sequence**:

1. Check `grammar-style/QUICK-START.md` — answers 80% of questions.
2. If a conflict exists, load `grammar-style/cross-reference.md`.
3. For deeper rules, load the specific CMS or EoS file.
4. For topic routing, use `grammar-style/index.md`.

Project-specific agents extend this base by adding domain terminology and context-specific rules.
