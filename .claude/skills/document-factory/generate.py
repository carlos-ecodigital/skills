#!/usr/bin/env python3
"""
Digital Energy Document Generator
===================================
Single-file generator. No XML manipulation. Only native python-docx API.

Usage:
    python3 generate.py --profile letter
    python3 generate.py --profile agreement --title "Colocation Agreement" --client "Younggrow BV"
    python3 generate.py --profile seed_memo --client "Acme Fund"
    python3 generate.py --profile investor_memo --client "Infrastructure Partners"
    python3 generate.py --profile exec_summary --title "PowerGrow Project Update"

Add --dotx to also save a Word template file.
"""

import argparse
import os
import sys
import re
from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional

try:
    from docx import Document
    from docx.shared import Mm, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
    from docx.oxml.ns import qn
    from lxml import etree
except ImportError:
    print("Error: python-docx is required. Install with: pip install python-docx")
    sys.exit(1)

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

DE_WEBSITE = "digital-energy.group"

ENTITY_FOOTERS = {
    "ag": {
        "legal_name": "Digital Energy Group AG",
        "address": "Baarerstrasse 43, 6300 Zug, Switzerland",
        "registration": "CHE-408.639.320",
        "website": DE_WEBSITE,
        "return_address": "Digital Energy Group AG  \u2022  Baarerstrasse 43  \u2022  6300 Zug",
    },
    "nl": {
        "legal_name": "Digital Energy Netherlands B.V.",
        "address": "Mijnsherenweg 33 A, 1433 AP Kudelstaart, The Netherlands",
        "registration": "KvK 98580086",
        "website": DE_WEBSITE,
        "return_address": "Digital Energy Netherlands B.V.  \u2022  Mijnsherenweg 33 A  \u2022  1433 AP Kudelstaart",
    },
}
ENTITY = ENTITY_FOOTERS["ag"]  # Backward-compat default


def _footer_text(entity_key="ag"):
    e = ENTITY_FOOTERS.get(entity_key, ENTITY_FOOTERS["ag"])
    return "  \u00b7  ".join([e["legal_name"], e["address"], e["registration"], e["website"]])

FONT = "Inter"

# DE Approved Palette (2026-03-31) — see memory/project_de_brand_palette.md
# Intended use by domain:
#   COBALT  → primary CTA / headers / links (default accent)
#   VOLT    → success / growth accents (finance reports, KPI tables)
#   NEON    → technology / AI themes (product, pitch)
#   MINERAL → compute / premium (investor memos)
#   FORGE   → heat / construction (permits, engineering)
#   SAFFRON → value / returns (IRR tables, unit economics)
#   PATINA  → sustainability (ESG, emissions)
#   SLATE   → secondary / captions (default body secondary)
# Constants are exported for import by any skill that needs them.
COBALT = RGBColor(0x00, 0x34, 0xAF)      # Primary CTA, headers
VOLT = RGBColor(0x63, 0xE2, 0x34)        # Success, growth
NEON = RGBColor(0x16, 0xD3, 0xF2)        # Info, technology
MINERAL = RGBColor(0x58, 0x1C, 0x87)     # AI/compute, premium
FORGE = RGBColor(0xC0, 0x56, 0x21)       # Heat, construction
SAFFRON = RGBColor(0xE5, 0xB2, 0x1D)     # Value, returns
PATINA = RGBColor(0x0F, 0x76, 0x6E)      # Sustainability
SLATE = RGBColor(0x64, 0x74, 0x8B)       # Slate 500 — captions, secondary

# Neutral ramp (Slate)
SLATE_50_HEX = "F8FAFC"                   # Table alt-row shading (hex for XML attrs)
SLATE_300_HEX = "CBD5E1"                   # Table borders (hex for XML attrs)
COBALT_HEX = "0034AF"                      # Header fill (hex for XML attrs)
SLATE_800 = RGBColor(0x1E, 0x29, 0x3B)   # Body text
SLATE_900 = RGBColor(0x0F, 0x17, 0x2A)   # Headings
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(SCRIPT_DIR, "assets", "DE_Logo_Black.png")
if not os.path.exists(LOGO):
    # Fallback: check script directory root
    LOGO = os.path.join(SCRIPT_DIR, "DE_Logo_Black.png")
if not os.path.exists(LOGO):
    print("Warning: DE_Logo_Black.png not found — documents will be generated without logo",
          file=sys.stderr)
OUTPUT = os.path.join(SCRIPT_DIR, "output")

PROFILE_CODES = {
    "letter": "Letter",
    "agreement": "Agreement",
    "seed_memo": "Seed_Memo",
    "investor_memo": "Investor_Memo",
    "exec_summary": "Exec_Summary",
}



# ---------------------------------------------------------------------------
# PARTY DATA MODEL + ENTITY SYSTEM
# ---------------------------------------------------------------------------

@dataclass
class Party:
    legal_name: str = ""
    address: str = ""
    registration_type: Optional[str] = None    # "KvK", "CHE", "EIN"
    registration_number: Optional[str] = None
    parent: Optional[str] = None               # Parent company name + reg


DE_ENTITIES = {
    "ag": Party(
        legal_name="Digital Energy Group AG",
        address="Baarerstrasse 43, 6300 Zug, Switzerland",
        registration_type="CHE",
        registration_number="408.639.320",
    ),
    "nl": Party(
        legal_name="Digital Energy Netherlands B.V.",
        address="Mijnsherenweg 33 A, 1433 AP Kudelstaart, The Netherlands",
        registration_type="KvK",
        registration_number="98580086",
    ),  # No parent — NL presented as standalone entity on all documents
}


AGREEMENT_FORMALITY = {
    # Non-binding: name + address. Labels: "Between:" / "And:"
    "Letter of Intent": "non_binding",
    "Letter of Intent and NCNDA": "non_binding",
    "LOI": "non_binding",
    "NCNDA": "non_binding",
    "NDA": "non_binding",
    "HoT": "non_binding",
    "Heads of Terms": "non_binding",
    "MoU": "non_binding",
    "Memorandum of Understanding": "non_binding",
    "Term Sheet": "non_binding",
    "Non-Disclosure Agreement": "non_binding",
    "Non-Circumvention Non-Disclosure Agreement": "non_binding",
    # Binding: name + address + registration. Labels: "By and between:" / "And:"
    "Master Service Agreement": "binding",
    "MSA": "binding",
    "SPA": "binding",
    "Sales and Purchase Agreement": "binding",
    "JVA": "binding",
    "Joint Venture Agreement": "binding",
    "SHA": "binding",
    "Shareholders Agreement": "binding",
    "License Agreement": "binding",
    "Services Agreement": "binding",
    "Colocation Agreement": "binding",
    "Advisory Agreement": "binding",
    "SAR Grant Agreement": "binding",
    "Board Resolution": "binding",
    "Program Policy": "non_binding",
    "Terms of Reference": "non_binding",
    "Stock Appreciation Rights — Term Sheet": "non_binding",
}


def _detect_formality(title):
    """Look up formality by exact match, then by prefix match."""
    if not title:
        return "non_binding"
    if title in AGREEMENT_FORMALITY:
        return AGREEMENT_FORMALITY[title]
    # Prefix match: "Board Resolution — SAR Program" matches "Board Resolution"
    for key, val in AGREEMENT_FORMALITY.items():
        if title.startswith(key):
            return val
    return "non_binding"


_TYPE_ABBREVS = {
    "Letter of Intent": "LOI",
    "Letter of Intent and NCNDA": "LOI_NCNDA",
    "NCNDA": "NCNDA",
    "NDA": "NDA",
    "Heads of Terms": "HoT",
    "HoT": "HoT",
    "MoU": "MoU",
    "Term Sheet": "TS",
    "Master Service Agreement": "MSA",
    "MSA": "MSA",
    "SPA": "SPA",
    "Sales and Purchase Agreement": "SPA",
    "JVA": "JVA",
    "Joint Venture Agreement": "JVA",
    "SHA": "SHA",
    "Shareholders Agreement": "SHA",
    "License Agreement": "License",
    "Services Agreement": "Services",
    "Colocation Agreement": "Colo",
}


def _type_code(agreement_type):
    if not agreement_type:
        return None
    if agreement_type in _TYPE_ABBREVS:
        return _TYPE_ABBREVS[agreement_type]
    # Fallback: alphanumeric with underscores, word-boundary truncation at 20
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", agreement_type).strip("_")
    if not cleaned:
        return None
    max_len = 25
    if len(cleaned) <= max_len:
        return cleaned
    # Find the last underscore at-or-before max_len; if none, hard-trim at 20
    cut = cleaned.rfind("_", 0, max_len + 1)
    if cut <= 0:
        return cleaned[:20]
    return cleaned[:cut]


def auto_name(profile, client=None, version=1, dt=None, agreement_type=None):
    if dt is None:
        dt = date.today()
    if profile == "agreement" and agreement_type:
        type_part = _type_code(agreement_type) or PROFILE_CODES["agreement"]
    else:
        type_part = PROFILE_CODES.get(profile, profile)
    parts = [dt.strftime("%Y%m%d"), "DE", type_part]
    if client:
        parts.append(client.replace(" ", "_")[:30])
    parts.append(f"v{version}")
    return "_".join(parts) + ".docx"


# ---------------------------------------------------------------------------
# BUILDING BLOCKS (no OxmlElement, no raw XML)
# ---------------------------------------------------------------------------

def _fix_zoom(doc):
    """Ensure w:zoom has w:percent attribute (python-docx omits it, fails OOXML validation)."""
    settings = doc.settings.element
    zoom = settings.find(qn('w:zoom'))
    if zoom is not None and zoom.get(qn('w:percent')) is None:
        zoom.set(qn('w:percent'), '100')


def save_doc(doc, path):
    """Save document with all post-processing fixes applied."""
    _fix_zoom(doc)
    doc.save(path)


def _run(para, text, size=Pt(11), color=SLATE_800, bold=False, italic=False, font=FONT):
    """Add a styled run."""
    r = para.add_run(text)
    r.font.name = font
    r.font.size = size
    r.font.color.rgb = color
    r.font.bold = bold
    r.font.italic = italic
    return r


def new_doc(top=Mm(20), bottom=Mm(35), diff_first=False):
    """Create A4 document."""
    doc = Document()
    s = doc.sections[0]
    s.page_width = Mm(210)
    s.page_height = Mm(297)
    s.left_margin = Mm(25)
    s.right_margin = Mm(20)
    s.top_margin = top
    s.bottom_margin = bottom
    s.different_first_page_header_footer = diff_first
    return doc


def setup_first_page_header(section, logo_height=Mm(12)):
    """First page: logo only."""
    h = section.first_page_header
    h.is_linked_to_previous = False
    if os.path.exists(LOGO):
        h.paragraphs[0].add_run().add_picture(LOGO, height=logo_height)


def setup_cont_header(section, title=""):
    """Continuation pages: small logo left, title right."""
    h = section.header
    h.is_linked_to_previous = False
    p = h.paragraphs[0]
    p.paragraph_format.tab_stops.add_tab_stop(Mm(165), WD_TAB_ALIGNMENT.RIGHT)
    if os.path.exists(LOGO):
        p.add_run().add_picture(LOGO, height=Mm(8))
    if title:
        p.add_run("\t")
        r = p.add_run(title)
        r.font.size = Pt(9)
        r.font.name = FONT
        r.font.color.rgb = SLATE


def setup_footer(footer, classification=None, entity="ag"):
    """Footer: entity details left, page number right.

    Classification is intentionally NOT prefixed into the footer — it appears
    once on the cover page's metadata block. Repeating "Confidential" on every
    page footer is redundant noise. The `classification` arg is retained for
    signature compatibility but ignored here.
    """
    p = footer.paragraphs[0]
    p.paragraph_format.tab_stops.add_tab_stop(Mm(165), WD_TAB_ALIGNMENT.RIGHT)
    r = p.add_run(_footer_text(entity))
    r.font.size = Pt(7)
    r.font.name = FONT
    r.font.color.rgb = SLATE


def setup_first_footer(section, classification=None, entity="ag"):
    f = section.first_page_footer
    f.is_linked_to_previous = False
    setup_footer(f, classification, entity)


def setup_cont_footer(section, classification=None, entity="ag"):
    f = section.footer
    f.is_linked_to_previous = False
    setup_footer(f, classification, entity)


def _cover_title(agreement_type):
    """Derive the concise cover-page title from the full agreement type.

    Compound agreement names (e.g. "Letter of Intent and Non-Circumvention
    Non-Disclosure Agreement") are shortened to the primary type on the cover.
    The full legal name continues to appear in the body/recitals.

    Examples:
        "Letter of Intent and Non-Circumvention Non-Disclosure Agreement" -> "Letter of Intent"
        "Letter of Intent and NCNDA" -> "Letter of Intent"
        "Master Service Agreement" -> "Master Service Agreement"
    """
    if not agreement_type:
        return agreement_type
    # Split on " and " — primary type is the first segment
    primary = agreement_type.split(" and ")[0].strip()
    return primary or agreement_type


def add_cover(doc, agreement_type, subject=None, date_str=None,
              parties=None, party_labels=None, formality="non_binding",
              reference=None, version=None, classification="Confidential",
              cover_title=None):
    """IB-standard cover page with structured hierarchy.

    Rendering order:
      1. Agreement type (28pt bold) — e.g. "Letter of Intent"
         (auto-shortened from compound names; override via cover_title)
      2. Subject / deal description (14pt slate) — e.g. "for AI Infrastructure Distribution"
      3. Date (11pt, document-level)
      4. Party blocks — legal name, address, registration (binding only)
      5. Metadata — reference, version, classification
    """
    # Push title down from logo
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(140)
    spacer.paragraph_format.space_after = Pt(0)

    # 1. Agreement type
    tp = doc.add_paragraph()
    tp.paragraph_format.space_before = Pt(8)
    tp.paragraph_format.space_after = Pt(4)
    displayed_title = cover_title if cover_title else _cover_title(agreement_type)
    _run(tp, displayed_title, size=Pt(28), color=SLATE_900, bold=True)

    # 2. Subject / deal description
    if subject:
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(2)
        sp.paragraph_format.space_after = Pt(0)
        _run(sp, subject, size=Pt(14), color=SLATE)

    # 3. Date (document-level, below title block)
    if date_str:
        dp = doc.add_paragraph()
        dp.paragraph_format.space_before = Pt(16)
        dp.paragraph_format.space_after = Pt(0)
        _run(dp, date_str, size=Pt(11), color=SLATE_900)

    # 4. Party blocks
    if parties:
        # Determine labels
        if party_labels is None:
            if formality == "binding":
                party_labels = ["By and between:"] + ["And:"] * (len(parties) - 1)
            else:
                party_labels = ["Between:"] + ["And:"] * (len(parties) - 1)
        # Pad labels if fewer than parties
        while len(party_labels) < len(parties):
            party_labels.append("And:")

        ps = doc.add_paragraph()
        ps.paragraph_format.space_before = Pt(40)
        ps.paragraph_format.space_after = Pt(0)

        for i, party in enumerate(parties):
            # Party label
            lp = doc.add_paragraph()
            lp.paragraph_format.space_before = Pt(12) if i > 0 else Pt(0)
            lp.paragraph_format.space_after = Pt(2)
            _run(lp, party_labels[i], size=Pt(10), color=SLATE)

            # Legal name
            np = doc.add_paragraph()
            np.paragraph_format.space_before = Pt(0)
            np.paragraph_format.space_after = Pt(0)
            _run(np, party.legal_name, size=Pt(11), color=SLATE_900, bold=True)

            # Address (skip empty — prevents blank paragraph for investor-style covers)
            if party.address and party.address.strip():
                ap = doc.add_paragraph()
                ap.paragraph_format.space_before = Pt(0)
                ap.paragraph_format.space_after = Pt(0)
                _run(ap, party.address, size=Pt(10), color=SLATE_900)

            # Registration (binding only)
            if formality == "binding" and party.registration_type and party.registration_number:
                rp = doc.add_paragraph()
                rp.paragraph_format.space_before = Pt(0)
                rp.paragraph_format.space_after = Pt(0)
                _run(rp, f"{party.registration_type}: ", size=Pt(10), color=SLATE_900, bold=True)
                _run(rp, party.registration_number, size=Pt(10), color=SLATE_900)

            # Parent company
            if party.parent:
                pp = doc.add_paragraph()
                pp.paragraph_format.space_before = Pt(0)
                pp.paragraph_format.space_after = Pt(0)
                _run(pp, f"a subsidiary of {party.parent}", size=Pt(9), color=SLATE, italic=True)

    # 5. Metadata
    meta_items = []
    if reference:
        meta_items.append(("Reference", reference))
    if version is not None:
        meta_items.append(("Version", f"v{version}"))
    if classification:
        meta_items.append(("Classification", classification))

    if meta_items:
        ms = doc.add_paragraph()
        ms.paragraph_format.space_before = Pt(40)
        ms.paragraph_format.space_after = Pt(0)
        for key, val in meta_items:
            mp = doc.add_paragraph()
            mp.paragraph_format.space_before = Pt(2)
            mp.paragraph_format.space_after = Pt(2)
            _run(mp, f"{key}:  ", size=Pt(10), color=SLATE, bold=True)
            _run(mp, str(val), size=Pt(10), color=SLATE_900)

    doc.add_page_break()


def add_section(doc, title, guidance, level=2):
    """Section heading + italic guidance text."""
    sizes = {1: Pt(24), 2: Pt(18), 3: Pt(14), 4: Pt(12)}
    hp = doc.add_paragraph()
    hp.paragraph_format.space_before = Pt(14) if level <= 2 else Pt(8)
    hp.paragraph_format.space_after = Pt(6)
    hp.paragraph_format.keep_with_next = True
    _run(hp, title, size=sizes.get(level, Pt(12)), color=SLATE_900, bold=True)

    gp = doc.add_paragraph()
    gp.paragraph_format.space_before = Pt(0)
    gp.paragraph_format.space_after = Pt(8)
    _run(gp, guidance, size=Pt(11), color=SLATE, italic=True)


def _compute_col_widths(headers, rows, avail_emu):
    """Compute proportional column widths based on content length."""
    ncols = len(headers)
    # Weight = max character length across header + all rows for each column
    weights = []
    for j in range(ncols):
        max_len = len(headers[j])
        for row in rows:
            if j < len(row):
                max_len = max(max_len, len(str(row[j])))
        weights.append(max(max_len, 3))  # minimum weight 3
    total = sum(weights)
    return [int(avail_emu * w / total) for w in weights]


def _insert_element(parent, tag_name, after_tags=()):
    """Insert a new child element respecting OOXML schema ordering.

    Finds the position after the last occurrence of any element in after_tags,
    or appends at end if none found. Returns the new element.
    """
    new_elem = etree.Element(qn(tag_name))
    insert_idx = 0
    for idx, child in enumerate(parent):
        for at in after_tags:
            if child.tag == qn(at):
                insert_idx = idx + 1
    if insert_idx < len(parent):
        parent.insert(insert_idx, new_elem)
    else:
        parent.append(new_elem)
    return new_elem


def _format_table(table, headers=None, rows=None):
    """IB-grade table formatting: Cobalt header, alternating rows, Slate borders.

    Uses lxml.etree + docx.oxml.ns.qn to set cell properties. Respects OOXML
    element ordering (tcBorders before shd; tblW before tblLayout before tblBorders).
    This is NOT OxmlElement or raw XML string parsing — it works through the
    same lxml tree that python-docx builds internally and is safe on Word for Mac.
    """
    ncols = len(table.columns)
    avail_emu = int(Mm(165))     # page 210mm - 25mm left - 20mm right (in EMU for col widths)
    avail_twips = int(165 / 25.4 * 1440)  # same width in twips (dxa) for tblW

    # Set total table width via tblPr to prevent overflow
    # OOXML tblPr order: tblStyle, tblpPr, tblOverlap, bidiVisual,
    #   tblStyleRowBandSize, tblStyleColBandSize, tblW, jc, tblCellSpacing,
    #   tblInd, tblBorders, shd, tblLayout, tblCellMar, tblLook, ...
    tbl_elem = table._tbl
    tblPr = tbl_elem.find(qn('w:tblPr'))
    if tblPr is None:
        tblPr = etree.SubElement(tbl_elem, qn('w:tblPr'))
        tbl_elem.insert(0, tblPr)

    for tag in ('w:tblW', 'w:tblLayout'):
        existing = tblPr.find(qn(tag))
        if existing is not None:
            tblPr.remove(existing)

    tblW = _insert_element(tblPr, 'w:tblW',
                           after_tags=('w:tblStyle', 'w:tblpPr', 'w:tblOverlap',
                                       'w:bidiVisual', 'w:tblStyleRowBandSize',
                                       'w:tblStyleColBandSize'))
    tblW.set(qn('w:w'), str(avail_twips))
    tblW.set(qn('w:type'), 'dxa')

    tblLayout = _insert_element(tblPr, 'w:tblLayout',
                                after_tags=('w:tblStyle', 'w:tblpPr', 'w:tblOverlap',
                                            'w:bidiVisual', 'w:tblStyleRowBandSize',
                                            'w:tblStyleColBandSize', 'w:tblW', 'w:jc',
                                            'w:tblCellSpacing', 'w:tblInd', 'w:tblBorders',
                                            'w:shd'))
    tblLayout.set(qn('w:type'), 'fixed')

    # Proportional column widths (EMU for python-docx col.width)
    if headers and rows:
        col_widths = _compute_col_widths(headers, rows, avail_emu)
    else:
        col_width = avail_emu // ncols
        col_widths = [col_width] * ncols
    for j, col in enumerate(table.columns):
        col.width = col_widths[j] if j < len(col_widths) else col_widths[-1]

    # OOXML tcPr order: cnfStyle, tcW, gridSpan, hMerge, vMerge,
    #   tcBorders, shd, noWrap, tcMar, textDirection, ...
    for i, row in enumerate(table.rows):
        for cell in row.cells:
            tc = cell._tc
            tcPr = tc.find(qn('w:tcPr'))
            if tcPr is None:
                tcPr = etree.SubElement(tc, qn('w:tcPr'))
                tc.insert(0, tcPr)

            for tag in ('w:tcBorders', 'w:shd'):
                existing = tcPr.find(qn(tag))
                if existing is not None:
                    tcPr.remove(existing)

            # tcBorders FIRST (before shd in OOXML schema)
            tcBorders = _insert_element(tcPr, 'w:tcBorders',
                                        after_tags=('w:cnfStyle', 'w:tcW', 'w:gridSpan',
                                                    'w:hMerge', 'w:vMerge'))
            for edge in ('top', 'left', 'bottom', 'right'):
                b = etree.SubElement(tcBorders, qn('w:{}'.format(edge)))
                b.set(qn('w:val'), 'single')
                b.set(qn('w:sz'), '4')       # 4 eighth-points = 0.5pt
                b.set(qn('w:space'), '0')
                b.set(qn('w:color'), SLATE_300_HEX)

            # shd AFTER tcBorders
            shd = _insert_element(tcPr, 'w:shd',
                                  after_tags=('w:cnfStyle', 'w:tcW', 'w:gridSpan',
                                              'w:hMerge', 'w:vMerge', 'w:tcBorders'))
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            if i == 0:
                shd.set(qn('w:fill'), COBALT_HEX)
            elif i % 2 == 0:
                shd.set(qn('w:fill'), SLATE_50_HEX)
            else:
                shd.set(qn('w:fill'), 'FFFFFF')

            # Cell padding for breathing room
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(3)
                p.paragraph_format.space_after = Pt(3)


def add_table(doc, headers, rows):
    """Branded table: Cobalt header, proportional columns, inline formatting."""
    # Pre-table spacing (12pt gap from preceding text)
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(0)
    pf = spacer.paragraph_format
    pf.space_before = Pt(6)
    pf.space_after = Pt(6)

    tbl = doc.add_table(rows=1 + len(rows), cols=len(headers), style="Table Grid")
    for j, h in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.text = ""
        _run(cell.paragraphs[0], h, size=Pt(10), color=WHITE, bold=True)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = tbl.cell(i + 1, j)
            cell.text = ""
            _add_inline(cell.paragraphs[0], str(val), size=Pt(10), color=SLATE_800)
    _format_table(tbl, headers, rows)

    # Post-table spacing
    spacer2 = doc.add_paragraph()
    spacer2.paragraph_format.space_before = Pt(6)
    spacer2.paragraph_format.space_after = Pt(0)


# ---------------------------------------------------------------------------
# PROFILES
# ---------------------------------------------------------------------------

def profile_letter(title="", date_str="", entity="ag", **kw):
    ent = ENTITY_FOOTERS.get(entity, ENTITY_FOOTERS["ag"])
    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title=title or "Letter")
    setup_first_footer(doc.sections[0], entity=entity)
    setup_cont_footer(doc.sections[0], entity=entity)

    # Return address
    rp = doc.add_paragraph()
    rp.paragraph_format.space_before = Pt(24)
    rp.paragraph_format.space_after = Pt(2)
    r = _run(rp, ent["return_address"], size=Pt(7), color=SLATE)
    r.underline = True

    # Recipient
    for line in ["[Recipient Name]", "[Company Name]", "[Street Address]",
                 "[Postcode] [City]", "[Country]"]:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        _run(p, line, size=Pt(11))

    # Date
    dp = doc.add_paragraph()
    dp.paragraph_format.space_before = Pt(16)
    dp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _run(dp, f"Zug, {date_str}", size=Pt(10))

    # Subject
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(16)
    sp.paragraph_format.space_after = Pt(12)
    _run(sp, "[Subject Line]", size=Pt(11), color=SLATE_900, bold=True)

    # Salutation + body
    _run(doc.add_paragraph(), "Dear [Mr./Ms. Last Name],", size=Pt(11))

    bp = doc.add_paragraph()
    bp.paragraph_format.line_spacing = Pt(16.5)
    _run(bp, "[Letter body text. DIN 5008 Form B compliant for windowed envelopes.]", size=Pt(11))

    # Closing
    cp = doc.add_paragraph()
    cp.paragraph_format.space_before = Pt(18)
    _run(cp, "Kind regards,", size=Pt(11))

    sig = doc.add_paragraph()
    sig.paragraph_format.space_before = Pt(36)
    _run(sig, "[Name]", size=Pt(11), bold=True)
    _run(doc.add_paragraph(), "[Title]", size=Pt(11), color=SLATE)
    _run(doc.add_paragraph(), ent["legal_name"], size=Pt(11), color=SLATE)

    return doc


def profile_agreement(agreement_type="[Agreement Type]", subject=None,
                      client="[Counterparty]", client_address=None,
                      client_reg_type=None, client_reg_number=None,
                      date_str="", version=1, formality=None,
                      entity="ag", title=None, cover_title=None, reference=None, **kw):
    # Backward compat: --title maps to agreement_type
    if title and agreement_type == "[Agreement Type]":
        agreement_type = title

    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title=_cover_title(agreement_type))
    setup_first_footer(doc.sections[0], classification="Confidential", entity=entity)
    setup_cont_footer(doc.sections[0], classification="Confidential", entity=entity)

    # Auto-detect formality from agreement type
    if formality is None:
        formality = _detect_formality(agreement_type)

    # Build party list
    de_party = DE_ENTITIES.get(entity, DE_ENTITIES["ag"])
    counterparty = Party(
        legal_name=client,
        address=client_address or "[Address]",
        registration_type=client_reg_type,
        registration_number=client_reg_number,
    )

    add_cover(doc,
              agreement_type=agreement_type,
              subject=subject,
              date_str=date_str,
              parties=[de_party, counterparty],
              formality=formality,
              reference=reference or "[DE-AGR-YYYY-NNN]",
              version=version,
              classification="Confidential",
              cover_title=cover_title)

    gp = doc.add_paragraph()
    gp.paragraph_format.line_spacing = Pt(16.5)
    _run(gp, "[Agreement content begins here. Replace with agreement body.]",
         size=Pt(11), color=SLATE, italic=True)

    return doc


SEED_SECTIONS = [
    ("1. Company Overview",
     "One paragraph: what DE does, where, for whom. Founding date, HQ, one-sentence positioning."),
    ("2. Problem",
     "Grid scarcity (60 GW queue vs 20 GW peak), stranded greenhouse heat (30-50% gas costs), no sovereign EU AI compute. Use 2-3 sourced data points."),
    ("3. Solution",
     "How DECs solve it. 'One Watt, Three Jobs': compute + heat + grid flexibility. Co-location on existing grid connections, 97% energy recycling."),
    ("4. Business Model",
     "Four revenue streams: colocation, heat sales, BESS/flexibility, development fees. DevCo recycling model. Include unit economics table."),
    ("5. Market Opportunity",
     "TAM/SAM/SOM. European AI compute demand, Dutch grid-constrained supply, greenhouse heat market (EUR 2.8B energy spend)."),
    ("6. Traction",
     "14 sites, 600 MW grid infrastructure, partnerships (Lenovo, Nokia, Ampower), Fonti 4 months from FID, PowerGrow 12 months."),
    ("7. Team",
     "Core team with infrastructure, energy, and technology credentials. Board/advisors if notable."),
    ("8. The Ask",
     "Round size, instrument (SAFE/note), valuation cap, use of proceeds breakdown, timeline to close."),
]


def profile_seed_memo(client="[Investor Name]", date_str="", version=1, entity="ag", **kw):
    de_party = DE_ENTITIES.get(entity, DE_ENTITIES["ag"])
    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title="Seed Investment Memo")
    setup_first_footer(doc.sections[0], classification="Confidential", entity=entity)
    setup_cont_footer(doc.sections[0], classification="Confidential", entity=entity)

    add_cover(doc,
              agreement_type="Seed Investment Memo",
              subject="Sovereign AI Infrastructure for Europe",
              date_str=date_str,
              parties=[
                  de_party,
                  Party(legal_name=client, address=""),
              ],
              party_labels=["Prepared by:", "Prepared for:"],
              formality="non_binding",
              version=version,
              classification="Confidential")

    for sect_title, guidance in SEED_SECTIONS:
        add_section(doc, sect_title, guidance)

    return doc


IM_SECTIONS = [
    ("1. Executive Overview",
     "One-page standalone summary: investment thesis, key metrics, round details, why now."),
    ("2. Asset Overview",
     "DEC architecture: modular 4.2 MW, liquid cooling (40-140 kW/rack, PUE 1.2), heat integration, BESS, Super-Factory concept."),
    ("3. Market Dynamics",
     "EU AI compute demand, Dutch grid congestion (60 GW queue), Wcw regulation, SDE++ subsidies, restwarmteplicht."),
    ("4. Business Model",
     "Four fee streams: colocation (EUR/kW/month), heat (EUR/MWh + CPI), BESS, development fees. DevCo/HoldCo recycling. AG structure."),
    ("5. Pipeline & Traction",
     "14 sites, 600 MW, 12M m\u00b2 greenhouse area. Pipeline table: site, location, MW, status, target FID. Lead projects: Fonti, PowerGrow."),
    ("6. Unit Economics",
     "Per-DEC: CAPEX/MW, revenue/MW, EBITDA margin, payback, IRR. Three scenarios (conservative/base/optimistic). Source: FM v3.51."),
    ("7. Risk Factors",
     "Grid/DSO, permitting, technology, market, regulatory, execution risks. Each with probability, impact, mitigant."),
    ("8. Financial Projections",
     "3-5 year projections: revenue, EBITDA, cash flow, CAPEX, net debt. Three scenarios. Key assumptions stated."),
    ("9. Capital Structure",
     "Current cap table, round terms, use of proceeds breakdown, pro forma post-raise."),
    ("10. Appendix",
     "Site profiles, FM v3.51 outputs, team bios, glossary (Wcw, SDE++, transportschaarste, omgevingsvergunning, recht van opstal)."),
]


def profile_investor_memo(client="[Investor Name]", date_str="", version=1, entity="ag", **kw):
    de_party = DE_ENTITIES.get(entity, DE_ENTITIES["ag"])
    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title="Investment Memorandum")
    setup_first_footer(doc.sections[0], classification="Confidential", entity=entity)
    setup_cont_footer(doc.sections[0], classification="Confidential", entity=entity)

    add_cover(doc,
              agreement_type="Investment Memorandum",
              subject="European Sovereign AI Infrastructure",
              date_str=date_str,
              parties=[
                  de_party,
                  Party(legal_name=client, address=""),
              ],
              party_labels=["Prepared by:", "Prepared for:"],
              formality="non_binding",
              version=version,
              classification="Confidential")

    for sect_title, guidance in IM_SECTIONS:
        add_section(doc, sect_title, guidance)

    return doc


def profile_exec_summary(title="[Executive Summary]", date_str="", entity="ag", **kw):
    doc = new_doc(top=Mm(15), bottom=Mm(25))
    setup_cont_header(doc.sections[0], title=title)
    setup_cont_footer(doc.sections[0], entity=entity)

    # Title
    tp = doc.add_paragraph()
    tp.paragraph_format.space_before = Pt(4)
    tp.paragraph_format.space_after = Pt(2)
    _run(tp, title, size=Pt(24), color=SLATE_900, bold=True)

    _run(doc.add_paragraph(), date_str, size=Pt(10), color=SLATE)

    # Metrics placeholder
    add_table(doc,
              ["[Metric 1]", "[Metric 2]", "[Metric 3]"],
              [["[Value]", "[Value]", "[Value]"]])

    add_section(doc, "Context",
                "[Why this document exists. 2-3 sentences setting the scene.]")
    add_section(doc, "Key Findings",
                "[3-5 numbered findings, each 1-2 sentences. Lead with conclusion, then evidence.]")

    doc.add_page_break()

    add_section(doc, "Analysis",
                "[Supporting detail. Can include a summary table.]")
    add_section(doc, "Recommendation",
                "[What to do, by when, who owns it. 3-5 sentences max.]")
    add_section(doc, "Next Steps",
                "[3-5 numbered action items: action + owner + deadline.]")

    return doc


# ---------------------------------------------------------------------------
# MARKDOWN CONVERTER
# ---------------------------------------------------------------------------

def md_to_docx(md_text, title=None, client=None, date_str=None, cover=False,
               entity="ag", subject=None, formality=None):
    """Convert markdown to branded docx.

    Args:
        formality: "binding" or "non_binding". If None, auto-detects from
                   AGREEMENT_FORMALITY dict using title, defaulting to "non_binding".
        subject: Cover page subtitle (e.g. "Chairman, Horticulture Advisory Board").
    """
    has_cover = cover and title
    doc = new_doc(diff_first=has_cover)

    if has_cover:
        setup_first_page_header(doc.sections[0])
        setup_cont_header(doc.sections[0], title=_cover_title(title))
        setup_first_footer(doc.sections[0], entity=entity)
        setup_cont_footer(doc.sections[0], entity=entity)
        de_party = DE_ENTITIES.get(entity, DE_ENTITIES["ag"])
        parties = [de_party]
        if client:
            parties.append(Party(legal_name=client, address=""))
        if formality is None:
            formality = _detect_formality(title)
        add_cover(doc,
                  agreement_type=title,
                  subject=subject,
                  date_str=date_str,
                  parties=parties,
                  party_labels=["Prepared by:", "Prepared for:"] if client else None,
                  formality=formality)
    else:
        setup_cont_header(doc.sections[0], title=title or "")
        setup_cont_footer(doc.sections[0], entity=entity)

    heading_sizes = {1: Pt(24), 2: Pt(18), 3: Pt(14), 4: Pt(12), 5: Pt(11), 6: Pt(11)}

    lines = md_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # Heading
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(18) if level <= 2 else Pt(12)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            _add_inline(p, m.group(2).strip(), size=heading_sizes.get(level, Pt(11)),
                        color=SLATE_900, bold=True)
            i += 1
            continue

        # HR
        if re.match(r'^[-*_]{3,}\s*$', line):
            i += 1
            continue

        # Unordered list — native Word bullet style
        if re.match(r'^[\s]*[-*+]\s+', line):
            first = True
            while i < len(lines) and re.match(r'^[\s]*[-*+]\s+', lines[i]):
                text = re.sub(r'^[\s]*[-*+]\s+', '', lines[i]).strip()
                p = doc.add_paragraph(style='List Bullet')
                if first:
                    p.paragraph_format.space_before = Pt(6)
                    first = False
                else:
                    p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                _add_inline(p, text)
                i += 1
            # Space after last item
            if p:
                p.paragraph_format.space_after = Pt(6)
            continue

        # Ordered list — native Word numbered style
        if re.match(r'^[\s]*\d+[.)]\s+', line):
            first = True
            while i < len(lines) and re.match(r'^[\s]*\d+[.)]\s+', lines[i]):
                text = re.sub(r'^[\s]*\d+[.)]\s+', '', lines[i]).strip()
                p = doc.add_paragraph(style='List Number')
                if first:
                    p.paragraph_format.space_before = Pt(6)
                    first = False
                else:
                    p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                _add_inline(p, text)
                i += 1
            # Space after last item
            if p:
                p.paragraph_format.space_after = Pt(6)
            continue

        # Table
        if '|' in line and i + 1 < len(lines) and re.match(r'^[\s]*\|?[\s]*[-:]', lines[i + 1]):
            headers = [c.strip() for c in line.strip().strip('|').split('|')]
            i += 2
            rows = []
            while i < len(lines) and '|' in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            add_table(doc, headers, rows)
            continue

        # Blockquote
        if line.startswith('>'):
            parts = []
            while i < len(lines) and lines[i].startswith('>'):
                parts.append(lines[i].lstrip('>').strip())
                i += 1
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Mm(10)
            _run(p, ' '.join(parts), size=Pt(11), color=SLATE, italic=True)
            continue

        # Signature block detection: lines with ___ or "Name:"/"Title:"/"Signature:"/"Date:"
        # Keep all signature-related paragraphs together on one page
        sig_pattern = re.compile(r'^(_{3,}|.*\b(Name|Title|Signature|Date|Signed|By)\s*:)', re.IGNORECASE)
        if sig_pattern.match(line):
            sig_lines = []
            while i < len(lines) and (sig_pattern.match(lines[i]) or not lines[i].strip()):
                if lines[i].strip():
                    sig_lines.append(lines[i])
                i += 1
            # Also grab trailing non-blank lines that look like signature content
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('#'):
                if sig_pattern.match(lines[i]) or len(lines[i].strip()) < 60:
                    sig_lines.append(lines[i])
                    i += 1
                else:
                    break
            for idx, sl in enumerate(sig_lines):
                p = doc.add_paragraph()
                p.paragraph_format.keep_together = True
                p.paragraph_format.keep_with_next = (idx < len(sig_lines) - 1)
                if idx == 0:
                    p.paragraph_format.space_before = Pt(24)
                else:
                    p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                _add_inline(p, sl.strip())
            continue

        # Paragraph
        para_lines = []
        while (i < len(lines) and lines[i].strip()
               and not lines[i].startswith('#')
               and not re.match(r'^[-*_]{3,}\s*$', lines[i])):
            para_lines.append(lines[i])
            i += 1
        if para_lines:
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = Pt(16.5)
            p.paragraph_format.space_after = Pt(6)
            _add_inline(p, ' '.join(para_lines))
            continue

        i += 1

    return doc


def _add_inline(para, text, size=Pt(11), color=SLATE_800, bold=False):
    """Add text with **bold**, *italic*, `code` inline formatting."""
    for part in re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)', text):
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            _run(para, part[2:-2], size=size, color=color, bold=True)
        elif part.startswith('*') and part.endswith('*'):
            _run(para, part[1:-1], size=size, color=color, italic=True)
        elif part.startswith('`') and part.endswith('`'):
            _run(para, part[1:-1], size=Pt(10), color=color, font="JetBrains Mono")
        else:
            _run(para, part, size=size, color=color, bold=bold)


# ---------------------------------------------------------------------------
# PDF CONVERSION (Microsoft Word via docx2pdf)
# ---------------------------------------------------------------------------

def docx_to_pdf(docx_path, pdf_path=None):
    """Convert .docx → .pdf via Microsoft Word (docx2pdf).

    Word is the canonical .docx renderer on the team's machines.
    On macOS this uses AppleScript automation; on Windows, COM.
    No fallback — if Word is unavailable, raises RuntimeError with
    install instructions.

    Returns the output PDF path on success.
    """
    docx_path = os.path.abspath(docx_path)
    if not os.path.exists(docx_path):
        raise FileNotFoundError(docx_path)
    if pdf_path is None:
        pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
    pdf_path = os.path.abspath(pdf_path)

    try:
        from docx2pdf import convert as _word_convert
    except ImportError:
        raise RuntimeError(
            "docx2pdf not installed. Run: pip install docx2pdf\n"
            "Also ensure Microsoft Word is installed (macOS: Office 365; Windows: Office)."
        )

    try:
        _word_convert(docx_path, pdf_path)
    except Exception as e:
        raise RuntimeError(
            f"Word conversion failed: {e}\n"
            "Verify Microsoft Word is installed and, on macOS, that AppleScript is permitted."
        )

    if not os.path.exists(pdf_path):
        raise RuntimeError("docx2pdf ran but produced no output file.")
    return pdf_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

PROFILES = {
    "letter": profile_letter,
    "agreement": profile_agreement,
    "seed_memo": profile_seed_memo,
    "investor_memo": profile_investor_memo,
    "exec_summary": profile_exec_summary,
}


def _run_validate(docx_path):
    """Run office_bridge validation if available."""
    try:
        from office_bridge import OfficeBridge
        bridge = OfficeBridge()
        result = bridge.validate(docx_path)
        print(f"Validate:  {result.strip()}")
    except ImportError:
        print("Validate:  skipped (office_bridge not available)", file=sys.stderr)
    except Exception as e:
        print(f"Validate:  FAILED — {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Generate branded DE documents")
    parser.add_argument("--profile", choices=list(PROFILES.keys()),
                       help="Document profile")
    parser.add_argument("--title", default=None,
                       help="DEPRECATED for agreement profile; use --agreement-type. Still valid for other profiles.")
    parser.add_argument("--agreement-type", default=None,
                       help="Agreement type name (e.g. 'Letter of Intent', 'Master Service Agreement')")
    parser.add_argument("--cover-title", default=None,
                       help="Override cover-page title (28pt). Defaults to auto-shortened agreement-type")
    parser.add_argument("--reference", default=None,
                       help="Document reference (e.g. 'DE-AGR-2026-001'). Defaults to placeholder")
    parser.add_argument("--subject", default=None,
                       help="Deal description sub-header (e.g. 'for AI Infrastructure Distribution')")
    parser.add_argument("--client", default=None)
    parser.add_argument("--client-address", default=None, help="Counterparty address")
    parser.add_argument("--client-reg-type", default=None, help="Registration type (KvK, CHE, EIN)")
    parser.add_argument("--client-reg-number", default=None, help="Registration number")
    parser.add_argument("--entity", choices=list(DE_ENTITIES.keys()), default="ag",
                       help="DE contracting entity (default: ag)")
    parser.add_argument("--formality", choices=["binding", "non_binding"], default=None,
                       help="Override formality auto-detection")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD")
    parser.add_argument("--version", type=int, default=1)
    parser.add_argument("--output", default=None)
    parser.add_argument("--dotx", action="store_true")
    parser.add_argument("--pdf", action="store_true",
                       help="Also produce a PDF via Microsoft Word")
    parser.add_argument("--validate", action="store_true",
                       help="Validate .docx via office_bridge after generation")
    parser.add_argument("--strip-review", action="store_true",
                       help="Strip [REVIEW REQUIRED] markers from output (md mode)")
    # Markdown mode
    parser.add_argument("--md", default=None, help="Input markdown file")
    parser.add_argument("--cover", action="store_true", help="Add cover page to md output")

    args = parser.parse_args()

    if args.date:
        dt = datetime.strptime(args.date, "%Y-%m-%d").date()
    else:
        dt = date.today()
    date_str = dt.strftime("%d %B %Y").lstrip("0")  # Cross-platform (no %-d)

    os.makedirs(OUTPUT, exist_ok=True)

    # Markdown mode
    if args.md:
        if not os.path.exists(args.md):
            print(f"Error: {args.md} not found")
            sys.exit(1)
        with open(args.md, 'r') as f:
            md_text = f.read()
        if args.strip_review:
            md_text, n_stripped = re.subn(r'\[REVIEW REQUIRED[^\]]*\]', '', md_text)
            if n_stripped:
                print(f"Stripped:  {n_stripped} [REVIEW REQUIRED] marker(s)", file=sys.stderr)
        doc = md_to_docx(md_text, title=args.title, client=args.client,
                         date_str=date_str, cover=args.cover, entity=args.entity,
                         subject=args.subject, formality=args.formality)
        out = args.output or os.path.join(OUTPUT, "md_output.docx")
        save_doc(doc, out)
        print(f"Saved: {out}")
        if args.validate:
            _run_validate(out)
        if args.pdf:
            try:
                pdf = docx_to_pdf(out)
                print(f"PDF:   {pdf}")
            except RuntimeError as e:
                print(f"PDF conversion failed: {e}", file=sys.stderr)
                sys.exit(1)
        return

    # Profile mode
    if not args.profile:
        parser.error("--profile or --md required")

    fn = PROFILES[args.profile]
    kwargs = {"date_str": date_str, "version": args.version}

    # Agreement profile uses new structured flags
    if args.profile == "agreement":
        agreement_type = args.agreement_type or args.title or "[Agreement Type]"
        kwargs["agreement_type"] = agreement_type
        kwargs["subject"] = args.subject
        kwargs["entity"] = args.entity
        if getattr(args, "cover_title", None):
            kwargs["cover_title"] = args.cover_title
        if getattr(args, "reference", None):
            kwargs["reference"] = args.reference
        if args.client:
            kwargs["client"] = args.client
        if getattr(args, "client_address", None):
            kwargs["client_address"] = args.client_address
        if getattr(args, "client_reg_type", None):
            kwargs["client_reg_type"] = args.client_reg_type
        if getattr(args, "client_reg_number", None):
            kwargs["client_reg_number"] = args.client_reg_number
        if args.formality:
            kwargs["formality"] = args.formality
    else:
        if args.title:
            kwargs["title"] = args.title
        if args.client:
            kwargs["client"] = args.client
        if args.profile in ("letter", "seed_memo", "investor_memo", "exec_summary"):
            kwargs["entity"] = args.entity

    doc = fn(**kwargs)

    if args.output:
        out = args.output
    else:
        out = os.path.join(OUTPUT, auto_name(
            args.profile, args.client, args.version, dt,
            agreement_type=kwargs.get("agreement_type")))

    save_doc(doc, out)
    print(f"Generated: {out}")

    if args.validate:
        _run_validate(out)

    if args.dotx:
        dotx = out.replace(".docx", ".dotx")
        save_doc(doc, dotx)
        print(f"Template:  {dotx}")

    if args.pdf:
        try:
            pdf = docx_to_pdf(out)
            print(f"PDF:       {pdf}")
        except RuntimeError as e:
            print(f"PDF conversion failed: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
