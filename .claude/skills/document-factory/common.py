"""Public API for document-factory.

This module is the stable contract that other skills import against.
Underlying implementation in `document_factory.py` may refactor; the surface
re-exported here is preserved across reorganisations.

Import from here, not from `generate`:

    from common import Party, add_cover, COBALT, md_to_docx, save_doc

Underscore-prefixed symbols (_SP, _fix_zoom, _detect_formality) are
exposed for now to support downstream callers that depend on them
(tools/visual_qa.py, legal-assistant). They remain semi-private; treat
them as unstable and open an issue before adding new dependents.
"""
from __future__ import annotations

# Party model + cover rendering
from document_factory import Party, add_cover

# Brand color constants — single source of truth
from document_factory import COBALT, SLATE, SLATE_800, SLATE_900, WHITE

# Spacing + entity dicts (shared primitives)
from document_factory import _SP, DE_ENTITIES, ENTITY_FOOTERS

# Header/footer primitives used by legal-assistant for body-page branding
from document_factory import (
    setup_first_page_header,
    setup_cont_header,
    setup_first_footer,
    setup_cont_footer,
)

# Rendering + audit + save
from document_factory import md_to_docx, audit_document, save_doc

# PDF conversion (primary: Word; fallback: LibreOffice handled inside)
from document_factory import docx_to_pdf

# Formality auto-detection (semi-private; used by legal-assistant)
from document_factory import _detect_formality

# Zoom element fix — semi-private, retained for tools/visual_qa.py
from document_factory import _fix_zoom

# M2: build-time validators + per-profile structural audits
from validators import (
    AgreementValidationError,
    validate_agreement_inputs,
)
from audit_profiles import audit_agreement

# M3: Pipeline B preserving rebrand
from rebrand import RebrandSpec, rebrand

# M5: routing dispatcher + deprecation policy
from dispatcher import build, AGREEMENT_PROFILES

__all__ = [
    # Stable surface
    "Party",
    "add_cover",
    "COBALT",
    "SLATE",
    "SLATE_800",
    "SLATE_900",
    "WHITE",
    "DE_ENTITIES",
    "ENTITY_FOOTERS",
    "setup_first_page_header",
    "setup_cont_header",
    "setup_first_footer",
    "setup_cont_footer",
    "md_to_docx",
    "audit_document",
    "save_doc",
    "docx_to_pdf",
    # M2 (build-time enforcement + per-profile audit)
    "AgreementValidationError",
    "validate_agreement_inputs",
    "audit_agreement",
    # M3 (Pipeline B — preserving rebrand)
    "RebrandSpec",
    "rebrand",
    # M5 (routing dispatcher + Pipeline C deprecation for agreements)
    "build",
    "AGREEMENT_PROFILES",
    # Semi-private (retained for compatibility, likely to stabilise later)
    "_SP",
    "_detect_formality",
    "_fix_zoom",
]
