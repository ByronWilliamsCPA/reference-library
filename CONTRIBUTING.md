# Contributing to Reference Library

Thank you for your interest in contributing. This repository is a docs-only reference
library containing writing style standards, Oregon legal drafting references, and Claude
agent definitions. There is no application code to build or test.

## What This Repo Contains

- Oregon legal style and drafting reference files (`legal-style/`)
- Writing style standards and AI pattern detection (`writing-style/`)
- Claude agent definitions installed globally via `scripts/setup.sh` (`agents/`)
- A PDF extraction utility script (`scripts/`)

## How to Contribute

1. **Find or File an Issue**
   - Search existing issues to avoid duplication.
   - To report an error in a reference file, open an issue describing the incorrect
     content, the source authority that contradicts it, and the correct text.
   - To propose a new reference file or agent, open an issue describing the scope
     and authority source before drafting content.

2. **Fork and Clone**

   ```bash
   git clone https://github.com/ByronWilliamsCPA/reference-library.git
   cd reference-library
   git remote add upstream https://github.com/ByronWilliamsCPA/reference-library.git
   ```

## Pull Request Guidelines

- **Branch from main**

  ```bash
  git checkout -b docs/<short-description>
  ```

- **Link your issue**
  Include "Closes #ISSUE-NUMBER" in your PR description to auto-close the issue.

- **Commit messages**
  Use the format:

  ```text
  <type>(<scope>): <subject>
  ```

  where `<type>` is one of `docs`, `fix`, `feat`, `refactor`, or `chore`.
  Example: `docs(legal-style): correct serial comma rule for LC source`

- **DCO Sign-off Required**
  Every commit must include:

  ```text
  Signed-off-by: Your Name <you@example.com>
  ```

  Add with:

  ```bash
  git commit --signoff
  ```

## Content Standards

Because this is a reference library, accuracy and source attribution matter more than
any other quality criterion.

- **Attribute every claim** to a specific source (a section of the Appellate Style Manual,
  a CMS paragraph number, a specific EoS rule).
- **No em-dashes** anywhere in contributed content. Use commas, semicolons, colons, or
  restructured sentences instead.
- **Plain language**: keep reference text concise and scannable. Use tables where a
  comparison would otherwise require a paragraph.
- **Markdown formatting**: follow the rules in
  `writing-style/structural-formatting.md`.

## Agent Contributions

Agent files in `agents/` are installed globally by `scripts/setup.sh`. When modifying
an agent:

- Test it by running `bash scripts/setup.sh` and exercising the agent in a Claude Code
  session before submitting a PR.
- Keep agents free of project-specific content. Project-specific extensions belong in
  the consuming project's `.claude/agents/` directory.

## Editor and Tooling Configuration

The repository commits a small set of shared tooling configs so behavior is
consistent across contributors:

- **`.vscode/settings.json`** binds SonarLint to the SonarCloud project in
  connected mode. The `connectionId` field (`byronwilliamscpa`) is a local
  identifier that must match a connection you define in your own SonarLint
  global settings (Command Palette: "SonarLint: Add SonarCloud Connection").
  If your local connection uses a different ID, update it there or connected
  mode will silently fail to bind; the committed value is not changed per
  contributor.
- **`.markdownlint.yaml`** (repo root) configures the VS Code markdownlint
  extension and manual `markdownlint-cli` runs. It inherits
  `.qlty/configs/.markdownlint.yaml` and disables MD013 (line length). The
  pre-commit markdownlint hook is pinned to the qlty config directly, so it
  still enforces a 120-character limit; this divergence is intentional.
- **Bandit** is configured under `[tool.bandit]` in `pyproject.toml` but is
  not run in CI or pre-commit (this is a docs-first repo). Run it on demand
  with `uv tool run --from bandit bandit -c pyproject.toml -r scripts tests`.

## Local Setup

No build step is required. To install the agents locally for testing:

```bash
bash scripts/setup.sh
```

To re-extract text from the Oregon legal PDFs (requires local copies in
`legal-style/source-pdfs/`):

```bash
python scripts/extract_legal_pdfs.py
```

## Last Updated: 2026-05-13
