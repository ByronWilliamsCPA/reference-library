#!/usr/bin/env python3
"""Build phase_2_5_samples.md: a self-contained sample package for external
AI-detector evaluation. Read-only on the repo; writes one file in the repo root.
"""

from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SAMPLES = REPO / "samples"
OUT = REPO / "phase_2_5_samples.md"

FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1).strip()


def extract_rewrite(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    m = re.search(r"^## Rewritten Document\s*$", raw, flags=re.MULTILINE)
    if m is None:
        raise ValueError(f"no Rewritten Document heading in {path}")
    after = raw[m.start():]
    div = re.search(r"\n---\n", after)
    body_start = m.start() + div.end()
    tail = raw[body_start:]
    div_end = re.search(r"\n---\n", tail)
    body_end = body_start + (div_end.start() if div_end else len(tail))
    return raw[body_start:body_end].strip()


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", text))


def truncate_paragraphs(text: str, max_words: int) -> tuple[str, bool]:
    """Trim from the end at paragraph boundaries until under max_words."""
    paras = text.split("\n\n")
    out: list[str] = []
    total = 0
    for p in paras:
        w = word_count(p)
        if total + w > max_words and out:
            break
        out.append(p)
        total += w
    trimmed = "\n\n".join(out).strip()
    return trimmed, len(out) < len(paras)


def short_sha() -> str:
    r = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    return r.stdout.strip()


def load_before(slug: str) -> str:
    return strip_frontmatter((SAMPLES / "before" / f"{slug}.md").read_text(encoding="utf-8"))


def load_stage3(slug: str) -> str:
    return extract_rewrite(SAMPLES / "after" / slug / "stage-3-voice.md")


# Selection: three matched pairs (U + S) on topics 02, 04, 05 plus topic 03.
# - Topic 01 (paragraph summary) is 163 words before-edit; below the 300-word
#   floor in the prompt, so excluded from the package.
# - Topic 03 (expense policy memo) before-body runs 849 words; stage-3 runs
#   ~884. Both trimmed to ≤800 words at paragraph boundaries.
# - Topic 04 stage-3 also trimmed.
# Each stage-3 extraction is the final rewrite body only; meta commentary,
# stylometry reports, and pipeline YAML are stripped.

ENTRIES = [
    {
        "title": "Client Status Email — Unedited AI Output",
        "bucket": "U",
        "source_path": "samples/before/02-client-status-email.md",
        "domain": "Business correspondence (management-consulting status email to a manufacturing client, SME role prompt)",
        "loader": lambda: load_before("02-client-status-email"),
        "max_words": 800,
    },
    {
        "title": "Client Status Email — System-Edited Rewrite",
        "bucket": "S",
        "source_path": "samples/after/02-client-status-email/stage-3-voice.md",
        "domain": "Business correspondence (same topic and register as the unedited companion, run through the three-stage editing pipeline)",
        "loader": lambda: load_stage3("02-client-status-email"),
        "max_words": 800,
    },
    {
        "title": "Expense Policy Memo — Unedited AI Output",
        "bucket": "U",
        "source_path": "samples/before/03-expense-policy-memo.md",
        "domain": "Policy memo (HR, tax compliance, reimbursement rules; SME role prompt)",
        "loader": lambda: load_before("03-expense-policy-memo"),
        "max_words": 800,
    },
    {
        "title": "Expense Policy Memo — System-Edited Rewrite",
        "bucket": "S",
        "source_path": "samples/after/03-expense-policy-memo/stage-3-voice.md",
        "domain": "Policy memo (same topic, post-pipeline; retains two [AUTHOR MUST CORRECT] flags on mileage rate and gift-cap disclosure as residual factual items)",
        "loader": lambda: load_stage3("03-expense-policy-memo"),
        "max_words": 800,
    },
    {
        "title": "Onboarding Proposal — Unedited AI Output",
        "bucket": "U",
        "source_path": "samples/before/04-onboarding-proposal.md",
        "domain": "Internal proposal (regional accounting firm new-hire program, no system prompt)",
        "loader": lambda: load_before("04-onboarding-proposal"),
        "max_words": 800,
    },
    {
        "title": "Onboarding Proposal — System-Edited Rewrite",
        "bucket": "S",
        "source_path": "samples/after/04-onboarding-proposal/stage-3-voice.md",
        "domain": "Internal proposal (same topic, post-pipeline; contains one explicit [AUTHOR TO COMPLETE] placeholder block preserved as the repo committed it)",
        "loader": lambda: load_stage3("04-onboarding-proposal"),
        "max_words": 800,
    },
    {
        "title": "Workforce Planning Analysis — Unedited AI Output",
        "bucket": "U",
        "source_path": "samples/before/05-workforce-planning-analysis.md",
        "domain": "Analytical essay (automation and mid-market professional-services workforce planning, no system prompt)",
        "loader": lambda: load_before("05-workforce-planning-analysis"),
        "max_words": 800,
    },
    {
        "title": "Workforce Planning Analysis — System-Edited Rewrite",
        "bucket": "S",
        "source_path": "samples/after/05-workforce-planning-analysis/stage-3-voice.md",
        "domain": "Analytical essay (same topic, post-pipeline)",
        "loader": lambda: load_stage3("05-workforce-planning-analysis"),
        "max_words": 800,
    },
]

EXCLUDED = [
    (
        "samples/before/01-paragraph-summary.md and its stage-3 companion",
        "163-word and 209-word bodies fall below the 300-word floor specified in "
        "the Phase 2.5 guardrails. Most free-tier detectors also require 250+ words.",
    ),
]

CONFIDENTIALITY_SCAN = (
    "All eight selected samples are from samples/before and samples/after in the "
    "reference-library repo. They were generated via the committed "
    "scripts/generate_before_samples.py against an OpenRouter model with generic "
    "topic prompts. None contains real client names, employee names, taxpayer "
    "identifiers, account details, dollar figures tied to real engagements, or "
    "OST-internal codenames. The expense-memo sample references 'the firm' "
    "generically. The client-status email uses 'Key Sponsor' as a placeholder "
    "and a bracketed [Your Name] closing block. No PII redaction needed."
)

CLASSIFICATION_NOTE = (
    "The repo contains no human-authored (pre-AI) baseline prose. The samples/ "
    "directory is built exclusively from minimax/minimax-m2 outputs to expose "
    "AI patterns for the editing pipeline to catch. That design choice is "
    "documented in samples/README.md. The package therefore ships with zero "
    "bucket-H samples; the external detector study must source human baselines "
    "from outside this repo if false-positive testing is required. Buckets S "
    "and U carry shared topics so the external tool can compare pre-edit versus "
    "post-edit scores on matched text."
)


def render() -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    sha = short_sha()
    entries_rendered = []
    bucket_counts = {"H": 0, "S": 0, "U": 0, "X": 0}
    total_words = 0

    for i, e in enumerate(ENTRIES, start=1):
        text = e["loader"]()
        trimmed, was_trimmed = truncate_paragraphs(text, e["max_words"])
        wc = word_count(trimmed)
        bucket_counts[e["bucket"]] += 1
        total_words += wc
        excerpt_note = "Full body" if not was_trimmed else "Excerpted: leading paragraphs only, full paragraphs kept intact"
        entries_rendered.append(
            f"## Sample {i:02d} — {e['title']}\n"
            f"- **Classification:** {e['bucket']}\n"
            f"- **Source path:** {e['source_path']}\n"
            f"- **Word count:** {wc}\n"
            f"- **Domain / register:** {e['domain']}\n"
            f"- **Excerpt note:** {excerpt_note}\n\n"
            f"{trimmed}\n\n---"
        )

    excluded_block = "\n".join(
        f"  - `{path}` — {reason}" for path, reason in EXCLUDED
    )

    header = (
        f"# Phase 2.5 Sample Package\n\n"
        f"Generated: {today}\n"
        f"Source repo: ByronWilliamsCPA/reference-library\n"
        f"Commit SHA: {sha}\n\n"
        f"## Inventory Summary\n\n"
        f"- Total candidates scouted: 15 prose files under `samples/` "
        f"(5 `before/*.md`, 5 `after/*/stage-3-voice.md`, 5 `after/*/recap.md`); "
        f"all other Markdown in the repo is reference-rule or agent-definition material, not prose.\n"
        f"- Samples selected: {len(ENTRIES)} "
        f"(H={bucket_counts['H']}, S={bucket_counts['S']}, "
        f"U={bucket_counts['U']}, X={bucket_counts['X']})\n"
        f"- Total selected word count: {total_words}\n"
        f"- Excluded for confidentiality: 0\n"
        f"- Excluded for size or scope:\n{excluded_block}\n\n"
        f"### Classification Note\n\n{CLASSIFICATION_NOTE}\n\n"
        f"### Confidentiality Pre-Screen\n\n{CONFIDENTIALITY_SCAN}\n\n"
        f"---\n\n"
    )

    return header + "\n\n".join(entries_rendered) + "\n"


def main() -> None:
    OUT.write_text(render(), encoding="utf-8")
    # Print a short report for the caller.
    body = OUT.read_text(encoding="utf-8")
    total_words = sum(word_count(s) for s in [body])  # noqa: F841
    print(f"wrote: {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
