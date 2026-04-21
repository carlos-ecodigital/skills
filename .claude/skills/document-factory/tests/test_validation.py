"""M2 — build-time validation + per-profile structural audit tests.

Covers:
  - validate_agreement_inputs: happy path + every rejection case.
  - profile_agreement: raises AgreementValidationError when silent
    placeholder fallback would otherwise fire.
  - audit_agreement: R-24 detects THE UNDERSIGNED duplication when the
    cover carries party blocks; placeholder tokens in the rendered
    document are flagged.

Tests call `audit_agreement` directly without any `_fix_zoom` setup —
the audit wraps `_fix_zoom` internally so callers need not know about
python-docx's zoom quirk.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_FACTORY = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_FACTORY))

from validators import (  # noqa: E402
    AgreementValidationError,
    validate_agreement_inputs,
)
from audit_profiles import audit_agreement  # noqa: E402
from generate import profile_agreement  # noqa: E402


# ───────────────────────────── validate_agreement_inputs — happy paths


def test_validate_happy_non_binding() -> None:
    # Must not raise.
    validate_agreement_inputs(
        agreement_type="Letter of Intent",
        client="Acme B.V.",
        client_address="123 Main St, 1000 AA Amsterdam",
        formality="non_binding",
    )


def test_validate_happy_binding_with_registration() -> None:
    validate_agreement_inputs(
        agreement_type="Master Service Agreement",
        client="Acme B.V.",
        client_address="123 Main St, 1000 AA Amsterdam",
        formality="binding",
        client_reg_type="KvK",
        client_reg_number="12345678",
    )


# ───────────────────────────── validate_agreement_inputs — rejections


def test_validate_rejects_missing_address() -> None:
    with pytest.raises(AgreementValidationError) as ei:
        validate_agreement_inputs(
            agreement_type="Letter of Intent",
            client="Acme B.V.",
            client_address=None,
            formality="non_binding",
        )
    assert "client_address" in str(ei.value)


@pytest.mark.parametrize("whitespace_value", ["", "   ", "\t", "\n  \t"])
def test_validate_rejects_whitespace_only_address(whitespace_value: str) -> None:
    """Whitespace-only string must be treated the same as None/placeholder."""
    with pytest.raises(AgreementValidationError) as ei:
        validate_agreement_inputs(
            agreement_type="Letter of Intent",
            client="Acme B.V.",
            client_address=whitespace_value,
            formality="non_binding",
        )
    assert "client_address" in str(ei.value)


@pytest.mark.parametrize(
    "placeholder_address",
    ["[Address]", "[Client]"],   # address field can be polluted with either
)
def test_validate_rejects_placeholder_address(placeholder_address: str) -> None:
    with pytest.raises(AgreementValidationError) as ei:
        validate_agreement_inputs(
            agreement_type="Letter of Intent",
            client="Acme B.V.",
            client_address=placeholder_address,
            formality="non_binding",
        )
    assert "client_address" in str(ei.value)


@pytest.mark.parametrize(
    "placeholder_client", ["[Counterparty]", "[Client]"],
)
def test_validate_rejects_placeholder_client(placeholder_client: str) -> None:
    with pytest.raises(AgreementValidationError) as ei:
        validate_agreement_inputs(
            agreement_type="Letter of Intent",
            client=placeholder_client,
            client_address="123 Main St",
            formality="non_binding",
        )
    assert "client" in str(ei.value)


def test_validate_rejects_placeholder_agreement_type() -> None:
    with pytest.raises(AgreementValidationError) as ei:
        validate_agreement_inputs(
            agreement_type="[Agreement Type]",
            client="Acme B.V.",
            client_address="123 Main St",
            formality="non_binding",
        )
    assert "agreement_type" in str(ei.value)


def test_validate_rejects_binding_without_registration() -> None:
    with pytest.raises(AgreementValidationError) as ei:
        validate_agreement_inputs(
            agreement_type="Master Service Agreement",
            client="Acme B.V.",
            client_address="123 Main St",
            formality="binding",
            client_reg_type=None,
            client_reg_number=None,
        )
    msg = str(ei.value)
    # Error message uses CLI flag names for user-facing guidance.
    assert "--client-reg-type" in msg
    assert "--client-reg-number" in msg


def test_validate_reports_all_errors_at_once() -> None:
    """Multi-field failure must surface every field in one exception so a
    CLI caller sees all missing flags on the first run, not one at a time.
    Asserts the three specific CLI flag names are mentioned."""
    with pytest.raises(AgreementValidationError) as ei:
        validate_agreement_inputs(
            agreement_type="[Agreement Type]",
            client="[Counterparty]",
            client_address=None,
            formality="non_binding",
        )
    msg = str(ei.value)
    assert "--agreement-type" in msg
    assert "--client" in msg
    assert "--client-address" in msg


# ───────────────────────────── profile_agreement integration


def test_profile_agreement_rejects_silent_placeholders() -> None:
    # This is the MDCS defect: profile_agreement used to render a
    # valid-looking document with [Address] on the cover. It must now fail.
    # This is the single most important regression guard in the file —
    # deleting it silently re-opens the MDCS-class bug.
    with pytest.raises(AgreementValidationError):
        profile_agreement("Letter of Intent", entity="nl")


def test_profile_agreement_builds_with_full_inputs() -> None:
    doc = profile_agreement(
        "Letter of Intent",
        subject="for AI Infrastructure Services",
        client="Acme B.V.",
        client_address="123 Main St, 1000 AA Amsterdam",
        entity="nl",
    )
    # Full structural audit must pass (includes R-24 + placeholder checks).
    # No _fix_zoom call — audit_agreement handles it internally.
    violations = audit_agreement(doc)
    assert violations == [], violations


# ───────────────────────────── audit_agreement (R-24 + placeholder)


_R24_PREFIX = "agreement: R-24 —"


def test_audit_agreement_passes_clean_build() -> None:
    doc = profile_agreement(
        "Letter of Intent",
        client="Acme B.V.",
        client_address="123 Main St, 1000 AA Amsterdam",
        entity="nl",
    )
    assert audit_agreement(doc) == []


def test_audit_agreement_flags_undersigned_duplication() -> None:
    """R-24 — if cover carries parties, body with UNDERSIGNED heading fails.

    Asserts on the canonical rule-message prefix, not just the rule ID.
    If the rule's message text is reworked the test fails — which is the
    right signal: rule-message changes are user-visible and should be
    reviewed."""
    doc = profile_agreement(
        "Letter of Intent",
        client="Acme B.V.",
        client_address="123 Main St, 1000 AA Amsterdam",
        entity="nl",
    )
    # Simulate the bug: body re-declares the parties.
    doc.add_paragraph("THE UNDERSIGNED:")
    doc.add_paragraph("(1) Digital Energy Netherlands B.V., ...")
    doc.add_paragraph("(2) Acme B.V., ...")
    vios = audit_agreement(doc)
    assert any(v.startswith(_R24_PREFIX) for v in vios), (
        f"No violation starting with {_R24_PREFIX!r}. Got: {vios}"
    )


@pytest.mark.parametrize(
    "placeholder", ["[Counterparty]", "[Client]", "[Address]", "[Agreement Type]"],
)
def test_audit_agreement_flags_placeholder_token_in_body(placeholder: str) -> None:
    """Every token in `_UNACCEPTABLE_COVER_PLACEHOLDERS` must be rejected
    when it surfaces anywhere in the document body. Parametrized so the
    test explicitly covers the full catalogue — additions to the tuple
    must be matched by a new parameter entry here."""
    doc = profile_agreement(
        "Letter of Intent",
        client="Acme B.V.",
        client_address="123 Main St, 1000 AA Amsterdam",
        entity="nl",
    )
    doc.add_paragraph(f"Some clause referencing {placeholder} as the recipient.")
    vios = audit_agreement(doc)
    assert any(placeholder in v and "placeholder token" in v for v in vios), (
        f"Expected placeholder violation for {placeholder!r}. Got: {vios}"
    )
