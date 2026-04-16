#!/usr/bin/env python3
"""Automated test suite for Document Factory generate.py.

Tests cover: column widths, table formatting, spacing, lists (bullet/numbered/
alphabetic/roman), signature blocks, cover pages, OOXML compliance, document
properties, and font fallback. All tests generate documents in memory — no
file I/O or Word installation required.

Run: pytest test_generate.py -v
"""

import re
import sys
import os

import pytest
from docx import Document
from docx.shared import Mm, Pt, Emu
from docx.oxml.ns import qn

# Import from generate.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import (
    _compute_col_widths, _display_len, _longest_word_len, _SP,
    _CHAR_WIDTH_EMU, _CELL_PAD_EMU, _MIN_COL_EMU,
    _setup_custom_numbering, _new_list_instance, _apply_numbering,
    _ALPHA_ABSTRACT_ID, _ROMAN_ABSTRACT_ID, _DECIMAL_ABSTRACT_ID, _BULLET_ABSTRACT_ID,
    md_to_docx, new_doc, add_table, add_section, _run, _format_table,
    save_doc, profile_agreement, profile_letter, profile_seed_memo,
    profile_investor_memo, profile_exec_summary, add_cover,
    Party, DE_ENTITIES, COBALT, SLATE_800, SLATE_900, SLATE,
    COBALT_HEX, SLATE_50_HEX, FONT,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_doc(md_text, **kwargs):
    """Shorthand for md_to_docx with common defaults."""
    defaults = dict(title="Test Doc", cover=True, entity="nl")
    defaults.update(kwargs)
    return md_to_docx(md_text, **defaults)


def _para_texts(doc):
    """Return list of (text, style_name) for all paragraphs."""
    return [(p.text, p.style.name if p.style else '') for p in doc.paragraphs]


# ---------------------------------------------------------------------------
# I1. Column Width Tests
# ---------------------------------------------------------------------------

class TestColumnWidths:
    def test_2col_kv_heuristic(self):
        headers = ["Label", "Value"]
        rows = [["Short", "A" * 100]]
        avail = int(Mm(165))
        widths = _compute_col_widths(headers, rows, avail)
        assert widths[0] == int(avail * 0.25)
        assert widths[1] == int(avail * 0.75)

    def test_starved_columns_milestone_table(self):
        """Simulates the Milestone table: one 300-char cell shouldn't starve others."""
        headers = ["Milestone", "Units", "% Pool", "Vesting Trigger", "Sunset", "Certified By"]
        rows = [
            ["GTNL Milestone", "5000", "14%", "A" * 300, "31 Dec 2028", "Management Board"],
        ]
        avail = int(Mm(165))
        widths = _compute_col_widths(headers, rows, avail)
        for j, w in enumerate(widths):
            assert w >= _MIN_COL_EMU, f"Column {j} ({headers[j]}) = {w} EMU < minimum {_MIN_COL_EMU}"

    def test_all_compact_surplus_distributed(self):
        headers = ["A", "B", "C", "D", "E"]
        rows = [["12345", "123", "1234", "12345", "123"]]
        avail = int(Mm(165))
        widths = _compute_col_widths(headers, rows, avail)
        assert sum(widths) == avail
        for w in widths:
            assert w >= _MIN_COL_EMU

    def test_display_len_strips_bold(self):
        assert _display_len("**bold**") == 4
        assert _display_len("*italic*") == 6
        assert _display_len("`code`") == 4
        assert _display_len("plain text") == 10

    def test_longest_word(self):
        assert _longest_word_len("% of Time-Based Tranche") == len("Time-Based")
        assert _longest_word_len("**bold text**") == 4  # "bold" or "text"

    def test_total_equals_available(self):
        headers = ["A", "B", "C", "D"]
        rows = [["short", "medium text here", "A" * 200, "x"]]
        avail = int(Mm(165))
        widths = _compute_col_widths(headers, rows, avail)
        assert abs(sum(widths) - avail) <= 1  # Allow 1 EMU rounding

    def test_overflow_guard(self):
        """8 compact columns exceeding 70% should use proportional fallback."""
        headers = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]
        rows = [["12345678901234567890"] * 8]  # 20-char each = compact
        avail = int(Mm(165))
        widths = _compute_col_widths(headers, rows, avail)
        assert sum(widths) == avail or abs(sum(widths) - avail) <= 1
        for w in widths:
            assert w >= _MIN_COL_EMU


# ---------------------------------------------------------------------------
# I2. Table Formatting Tests
# ---------------------------------------------------------------------------

class TestTableFormatting:
    def test_table_width_twips(self):
        doc = _make_doc("# Heading\n\n| A | B |\n|---|---|\n| 1 | 2 |")
        for table in doc.tables:
            tblPr = table._tbl.find(qn('w:tblPr'))
            tblW = tblPr.find(qn('w:tblW'))
            assert tblW.get(qn('w:type')) == 'dxa'
            assert int(tblW.get(qn('w:w'))) <= 9360  # ~165mm in twips

    def test_table_layout_fixed(self):
        doc = _make_doc("| A | B |\n|---|---|\n| 1 | 2 |")
        for table in doc.tables:
            tblPr = table._tbl.find(qn('w:tblPr'))
            layout = tblPr.find(qn('w:tblLayout'))
            assert layout is not None
            assert layout.get(qn('w:type')) == 'fixed'

    def test_table_header_row_repeat(self):
        rows_md = "\n".join(f"| {i} | data |" for i in range(10))
        doc = _make_doc(f"| # | Col |\n|---|---|\n{rows_md}")
        for table in doc.tables:
            if len(table.rows) > 5:
                tr = table.rows[0]._tr
                trPr = tr.find(qn('w:trPr'))
                assert trPr is not None
                assert trPr.find(qn('w:tblHeader')) is not None

    def test_table_header_fill_cobalt(self):
        doc = _make_doc("| A | B |\n|---|---|\n| 1 | 2 |")
        for table in doc.tables:
            for cell in table.rows[0].cells:
                tc = cell._tc
                tcPr = tc.find(qn('w:tcPr'))
                shd = tcPr.find(qn('w:shd'))
                assert shd.get(qn('w:fill')).upper() == COBALT_HEX.upper()

    def test_table_cell_vertical_alignment(self):
        from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
        doc = _make_doc("| A | B |\n|---|---|\n| 1 | 2 |")
        for table in doc.tables:
            for cell in table.rows[0].cells:
                assert cell.vertical_alignment == WD_CELL_VERTICAL_ALIGNMENT.CENTER

    def test_table_no_overflow(self):
        doc = _make_doc("| A | B | C | D | E |\n|---|---|---|---|---|\n| " + " | ".join(["x"*50]*5) + " |")
        for table in doc.tables:
            tblPr = table._tbl.find(qn('w:tblPr'))
            tblW = tblPr.find(qn('w:tblW'))
            tw = int(tblW.get(qn('w:w')))
            assert tw <= 9360


# ---------------------------------------------------------------------------
# I3. Spacing Tests
# ---------------------------------------------------------------------------

class TestSpacing:
    def test_heading_spacing_h2(self):
        doc = _make_doc("## Heading Two\n\nBody text here.")
        for p in doc.paragraphs:
            if p.text == "Heading Two":
                assert p.paragraph_format.space_before == _SP['h1_before']
                break

    def test_heading_spacing_h3(self):
        doc = _make_doc("### Heading Three\n\nBody text here.")
        for p in doc.paragraphs:
            if p.text == "Heading Three":
                assert p.paragraph_format.space_before == _SP['h3_before']
                break

    def test_heading_keep_with_next(self):
        doc = _make_doc("## H2\n\n### H3\n\nBody")
        for p in doc.paragraphs:
            if p.text in ("H2", "H3"):
                assert p.paragraph_format.keep_with_next is True

    def test_add_section_spacing(self):
        doc = new_doc()
        add_section(doc, "Test Title", "Test guidance", level=2)
        # Find the heading paragraph
        for p in doc.paragraphs:
            if p.text == "Test Title":
                assert p.paragraph_format.space_before == _SP['h1_before']
                assert p.paragraph_format.space_after == _SP['heading_after']
                break

    def test_body_paragraph_spacing(self):
        doc = _make_doc("## H\n\nBody paragraph text here.")
        for p in doc.paragraphs:
            if p.text == "Body paragraph text here.":
                assert p.paragraph_format.space_after == _SP['body_after']
                assert p.paragraph_format.line_spacing == _SP['body_line']
                break

    def test_body_widow_control(self):
        doc = _make_doc("## H\n\nBody text here.")
        for p in doc.paragraphs:
            if p.text == "Body text here.":
                assert p.paragraph_format.widow_control is True
                break

    def test_list_item_widow_control(self):
        doc = _make_doc("- Item one\n- Item two")
        for p in doc.paragraphs:
            if p.text.strip() in ("Item one", "Item two"):
                assert p.paragraph_format.widow_control is True


# ---------------------------------------------------------------------------
# I4. List Tests
# ---------------------------------------------------------------------------

class TestLists:
    def test_bullet_list_has_numPr(self):
        """Bullet list items must have explicit w:numPr in the XML."""
        doc = _make_doc("- First\n- Second\n- Third")
        bullet_paras = [p for p in doc.paragraphs
                        if p.text.strip() in ("First", "Second", "Third")
                        and p._element.find(f'.//{qn("w:numPr")}') is not None]
        assert len(bullet_paras) == 3, (
            f"All 3 bullet items must have w:numPr, got {len(bullet_paras)}")

    def test_bullet_list_shares_numId(self):
        """All items in one bullet block should share a single numId."""
        doc = _make_doc("- A\n- B\n- C")
        num_ids = set()
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                nid = numPr.find(qn('w:numId'))
                if nid is not None:
                    num_ids.add(nid.get(qn('w:val')))
        assert len(num_ids) == 1, f"Expected 1 numId for one bullet block, got {num_ids}"

    def test_numbered_list_has_numPr(self):
        """Numbered list items must have explicit w:numPr in the XML."""
        doc = _make_doc("1. First\n2. Second\n3. Third")
        numbered_paras = [p for p in doc.paragraphs
                          if p.text.strip() in ("First", "Second", "Third")
                          and p._element.find(f'.//{qn("w:numPr")}') is not None]
        assert len(numbered_paras) == 3, (
            f"All 3 numbered items must have w:numPr, got {len(numbered_paras)}")

    def test_numbered_list_restarts(self):
        """Two separate numbered blocks must have DIFFERENT numIds."""
        doc = _make_doc("1. A\n2. B\n\nSome text.\n\n1. C\n2. D")
        num_ids = []
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                nid = numPr.find(qn('w:numId'))
                if nid is not None:
                    num_ids.append(nid.get(qn('w:val')))
        assert len(num_ids) == 4, f"Expected 4 numbered items, got {len(num_ids)}"
        assert num_ids[0] == num_ids[1], "Items in first block should share numId"
        assert num_ids[2] == num_ids[3], "Items in second block should share numId"
        assert num_ids[0] != num_ids[2], "Two blocks must have different numIds to restart"

    def test_numbered_list_decimal_abstractnum(self):
        """Numbered lists should use abstractNum 102 (decimal format)."""
        doc = _make_doc("1. Test item")
        numbering_el = doc.part.numbering_part.element
        abstract = None
        for a in numbering_el.findall(qn('w:abstractNum')):
            if a.get(qn('w:abstractNumId')) == str(_DECIMAL_ABSTRACT_ID):
                abstract = a
                break
        assert abstract is not None, f"abstractNum {_DECIMAL_ABSTRACT_ID} must exist"
        lvl = abstract.find(qn('w:lvl'))
        fmt = lvl.find(qn('w:numFmt'))
        assert fmt.get(qn('w:val')) == 'decimal', "Numbered list format must be 'decimal'"

    def test_alpha_list_numbering_exists(self):
        doc = _make_doc("(a) First item\n\n(b) Second item\n\n(c) Third item")
        alpha_paras = []
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                alpha_paras.append(p.text)
        assert len(alpha_paras) >= 3, f"Expected ≥3 native-numbered items, got {len(alpha_paras)}: {alpha_paras}"

    def test_alpha_list_blank_line_continuation(self):
        """Blank-line-separated (a)-(c) items should share ONE numId."""
        doc = _make_doc("(a) First\n\n(b) Second\n\n(c) Third")
        num_ids = set()
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                nid = numPr.find(qn('w:numId'))
                if nid is not None:
                    num_ids.add(nid.get(qn('w:val')))
        assert len(num_ids) == 1, f"Expected 1 numId for continuous list, got {len(num_ids)}: {num_ids}"

    def test_alpha_list_separate_blocks_restart(self):
        """Two separate (a)-(c) blocks should have DIFFERENT numIds."""
        md = "## Section 1\n\n(a) A1\n\n(b) A2\n\n## Section 2\n\n(a) B1\n\n(b) B2"
        doc = _make_doc(md)
        num_ids = []
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                nid = numPr.find(qn('w:numId'))
                if nid is not None:
                    num_ids.append(nid.get(qn('w:val')))
        unique_ids = set(num_ids)
        assert len(unique_ids) >= 2, f"Expected ≥2 numIds for separate lists, got {unique_ids}"

    def test_alpha_list_abstract_num_format(self):
        doc = _make_doc("(a) Item\n\n(b) Item")
        numbering = doc.part.numbering_part.element
        found = False
        for an in numbering.findall(qn('w:abstractNum')):
            if an.get(qn('w:abstractNumId')) == str(_ALPHA_ABSTRACT_ID):
                lvl = an.find(qn('w:lvl'))
                fmt = lvl.find(qn('w:numFmt'))
                assert fmt.get(qn('w:val')) == 'lowerLetter'
                lt = lvl.find(qn('w:lvlText'))
                assert lt.get(qn('w:val')) == '(%1)'
                found = True
        assert found, "abstractNum 100 (lowerLetter) not found"

    def test_paragraph_guard_no_swallow(self):
        """A body paragraph followed by (a) should not swallow (a) into the paragraph."""
        md = "Some body text here.\n(a) This should be a list item"
        doc = _make_doc(md)
        has_list = False
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                has_list = True
                break
        assert has_list, "(a) should be detected as list, not swallowed into paragraph"

    def test_list_spacing(self):
        doc = _make_doc("(a) First\n\n(b) Second\n\n(c) Third")
        list_paras = []
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                list_paras.append(p)
        if len(list_paras) >= 3:
            assert list_paras[0].paragraph_format.space_before == _SP['list_first_before']
            assert list_paras[1].paragraph_format.space_before == _SP['list_gap']
            assert list_paras[-1].paragraph_format.space_after == _SP['list_last_after']


# ---------------------------------------------------------------------------
# I5. Signature Tests
# ---------------------------------------------------------------------------

class TestSignatures:
    SIG_MD = """## Signatures

**DIGITAL ENERGY NETHERLANDS B.V.**

By: Jelmer Durk ten Wolde
Title: Bestuurder
Date: [●]
Signature: ____________________________


**ARCO VREUGDENHIL**

Name: Arco Vreugdenhil
Date: [●]
Signature: ____________________________
"""

    def test_sig_heading_triggers_section(self):
        doc = _make_doc(self.SIG_MD)
        # Verify the sig lines have keep_together
        sig_texts = []
        for p in doc.paragraphs:
            if p.paragraph_format.keep_together and p.text.strip():
                sig_texts.append(p.text.strip())
        assert any("DIGITAL ENERGY" in t for t in sig_texts)
        assert any("ARCO VREUGDENHIL" in t for t in sig_texts)

    def test_sig_party_name_keep_with_next(self):
        doc = _make_doc(self.SIG_MD)
        for p in doc.paragraphs:
            if "DIGITAL ENERGY" in p.text and p.paragraph_format.keep_together:
                assert p.paragraph_format.keep_with_next is True
                break

    def test_sig_line_keep_together(self):
        doc = _make_doc(self.SIG_MD)
        for p in doc.paragraphs:
            if p.text.strip().startswith("By:") or p.text.strip().startswith("Title:"):
                assert p.paragraph_format.keep_together is True

    def test_sig_multi_party_spacing(self):
        doc = _make_doc(self.SIG_MD)
        party_paras = []
        for p in doc.paragraphs:
            if p.paragraph_format.keep_together and p.text.strip():
                party_paras.append(p)
        # First party block's first line should have sig_section_before
        if party_paras:
            assert party_paras[0].paragraph_format.space_before == _SP['sig_section_before']

    def test_sig_last_line_no_keep_with_next(self):
        doc = _make_doc(self.SIG_MD)
        last_sig = None
        for p in doc.paragraphs:
            if p.paragraph_format.keep_together and p.text.strip():
                last_sig = p
        if last_sig:
            assert last_sig.paragraph_format.keep_with_next is not True

    def test_sig_section_exit_on_non_sig_heading(self):
        md = self.SIG_MD + "\n## Drafting Notes\n\nThis is body text after signatures."
        doc = _make_doc(md)
        # "Drafting Notes" heading should NOT have keep_together
        for p in doc.paragraphs:
            if p.text.strip() == "Drafting Notes":
                assert p.paragraph_format.keep_together is not True
                break

    def test_sig_fallback_without_heading(self):
        """Documents without ## Signatures heading should still detect sig lines."""
        md = "## Terms\n\nSome terms.\n\nBy: Jelmer\nName: Test\nTitle: CEO\nSignature: ______"
        doc = _make_doc(md)
        found = False
        for p in doc.paragraphs:
            if p.text.strip().startswith("By:") and p.paragraph_format.keep_together:
                found = True
                break
        assert found, "Signature lines should get keep_together even without ## Signatures heading"


# ---------------------------------------------------------------------------
# I6. Cover & Entity Tests
# ---------------------------------------------------------------------------

class TestCover:
    def test_cover_binding_formality(self):
        doc = profile_agreement(
            agreement_type="Master Service Agreement",
            client="Test BV", entity="nl"
        )
        found = False
        for p in doc.paragraphs:
            if "By and between:" in p.text:
                found = True
                break
        assert found, "Binding MSA should use 'By and between:'"

    def test_cover_non_binding_formality(self):
        doc = profile_agreement(
            agreement_type="Letter of Intent",
            client="Test Ltd", entity="ag"
        )
        found = False
        for p in doc.paragraphs:
            if p.text.strip() == "Between:":
                found = True
                break
        assert found, "Non-binding LOI should use 'Between:'"

    def test_cover_cobalt_labels(self):
        doc = profile_agreement(
            agreement_type="Advisory Agreement",
            client="Test", entity="nl"
        )
        cobalt_texts = []
        for p in doc.paragraphs[:30]:
            for r in p.runs:
                if r.font.color and r.font.color.rgb == COBALT:
                    cobalt_texts.append(r.text.strip())
        assert any("between" in t.lower() or "and" in t.lower() for t in cobalt_texts), \
            f"Party labels should use COBALT color. Found: {cobalt_texts}"

    def test_cover_no_parent_text(self):
        doc = profile_agreement(
            agreement_type="LOI", client="Test", entity="nl"
        )
        for p in doc.paragraphs:
            assert "subsidiary" not in p.text.lower(), "NL entity should not show 'subsidiary of'"

    def test_cover_registration_no_double_prefix(self):
        doc = profile_agreement(
            agreement_type="Master Service Agreement",
            client="Test BV", client_reg_type="KvK", client_reg_number="12345678",
            entity="nl"
        )
        for p in doc.paragraphs:
            assert "KvK: KvK" not in p.text, "Registration should not double the prefix"


# ---------------------------------------------------------------------------
# I7. OOXML Compliance Tests
# ---------------------------------------------------------------------------

class TestOOXML:
    def test_zoom_has_percent(self):
        doc = _make_doc("## Test")
        # Save to memory to trigger _fix_zoom
        import io
        buf = io.BytesIO()
        from generate import _fix_zoom
        _fix_zoom(doc)
        zoom = doc.settings.element.find(qn('w:zoom'))
        if zoom is not None:
            assert zoom.get(qn('w:percent')) is not None

    def test_numPr_schema_order(self):
        """numPr should come before spacing in pPr."""
        doc = _make_doc("(a) Item one\n\n(b) Item two")
        for p in doc.paragraphs:
            pPr = p._element.find(qn('w:pPr'))
            if pPr is None:
                continue
            numPr = pPr.find(qn('w:numPr'))
            spacing = pPr.find(qn('w:spacing'))
            if numPr is not None and spacing is not None:
                # numPr should come before spacing in the element tree
                children = list(pPr)
                numPr_idx = children.index(numPr)
                spacing_idx = children.index(spacing)
                assert numPr_idx < spacing_idx, \
                    f"numPr at {numPr_idx} should precede spacing at {spacing_idx}"

    def test_abstractNum_before_num(self):
        doc = _make_doc("(a) Item\n\n(b) Item")
        numbering = doc.part.numbering_part.element
        last_abstractNum_idx = -1
        first_num_idx = len(numbering) + 1
        for idx, child in enumerate(numbering):
            if child.tag == qn('w:abstractNum'):
                last_abstractNum_idx = max(last_abstractNum_idx, idx)
            elif child.tag == qn('w:num'):
                first_num_idx = min(first_num_idx, idx)
        if last_abstractNum_idx >= 0 and first_num_idx < len(numbering) + 1:
            assert last_abstractNum_idx < first_num_idx, \
                "All abstractNum elements must precede all num elements"

    def test_tblPr_element_order(self):
        doc = _make_doc("| A | B |\n|---|---|\n| 1 | 2 |")
        for table in doc.tables:
            tblPr = table._tbl.find(qn('w:tblPr'))
            if tblPr is None:
                continue
            tblW = tblPr.find(qn('w:tblW'))
            tblLayout = tblPr.find(qn('w:tblLayout'))
            if tblW is not None and tblLayout is not None:
                children = list(tblPr)
                assert children.index(tblW) < children.index(tblLayout)


# ---------------------------------------------------------------------------
# I8. Document Properties & Global Tests
# ---------------------------------------------------------------------------

class TestDocProperties:
    def test_document_properties_set(self):
        doc = _make_doc("## Test", title="My Title")
        assert doc.core_properties.title == "My Title"
        assert doc.core_properties.author == "Digital Energy"

    def test_auto_hyphenation_disabled(self):
        doc = _make_doc("## Test")
        ah = doc.settings.element.find(qn('w:autoHyphenation'))
        assert ah is not None
        assert ah.get(qn('w:val')) == '0'

    def test_font_fallback_chain(self):
        doc = _make_doc("## Test\n\nBody text here.")
        found = False
        for p in doc.paragraphs:
            for r in p.runs:
                rPr = r._element.find(qn('w:rPr'))
                if rPr is not None:
                    rf = rPr.find(qn('w:rFonts'))
                    if rf is not None and rf.get(qn('w:cs')) == 'Arial':
                        found = True
                        break
            if found:
                break
        assert found, "Body text should have w:cs=Arial fallback"

    def test_all_profiles_generate(self):
        """All profiles should generate valid Document objects."""
        docs = [
            profile_letter(date_str="1 Jan 2026"),
            profile_agreement(agreement_type="LOI", client="Test", date_str="1 Jan 2026"),
            profile_seed_memo(client="Fund X", date_str="1 Jan 2026"),
            profile_investor_memo(client="Capital Y", date_str="1 Jan 2026"),
            profile_exec_summary(title="Summary", date_str="1 Jan 2026"),
        ]
        for doc in docs:
            assert hasattr(doc, 'paragraphs')
            assert len(doc.paragraphs) > 0

    def test_md_to_docx_basic(self):
        md = "## Heading\n\nParagraph text.\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n- bullet"
        doc = md_to_docx(md, title="Test")
        assert len(doc.paragraphs) > 3
        assert len(doc.tables) >= 1

    def test_md_to_docx_with_cover(self):
        doc = md_to_docx("## Body", title="Test Doc", cover=True, entity="nl")
        # Should have cover page elements
        found_cover = False
        for p in doc.paragraphs:
            if p.text == "Test Doc":
                found_cover = True
                break
        assert found_cover


# ---------------------------------------------------------------------------
# I9. Integration Tests (real markdown patterns)
# ---------------------------------------------------------------------------

class TestIntegration:
    def test_alpha_list_in_legal_context(self):
        """Simulates Advisory Agreement §4.3 pattern with blank-line-separated items."""
        md = """## 4. Duties

The Advisor shall:

(a) advise the Board on strategy

(b) represent the company externally

(c) chair Advisory Board meetings

(d) support strategic goals

(e) provide periodic input
"""
        doc = _make_doc(md)
        numbered = []
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                numbered.append(p.text)
        assert len(numbered) == 5, f"Expected 5 alpha-list items, got {len(numbered)}: {numbered}"

    def test_signature_block_connectivity(self):
        """All lines in a signature block should be connected via keep_together."""
        md = """## Signatures

**DIGITAL ENERGY NETHERLANDS B.V.**

By: Jelmer Durk ten Wolde
Title: Bestuurder
Signature: ____________________________


**ARCO VREUGDENHIL**

Name: Arco Vreugdenhil
Signature: ____________________________
"""
        doc = _make_doc(md)
        connected = []
        for p in doc.paragraphs:
            if p.paragraph_format.keep_together and p.text.strip():
                connected.append(p.text.strip()[:50])
        assert len(connected) >= 7, f"Expected ≥7 connected sig lines, got {len(connected)}: {connected}"

    def test_heading_spacing_consistent(self):
        """H2 headings from md_to_docx and add_section should use same spacing."""
        # md_to_docx heading
        md_doc = _make_doc("## Section Title\n\nBody text.")
        md_h2_spacing = None
        for p in md_doc.paragraphs:
            if p.text == "Section Title":
                md_h2_spacing = p.paragraph_format.space_before
                break

        # add_section heading
        sec_doc = new_doc()
        add_section(sec_doc, "Section Title", "Guidance text", level=2)
        sec_h2_spacing = None
        for p in sec_doc.paragraphs:
            if p.text == "Section Title":
                sec_h2_spacing = p.paragraph_format.space_before
                break

        assert md_h2_spacing == sec_h2_spacing == _SP['h1_before'], \
            f"H2 spacing mismatch: md={md_h2_spacing}, section={sec_h2_spacing}, expected={_SP['h1_before']}"

    def test_bold_label_before_bullets_not_swallowed(self):
        """Bold label followed by bullets must NOT be swallowed by signature handler."""
        md = "**Management Board:**\n- Person A\n- Person B\n"
        doc = _make_doc(md)
        bullet_paras = [p for p in doc.paragraphs
                        if p._element.find(f'.//{qn("w:numPr")}') is not None]
        assert len(bullet_paras) == 2, (
            f"Expected 2 native bullet items, got {len(bullet_paras)}. "
            f"Texts: {[p.text for p in doc.paragraphs if p.text.strip()]}")
        # Verify prefix stripped
        assert all("- " not in p.text for p in bullet_paras), \
            "Bullet prefix '- ' should be stripped from text"

    def test_numbered_list_separate_from_headings(self):
        """Heading numbers (## 1. Title) must NOT get numPr; list numbers (1. item) must."""
        md = "## 1. Background\n\n1. First item\n2. Second item\n"
        doc = _make_doc(md)
        for p in doc.paragraphs:
            has_numPr = p._element.find(f'.//{qn("w:numPr")}') is not None
            if "Background" in p.text:
                assert not has_numPr, "Heading '1. Background' should NOT have numPr"
            elif p.text.strip() in ("First item", "Second item"):
                assert has_numPr, f"List item '{p.text}' should have numPr"

    def test_every_list_paragraph_has_numPr(self):
        """ALL list types must produce paragraphs with explicit w:numPr."""
        md = """- Bullet A
- Bullet B

1. Number one
2. Number two

(a) Alpha first

(b) Alpha second
"""
        doc = _make_doc(md)
        expected = {"Bullet A", "Bullet B", "Number one", "Number two",
                    "Alpha first", "Alpha second"}
        for p in doc.paragraphs:
            text = p.text.strip()
            if text in expected:
                has_numPr = p._element.find(f'.//{qn("w:numPr")}') is not None
                assert has_numPr, f"'{text}' must have w:numPr but doesn't"
                expected.discard(text)
        assert not expected, f"Missing list items in output: {expected}"
