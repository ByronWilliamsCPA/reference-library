# Structural Formatting Reference

> **Source**: Derived from PromptCraft Pro C.R.E.A.T.E. Framework, 06 Tone-and-Format.md §4
> (May 2025). Internal framework defaults — not external copyrighted material.

## PromptCraft Pro Defaults

Unless the user explicitly requests a different structure, all output follows these rules:

- **Prose over lists**: Write narrative prose. Use bullet or numbered lists only when the user
  explicitly asks for steps, a list, or items.
- **No unsolicited formatting**: Do not add bold, headers, or tables unless the content requires
  them or the user requested structure.
- **No em-dashes**: Banned entirely. Substitute commas, colons, semicolons, or parentheses.

### When Lists Are Triggered

**Explicit requests** — use a list when the user says or implies one of these:

- "List the steps / requirements / options / risks"
- "Give me a numbered process" / "Walk me through the steps"
- "What are the items / factors / criteria?"
- "Summarize as bullet points" / "In bullet form"
- "Break this down" (when context makes a list the obvious structure)

**Implicit triggers** — use a list when the content is genuinely enumerable and unordered:

- Checklist items that will be acted on independently
- Reference items the reader will scan rather than read linearly

**Not a list trigger** — write prose for:

- Analytical responses explaining why or how (even if there are multiple reasons)
- Narrative summaries or descriptions
- Recommendations with connected reasoning
- Responses fewer than 4 items that flow naturally in prose ("The three factors are X, Y, and Z.")

## Heading Hierarchy

Always maintain semantic heading order. Never skip levels.

```text
# H1 — Document title (one per document)
## H2 — Major sections
### H3 — Subsections
#### H4 — Sub-subsections (use sparingly)
```

**Accessibility note**: Logical heading hierarchy is required for screen reader navigation and
compliance with WCAG 2.2 and Section 508 of the Rehabilitation Act. Automated converters
(HTML, PDF/UA) depend on it.

## Formatting Triggers

Use these phrases in prompts to request specific structural formats:

| Request | Trigger Phrase |
| --- | --- |
| Headed sections | "Use H2/H3 headings for main sections and sub-sections." |
| Numbered steps | "Present the steps as a numbered list." |
| Bulleted items | "List the items as bullet points." |
| Code blocks | "Wrap code in triple backticks using [language] syntax highlighting." |
| Markdown tables | "Use inline Markdown tables." |
| Slide content | "Format as 5×5 rule (≤5 bullets of ≤5 words per slide)." |

## Code Blocks

Always specify a language identifier on the opening fence:

````text
```python
# Python code here
```

```bash
# Shell commands here
```

```text
# Plain text or tree diagrams here
```
````

## Tables

Use Markdown table format. Place definitions adjacent to the term they define. Prefer tables over
bulleted definition lists when comparing two or more attributes across multiple items.

**When tables are appropriate**:

- Comparing attributes across 3+ items (use table; fewer items → prose or list)
- Reference data users will scan non-linearly (e.g., code keys, option comparisons)
- Structured data with a consistent schema (all rows have the same columns)

**When tables are NOT appropriate**:

- Fewer than 3 rows of data (write prose)
- More than 6 columns (too wide for most contexts; restructure or split)
- Narrative or sequential content (use prose or numbered list instead)
- When most cells would be empty or "N/A" (sparse tables are harder to read than prose)

**Cell conventions**:

- Left-align text columns; right-align numeric columns
- Use "N/A" (not a blank) for intentionally empty cells
- Keep header labels concise (2–4 words); add a note below the table if headers need explanation
- Do not use merged cells in Markdown tables (not supported in most renderers)

## Markdown Validity

For critical documents, add a QA check: "Ensure all Markdown is valid (headers, lists, code blocks
properly rendered)." Malformed Markdown degrades output in rendered environments.

## Document Length Tiers (PromptCraft Pro)

Reference tiers for specifying output length when needed:

| Tier | Approx. Word Count | Typical Use | When to Choose |
| --- | --- | --- | --- |
| 1 | 100–200 words | Quick answer, tweet-length summary | Single direct question; user asks for the short version |
| 2 | 200–400 words | Short memo, email, brief explanation | Response to a clear question with 2–3 supporting points |
| 3 | 350–600 words | Executive summary, short brief | User asks for a summary or overview; standard email memo |
| 4 | 600–900 words | Standard memo, analysis section | Single-topic analysis; one section of a longer document |
| 5 | 900–1,500 words | Full policy brief, detailed report section | Multi-part analysis; standalone document with recommendation |
| 6+ | 1,500+ words | Long-form analysis, full report | Comprehensive analysis, full report, multi-section deliverable |

**Default behavior**: When the user does not specify a length, infer the tier from context:

- Conversational question → Tier 1–2
- Request for explanation or analysis → Tier 3–4
- Request for a document, brief, report, or memo → Tier 4–5
- Explicit "comprehensive" or "full" → Tier 5–6+

Specify tier in prompts: "Tier 3 response" or "approximately 400 words."

## Accessibility (WCAG 2.2 and Section 508)

Heading hierarchy is the most common accessibility requirement, but not the only one.
Apply these rules to documents that will be rendered as HTML, converted to PDF, or read by
screen readers.

**Heading sequence**: Never skip levels (H1 → H3 without H2 is an error). Automated HTML
converters and screen readers use heading sequence to build document outlines.

**Table accessibility**: Every table used for data (not layout) needs a descriptive caption
or title immediately above it. Screen readers announce the table title before reading cell
content. Column headers must be present; do not use blank header rows.

**Link text**: Links must describe the destination, not the action. "See the filing
requirements" (correct) not "Click here" or "Read more" (incorrect). Screen readers present
all links as a list; non-descriptive link text becomes meaningless out of context.

**Color as information**: Do not use color as the sole way to convey meaning. If a table
row is highlighted to signal a warning, also add a text label ("Warning:" or a symbol).
This applies to charts, diagrams, and status indicators.

**Alt text for images and diagrams**: Every image that conveys information needs alt text.
Decorative images use `alt=""`. For complex diagrams, provide a text equivalent in the
surrounding prose or a linked description.
