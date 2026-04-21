"""Document-factory profile builders — stable public entry points.

Each `build_*` function is the recommended programmatic API for building
a profile-typed Document. They are thin aliases for the `profile_*`
functions in `generate.py`; the aliasing establishes a stable surface so
later refactors can move profile logic into dedicated builder modules
without breaking callers.

Usage:

    from builders import build_letter, build_agreement, build_memo

    doc = build_letter(title="Advisory Brief", date_str="17 April 2026",
                        entity="nl")

    doc = build_agreement(
        agreement_type="Letter of Intent",
        subject="for AI Infrastructure Services",
        client="Acme B.V.",
        client_address="1 Main St, 1000 AA Amsterdam",
        entity="nl",
    )

Related:
  - `common.build_letter` etc. re-export these as the skill-wide API.
  - Legacy callers using `from generate import profile_X` continue to
    work (aliases are bidirectional at call time).
"""
from __future__ import annotations

from builders.letter import build_letter
from builders.agreement import build_agreement
from builders.seed_memo import build_seed_memo
from builders.investor_memo import build_investor_memo
from builders.exec_summary import build_exec_summary

__all__ = [
    "build_letter",
    "build_agreement",
    "build_seed_memo",
    "build_investor_memo",
    "build_exec_summary",
]
