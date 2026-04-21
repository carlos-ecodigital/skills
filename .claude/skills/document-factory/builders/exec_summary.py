"""Two-page executive summary profile.

Public entry point: `build_exec_summary(title, date_str, entity, ...) -> Document`
"""
from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

_FACTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _FACTORY not in sys.path:
    sys.path.insert(0, _FACTORY)

from generate import profile_exec_summary as _profile_exec_summary  # noqa: E402

if TYPE_CHECKING:
    from docx.document import Document


def build_exec_summary(
    title: str = "[Executive Summary]",
    date_str: str = "",
    entity: str = "ag",
    **kwargs,
) -> "Document":
    """Build a 2-page standalone executive summary.

    Args:
      title: Document title (rendered on the cover).
      date_str: Document date.
      entity: DE contracting entity — "ag" or "nl".
      **kwargs: Additional arguments passed to `profile_exec_summary`.

    Returns: a python-docx `Document` object.
    """
    return _profile_exec_summary(
        title=title, date_str=date_str, entity=entity, **kwargs,
    )
