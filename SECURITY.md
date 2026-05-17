# Security Policy

## Reporting a Vulnerability

To report a security vulnerability privately, use GitHub's Private Vulnerability Reporting
feature. Submit your report through the [Security Advisories page](https://github.com/ByronWilliamsCPA/reference-library/security/advisories/new).
All reports are kept confidential and are not publicly visible until a fix is released.

**Do not open a public issue for security vulnerabilities.**

If you find a security issue (exposed credentials, sensitive data in history, etc.):

1. Go to the repository's **Security** tab
2. Click **"Report a vulnerability"**
3. Submit details through the private form

## Response Timeline

We commit to acknowledging all vulnerability reports within 14 days of submission
(typically within 5 business days). For this repository, most issues will resolve
quickly since no application code or infrastructure is involved.

## Scope

This is a personal reference library containing writing style guides and legal
drafting standards. It holds no credentials, keys, or sensitive personal data.
The primary security concern is accidental credential or PII exposure in commits.

## Security Practices

- **Secrets detection**: Trufflehog scans commits via Qlty (`.qlty/qlty.toml`)
- **Pattern scanning**: Ripgrep flags credential-shaped strings
- **Git-ignored locals**: PDF sources and extracted text are never committed

## Secret Rotation Policy

This repository uses two GitHub Actions secrets: `SONAR_TOKEN` (SonarCloud analysis) <!-- pragma: allowlist secret -->
and `QLTY_COVERAGE_TOKEN` (Qlty coverage reporting). Both tokens are fine-grained <!-- pragma: allowlist secret -->
service-issued credentials scoped to the minimum permissions required by each service
(SonarCloud project-scoped tokens and Qlty repo-scoped tokens). Classic GitHub PATs
are not used as repository or organization secrets. Both tokens are rotated annually
or immediately upon any indicator of compromise (unexpected API activity, token exposure
in logs, or repository access anomaly). To rotate, generate a new token from the
respective service dashboard and update it at **Settings > Secrets and variables >
Actions** in the GitHub repository settings.

*Policy mirrors [ByronWilliamsCPA/.github SECURITY.md](https://github.com/ByronWilliamsCPA/.github/blob/main/SECURITY.md).*
