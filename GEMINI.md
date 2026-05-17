# Gemini CLI Support

This repository supports Gemini CLI in addition to Claude Code.

## Project Context

For full project context, architecture decisions, and content standards, read `CLAUDE.md`
at the repository root. That file is the authoritative source of truth for this repository
regardless of which AI assistant you are using.

Key sections in CLAUDE.md:

- **Purpose**: what this library contains and what it does not contain
- **Repository Structure**: directory layout and file purposes
- **Architecture: Grammar-Style Three-Tier System**: the three-tier authority hierarchy
  for grammar and writing decisions
- **Architecture: Three-Source Oregon Legal System**: the three Oregon legal sources and
  which governs which document type
- **Agent Architecture: Writing Quality Pipeline**: the seven-agent pipeline and how to
  install and use it

## Agents

The agents in `agents/` are Claude agent definition files and are not directly executable
by Gemini CLI. For a description of what each agent does and how the pipeline works, see
`AGENTS.md` at the repository root.

## Writing Rule

No em-dashes anywhere in this repository. Use commas, semicolons, colons, or restructured
sentences. This applies to all repository content you generate or edit, including
documentation, code comments, commit messages, and PR descriptions. The `no-em-dash`
pre-commit hook (PC-011) enforces this mechanically on every commit.
