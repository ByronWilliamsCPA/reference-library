# ADR-001: Writing Authority Hierarchy

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-03-15 |
| **Deciders** | Byron Williams |
| **Tags** | writing-standards, legal-style, grammar |

## Context

This repository centralizes writing style and legal drafting standards across personal,
CPA, and investment projects. Two distinct authority hierarchies govern content in this
library: one for grammar and general writing decisions, and one for Oregon legal documents.
Both hierarchies have multiple authoritative sources that sometimes conflict. A clear rule
for resolving conflicts is necessary so that every contributor and every AI agent produces
consistent output.

## Decision 1: Grammar-Style Three-Tier Authority System

The `writing-style/grammar-style/` content adopts a three-tier authority hierarchy. The
governing tier depends on the operation being performed, not the document being read.

| Operation | Governing Authority | Tier |
| --- | --- | --- |
| Drafting (writing first draft) | Elements of Style (EoS) | 1 (baseline) |
| Editing (reviewing any draft) | Chicago Manual of Style, 17th ed. (CMS) | 2 (overrides EoS) |
| User-confirmed preference deviations | PromptCraft Pro defaults | 3 (overrides CMS) |

**Why this order**: EoS provides the most concise and memorable rules for a writer
starting from a blank page. CMS is more comprehensive and authoritative for editing
decisions where precision matters more than speed. Tier 3 captures deliberate user
preferences that deviate from both sources.

**Confirmed Tier 3 overrides**:

- No em-dashes. CMS sections 6.85 through 6.87 permit em-dashes; this library bans them.
  Replace with commas, colons, semicolons, or restructured sentences. This override is
  documented in `writing-style/grammar-style/cross-reference.md` item 21.

**Conflict resolution**: When EoS and CMS conflict on a point not covered by a Tier 3
override, CMS governs (Tier 2 overrides Tier 1). The full list of 21 documented conflicts
and their resolutions is in `writing-style/grammar-style/cross-reference.md`.

**Agent file-loading strategy**: Load `writing-style/grammar-style/QUICK-START.md` first.
For conflicts, load `cross-reference.md`. For deeper rules, load only the specific source
file. Never load all grammar-style files at once; the full set exceeds 12,000 tokens.

## Decision 2: Three-Source Oregon Legal Authority System

The `legal-style/` content comes from three distinct Oregon sources that sometimes conflict.
The governing source depends on what document is being written, not what is being read.

| Document Type | Governing Source |
| --- | --- |
| Court opinions, briefs, and filings | Oregon Appellate Courts Style Manual (2002) |
| Bills and session law | Oregon LC Form and Style Manual |
| Statutory language interpretation and construction | Oregon LC Drafting Manual |

**Why source governs by document type**: The three sources were written for different
audiences with different conventions. Applying the Appellate Style Manual to a bill draft,
or the LC Drafting Manual to a brief, would introduce style errors that would stand out
to the intended audience.

**Critical divergences between sources**:

| Rule | LC (bills/statutory) | Appellate (briefs/opinions) |
| --- | --- | --- |
| Serial comma | Omit: `A, B and C` | Include: `A, B, and C` |
| Quotation mark punctuation | Punctuation outside quotes | Punctuation inside quotes |
| ORS ranges | Always use "to" | Use hyphen with spaces: ` - ` |
| Ellipsis format | `...` | `* * *` |
| Verb tense | Present throughout | Past for facts, present for legal rules |

The full list of divergences and their resolution guidance is in
`legal-style/cross-reference.md`. Read that file before drafting any legal document.

## Alternatives Considered

**Single unified authority**: Using only CMS for all writing decisions would simplify
the rules but would conflict with Oregon legal practice, which has document-type-specific
conventions enforced by courts and the legislature. A single authority cannot satisfy both.

**Alphabetical or topic-based conflict resolution**: Resolving conflicts by topic
(punctuation, citations, etc.) rather than by operation type would require contributors
to look up each individual rule. Operation-based tiers (draft vs. edit vs. override) are
easier to remember and apply consistently.

**No Tier 3**: Omitting the user-override tier would force non-standard preferences into
informal practice. Documenting confirmed overrides explicitly makes them reproducible and
auditable.

## Consequences

- All contributors and agents must check the governing authority before drafting or editing.
- The `writing-style/grammar-style/QUICK-START.md` file covers approximately 80% of
  daily grammar decisions without requiring deep source lookups.
- The `legal-style/QUICK-START.md` file covers approximately 80% of daily legal style
  decisions without requiring source lookups.
- Any new confirmed Tier 3 override must be documented in `cross-reference.md` and
  in this ADR before it takes effect.
- New source additions (a fourth legal authority, a Tier 4 override category) require
  a new ADR rather than silent modification of existing rules.

## Security Considerations

This is a documentation-only architectural decision with no runtime code and no
credentials, secrets, or user data involved. There are no network calls, no
authentication surfaces, and no data persistence beyond static files in version
control.

One supply-chain analogue risk is worth noting: the agent files installed by
`scripts/setup.sh` become executable context loaded into every Claude Code session
across all projects that run the installer. If the authority hierarchy in those files
were changed silently (for example, by substituting a different grammar authority or
redirecting users to an outdated or incorrect source), every downstream AI-assisted
writing session would receive the corrupted guidance without any visible error. This
mirrors the trust-chain concern in software supply chains where a compromised shared
dependency propagates silently. Mitigation: all changes to the hierarchy must go
through a new or amended ADR, and the `setup.sh` installer is version-controlled
alongside the agent files it deploys.
