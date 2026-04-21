"""Financier consent-letter parser.

Consent letters from a land financier (typically a bank, Rabobank
agricultural-lender arm, or private mortgage holder) confirming that
they do not object to the DEC development on land they hold a charge
over. Registry key: ``financier_consent``. Registry ``verifies`` is
empty; this parser populates narrative meta-fields.

Populated meta-fields:
  - ``_consent_date``            : date of the letter (ISO ``YYYY-MM-DD``).
  - ``_financier_name``          : bank / lender name.
  - ``_financier_kvk``           : 8-digit KvK number (banks have one).
  - ``_encumbrance_reference``   : mortgage / hypotheek reference
                                   (e.g. ``Hypotheek nr. 12345``).
  - ``_signed``                  : bool — signature marker detected?

Any unexpected failure is wrapped by the base class as ``CorruptDocError``.
"""

from __future__ import annotations

import re
from datetime import date
from typing import Any, Dict, List, Optional, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


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
        return date(int(year), int(month), int(day)).isoformat()
    except ValueError:
        return None


class FinancierConsentParser(DocumentParser):
    """Parser for NL-language financier / lender consent letters."""

    doc_type = "financier_consent"
    parser_version = "0.1"
    populates_fields = [
        "_consent_date",
        "_financier_name",
        "_financier_kvk",
        "_encumbrance_reference",
        "_signed",
    ]

    DATE_NUM_RE = re.compile(r"\b(\d{1,2})[-/\.](\d{1,2})[-/\.](\d{4})\b")
    DATE_WORD_RE = re.compile(
        r"\b(\d{1,2})\s+("
        + "|".join(_NL_MONTHS.keys())
        + r")\s+(\d{4})\b",
        re.IGNORECASE,
    )

    # Signature markers — same set as landowner.
    SIGNATURE_MARKERS = ["Handtekening", "Getekend", "w.g.", "Ondertekend"]
    SIGNATURE_RE = re.compile(
        r"(?:" + "|".join(re.escape(m) for m in SIGNATURE_MARKERS) + r")",
        re.IGNORECASE,
    )

    # KvK — prefer labelled; 8 digits.
    KVK_LABELED_RE = re.compile(
        r"(?:KvK(?:[\s\-\.:nummer]*)?|Kamer\s+van\s+Koophandel[\s\-\.:nummer]*)"
        r"(\d{8})\b",
        re.IGNORECASE,
    )

    # Financier name — labelled forms first, then fallback to known NL banks.
    FINANCIER_LABELED_RE = re.compile(
        r"(?:financier|kredietgever|hypotheekhouder|bank|lender)"
        r"[\s,:]+"
        r"(?P<name>[A-Z][\w\.\-\' &]{2,80}?(?:B\.V\.|N\.V\.|Bank|Groep)?)"
        r"(?=[,\n]|\s+(?:gevestigd|verklaart|verklaar|hierbij|KvK))",
        re.IGNORECASE,
    )
    # Known bank / lender substrings — fallback ranking when no label.
    KNOWN_FINANCIERS = [
        r"Rabobank",
        r"ABN\s+AMRO",
        r"ING\s+Bank",
        r"ING\b",
        r"Triodos\s+Bank",
        r"Triodos",
        r"de\s+Volksbank",
        r"Knab",
        r"Bunq",
        r"BNG\s+Bank",
        r"NWB\s+Bank",
    ]
    KNOWN_FINANCIER_RE = re.compile(
        r"\b(" + "|".join(KNOWN_FINANCIERS) + r")\b",
        re.IGNORECASE,
    )

    # Encumbrance reference: "hypotheek(akte)? nr./nummer/kenmerk ...",
    # "Hypothecaire inschrijving <digits>", etc.
    ENCUMBRANCE_RE = re.compile(
        r"(?:hypotheek(?:akte)?|hypothecaire\s+inschrijving|zekerheidsrecht|"
        r"mortgage|encumbrance)"
        r"[\s\-:,]*"
        r"(?:nr\.?|nummer|kenmerk|ref\.?|reference)?"
        r"[\s\-:,]*"
        r"(?P<ref>[A-Z0-9][A-Z0-9\-/\.]{3,40})",
        re.IGNORECASE,
    )

    # ------------------------------------------------------------------
    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz  # PyMuPDF
        except ImportError as e:  # pragma: no cover — env sanity
            raise ImportError(
                "financier_consent parser requires PyMuPDF (fitz). "
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
            "financier_consent: registry `verifies` is empty; parser "
            "populates narrative meta-fields (_financier_*, _encumbrance_*, "
            "_consent_date) rather than registry field IDs"
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

        # --- financier name -------------------------------------------
        # Order: known NL banks first (unambiguous proper nouns), then
        # labelled fallback. Label-first is unsafe because generic labels
        # like "bank" / "financier" appear in copy ("Namens ABN AMRO Bank
        # bevestigen wij...") and would capture the following text as the
        # name.
        fin_name: Optional[str] = None
        known_m = self.KNOWN_FINANCIER_RE.search(text)
        if known_m:
            fin_name = re.sub(r"\s+", " ", known_m.group(1).strip())
        if fin_name is None:
            lab_m = self.FINANCIER_LABELED_RE.search(text)
            if lab_m:
                fin_name = re.sub(
                    r"\s+", " ", lab_m.group("name").strip().rstrip(",;:")
                )
        if fin_name:
            fields["_financier_name"] = fin_name
        else:
            warnings.append(
                "_financier_name: no labelled financier and no known "
                "NL bank / lender string matched"
            )

        # --- KvK ------------------------------------------------------
        kvk_m = self.KVK_LABELED_RE.search(text)
        if kvk_m:
            fields["_financier_kvk"] = kvk_m.group(1)
        else:
            warnings.append("_financier_kvk: no labelled KvK number found")

        # --- encumbrance reference ------------------------------------
        enc_m = self.ENCUMBRANCE_RE.search(text)
        if enc_m:
            raw = enc_m.group("ref").strip().rstrip(",;:.")
            fields["_encumbrance_reference"] = raw
        else:
            warnings.append(
                "_encumbrance_reference: no hypotheek / encumbrance "
                "reference found"
            )

        # --- signed ---------------------------------------------------
        if self.SIGNATURE_RE.search(text):
            fields["_signed"] = True
        else:
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
                    "/ w.g. / Ondertekend) found"
                )

        confidence = len(fields) / len(self.populates_fields)
        return fields, warnings, confidence
