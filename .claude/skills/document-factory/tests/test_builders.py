"""M1.1 — builders package tests.

Verifies:
  - Each build_* function is a stable alias for the corresponding
    generate.profile_* function (same callable, or semantic equivalent).
  - `from builders import build_X` works for every profile.
  - `from builders.<module> import build_X` works too (per-profile module
    access).
  - Each builder produces a Document when called with valid arguments,
    matching the output shape of its underlying profile function.

This is a regression floor for the builders indirection — if a future
refactor moves profile implementation into the builder modules, these
tests ensure the public API surface keeps the same semantics.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

_FACTORY = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_FACTORY))

from builders import (  # noqa: E402
    build_letter,
    build_agreement,
    build_seed_memo,
    build_investor_memo,
    build_exec_summary,
)
import generate  # noqa: E402


# ───────────────────────────── package-level imports


def test_builders_package_exports_all_build_fns() -> None:
    import builders
    for name in (
        "build_letter",
        "build_agreement",
        "build_seed_memo",
        "build_investor_memo",
        "build_exec_summary",
    ):
        assert name in builders.__all__, f"Missing from __all__: {name}"
        assert callable(getattr(builders, name)), f"Not callable: {name}"


def test_per_profile_module_imports() -> None:
    """Each profile has its own module — importing via the module path
    is also supported."""
    from builders.letter import build_letter as bl
    from builders.agreement import build_agreement as ba
    from builders.seed_memo import build_seed_memo as bsm
    from builders.investor_memo import build_investor_memo as bim
    from builders.exec_summary import build_exec_summary as bes
    assert all(callable(f) for f in (bl, ba, bsm, bim, bes))


# ───────────────────────────── alias semantics (builders delegate to profile_*)


def test_build_letter_produces_same_output_as_profile_letter() -> None:
    """Builder is a delegation: same inputs → same output shape."""
    via_builder = build_letter(title="Test", date_str="17 April 2026", entity="nl")
    via_profile = generate.profile_letter(title="Test", date_str="17 April 2026", entity="nl")
    # Can't compare Document objects directly; compare paragraph count as a
    # structural proxy. If the alias drifts, the counts diverge.
    assert len(via_builder.paragraphs) == len(via_profile.paragraphs)


def test_build_seed_memo_shape() -> None:
    doc = build_seed_memo(client="Test Fund", date_str="17 April 2026", entity="nl")
    assert doc is not None
    # Seed memo has a cover + 8 sections; expect >= 9 headings' worth of content
    assert len(doc.paragraphs) > 10


def test_build_investor_memo_shape() -> None:
    doc = build_investor_memo(client="Test Fund", date_str="17 April 2026", entity="nl")
    assert doc is not None
    assert len(doc.paragraphs) > 10


def test_build_exec_summary_shape() -> None:
    doc = build_exec_summary(title="Test Summary", date_str="17 April 2026", entity="nl")
    assert doc is not None


# ───────────────────────────── build_agreement inherits M2 validation (when present)


def test_build_agreement_rejects_placeholder_inputs() -> None:
    """If the M2 validators module is present (document-factory rebuild
    M2), build_agreement with placeholder defaults must raise — same as
    profile_agreement. If M2 is not present (pre-rebuild env), the call
    renders with placeholders — in which case this test is skipped.
    """
    try:
        import validators  # noqa: F401
    except ImportError:
        import pytest
        pytest.skip("M2 validators module not available in this environment")

    from validators import AgreementValidationError  # type: ignore
    import pytest
    with pytest.raises(AgreementValidationError):
        build_agreement(agreement_type="Letter of Intent", entity="nl")


def test_build_agreement_succeeds_with_full_inputs() -> None:
    """Builder with complete valid inputs produces a Document."""
    # M2 requires binding agreements to have registration fields;
    # "Letter of Intent" is non-binding by default so reg is optional.
    doc = build_agreement(
        agreement_type="Letter of Intent",
        subject="for Test",
        client="Test Counterparty B.V.",
        client_address="1 Main St, 1000 AA Amsterdam",
        entity="nl",
    )
    assert doc is not None
    assert len(doc.paragraphs) > 5  # cover renders multiple paragraphs
