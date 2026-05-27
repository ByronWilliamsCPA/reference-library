# Punctuation Preferences

> **Purpose**: Catalog of person-configurable punctuation and usage preferences (PCP-style Tier 3 overrides).
> **Authority**: This file describes *possible* preferences and how agents enforce each one. It does NOT declare which preferences are active. Active preferences come from the resolved profile (see `scripts/profile_resolver.py`).
> **Scope**: Person-scoped. Each person's profile may set any subset of these in its `tier_3_overrides` list.

---

## How This Works

Each entry below names a single overridable preference. Agents (drafter, grammar editor, tone rewriter, style editor) read the resolved profile's `tier_3_overrides` list at the start of every invocation. For each override in the list, the agent applies the enforcement described here.

Default profile ships with `tier_3_overrides = ["no-em-dash"]` so today's behavior is preserved when nothing else is configured. Other profiles may omit `no-em-dash` (em-dashes permitted) or add additional overrides.

---

## Catalog

### `no-em-dash`

**What it means**: Em-dashes (`—`) are not used in prose. Substitute commas (for parenthetical asides), colons (for amplification or examples), parentheses (for insertions), or semicolons (for linking related clauses).

**When active**:

- Drafters and rewriters must not introduce em-dashes during generation.
- Stage 1 (grammar editor) flags any em-dash as a mechanical error.
- Stage 3 (style editor) flags em-dashes as voice violations and rewrites with the substitutions above.
- Stage 1 also flags repeated "X, insertion, Y" comma patterns that read as em-dash substitutes when the structure becomes formulaic.

**When inactive**: Em-dashes are governed by CMS §6.85–6.87. They are valid for parenthetical insertion, abrupt shift, amplification, and attribution of block quotation. Agents do not flag them but still discourage stacked uses.

**Source authority**: CMS §6.85–6.87; cross-referenced as divergence #15 and #21 in `grammar-style/cross-reference.md`.

---

### Reserved for future overrides

The catalog is intentionally short. Add new entries here only after the override has been confirmed in a person's profile. Document each addition with:

- The override key (e.g., `no-oxford-comma`, `prefer-spelled-numbers`)
- A one-paragraph "What it means" description
- "When active" enforcement rules for every relevant agent
- "When inactive" fallback authority

Do not introduce overrides that contradict the grammar-style three-tier hierarchy (EoS → CMS → PCP) without updating that hierarchy first.

---

## Style-Driven Punctuation (Not Person Overrides)

Some punctuation rules vary by *style context*, not by person. These are governed by the resolved `style.legal_source` and related fields, not by `tier_3_overrides`. See:

- `legal-style/cross-reference.md`: serial comma, quote punctuation, ellipsis, tense, ORS ranges (LC vs. Appellate)
- `writing-style/grammar-style/cross-reference.md`: EoS/CMS divergences resolved by tier

If a person wants a style-level rule applied universally (e.g., always use the serial comma regardless of legal context), that's a separate concept from a Tier 3 override and should be handled by setting the appropriate style as the default rather than by adding an override here.

---

## Relationship to Other References

- **Profile resolver** (`scripts/profile_resolver.py`): emits the active `tier_3_overrides` list as part of every resolution.
- **Profiles config** (`config/profiles.toml`, gitignored): declares each person's override list.
- **Example config** (`config/profiles.example.toml`): ships with `tier_3_overrides = ["no-em-dash"]` on the default profile.
- **CLAUDE.md**: documents the three-tier hierarchy at a high level; defers to this catalog for the actual override entries.
- **Grammar cross-reference** (`writing-style/grammar-style/cross-reference.md`): the "PCP Override" column references entries in this catalog.
