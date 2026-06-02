# Holistic Legacy and Architecture Audit: reference-library

Audit date: 2026-05-29 (UTC). HEAD: 60e1cda. Orchestrated review across six domains: dependencies, code quality, architecture, security, CI/CD, and documentation. Per-domain detail is in `01` through `06`; this report synthesizes and resolves overlaps.

## 1. Repo map

- Purpose: a docs-first reference library of writing and Oregon-legal style standards. Not an application.
- Size: 124 tracked files. ~23,000 lines of markdown across 86 files. Python surface is 4 files / 1434 LOC: `scripts/profile_resolver.py` (471), `scripts/generate_before_samples.py` (319), `scripts/extract_legal_pdfs.py` (198), `tests/test_profile_resolver.py` (446). One shell script (`setup.sh`).
- Language and runtime: Python, `requires-python >=3.11`, CI on 3.12. 3.11 has upstream security support to roughly 2027-10, so no version pressure.
- Build/package: `pyproject.toml` only. Zero declared dependencies, no dependency groups, no lockfile of any kind (no `uv.lock`, no `requirements*.txt`). No migration residue from a prior package manager; the only residue is the missing `uv.lock` that docs imply should exist.
- Tests/tooling: pytest (44 tests, 77 asserts, pass in 0.14s), ruff (passes in-scope), basedpyright (configured `standard`, not installed here), mypy (one import-not-found). Coverage scoped to one of three scripts.
- CI: GitHub Actions, 11 workflows (7 of them security/quality scanners), plus pre-commit (detect-secrets, trufflehog, commitizen, yamllint, markdownlint, renovate-validator, local no-em-dash), Renovate, SonarCloud, Qlty, OpenSSF Scorecard, REUSE.
- Churn: most-edited files are workflows (`scorecard.yml` 11, `security-analysis.yml` 10) and top docs (`README.md` 9, `CLAUDE.md` 9). 53 commits since 2026-02-20. The churn is concentrated in CI config and governance docs, not in the Python.
- Incomplete migration signals: none of the classic ones. The notable mismatch is documentation referencing a uv-based freshness check with no `uv.lock` behind it.

## 2. Code quality (critical view)

The in-scope Python is genuinely clean and small: zero ruff findings, zero debt markers, modern idioms throughout, a fast and assertion-dense test suite. The weakness is that the quality signals are scoped narrowly enough to flatter the code. Two of the three scripts are excluded from both ruff and coverage, and running ruff on them directly surfaces 22 errors (CQ-01). The "strict" type-checking story is weaker than it reads: basedpyright is set to `standard` not `strict`, and the resolver routes every profile field through `dict[str, Any]` (CQ-02), so the one file under the type gate is barely constrained by it. Coverage describes a single script and omits the other two by configuration (CQ-03). None of this is dangerous on 1434 LOC, but the pattern is consistent: the config draws the measurement boundary around the clean code and excludes the rest. That is a maintainability tax that grows if the scripts grow.

## 3. Architecture (critical view)

The runtime architecture is sound and matches its documentation: the V2 person x style resolver implements the documented merge order, list semantics, and domain gating, and the seven agents reference profile fields consistently without hardcoding Tier-3 rules into agent bodies. Where the structure works against maintainers is governance, not code. Four assistant-instruction files (CLAUDE.md, AGENTS.md, GEMINI.md, copilot-instructions.md) restate the same architecture, so every change must be propagated up to four times with no single source of truth (ARCH-01). And the repo contradicts its own stated principle: it documents `no-em-dash` as a configurable per-profile Tier-3 override that "other profiles may omit," then hardcodes that exact rule into a pre-commit gate and three instruction files (ARCH-02). The design says configurable; the infrastructure says mandatory. A maintainer who trusts the documented flexibility will hit a CI wall.

## 4. Cross-cutting themes

- Configuration over substance. The dominant root cause across domains is that tooling is configured at a scale and ambition the codebase does not match: 11 workflows and 7 scanners for 1434 LOC with zero dependencies (CICD-01), an SBOM over an empty surface (DEP-05), dependency-review with nothing to review, and a "strict" type entry point that is not strict (CQ-02). Several scanners run with their scan types disabled. The effort spent maintaining this CI surface exceeds its value for a docs repo.
- Enforcement is real but invisible. The in-repo `ci.yml` gate only checks that doc files exist (CICD-02); the actual test/lint/coverage enforcement lives in an external reusable workflow tracking a moving `main` (DEP-03), and pre-commit runs no Python lint or test hook (CICD-04). What blocks a merge is neither visible in this repo nor pinned to a release.
- Documentation drift against a documented anti-drift culture. The repo invests heavily in writing standards yet carries a stale model table (ARCH-03), an empty CHANGELOG `[Unreleased]` (DOC-02), a uv reference with no lockfile (DEP-01), and one ADR for several decisions (DOC-01). The governance ambition is high; the upkeep lags it.
- Age stratification. The two pre-V2 operational scripts (`extract_legal_pdfs.py`, `generate_before_samples.py`) are walled off from the lint/coverage/type config that governs the newer `profile_resolver.py`. The repo has an older tier and a newer tier, and the boundary is drawn with exclusions rather than cleanup (CQ-01, CQ-03).

Where subagents overlapped: the four-instruction-file problem surfaced in both architecture and docs; I assign it to architecture (ARCH-01) as the structural owner and treat the docs angle as onboarding cost. The committed `.qlty` symlinks surfaced as both a path leak and a tracked-artifact bug; the better-supported framing is the CI/tooling one (CICD-03), since the root cause is an ineffective `.gitignore` pattern, not an intent to expose a secret. The reusable-workflow `main`-tracking issue is owned by dependencies (DEP-03, supply-chain pinning model) with CI/CD referencing it for the enforcement-visibility angle (CICD-02).

## 5. Prioritized remediation backlog

Sorted by severity, then effort.

| ID | Finding | Domain | Severity | Effort | Files |
| --- | --- | --- | --- | --- | --- |
| ARCH-01 | Four overlapping assistant-instruction files duplicate the architecture | architecture | High | M | CLAUDE.md; AGENTS.md; GEMINI.md; .github/copilot-instructions.md |
| DEP-01 | No uv.lock; CLAUDE.md CI-024/uv reference is unbacked | dependencies | Medium | S | CLAUDE.md; docs/reusable-workflow-jobs.yaml |
| DEP-03 | Reusable workflows track floating main, not a release tag | dependencies | Medium | S | .github/workflows/qlty.yml; security-analysis.yml; scorecard.yml; docs/reusable-workflow-jobs.yaml |
| DEP-04 | Renovate does not manage pre-commit hooks | dependencies | Medium | S | renovate.json; .pre-commit-config.yaml |
| CQ-01 | 22 lint errors hidden in ruff/coverage-excluded scripts | code-quality | Medium | S | scripts/extract_legal_pdfs.py; scripts/generate_before_samples.py; pyproject.toml |
| SEC-01 | Source PDF downloads have no integrity verification | security | Medium | S | scripts/extract_legal_pdfs.py; CLAUDE.md |
| CICD-02 | In-repo CI gate only checks docs exist; real gate is external | cicd | Medium | S | .github/workflows/ci.yml; qlty.yml; security-analysis.yml |
| CICD-03 | Committed broken .qlty symlinks leak a local path; gitignore misses them | cicd | Medium | S | .qlty/logs; .qlty/out; .qlty/results; .qlty/plugin_cachedir; .gitignore |
| CQ-02 | dict[str, Any] pervades the resolver; the type gate proves little | code-quality | Medium | M | scripts/profile_resolver.py |
| CQ-03 | Coverage measures one of three runtime scripts | code-quality | Medium | M | scripts/extract_legal_pdfs.py; scripts/generate_before_samples.py; tests/ |
| CICD-01 | Eleven workflows with heavy scanner overlap, most scans disabled | cicd | Medium | M | .github/workflows/codeql.yml; scorecard.yml; sonarcloud.yml; qlty.yml; sbom.yml; dependency-review.yml; security-analysis.yml |
| DEP-02 | pyproject declares zero deps; SonarCloud installs unpinned test tools | dependencies | Low | S | pyproject.toml; .github/workflows/sonarcloud.yml |
| DEP-05 | SBOM coverage is thin relative to the dependency surface | dependencies | Low | S | .github/workflows/sbom.yml |
| CQ-04 | tomli fallback import is untyped and unreachable on supported runtimes | code-quality | Low | S | scripts/profile_resolver.py |
| ARCH-02 | no-em-dash documented as a per-profile override but hardcoded repo-wide | architecture | Low | S | CLAUDE.md; .pre-commit-config.yaml; .github/copilot-instructions.md; AGENTS.md; GEMINI.md |
| ARCH-03 | Model Selection table references a superseded model generation | architecture | Low | S | CLAUDE.md |
| SEC-02 | detect-secrets baseline could not be re-verified locally | security | Low | S | .secrets.baseline |
| CICD-04 | Pre-commit runs no Python lint, type, or test hook | cicd | Low | S | .pre-commit-config.yaml |
| DOC-02 | CHANGELOG [Unreleased] is empty despite post-1.1.0 changes | docs | Low | S | CHANGELOG.md |
| DOC-01 | Only one ADR exists; major decisions are undocumented | docs | Low | M | docs/architecture/ |

## 6. Verdict

Healthy, with governance drift. There is no Critical finding, no live security exposure, no EOL pressure, and the code that ships is clean and tested. The repo is not at risk; it is over-engineered at the edges and under-maintained at the documentation core. The three changes that would move it most:

1. Collapse the four assistant-instruction files to one canonical source with thin pointers (ARCH-01), removing the largest recurring maintenance tax.
2. Right-size CI: drop or consolidate the scanners that have no target on a zero-dependency docs repo, and make the merge-blocking gate visible in-repo (CICD-01, CICD-02).
3. Stop drawing quality boundaries with exclusions: lint and cover all of `scripts/`, and either commit a lockfile or remove the uv claim (CQ-01, CQ-03, DEP-01).
