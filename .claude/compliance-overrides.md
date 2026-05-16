# Compliance Overrides

Repo-specific overrides for the `repo-compliance` skill. Entries here are skipped
during audit runs without raising FINDING blocks. See
`~/.claude/docs/standards-manifest.yaml` for the canonical check definitions.

| Check ID | Reason | Date added |
| --- | --- | --- |
| TOOL-009 | `basedpyright` is not in qlty's default plugin registry and requires a `pyproject.toml` to function. This is a docs-only repository with no `pyproject.toml`; the two Python scripts in `scripts/` are utility code, not a library. The docs-only type profile already exempts the basedpyright pre-commit hook for the same reason. | 2026-05-14 |
| CI-037 | PR title validation is implemented inline in pr-validation.yml using a conventional-commit regex matching the org's commitlint config. This is functionally equivalent to amannn/action-semantic-pull-request and avoids adding a third-party action dependency for a solo-maintainer docs-only repo. | 2026-05-15 |
| OSSF-006 | Silver badge criteria (two-independent-reviewer code review, bus factor >= 2) are structurally infeasible for a solo-maintainer docs-only repo. Recruiting external contributors solely to satisfy a badge criterion is not a reasonable remediation path. The Passing badge is the appropriate and achievable target. | 2026-05-15 |
