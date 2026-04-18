#!/usr/bin/env python3
"""Stylometric feature extraction for the AI-detection research audit.

Computes the metrics the repo's own style-profile.md targets — sentence length
mean and standard deviation, type-token ratio, short/long-sentence fractions,
punctuation density, hedge density, banned-term density — plus proxies for
signals known to drive detector scores (burstiness, opener diversity, em-dash
frequency). Operates on the repo's before/after samples to quantify the
system's stylometric effect.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from statistics import mean, pstdev

REPO = Path(__file__).resolve().parents[3]
SAMPLES = REPO / "samples"
OUT_DIR = REPO / "docs" / "research" / "2026-04-ai-detection-audit"

# Terms from writing-style/ai-detection.md — verbatim blacklist.
BANNED_TERMS = [
    # vague qualifiers
    "significantly", "substantially", "considerably", "greatly", "markedly",
    # corporate buzzwords
    "leverage", "leveraging", "leverages", "synergies", "synergy",
    "optimize", "optimizes", "optimizing", "streamline", "streamlines",
    "streamlining", "empower", "empowers", "empowering", "enable", "enables", "enabling",
    # hype
    "best-in-class", "cutting-edge", "game-changer", "innovative",
    "revolutionary", "transformative", "state-of-the-art",
    # AI filler
    "delve into", "delves into", "delving into", "crucial",
    "robust", "seamless", "holistic", "comprehensive",
    "it's important to note", "in conclusion", "in summary", "to summarize",
    "moving forward", "in today's landscape", "at the end of the day",
    # puffery
    "pivotal", "vital", "groundbreaking", "testament", "enduring legacy",
    "unwavering", "unparalleled", "exemplary",
    # empty gerund phrases (substrings)
    "ensuring reliability", "showcasing features", "fostering collaboration",
    "driving growth", "enhancing performance", "delivering value",
    "enabling success",
]

HEDGE_TERMS = [
    "typically", "often", "usually", "generally", "frequently",
    "suggests", "suggest", "appears", "appear", "seems", "seem",
    "tends to", "tend to", "likely", "probably", "perhaps", "may ",
    "might", "could", "in most cases", "based on", "evidence suggests",
]

REPETITIVE_OPENERS = {"this", "the", "additionally", "furthermore", "moreover"}

SENT_END_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def extract_before(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    return strip_frontmatter(raw).strip()


def extract_rewrite(path: Path) -> str:
    """Pull the final rewrite from a stage-3-voice.md file.

    The repo's stage-3 convention is ``## Rewritten Document`` followed by a
    prose preamble, a ``---`` divider, the rewrite, and a closing ``---``.
    """
    raw = path.read_text(encoding="utf-8")
    m = re.search(r"^## Rewritten Document\s*$", raw, flags=re.MULTILINE)
    if m is None:
        raise ValueError(f"no Rewritten Document heading in {path}")
    start_heading = m.start()
    # first divider after the heading
    after_heading = raw[start_heading:]
    div_start = re.search(r"\n---\n", after_heading)
    if div_start is None:
        raise ValueError(f"no divider after heading in {path}")
    body_start = start_heading + div_start.end()
    # next divider closes the rewrite
    tail = raw[body_start:]
    div_end = re.search(r"\n---\n", tail)
    body_end = body_start + (div_end.start() if div_end else len(tail))
    rewrite = raw[body_start:body_end].strip()
    return rewrite


def strip_markdown_noise(text: str) -> str:
    """Drop code fences, YAML blocks, and bracketed author notes so the
    stylometric measurement reflects running prose, not scaffolding.
    """
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"\[AUTHOR[^\]]*\]", " ", text)
    text = re.sub(r"\[[A-Z ]+(—|--)[^\]]*\]", " ", text)  # [VERIFIED — ...]
    text = re.sub(r"\[(VERIFIED|UNVERIFIED|EXPERT JUDGMENT|ASSUMPTION|PROJECTION|SUSPECT)\]", " ", text)
    text = re.sub(r"^\s*#{1,6}\s+.*$", " ", text, flags=re.MULTILINE)  # drop headings
    text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.MULTILINE)  # bullet markers
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)  # numbered list markers
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # strip bold
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text


def split_sentences(text: str) -> list[str]:
    # Normalize whitespace then split on sentence-final punctuation.
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    sentences: list[str] = []
    for para in paragraphs:
        para = re.sub(r"\s+", " ", para)
        parts = SENT_END_RE.split(para)
        for p in parts:
            p = p.strip()
            if len(p) < 3:
                continue
            # Drop anything that's clearly a heading or ends with a colon acting as a header.
            if p.endswith(":") and len(p.split()) <= 6:
                continue
            sentences.append(p)
    return sentences


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))


def tokens(text: str) -> list[str]:
    return [m.group(0).lower() for m in WORD_RE.finditer(text)]


def count_banned(text: str) -> tuple[int, list[str]]:
    lower = text.lower()
    hits: list[str] = []
    for term in BANNED_TERMS:
        # word-boundary match for single words; substring for multi-word.
        if " " in term or "-" in term:
            if term in lower:
                count = lower.count(term)
                hits.extend([term] * count)
        else:
            matches = re.findall(rf"\b{re.escape(term)}\b", lower)
            hits.extend([term] * len(matches))
    return len(hits), hits


def count_hedges(sentences: list[str]) -> int:
    lower_sents = [s.lower() for s in sentences]
    hits = 0
    for s in lower_sents:
        for term in HEDGE_TERMS:
            if term in s:
                hits += 1
                break
    return hits


def opener_diversity(sentences: list[str]) -> tuple[int, int, float]:
    first_words = []
    for s in sentences:
        w = WORD_RE.findall(s)
        if w:
            first_words.append(w[0].lower())
    unique = len(set(first_words))
    repetitive_hits = sum(1 for w in first_words if w in REPETITIVE_OPENERS)
    ttr = unique / len(first_words) if first_words else 0.0
    return unique, repetitive_hits, ttr


def paragraph_lengths(text: str) -> list[int]:
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    out = []
    for p in paras:
        # count sentences in the paragraph
        p_sents = split_sentences(p)
        if p_sents:
            out.append(len(p_sents))
    return out


def analyze(text: str) -> dict:
    clean = strip_markdown_noise(text)
    sentences = split_sentences(clean)
    sent_lengths = [word_count(s) for s in sentences]
    toks = tokens(clean)
    uniq = set(toks)

    if sent_lengths:
        sl_mean = round(mean(sent_lengths), 2)
        sl_sd = round(pstdev(sent_lengths), 2) if len(sent_lengths) > 1 else 0.0
        short_frac = round(sum(1 for x in sent_lengths if x < 8) / len(sent_lengths), 3)
        long_frac = round(sum(1 for x in sent_lengths if x > 30) / len(sent_lengths), 3)
    else:
        sl_mean = sl_sd = short_frac = long_frac = 0.0

    ttr = round(len(uniq) / len(toks), 3) if toks else 0.0
    banned_count, banned_hits = count_banned(clean)
    hedge_n = count_hedges(sentences)
    hedge_density = round(hedge_n / len(sentences), 3) if sentences else 0.0
    unique_openers, repetitive_openers, opener_ttr = opener_diversity(sentences)
    em_dashes = clean.count("—")
    ascii_dashes = clean.count(" -- ")
    para_lengths = paragraph_lengths(clean)

    return {
        "word_count": len(toks),
        "sentence_count": len(sentences),
        "sentence_len_mean": sl_mean,
        "sentence_len_sd": sl_sd,
        "short_sentence_frac": short_frac,
        "long_sentence_frac": long_frac,
        "ttr": ttr,
        "banned_term_hits": banned_count,
        "banned_term_density_per_100w": round(banned_count / len(toks) * 100, 3) if toks else 0.0,
        "banned_term_examples": sorted(set(banned_hits))[:8],
        "hedge_density": hedge_density,
        "unique_sentence_openers": unique_openers,
        "repetitive_opener_hits": repetitive_openers,
        "opener_ttr": round(opener_ttr, 3),
        "em_dash_count": em_dashes,
        "ascii_double_dash_count": ascii_dashes,
        "paragraph_count": len(para_lengths),
        "paragraph_sentence_counts": para_lengths,
    }


def pipeline_targets_check(stats: dict) -> dict:
    """Map to the authoritative targets in writing-style/style-profile.md."""
    return {
        "sl_mean_17_22": 17 <= stats["sentence_len_mean"] <= 22,
        "sl_sd_ge_8": stats["sentence_len_sd"] >= 8,
        "short_ge_15pct": stats["short_sentence_frac"] >= 0.15,
        "long_ge_15pct": stats["long_sentence_frac"] >= 0.15,
        "ttr_ge_040": stats["ttr"] >= 0.40,
        "hedge_5_10pct": 0.05 <= stats["hedge_density"] <= 0.10,
        "banned_zero": stats["banned_term_hits"] == 0,
    }


def main() -> None:
    samples = ["01-paragraph-summary", "02-client-status-email",
               "03-expense-policy-memo", "04-onboarding-proposal",
               "05-workforce-planning-analysis"]

    results = {}
    for s in samples:
        before_path = SAMPLES / "before" / f"{s}.md"
        after_path = SAMPLES / "after" / s / "stage-3-voice.md"
        before_text = extract_before(before_path)
        after_text = extract_rewrite(after_path)

        before_stats = analyze(before_text)
        after_stats = analyze(after_text)
        results[s] = {
            "before": {
                "path": str(before_path.relative_to(REPO)),
                "stats": before_stats,
                "targets_met": pipeline_targets_check(before_stats),
            },
            "after_stage3": {
                "path": str(after_path.relative_to(REPO)),
                "stats": after_stats,
                "targets_met": pipeline_targets_check(after_stats),
            },
        }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / "stylometry-results.json"
    out_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"wrote {out_file.relative_to(REPO)}")

    # Summary table to stdout for inspection.
    header = (
        f"{'sample':<36}{'phase':<8}{'words':>6}{'sents':>6}"
        f"{'sl_mean':>9}{'sl_sd':>8}{'short%':>8}{'long%':>8}"
        f"{'ttr':>7}{'ban':>5}{'hedge%':>8}"
    )
    print(header)
    print("-" * len(header))
    for s, data in results.items():
        for phase in ("before", "after_stage3"):
            st = data[phase]["stats"]
            label = "before" if phase == "before" else "stage3"
            print(
                f"{s:<36}{label:<8}{st['word_count']:>6}{st['sentence_count']:>6}"
                f"{st['sentence_len_mean']:>9.2f}{st['sentence_len_sd']:>8.2f}"
                f"{int(st['short_sentence_frac']*100):>7}%"
                f"{int(st['long_sentence_frac']*100):>7}%"
                f"{st['ttr']:>7.3f}{st['banned_term_hits']:>5}"
                f"{int(st['hedge_density']*100):>7}%"
            )


if __name__ == "__main__":
    main()
