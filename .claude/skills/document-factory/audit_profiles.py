"""Per-profile structural audits.

Wraps the generic `audit_document()` with profile-aware assertions that
catch semantic defects the generic audit cannot see. Returns the
combined violation list; an empty list means pass.

Addresses Layer 2 of the four-layer test strategy from the rebuild plan.
"""
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from document_factory import audit_document, _fix_zoom

if TYPE_CHECKING:  # avoid runtime import cycle
    from docx.document import Document


# Tokens that indicate the caller did not supply real values — these
# should never survive to a finished agreement output. `[DE-AGR-YYYY-NNN]`
# is an acceptable draft placeholder for the reference field and is
# deliberately not included here (handled by a separate rule later).
_UNACCEPTABLE_COVER_PLACEHOLDERS = (
    "[Counterparty]",
    "[Client]",
    "[Address]",
    "[Agreement Type]",
)

# Party-block label signatures on a cover page. If any of these appear,
# the cover is carrying parties — and the body must not duplicate them
# via a "THE UNDERSIGNED" heading (rule R-24).
_COVER_PARTY_LABELS = ("Between:", "By and between:", "And:")

_UNDERSIGNED_RE = re.compile(r"^\s*THE\s+UNDERSIGNED\b", re.IGNORECASE)


def _collect_paragraph_texts(doc: "Document") -> list[str]:
    """Flat list of paragraph texts, in document order."""
    return [p.text for p in doc.paragraphs]


def _cover_has_parties(texts: list[str]) -> bool:
    """Heuristic: a cover carries parties if any paragraph text contains
    one of the party-block labels emitted by `add_cover()`.

    False positives are possible only if a body paragraph literally
    starts "Between:" or similar — acceptable for now; the rules the
    heuristic drives only fire when there's an actual UNDERSIGNED block
    in the body, so a false positive in isolation is harmless.
    """
    return any(
        any(label in t for label in _COVER_PARTY_LABELS) for t in texts
    )


def audit_agreement(doc: "Document") -> list[str]:
    """Structural + content audit for the `agreement` profile.

    Runs the generic `audit_document()` first, then adds:
      - cover placeholders: no `[Address]`, `[Counterparty]`, `[Client]`,
        `[Agreement Type]` anywhere in the document.
      - R-24: if the cover has party blocks, the body must not contain a
        heading matching `/^\\s*THE\\s+UNDERSIGNED\\b/i` (party
        duplication).

    Idempotently applies `_fix_zoom()` first — the generic audit is
    strict about a missing `w:percent` attribute on `w:zoom`, which
    python-docx doesn't emit by default. In production, `save_doc()`
    calls `_fix_zoom()` before serialization; unsaved in-memory docs
    (e.g. inside tests) would otherwise trip the audit for a reason
    unrelated to agreement semantics. Calling it here makes the audit
    self-sufficient: callers don't need to know about the quirk.
    """
    _fix_zoom(doc)
    violations = list(audit_document(doc))

    texts = _collect_paragraph_texts(doc)

    # Cover-placeholder check — matches anywhere in any paragraph.
    # We do not scope to "cover only" because these tokens should never
    # appear anywhere in a production agreement.
    for ph in _UNACCEPTABLE_COVER_PLACEHOLDERS:
        if any(ph in t for t in texts):
            violations.append(
                f"agreement: placeholder token '{ph}' present in document "
                f"(unfilled input)."
            )

    # R-24: cover-vs-body party duplication
    if _cover_has_parties(texts):
        for t in texts:
            if _UNDERSIGNED_RE.match(t):
                violations.append(
                    "agreement: R-24 — cover carries party blocks but body "
                    "contains a 'THE UNDERSIGNED' heading. Remove the body "
                    "block; the cover is already the declaration of parties."
                )
                break

    return violations
