"""Bestemmingsplan (Dutch zoning plan) excerpt parser.

Populates registry fields:
  - D4_zoning_designation : the zoning category that applies to the
                            parcel (e.g., "Agrarisch - Glastuinbouw",
                            "Bedrijventerrein").
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


class BestemmingsplanParser(DocumentParser):
    doc_type = "bestemmingsplan_excerpt"
    parser_version = "0.1"
    populates_fields = ["D4_zoning_designation"]

    #: Canonical zoning categories commonly found on greenhouse / industrial
    #: sites, with priority order (most specific first). Each category maps
    #: to a list of regex patterns; any match → category wins.
    ZONING_CATEGORIES: List[Tuple[str, List[re.Pattern]]] = [
        ("Agrarisch - Glastuinbouw", [
            re.compile(r"Agrarisch.{0,30}Glastuinbouw", re.IGNORECASE | re.DOTALL),
            re.compile(r"Glastuinbouwgebied", re.IGNORECASE),
            re.compile(r"\bAG\s*-\s*GT\b", re.IGNORECASE),
        ]),
        ("Bedrijventerrein", [
            re.compile(r"Bedrijventerrein", re.IGNORECASE),
            re.compile(r"Bedrijfsdoeleinden", re.IGNORECASE),
        ]),
        ("Agrarisch", [
            re.compile(r"\bAgrarisch\b", re.IGNORECASE),
        ]),
        ("Gemengd", [
            re.compile(r"\bGemengd\b", re.IGNORECASE),
        ]),
        ("Wonen", [
            re.compile(r"\bWonen\b", re.IGNORECASE),
        ]),
        ("Groen", [
            re.compile(r"\bGroen\b", re.IGNORECASE),
        ]),
    ]

    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz
        except ImportError as e:
            raise ImportError("bestemmingsplan parser requires PyMuPDF") from e
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

        for category, patterns in self.ZONING_CATEGORIES:
            if any(p.search(text) for p in patterns):
                fields["D4_zoning_designation"] = category
                break
        else:
            warnings.append(
                "D4_zoning_designation: no recognised zoning category "
                "found; document may use municipality-specific terms"
            )

        confidence = 1.0 if "D4_zoning_designation" in fields else 0.0
        return fields, warnings, confidence
