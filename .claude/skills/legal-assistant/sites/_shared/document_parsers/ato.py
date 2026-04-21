"""ATO (Aansluit- en Transportovereenkomst) parser.

Extracts fields from Dutch DSO connection/transport agreements:
  - B1_dso              : Liander / Stedin / Enexis / Westland Infra / Other
  - B2_ean_code         : 18-digit EAN (871...)
  - B3_ato_reference    : internal ATO reference number
  - B4_total_connection_mva : contracted connection capacity (MVA)
  - B5_total_import_mw  : import capacity (MW)
  - B6_total_export_mw  : export capacity (MW)

Heuristics:
  - Dutch decimal comma (``16,5``) converted to float ``16.5``.
  - Multiple MVA mentions: the largest is taken as the total connection
    capacity (sub-connections tend to be smaller than the umbrella value).
  - DSO detection is case-insensitive and matches any whole-word occurrence.

Any unexpected failure is wrapped by the base class as CorruptDocError.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


def _nl_to_float(raw: str) -> Optional[float]:
    """Convert a Dutch-formatted number string to float.

    Handles ``16,5`` → 16.5 and ``1.234,56`` → 1234.56 and ``16.5`` → 16.5.
    """
    s = raw.strip()
    if not s:
        return None
    # If the string contains both . and , assume . is thousands and , is decimal.
    if "." in s and "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        # Single comma -> decimal separator.
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


class ATOParser(DocumentParser):
    doc_type = "ato_document"
    parser_version = "0.1"
    populates_fields = [
        "B1_dso",
        "B2_ean_code",
        "B3_ato_reference",
        "B4_total_connection_mva",
        "B5_total_import_mw",
        "B6_total_export_mw",
    ]

    # --- DSO recognition --------------------------------------------------
    # Keys correspond to registry ``B1_dso.options`` exactly.
    DSO_PATTERNS = {
        "Enexis": re.compile(r"\bEnexis(?:\s+Netbeheer)?\b", re.IGNORECASE),
        "Liander": re.compile(r"\bLiander\b", re.IGNORECASE),
        "Stedin": re.compile(r"\bStedin\b", re.IGNORECASE),
        "Westland Infra": re.compile(r"\bWestland\s+Infra\b", re.IGNORECASE),
    }

    # NL EAN-code: 18 digits starting with 871.
    EAN_RE = re.compile(r"\b(871\d{15})\b")

    # ATO reference: permissive; "ATO" optionally spaced/hyphened then digits.
    ATO_REF_RE = re.compile(
        r"\b(ATO[\s\-:]*\d{6,12})\b",
        re.IGNORECASE,
    )

    # Capacity patterns — numbers allow Dutch decimal comma.
    _NUM = r"(\d{1,4}(?:[.,]\d+)?)"
    MVA_RE = re.compile(rf"{_NUM}\s*MVA\b", re.IGNORECASE)
    MW_IMPORT_RE = re.compile(
        rf"(?:import|afname|invoer)[^0-9\n]{{0,40}}{_NUM}\s*MW\b",
        re.IGNORECASE,
    )
    MW_EXPORT_RE = re.compile(
        rf"(?:export|invoeding|teruglevering|uitvoer)[^0-9\n]{{0,40}}{_NUM}\s*MW\b",
        re.IGNORECASE,
    )

    # ------------------------------------------------------------------
    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz  # PyMuPDF
        except ImportError as e:  # pragma: no cover — env sanity
            raise ImportError(
                "ato parser requires PyMuPDF (fitz). "
                "Install via `pip install pymupdf`."
            ) from e

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
                f"{self.doc_path.name} has <50 chars extractable text; "
                "likely an image-only scan. OCR required (out of v0.1 scope)."
            )

        fields: Dict[str, Any] = {}
        warnings: List[str] = []

        # --- DSO -----------------------------------------------------
        dso_found = None
        for name, pat in self.DSO_PATTERNS.items():
            if pat.search(text):
                dso_found = name
                break
        if dso_found:
            fields["B1_dso"] = dso_found
        else:
            warnings.append("B1_dso: no recognized DSO name found")

        # --- EAN -----------------------------------------------------
        ean_match = self.EAN_RE.search(text)
        if ean_match:
            fields["B2_ean_code"] = ean_match.group(1)
        else:
            warnings.append("B2_ean_code: no 18-digit EAN starting 871 found")

        # --- ATO reference -------------------------------------------
        ato_match = self.ATO_REF_RE.search(text)
        if ato_match:
            # Normalise internal whitespace/hyphens for cleanliness.
            raw = ato_match.group(1)
            fields["B3_ato_reference"] = re.sub(r"\s+", "", raw).upper()
        else:
            warnings.append("B3_ato_reference: no ATO reference found")

        # --- MVA (take the largest number) ---------------------------
        mva_values: List[float] = []
        for m in self.MVA_RE.finditer(text):
            v = _nl_to_float(m.group(1))
            if v is not None:
                mva_values.append(v)
        if mva_values:
            fields["B4_total_connection_mva"] = max(mva_values)
            if len(mva_values) > 1:
                warnings.append(
                    f"B4_total_connection_mva: {len(mva_values)} MVA mentions "
                    f"found; took the largest ({max(mva_values)})"
                )
        else:
            warnings.append("B4_total_connection_mva: no MVA value found")

        # --- MW import / export -------------------------------------
        imp = self.MW_IMPORT_RE.search(text)
        if imp:
            v = _nl_to_float(imp.group(1))
            if v is not None:
                fields["B5_total_import_mw"] = v
            else:
                warnings.append("B5_total_import_mw: unparseable number")
        else:
            warnings.append("B5_total_import_mw: no import MW value found")

        exp = self.MW_EXPORT_RE.search(text)
        if exp:
            v = _nl_to_float(exp.group(1))
            if v is not None:
                fields["B6_total_export_mw"] = v
            else:
                warnings.append("B6_total_export_mw: unparseable number")
        else:
            warnings.append("B6_total_export_mw: no export MW value found")

        confidence = len(fields) / len(self.populates_fields)
        return fields, warnings, confidence
