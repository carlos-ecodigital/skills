"""Pipeline routing dispatcher — M5.

Single entry point `build()` that dispatches to the right pipeline based
on the shape of the input.

Three pipelines exist in the document-factory:

  A — Structured intake (YAML/JSON → python-docx builder)
      Pipeline A produces deterministic agreements from a validated spec
      (LOI, NDA, MSA, bespoke, …). **Not yet wired through this
      dispatcher.** The current entry point is
      ``legal-assistant/colocation/generate_loi.py`` (YAML intake). M4
      extends that path with the Bespoke type. An ``AgreementSpec``
      dataclass + ``build_agreement(spec)`` public API is planned for
      after M4 lands; routing for those shapes raises
      ``NotImplementedError`` with a clear pointer until then.

  B — Preserving rebrand (docx → docx)
      Keep body content intact (numbering, lists, tables, track changes)
      and replace cover/headers/footers with DE branding. Entry point:
      ``rebrand.rebrand(input_path, spec)``. Routed here when caller
      passes a ``.docx`` path plus a ``RebrandSpec``.

  C — Markdown (content skills → branded docx)
      ``md_to_docx(...)`` renders a markdown string/file through the
      branded pipeline. Suitable for non-legal documents (board memos,
      exec summaries, reports). **Emits ``DeprecationWarning`` when the
      profile is an agreement** — markdown round-tripping loses native
      numbering, lists, and style-aware QA. Use Pipeline A or B instead
      for agreements. Next minor version promotes the warning to an
      error.

Deprecation (M5 phase 1):
  ``AGREEMENT_PROFILES`` names the profiles for which markdown is
  discouraged. Passing any of them to ``build()`` via the markdown path
  emits a ``DeprecationWarning`` that names both alternative pipelines
  and the structural reasons (numbering, QA) for the deprecation.

This module does **not** change the behavior of the underlying
pipelines. It is a thin router: it inspects the input shape, validates
the caller's arguments, then delegates to ``rebrand`` or ``md_to_docx``
as appropriate. M0 golden byte-diff tests continue to pass byte-identical.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path
from typing import Any, TYPE_CHECKING, Union

# Make same-dir imports work whether imported as a top-level module
# (common.py pattern) or a package module.
_THIS = Path(__file__).resolve().parent
if str(_THIS) not in sys.path:
    sys.path.insert(0, str(_THIS))

if TYPE_CHECKING:  # pragma: no cover — typing-only
    from rebrand import RebrandSpec


# ──────────────────────────────────────────────────────────────────────
# Deprecation policy

# Profiles for which Pipeline C (markdown) is being phased out.
# Extend this set as new agreement-like profiles are added.
AGREEMENT_PROFILES: frozenset[str] = frozenset({"agreement"})


_MD_AGREEMENT_DEPRECATION_MSG = (
    "Rendering an agreement profile ({profile!r}) through Pipeline C "
    "(markdown) is deprecated. Markdown round-tripping loses native "
    "numbering, loses native list/recital lettering, and cannot carry "
    "the build-time QA that agreements require (R-11 banned phrases, "
    "R-21 no-undersigned-when-cover-has-parties, party-duplication "
    "checks, etc.). Use Pipeline A for new drafts "
    "(legal-assistant/colocation/generate_loi.py — YAML intake, "
    "validated spec, audit_agreement gate) or Pipeline B "
    "(document_factory.rebrand — preserving .docx → .docx rebrand). "
    "This warning will become an error in the next minor version."
)


# ──────────────────────────────────────────────────────────────────────
# Public entry point


InputLike = Union[str, Path, dict, Any]  # AgreementSpec shape is unfixed


def build(
    input: InputLike,
    *,
    profile: str | None = None,
    md_opts: dict | None = None,
    rebrand_spec: "RebrandSpec | None" = None,
    agreement_spec: Any | None = None,
    **kwargs: Any,
):
    """Single entry point. Dispatches to Pipeline A / B / C based on
    the shape of ``input``.

    Routing rules (evaluated in order):

      1. ``input`` is a ``dict`` or matches an agreement-spec shape
         (``agreement_spec=...`` is also accepted): route to Pipeline A.
         Currently raises ``NotImplementedError`` with a pointer to
         ``legal-assistant/colocation/generate_loi.py`` — the canonical
         Pipeline A entry point. M4 is extending that path.

      2. ``input`` is a ``.docx`` path on disk: route to Pipeline B.
         Requires ``rebrand_spec``. Delegates to ``rebrand.rebrand``.
         Returns the raw ``.docx`` bytes (same return type as
         ``rebrand()`` itself).

      3. ``input`` is a markdown string or a ``.md`` file path: route
         to Pipeline C. Uses ``md_opts`` (a dict merged into the
         ``md_to_docx`` keyword arguments) plus the ``profile``. If
         ``profile`` is in ``AGREEMENT_PROFILES``, emits
         ``DeprecationWarning`` before calling through. Delegates to
         ``generate.md_to_docx``. Returns a ``python-docx`` Document.

    Parameters
    ----------
    input
        Path to a ``.docx`` (Pipeline B), path to a ``.md`` or a
        markdown string (Pipeline C), or a ``dict`` / agreement spec
        (Pipeline A).
    profile
        Profile name. Relevant for Pipeline C deprecation decisions
        (agreement profiles emit the warning). For Pipeline B the
        profile is implicit in the ``RebrandSpec``.
    md_opts
        Additional keyword arguments forwarded to ``md_to_docx`` —
        e.g. ``{"client": "Acme", "entity": "nl", "cover": True}``.
        Ignored for Pipelines A and B.
    rebrand_spec
        Required when routing to Pipeline B. A ``RebrandSpec``
        instance (see ``rebrand.py``).
    agreement_spec
        Alternative way to pass an agreement spec; reserved for
        Pipeline A when builders are wired in.
    **kwargs
        Caller's pass-through. Currently accepted only by Pipeline C
        (merged with ``md_opts``); Pipelines A and B reject unknown
        kwargs to surface mistakes early.

    Returns
    -------
    bytes | docx.document.Document
        Pipeline B returns the raw ``.docx`` bytes (as ``rebrand``
        does). Pipeline C returns a ``python-docx`` ``Document``
        object (as ``md_to_docx`` does). Pipeline A will return a
        ``Document`` once implemented.

    Raises
    ------
    NotImplementedError
        When the input shape maps to Pipeline A — see module docstring
        for the interim workflow.
    TypeError
        When the input shape is ambiguous or the wrong companion
        argument is missing (e.g. ``.docx`` path with no
        ``rebrand_spec``).
    """
    # ── Pipeline A: dict / agreement-spec shape ───────────────────
    if isinstance(input, dict) or agreement_spec is not None:
        _raise_pipeline_a_not_implemented()

    # A RebrandSpec object passed as the input argument itself is a
    # caller mistake — the spec goes in rebrand_spec; the docx path is
    # what routes. Catch it clearly rather than falling through to
    # str/Path detection.
    from rebrand import RebrandSpec  # local import — avoid circularity

    if isinstance(input, RebrandSpec):
        raise TypeError(
            "build(input=<RebrandSpec>) is not supported. Pass the "
            "input .docx path as `input=` and the spec as "
            "`rebrand_spec=`."
        )

    # ── Pipeline B: .docx path on disk ────────────────────────────
    if isinstance(input, (str, Path)):
        p = Path(input)
        if _looks_like_docx_path(p):
            if rebrand_spec is None:
                raise TypeError(
                    f"build({p!s}) looks like a .docx on disk but no "
                    "rebrand_spec was provided. Pipeline B requires a "
                    "RebrandSpec. See document-factory/rebrand.py."
                )
            if kwargs:
                # Pipeline B has a fixed signature; unknown kwargs
                # would be silently dropped otherwise.
                raise TypeError(
                    f"build() received unexpected keyword arguments "
                    f"for Pipeline B: {sorted(kwargs)}. rebrand() does "
                    "not accept them."
                )
            from rebrand import rebrand  # local import — avoid circularity
            return rebrand(p, rebrand_spec)

    # ── Pipeline C: markdown string or .md file path ──────────────
    md_text = _coerce_markdown(input)
    if md_text is not None:
        if profile in AGREEMENT_PROFILES:
            warnings.warn(
                _MD_AGREEMENT_DEPRECATION_MSG.format(profile=profile),
                DeprecationWarning,
                stacklevel=2,
            )
        return _invoke_pipeline_c(md_text, md_opts=md_opts, **kwargs)

    # Fall-through — shape unrecognised.
    raise TypeError(
        "build() could not route the input. Expected one of: "
        "(a) a .docx path with rebrand_spec= (Pipeline B), "
        "(b) a markdown string or .md path (Pipeline C), "
        "(c) a dict or AgreementSpec (Pipeline A — not yet "
        "implemented; use legal-assistant/colocation/generate_loi.py). "
        f"Got input of type {type(input).__name__}."
    )


# ──────────────────────────────────────────────────────────────────────
# Helpers


def _raise_pipeline_a_not_implemented() -> None:
    """Emit the standard Pipeline A not-implemented message.

    Kept as a single function so the wording is consistent across
    branches (dict input, explicit agreement_spec=, future spec
    types).
    """
    raise NotImplementedError(
        "Pipeline A (structured agreement intake → python-docx) is "
        "not wired through document_factory.build() yet. The current "
        "entry point for YAML-intake agreements is "
        "legal-assistant/colocation/generate_loi.py (being extended "
        "in M4 to add the Bespoke type). Once M4 lands and the "
        "AgreementSpec builders move into document-factory/builders/, "
        "build() will route dict/AgreementSpec inputs here. For "
        "non-agreement structured builds today, use the individual "
        "profile functions in document_factory.py directly. For docx→docx "
        "rebrand, pass a .docx path + rebrand_spec (Pipeline B). For "
        "markdown non-legal documents, pass a markdown string "
        "(Pipeline C)."
    )


def _looks_like_docx_path(p: Path) -> bool:
    """Heuristic: a ``.docx`` suffix that exists on disk.

    We require the file to exist; a string that merely ends in
    ``.docx`` without a file behind it is ambiguous (could be a
    user-supplied-but-stale path). The caller gets a clear
    ``FileNotFoundError`` from ``rebrand.rebrand`` if the path
    exists-but-is-wrong, and an explicit TypeError here if it
    doesn't exist.
    """
    if p.suffix.lower() != ".docx":
        return False
    return p.exists()


def _coerce_markdown(input: Any) -> str | None:
    """If ``input`` is a markdown string or a .md file, return the text.

    Returns ``None`` when the input doesn't look like markdown. The
    caller uses ``None`` as the "could not route" signal.

    Heuristic:
      - ``Path`` ending in ``.md`` / ``.markdown`` → read the file.
      - ``str`` ending in ``.md`` / ``.markdown`` that exists on disk
        → read the file.
      - Any other ``str`` → treat as markdown text.
    """
    if isinstance(input, Path):
        if input.suffix.lower() in {".md", ".markdown"}:
            return input.read_text(encoding="utf-8")
        return None

    if isinstance(input, str):
        # Short string that happens to point at an .md file.
        if input.endswith((".md", ".markdown")) and Path(input).exists():
            return Path(input).read_text(encoding="utf-8")
        # Otherwise assume markdown text. Bare strings that are neither
        # file paths nor markdown are rare; the heuristic favours the
        # common case. (Truly invalid input produces a downstream
        # rendering error — the dispatcher is not a validator.)
        return input

    return None


def _invoke_pipeline_c(md_text: str, *, md_opts: dict | None, **kwargs: Any):
    """Call ``md_to_docx`` with merged kwargs.

    ``md_opts`` (the explicit bag) and loose ``**kwargs`` are both
    supported; ``md_opts`` takes precedence on key collision because
    the caller set it explicitly.
    """
    from document_factory import md_to_docx  # local import — avoid circularity

    merged: dict[str, Any] = {}
    merged.update(kwargs)
    if md_opts:
        merged.update(md_opts)
    return md_to_docx(md_text, **merged)


__all__ = [
    "build",
    "AGREEMENT_PROFILES",
]
