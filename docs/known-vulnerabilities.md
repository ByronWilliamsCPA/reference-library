---
schema_type: common
title: "Known Vulnerabilities"
status: published
owner: ByronWilliamsCPA
purpose: "Tracks CVEs that cannot be immediately resolved in project dependencies."
tags:
  - security
  - dependencies
---

> Tracks CVEs and accepted compliance exceptions. Review quarterly.
> No entry may age past 60 days without reassessment; escalate or resolve.
> This mirrors the global standard in `~/.claude/CLAUDE.md` "Unfixed CVEs" section.

## Current Status

This repository is a docs-only reference library. It has no runtime Python package
dependencies beyond a single optional script (`scripts/extract_legal_pdfs.py`) that uses
`pymupdf` as a fallback for PDF extraction. There are no known vulnerabilities at this time.

If a future dependency audit identifies a CVE that cannot be immediately resolved, document
it below using the entry format from the template at
`~/.claude/docs/known-vulnerabilities-template.md`.

---

## Accepted Architectural Exceptions

These entries document accepted Scorecard findings that are not CVEs but require
explicit documentation as accepted exceptions. Each entry follows the same 60-day
reassessment policy; no entry ages past 60 days without a dated review note.

---

### SCORECARD:publish_results -- Scorecard publish disabled (architectural)

| Field | Value |
| --- | --- |
| Finding | OpenSSF Scorecard `publish-results: false` in scorecard.yml |
| Date documented | 2026-05-16 |
| Re-review date | 2026-07-15 |
| Remediation planned | No |

**Reason**: This workflow calls the org-level reusable workflow at
`ByronWilliamsCPA/.github/.github/workflows/python-scorecard.yml`. When a reusable
workflow publishes SARIF results, the OIDC repository claim resolves to the caller org's
`.github` repository, not the calling repository. Setting `publish-results: true` would
misattribute results to `ByronWilliamsCPA/.github` rather than
`ByronWilliamsCPA/reference-library`. SARIF artifacts remain available locally for audit
purposes via the Actions artifact store. No remediation is planned until GitHub resolves
the OIDC claim scoping for reusable workflow callers.

---

### SCORECARD:Fuzzing -- Fuzzing score 0/10 (structural exception)

| Field | Value |
| --- | --- |
| Finding | OpenSSF Scorecard Fuzzing check score 0/10 |
| Date documented | 2026-05-16 |
| Re-review date | 2026-07-15 |
| Remediation planned | No |

**Reason**: This is a docs-only reference library. The only executable code is
`scripts/extract_legal_pdfs.py` (a PDF extraction utility with no untrusted network
input) and sample generator scripts. There is no untrusted input surface that warrants
fuzz testing. Additionally, Scorecard v5.3.0 does not recognize Hypothesis as a Python
fuzzer; its detection covers Go, Haskell, JavaScript/TypeScript, and Erlang only.
ClusterFuzzLite integration would be structurally disproportionate for a docs repository
of this scope. A score of 0 is accepted for this check. If the repository ever gains a
runtime service component or public API surface, this exception must be re-evaluated
before that component reaches production.

<!-- No open CVEs. Add entries here as needed using the template format. -->
