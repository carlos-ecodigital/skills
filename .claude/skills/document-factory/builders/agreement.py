"""Agreement profile (LOI, NDA, MSA covers).

Public entry point: `build_agreement(...) -> Document`

Thin alias for `generate.profile_agreement`. When M2's
`validate_agreement_inputs` is present (document-factory rebuild milestone
M2), it fires at the top of `profile_agreement` — build_agreement
inherits that build-time rejection of placeholder inputs.
"""
from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

_FACTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _FACTORY not in sys.path:
    sys.path.insert(0, _FACTORY)

from document_factory import profile_agreement as _profile_agreement  # noqa: E402

if TYPE_CHECKING:
    from docx.document import Document


def build_agreement(
    agreement_type: str = "[Agreement Type]",
    subject: str | None = None,
    client: str = "[Counterparty]",
    client_address: str | None = None,
    client_reg_type: str | None = None,
    client_reg_number: str | None = None,
    date_str: str = "",
    version: int = 1,
    formality: str | None = None,
    entity: str = "ag",
    title: str | None = None,
    cover_title: str | None = None,
    reference: str | None = None,
    **kwargs,
) -> "Document":
    """Build an agreement (LOI / NDA / MSA / etc.) with a branded cover.

    Args:
      agreement_type: e.g. "Letter of Intent", "Master Service Agreement".
      subject: Deal description (renders below the title on the cover).
      client: Counterparty legal name.
      client_address: Counterparty registered address.
      client_reg_type: Registration type (e.g. "KvK", "CHE", "CRN").
      client_reg_number: Registration number.
      date_str: Agreement date (e.g. "17 April 2026").
      version: Version number (e.g. 1).
      formality: Override formality detection ("binding" / "non_binding").
        If None (default), inferred from agreement_type.
      entity: DE contracting entity — "ag" or "nl".
      title: Legacy arg; maps to agreement_type if agreement_type is the
        default placeholder.
      cover_title: Override the title text on the cover (rare).
      reference: Reference number (e.g. "DE-LOI-2026-042").
      **kwargs: Additional arguments passed to `profile_agreement`.

    Returns: a python-docx `Document` object.

    Raises: `AgreementValidationError` (from M2 validators) if the inputs
      would produce a placeholder-riddled document.
    """
    return _profile_agreement(
        agreement_type=agreement_type,
        subject=subject,
        client=client,
        client_address=client_address,
        client_reg_type=client_reg_type,
        client_reg_number=client_reg_number,
        date_str=date_str,
        version=version,
        formality=formality,
        entity=entity,
        title=title,
        cover_title=cover_title,
        reference=reference,
        **kwargs,
    )
