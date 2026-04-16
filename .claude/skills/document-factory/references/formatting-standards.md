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
- Total table width = content width (165mm / page width minus margins)
- Column widths proportional to content length
- Layout: fixed (prevents Word auto-resizing)

### Visual hierarchy
- **Header row:** Cobalt (#0034AF) background, white text, bold
- **Odd data rows:** White background
- **Even data rows:** Slate 50 (#F8FAFC) background
- **Borders:** 0.5pt Slate 300 (#CBD5E1) on all cell edges
- **Cell padding:** 3pt top/bottom

## Anti-Patterns

1. **Never use plain text for lists.** `1.` followed by text is not a list — Word cannot renumber it, indent it, or style it. Use `style='List Number'` or `style='List Bullet'`.
2. **Never color list numbers/bullets differently from body text.** Accent-colored numbers look like hyperlinks or errors. List markers inherit body text color.
3. **Never let a heading sit at the bottom of a page without body text.** Always set `keep_with_next = True`.
4. **Never let a signature block split across pages.** Use `keep_together` and `keep_with_next` on all signature paragraphs.
5. **Never place a table flush against preceding/following text.** Minimum 12pt gap above and below.
6. **Never make tables wider than the text body.** If a table overflows, the document looks broken.
7. **Never mix light and dark text colors within the same logical block** on a cover page. It fragments the visual hierarchy.
