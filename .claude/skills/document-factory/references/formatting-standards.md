# Document Formatting Standards

> Professional formatting rules for all Document Factory output.
> Sources: Legal document standards (Georgetown Law, Clio), IB formatting conventions,
> APA/Chicago typographic standards, python-docx implementation patterns.

## Page Layout (A4)

| Property | Value | Notes |
|----------|-------|-------|
| Page size | 210 x 297 mm | A4 |
| Left margin | 25 mm | Standard European business |
| Right margin | 20 mm | |
| Top margin | 20 mm | |
| Bottom margin | 35 mm | Room for footer |
| Content width | 165 mm | 210 - 25 - 20 |

## Typography

| Element | Font | Size | Color | Weight | Line spacing |
|---------|------|------|-------|--------|-------------|
| Body text | Inter (Arial fallback) | 11pt | Slate 800 | Regular | 16.5pt (1.5x) |
| H1 | Inter | 24pt | Slate 900 | Bold | Single |
| H2 | Inter | 18pt | Slate 900 | Bold | Single |
| H3 | Inter | 14pt | Slate 900 | Bold | Single |
| H4 | Inter | 12pt | Slate 900 | Bold | Single |
| Table header | Inter | 10pt | White | Bold | Single |
| Table body | Inter | 10pt | Slate 800 | Regular | Single |
| Footer | Inter | 7pt | Slate 500 | Regular | Single |
| Cover title | Inter | 28pt | Slate 900 | Bold | Single |
| Cover subject | Inter | 14pt | Slate 500 | Regular | Single |

## Spacing Rules

### Headings
- **Space before H1/H2:** 18pt (creates clear section breaks)
- **Space before H3/H4:** 12pt
- **Space after all headings:** 6pt (tight coupling to first body paragraph)
- **keep_with_next:** Always True on headings (never orphan a heading at page bottom)

### Body paragraphs
- **Space before:** 0pt
- **Space after:** 6pt (standard inter-paragraph gap)
- **Line spacing:** 16.5pt (1.5x at 11pt — readable without wasting space)

### Tables
- **Space before table:** 12pt (clear separation from preceding text)
- **Space after table:** 12pt (clear separation from following text)
- **Cell padding (internal):** 3pt top/bottom (breathing room inside cells)
- **Table must never be wider than content width** (165mm). Use exact content width.

### Lists
- **Space before first item:** 6pt
- **Space after last item:** 6pt
- **Space between items:** 2pt
- **Use Word native list styles** (`List Number`, `List Bullet`) — not plain text with manual numbers/bullets. Native styles ensure proper indentation, hanging indent, and renumbering.

### Signature blocks
- **Space before signature section:** 24pt minimum
- **keep_together:** True on all paragraphs in a signature block
- **keep_with_next:** True on all paragraphs except the last in each block
- A signature block = label + name + title + line. The entire set of signature blocks for all parties must stay on the same page. If they won't fit, force a page break before the signature section.

## Cover Page

### Color consistency
All party block text uses a single color (Slate 900) for professionalism. Do not mix light grey labels with dark values — it looks fragmented.

- **Party labels** ("By and between:", "And:"): Slate 500, 10pt
- **Legal name:** Slate 900, 11pt, bold
- **Address, registration, metadata values:** Slate 900, 10pt (not Slate 500)

The only elements in Slate 500 on the cover are: subject line, party labels, and metadata labels. Everything else is Slate 900.

### Metadata
- **Labels** ("Classification:", "Reference:"): Slate 500, 10pt, bold
- **Values**: Slate 900, 10pt

## Table Formatting

### Width
- Total table width = content width (165mm = 9,354 twips for `w:tblW`)
- Column widths in EMU for `col.width` (165mm = 5,940,000 EMU)
- Layout: fixed (`w:tblLayout type="fixed"`) — prevents Word auto-resizing
- **Unit trap:** `w:tblW` with `type="dxa"` expects twips, not EMU. `col.width` expects EMU. Never mix them.

### Column proportioning
- Weight = max character length per column, capped at 80 chars
- Minimum weight = header text length + 2
- **2-column key-value tables:** if label column < 30 chars and value > 60 chars, use 25/75 split. This prevents label columns from getting starved when one value cell has a long paragraph.
- For 3+ column tables: proportional with cap prevents any single column from dominating

### Cell formatting
- **Vertical alignment:** Header cells = CENTER, data cells = TOP
- **Cell padding:** 3pt top/bottom (via `paragraph_format.space_before/after` on cell paragraphs)
- **Text wrapping:** Automatic — cells expand vertically. Never set fixed row height.

### Visual hierarchy
- **Header row:** Cobalt (#0034AF) background, white text, bold, center-aligned vertically
- **Odd data rows:** White background
- **Even data rows:** Slate 50 (#F8FAFC) background
- **Borders:** 0.5pt Slate 300 (#CBD5E1) on all cell edges
- **Font:** 10pt Inter, Slate 800 (data), White (headers)

## Native Word Formatting Tools

Every formatting decision should use a native Word/python-docx feature. Never invent a workaround when Word provides the tool.

### Paragraph format (all available via `paragraph_format`)
| Property | Purpose | When to use |
|----------|---------|-------------|
| `keep_with_next` | Prevents page break between this paragraph and next | Headings, signature block labels |
| `keep_together` | Prevents page break within this paragraph | Signature blocks, short critical sections |
| `page_break_before` | Forces page break before paragraph | Chapter starts, signature sections that won't fit |
| `widow_control` | Prevents single lines at top/bottom of page | All body paragraphs |
| `space_before` / `space_after` | Vertical spacing | Headings, lists, table spacers |
| `line_spacing` | Line height | Body text (16.5pt = 1.5x at 11pt) |
| `left_indent` / `right_indent` | Horizontal indentation | Blockquotes |
| `first_line_indent` | First line indent (positive) or hanging indent (negative) | Legal clause numbering |
| `alignment` | Left/center/right/justify | Headers, footers, cover titles |
| `tab_stops` | Custom tab positions | Header: logo left + title right |

### List styles (native Word numbering engine)
| Style | Purpose | Notes |
|-------|---------|-------|
| `List Bullet` | Unordered list level 1 | Proper hanging indent, Word-managed bullet |
| `List Bullet 2` | Unordered list level 2 | Nested bullets |
| `List Number` | Ordered list level 1 | Auto-numbered, restartable |
| `List Number 2` | Ordered list level 2 | Nested numbered |

### Table cell properties
| Property | Purpose | API |
|----------|---------|-----|
| `vertical_alignment` | TOP/CENTER/BOTTOM | `cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP` |
| `width` | Column width in EMU | `col.width = Mm(40)` |
| `merge` | Span cells | `cell.merge(other_cell)` |

### Run formatting (all available via `run.font`)
| Property | Purpose |
|----------|---------|
| `name` | Font family |
| `size` | Font size in Pt |
| `bold` / `italic` | Weight/style |
| `color.rgb` | Text color |
| `underline` | Underline style |
| `strike` | Strikethrough |
| `superscript` / `subscript` | Vertical position |

### Section properties (headers, footers, page setup)
| Property | Purpose |
|----------|---------|
| `different_first_page_header_footer` | Cover page has separate header/footer |
| `first_page_header` / `first_page_footer` | Cover-specific header/footer |
| `header` / `footer` | Continuation page header/footer |
| `page_width` / `page_height` | A4: 210 x 297 mm |
| `left_margin` / `right_margin` / `top_margin` / `bottom_margin` | Page margins |

### OOXML elements (via lxml.etree + qn)
Only use these when python-docx has no native API:
| Element | Purpose | Why no API |
|---------|---------|-----------|
| `w:tblW` | Table total width in twips | python-docx sets auto-width only |
| `w:tblLayout` | Fixed vs auto table layout | Not exposed in API |
| `w:shd` | Cell background fill color | Not exposed for individual cells |
| `w:tcBorders` | Cell border style/color/width | Not exposed in API |
| `w:zoom` | Document zoom percent | python-docx omits `w:percent` attr |

## Table Header Row Repeat

Tables with more than 5 data rows MUST enable header row repeat via `w:tblHeader` on the first row's `w:trPr`. This ensures the header is visible when a table spans a page break.

```python
tr = table.rows[0]._tr
trPr = tr.find(qn('w:trPr'))
if trPr is None:
    trPr = etree.SubElement(tr, qn('w:trPr'))
    tr.insert(0, trPr)
if trPr.find(qn('w:tblHeader')) is None:
    etree.SubElement(trPr, qn('w:tblHeader'))
```

## Column Width Algorithm

Minimum-guarantee + proportional overflow:

1. **Measure** each column: `display_chars = max(header_len, min(max_data_len, 20))`, stripping markdown markers via `_display_len()`
2. **Classify**: "compact" (≤25 chars) or "flex" (>25 chars)
3. **Allocate**: Compact columns get their min_width (`display_chars * _CHAR_WIDTH_EMU + _CELL_PAD_EMU`, floored at `_MIN_COL_EMU = Mm(15)`). Flex columns share remaining space proportionally.
4. **Guards**: If compact total > 70% of available width, fall back to proportional with floor. Longest-word minimum prevents headers from being crammed.

Constants: `_CHAR_WIDTH_EMU = 63,500` (~5pt), `_CELL_PAD_EMU = Mm(4)`, `_MIN_COL_EMU = Mm(15)`.

## Alphabetic & Roman List Patterns

Legal sub-clause lists use `(a)`, `(b)`, `(c)` (lowerLetter) and `(i)`, `(ii)`, `(iii)` (lowerRoman). These MUST use native Word numbering, not plain text.

- **Custom numbering**: abstractNumId 100 = lowerLetter `(%1)`, abstractNumId 101 = lowerRoman `(%1)`. IDs 100+ avoid conflict with template built-ins (0–9).
- **Blank-line look-ahead**: Legal documents put blank lines between items. The detector skips blank lines and checks if the next non-blank line continues the list pattern.
- **`(i)` ambiguity**: If followed by `(ii)` → roman. If followed by `(j)` → alphabetic. Default to alphabetic.
- **Restart**: Each separate list block gets its own `w:num` with `w:startOverride val="1"`.

See `references/ooxml-numbering.md` for the underlying OOXML structure.

## Spacing Constants (`_SP` dict)

All spacing values are centralized in the `_SP` module-level dict in `generate.py`. Both `add_section()` and `md_to_docx()` reference it. Never hardcode `Pt()` values for spacing — use `_SP['key']`.

| Key | Value | Used for |
|-----|-------|----------|
| `h1_before` / `h2_before` | 18pt | Section break before H1/H2 headings |
| `h3_before` / `h4_before` | 12pt | Subsection break before H3/H4 |
| `heading_after` | 6pt | Tight coupling heading → first body paragraph |
| `body_after` | 6pt | Inter-paragraph gap |
| `body_line` | 16.5pt | Line spacing (1.5× at 11pt) |
| `table_before` / `table_after` | 12pt | Gap above/below tables |
| `sig_section_before` | 36pt | Gap before first signature party |
| `sig_party_gap` | 18pt | Gap between signature parties |
| `sig_line_gap` | 2pt | Within a signature block |

## Cover Page Colors (Updated)

Structural labels use **Cobalt (#0034AF)** — DE's primary brand accent, already used in table headers. Creates intentional hierarchy without looking faded.

| Element | Color | Size |
|---------|-------|------|
| Party labels ("By and between:", "And:") | Cobalt (#0034AF) | 10pt |
| Legal name | Slate 900 (#0F172A) | 11pt, bold |
| Address, registration, metadata values | Slate 900 (#0F172A) | 10pt |
| Subject line | Slate 800 (#1E293B) | 14pt |
| Metadata labels ("Classification:", "Reference:") | Cobalt (#0034AF) | 10pt, bold |

The only non-Cobalt, non-Slate-900 element is the subject line (Slate 800).

## OOXML Element Ordering

Word processors silently repair out-of-order elements, potentially stripping adjacent formatting. Maintain strict schema order.

### `w:pPr` child order (relevant subset)
`pStyle` → `keepNext` → `keepLines` → `pageBreakBefore` → `framePr` → `widowControl` → **`numPr`** → `suppressLineNumbers` → `pBorders` → `shd` → `tabs` → `suppressAutoHyphens` → `spacing` → `ind` → `jc` → `rPr`

### `w:numbering` child order
All `w:abstractNum` elements MUST precede all `w:num` elements.

### `w:tcPr` child order (relevant subset)
`tcW` → `gridSpan` → `tcBorders` → `shd` → `vAlign`

### `w:tblPr` child order (relevant subset)
`tblStyle` → `tblpPr` → `tblW` → `tblLayout` → `tblCellMar` → `tblLook`

## Anti-Patterns

1. **Never use plain text for lists.** `1.` followed by text is not a list — Word cannot renumber it, indent it, or style it. Use `style='List Number'` or `style='List Bullet'`.
2. **Never color list numbers/bullets differently from body text.** Accent-colored numbers look like hyperlinks or errors. List markers inherit body text color.
3. **Never let a heading sit at the bottom of a page without body text.** Always set `keep_with_next = True`.
4. **Never let a signature block split across pages.** Use `keep_together` and `keep_with_next` on all signature paragraphs.
5. **Never place a table flush against preceding/following text.** Minimum 6pt gap above and below.
6. **Never make tables wider than the text body.** If a table overflows, the document looks broken.
7. **Never mix light and dark text colors within the same logical block** on a cover page. It fragments the visual hierarchy.
8. **Never let a key-value table's label column starve.** Cap content-weight at 80 chars; use 25/75 split for 2-column key-value layouts.
9. **Never set fixed row heights on tables with variable content.** Let Word auto-expand rows.
10. **Never skip widow/orphan control on body paragraphs.** Single orphan lines at page boundaries look unprofessional.
