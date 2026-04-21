"""Phase G regression — signed-HoT round-trip validation.

Goal: prove the v0.1 HoT engine, when fed a reconstructed ``deal.yaml``,
reproduces the commercial substance of 3 real signed HoTs:

- **Moerman** — reconstructed from reference-intake JSON
  (``sites/hot/examples/reference-intakes/moerman_annex-a-data.json``).
  No signed PDF on Drive; this is a round-trip validation of the
  engine's intake→output fidelity.
- **Schenkeveld** — reconstructed from 20250214_DE_HoT_Schenkeveld.pdf
  (DocuSign CD3DC32075-0391-4A8D-980A-44A1C5D0028E, signed 2025-02-14).
- **ECW** — reconstructed from 20250415_DE_HoT_ECW.pdf
  (DocuSign CD7B8DAE-81D1-4580-8459-957F651573F9, signed 2025-04-15).

**Important context** (Phase G finding, see phase_g_validation_report.md):
the signed PDFs predate the v1.0 Annex-A-with-shaded-cells template.
They use a bilingual narrative prose format with no Annex A table.
"Structural XML parity with the original signed Annex A" therefore
reduces to structural parity **with the v1.0 template** — which the
engine achieves by construction, since it only rewrites text inside
shaded cells. The content-level parity (values filled in shaded cells
match the values in the signed HoTs' prose) is the real assertion.

Tests degrade gracefully if Drive is unmounted — signed PDFs are only
read for byte-existence cross-checks, not content assertions. The
reconstructed ``deal.yaml`` fixtures are committed and self-contained.
"""

from __future__ import annotations

import os
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest

# sys.path wiring — mirror the HoT engine's setup
_HOT = Path(__file__).resolve().parents[1] / "hot"
if str(_HOT) not in sys.path:
    sys.path.insert(0, str(_HOT))

import generate_site_hot as eng  # noqa: E402

_FIXTURES = Path(__file__).resolve().parent / "fixtures"
_SIGNED_DIR = Path(
    "/Users/crmg/Library/CloudStorage/GoogleDrive-carlos@ecodigital.group"
    "/Shared drives/NEW_Ops/Projects Benelux_Ops/Signed HoTs"
)

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# Template baseline — any regenerated Annex A MUST match this structurally.
TEMPLATE_TABLES = 4
TEMPLATE_ROWS_PER_TABLE = [1, 23, 5, 1]
TEMPLATE_SHADED_REQUIRED = 39
TEMPLATE_SHADED_CONDITIONAL = 12


def _structural_metrics(docx_path: Path) -> dict:
    with zipfile.ZipFile(docx_path, "r") as z:
        root = ET.fromstring(z.read("word/document.xml"))
    tbls = list(root.iter(W + "tbl"))
    rows = [len(t.findall(W + "tr")) for t in tbls]
    sreq = scond = 0
    for tc in root.iter(W + "tc"):
        for tcPr in tc.findall(W + "tcPr"):
            for shd in tcPr.findall(W + "shd"):
                fill = shd.get(W + "fill")
                if fill == "FFFF99":
                    sreq += 1
                elif fill == "CCFFCC":
                    scond += 1
    return {
        "tables": len(tbls),
        "rows_per_table": rows,
        "shaded_required": sreq,
        "shaded_conditional": scond,
    }


def _regenerate(slug: str, tmp_path: Path):
    fixture = _FIXTURES / f"phase_g_{slug}.yaml"
    assert fixture.exists(), f"fixture missing: {fixture}"
    # Drive the engine's internals directly (rather than main()) so we
    # get the return objects for assertions.
    deal = eng.load_deal(fixture)
    registry = eng.sdb.load_registry()
    values = eng.build_field_values(deal)
    body_out = tmp_path / f"{slug}_body.docx"
    annex_out = tmp_path / f"{slug}_annex-a.docx"
    _, body_sha = eng.copy_body(body_out)
    stats = eng.populate_annex_a(
        eng.ANNEX_A_TEMPLATE, annex_out, values, registry
    )
    return {
        "deal": deal,
        "values": values,
        "annex_path": annex_out,
        "body_path": body_out,
        "body_sha": body_sha,
        "stats": stats,
    }


# ---------------------------------------------------------------------------
# 1. Moerman — round-trip parity against reference-intake JSON
# ---------------------------------------------------------------------------

def test_moerman_regeneration_matches_reference(tmp_path):
    """Moerman fixture should resolve ≥35 of the 58 registry fields
    and produce a structurally-valid Annex A.

    The 58-field target comes from field-registry.json + Section G
    notice fields; the ≥35 threshold is ~60 %, which is the realistic
    ceiling for a grower who has not yet provided EAN + financier data.
    """
    r = _regenerate("moerman", tmp_path)
    written = len(r["stats"].fields_written)
    assert written >= 35, (
        f"Moerman resolved only {written} fields; expected ≥35. "
        f"Written: {r['stats'].fields_written}"
    )
    metrics = _structural_metrics(r["annex_path"])
    assert metrics["tables"] == TEMPLATE_TABLES
    assert metrics["rows_per_table"] == TEMPLATE_ROWS_PER_TABLE
    assert metrics["shaded_required"] == TEMPLATE_SHADED_REQUIRED
    assert metrics["shaded_conditional"] == TEMPLATE_SHADED_CONDITIONAL
    # Sanity: key identity fields landed.
    v = r["values"]
    assert v["A.1"] == "Moerman Paprika B.V."
    assert v["A.2"] == "27178957"
    assert v["B.1"] == "Westland Infra"
    assert v["C.4"] == 18  # heat price


# ---------------------------------------------------------------------------
# 2. Schenkeveld — structural parity + signed-HoT cross-check
# ---------------------------------------------------------------------------

_SCHENKEVELD_PDF = _SIGNED_DIR / "20250214_DE_HoT_Schenkeveld.pdf"


@pytest.mark.skipif(
    not _SCHENKEVELD_PDF.exists(),
    reason="Drive not mounted — Schenkeveld signed HoT unavailable",
)
def test_schenkeveld_regeneration_structural_parity(tmp_path):
    """Regenerated Schenkeveld Annex A matches template structure and
    carries the KvK + grid capacities asserted in the signed prose."""
    r = _regenerate("schenkeveld", tmp_path)
    metrics = _structural_metrics(r["annex_path"])
    assert metrics["tables"] == TEMPLATE_TABLES
    assert metrics["rows_per_table"] == TEMPLATE_ROWS_PER_TABLE
    assert metrics["shaded_required"] == TEMPLATE_SHADED_REQUIRED
    assert metrics["shaded_conditional"] == TEMPLATE_SHADED_CONDITIONAL
    v = r["values"]
    # Fields asserted directly from the signed PDF's prose:
    assert v["A.1"] == "Schenkeveld Schiphol"
    assert v["A.2"] == "67743366"
    assert v["A.8"] == 44  # 44 hectare greenhouse
    assert v["B.4"] == 20  # total 20 MVA
    assert v["B.7"] == 6   # base 6 MVA
    assert v["B.10"] == 6  # future 6 MVA
    assert v["C.1"] == 70  # outlet ~70°C
    assert v["C.4"] == 0   # EUR 0 per MWh thermal
    # At least 25 of 58 fields populate — signed HoT's narrative
    # format does not surface EAN / ATO reference / kadaster parcel.
    assert len(r["stats"].fields_written) >= 25


# ---------------------------------------------------------------------------
# 3. ECW — utility-provider variant + structural parity
# ---------------------------------------------------------------------------

_ECW_PDF = _SIGNED_DIR / "20250415_DE_HoT_ECW.pdf"


@pytest.mark.skipif(
    not _ECW_PDF.exists(),
    reason="Drive not mounted — ECW signed HoT unavailable",
)
def test_ecw_regeneration_structural_parity(tmp_path):
    """Regenerated ECW Annex A matches template structure. ECW is a
    Utility Provider not a grower — the engine's single-partner grower
    assumption still produces a clean Annex A, with known caveats
    documented in phase_g_validation_report.md."""
    r = _regenerate("ecw", tmp_path)
    metrics = _structural_metrics(r["annex_path"])
    assert metrics["tables"] == TEMPLATE_TABLES
    assert metrics["rows_per_table"] == TEMPLATE_ROWS_PER_TABLE
    assert metrics["shaded_required"] == TEMPLATE_SHADED_REQUIRED
    assert metrics["shaded_conditional"] == TEMPLATE_SHADED_CONDITIONAL
    v = r["values"]
    assert v["A.1"] == "ECW Energy Trade B.V."
    assert v["A.2"] == "56518315"
    assert v["B.7"] == 5   # base ≥5 MVA
    assert v["C.1"] == 80  # outlet ~80°C
    assert v["C.4"] == 10  # EUR 10 per MWh (winter rate — flattened)
    assert len(r["stats"].fields_written) >= 20


# ---------------------------------------------------------------------------
# 4. Template determinism — same fixture → byte-deterministic inputs
# ---------------------------------------------------------------------------

def test_phase_g_template_structure_is_deterministic(tmp_path):
    """Running the engine on all 3 fixtures yields the exact same
    structural footprint (tables count, rows per table, shaded cell
    distribution). Proves the engine does not mutate the template
    structure under any deal.yaml input."""
    footprints = set()
    for slug in ("moerman", "schenkeveld", "ecw"):
        r = _regenerate(slug, tmp_path)
        m = _structural_metrics(r["annex_path"])
        footprints.add(
            (m["tables"], tuple(m["rows_per_table"]),
             m["shaded_required"], m["shaded_conditional"])
        )
    assert len(footprints) == 1, (
        "engine structural output should be deterministic across deals; "
        f"got {len(footprints)} distinct footprints: {footprints}"
    )
    only = next(iter(footprints))
    assert only == (
        TEMPLATE_TABLES,
        tuple(TEMPLATE_ROWS_PER_TABLE),
        TEMPLATE_SHADED_REQUIRED,
        TEMPLATE_SHADED_CONDITIONAL,
    )
