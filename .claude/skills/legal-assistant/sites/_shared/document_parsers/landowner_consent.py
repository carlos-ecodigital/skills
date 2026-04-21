"""Landowner consent-letter parser.

Consent letters are short NL-language documents where a third-party
landowner confirms their awareness + non-objection to a DEC development
on their land. The parser extracts narrative meta-fields rather than
registry IDs (registry ``landowner_consent.verifies`` is empty).

Populated meta-fields:
  - ``_consent_date``     : date of the letter (ISO ``YYYY-MM-DD``).
  - ``_landowner_name``   : natural-person or company name of the grantor.
  - ``_landowner_kvk``    : 8-digit KvK number (if present — residential
                            landowners may not have one).
  - ``_consent_scope``    : one-line summary of what is being consented
                            to (extracted around the consent keyword).
  - ``_signed``           : bool — did we detect a signature line?

Any unexpected failure is wrapped by the base class as ``CorruptDocError``.
"""

from __future__ import annotations

import re
from datetime import date
from typing import Any, Dict, List, Optional, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


# Dutch month-name -> numeric month.
_NL_MONTHS = {
    "januari": 1, "februari": 2, "maart": 3, "april": 4, "mei": 5,
    "juni": 6, "juli": 7, "augustus": 8, "september": 9, "oktober": 10,
    "november": 11, "december": 12,
}


def _parse_nl_date_words(day: str, month_name: str, year: str) -> Optional[str]:
    mnum = _NL_MONTHS.get(month_name.lower())
    if not mnum:
        return None
    try:
        return date(int(year), mnum, int(day)).isoformat()
    except ValueError:
        return None


def _parse_numeric_date(day: str, month: str, year: str) -> Optional[str]:
    try:
        d = int(day)
        m = int(month)
        y = int(year)
        return date(y, m, d).isoformat()
    except ValueError:
        return None


class LandownerConsentParser(DocumentParser):
    """Parser for NL-language landowner consent letters."""

    doc_type = "landowner_consent"
    parser_version = "0.1"
    populates_fields = [
        "_consent_date",
        "_landowner_name",
        "_landowner_kvk",
        "_consent_scope",
        "_signed",
    ]

    # Numeric date: DD-MM-YYYY / DD/MM/YYYY / DD.MM.YYYY.
    DATE_NUM_RE = re.compile(
        r"\b(\d{1,2})[-/\.](\d{1,2})[-/\.](\d{4})\b"
    )
    # Word-form date: "14 april 2026".
    DATE_WORD_RE = re.compile(
        r"\b(\d{1,2})\s+("
        + "|".join(_NL_MONTHS.keys())
        + r")\s+(\d{4})\b",
        re.IGNORECASE,
    )

    # Consent keywords — keep these Dutch + ensure single match gives us scope.
    CONSENT_KEYWORDS = [
        "hierbij verleen",
        "hierbij verlenen",
        "stem(?:men)? in",
        "maakt? geen bezwaar",
        "maken geen bezwaar",
        "ga(?:at|an)? akkoord",
        "verklaar(?:t|en)?\\s+hierbij",
    ]
    CONSENT_RE = re.compile(
        r"(?P<scope>(?:" + "|".join(CONSENT_KEYWORDS) + r")[^\n\.]{0,240})",
        re.IGNORECASE,
    )

    # Signature markers. Negative lookbehind prevents Getekend/Ondertekend
    # from firing on the standard NL opener Ondergetekende/Ondergetekenden
    # (the undersigned), which would otherwise false-positive every letter.
    SIGNATURE_RE = re.compile(
        r"(?:"
        r"\bHandtekening\b"
        r"|(?<!onder)\bGetekend\b"
        r"|\bw\.g\.\b"
        r"|(?<!onder)\bOndertekend\b"
        r")",
        re.IGNORECASE,
    )

    # KvK: 8-digit number, often labelled "KvK" or "Kamer van Koophandel".
    KVK_LABELED_RE = re.compile(
        r"(?:KvK(?:[\s\-\.:nummer]*)?|Kamer\s+van\s+Koophandel[\s\-\.:nummer]*)"
        r"(\d{8})\b",
        re.IGNORECASE,
    )
    KVK_BARE_RE = re.compile(r"\b(\d{8})\b")

    # Landowner name patterns:
    #   - "Ondergetekende: <name>" / "Ondergetekende, <name>"
    #   - "Naam: <name>"
    #   - "Grondeigenaar: <name>"
    NAME_LABELED_RE = re.compile(
        r"(?:ondergetekende|naam|grondeigenaar|landowner)"
        r"[\s,:]+"
        r"(?P<name>[A-Z][\w\.\-\' ]{2,80}?(?:B\.V\.|N\.V\.|v\.o\.f\.|Holding)?)"
        r"(?=[,\n]|\s+(?:gevestigd|wonende|verklaart|verklaar|hierbij))",
        re.IGNORECASE,
    )

    # ------------------------------------------------------------------
    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz  # PyMuPDF
        except ImportError as e:  # pragma: no cover — env sanity
            raise ImportError(
                "landowner_consent parser requires PyMuPDF (fitz). "
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
            "landowner_consent: registry `verifies` is empty; parser "
            "populates narrative meta-fields (_consent_*, _landowner_*) "
            "rather than registry field IDs"
        ]

        if page_count and len(text) / page_count < 200:
            warnings.append(
                f"low text density ({len(text) // page_count} chars/page); "
                "may be partial scan"
            )

        # --- date -----------------------------------------------------
        iso_date: Optional[str] = None
        word_m = self.DATE_WORD_RE.search(text)
        if word_m:
            iso_date = _parse_nl_date_words(
                word_m.group(1), word_m.group(2), word_m.group(3)
            )
        if iso_date is None:
            num_m = self.DATE_NUM_RE.search(text)
            if num_m:
                iso_date = _parse_numeric_date(
                    num_m.group(1), num_m.group(2), num_m.group(3)
                )
        if iso_date:
            fields["_consent_date"] = iso_date
        else:
            warnings.append("_consent_date: no date found in letter")

        # --- landowner name -------------------------------------------
        name_m = self.NAME_LABELED_RE.search(text)
        if name_m:
            nm = name_m.group("name").strip().rstrip(",;:")
            # Collapse internal whitespace.
            nm = re.sub(r"\s+", " ", nm)
            fields["_landowner_name"] = nm
        else:
            warnings.append("_landowner_name: no labelled name found")

        # --- landowner KvK --------------------------------------------
        kvk_m = self.KVK_LABELED_RE.search(text)
        if kvk_m:
            fields["_landowner_kvk"] = kvk_m.group(1)
        else:
            # A residential landowner often has no KvK — emit a note but
            # don't force a false positive from a BSN / postcode digits.
            warnings.append(
                "_landowner_kvk: no labelled KvK number found (acceptable "
                "for residential landowners)"
            )

        # --- consent scope + signal -----------------------------------
        consent_m = self.CONSENT_RE.search(text)
        if consent_m:
            scope = consent_m.group("scope").strip()
            scope = re.sub(r"\s+", " ", scope)
            # Truncate scope to 240 chars defensively.
            fields["_consent_scope"] = scope[:240]
        else:
            warnings.append(
                "_consent_scope: no consent keyword "
                "(hierbij verleen / stem in / ga akkoord / geen bezwaar) found"
            )

        # --- signed ---------------------------------------------------
        if self.SIGNATURE_RE.search(text):
            fields["_signed"] = True
        else:
            # Fallback — name + date pair near end of document counts as
            # a soft positive signal.
            tail = text[-400:]
            if (self.DATE_NUM_RE.search(tail) or self.DATE_WORD_RE.search(tail)) \
                    and re.search(r"[A-Z][a-z]+\s+[A-Z][a-z]+", tail):
                fields["_signed"] = True
                warnings.append(
                    "_signed: no explicit marker but name+date pair near "
                    "end of document — soft positive"
                )
            else:
                fields["_signed"] = False
                warnings.append(
                    "_signed: no signature marker (Handtekening / Getekend "
                    "/ w.g.) found"
                )

        confidence = len(fields) / len(self.populates_fields)
        return fields, warnings, confidence
