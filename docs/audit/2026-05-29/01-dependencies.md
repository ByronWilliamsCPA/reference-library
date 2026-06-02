# Dependencies and Supply Chain Audit: reference-library

Audit date: 2026-05-29 (UTC). HEAD: 60e1cda. Scope: Python dependencies, lockfile
reproducibility, GitHub Actions pinning, Renovate coverage, SBOM coverage, pre-commit hook
pins. Read-only.

## Summary

The Python dependency surface is near zero: `pyproject.toml` declares zero project
dependencies and zero dev/optional groups. The only third-party imports are two lazy,
guarded fallbacks in scripts (`pymupdf` in `extract_legal_pdfs.py`, `tomli` in
`profile_resolver.py`); both are optional and never installed by CI. requires-python is
`>=3.11`; CI runs 3.12; Python 3.11 has security support through 2027-10, so no version
pressure. All 11 distinct GitHub Actions are pinned to full 40-char commit SHAs, and all 6
pre-commit hook repos are SHA-pinned: supply-chain pinning hygiene is strong. The notable
gaps are: (1) no `uv.lock` exists anywhere in the repo despite CLAUDE.md referencing a
"CI-024 freshness check" for uv, leaving the uv toolchain claim unbacked; (2) three org
reusable workflows are SHA-pinned but track a floating `main` branch rather than a release
tag; (3) Renovate does not enable the `pre-commit` manager, so the 6 SHA-pinned hook repos
are not auto-updated; (4) the SBOM generator runs against a near-empty dependency surface.

## Findings

### DEP-01: No uv.lock exists; CLAUDE.md "CI-024 / uv" reference is unbacked

- Severity: Medium
- Effort: S (decide and either add uv adoption or strike the stale reference; under a day)
- Affected files: `CLAUDE.md:56`, `docs/reusable-workflow-jobs.yaml`, repo root
- Evidence:
  - `ls uv.lock` and `git ls-files | grep -iE "uv.lock|requirements|setup.py|poetry.lock|Pipfile"` both return nothing. No lockfile of any kind is tracked.
  - `git grep -iE "uv.lock|uv sync|uv pip|uv run|astral-sh/setup-uv"` returns a single hit: `CLAUDE.md:56` ("reusable-workflow-jobs.yaml # Workflow inventory for CI-024 freshness check"). No workflow runs `uv` and `docs/reusable-workflow-jobs.yaml` does not mention uv or uv.lock anywhere.
  - The audit brief states CLAUDE.md and docs/reusable-workflow-jobs.yaml reference uv and a uv.lock; verified: only the indirect CLAUDE.md line 56 alludes to a "CI-024 freshness check," and there is no uv.lock for it to check. The CI-024 check has no target.
- Reproducibility impact: low in practice (zero declared deps means there is nothing to lock), but the documentation asserts a uv-based freshness gate that does not exist, which is a correctness/traceability defect. If uv adoption is intended, the lock is missing; if not, the CLAUDE.md reference is stale residue.
- Recommendation: Either adopt uv and commit `uv.lock` (only worthwhile if real deps get declared) or remove the CI-024/uv freshness language from CLAUDE.md and confirm `docs/reusable-workflow-jobs.yaml` never claimed uv. This is the real migration residue, not legacy package files.
- CVE: none

### DEP-02: pyproject.toml declares zero dependencies; SonarCloud installs unpinned test tools at runtime

- Severity: Low
- Effort: S (add a pinned dev group or a constraints file; under a day)
- Affected files: `pyproject.toml:6-11`, `.github/workflows/sonarcloud.yml:46-51`
- Evidence:
  - `pyproject.toml` has no `[project.dependencies]`, no `[project.optional-dependencies]`, no `[dependency-groups]` (`grep -niE "dependencies|optional-dependencies|dependency-groups" pyproject.toml` -> NONE).
  - `sonarcloud.yml:51`: `python -m pip install 'pytest>=7.0,<9' 'pytest-cov>=4.0,<7'`. Tools are floor-and-ceiling ranged, not hash-pinned, and resolved fresh on a runner that holds `SONAR_TOKEN` (env at `sonarcloud.yml:61`). The workflow comment acknowledges this is a deliberate floor to "reduce supply-chain risk," but a range still resolves to a mutable latest-in-range build each run.
  - The two third-party imports (`pymupdf`, `tomli`) are lazy and guarded (`extract_legal_pdfs.py:64` behind a try/except; `profile_resolver.py:53` tomli fallback only for <3.11), never declared as deps and never installed in CI.
- Recommendation: Declare pytest and pytest-cov in a `[dependency-groups]` test group in pyproject.toml so the test toolchain is versioned in one place, and consider a hash-pinned constraints file for the token-bearing SonarCloud job. Low priority given the tiny surface.
- CVE: none

### DEP-03: Three org reusable workflows track floating `main`, not a release tag

- Severity: Medium
- Effort: S (repoint to a tagged release once the org repo cuts one; under a day, blocked on org tagging)
- Affected files: `.github/workflows/qlty.yml:17`, `.github/workflows/security-analysis.yml:29`, `.github/workflows/scorecard.yml:29`, `docs/reusable-workflow-jobs.yaml:11-12,28-29,40-41`
- Evidence:
  - All three callers pin `ByronWilliamsCPA/.github/.github/workflows/*.yml@74c633acfdd5f707ab154fd59bd212c6df663dd6  # main`. The SHA is fixed (good), but the trailing `# main` and the Renovate datasource (`currentValue=main`, `docs/reusable-workflow-jobs.yaml:11`) confirm the pin tracks the branch head, not a semver tag.
  - `renovate.json:66-77` has a rule to follow tag `v1` for `ByronWilliamsCPA/.github` and `williaby/.github`, but the actual pins reference `main`, so Renovate's `followTag: v1` rule will not match the `currentValue=main` git-refs datasource. The intended v1 tracking and the actual main tracking are inconsistent.
- Supply-chain angle: a SHA pin on a `main` head means each Renovate digest bump advances to whatever `main` last committed, with no release gate or changelog boundary. Versioned tags give a review/rollback boundary. (Workflow correctness and deprecation of these reusables is the CICD subagent's scope; this finding covers only the pinning model.)
- Recommendation: Have the org `.github` repo publish a `v1` (or dated) release tag and repoint these three callers to the tag's SHA, aligning with the existing `followTag: v1` Renovate rule so updates land on releases rather than branch heads.
- CVE: none

### DEP-04: Renovate does not manage pre-commit hooks

- Severity: Medium
- Effort: S (add `pre-commit` to enabledManagers; under a day)
- Affected files: `renovate.json:79-84`, `.pre-commit-config.yaml`
- Evidence:
  - `renovate.json:79-84` enabledManagers = `pep621`, `pip_requirements`, `github-actions`, `custom.regex`. The `pre-commit` manager is absent.
  - `.pre-commit-config.yaml` pins 6 hook repos by SHA: detect-secrets (`01886c8...` v1.5.0, line 18), trufflehog (`37b7700...` v3.95.3, line 36), commitizen (`cc981fc...` v4.9.1, line 51), yamllint (`cba56bc...` v1.38.0, line 60), markdownlint-cli (`e72a3ca...` v0.48.0, line 69), renovatebot/pre-commit-hooks (`2a27c9f...` v43.150.0, line 134, with `additional_dependencies: renovate@42.92.14`).
  - Because the pre-commit manager is off, none of these SHAs are auto-updated by Renovate. They drift manually. Note the renovatebot hook also carries a pinned `renovate@42.92.14` in additional_dependencies that no manager tracks.
- Recommendation: Add `"pre-commit"` to `enabledManagers` in renovate.json so the 6 SHA-pinned hooks and the embedded `renovate@42.92.14` get update PRs on the same cadence as Actions. Without it, security-relevant scanners (detect-secrets, trufflehog) age silently.
- CVE: none

### DEP-05: SBOM coverage is thin relative to the actual dependency surface

- Severity: Low
- Effort: S (accept as-is or document scope; under a day)
- Affected files: `.github/workflows/sbom.yml:43-51`
- Evidence:
  - `sbom.yml` runs `anchore/sbom-action@e22c389...` v0.24.0 with `path: .`, cyclonedx-json, on push-to-main and weekly (`cron '17 6 * * 1'`). The header comment claims it "captures the GitHub Actions and pre-commit hook dependency surface."
  - syft (anchore's engine) catalogs package manifests it recognizes; with zero declared Python deps (DEP-02) and no lockfile (DEP-01), the Python component list will be near-empty. syft does not natively enumerate `.github/workflows` action SHAs or `.pre-commit-config.yaml` hook repos as SBOM components, so the comment overstates coverage. The most security-relevant supply-chain inputs here (Actions, hooks) are likely not in the generated SBOM.
  - retention 90 days, artifact only (`upload-release-assets: false`, `sbom.yml:49`).
- Recommendation: Either accept the SBOM as a low-value formality for this docs-first repo and correct the header comment, or add explicit cataloging of Actions and pre-commit pins (for example a separate generator) if a true supply-chain SBOM is the goal.
- CVE: none

## Clean areas

- GitHub Actions pinning: all 11 distinct actions (step-security/harden-runner v2.19.4, actions/checkout v6.0.2, actions/upload-artifact v7.0.1, actions/setup-python v6, actions/dependency-review-action v5.0.0, github/codeql-action init+analyze v4.36.0, anchore/sbom-action v0.24.0, fsfe/reuse-action v6.0.0, SonarSource/sonarcloud-github-action v5.0.0, and the 3 org reusables) are pinned to full 40-char commit SHAs with version comments. No floating tags or major-version refs. Renovate `pinDigests: true` enforces this for new actions (renovate.json:48-53). Clean.
- Migration residue from prior package managers: none tracked. No requirements*.txt, setup.py, setup.cfg, poetry.lock, or Pipfile (`git ls-files` grep returned nothing). The only residue is the missing uv.lock referenced by docs (see DEP-01).
- Python version window: requires-python `>=3.11` (pyproject.toml:11), CI on 3.12. Python 3.11 has security support through approximately 2027-10 and 3.12 through approximately 2028-10. No EOL pressure; no action needed.
- Stale-dependency check (no upstream release in 18+ months): not applicable to declared deps (there are none). For Actions and hook pins, exact upstream release dates require network/registry queries that were not run in this read-only pass; data unavailable. The version tags present (for example trufflehog v3.95.3, markdownlint-cli v0.48.0) are recent-series and show no obvious abandonment.
- Renovate manager coverage for declared package types: pep621 + pip_requirements + github-actions + custom.regex are enabled, plus a vulnerabilityAlerts block, osvVulnerabilityAlerts, and transitiveRemediation (renovate.json:104-117). Coverage for Python and Actions is adequate; the only gap is pre-commit (DEP-04).
