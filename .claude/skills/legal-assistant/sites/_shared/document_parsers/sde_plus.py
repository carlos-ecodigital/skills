"""SDE++ (Stimulering Duurzame Energieproductie en Klimaattransitie) parser.

Parses RVO grant (beschikking) letters issued under the SDE++ scheme.
The field-registry does NOT yet define a ``sde_plus_plus`` entry under
``supporting_documents`` — this parser uses that key as a placeholder and
populates meta-fields (``_sde_*``) rather than registry IDs. A warning is
emitted so the SAL surfaces the gap for registry owners.

Extracted fields:
  - _sde_reference      : grant reference (SDE++...)
  - _sde_category       : subsidy category / technology (free text, best-effort)
  - _sde_awarded_eur    : maximum subsidy amount in euro (float)
  - _sde_decision_date  : date of the beschikking (ISO YYYY-MM-DD)
  - _sde_duration_years : subsidy contract duration in years (int)

The parser is lenient — RVO letter layouts vary across years. Any single
missing field lowers ``confidence`` proportionally, rather than raising.
"""

from __future__ import annotations

import re
from datetime import date
from typing import Any, Dict, List, Optional, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


# Dutch month-name → numeric month.
_NL_MONTHS = {
    "januari": 1, "februari": 2, "maart": 3, "april": 4, "mei": 5,
    "juni": 6, "juli": 7, "augustus": 8, "september": 9, "oktober": 10,
    "november": 11, "december": 12,
}


def _parse_nl_amount(raw: str) -> Optional[float]:
    """Parse Dutch euro amount: '1.234.567,89' -> 1234567.89.

    Also accepts plain '1234567.89' and '1234567,89'.
    """
    s = raw.strip().replace("\u00a0", "").replace(" ", "")
    if not s:
        return None
    if "." in s and "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def _parse_nl_date(day: str, month_name: str, year: str) -> Optional[str]:
    mnum = _NL_MONTHS.get(month_name.lower())
    if not mnum:
        return None
    try:
        return date(int(year), mnum, int(day)).isoformat()
    except ValueError:
        return None


class SDEPlusParser(DocumentParser):
    doc_type = "sde_plus_plus"       # placeholder — not yet in registry
    parser_version = "0.1"
    populates_fields = [
        "_sde_reference",
        "_sde_category",
        "_sde_awarded_eur",
        "_sde_decision_date",
        "_sde_duration_years",
    ]

    # Reference pattern: "SDE++ 2023-001234" / "SDE+ kenmerk 1234567" /
    # "SDE++ nr. 1234567" etc. Capture the whole token.
    REF_RE = re.compile(
        r"\b(SDE\+{1,2})(?:[\s\-:]*(?:nr\.?|nummer|kenmerk|ref\.?)?[\s\-:]*)"
        r"(\d{4}[\s\-]?\d{3,8}|\d{6,12})\b",
        re.IGNORECASE,
    )

    # Category: explicit "categorie <value>" label, capture until newline or period.
    CATEGORY_RE = re.compile(
        r"(?:categorie|technologie|technology)[\s:]+([^\n\.]{3,120})",
        re.IGNORECASE,
    )

    # Awarded amount (maximum subsidy). Match "maximaal(e) (subsidie) ... EUR X"
    # or "subsidie .. € X". X allows Dutch thousand-separator + decimal comma.
    AMOUNT_RE = re.compile(
        r"(?:maximale?\s+subsidie|subsidie(?:bedrag)?|toegekend(?:e)?\s+subsidie|"
        r"maximaal\s+te\s+ontvangen(?:\s+subsidie)?)"
        r"[^0-9€]{0,60}"
        r"(?:€|EUR)\s*([\d\.\u00a0 ]{1,15}(?:,\d{2})?)",
        re.IGNORECASE,
    )

    # Fallback amount pattern — any € amount ≥ 6 digits.
    AMOUNT_FALLBACK_RE = re.compile(
        r"(?:€|EUR)\s*(\d{1,3}(?:\.\d{3}){1,4}(?:,\d{2})?)",
    )

    # Decision date: "Datum besluit: 12 maart 2026" / "Beschikt op 1 april 2026"
    DATE_RE = re.compile(
        r"(?:datum\s+besluit|beschikkingsdatum|beschikt\s+op|datum)"
        r"[\s:]+"
        r"(\d{1,2})\s+("
        + "|".join(_NL_MONTHS.keys())
        + r")\s+(\d{4})",
        re.IGNORECASE,
    )

    # Duration: "subsidieduur 15 jaar" / "looptijd 12 jaar" / "gedurende 15 jaar"
    DURATION_RE = re.compile(
        r"(?:subsidieduur|looptijd|gedurende|duur)[\s:]+(\d{1,2})\s*jaar",
        re.IGNORECASE,
    )

    # ------------------------------------------------------------------
    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz  # PyMuPDF
        except ImportError as e:  # pragma: no cover — env sanity
            raise ImportError(
                "sde_plus parser requires PyMuPDF (fitz). "
                "Install via `pip install pymupdf`."
            ) from e

        try:
            doc = fitz.open(str(self.doc_path))
        except Exception as e:
            raise CorruptDocError(f"cannot open PDF: {e}") from e

        text = ""
        page_count = doc.page_count
        for page in doc:
            text += page.get_text() or ""
        doc.close()

        if len(text.strip()) < 50:
            raise UnreadableScanError(
                f"{self.doc_path.name} has <50 chars extractable text; "
                "likely an image-only scan. OCR required (out of v0.1 scope)."
            )

        fields: Dict[str, Any] = {}
        warnings: List[str] = [
            "sde_plus_plus: no supporting_documents entry in field-registry; "
            "parser populates meta-fields (_sde_*) as placeholders"
        ]

        # Low-density warning (useful for partial scans).
        if page_count and len(text) / page_count < 200:
            warnings.append(
                f"low text density ({len(text) // page_count} chars/page); "
                "may be partial scan"
            )

        # --- reference ------------------------------------------------
        ref_m = self.REF_RE.search(text)
        if ref_m:
            scheme = ref_m.group(1).upper()
            number = re.sub(r"\s+", "", ref_m.group(2))
            fields["_sde_reference"] = f"{scheme} {number}"
        else:
            warnings.append("_sde_reference: no SDE+/SDE++ reference found")

        # --- category -------------------------------------------------
        cat_m = self.CATEGORY_RE.search(text)
        if cat_m:
            fields["_sde_category"] = cat_m.group(1).strip().rstrip(",;:")
        else:
            warnings.append("_sde_category: no category label found")

        # --- awarded amount ------------------------------------------
        amt_m = self.AMOUNT_RE.search(text)
        amount_val: Optional[float] = None
        if amt_m:
            amount_val = _parse_nl_amount(amt_m.group(1))
        if amount_val is None:
            # Fallback: take the largest € amount in the doc.
            candidates: List[float] = []
            for m in self.AMOUNT_FALLBACK_RE.finditer(text):
                v = _parse_nl_amount(m.group(1))
                if v is not None:
                    candidates.append(v)
            if candidates:
                amount_val = max(candidates)
                warnings.append(
                    "_sde_awarded_eur: label not found; took the largest € "
                    f"amount in the document ({amount_val})"
                )
        if amount_val is not None:
            fields["_sde_awarded_eur"] = amount_val
        else:
            warnings.append("_sde_awarded_eur: no euro amount found")

        # --- decision date --------------------------------------------
        date_m = self.DATE_RE.search(text)
        if date_m:
            iso = _parse_nl_date(date_m.group(1), date_m.group(2), date_m.group(3))
            if iso:
                fields["_sde_decision_date"] = iso
            else:
                warnings.append("_sde_decision_date: unparseable date tokens")
        else:
            warnings.append("_sde_decision_date: no decision date found")

        # --- duration -------------------------------------------------
        dur_m = self.DURATION_RE.search(text)
        if dur_m:
            try:
                fields["_sde_duration_years"] = int(dur_m.group(1))
            except ValueError:
                warnings.append("_sde_duration_years: unparseable integer")
        else:
            warnings.append("_sde_duration_years: no subsidy duration found")

        confidence = len(fields) / len(self.populates_fields)
        return fields, warnings, confidence
