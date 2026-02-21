# Security Policy

## Reporting a Vulnerability

If you find a security issue (exposed credentials, sensitive data in history, etc.),
**do not open a public issue**. Use GitHub's Security tab:

1. Go to the repository's **Security** tab
2. Click **"Report a vulnerability"**
3. Submit details through the form

All reports are kept confidential.

## Scope

This is a personal reference library containing writing style guides and legal
drafting standards. It holds no credentials, keys, or sensitive personal data.
The primary security concern is accidental credential or PII exposure in commits.

## Security Practices

- **Secrets detection**: Trufflehog scans commits via Qlty (`.qlty/qlty.toml`)
- **Pattern scanning**: Ripgrep flags credential-shaped strings
- **Git-ignored locals**: PDF sources and extracted text are never committed

## Response

Acknowledgment within 5 business days. For this repository, most issues will
resolve quickly since no application code or infrastructure is involved.

*Policy mirrors [ByronWilliamsCPA/.github SECURITY.md](https://github.com/ByronWilliamsCPA/.github/blob/main/SECURITY.md).*
