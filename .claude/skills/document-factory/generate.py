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
from datetime import datetime, date

try:
    from docx import Document
    from docx.shared import Mm, Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
except ImportError:
    print("Error: python-docx is required. Install with: pip install python-docx")
    sys.exit(1)

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

ENTITY = {
    "legal_name": "Digital Energy Group AG",
    "address": "Baarerstrasse 43, 6300 Zug, Switzerland",
    "registration": "CHE-408.639.320",
    "website": "digital-energy.group",
    "return_address": "Digital Energy Group AG  \u2022  Baarerstrasse 43  \u2022  6300 Zug",
}

FONT = "Inter"
FONT_FALLBACK = "Arial"
COBALT = RGBColor(0x00, 0x34, 0xAF)
DARK = RGBColor(0x14, 0x29, 0x45)
BODY_COLOR = RGBColor(0x1E, 0x29, 0x3B)
SLATE = RGBColor(0x64, 0x74, 0x8B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(SCRIPT_DIR, "assets", "DE_Logo_Black.png")
if not os.path.exists(LOGO):
    # Fallback: check script directory root
    LOGO = os.path.join(SCRIPT_DIR, "DE_Logo_Black.png")
OUTPUT = os.path.join(SCRIPT_DIR, "output")

PROFILE_CODES = {
    "letter": "Letter",
    "agreement": "Agreement",
    "seed_memo": "Seed_Memo",
    "investor_memo": "Investor_Memo",
    "exec_summary": "Exec_Summary",
}

FOOTER_TEXT = "  |  ".join([
    ENTITY["legal_name"],
    ENTITY["address"],
    ENTITY["registration"],
    ENTITY["website"],
])


def auto_name(profile, client=None, version=1, dt=None):
    if dt is None:
        dt = date.today()
    parts = [dt.strftime("%Y%m%d"), "DE", PROFILE_CODES.get(profile, profile)]
    if client:
        parts.append(client.replace(" ", "_")[:30])
    parts.append(f"v{version}")
    return "_".join(parts) + ".docx"


# ---------------------------------------------------------------------------
# BUILDING BLOCKS (no OxmlElement, no raw XML)
# ---------------------------------------------------------------------------

def _run(para, text, size=Pt(11), color=BODY_COLOR, bold=False, italic=False, font=FONT):
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


def setup_footer(footer, classification=None):
    """Footer: entity details left, page number right."""
    p = footer.paragraphs[0]
    p.paragraph_format.tab_stops.add_tab_stop(Mm(165), WD_TAB_ALIGNMENT.RIGHT)
    prefix = f"{classification}    " if classification else ""
    r = p.add_run(prefix + FOOTER_TEXT)
    r.font.size = Pt(8)
    r.font.name = FONT
    r.font.color.rgb = SLATE


def setup_first_footer(section, classification=None):
    f = section.first_page_footer
    f.is_linked_to_previous = False
    setup_footer(f, classification)


def setup_cont_footer(section, classification=None):
    f = section.footer
    f.is_linked_to_previous = False
    setup_footer(f, classification)


def add_cover(doc, title, subtitle=None, metadata=None):
    """Clean white cover page."""
    # Push title down
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(160)
    spacer.paragraph_format.space_after = Pt(0)

    # Title
    tp = doc.add_paragraph()
    tp.paragraph_format.space_before = Pt(8)
    tp.paragraph_format.space_after = Pt(4)
    _run(tp, title, size=Pt(28), color=DARK, bold=True)

    # Subtitle
    if subtitle:
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(0)
        _run(sp, subtitle, size=Pt(14), color=SLATE)

    # Metadata
    if metadata:
        ms = doc.add_paragraph()
        ms.paragraph_format.space_before = Pt(80)
        ms.paragraph_format.space_after = Pt(0)
        for key, val in metadata.items():
            mp = doc.add_paragraph()
            mp.paragraph_format.space_before = Pt(2)
            mp.paragraph_format.space_after = Pt(2)
            _run(mp, f"{key}:  ", size=Pt(10), color=SLATE, bold=True)
            _run(mp, str(val), size=Pt(10), color=DARK)

    doc.add_page_break()


def add_section(doc, title, guidance, level=2):
    """Section heading + italic guidance text."""
    sizes = {1: Pt(24), 2: Pt(18), 3: Pt(14), 4: Pt(12)}
    hp = doc.add_paragraph()
    hp.paragraph_format.space_before = Pt(14) if level <= 2 else Pt(8)
    hp.paragraph_format.space_after = Pt(6)
    hp.paragraph_format.keep_with_next = True
    _run(hp, title, size=sizes.get(level, Pt(12)), color=DARK, bold=True)

    gp = doc.add_paragraph()
    gp.paragraph_format.space_before = Pt(0)
    gp.paragraph_format.space_after = Pt(8)
    _run(gp, guidance, size=Pt(11), color=SLATE, italic=True)


def add_table(doc, headers, rows):
    """Branded table with dark header."""
    tbl = doc.add_table(rows=1 + len(rows), cols=len(headers), style="Table Grid")
    for j, h in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.text = ""
        _run(cell.paragraphs[0], h, size=Pt(9), color=WHITE, bold=True)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = tbl.cell(i + 1, j)
            cell.text = ""
            _run(cell.paragraphs[0], str(val), size=Pt(9), color=BODY_COLOR)


# ---------------------------------------------------------------------------
# PROFILES
# ---------------------------------------------------------------------------

def profile_letter(title="", date_str="", **kw):
    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title=title or "Letter")
    setup_first_footer(doc.sections[0])
    setup_cont_footer(doc.sections[0])

    # Return address
    rp = doc.add_paragraph()
    rp.paragraph_format.space_before = Pt(24)
    rp.paragraph_format.space_after = Pt(2)
    r = _run(rp, ENTITY["return_address"], size=Pt(7), color=SLATE)
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
    _run(sp, "[Subject Line]", size=Pt(11), color=DARK, bold=True)

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
    _run(doc.add_paragraph(), ENTITY["legal_name"], size=Pt(11), color=SLATE)

    return doc


def profile_agreement(title="[Agreement Title]", client="[Counterparty]",
                      date_str="", version=1, **kw):
    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title=title)
    setup_first_footer(doc.sections[0], classification="Confidential")
    setup_cont_footer(doc.sections[0], classification="Confidential")

    add_cover(doc, title=title,
              subtitle=f"Between {ENTITY['legal_name']} and {client}",
              metadata={
                  "Parties": f"{ENTITY['legal_name']}  /  {client}",
                  "Date": date_str,
                  "Reference": "[DE-AGR-YYYY-NNN]",
                  "Version": f"v{version}",
                  "Classification": "Confidential",
              })

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


def profile_seed_memo(client="[Investor Name]", date_str="", version=1, **kw):
    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title="Seed Investment Memo")
    setup_first_footer(doc.sections[0], classification="Confidential")
    setup_cont_footer(doc.sections[0], classification="Confidential")

    add_cover(doc, title="Seed Investment Memo",
              subtitle="Sovereign AI Infrastructure for Europe",
              metadata={
                  "Prepared for": client,
                  "Prepared by": ENTITY["legal_name"],
                  "Date": date_str,
                  "Version": f"v{version}",
                  "Classification": "Confidential",
              })

    for title, guidance in SEED_SECTIONS:
        add_section(doc, title, guidance)

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


def profile_investor_memo(client="[Investor Name]", date_str="", version=1, **kw):
    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title="Investment Memorandum")
    setup_first_footer(doc.sections[0], classification="Confidential")
    setup_cont_footer(doc.sections[0], classification="Confidential")

    add_cover(doc, title="Investment Memorandum",
              subtitle="European Sovereign AI Infrastructure",
              metadata={
                  "Prepared for": client,
                  "Prepared by": ENTITY["legal_name"],
                  "Date": date_str,
                  "Version": f"v{version}",
                  "Classification": "Confidential",
              })

    for title, guidance in IM_SECTIONS:
        add_section(doc, title, guidance)

    return doc


def profile_exec_summary(title="[Executive Summary]", date_str="", **kw):
    doc = new_doc(top=Mm(15), bottom=Mm(25))
    setup_cont_header(doc.sections[0], title=title)
    setup_cont_footer(doc.sections[0])

    # Title
    tp = doc.add_paragraph()
    tp.paragraph_format.space_before = Pt(4)
    tp.paragraph_format.space_after = Pt(2)
    _run(tp, title, size=Pt(24), color=DARK, bold=True)

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

def md_to_docx(md_text, title=None, client=None, date_str=None, cover=False):
    """Convert markdown to branded docx."""
    has_cover = cover and title
    doc = new_doc(diff_first=has_cover)

    if has_cover:
        setup_first_page_header(doc.sections[0])
        setup_cont_header(doc.sections[0], title=title)
        setup_first_footer(doc.sections[0])
        setup_cont_footer(doc.sections[0])
        meta = {}
        if client:
            meta["Prepared for"] = client
        meta["Prepared by"] = ENTITY["legal_name"]
        if date_str:
            meta["Date"] = date_str
        add_cover(doc, title=title, metadata=meta)
    else:
        setup_cont_header(doc.sections[0], title=title or "")
        setup_cont_footer(doc.sections[0])

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
            p.paragraph_format.space_before = Pt(14) if level <= 2 else Pt(8)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            _add_inline(p, m.group(2).strip(), size=heading_sizes.get(level, Pt(11)),
                        color=DARK, bold=True)
            i += 1
            continue

        # HR
        if re.match(r'^[-*_]{3,}\s*$', line):
            i += 1
            continue

        # Unordered list
        if re.match(r'^[\s]*[-*+]\s+', line):
            while i < len(lines) and re.match(r'^[\s]*[-*+]\s+', lines[i]):
                text = re.sub(r'^[\s]*[-*+]\s+', '', lines[i]).strip()
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Mm(5)
                _run(p, "\u2022  ", size=Pt(11), color=COBALT)
                _add_inline(p, text)
                i += 1
            continue

        # Ordered list
        if re.match(r'^[\s]*\d+[.)]\s+', line):
            n = 1
            while i < len(lines) and re.match(r'^[\s]*\d+[.)]\s+', lines[i]):
                text = re.sub(r'^[\s]*\d+[.)]\s+', '', lines[i]).strip()
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Mm(5)
                _run(p, f"{n}.  ", size=Pt(11), color=COBALT)
                _add_inline(p, text)
                n += 1
                i += 1
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
            _add_inline(p, ' '.join(para_lines))
            continue

        i += 1

    return doc


def _add_inline(para, text, size=Pt(11), color=BODY_COLOR, bold=False):
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
# CLI
# ---------------------------------------------------------------------------

PROFILES = {
    "letter": profile_letter,
    "agreement": profile_agreement,
    "seed_memo": profile_seed_memo,
    "investor_memo": profile_investor_memo,
    "exec_summary": profile_exec_summary,
}


def main():
    parser = argparse.ArgumentParser(description="Generate branded DE documents")
    parser.add_argument("--profile", choices=list(PROFILES.keys()),
                       help="Document profile")
    parser.add_argument("--title", default=None)
    parser.add_argument("--client", default=None)
    parser.add_argument("--date", default=None, help="YYYY-MM-DD")
    parser.add_argument("--version", type=int, default=1)
    parser.add_argument("--output", default=None)
    parser.add_argument("--dotx", action="store_true")
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
        doc = md_to_docx(md_text, title=args.title, client=args.client,
                         date_str=date_str, cover=args.cover)
        out = args.output or os.path.join(OUTPUT, "md_output.docx")
        doc.save(out)
        print(f"Saved: {out}")
        return

    # Profile mode
    if not args.profile:
        parser.error("--profile or --md required")

    fn = PROFILES[args.profile]
    kwargs = {"date_str": date_str, "version": args.version}
    if args.title:
        kwargs["title"] = args.title
    if args.client:
        kwargs["client"] = args.client

    doc = fn(**kwargs)

    if args.output:
        out = args.output
    else:
        out = os.path.join(OUTPUT, auto_name(args.profile, args.client, args.version, dt))

    doc.save(out)
    print(f"Generated: {out}")

    if args.dotx:
        dotx = out.replace(".docx", ".dotx")
        doc.save(dotx)
        print(f"Template:  {dotx}")


if __name__ == "__main__":
    main()
