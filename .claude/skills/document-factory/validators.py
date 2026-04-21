"""Build-time input validators for agreement / letter / memo profiles.

Raises `AgreementValidationError` on inputs that would produce a wrong
document. The previous behavior — silently rendering `[Address]` or
`[Counterparty]` placeholders — is now rejected at build time.

Addresses M2 of the document-factory rebuild (plan root-cause #1: silent
placeholder fallback).
"""
from __future__ import annotations


class AgreementValidationError(ValueError):
    """Raised when inputs to an agreement build would produce a wrong document.

    Examples that raise:
      - `client_address` omitted → would render `[Address]` placeholder.
      - `client == "[Counterparty]"` → default placeholder not overridden.
      - Binding agreement with missing registration on counterparty.
      - `agreement_type == "[Agreement Type]"` → default not overridden.
    """


# Placeholder tokens the factory uses in the absence of real input.
# Any of these surviving to build time means the caller forgot to supply
# real data. We reject here rather than let them leak into the output.
_PLACEHOLDER_TOKENS = frozenset({
    "[Counterparty]",
    "[Client]",
    "[Address]",
    "[Agreement Type]",
})


def _is_placeholder(value: str | None) -> bool:
    if value is None:
        return True
    v = value.strip()
    if not v:
        return True
    return v in _PLACEHOLDER_TOKENS


def validate_agreement_inputs(
    *,
    agreement_type: str | None,
    client: str | None,
    client_address: str | None,
    formality: str | None,
    client_reg_type: str | None = None,
    client_reg_number: str | None = None,
) -> None:
    """Validate inputs for an agreement build.

    Raises AgreementValidationError on the first violation found, with a
    message naming every missing/invalid field (not just the first) so the
    caller gets the full picture in one pass.
    """
    errors: list[str] = []

    if _is_placeholder(agreement_type):
        errors.append(
            "agreement_type is a placeholder or empty. "
            "Pass --agreement-type (e.g. 'Letter of Intent')."
        )

    if _is_placeholder(client):
        errors.append(
            "client (counterparty legal name) is a placeholder or empty. "
            "Pass --client (e.g. --client \"Acme B.V.\")."
        )

    if _is_placeholder(client_address):
        errors.append(
            "client_address is missing or a placeholder. "
            "Pass --client-address (e.g. --client-address \"123 Main St, 1000 AA Amsterdam\"). "
            "A branded agreement without a counterparty address is rejected at build time."
        )

    if formality == "binding":
        if not client_reg_type or not client_reg_type.strip():
            errors.append(
                "formality=binding requires --client-reg-type "
                "(e.g. KvK, CHE, EIN)."
            )
        if not client_reg_number or not client_reg_number.strip():
            errors.append(
                "formality=binding requires --client-reg-number."
            )

    if errors:
        raise AgreementValidationError(
            "Invalid inputs to build_agreement / profile_agreement:\n  - "
            + "\n  - ".join(errors)
        )
