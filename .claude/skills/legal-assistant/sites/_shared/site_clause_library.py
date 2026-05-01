"""Site clause library — YAML loader + bilingual section renderer (rc3.3).

The Sites stream's clause text used to live as inline string lists inside
each engine (LOI, HoT, ...). This module externalises that text into a
YAML file per template so:

  1. Legal can review clause text in one place without grepping Python.
  2. Engines stop diverging on shared clauses (§1 Parties is identical
     across LOI and HoT — there should be one source of truth).
  3. New site templates ship a YAML file, not a copy-pasted Python list.

The loader is deliberately minimal:

  - regex placeholder substitution (no Jinja2 dependency)
  - dotted-path lookup against a context dict (e.g. ``{{provider.legal_name}}``)
  - non-string substitution values flow through
    ``site_doc_base.normalise_placeholder`` so ``None`` / empty / TODO
    markers collapse to ``[TBC]`` consistently with the rest of the chassis
  - missing dotted paths → ``[TBC]`` (never raises, never leaks ``None``)

Public API:

    @dataclass(frozen=True) class Clause                     # row in the YAML
    load_clauses(path) -> dict[str, Clause]                  # parse + validate
    get_clause(clauses, section_id, lang="en") -> list[str]  # safe lookup
    render_bilingual_section(doc, clauses, section_ids, ...) # render → docx

Asset-gating (Clause.asset_gate) is parsed but ignored at load time;
engines apply it post-load when composing section_ids for a render call.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Mapping, Optional

import yaml

# Loader runs from sites/_shared so siblings (site_doc_base) and document-
# factory siblings are both importable.
from site_doc_base import TBC_TOKEN, normalise_placeholder


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Clause:
    """A single clause row from the YAML library.

    Attributes:
        section_id:  Dotted section number, e.g. ``"1.1"`` or ``"3.2"``.
        heading_en:  EN heading. ``None`` when the parent section carries
                     the heading and this row is a sub-clause body.
        heading_nl:  NL heading; same semantics as ``heading_en``.
        en:          EN paragraphs (one string per paragraph).
        nl:          NL paragraphs; ``len(nl)`` MUST equal ``len(en)`` so
                     bilingual rendering keeps row alignment.
        asset_gate:  Optional dict describing engine-side gating, e.g.
                     ``{"any_partner_contributes": "land"}``. Loader does
                     not act on this — engines compose section_id lists.
        render_order: Numeric sort key. Engines that render an entire
                      section can sort by this; the explicit-list path
                      (``render_bilingual_section(..., ["1.1", "1.2"])``)
                      preserves caller order instead.
    """

    section_id: str
    heading_en: Optional[str]
    heading_nl: Optional[str]
    en: List[str]
    nl: List[str]
    asset_gate: Optional[dict]
    render_order: int


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------


def load_clauses(path: Path) -> dict[str, Clause]:
    """Parse the YAML file at ``path`` into a dict keyed by ``section_id``.

    Validates:
      - every clause has matching ``len(en) == len(nl)``
      - ``section_id`` values are unique across the file

    Raises:
        ValueError: on duplicate section_id or EN/NL paragraph-count mismatch.
        FileNotFoundError: if ``path`` doesn't exist.
        yaml.YAMLError: on malformed YAML.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    raw_clauses = data.get("clauses") or []
    out: dict[str, Clause] = {}
    for row in raw_clauses:
        section_id = row.get("section_id")
        if section_id is None:
            raise ValueError(
                f"clause row in {path} missing required field 'section_id'"
            )
        en = list(row.get("en") or [])
        nl = list(row.get("nl") or [])
        if len(en) != len(nl):
            raise ValueError(
                f"section {section_id} in {path}: EN/NL paragraph-count "
                f"mismatch (EN={len(en)} NL={len(nl)})"
            )
        if section_id in out:
            raise ValueError(
                f"duplicate section_id {section_id!r} in {path}"
            )
        out[section_id] = Clause(
            section_id=section_id,
            heading_en=row.get("heading_en"),
            heading_nl=row.get("heading_nl"),
            en=en,
            nl=nl,
            asset_gate=row.get("asset_gate"),
            render_order=int(row.get("render_order") or 0),
        )
    return out


# ---------------------------------------------------------------------------
# Lookup
# ---------------------------------------------------------------------------


def get_clause(
    clauses: Mapping[str, Clause],
    section_id: str,
    lang: str = "en",
) -> List[str]:
    """Return paragraphs for ``section_id`` in ``lang`` (``"en"`` or ``"nl"``).

    Returns ``["[TBC]"]`` if the section is missing — never raises. This is
    the canonical "missing clause" rendering, consistent with how
    ``site_doc_base.normalise_placeholder`` collapses missing scalars.
    """
    if lang not in ("en", "nl"):
        raise ValueError(f"lang must be 'en' or 'nl', got {lang!r}")
    clause = clauses.get(section_id)
    if clause is None:
        return [TBC_TOKEN]
    return list(clause.en if lang == "en" else clause.nl)


# ---------------------------------------------------------------------------
# Placeholder substitution
# ---------------------------------------------------------------------------


_PLACEHOLDER_RE = re.compile(r"\{\{([\w.]+)\}\}")


def _lookup_dotted(context: Mapping[str, Any], dotted: str) -> Any:
    """Walk ``context`` along dotted-path ``dotted``.

    Returns ``None`` (sentinel for "missing") at the first level where the
    path can't be followed — caller maps this to ``[TBC]``.
    """
    cur: Any = context
    for part in dotted.split("."):
        if isinstance(cur, Mapping) and part in cur:
            cur = cur[part]
        elif hasattr(cur, part):
            cur = getattr(cur, part)
        else:
            return None
    return cur


def _substitute(text: str, context: Optional[Mapping[str, Any]]) -> str:
    """Apply ``{{dotted.path}}`` substitution to ``text`` against ``context``.

    Non-string values flow through ``normalise_placeholder`` so ``None`` /
    empty / TODO markers collapse to ``[TBC]`` consistently with the rest
    of the chassis. Missing keys → ``[TBC]``.
    """
    if context is None:
        # Empty context → every placeholder collapses to [TBC].
        return _PLACEHOLDER_RE.sub(lambda m: TBC_TOKEN, text)

    def _replace(match: re.Match) -> str:
        dotted = match.group(1)
        value = _lookup_dotted(context, dotted)
        if value is None:
            return TBC_TOKEN
        if isinstance(value, str):
            # Empty / whitespace strings collapse to [TBC] via the
            # chassis normaliser; non-empty strings render verbatim
            # (no .strip()) so trailing punctuation in clause text
            # stays exact.
            stripped = value.strip()
            if not stripped:
                return TBC_TOKEN
            return value
        return normalise_placeholder(value)

    return _PLACEHOLDER_RE.sub(_replace, text)


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------


def render_bilingual_section(
    doc,
    clauses: Mapping[str, Clause],
    section_ids: List[str],
    *,
    heading_en: Optional[str] = None,
    heading_nl: Optional[str] = None,
    placeholder_subs: Optional[Mapping[str, Any]] = None,
) -> None:
    """Render the EN+NL paragraphs for ``section_ids`` as one bilingual table.

    Order: paragraphs appear in the order ``section_ids`` is supplied
    (NOT sorted by ``render_order``). This lets the engine compose
    asset-gated sections explicitly:

        render_bilingual_section(
            doc, _CLAUSES, ["1.1", "1.2", "1.3", "1.4"],
            heading_en="1. Parties", heading_nl="1. Partijen",
            placeholder_subs={"provider": provider},
        )

    Each placeholder ``{{a.b.c}}`` in a paragraph is substituted by walking
    ``placeholder_subs`` along the dotted path. Missing or empty keys
    render as ``[TBC]``.

    Args:
        doc:             python-docx ``Document``.
        clauses:         Output of ``load_clauses``.
        section_ids:     Section IDs to render, in the order listed.
        heading_en:      Optional EN heading rendered above the rows.
        heading_nl:      Optional NL heading; defaults to ``heading_en``.
        placeholder_subs: Context dict for ``{{...}}`` substitution.

    Raises:
        ValueError: propagated from ``render_bilingual_clause`` if the
            paragraph counts diverge after substitution (shouldn't happen
            given ``load_clauses`` validates EN/NL alignment).
    """
    en_paragraphs: List[str] = []
    nl_paragraphs: List[str] = []
    for sid in section_ids:
        en_paragraphs.extend(get_clause(clauses, sid, "en"))
        nl_paragraphs.extend(get_clause(clauses, sid, "nl"))

    en_paragraphs = [_substitute(p, placeholder_subs) for p in en_paragraphs]
    nl_paragraphs = [_substitute(p, placeholder_subs) for p in nl_paragraphs]

    # Local import to avoid hard dependency on document-factory at module
    # import time — engines that load the library for non-rendering use
    # (e.g. clause-text inspection in tests) shouldn't need the factory
    # path on sys.path.
    from bilingual_body import render_bilingual_clause

    render_bilingual_clause(
        doc,
        en_paragraphs,
        nl_paragraphs,
        heading=heading_en,
        heading_nl=heading_nl,
    )
