# Security and Secrets Audit: reference-library

Audit date: 2026-05-29 (UTC). HEAD: 60e1cda. Scope: hardcoded secrets, insecure code patterns in `scripts/`, external-resource integrity, GitHub Actions security posture, the detect-secrets baseline, and the CVE log. Read-only. Scanners bandit/detect-secrets/pip-audit/semgrep/trivy are not installed; findings below come from manual inspection and grep.

## Summary

No live secrets, no exploitable injection, and a strong Actions posture (SHA-pinned actions, harden-runner egress blocking on every job, least-privilege permissions, untrusted PR input handled through env-var indirection). The one substantive gap is that the source PDFs are downloaded over HTTPS with no checksum verification, so a changed or tampered upstream file would be ingested silently. The committed broken `.qlty` symlinks also leak a local path; that is tracked as a CI/CD finding (CICD-03) and noted here only for cross-reference.

## Findings

### SEC-01: Source PDF downloads have no integrity verification

- Severity: Medium
- Effort: S (publish and check SHA-256 sums; under a day)
- Affected files: `scripts/extract_legal_pdfs.py`, `CLAUDE.md` (Re-Extracting PDF Source Material section)
- Evidence: CLAUDE.md instructs `curl -O` of three PDFs from `courts.oregon.gov` and `oregonlegislature.gov`, and `extract_legal_pdfs.py` consumes them, with no checksum or signature check at any step. The extracted text becomes the authoritative legal-style reference content for the whole library, so a silently changed upstream PDF (or a man-in-the-middle on a redirect) would propagate into drafting guidance undetected. The CLAUDE.md RAD section says irreplaceable external fetches should be `#CRITICAL`-tagged with a `#VERIFY` instruction; the curl block carries no such tag.
- Recommendation: Record expected SHA-256 sums for the three PDFs and verify after download (and add the `#CRITICAL`/`#VERIFY` RAD tags the repo's own convention requires).

### SEC-02: detect-secrets baseline cannot be re-verified in this environment

- Severity: Low
- Effort: S
- Affected files: `.secrets.baseline`
- Evidence: `.secrets.baseline` exists and the detect-secrets pre-commit hook is SHA-pinned (`.pre-commit-config.yaml:17-20`). The `detect-secrets` CLI is not installed here, so baseline-vs-tree drift (stale entries, or live secrets not baselined) could not be recomputed. A manual grep for `api_key`/`secret`/`token`/`password`/`BEGIN PRIVATE KEY`/`sk-` across `scripts/` and `config/` surfaced only the OpenRouter key-loading code (see clean areas), no literal secret values.
- Recommendation: Confirm in CI (where detect-secrets runs) that `detect-secrets scan --baseline .secrets.baseline` reports no new findings and no orphaned baseline entries; this audit could not run that check locally.

## Clean areas

- API key handling: `generate_before_samples.py` reads `OPENROUTER_API_KEY` from a gitignored `.env` (`load_api_key`, lines 128-148), passes it only as an `Authorization: Bearer` header (line 181), and never prints it. No key is hardcoded.
- Insecure patterns: no `shell=True`, no `os.system`, no `eval`/`exec`, no `pickle`/`yaml.load` unsafe deserialization. `subprocess.run` in `extract_legal_pdfs.py` calls a fixed binary (`pdftotext`) with no user-controlled arguments and is annotated for the scanners. No bare or broad `except` that swallows errors.
- GitHub Actions posture: all third-party actions are SHA-pinned (no tag-only refs); every job runs `step-security/harden-runner` with `egress-policy: block`; the default `permissions` is `contents: read` and jobs add only the scopes they need (17 `permissions:` blocks across 11 workflows); untrusted PR input is passed through env vars (`PR_TITLE`, `PR_BODY` in `pr-validation.yml:31,59`) rather than interpolated into `run:` scripts, closing the script-injection vector. No `pull_request_target` with PR-head checkout.
- CVE log: `docs/known-vulnerabilities.md` shows zero open CVEs, two accepted Scorecard exceptions documented 2026-05-16 with a 2026-07-15 re-review date, inside the stated 60-day cycle as of 2026-05-29.
- SECURITY.md: present with a disclosure process.
