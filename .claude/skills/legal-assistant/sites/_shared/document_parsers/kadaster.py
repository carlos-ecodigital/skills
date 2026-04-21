"""Kadaster (Dutch land registry) extract parser.

Populates registry fields:
  - D1_kadaster_parcels : list[str] of parcel references
                          (e.g., ["Horst sectie A nummer 1234",
                          "Grubbenvorst sectie B nummer 567"])
  - D2_title_type       : "Eigendom" | "Erfpacht" | "Recht van opstal"
                          (bare tokens; registry v1.1 uses slash-combined
                          bilingual values — normalisation layer needed
                          downstream, flagged to registry owner)
  - D3_encumbrances     : True if any hypotheek/beslag/kwalitatieve
                          verplichting detected, False otherwise.
                          (Registry D3 enumerates
                          "None / Geen" vs "Mortgage / Hypotheek" — for
                          v0.1 we return bool; downstream maps to the
                          enum.)
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


class KadasterParser(DocumentParser):
    doc_type = "kadaster_uittreksel"
    parser_version = "0.1"
    populates_fields = ["D1_kadaster_parcels", "D2_title_type", "D3_encumbrances"]

    # Parcel pattern: typical Kadaster format is
    # "gemeente Horst aan de Maas, sectie A, nummer 1234".
    # We tolerate variations: "sect. A nr. 1234", "sectie B nummer 567".
    PARCEL_RE = re.compile(
        r"(?:gemeente\s+)?([A-Z][a-zA-Z\u00C0-\u017F\s-]{1,40}?)"
        r"[,\s]+"
        r"(?:sectie|sect\.)\s+([A-Z])"
        r"[,\s]+"
        r"(?:nummer|nr\.?|perceel)\s+(\d{1,6})",
        re.IGNORECASE,
    )

    # Title-type priority: if "Recht van opstal" present → return it.
    # Else "Erfpacht". Else "Eigendom" (default — every parcel has Eigendom
    # recorded, but specific rights trump when explicitly granted).
    TITLE_PRIORITY = (
        ("Recht van opstal", re.compile(r"\brecht\s+van\s+opstal\b", re.IGNORECASE)),
        ("Erfpacht", re.compile(r"\berfpacht\b", re.IGNORECASE)),
        ("Eigendom", re.compile(r"\beigendom\b", re.IGNORECASE)),
    )

    # Encumbrance markers — any match → True
    ENCUMBRANCE_RES = [
        re.compile(r"\bhypotheek\b", re.IGNORECASE),
        re.compile(r"\bbeslag\b", re.IGNORECASE),
        re.compile(r"\bkwalitatieve\s+verplichting\b", re.IGNORECASE),
        re.compile(r"\bbewaring\b", re.IGNORECASE),  # beslag-variant
    ]

    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz
        except ImportError as e:
            raise ImportError("kadaster parser requires PyMuPDF") from e
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

        # --- Parcels ---
        parcels: List[str] = []
        for m in self.PARCEL_RE.finditer(text):
            municipality = re.sub(r"\s+", " ", m.group(1)).strip().rstrip(",")
            sectie = m.group(2).upper()
            nummer = m.group(3)
            parcels.append(f"{municipality} sectie {sectie} nummer {nummer}")
        if parcels:
            # Dedupe preserving order
            seen: set = set()
            dedup: List[str] = []
            for p in parcels:
                if p not in seen:
                    seen.add(p)
                    dedup.append(p)
            fields["D1_kadaster_parcels"] = dedup
        else:
            warnings.append(
                "D1_kadaster_parcels: no parcel references matched; "
                "PDF may use non-standard Kadaster format"
            )

        # --- Title type ---
        for title_token, pat in self.TITLE_PRIORITY:
            if pat.search(text):
                fields["D2_title_type"] = title_token
                break
        else:
            warnings.append("D2_title_type: no recognised title type")

        # --- Encumbrances ---
        has_encumbrance = any(pat.search(text) for pat in self.ENCUMBRANCE_RES)
        fields["D3_encumbrances"] = has_encumbrance
        if has_encumbrance:
            # Surface which keyword matched so reviewers can inspect
            matched = [p.pattern for p in self.ENCUMBRANCE_RES if p.search(text)]
            warnings.append(
                f"D3_encumbrances: detected marker(s): {matched}; "
                "legal review required"
            )

        confidence = len([k for k in fields if not k.startswith("_")]) / \
                     len(self.populates_fields)
        return fields, warnings, confidence
