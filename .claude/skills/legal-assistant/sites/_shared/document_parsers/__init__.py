"""Document parsers for sites-stream enrichment.

Exports base classes + exception hierarchy. Specialised parsers live as
sibling modules (ato.py, kadaster.py, kvk.py, etc.) and register against
the registry supporting_documents entries via their ``doc_type`` attribute.
"""

from .base import (  # noqa: F401
    CorruptDocError,
    DocumentParser,
    FieldNotFoundError,
    ParseResult,
    ParserError,
    SchemaMismatchError,
    UnreadableScanError,
)
