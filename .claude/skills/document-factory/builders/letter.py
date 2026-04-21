"""DIN 5008 letter profile.

Public entry point: `build_letter(title, date_str, entity, **kw) -> Document`

Thin alias for `generate.profile_letter`. The indirection exists so the
public API surface is stable — a future refactor can move the
implementation into this module without changing callers.
"""
from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

# Make same-dir imports work from any cwd.
_FACTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _FACTORY not in sys.path:
    sys.path.insert(0, _FACTORY)

from generate import profile_letter as _profile_letter  # noqa: E402

if TYPE_CHECKING:
    from docx.document import Document


def build_letter(
    title: str = "",
    date_str: str = "",
    entity: str = "ag",
    **kwargs,
) -> "Document":
    """Build a DIN 5008 business letter.

    Args:
      title: Letter title (e.g. "Advisory Brief").
      date_str: Letter date (e.g. "17 April 2026"). Default: empty.
      entity: DE contracting entity — "ag" (Digital Energy Group AG) or
        "nl" (Digital Energy Netherlands B.V.).
      **kwargs: Additional arguments passed to `profile_letter`.

    Returns: a python-docx `Document` object.
    """
    return _profile_letter(
        title=title, date_str=date_str, entity=entity, **kwargs
    )
