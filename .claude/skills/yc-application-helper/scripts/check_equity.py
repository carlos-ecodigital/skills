#!/usr/bin/env python3
"""
SKILL-003 / EQUITY-001 — Numeric equity-summation validator gate.

Extracts founder-equity percentages from the facts file (per-founder P-ROLE-2
entries and the Q-EQ-3 cap-table description) and validates:
  - SUM_PROFILES <= 100
  - SUM_CAPTABLE <= 100
  - |SUM_PROFILES - SUM_CAPTABLE| <= tolerance (default 1)

Exits non-zero with EQUITY-FLAG if any check fails.

Usage: python3 check_equity.py <facts-file.md> [--tolerance N]
"""

import sys
import re
import argparse


def find_section(text: str, header_pattern: str) -> str:
    """Return the body of a markdown section whose header matches, until next ##."""
    m = re.search(rf"^##\s+.*{header_pattern}.*$", text, re.IGNORECASE | re.MULTILINE)
    if not m:
        return ""
    start = m.end()
    next_h = re.search(r"^##\s+", text[start:], re.MULTILINE)
    end = start + next_h.start() if next_h else len(text)
    return text[start:end]


def extract_equity_percentages(text: str) -> list[float]:
    """Extract percentages adjacent to 'equity'-tagged labels only.

    Avoids picking up time-commitment, vesting, or unrelated %s.
    Looks for lines containing 'equity' (case-insensitive) plus 'NN%'.
    """
    result = []
    for line in text.split("\n"):
        if not re.search(r"equity", line, re.IGNORECASE):
            continue
        # Skip 'employee pool' / 'option pool' (still equity but not founder share)
        # Actually keep them — they count toward 100%
        for pct in re.findall(r"(\d+(?:\.\d+)?)\s*%", line):
            result.append(float(pct))
    return result


def extract_percentages(text: str) -> list[float]:
    """Legacy / fallback: extract all 'NN%' occurrences."""
    return [float(p) for p in re.findall(r"(\d+(?:\.\d+)?)\s*%", text)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("facts_file")
    ap.add_argument("--tolerance", type=float, default=1.0)
    args = ap.parse_args()

    with open(args.facts_file, encoding="utf-8") as f:
        text = f.read()

    # Heuristic: per-founder P-ROLE-2 lives under "## Founders" sub-sections.
    founders_section = find_section(text, r"founders?")
    captable_section = (
        find_section(text, r"cap\s*table") or find_section(text, r"equity\s*structure")
    )

    # Prefer equity-tagged lines; do NOT fall back to all-percentages
    # (that picks up time-commitment %, vesting %, etc. — too loose).
    # If no equity-tagged lines found, report explicitly so user knows.
    profile_pcts = extract_equity_percentages(founders_section)
    captable_pcts = extract_equity_percentages(captable_section)

    if not profile_pcts and not captable_pcts:
        # Could be pre-incorporation OR equity fields are gap-marked.
        # Distinguish by looking for [GAP] markers near "equity" keyword.
        has_equity_gaps = bool(
            re.search(r"equity[^\n]*\[GAP", text, re.IGNORECASE)
        )
        if has_equity_gaps:
            print("[EQUITY-INFO: equity fields are [GAP]-marked. Founders must specify equity percentages before submission. Pre-draft fuzziness gate flags this.]")
        else:
            print("[EQUITY-INFO: no equity percentages found in facts file. If pre-incorporation, this is fine; otherwise add cap table.]")
        sys.exit(0)

    # Heuristic filter: each founder's profile typically has equity + time-commitment
    # both expressed as %; we want only the equity figure. Without explicit labels
    # we can't disambiguate cleanly, so flag if ambiguous.
    sum_profiles = sum(profile_pcts) if profile_pcts else None
    sum_captable = sum(captable_pcts) if captable_pcts else None

    if sum_profiles is None and sum_captable is None:
        print("[EQUITY-INFO: no equity percentages found in facts file. "
              "If pre-incorporation, this is fine; otherwise add cap table.]")
        sys.exit(0)

    msgs = []
    # Each side independently: must sum to ≤100% (founder + employee + investor totals).
    if sum_profiles is not None and sum_profiles > 100 + args.tolerance:
        msgs.append(f"[EQUITY-FLAG: profile section equity sums to {sum_profiles}% (>100%).]")
    if sum_captable is not None and sum_captable > 100 + args.tolerance:
        msgs.append(f"[EQUITY-FLAG: cap-table sums to {sum_captable}% (>100%).]")

    # Cross-check between profile and cap-table when both are present.
    if (
        sum_profiles is not None
        and sum_captable is not None
        and abs(sum_profiles - sum_captable) > args.tolerance
    ):
        msgs.append(
            f"[EQUITY-FLAG: profile sum {sum_profiles}% vs cap-table sum "
            f"{sum_captable}% differ by more than tolerance "
            f"(±{args.tolerance}%). Reconcile before drafting.]"
        )

    if msgs:
        for m in msgs:
            print(m)
        sys.exit(1)

    print(
        f"[EQUITY-PASS: profile sum {sum_profiles}%, cap-table sum {sum_captable}%, "
        f"within tolerance.]"
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
