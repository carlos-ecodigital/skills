"""Institutional investor memo profile (10 sections).

Public entry point: `build_investor_memo(client, date_str, version, entity, ...) -> Document`
"""
from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

_FACTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _FACTORY not in sys.path:
    sys.path.insert(0, _FACTORY)

from document_factory import profile_investor_memo as _profile_investor_memo  # noqa: E402

if TYPE_CHECKING:
    from docx.document import Document


def build_investor_memo(
    client: str = "[Investor Name]",
    date_str: str = "",
    version: int = 1,
    entity: str = "ag",
    **kwargs,
) -> "Document":
    """Build an institutional-grade investor memo (10 sections, branded cover).

    Args:
      client: Investor / recipient name (rendered on the cover).
      date_str: Document date.
      version: Version number.
      entity: DE contracting entity — "ag" or "nl".
      **kwargs: Additional arguments passed to `profile_investor_memo`.

    Returns: a python-docx `Document` object.
    """
    return _profile_investor_memo(
        client=client, date_str=date_str, version=version,
        entity=entity, **kwargs,
    )
