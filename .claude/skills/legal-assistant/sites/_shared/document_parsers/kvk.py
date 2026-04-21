"""KvK (Kamer van Koophandel) uittreksel parser.

Populates registry fields:
  - A1_legal_name         : statutaire naam
  - A2_kvk_number         : 8-digit KvK number
  - A3_registered_address : vestigingsadres (address line)
  - A4_signatory_name     : first bestuurder name (flagged to registry
                            owner as missing from supporting_documents.
                            kvk_uittreksel.verifies[])
  - A6_signing_authority  : "Sole" | "Joint" | "Other" (bare tokens;
                            registry enums are slash-combined bilingual —
                            downstream normalisation layer expected)
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


class KvKParser(DocumentParser):
    doc_type = "kvk_uittreksel"
    parser_version = "0.1"
    populates_fields = [
        "A1_legal_name",
        "A2_kvk_number",
        "A3_registered_address",
        "A4_signatory_name",
        "A6_signing_authority",
    ]

    # KvK number: "KvK-nummer 12345678" or "Handelsregisternummer 12345678"
    KVK_LABELED_RE = re.compile(
        r"(?:KvK[-\s]*nummer|Handelsregisternummer|KVK[-\s]*#?)[:\s]*(\d{8})",
        re.IGNORECASE,
    )
    # Fallback: any bare 8-digit token (use only if labelled match absent)
    KVK_BARE_RE = re.compile(r"\b(\d{8})\b")

    # Statutaire naam — the line immediately after "Statutaire naam" label
    STATUTAIRE_RE = re.compile(
        r"(?:Statutaire\s+naam|Naam\s+rechtspersoon)[:\s]*(?:\n\s*)?([A-Z][^\n]{2,120})",
        re.IGNORECASE,
    )

    # Registered address — after "Vestigingsadres" or "Bezoekadres"
    ADDRESS_RE = re.compile(
        r"(?:Vestigingsadres|Bezoekadres|Statutaire\s+zetel)[:\s]*"
        r"(?:\n\s*)?([A-Z][^\n]{10,150})",
        re.IGNORECASE,
    )

    # Bestuurder — first name after the Bestuurder(s) header
    BESTUURDER_RE = re.compile(
        r"(?:Bestuurder|Directeur)(?:s)?[:\s]*(?:\n\s*)?"
        r"([A-Z][a-zA-Z\u00C0-\u017F\s\.-]{2,80})",
        re.IGNORECASE,
    )

    # Signing authority
    SOLE_AUTH_RE = re.compile(r"Zelfstandig\s+bevoegd", re.IGNORECASE)
    JOINT_AUTH_RE = re.compile(r"Gezamenlijk\s+bevoegd", re.IGNORECASE)

    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz
        except ImportError as e:
            raise ImportError("kvk parser requires PyMuPDF") from e
        try:
            doc = fitz.open(str(self.doc_path))
        except Exception as e:
            raise CorruptDocError(f"cannot open PDF: {e}") from e
        text = ""
        for page in doc:
            text += page.get_text() or ""
        doc.close()
        if len(text.strip()) < 50:
            raise UnreadableScanError(
                f"{self.doc_path.name}: <50 chars extractable text (scan)"
            )

        fields: Dict[str, Any] = {}
        warnings: List[str] = []

        # --- KvK number ---
        m = self.KVK_LABELED_RE.search(text)
        if m:
            fields["A2_kvk_number"] = m.group(1)
        else:
            # Fallback: first bare 8-digit token
            m2 = self.KVK_BARE_RE.search(text)
            if m2:
                fields["A2_kvk_number"] = m2.group(1)
                warnings.append(
                    "A2_kvk_number: labelled match not found; used first "
                    "bare 8-digit token as fallback (may be wrong)"
                )
            else:
                warnings.append("A2_kvk_number: no 8-digit KvK number found")

        # --- Statutaire naam ---
        m = self.STATUTAIRE_RE.search(text)
        if m:
            name = m.group(1).strip().rstrip(",;.")
            fields["A1_legal_name"] = name
        else:
            warnings.append("A1_legal_name: no statutaire naam label")

        # --- Address ---
        m = self.ADDRESS_RE.search(text)
        if m:
            addr = re.sub(r"\s+", " ", m.group(1)).strip()
            fields["A3_registered_address"] = addr
        else:
            warnings.append("A3_registered_address: no vestigingsadres label")

        # --- Signatory (first bestuurder) ---
        m = self.BESTUURDER_RE.search(text)
        if m:
            sig = m.group(1).strip().rstrip(",;")
            # Drop trailing role markers like "namens X"
            sig = re.sub(r"\s+namens\s+.*$", "", sig, flags=re.IGNORECASE)
            fields["A4_signatory_name"] = sig
        # No warning if absent — some KvK uittreksels have no bestuurder block

        # --- Signing authority ---
        has_sole = bool(self.SOLE_AUTH_RE.search(text))
        has_joint = bool(self.JOINT_AUTH_RE.search(text))
        if has_joint:
            fields["A6_signing_authority"] = "Joint"
        elif has_sole:
            fields["A6_signing_authority"] = "Sole"
        else:
            warnings.append(
                "A6_signing_authority: neither 'Zelfstandig bevoegd' nor "
                "'Gezamenlijk bevoegd' found"
            )

        confidence = len(fields) / len(self.populates_fields)
        return fields, warnings, confidence
