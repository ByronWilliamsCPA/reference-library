"""Generate before-state samples for the writing quality pipeline.

Usage:
    python scripts/generate_before_samples.py
    python scripts/generate_before_samples.py --only 05-workforce-planning-analysis.md

Calls the OpenRouter API with minimal prompts to produce natural AI-mechanical
output — vague qualifiers, gerund padding, transition overuse — that the
three-stage pipeline (grammar -> validation -> voice) is designed to catch.

Model: minimax/minimax-m2 (top-used OpenRouter model, no house-style tuning)

System prompt strategy:
  Samples 01, 04, and 05: no system prompt (raw baseline output)
  Samples 02 and 03: SME role (realistic use case where user frames expertise,
    not writing quality; suppresses self-editing on style)

Output: samples/before/{filename}.md with YAML frontmatter header
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import TypedDict

REPO_ROOT = Path(__file__).parent.parent
SAMPLES_DIR = REPO_ROOT / "samples" / "before"
ENV_FILE = REPO_ROOT / ".env"
MODEL = "minimax/minimax-m2"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


class Sample(TypedDict):
    """Configuration for one before-state sample."""

    filename: str
    format_label: str
    topic: str
    system_prompt: str | None
    user_prompt: str


SAMPLES: list[Sample] = [
    {
        "filename": "01-paragraph-summary.md",
        "format_label": "paragraph-summary",
        "topic": "Remote work long-term effects on productivity and culture",
        "system_prompt": None,
        "user_prompt": (
            "Write a single paragraph executive summary (120-180 words) of current research "
            "findings on remote work's long-term effects on employee productivity and "
            "organizational culture. Use no headers, subheadings, or bullet points. "
            "Plain prose only."
        ),
    },
    {
        "filename": "02-client-status-email.md",
        "format_label": "email",
        "topic": "Operational efficiency project status update to manufacturing client",
        "system_prompt": (
            "You are a senior management consultant with 15 years of experience in "
            "operational efficiency."
        ),
        "user_prompt": (
            "Write a professional project-status email to a mid-size manufacturing client. "
            "The project is a 6-month operational efficiency review, currently in month 4. "
            "Include a greeting, 3-4 body paragraphs covering status, risks, and next steps, "
            "and a professional closing. 250-400 words."
        ),
    },
    {
        "filename": "03-expense-policy-memo.md",
        "format_label": "memo",
        "topic": "Employee expense reimbursement policy update recommendation",
        "system_prompt": "You are the HR Director at a 200-person professional services firm.",
        "user_prompt": (
            "Write an internal memo recommending that the firm update its employee expense "
            "reimbursement policy. Use a standard memo header (To / From / Date / Subject), "
            "followed by Executive Summary, Background, Analysis, Recommendation, and "
            "Implementation Steps sections. 500-800 words."
        ),
    },
    {
        "filename": "04-onboarding-proposal.md",
        "format_label": "proposal",
        "topic": "New-hire onboarding program restructure for regional accounting firm",
        "system_prompt": None,
        "user_prompt": (
            "Write a short internal proposal recommending a restructured new-hire onboarding "
            "program for a regional accounting firm. Include a problem statement, proposed "
            "solution, expected benefits, and a brief implementation outline. 350-500 words. "
            "Prose paragraphs, not bullet lists."
        ),
    },
    {
        "filename": "05-workforce-planning-analysis.md",
        "format_label": "analytical-report",
        "topic": "Automation impact on workforce planning for mid-market professional services firms",
        "system_prompt": None,
        "user_prompt": (
            "Write an analytical report (400-550 words) examining how automation is affecting "
            "workforce planning for mid-market professional services firms. Analyze four "
            "distinct dimensions: (1) productivity and output effects, (2) role displacement "
            "and skill evolution, (3) talent acquisition and retention shifts, and "
            "(4) implementation costs and return on investment. Write in continuous prose "
            "paragraphs — no bullet points, no numbered lists, no subheadings. Each dimension "
            "should be its own paragraph, connected by transitions between them."
        ),
    },
]


def load_api_key() -> str:
    """Parse OPENROUTER_API_KEY from the .env file.

    Returns:
        The API key string.

    Raises:
        SystemExit: If .env is missing or the key is absent.
    """
    if not ENV_FILE.exists():
        print(f"Error: .env not found at {ENV_FILE}", file=sys.stderr)
        sys.exit(1)

    for raw_line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("OPENROUTER_API_KEY="):
            key = line.split("=", 1)[1].strip()
            if key:
                return key

    print("Error: OPENROUTER_API_KEY not found in .env", file=sys.stderr)
    sys.exit(1)


def call_openrouter(
    api_key: str,
    system_prompt: str | None,
    user_prompt: str,
) -> str:
    """Call the OpenRouter chat completions endpoint.

    Args:
        api_key: OpenRouter API key.
        system_prompt: Optional system message. None omits the system turn entirely.
        user_prompt: User message content.

    Returns:
        The model's text response.

    Raises:
        SystemExit: On HTTP error or unexpected response structure.
    """
    messages: list[dict[str, str]] = []
    if system_prompt is not None:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_prompt})

    payload = json.dumps({"model": MODEL, "messages": messages}).encode("utf-8")

    req = urllib.request.Request(
        OPENROUTER_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        # qlty-ignore: bandit:B310 -- URL is a module-level constant, not user input
        with urllib.request.urlopen(req, timeout=60) as response:  # noqa: S310
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8")
        print(f"\nHTTP {exc.code}: {error_body}", file=sys.stderr)
        sys.exit(1)

    data: dict[str, object] = json.loads(body)

    try:
        choices = data["choices"]
        if not isinstance(choices, list):
            raise TypeError(f"choices: expected list, got {type(choices).__name__}")
        first = choices[0]
        if not isinstance(first, dict):
            raise TypeError(f"choices[0]: expected dict, got {type(first).__name__}")
        message = first["message"]
        if not isinstance(message, dict):
            raise TypeError(f"message: expected dict, got {type(message).__name__}")
        content = message["content"]
        if not isinstance(content, str):
            raise TypeError(f"content: expected str, got {type(content).__name__}")
        return content
    except (KeyError, IndexError, TypeError) as exc:
        print(f"\nUnexpected response structure: {exc}\n{body}", file=sys.stderr)
        sys.exit(1)


def build_frontmatter(sample: Sample) -> str:
    """Build YAML frontmatter for a sample file.

    Args:
        sample: Sample configuration.

    Returns:
        Frontmatter block including opening and closing --- delimiters and a
        trailing blank line before the content body.
    """
    system_label = "none" if sample["system_prompt"] is None else "sme-role"
    timestamp = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "---",
        f"format: {sample['format_label']}",
        f"topic:  {sample['topic']}",
        f"model:  {MODEL}",
        f"system_prompt: {system_label}",
        f"generated: {timestamp}",
        "stage: before",
        "---",
        "",
    ]
    return "\n".join(lines) + "\n"


def save_sample(sample: Sample, content: str) -> Path:
    """Write a sample file to samples/before/.

    Args:
        sample: Sample configuration (provides filename and metadata).
        content: Model-generated text.

    Returns:
        Absolute path of the written file.
    """
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    output_path = SAMPLES_DIR / sample["filename"]
    output_path.write_text(build_frontmatter(sample) + content, encoding="utf-8")
    return output_path


def main() -> None:
    """Generate all before-state samples and save to samples/before/."""
    parser = argparse.ArgumentParser(description="Generate pipeline before-state samples.")
    parser.add_argument(
        "--only",
        metavar="FILENAME",
        help="Generate only the sample with this filename (e.g. 05-workforce-planning-analysis.md)",
    )
    args = parser.parse_args()

    api_key = load_api_key()

    samples_to_run = (
        [s for s in SAMPLES if s["filename"] == args.only] if args.only else SAMPLES
    )
    if not samples_to_run:
        print(f"Error: no sample with filename '{args.only}'", file=sys.stderr)
        sys.exit(1)

    print(f"Model:   {MODEL}")
    print(f"Output:  {SAMPLES_DIR.relative_to(REPO_ROOT)}")
    print(f"Samples: {len(samples_to_run)}")
    print()

    for index, sample in enumerate(samples_to_run, start=1):
        system_label = "no system prompt" if sample["system_prompt"] is None else "sme role"
        print(
            f"[{index}/{len(samples_to_run)}] {sample['filename']} ({system_label})...",
            end=" ",
            flush=True,
        )

        content = call_openrouter(
            api_key=api_key,
            system_prompt=sample["system_prompt"],
            user_prompt=sample["user_prompt"],
        )

        output_path = save_sample(sample, content)
        word_count = len(content.split())
        print(f"OK ({word_count} words) -> {output_path.relative_to(REPO_ROOT)}")

    print()
    print(f"Done. {len(samples_to_run)} sample(s) written to {SAMPLES_DIR.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
