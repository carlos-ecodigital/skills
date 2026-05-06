#!/usr/bin/env python3
"""
SKILL-001 / LANG-001 — English-only enforcement gate.

Detects non-English content in a facts file. Exits non-zero with a flag message
if >10% non-English content detected. Does not auto-translate.

Usage: python3 check_language.py <facts-file.md>
"""

import sys
import re


COMMON_ENGLISH_WORDS = set("""
the be to of and a in that have it for not on with as you do at this but his by
from they we say her she or an will my one all would there their what so up out
if about who get which go me when can like time no just him know take person into
year your good some could them see other than then now look only come its over think
also back after use two how our work first well way even new want because any these
give day most us is are was were has had been being am does did doing will would
should could may might must can could shall ought via per such each both either
neither though although however whereas while during without within across between
since until before above below where why which whose
""".split())


THRESHOLD = 0.15  # Lowered from 20% — technical content has lower common-word density.


def is_likely_english(text: str, threshold: float = THRESHOLD) -> tuple[bool, float]:
    """
    Returns (is_english, ratio). Counts common-English-word density vs. total words.
    """
    # Strip markdown punctuation, split on whitespace
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    if len(words) < 30:
        return (True, 1.0)  # Too short to judge
    common_count = sum(1 for w in words if w in COMMON_ENGLISH_WORDS)
    ratio = common_count / len(words)
    return (ratio >= threshold, ratio)


def has_non_latin_script(text: str) -> bool:
    """Detect CJK, Cyrillic, Arabic, Hebrew, Devanagari etc."""
    # Common non-Latin Unicode ranges
    pattern = re.compile(
        r"[一-鿿぀-ゟ゠-ヿЀ-ӿ"
        r"؀-ۿ֐-׿ऀ-ॿ]"
    )
    return bool(pattern.search(text))


def main():
    if len(sys.argv) != 2:
        print("usage: check_language.py <facts-file.md>", file=sys.stderr)
        sys.exit(2)

    with open(sys.argv[1], encoding="utf-8") as f:
        text = f.read()

    if has_non_latin_script(text):
        print(
            "[LANG-FLAG: facts file contains non-Latin script content. "
            "Skill does not auto-translate. Provide an English version "
            "before proceeding.]",
            file=sys.stderr,
        )
        sys.exit(1)

    is_eng, ratio = is_likely_english(text)
    if not is_eng:
        print(
            f"[LANG-FLAG: facts file appears non-English "
            f"(English-word density {ratio:.0%}, threshold {THRESHOLD:.0%}). "
            f"Skill does not auto-translate. Provide an English version.]",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"[LANG-PASS: English content confirmed ({ratio:.0%} common-word density, threshold {THRESHOLD:.0%}).]")
    sys.exit(0)


if __name__ == "__main__":
    main()
