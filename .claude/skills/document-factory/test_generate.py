#!/usr/bin/env python3
"""Document Factory test suite.

Two test classes:
  TestColumnWidths — pure function tests for _compute_col_widths()
  TestAudit — every generated document passes audit_document() with zero violations

Run: pytest test_generate.py -v
"""

import re
import sys
import os

import pytest
from docx.shared import Mm, Pt, Emu
from docx.oxml.ns import qn

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import (
    _compute_col_widths, _display_len, _longest_word_len, _SP,
    _CHAR_WIDTH_EMU, _CELL_PAD_EMU, _MIN_COL_EMU,
    _ALPHA_ABSTRACT_ID, _ROMAN_ABSTRACT_ID, _DECIMAL_ABSTRACT_ID, _BULLET_ABSTRACT_ID,
    md_to_docx, new_doc, add_table, add_section, _run, _fix_zoom,
    audit_document, profile_agreement, profile_letter, profile_seed_memo,
    profile_investor_memo, profile_exec_summary,
    Party, DE_ENTITIES, COBALT_HEX, SLATE_50_HEX,
)


def _make_doc(md_text, **kwargs):
    defaults = dict(title="Test Doc", cover=True, entity="nl")
    defaults.update(kwargs)
    doc = md_to_docx(md_text, **defaults)
    _fix_zoom(doc)  # save_doc() applies this before audit
    return doc


# ---------------------------------------------------------------------------
# TestColumnWidths — pure function tests (no audit overlap)
# ---------------------------------------------------------------------------

class TestColumnWidths:
    def test_2col_kv_heuristic(self):
        headers = ["Label", "Value"]
        rows = [["Short", "A" * 80]]
        avail = int(Mm(165))
        widths = _compute_col_widths(headers, rows, avail)
        assert abs(widths[0] - int(avail * 0.25)) < avail * 0.02

    def test_starved_columns_milestone_table(self):
        headers = ["Milestone", "Units", "% Pool", "Trigger", "Sunset", "Certified"]
        rows = [["Build-out phase 1", "5000", "2.5%", "A" * 300, "2027-Q4", "Board resolution"]]
        widths = _compute_col_widths(headers, rows, int(Mm(165)))
        for w in widths:
            assert w >= _MIN_COL_EMU, f"Column width {w} < minimum {_MIN_COL_EMU}"

    def test_all_compact_surplus_distributed(self):
        headers = ["A", "B", "C", "D", "E"]
        rows = [["12345", "12345", "12345", "12345", "12345"]]
        widths = _compute_col_widths(headers, rows, int(Mm(165)))
        assert all(w > _MIN_COL_EMU for w in widths)

    def test_display_len_strips_bold(self):
        assert _display_len("**bold**") == 4
        assert _display_len("normal") == 6
        assert _display_len("`code`") == 4

    def test_longest_word(self):
        assert _longest_word_len("Time-Based Tranche") == len("Time-Based")

    def test_total_equals_available(self):
        headers = ["A", "B", "C"]
        rows = [["Short", "Medium text here", "A" * 100]]
        avail = int(Mm(165))
        widths = _compute_col_widths(headers, rows, avail)
        assert sum(widths) == avail

    def test_overflow_guard(self):
        headers = [f"H{i}" for i in range(8)]
        rows = [[f"D{i}" for i in range(8)]]
        avail = int(Mm(165))
        widths = _compute_col_widths(headers, rows, avail)
        for w in widths:
            assert w >= _MIN_COL_EMU


# ---------------------------------------------------------------------------
# TestAudit — audit_document() on every document pattern
# ---------------------------------------------------------------------------

class TestAudit:
    """Every generated document must pass audit_document() with zero violations."""

    LEGAL_MD = """\
## 1. Definitions

"**Agreement**" means this Advisory Agreement.

## 2. Scope

The Advisor shall provide:

(a) Strategic guidance on positioning

(b) Introductions to potential partners

(c) Review of business plans

## 3. Deliverables

**Project Team:**
- Alice van der Berg
- Bob Smith

1. Phase one deliverables
2. Phase two deliverables

| Deliverable | Due Date | Owner |
|-------------|----------|-------|
| Report A    | Q1 2026  | Alice |
| Report B    | Q2 2026  | Bob   |

## 4. General

> This agreement is governed by Dutch law.

## Signatures

**DIGITAL ENERGY NETHERLANDS B.V.**

By: ___________________________
Name: Jelmer ten Wolde
Title: Bestuurder


**ADVISOR**

By: ___________________________
Name: Jane Doe
Title: Advisor
"""

    def test_simple_md(self):
        doc = _make_doc("## Heading\n\nBody text paragraph.\n\n- Bullet A\n- Bullet B\n\n1. Number one\n2. Number two\n")
        violations = audit_document(doc)
        assert violations == [], violations

    def test_legal_pattern(self):
        doc = _make_doc(self.LEGAL_MD)
        violations = audit_document(doc)
        assert violations == [], violations

    def test_bold_label_before_list(self):
        """Regression: signature handler must not swallow non-signature bold lines."""
        doc = _make_doc("**Management Board:**\n- Person A\n- Person B\n")
        violations = audit_document(doc)
        assert violations == [], violations

    def test_numbered_list_restart(self):
        """Two numbered blocks must get different numIds."""
        doc = _make_doc("1. A\n2. B\n\nSome paragraph.\n\n1. C\n2. D\n")
        violations = audit_document(doc)
        assert violations == [], violations
        # Verify restart: extract numIds
        num_ids = []
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                nid = numPr.find(qn('w:numId'))
                if nid is not None:
                    num_ids.append(nid.get(qn('w:val')))
        assert len(num_ids) == 4
        assert num_ids[0] == num_ids[1], "First block should share numId"
        assert num_ids[2] == num_ids[3], "Second block should share numId"
        assert num_ids[0] != num_ids[2], "Different blocks must restart"

    def test_alpha_list_blank_lines(self):
        doc = _make_doc("## Section\n\n(a) First\n\n(b) Second\n\n(c) Third\n")
        violations = audit_document(doc)
        assert violations == [], violations
        # All 3 share one numId
        num_ids = set()
        for p in doc.paragraphs:
            numPr = p._element.find(f'.//{qn("w:numPr")}')
            if numPr is not None:
                nid = numPr.find(qn('w:numId'))
                if nid is not None:
                    num_ids.add(nid.get(qn('w:val')))
        assert len(num_ids) == 1, f"Expected 1 numId for continuous block, got {num_ids}"

    def test_table_formatting(self):
        """Table with enough rows to trigger header repeat."""
        rows_md = "\n".join(f"| Data {i} | Value {i} |" for i in range(10))
        md = f"## Table Test\n\n| Header A | Header B |\n|----------|----------|\n{rows_md}\n"
        doc = _make_doc(md)
        violations = audit_document(doc)
        assert violations == [], violations

    def test_list_after_table(self):
        md = "## Section\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n- Bullet after table\n"
        doc = _make_doc(md)
        violations = audit_document(doc)
        assert violations == [], violations

    def test_blockquote(self):
        doc = _make_doc("## Section\n\n> This is a blockquote with important text.\n")
        violations = audit_document(doc)
        assert violations == [], violations

    def test_md_without_cover(self):
        doc = md_to_docx("## Title\n\nBody.\n", title="Test", cover=False)
        _fix_zoom(doc)
        violations = audit_document(doc)
        assert violations == [], violations

    def test_md_with_cover(self):
        doc = _make_doc("## Title\n\nBody.\n")
        violations = audit_document(doc)
        assert violations == [], violations
        # Verify cover page break exists
        body_el = doc.element.body
        found_break = False
        for p_el in body_el.findall(qn('w:p')):
            if p_el.find(f'.//{qn("w:br")}[@{qn("w:type")}="page"]') is not None:
                found_break = True
                break
        assert found_break, "Cover page should have a page break"

    def _audit_profile(self, doc):
        """Apply save_doc fixes then audit."""
        _fix_zoom(doc)
        return audit_document(doc)

    def test_profile_agreement(self):
        doc = profile_agreement("Advisory Agreement", entity="nl")
        violations = self._audit_profile(doc)
        assert violations == [], violations

    def test_profile_letter(self):
        doc = profile_letter(title="Test Letter", date_str="16 April 2026", entity="ag")
        violations = self._audit_profile(doc)
        assert violations == [], violations

    def test_profile_seed_memo(self):
        doc = profile_seed_memo()
        violations = self._audit_profile(doc)
        assert violations == [], violations

    def test_profile_investor_memo(self):
        doc = profile_investor_memo()
        violations = self._audit_profile(doc)
        assert violations == [], violations

    def test_profile_exec_summary(self):
        doc = profile_exec_summary(title="Q1 Update")
        violations = self._audit_profile(doc)
        assert violations == [], violations
