# Agent Architecture

This repository provides seven Claude agent definitions for a writing quality pipeline.
All agents are general-purpose with no project-specific content baked in. After installation,
they are available in every Claude Code project without per-project configuration.

## Installation

Run the setup script once from the repository root:

```bash
bash scripts/setup.sh
```

This installs all seven agents to `~/.claude/agents/` with the correct absolute paths
substituted for your clone location. It also bootstraps `config/profiles.toml` from the
shipped `config/profiles.example.toml` if no local config exists. Re-run after moving or
recloning the repository.

New users should run the `style-analyzer` agent first to calibrate the style profile
before using the generators or editing pipeline. The analyzer writes per-person calibration
data to `config/profiles/{person}/{style}.md` (gitignored), so calibrating a new person
never touches the repo's shipped default profile.

## Invocation: Person × Style

Every agent resolves a **person** and **style** at invocation time. Both have defaults from
`config/profiles.toml`, so calls without parameters still work.

```text
Use the document-drafter agent.                                      # → defaults
Use the document-drafter agent. person=byron style=work-email
Use the writing-style-editor agent with person=ariannah, style=client-memo.
```

The agent reads the resolved profile by calling `scripts/profile_resolver.py` and uses
those values for stylometry, palette, legal-source binding, and Tier 3 punctuation
overrides (e.g., `no-em-dash`). See `CLAUDE.md` for the resolution rules and
`writing-style/punctuation-preferences.md` for the override catalog.

## Agent Overview

### Pre-Pipeline: Calibration

| Agent | File | Purpose |
| --- | --- | --- |
| Style Analyzer | `agents/style-analyzer.md` | Analyze writing samples, compute stylometry, characterize voice, update `style-profile.md` |

Run the style analyzer once when a new user adopts the library or after a significant
evolution in writing style. Provide 3 to 5 writing samples totaling at least 2,000 words.
The analyzer outputs updated targets for `writing-style/style-profile.md` and adjustment
notes for the three pipeline agents.

### Pre-Pipeline: Generators

These agents produce text that feeds into the editing pipeline. Both apply
`writing-style/style-profile.md` targets and `writing-style/ai-detection.md` constraints
during generation to minimize downstream correction cycles.

| Agent | File | Purpose |
| --- | --- | --- |
| Document Drafter | `agents/document-drafter.md` | Generate voice-calibrated first drafts from outlines, bullets, prompts, or prior documents |
| Tone Rewriter | `agents/tone-rewriter.md` | Transform a document's register for a different audience while preserving all factual content |

Both agents tag output with `ai_generated: true` metadata, which signals Stage 3 to apply
heightened AI pattern scrutiny.

**Generator workflow**: Input → Generator Agent → Stage 1 → Stage 2 → Stage 3 → Submission

### Editing Pipeline: Stages 1 to 3

Run the three editing agents in order. Each stage has a distinct responsibility.

| Stage | Agent | File | Scope |
| --- | --- | --- | --- |
| 1 | Grammar and Composition Editor | `agents/grammar-composition-editor.md` | Grammar, composition, plain language, AI-mechanical patterns |
| 2 | Document Validator | `agents/document-validator.md` | Factual accuracy, assumptions, hallucinations, bias, reasoning errors |
| 3 | Writing Style Editor | `agents/writing-style-editor.md` | Voice alignment, AI pattern detection, stylometry matching |

**Why this order**: Grammar fixes are mechanical and objective. Factual errors are highest-stakes
for credibility. Style and persona are final polish on clean, verified text.

**Remediation**: If Stage 3 rewrites text for voice, those sections flow back through Stage 1
then Stage 2. Maximum 3 remediation cycles before requiring human review.

**Pipeline workflow**: Draft → Stage 1 (grammar) → Stage 2 (facts) → Stage 3 (voice) → Submission

### Post-Pipeline: Analysis

| Agent | File | Purpose |
| --- | --- | --- |
| Audience Reaction Analyzer | `agents/audience-reaction-analyzer.md` | Predict audience comprehension, persuasion effectiveness, emotional response, and action clarity |

Run after the editing pipeline completes. Provide the finished document plus a target
audience description and desired outcome. The analyzer reports comprehension gaps,
persuasion weaknesses, emotional trajectory, and action clarity ranked by impact.

The analyzer does not edit text. If findings require revision, the document-drafter or
tone-rewriter generates updated content, which then re-enters the editing pipeline.

**Full workflow**: Input → Generator → Stage 1 → Stage 2 → Stage 3 → Audience Analyzer → (revision if needed)

## Extending Agents for a Specific Project

To add project-specific rules on top of a base agent, create a `.claude/agents/` file in
the target project with the additional content. The globally installed base agent handles
the standard pipeline; the project file adds domain-specific rules on top.

```text
# In project/.claude/agents/writing-style-editor-legal.md
# Extends the base writing-style-editor with Oregon legal style rules.

## Oregon Legal Style Additions
[project-specific rules here]
```

## Source Files

All agent definition files live in `agents/` at the repository root. The setup script reads
each file, substitutes the absolute path to the reference library, and writes the result to
`~/.claude/agents/`.
