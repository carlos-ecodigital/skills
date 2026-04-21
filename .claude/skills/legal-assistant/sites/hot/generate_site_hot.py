"""Site HoT engine — v0.1.

Reads a ``deal.yaml`` file + ``field-registry.json``, produces a Heads of
Terms (HoT) package for a single-partner (grower) deal:

- **Body** — copies the locked ``hot-grower-body-v1.docx`` template verbatim
  (SHA-256 verified) to the output directory with a dated draft filename.
  The body template is LEGALLY LOCKED — NEVER modify its bytes.
- **Annex A** — opens ``hot-grower-annex-a-v1.docx`` as a zipfile, parses
  ``word/document.xml``, walks every shaded (yellow FFFF99 / conditional
  green CCFFCC) cell, and substitutes each field-marker paragraph's text
  with the value resolved from the deal via a section-to-path mapper.
  The original run/paragraph formatting (``rPr``/``pPr``) is preserved —
  only the inner ``<w:t>`` text is rewritten.
- **QA report** — plain-text summary (fields written, fields unresolved,
  cross-doc gate verdicts, Wave-2 TODOs).
- **Gate report** — JSON dump of ``cross_doc_gate.run(deal, stage='hot',
  prior_loi_deal=None)`` verdicts.

v0.1 scope: single Site Partner (grower-shaped). Multi-partner HoT
(e.g. separate Landowner or BESS JV party) ships in Wave 2; the engine
emits a warning for multi-partner inputs rather than silently merging.

Usage::

    python3 generate_site_hot.py path/to/deal.yaml --out-dir /tmp/

CLI shape mirrors ``sites/loi/generate_site_loi.py``.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from xml.etree import ElementTree as ET

import yaml

# ---------------------------------------------------------------------------
# sys.path setup — mirror the LOI engine pattern
# ---------------------------------------------------------------------------

_FACTORY_PATH = Path(__file__).resolve().parents[3] / "document-factory"
if str(_FACTORY_PATH) not in sys.path:
    sys.path.insert(0, str(_FACTORY_PATH))

_SHARED_PATH = Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED_PATH) not in sys.path:
    sys.path.insert(0, str(_SHARED_PATH))

import cross_doc_gate as cdg  # noqa: E402
import site_doc_base as sdb  # noqa: E402

# ---------------------------------------------------------------------------
# Constants — template paths + shading codes
# ---------------------------------------------------------------------------

_TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
BODY_TEMPLATE = _TEMPLATES_DIR / "hot-grower-body-v1.docx"
ANNEX_A_TEMPLATE = _TEMPLATES_DIR / "hot-grower-annex-a-v1.docx"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = "{" + W_NS + "}"

# Shading fills used to mark form-fill cells.
FILL_REQUIRED = "FFFF99"      # yellow: required fields
FILL_CONDITIONAL = "CCFFCC"   # green: conditional / optional fields


# ---------------------------------------------------------------------------
# SHA-256 helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Registry-driven field-ID lookup
# ---------------------------------------------------------------------------

#: Compiled regex that picks the "A.1" / "B.13" / "G.Grower_email" prefix
#: off a label-cell paragraph. Accepts both dot-number and dot-alnum forms.
_FIELD_ID_RE = re.compile(r"^\s*([A-G](?:\.[A-Za-z0-9_]+)+|[A-G]\.\d+[a-z]?)")


def _strip_field_prefix(text: str) -> str:
    m = _FIELD_ID_RE.match(text)
    return text[m.end():].strip() if m else text.strip()


def build_field_id_to_registry(registry: dict) -> Dict[str, Tuple[str, str, dict]]:
    """Map registry display IDs (e.g. "A.1") → (section_id, field_key, spec)."""
    out: Dict[str, Tuple[str, str, dict]] = {}
    for sec_id, field_id, spec in sdb.iter_fields(registry):
        display = spec.get("id") or field_id
        out[display] = (sec_id, field_id, spec)
    return out


# ---------------------------------------------------------------------------
# Deal → field-value mapping (section-to-path mapper)
# ---------------------------------------------------------------------------

def _partner(deal: dict) -> Optional[dict]:
    sps = deal.get("site_partners") or []
    return sps[0] if sps else None


def _find_contribution(partner: dict, asset: str) -> Optional[dict]:
    for c in partner.get("contributions") or []:
        if c.get("asset") == asset:
            return c
    return None


def _find_return(partner: dict, value: str) -> Optional[dict]:
    for r in partner.get("returns") or []:
        if r.get("value") == value:
            return r
    return None


def build_field_values(deal: dict) -> Dict[str, Any]:
    """Produce a flat ``display_id → value`` map covering every Annex A
    form-fill field we can resolve from the deal.yaml.

    Section-to-path mapper:
      A.* → site_partners[0] identity + greenhouse
      B.* → contributions[asset=grid_interconnection].details
      C.* → returns[value=energy_heat].details
      D.* → contributions[asset=land].details
      E.* → commercial
      F.* → addons-derived
      G.* → notices

    Unresolved fields are omitted; the form-fill engine leaves the
    template placeholder in place for them.
    """
    values: Dict[str, Any] = {}
    partner = _partner(deal) or {}

    # Header
    values["project_name"] = deal.get("project_name") or deal.get("slug", "[TBC]")
    values["version"] = deal.get("version", "1.0")
    values["date"] = date.today().strftime("%d-%m-%Y")

    # --- Section A: Grower + Greenhouse --------------------------------
    sig = partner.get("signatory") or {}
    greenhouse = partner.get("greenhouse") or {}
    values["A.1"] = partner.get("legal_name")
    values["A.2"] = partner.get("kvk")
    values["A.3"] = partner.get("registered_address")
    values["A.4"] = sig.get("name")
    values["A.5"] = sig.get("title")
    auth = sig.get("signing_authority")
    if auth:
        values["A.6"] = (
            "Sole / Zelfstandig bevoegd"
            if str(auth).lower().startswith("sole")
            else "Joint / Gezamenlijk bevoegd"
        )
    values["A.7"] = greenhouse.get("address") or partner.get("registered_address")
    values["A.8"] = greenhouse.get("current_size_ha")
    values["A.9"] = greenhouse.get("planned_size_ha") or greenhouse.get("current_size_ha")
    values["A.10"] = greenhouse.get("expansion_timeline") or "N/A"
    values["A.11"] = greenhouse.get("cultivation_type")

    # --- Section B: Grid Connection ------------------------------------
    grid = _find_contribution(partner, "grid_interconnection") or {}
    gd = grid.get("details") or {}
    values["B.1"] = gd.get("dso")
    values["B.2"] = gd.get("ean_code")
    values["B.3"] = gd.get("ato_reference")
    values["B.4"] = gd.get("total_connection_mva") or gd.get("mva")
    values["B.5"] = gd.get("total_import_mw") or gd.get("import_mw")
    values["B.6"] = gd.get("total_export_mw") or gd.get("export_mw")
    values["B.7"] = gd.get("base_connection_mva")
    values["B.8"] = gd.get("base_import_mw")
    values["B.9"] = gd.get("base_export_mw")
    values["B.10"] = gd.get("future_connection_mva")
    values["B.11"] = gd.get("future_import_mw")
    values["B.12"] = gd.get("future_export_mw")
    values["B.13"] = gd.get("sap_configuration")

    # --- Section C: Heat Supply ----------------------------------------
    heat = _find_return(partner, "energy_heat") or {}
    hd = heat.get("details") or {}
    values["C.1"] = hd.get("target_outlet_temp_c")
    values["C.2"] = hd.get("expected_return_temp_c")
    values["C.4"] = hd.get("heat_price_eur_mwh")
    values["C.5"] = hd.get("combined_eb")

    # --- Section D: Land & Property ------------------------------------
    land = _find_contribution(partner, "land") or _find_contribution(partner, "property") or {}
    ld = land.get("details") or {}
    values["D.1"] = ld.get("kadaster_parcels")
    values["D.2"] = ld.get("title_type")
    values["D.3"] = ld.get("encumbrances")
    values["D.4"] = ld.get("zoning_designation")
    values["D.5"] = ld.get("land_area_per_mw_m2")
    values["D.6"] = ld.get("opstalrecht_term_years")
    values["D.7"] = ld.get("mv_cable_length_m")

    # Conditional D.8–D.11 only when distinct landowner / land financier
    if ld.get("landowner_name") and ld.get("landowner_name") != partner.get("legal_name"):
        values["D.8"] = ld.get("landowner_name")
        values["D.9"] = ld.get("landowner_signatory")
    if ld.get("land_financier_name"):
        values["D.10"] = ld.get("land_financier_name")
        values["D.11"] = ld.get("land_financier_signatory")

    # --- Section E: Commercial Terms -----------------------------------
    commercial = deal.get("commercial") or {}
    values["E.1"] = commercial.get("heat_sales_split") or "50 : 50"
    values["E.2"] = commercial.get("payment_term_days")
    values["E.3"] = commercial.get("effective_date") or (
        (deal.get("timeline") or {}).get("hot_drafted_date")
    )

    # --- Section F: Optional provisions (addon-gated) ------------------
    addons = deal.get("addons") or {}
    values["F.1"] = "Include / Opnemen" if addons.get("chp_present") else "Delete / Verwijderen"
    values["F.2"] = "Include / Opnemen" if addons.get("co_investment") else "Delete / Verwijderen"

    # --- Section G: Notices --------------------------------------------
    notices = deal.get("notices") or {}
    values["G.DE_email"] = notices.get("de_email") or "contact@digitalenergy.ch"
    values["G.Grower_address"] = notices.get("grower_address") or partner.get("registered_address")
    values["G.Grower_email"] = notices.get("grower_email") or sig.get("email")
    if values.get("D.8"):
        values["G.Landowner_address"] = notices.get("landowner_address")
        values["G.Landowner_email"] = notices.get("landowner_email")
    if values.get("D.10"):
        values["G.Financier_address"] = notices.get("financier_address")
        values["G.Financier_email"] = notices.get("financier_email")

    # Strip None / "" so the form-fill engine leaves placeholders in place.
    return {k: v for k, v in values.items() if v not in (None, "")}


# ---------------------------------------------------------------------------
# Body template copy (verbatim, SHA-verified)
# ---------------------------------------------------------------------------

def copy_body(out_path: Path, source: Path = BODY_TEMPLATE) -> Tuple[Path, str]:
    """Copy the locked body template to ``out_path`` verbatim.

    Returns ``(out_path, sha256)``. The hash is computed on the source
    BEFORE and AFTER copy and asserted to match — this guards against
    FS corruption or accidental mid-stream modification.
    """
    if not source.exists():
        raise FileNotFoundError(f"body template missing: {source}")
    src_sha = sha256_of(source)
    shutil.copy2(str(source), str(out_path))
    dst_sha = sha256_of(out_path)
    if src_sha != dst_sha:
        raise RuntimeError(
            f"body template SHA mismatch after copy: {src_sha} != {dst_sha}"
        )
    return out_path, dst_sha


# ---------------------------------------------------------------------------
# Annex A XML form-fill
# ---------------------------------------------------------------------------

def _cell_fill(tc: ET.Element) -> Optional[str]:
    for tcPr in tc.findall(W + "tcPr"):
        for shd in tcPr.findall(W + "shd"):
            fill = shd.get(W + "fill")
            if fill:
                return fill
    return None


def _paragraph_text(p: ET.Element) -> str:
    return "".join((t.text or "") for t in p.iter(W + "t"))


def _set_paragraph_text(p: ET.Element, new_text: str) -> None:
    """Replace the text content of a paragraph while preserving the first
    run's properties. Extra runs are discarded; extra ``w:t`` collapsed."""
    runs = p.findall(W + "r")
    if not runs:
        r = ET.SubElement(p, W + "r")
        t = ET.SubElement(r, W + "t")
        t.text = new_text
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        return
    first = runs[0]
    ts = first.findall(W + "t")
    if ts:
        ts[0].text = new_text
        ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        for extra in ts[1:]:
            first.remove(extra)
    else:
        t = ET.SubElement(first, W + "t")
        t.text = new_text
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    for r in runs[1:]:
        p.remove(r)


def _render_select_value(existing_value_text: str, chosen: str) -> str:
    """For checkbox-style cells like "☐ Option1 | ☐ Option2", tick the
    chosen option and leave the others unticked. For plain-text cells,
    return the chosen value verbatim."""
    if "☐" not in existing_value_text:
        return str(chosen)
    parts = [p.strip() for p in existing_value_text.split("|")]
    out_parts: List[str] = []
    chosen_lc = str(chosen).strip().lower()
    for part in parts:
        label = part.replace("☐", "").replace("☑", "").strip()
        if chosen_lc and (chosen_lc in label.lower() or label.lower() in chosen_lc):
            out_parts.append(f"☑ {label}")
        else:
            out_parts.append(f"☐ {label}")
    return " | ".join(out_parts)


def _derive_field_id_from_label(label_paragraph_text: str) -> Optional[str]:
    """Extract the "A.1"/"G.Grower_email" display ID from a label paragraph."""
    m = _FIELD_ID_RE.match(label_paragraph_text)
    return m.group(1) if m else None


@dataclass
class FormFillStats:
    fields_written: List[str]
    fields_skipped: List[str]
    warnings: List[str]


#: Table 2 (Notice Addresses) party-keyword → (address_field_id, email_field_id)
_NOTICE_ROW_KEYS: Dict[str, Tuple[str, str]] = {
    "digital energy": ("G.DE_address", "G.DE_email"),
    "grower": ("G.Grower_address", "G.Grower_email"),
    "teler": ("G.Grower_address", "G.Grower_email"),
    "landowner": ("G.Landowner_address", "G.Landowner_email"),
    "grondeigenaar": ("G.Landowner_address", "G.Landowner_email"),
    "financier": ("G.Financier_address", "G.Financier_email"),
    "grondfinancier": ("G.Financier_address", "G.Financier_email"),
}


def populate_annex_a(
    source: Path,
    destination: Path,
    values: Dict[str, Any],
    registry: dict,
) -> FormFillStats:
    """XML-walk the Annex A template; substitute form-fill values.

    Three passes, each for a distinct row layout:

    1. **Shaded-row pass** (Tables 1+) — for rows with ≥2 shaded cells,
       treat the first shaded cell as the EN label and the last as the
       value cell. Match paragraphs positionally; each label paragraph
       carries a "A.1"-style field-ID prefix.
    2. **Header-table pass** (Table 0) — Project/Version/Date value cells
       are FFFF99 but the labels sit in the immediately-preceding cell
       (unshaded). Dispatch by label text.
    3. **Notice-address pass** (Table 2) — column 0 is the party name
       (unshaded), columns 1 and 2 are address + email (shaded). Dispatch
       by matching the party name against ``_NOTICE_ROW_KEYS``.

    Re-zips ``destination`` preserving all other .docx parts verbatim.
    """
    if not source.exists():
        raise FileNotFoundError(f"annex template missing: {source}")

    fields_written: List[str] = []
    fields_skipped: List[str] = []
    warnings: List[str] = []

    ET.register_namespace("", W_NS)
    ET.register_namespace("w", W_NS)

    with zipfile.ZipFile(source, "r") as zin:
        parts = {name: zin.read(name) for name in zin.namelist()}

    xml_raw = parts["word/document.xml"]
    root = ET.fromstring(xml_raw)

    # --- Pass 1: shaded-row pass (all tables) -------------------------
    for tbl in root.iter(W + "tbl"):
        for tr in tbl.findall(W + "tr"):
            cells = tr.findall(W + "tc")
            if not cells:
                continue
            shaded_cells = [(idx, c, _cell_fill(c)) for idx, c in enumerate(cells)]
            shaded_cells = [x for x in shaded_cells
                            if x[2] in (FILL_REQUIRED, FILL_CONDITIONAL)]
            if len(shaded_cells) < 2:
                continue  # header, fixed row, or notice-address row — handled below
            label_en_idx = shaded_cells[0][0]
            value_idx = shaded_cells[-1][0]
            if value_idx == label_en_idx:
                continue
            label_cell = cells[label_en_idx]
            value_cell = cells[value_idx]
            label_paragraphs = label_cell.findall(W + "p")
            value_paragraphs = value_cell.findall(W + "p")
            if len(label_paragraphs) != len(value_paragraphs):
                warnings.append(
                    f"paragraph count mismatch in shaded row "
                    f"(label={len(label_paragraphs)}, value={len(value_paragraphs)})"
                )
                continue
            for lp, vp in zip(label_paragraphs, value_paragraphs):
                lbl_text = _paragraph_text(lp)
                field_id = _derive_field_id_from_label(lbl_text)
                if not field_id:
                    continue
                if field_id in values:
                    existing_vp_text = _paragraph_text(vp)
                    rendered = _render_select_value(existing_vp_text, values[field_id])
                    _set_paragraph_text(vp, rendered)
                    fields_written.append(field_id)
                else:
                    fields_skipped.append(field_id)

    # --- Pass 2: header table (Project/Version/Date) ------------------
    tables = list(root.iter(W + "tbl"))
    if len(tables) >= 1:
        for tr in tables[0].findall(W + "tr"):
            cells = tr.findall(W + "tc")
            for i, tc in enumerate(cells):
                if _cell_fill(tc) != FILL_REQUIRED:
                    continue
                if i == 0:
                    continue
                label_txt = "".join(t.text or "" for t in cells[i - 1].iter(W + "t"))
                label_lc = label_txt.strip().lower().rstrip(":")
                hdr_key = {
                    "project": "project_name",
                    "version": "version",
                    "date": "date",
                }.get(label_lc)
                if hdr_key and hdr_key in values:
                    ps = tc.findall(W + "p")
                    if ps:
                        _set_paragraph_text(ps[0], str(values[hdr_key]))
                        fields_written.append(hdr_key)

    # --- Pass 3: notice-address table (Table 2) -----------------------
    if len(tables) >= 3:
        for tr in tables[2].findall(W + "tr"):
            cells = tr.findall(W + "tc")
            if len(cells) < 3:
                continue
            party_label = "".join(
                t.text or "" for t in cells[0].iter(W + "t")
            ).lower()
            matched: Optional[Tuple[str, str]] = None
            for kw, ids in _NOTICE_ROW_KEYS.items():
                if kw in party_label:
                    matched = ids
                    break
            if not matched:
                continue
            addr_id, email_id = matched
            for field_id, cell in ((addr_id, cells[1]), (email_id, cells[2])):
                fill = _cell_fill(cell)
                if fill not in (FILL_REQUIRED, FILL_CONDITIONAL):
                    continue
                if field_id not in values:
                    fields_skipped.append(field_id)
                    continue
                ps = cell.findall(W + "p")
                if ps:
                    _set_paragraph_text(ps[0], str(values[field_id]))
                    fields_written.append(field_id)

    # Re-zip mutated XML, preserving all other .docx parts verbatim.
    new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    parts["word/document.xml"] = new_xml

    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in parts.items():
            zout.writestr(name, data)

    return FormFillStats(
        fields_written=fields_written,
        fields_skipped=fields_skipped,
        warnings=warnings,
    )


# ---------------------------------------------------------------------------
# Pipeline entry points (mirroring LOI engine)
# ---------------------------------------------------------------------------

def load_deal(deal_yaml_path: Path) -> dict:
    with open(deal_yaml_path, "r", encoding="utf-8") as f:
        deal = yaml.safe_load(f) or {}
    schema_version = deal.get("deal_yaml_schema_version")
    if schema_version != "1.0":
        raise ValueError(
            f"deal.yaml schema version mismatch: got {schema_version!r}, "
            "expected '1.0'"
        )
    return deal


def hydrate_from_hubspot(deal: dict) -> dict:
    """TODO(Phase B7 / hubspot_sync.py): round-trip read/write Deal + Companies
    + Contacts, resolve conflicts. Passthrough for v0.1."""
    return deal


def parse_documents(deal: dict, documents_dir: Path) -> dict:
    """TODO(Phase B5 / document_parsers): iterate deal['documents'][],
    invoke parsers, populate enrichment. Passthrough for v0.1."""
    return deal


def run_cross_doc_gate(deal: dict, prior_loi_deal: Optional[dict] = None) -> list[dict]:
    """Phase B8 — invoke the cross-doc gate in HoT stage."""
    verdicts = cdg.run(deal, stage="hot", prior_loi_deal=prior_loi_deal)
    return cdg.to_dict_list(verdicts)


# ---------------------------------------------------------------------------
# QA report + gate report
# ---------------------------------------------------------------------------

def write_qa_report(
    deal: dict,
    values: Dict[str, Any],
    fill_stats: FormFillStats,
    gate_verdicts: List[dict],
    body_sha: str,
    out_path: Path,
) -> Path:
    lines: List[str] = []
    slug = deal.get("slug", "unknown")
    lines.append(f"QA report for Site HoT draft: {slug}")
    lines.append(f"Generated: {date.today().isoformat()}")
    lines.append("")
    lines.append(f"Body template SHA-256: {body_sha}")
    lines.append(f"Fields written   : {len(fill_stats.fields_written)}")
    for fid in fill_stats.fields_written:
        lines.append(f"  + {fid}")
    lines.append(f"Fields unresolved: {len(fill_stats.fields_skipped)}")
    for fid in fill_stats.fields_skipped:
        lines.append(f"  - {fid}")
    if fill_stats.warnings:
        lines.append("Form-fill warnings:")
        for w in fill_stats.warnings:
            lines.append(f"  ! {w}")
    lines.append("")
    lines.append(f"Cross-doc gate verdicts: {len(gate_verdicts)}")
    for v in gate_verdicts:
        lines.append(f"  - {v}")
    lines.append("")
    lines.append("Integration TODOs (Wave 2):")
    lines.append("  - Multi-partner HoT (v0.1 is single-partner only)")
    lines.append("  - Phase B7: hubspot_sync round-trip")
    lines.append("  - Phase B5: document_parsers enrichment")
    lines.append("  - Phase E wiring: output_router.route() Drive handoff")
    lines.append("  - Annex A: conditional D.8-D.11 / F.1-F.2a row deletion "
                 "when addon not active (currently leaves placeholder)")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def write_gate_report(gate_verdicts: List[dict], out_path: Path) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "stage": "hot",
        "generated_at": date.today().isoformat(),
        "verdicts": gate_verdicts,
    }
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render a Site HoT (body + Annex A) .docx pair from a deal.yaml file."
    )
    parser.add_argument("deal_yaml", type=Path, help="Path to deal.yaml")
    parser.add_argument(
        "--out-dir", type=Path, default=Path("/tmp"),
        help="Output directory (defaults to /tmp). output_router.route() "
             "Drive handoff is Phase E wiring.",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Run pipeline but do not write output files.",
    )
    args = parser.parse_args(argv)

    deal = load_deal(args.deal_yaml)
    deal = hydrate_from_hubspot(deal)
    deal = parse_documents(deal, args.deal_yaml.parent / "documents")

    # Multi-partner warning (v0.1 is single-partner only).
    if len(deal.get("site_partners") or []) > 1:
        print(
            "WARN: multi-partner HoT requested; v0.1 engine uses partner[0] "
            "as the grower and ignores the rest — TODO(Wave 2).",
            file=sys.stderr,
        )

    registry = sdb.load_registry()
    values = build_field_values(deal)
    gate_verdicts = run_cross_doc_gate(deal, prior_loi_deal=None)

    slug = deal.get("slug", "unknown")
    today_str = date.today().strftime("%Y%m%d")
    stem = f"{today_str}_DE_HoT_Site_{slug}_v1"

    if args.dry_run:
        print(f"[dry-run] would have written HoT for {slug}")
        print(f"[dry-run] resolved {len(values)} fields")
        print(f"[dry-run] gate verdicts: {len(gate_verdicts)}")
        return 0

    args.out_dir.mkdir(parents=True, exist_ok=True)
    body_path = args.out_dir / f"{stem}_(DRAFT)_body.docx"
    annex_path = args.out_dir / f"{stem}_(DRAFT)_annex-a.docx"
    qa_path = args.out_dir / f"{stem}_qa.txt"
    gate_path = args.out_dir / f"{stem}_gate-report.json"

    # Body — verbatim copy with SHA guard
    _, body_sha = copy_body(body_path)

    # Annex A — XML form-fill
    stats = populate_annex_a(ANNEX_A_TEMPLATE, annex_path, values, registry)

    # QA + gate-report
    write_qa_report(deal, values, stats, gate_verdicts, body_sha, qa_path)
    write_gate_report(gate_verdicts, gate_path)

    print(f"Body:        {body_path}")
    print(f"Annex A:     {annex_path}")
    print(f"QA report:   {qa_path}")
    print(f"Gate report: {gate_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
