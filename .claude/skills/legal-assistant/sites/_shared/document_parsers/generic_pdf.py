"""Generic PDF parser — last-resort fallback.

Extracts raw text; no field-specific population. Used when:
  - No specialised parser matches the uploaded doc type.
  - A specialised parser is still v0.1 / not yet built.

Raises ``UnreadableScanError`` if the PDF has no extractable text layer
(image-only scan) so the SAL can route the doc for OCR rather than
silently passing it.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


class GenericPDFParser(DocumentParser):
    doc_type = "generic_pdf"
    parser_version = "0.1"
    populates_fields: List[str] = []   # no field mapping — text only

    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz  # PyMuPDF
        except ImportError as e:
            raise ImportError(
                "generic_pdf parser requires PyMuPDF (fitz). "
                "Install via `pip install pymupdf`."
            ) from e

        try:
            doc = fitz.open(str(self.doc_path))
        except Exception as e:
            raise CorruptDocError(f"cannot open PDF: {e}") from e

        total_text = ""
        for page in doc:
            total_text += page.get_text() or ""

        if len(total_text.strip()) < 50:
            doc.close()
            raise UnreadableScanError(
                f"{self.doc_path.name} has <50 chars extractable text; "
                "likely an image-only scan. OCR required (out of v0.1 scope)."
            )

        warnings: List[str] = []
        page_count = doc.page_count
        if page_count and len(total_text) / page_count < 200:
            warnings.append(
                f"low text density ({len(total_text) // page_count} chars/page); "
                "may be partial scan"
            )

        doc.close()

        fields: Dict[str, Any] = {
            "_raw_text": total_text,
            "_page_count": page_count,
        }
        # Low confidence — we extracted nothing field-specific.
        return fields, warnings, 0.5
