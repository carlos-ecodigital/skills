"""Base parser framework — exception hierarchy, ParseResult, DocumentParser.

Phase B5. All specialised parsers extend ``DocumentParser`` and override
``_extract_fields()``. The base class provides SHA-256 hashing,
file-existence checks, and a template method that wraps unexpected
errors as ``CorruptDocError`` for consistent error surfacing to SAL.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Tuple


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class ParserError(Exception):
    """Base exception for parser failures."""


class CorruptDocError(ParserError):
    """Document is unreadable (corrupt PDF, malformed archive)."""


class UnreadableScanError(ParserError):
    """PDF has no extractable text layer (image-only scan). OCR required."""


class SchemaMismatchError(ParserError):
    """Document doesn't match the structure expected by this parser
    (e.g., ATO parser fed a Kadaster extract)."""


class FieldNotFoundError(ParserError):
    """A field the parser is contracted to populate could not be located.
    Surfaced to the SAL rather than silently passing with [TBC]."""


# ---------------------------------------------------------------------------
# ParseResult
# ---------------------------------------------------------------------------

@dataclass
class ParseResult:
    """Typed return value from ``DocumentParser.parse()``."""
    parser_name: str
    parser_version: str
    doc_path: Path
    doc_hash: str
    fields_populated: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
    confidence: float = 1.0          # 0..1 — parser-specific self-assessment

    def to_dict(self) -> dict:
        """Serialisable view for gate-report / audit log."""
        return {
            "parser_name": self.parser_name,
            "parser_version": self.parser_version,
            "doc_path": str(self.doc_path),
            "doc_hash": self.doc_hash,
            "fields_populated": self.fields_populated,
            "warnings": self.warnings,
            "confidence": self.confidence,
        }


# ---------------------------------------------------------------------------
# DocumentParser base class
# ---------------------------------------------------------------------------

class DocumentParser:
    """Template-method base for every specialised parser."""

    #: Registry ``supporting_documents`` key this parser handles.
    doc_type: str = "abstract"
    parser_version: str = "0.1"
    #: Registry field IDs this parser aims to populate.
    populates_fields: List[str] = []

    def __init__(self, doc_path: Path):
        self.doc_path = Path(doc_path)

    def _compute_hash(self) -> str:
        """SHA-256 of the file bytes."""
        h = hashlib.sha256()
        with open(self.doc_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def parse(self) -> ParseResult:
        """Template method. Subclasses override ``_extract_fields``."""
        if not self.doc_path.exists():
            raise FileNotFoundError(self.doc_path)
        doc_hash = self._compute_hash()
        try:
            fields, warnings, confidence = self._extract_fields()
        except (ParserError, FileNotFoundError):
            raise
        except Exception as e:
            # Any unexpected exception is wrapped as CorruptDocError so SAL
            # sees a consistent error class in the gate report.
            raise CorruptDocError(
                f"{self.doc_type} parser hit unexpected error on "
                f"{self.doc_path.name}: {e}"
            ) from e
        return ParseResult(
            parser_name=self.doc_type,
            parser_version=self.parser_version,
            doc_path=self.doc_path,
            doc_hash=doc_hash,
            fields_populated=fields,
            warnings=warnings,
            confidence=confidence,
        )

    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        """Subclass override. Returns ``(fields, warnings, confidence)``."""
        raise NotImplementedError(
            f"{self.__class__.__name__}._extract_fields must be overridden"
        )
