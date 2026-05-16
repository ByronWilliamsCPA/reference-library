# Compliance Overrides

Repo-specific overrides for the `repo-compliance` skill. Entries here are skipped
during audit runs without raising FINDING blocks. See
`~/.claude/docs/standards-manifest.yaml` for the canonical check definitions.

| Check ID | Reason | Date added |
| --- | --- | --- |
| TOOL-009 | `basedpyright` is not in qlty's default plugin registry and requires a `pyproject.toml` to function. This is a docs-only repository with no `pyproject.toml`; the two Python scripts in `scripts/` are utility code, not a library. The docs-only type profile already exempts the basedpyright pre-commit hook for the same reason. | 2026-05-14 |
