"""Visual-regression test for the Sites stream.

Phase 4 (rc3.4) — advisory CI gate per the plan's user-decision section
(LibreOffice render flakiness makes hard-gating impractical). The CI
job is marked ``continue-on-error: true`` so a golden mismatch reports
in the CI log but does not block merge.

Pipeline per fixture:

  deal.yaml → engine.main(...) → .docx
            → office_bridge.OfficeBridge.to_pdf_libreoffice(...)
            → pdfminer text extract → set-membership compare to
              tests/goldens/<slug>.txt

PDF conversion delegates to ``document-factory/office_bridge.py``
(`OfficeBridge.to_pdf_libreoffice`) — that's the canonical bridge that
wraps the bundled `anthropic-skills/docx/scripts/soffice.py`. It
encapsulates LibreOffice binary discovery + headless invocation; we
do not shell out to soffice here.

Goldens are captured manually with ``GOLDEN_REGEN=1 pytest`` against
the same engine + LibreOffice combo. CI never sets that env var.

Skips gracefully when:
  - ``libreoffice`` / ``soffice`` is missing (the bridge raises
    ``OfficeBridgeError`` — we map that to ``pytest.skip``)
  - ``pdfminer.six`` is not installed (cannot extract text)
  - the matching golden is missing AND ``GOLDEN_REGEN`` is not set
    (no baseline to compare against)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Iterable, List

import pytest

# conftest.py at sites/tests/conftest.py wires sites/_shared, sites/loi,
# sites/hot and document-factory onto sys.path.

GOLDEN_DIR = Path(__file__).parent / "goldens"
SITES = Path(__file__).resolve().parents[1]
LOI_FIXTURE = SITES / "loi" / "examples" / "deal_van-gog.yaml"
HOT_FIXTURE = SITES / "tests" / "fixtures" / "phase_g_moerman.yaml"


# ---------------------------------------------------------------------------
# Capability gates
# ---------------------------------------------------------------------------

pdfminer = pytest.importorskip("pdfminer.high_level", reason="pdfminer.six not installed")

# Lazy bridge construction — defer the OfficeBridge import + instantiation
# to first call, so an environment without the bridge importable still
# produces a clean skip rather than an ImportError at collection.

_BRIDGE = None
_BRIDGE_ERROR_CLS = None


def _get_bridge():
    global _BRIDGE, _BRIDGE_ERROR_CLS
    if _BRIDGE is not None:
        return _BRIDGE
    try:
        from office_bridge import OfficeBridge, OfficeBridgeError  # type: ignore
    except ImportError as exc:
        pytest.skip(f"document-factory office_bridge not importable: {exc}")
    _BRIDGE_ERROR_CLS = OfficeBridgeError
    _BRIDGE = OfficeBridge()
    return _BRIDGE


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _docx_to_pdf(docx_path: Path, out_dir: Path) -> Path:
    """Convert ``docx_path`` to a PDF in ``out_dir`` via the canonical
    document-factory bridge (``OfficeBridge.to_pdf_libreoffice``). The
    bridge wraps the bundled anthropic-skills soffice script — single
    source of truth for headless docx→pdf conversion in this repo.

    rc3.4 audit follow-up: rc1's direct ``shutil.which('soffice')`` +
    ``subprocess.run([soffice, ...])`` shell-out duplicated the bridge.
    Removed in favour of the canonical entry point.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    bridge = _get_bridge()
    pdf = out_dir / (docx_path.stem + ".pdf")
    try:
        bridge.to_pdf_libreoffice(str(docx_path), str(pdf))
    except _BRIDGE_ERROR_CLS as exc:  # type: ignore[arg-type]
        # bridge raises this when LibreOffice/soffice can't be found —
        # treat as a skip, not a hard failure (matches the rc1 contract:
        # "skip gracefully when libreoffice/soffice is missing").
        pytest.skip(f"LibreOffice unavailable via office_bridge: {exc}")
    if not pdf.exists():
        # Some bridge implementations honour the requested out path;
        # others leave the PDF next to the source. Reconcile.
        candidate = docx_path.with_suffix(".pdf")
        if candidate.exists():
            candidate.replace(pdf)
    if not pdf.exists():
        raise RuntimeError(
            f"office_bridge.to_pdf_libreoffice produced no PDF at {pdf} "
            f"(or sibling fallback). docx_path: {docx_path}"
        )
    return pdf


def _extract_text(pdf_path: Path) -> str:
    """Extract concatenated visible text from ``pdf_path``."""
    from pdfminer.high_level import extract_text
    return extract_text(str(pdf_path))


def _normalise(line: str) -> str:
    """Collapse runs of whitespace + strip; case-preserving."""
    return " ".join(line.split()).strip()


def _meaningful_lines(text: str) -> List[str]:
    """Split + filter to lines worth comparing (skip empties / pure ws /
    layout artifacts like single punctuation)."""
    out: List[str] = []
    for raw in text.splitlines():
        n = _normalise(raw)
        if not n:
            continue
        # Skip page-break artifacts, lone glyphs, page numbers
        if len(n) <= 2 and not n.isalnum():
            continue
        out.append(n)
    return out


def _compare_or_regen(
    actual_text: str,
    golden_path: Path,
) -> List[str]:
    """If ``GOLDEN_REGEN=1`` rewrite the golden and return []. Otherwise
    compare actual lines against golden lines (set membership) and
    return missing-golden lines."""
    if os.environ.get("GOLDEN_REGEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(actual_text, encoding="utf-8")
        return []

    if not golden_path.exists():
        pytest.skip(
            f"Golden {golden_path} not present. Run with GOLDEN_REGEN=1 "
            "to capture an initial baseline."
        )

    golden_lines = set(_meaningful_lines(golden_path.read_text(encoding="utf-8")))
    actual_lines = set(_meaningful_lines(actual_text))
    return sorted(golden_lines - actual_lines)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_van_gog_loi_visual_regression(tmp_path):
    """End-to-end: Van Gog LOI deal.yaml → docx → pdf → text →
    diff vs goldens/van_gog_loi.txt.

    Golden lines that don't appear in the freshly rendered output are
    reported. Use ``GOLDEN_REGEN=1`` to refresh after intentional
    output changes.
    """
    if not LOI_FIXTURE.exists():
        pytest.skip(f"LOI fixture missing: {LOI_FIXTURE}")

    import generate_site_loi as engine  # noqa: WPS433
    rc = engine.main([str(LOI_FIXTURE), "--out-dir", str(tmp_path)])
    assert rc == 0, "engine.main() returned non-zero"

    docx_files = list(tmp_path.glob("*_DE_LOI_Site_van-gog-grubbenvorst_v1_*.docx"))
    assert len(docx_files) == 1, f"expected 1 docx, got {docx_files}"
    docx = docx_files[0]

    pdf = _docx_to_pdf(docx, tmp_path / "pdf")
    text = _extract_text(pdf)

    golden = GOLDEN_DIR / "van_gog_loi.txt"
    missing = _compare_or_regen(text, golden)

    if missing:
        sample = "\n  - ".join(missing[:20])
        pytest.fail(
            f"Visual regression: {len(missing)} golden line(s) missing "
            f"from rendered Van Gog LOI PDF. First {min(20, len(missing))}:\n  - {sample}"
        )


def test_moerman_hot_visual_regression(tmp_path):
    """End-to-end: Moerman HoT deal.yaml → body + annex docx → pdfs →
    concatenated text → diff vs goldens/moerman_hot.txt.

    HoT outputs two .docx files (body + annex-a). Both are converted,
    text concatenated, and compared as one corpus.
    """
    if not HOT_FIXTURE.exists():
        pytest.skip(f"HoT fixture missing: {HOT_FIXTURE}")

    import generate_site_hot as engine  # noqa: WPS433
    rc = engine.main([str(HOT_FIXTURE), "--out-dir", str(tmp_path)])
    assert rc == 0, "engine.main() returned non-zero"

    body_files = list(tmp_path.glob("*_body.docx"))
    annex_files = list(tmp_path.glob("*_annex-a.docx"))
    assert len(body_files) == 1, f"expected 1 body docx, got {body_files}"
    assert len(annex_files) == 1, f"expected 1 annex-a docx, got {annex_files}"

    pdf_dir = tmp_path / "pdf"
    body_pdf = _docx_to_pdf(body_files[0], pdf_dir)
    annex_pdf = _docx_to_pdf(annex_files[0], pdf_dir)
    text = _extract_text(body_pdf) + "\n\n--- ANNEX A ---\n\n" + _extract_text(annex_pdf)

    golden = GOLDEN_DIR / "moerman_hot.txt"
    missing = _compare_or_regen(text, golden)

    if missing:
        sample = "\n  - ".join(missing[:20])
        pytest.fail(
            f"Visual regression: {len(missing)} golden line(s) missing "
            f"from rendered Moerman HoT PDFs. First {min(20, len(missing))}:\n  - {sample}"
        )
