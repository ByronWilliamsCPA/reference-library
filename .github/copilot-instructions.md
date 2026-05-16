# GitHub Copilot Code Review Instructions

Focus on: business logic correctness, error handling completeness, edge cases,
concurrency issues, and security logic flaws.

Exclude from review: code style, formatting, and whitespace. These are enforced
by pre-commit hooks and ruff -- do not flag them.

## Project context

This is a docs-only reference library for writing standards: Oregon legal style,
writing quality guidelines, and grammar references. No Python production code
exists; only utility scripts live in scripts/.

## Key conventions

- No em-dashes in any output. Use commas, colons, or semicolons instead.
- Seven agents in agents/ implement the writing quality pipeline (pre-pipeline
  generators, three-stage editing pipeline, post-pipeline analyzer).
- All workflow action references must be SHA-pinned (no tag-only refs like @v4).
- Legal style content is governed by three sources with different authority per
  document type. See legal-style/cross-reference.md before flagging divergences.
