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

> Tracks CVEs that cannot be immediately resolved. Review quarterly.
> No entry may age past 60 days without reassessment; escalate or resolve.

## Current Status

This repository is a docs-only reference library. It has no runtime Python package
dependencies beyond a single optional script (`scripts/extract_legal_pdfs.py`) that uses
`pymupdf` as a fallback for PDF extraction. There are no known vulnerabilities at this time.

If a future dependency audit identifies a CVE that cannot be immediately resolved, document
it below using the entry format from the template at
`~/.claude/docs/known-vulnerabilities-template.md`.

---

<!-- No open CVEs. Add entries here as needed using the template format. -->
