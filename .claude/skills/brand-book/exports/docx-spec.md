# DOCX Generation Spec

Agent-readable instructions for generating branded Word documents using brand-book design tokens. This spec tells an AI agent which libraries to use, how to map tokens to Word styles, and how to render every brand-book component in .docx format.

## Library Selection

| Language | Library | Install | Notes |
|----------|---------|---------|-------|
| Python | `python-docx` | `pip install python-docx` | Recommended. Full style control, header/footer support, table formatting |
| Node.js | `docx` | `npm install docx` | Alternative. Declarative API, good TypeScript support |

**Default:** Use `python-docx` unless the agent is already operating in a Node.js context.

---

## Document Setup

### Page Size

Load from `templates/document/page-masters.md` Global Rules:

```python
from docx.shared import Mm, Pt, Inches, Cm, Emu, RGBColor
from docx import Document

doc = Document()
section = doc.sections[0]

# A4 (default)
section.page_width = Mm(210)
section.page_height = Mm(297)
section.orientation = WD_ORIENT.PORTRAIT

# US Letter (alternative)
# section.page_width = Inches(8.5)
# section.page_height = Inches(11)
```

### Margins

Map from page-masters.md margin specs (25mm top/bottom, 20mm left/right for A4):

```python
section.top_margin = Mm(25)
section.bottom_margin = Mm(25)
section.left_margin = Mm(20)
section.right_margin = Mm(20)
```

One-Pager variant (tighter margins per page-masters Master 5):

```python
section.top_margin = Mm(15)
section.bottom_margin = Mm(15)
section.left_margin = Mm(15)
section.right_margin = Mm(15)
```

---

## Token-to-Style Mapping

### Typography Styles

Map every semantic typography composite to a named Word style. Read token values from `tokens/semantic.tokens.json` typography section.

| Semantic Token | Word Style Name | Base Style | Usage |
|----------------|----------------|------------|-------|
| `typography.display` | `Display` | None | Hero numbers, cover page title |
| `typography.hero` | `Hero` | None | Section titles on cover pages |
| `typography.h1` | `Heading 1` | Built-in | Top-level document headings |
| `typography.h2` | `Heading 2` | Built-in | Section headings |
| `typography.h3` | `Heading 3` | Built-in | Subsection headings |
| `typography.h4` | `Heading 4` | Built-in | Minor headings |
| `typography.body` | `Normal` | Built-in | Body text |
| `typography.body-lg` | `Body Large` | Normal | Lead paragraphs, callout text |
| `typography.body-sm` | `Body Small` | Normal | Secondary body text |
| `typography.caption` | `Caption` | Built-in | Figure captions, footnotes |
| `typography.overline` | `Overline` | Normal | Section labels, category tags |
| `typography.data` | `Data` | Normal | Table cells with numbers |
| `typography.data-lg` | `Data Large` | Normal | Metric card numbers |
| `typography.button` | `Button Text` | Normal | CTA text in callout boxes |
| `typography.label` | `Label` | Normal | Form labels, metadata keys |

### Style Creation Pattern

```python
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_brand_style(doc, name, token, color_hex):
    """Create a Word style from a semantic typography token."""
    style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    font = style.font
    font.name = token['fontFamily']       # e.g., "Inter"
    font.size = Pt(token['fontSize'])     # e.g., Pt(11)
    font.color.rgb = RGBColor.from_string(color_hex.lstrip('#'))

    # Bold for headings
    if token.get('fontWeight', 400) >= 600:
        font.bold = True

    # Line height
    pf = style.paragraph_format
    pf.line_spacing = token.get('lineHeight', 1.5)

    # Letter spacing (if defined)
    if 'letterSpacing' in token:
        font.letter_spacing = Pt(token['letterSpacing'])

    # Space after paragraph
    pf.space_after = Pt(token.get('spaceAfter', 6))

    return style
```

### Color Application

Map brand tokens to Word theme colors and direct formatting:

| Brand Token | Word Usage | Method |
|-------------|-----------|--------|
| `color.brand.primary` | Heading text, accent borders | `font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)` |
| `color.brand.secondary` | CTA backgrounds, highlight borders | Table cell shading, shape fills |
| `color.text.primary` | Body text | `font.color.rgb` on Normal style |
| `color.text.secondary` | Caption text, metadata | `font.color.rgb` on Caption style |
| `color.surface.default` | Page background | Section background (usually white) |
| `color.surface.subtle` | Table alternating rows, callout backgrounds | Cell shading |
| `color.border.default` | Table borders, horizontal rules | Border color |
| `color.feedback.error.fg` | Error/warning callout text | Inline formatting |
| `color.feedback.success.fg` | Success callout text | Inline formatting |

### Hex-to-RGBColor Helper

```python
def hex_to_rgb(hex_str):
    """Convert '#1B365D' to RGBColor."""
    h = hex_str.lstrip('#')
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
```

---

## Component Rendering

### Tables

Map `component.table.*` tokens from `tokens/component.tokens.json`:

```python
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def create_branded_table(doc, data, headers, tokens):
    """Create a branded table from component.table tokens."""
    table = doc.add_table(rows=1 + len(data), cols=len(headers))
    table.style = 'Table Grid'

    # Header row
    header_row = table.rows[0]
    for i, text in enumerate(headers):
        cell = header_row.cells[i]
        cell.text = text
        # Apply header shading from component.table.header.background
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), tokens['header']['background'].lstrip('#'))
        shading.set(qn('w:val'), 'clear')
        cell._element.get_or_add_tcPr().append(shading)
        # Header text styling
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = hex_to_rgb(tokens['header']['text'])
                run.font.bold = True
                run.font.size = Pt(tokens['header']['fontSize'])

    # Data rows with alternating shading
    for row_idx, row_data in enumerate(data):
        row = table.rows[row_idx + 1]
        bg = tokens['rowAlt']['background'] if row_idx % 2 else tokens['row']['background']
        for i, value in enumerate(row_data):
            cell = row.cells[i]
            cell.text = str(value)
            if bg != '#FFFFFF':
                shading = OxmlElement('w:shd')
                shading.set(qn('w:fill'), bg.lstrip('#'))
                shading.set(qn('w:val'), 'clear')
                cell._element.get_or_add_tcPr().append(shading)

    # Cell padding
    for row in table.rows:
        for cell in row.cells:
            cell.paragraphs[0].paragraph_format.space_before = Pt(4)
            cell.paragraphs[0].paragraph_format.space_after = Pt(4)

    return table
```

**Numeric cells:** For columns containing numbers, apply the `Data` style and set `paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT`. Use tabular figures if the font supports them via `font.font_variant_numeric = 'tabular-nums'` (requires direct XML manipulation in python-docx).

### Metric Cards

Render as text boxes or styled paragraphs with visual separation:

```python
def add_metric_card(doc, value, label, delta=None, tokens=None):
    """Render a metric card as styled paragraphs."""
    # Value (large number)
    p = doc.add_paragraph()
    run = p.add_run(str(value))
    run.font.size = Pt(36)  # from typography.data-lg
    run.font.name = tokens['fontFamily']
    run.font.color.rgb = hex_to_rgb(tokens['color.brand.primary'])
    run.font.bold = True
    p.paragraph_format.space_after = Pt(2)

    # Label
    p = doc.add_paragraph()
    run = p.add_run(label)
    run.font.size = Pt(11)  # from typography.body
    run.font.color.rgb = hex_to_rgb(tokens['color.text.secondary'])
    p.paragraph_format.space_after = Pt(4)

    # Delta (optional)
    if delta:
        p = doc.add_paragraph()
        prefix = '+' if delta > 0 else ''
        color = tokens['color.feedback.success.fg'] if delta > 0 else tokens['color.feedback.error.fg']
        run = p.add_run(f'{prefix}{delta}%')
        run.font.size = Pt(10)
        run.font.color.rgb = hex_to_rgb(color)

    # Separator
    doc.add_paragraph('_' * 40).runs[0].font.color.rgb = hex_to_rgb(tokens['color.border.default'])
```

For side-by-side metric cards, use a 2 or 3-column table with invisible borders.

### Callout Boxes

Map `component.callout.*` tokens. Render as paragraphs with left border:

```python
def add_callout(doc, text, variant='info', tokens=None):
    """Render a callout box. Variants: info, success, warning, error, brand."""
    callout_tokens = tokens['callout'][variant]

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(12)

    # Left border (accent)
    pPr = p._element.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single')
    left.set(qn('w:sz'), '24')  # 3pt = 24 eighth-points
    left.set(qn('w:color'), callout_tokens['borderColor'].lstrip('#'))
    left.set(qn('w:space'), '8')
    pBdr.append(left)
    pPr.append(pBdr)

    # Background shading
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), callout_tokens['background'].lstrip('#'))
    shading.set(qn('w:val'), 'clear')
    pPr.append(shading)

    # Indent for visual padding
    p.paragraph_format.left_indent = Mm(4)

    run = p.add_run(text)
    run.font.color.rgb = hex_to_rgb(callout_tokens['text'])
    run.font.size = Pt(10)
```

### Badges

Render as inline formatted text runs (Word doesn't support true pill shapes inline):

```python
def add_badge(paragraph, text, variant='info', tokens=None):
    """Add an inline badge to an existing paragraph."""
    badge_tokens = tokens['badge'][variant]
    run = paragraph.add_run(f' {text} ')
    run.font.size = Pt(9)
    run.font.color.rgb = hex_to_rgb(badge_tokens['text'])
    run.font.bold = True
    # Background highlight approximation
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), badge_tokens['background'].lstrip('#'))
    shading.set(qn('w:val'), 'clear')
    run._element.get_or_add_rPr().append(shading)
```

---

## Cover Page

Implement page-masters Master 1 (Cover Page):

```python
def create_cover_page(doc, title, subtitle, metadata, tokens, logo_path=None):
    """Create a branded cover page per page-masters Cover template."""
    section = doc.sections[0]

    # Full-color variant: set page background to brand.primary
    # (Word background colors require XML manipulation)
    background = OxmlElement('w:background')
    background.set(qn('w:color'), tokens['color.brand.primary'].lstrip('#'))
    doc.element.insert(0, background)

    # Logo (top-left or centered per Q4.3 answer)
    if logo_path:
        doc.add_picture(logo_path, width=Mm(40))

    # Spacer
    for _ in range(6):
        doc.add_paragraph()

    # Title
    p = doc.add_paragraph()
    run = p.add_run(title)
    run.font.size = Pt(36)
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)  # White on dark bg
    run.font.name = tokens['fontFamily.heading']
    run.font.bold = True

    # Accent stripe (horizontal rule in brand.secondary)
    p = doc.add_paragraph()
    pPr = p._element.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '36')  # ~4.5pt
    bottom.set(qn('w:color'), tokens['color.brand.secondary'].lstrip('#'))
    pBdr.append(bottom)
    pPr.append(pBdr)

    # Subtitle
    p = doc.add_paragraph()
    run = p.add_run(subtitle)
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    run.font.name = tokens['fontFamily.body']

    # Metadata block (date, author, version, confidentiality)
    for key, value in metadata.items():
        p = doc.add_paragraph()
        run_key = p.add_run(f'{key}: ')
        run_key.font.size = Pt(10)
        run_key.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)
        run_val = p.add_run(value)
        run_val.font.size = Pt(10)
        run_val.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    # Page break after cover
    doc.add_page_break()
```

**Variants** (per page-masters.md):
- **Full-color:** Dark brand.primary background, white text (shown above)
- **White + accent stripe:** White background, dark text, brand.secondary stripe
- **Minimal:** White background, brand.primary title only, no stripe
- **Photo overlay:** Background image with semi-transparent brand.primary overlay (limited in Word -- use shape with fill)

---

## Headers & Footers

Map `component.header.document` and `component.footer.document` tokens:

```python
def setup_headers_footers(doc, tokens, logo_path=None, doc_title=''):
    """Configure document headers and footers."""
    section = doc.sections[0]

    # Different first page (cover has no header/footer)
    section.different_first_page_header_footer = True

    # --- Header (pages 2+) ---
    header = section.header
    header.is_linked_to_previous = False

    # Header table for layout (logo left, title right)
    ht = header.add_table(rows=1, cols=2, width=Mm(170))
    ht.columns[0].width = Mm(30)
    ht.columns[1].width = Mm(140)

    # Logo cell
    if logo_path:
        ht.cell(0, 0).paragraphs[0].add_run().add_picture(logo_path, height=Mm(8))

    # Title cell
    title_cell = ht.cell(0, 1)
    title_cell.paragraphs[0].text = doc_title
    title_cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for run in title_cell.paragraphs[0].runs:
        run.font.size = Pt(8)
        run.font.color.rgb = hex_to_rgb(tokens['color.text.secondary'])

    # Header bottom border (accent line)
    # Apply via table border XML

    # --- Footer (pages 2+) ---
    footer = section.footer
    footer.is_linked_to_previous = False

    ft = footer.add_table(rows=1, cols=2, width=Mm(170))

    # Confidentiality / brand name
    ft.cell(0, 0).paragraphs[0].text = tokens.get('brand_name', '')
    for run in ft.cell(0, 0).paragraphs[0].runs:
        run.font.size = Pt(8)
        run.font.color.rgb = hex_to_rgb(tokens['color.text.secondary'])

    # Page number (right-aligned)
    page_cell = ft.cell(0, 1)
    page_cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    # Add page number field
    run = page_cell.paragraphs[0].add_run()
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    run._element.append(fldChar1)

    run2 = page_cell.paragraphs[0].add_run()
    instrText = OxmlElement('w:instrText')
    instrText.text = ' PAGE '
    run2._element.append(instrText)

    run3 = page_cell.paragraphs[0].add_run()
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'end')
    run3._element.append(fldChar2)

    for run in page_cell.paragraphs[0].runs:
        run.font.size = Pt(8)
        run.font.color.rgb = hex_to_rgb(tokens['color.text.secondary'])
```

---

## Page Breaks & Sections

Follow rules from page-masters.md:

| Rule | Implementation |
|------|---------------|
| New section after cover | `doc.add_page_break()` or `doc.add_section(WD_SECTION.NEW_PAGE)` |
| Landscape tables (>6 columns) | `new_section.orientation = WD_ORIENT.LANDSCAPE` with swapped width/height |
| Table split with header repeat | Set `tbl.rows[0].repeat_header = True` (header row repeats on page break) |
| Max ~25 rows per page | Manually insert page breaks after 25 rows, or let Word auto-paginate with header repeat |
| Appendix starts on new page | `doc.add_section(WD_SECTION.NEW_PAGE)` |
| One-Pager: single page only | Tighter margins (15mm), smaller font scale, max 5 content blocks |

---

## Accessibility

| Requirement | Implementation |
|-------------|---------------|
| Heading hierarchy | Use built-in Heading 1-4 styles (enables navigation pane and screen readers) |
| Alt text on images | `doc.add_picture().alt_text = 'Description'` (python-docx InlineShape) |
| Table headers | Set `tbl.rows[0].repeat_header = True` for assistive technology |
| Language tag | Set document core properties: `doc.core_properties.language = 'en-US'` |
| Reading order | Maintain logical content flow (no floating text boxes unless necessary) |
| Link text | Use descriptive link text, not bare URLs |
| Color contrast | All text/background combinations must pass WCAG AA per `references/accessibility-guide.md` |

---

## Font Handling

Google Fonts used by the brand-book (e.g., Inter, JetBrains Mono) must be installed on the system generating the DOCX, or the document must embed them.

**System install approach (recommended):**
1. Download TTF files from Google Fonts
2. Install to system fonts directory
3. python-docx will reference them by name

**Embedding approach:**
- python-docx does not natively support font embedding
- Use `python-docx` to create the document, then post-process with a tool that embeds fonts
- Alternatively, note in the document metadata which fonts are required

**Fallback chain:** Always specify fallback fonts:
```python
font.name = 'Inter'
# Set fallback via XML
rFonts = run._element.get_or_add_rPr().get_or_add_rFonts()
rFonts.set(qn('w:ascii'), 'Inter')
rFonts.set(qn('w:hAnsi'), 'Inter')
rFonts.set(qn('w:cs'), 'Arial')  # Fallback
```

---

## Complete Example: One-Pager

```python
from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generate_one_pager(brand_config, content, output_path):
    """Generate a branded one-pager from brand-book tokens."""
    doc = Document()

    # 1. Page setup (One-Pager: tight margins)
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(15)
    section.bottom_margin = Mm(15)
    section.left_margin = Mm(15)
    section.right_margin = Mm(15)

    # 2. Load tokens from brand-config resolved values
    primary = hex_to_rgb(brand_config['resolved_primary_color'])
    secondary = hex_to_rgb(brand_config['resolved_secondary_color'])
    heading_font = brand_config['resolved_heading_font']
    body_font = brand_config['resolved_body_font']

    # 3. Logo
    if content.get('logo_path'):
        doc.add_picture(content['logo_path'], width=Mm(30))

    # 4. Title
    p = doc.add_paragraph()
    run = p.add_run(content['title'])
    run.font.size = Pt(24)
    run.font.name = heading_font
    run.font.color.rgb = primary
    run.font.bold = True

    # 5. Subtitle / tagline
    p = doc.add_paragraph()
    run = p.add_run(content['subtitle'])
    run.font.size = Pt(12)
    run.font.name = body_font
    run.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)  # text.secondary

    # 6. Key metrics (2-3 cards in a row via table)
    if content.get('metrics'):
        t = doc.add_table(rows=1, cols=len(content['metrics']))
        for i, metric in enumerate(content['metrics']):
            cell = t.cell(0, i)
            p1 = cell.paragraphs[0]
            run = p1.add_run(str(metric['value']))
            run.font.size = Pt(28)
            run.font.color.rgb = primary
            run.font.bold = True
            p2 = cell.add_paragraph()
            run = p2.add_run(metric['label'])
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)

    # 7. Body sections (max 5 blocks)
    for block in content.get('blocks', [])[:5]:
        p = doc.add_paragraph()
        run = p.add_run(block['heading'])
        run.font.size = Pt(14)
        run.font.name = heading_font
        run.font.color.rgb = primary
        run.font.bold = True

        p = doc.add_paragraph()
        run = p.add_run(block['text'])
        run.font.size = Pt(10)
        run.font.name = body_font

    # 8. CTA
    if content.get('cta'):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        run = p.add_run(content['cta'])
        run.font.size = Pt(12)
        run.font.color.rgb = secondary
        run.font.bold = True

    # 9. Save
    doc.save(output_path)
```

---

## Token Loading Helper

```python
import json

def load_brand_tokens(brand_book_path):
    """Load all token tiers from brand-book skill directory."""
    with open(f'{brand_book_path}/tokens/primitives.tokens.json') as f:
        primitives = json.load(f)
    with open(f'{brand_book_path}/tokens/semantic.tokens.json') as f:
        semantic = json.load(f)
    with open(f'{brand_book_path}/tokens/component.tokens.json') as f:
        components = json.load(f)
    return {
        'primitives': primitives,
        'semantic': semantic,
        'components': components,
    }
```

---

## Feeding Questions

This export is fed by answers from:
- **Phase 0:** Material extraction (existing document styles)
- **Phase 2:** Typography (font families, sizes, weights, density)
- **Phase 3:** Layout (margins, spacing, grid, cover page style, table styling)
- **Phase 4:** Components (callout style, badge style, citation format, logo placement)
- **Phase 6:** Logo (file paths, clear space, minimum size)

See `references/question-deliverable-map.md` for complete traceability.
