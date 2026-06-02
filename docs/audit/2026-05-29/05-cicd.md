# CI/CD and Tooling Audit: reference-library

Audit date: 2026-05-29 (UTC). HEAD: 60e1cda. Scope: 11 workflows in `.github/workflows/`, static-analysis config consistency, gate enforcement, and committed tooling artifacts. Read-only. actionlint/yamllint not installed; analysis is from file inspection.

## Summary

Actions hygiene is current: no deprecated majors, no `set-output`/`save-state`, every job hardened and SHA-pinned. The problems are scale and visibility. Eleven workflows guard 1434 LOC of Python with zero declared dependencies, and the security scanners overlap heavily while most of their scan types are switched off. The in-repo `ci.yml` "CI Gate" only checks that documentation files exist; the actual test, lint, and coverage enforcement lives in an external reusable workflow, so what blocks a merge is not visible or version-bounded in this repo. Four broken `.qlty` symlinks are committed and leak a local path.

## Findings

### CICD-01: Eleven workflows with heavy scanner overlap, most scan types disabled

- Severity: Medium
- Effort: M (consolidate the security workflows; a few days)
- Affected files: `.github/workflows/{codeql,scorecard,sonarcloud,qlty,sbom,dependency-review,security-analysis}.yml`, `docs/reusable-workflow-jobs.yaml`
- Evidence: Seven of the 11 workflows are security/quality scanners. `docs/reusable-workflow-jobs.yaml` records that the `python-security-analysis` reusable runs with "run-safety, run-codeql, run-dependency-review, run-osv, run-bandit all false" for this docs-only repo, yet the repo also keeps a standalone `codeql.yml` and a standalone `dependency-review.yml`, duplicating scan types the reusable already enumerates (then disables). For a repo with zero declared dependencies, dependency-review and SBOM scan an empty surface (see DEP-03).
- Recommendation: Pick one path per scan type (either the org reusable or the standalone workflow, not both) and drop the scanners that have no target on a zero-dependency docs repo, documenting what remains and why.

### CICD-02: The in-repo CI gate only checks that docs exist; real enforcement is external and unpinned-to-version

- Severity: Medium
- Effort: S
- Affected files: `.github/workflows/ci.yml:36-50`, `.github/workflows/{qlty,security-analysis,scorecard}.yml`
- Evidence: `ci.yml`'s sole job verifies that README/CLAUDE/SECURITY/CONTRIBUTING/CHANGELOG files are present; it does not run pytest, ruff, or mypy (`grep -nE 'pytest|ruff|mypy' ci.yml` returns nothing). Test/coverage/lint enforcement is delegated to `ByronWilliamsCPA/.github/...@74c633a # main`, a reusable workflow in another repo tracking `main` rather than a release tag. A reader of this repo cannot see what actually blocks a merge, and the gate logic can change under a moving `main` without any commit here.
- Recommendation: Either run pytest+ruff+mypy directly in `ci.yml` (the suite is fast: 44 tests in 0.14s) or document in-repo exactly which jobs of the external reusable are merge-blocking and pin the reusable to a release tag (see DEP-03).

### CICD-03: Four committed `.qlty` symlinks are broken and leak a local path; .gitignore patterns miss them

- Severity: Medium
- Effort: S
- Affected files: `.qlty/logs`, `.qlty/out`, `.qlty/results`, `.qlty/plugin_cachedir`, `.gitignore`
- Evidence: `git ls-files .qlty/` lists these four entries as tracked. `file` on each shows a broken symlink to `/home/byron/.qlty/cache/repos/643c141.../...`, a machine-local path that exists on no other clone and exposes a local username. `.gitignore` lists `.qlty/logs/` etc. with trailing slashes, which match directories, not these symlink files, so `git check-ignore` returns nothing for them: the ignore never took effect and the artifacts were committed.
- Recommendation: `git rm --cached` the four symlinks and change the `.gitignore` entries from `.qlty/logs/` to `.qlty/logs` (drop the trailing slash) so the runtime artifacts stop being tracked.

### CICD-04: Pre-commit runs no Python lint, type, or test hook

- Severity: Low
- Effort: S
- Affected files: `.pre-commit-config.yaml`
- Evidence: The hook set is detect-secrets, trufflehog, commitizen, yamllint, markdownlint, renovate-config-validator, and a local no-em-dash check. There is no ruff, mypy/basedpyright, or pytest hook. Combined with CICD-02 (CI also does not run them in-repo), a contributor gets no local or visible-CI signal on Python quality unless the external reusable runs them.
- Recommendation: Add ruff and a fast pytest hook to pre-commit so Python regressions are caught before push, matching the tooling the repo already configures in pyproject.

## Clean areas

- Action versions: all current. `actions/checkout@v6.0.2`, `actions/upload-artifact@v7.0.1`, `actions/setup-python@v6`, `github/codeql-action@v4.36.0`, `actions/dependency-review-action@v5.0.0`. No deprecated majors, no `::set-output::` or `save-state`, no EOL runner pins.
- Hardening and concurrency: every job uses harden-runner with egress control; `ci.yml` sets `concurrency` with cancel-in-progress and a 5-minute timeout.
- Gate posture: no `continue-on-error` or `|| true` soft-fails found in any workflow, so the gates that do run are blocking.
- Custom Renovate manager keeps `docs/reusable-workflow-jobs.yaml` pins in sync with the workflow callers (`renovate.json` custom regex manager), addressing inventory drift.
