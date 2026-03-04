# PDF Generation Spec

Agent-readable instructions for generating branded PDFs using brand-book design tokens. Covers two generation paths (HTML-to-PDF and direct PDF), presentation PDF export, and print considerations.

## Generation Paths

| Path | Best For | Library | Fidelity |
|------|----------|---------|----------|
| **Path 1: HTML-to-PDF** | Documents, reports, one-pagers | Puppeteer (Node.js) or Playwright | Highest -- uses css-variables.css + tailwind-config.js directly |
| **Path 2: Direct PDF** | Server-side, no browser needed | reportlab (Python) or pdfkit (Node.js) | Good -- requires manual token mapping |
| **Path 3: Presentation PDF** | Slide decks as PDF | Puppeteer with slide-master HTML | Landscape, 16:9 aspect ratio pages |

**Default:** Use Path 1 (HTML-to-PDF) when a browser environment is available. It produces the highest fidelity output because it consumes the same css-variables.css and tailwind-config.js that web output uses.

---

## Path 1: HTML-to-PDF (Recommended)

### Setup

```javascript
const puppeteer = require('puppeteer');

async function generatePDF(htmlContent, outputPath, options = {}) {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();

  // Load brand CSS variables + Tailwind
  const brandCSS = fs.readFileSync('exports/css-variables.css', 'utf8');
  const fullHTML = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <style>${brandCSS}</style>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
      <style>
        /* Print-specific overrides */
        @media print {
          body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
          .page-break { page-break-before: always; }
          .no-break { page-break-inside: avoid; }
          table thead { display: table-header-group; }
          table { page-break-inside: auto; }
          tr { page-break-inside: avoid; }
        }
      </style>
    </head>
    <body>${htmlContent}</body>
    </html>
  `;

  await page.setContent(fullHTML, { waitUntil: 'networkidle0' });

  await page.pdf({
    path: outputPath,
    format: options.format || 'A4',          // 'A4' or 'Letter'
    margin: {
      top: options.marginTop || '25mm',       // from page-masters.md
      bottom: options.marginBottom || '25mm',
      left: options.marginLeft || '20mm',
      right: options.marginRight || '20mm',
    },
    printBackground: true,                    // Required for brand colors
    preferCSSPageSize: false,
    displayHeaderFooter: true,
    headerTemplate: options.headerTemplate || buildHeader(options),
    footerTemplate: options.footerTemplate || buildFooter(options),
  });

  await browser.close();
}
```

### Header Template

Map `component.header.document` tokens:

```javascript
function buildHeader(options) {
  // Puppeteer header/footer templates have limited CSS support
  // Font size must be explicitly set; no external CSS loaded
  return `
    <div style="width: 100%; font-size: 8px; font-family: Inter, sans-serif;
                color: var(--color-text-secondary, #6B7280);
                padding: 0 20mm; display: flex; justify-content: space-between;">
      <span>${options.brandName || ''}</span>
      <span>${options.docTitle || ''}</span>
    </div>
  `;
}
```

### Footer Template

Map `component.footer.document` tokens:

```javascript
function buildFooter(options) {
  return `
    <div style="width: 100%; font-size: 8px; font-family: Inter, sans-serif;
                color: var(--color-text-secondary, #6B7280);
                padding: 0 20mm; display: flex; justify-content: space-between;
                border-top: 1px solid var(--color-border-default, #E5E7EB);">
      <span>${options.confidentiality || 'Confidential'}</span>
      <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
    </div>
  `;
}
```

### HTML Structure for Documents

Use CSS variables from `exports/css-variables.css` throughout:

```html
<!-- Cover page -->
<div class="cover" style="
  background-color: var(--color-brand-primary);
  color: white;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: var(--spacing-layout-page-margin);
">
  <img src="logo-white.svg" style="height: 40px; margin-bottom: 48px;" alt="Brand logo">
  <h1 style="font-family: var(--font-family-heading); font-size: 36px; font-weight: 700;">
    Document Title
  </h1>
  <div style="width: 80px; height: 4px; background: var(--color-brand-secondary); margin: 24px 0;"></div>
  <p style="font-size: 16px; opacity: 0.8;">Subtitle or description</p>
</div>

<div class="page-break"></div>

<!-- Content pages use standard HTML with CSS variables -->
<h1 style="color: var(--color-brand-primary); font-family: var(--font-family-heading);">
  Section Title
</h1>
<p style="color: var(--color-text-primary); font-family: var(--font-family-body); line-height: 1.5;">
  Body content...
</p>

<!-- Branded table -->
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr style="background: var(--color-brand-primary); color: white;">
      <th style="padding: 8px 12px; text-align: left;">Column</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: var(--color-surface-default);">
      <td style="padding: 8px 12px; border-bottom: 1px solid var(--color-border-default);">Data</td>
    </tr>
    <tr style="background: var(--color-surface-subtle);">
      <td style="padding: 8px 12px; border-bottom: 1px solid var(--color-border-default);">Data</td>
    </tr>
  </tbody>
</table>
```

### Page Size Options

| Format | Puppeteer `format` | Dimensions | Use Case |
|--------|-------------------|------------|----------|
| A4 | `'A4'` | 210 x 297 mm | Default for EU documents |
| US Letter | `'Letter'` | 8.5 x 11 in | Default for US documents |
| Custom landscape | `width: '297mm', height: '210mm'` | A4 rotated | Wide tables, landscape sections |
| Presentation | `width: '338.67mm', height: '190.5mm'` | 16:9 ratio | Slide deck PDF export |

---

## Path 2: Direct PDF (reportlab)

### Setup

```python
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import mm, pt
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register brand fonts
pdfmetrics.registerFont(TTFont('Inter', 'Inter-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Inter-Bold', 'Inter-Bold.ttf'))
pdfmetrics.registerFont(TTFont('JetBrainsMono', 'JetBrainsMono-Regular.ttf'))
```

### Token-to-Style Mapping

```python
def create_brand_styles(tokens):
    """Create reportlab ParagraphStyles from semantic typography tokens."""
    styles = getSampleStyleSheet()

    # Map semantic tokens to reportlab styles
    brand_styles = {
        'h1': ParagraphStyle(
            'BrandH1',
            parent=styles['Heading1'],
            fontName='Inter-Bold',
            fontSize=tokens['typography']['h1']['fontSize'],
            textColor=HexColor(tokens['color']['brand']['primary']),
            spaceAfter=12,
            leading=tokens['typography']['h1']['fontSize'] * tokens['typography']['h1']['lineHeight'],
        ),
        'body': ParagraphStyle(
            'BrandBody',
            parent=styles['Normal'],
            fontName='Inter',
            fontSize=tokens['typography']['body']['fontSize'],
            textColor=HexColor(tokens['color']['text']['primary']),
            spaceAfter=6,
            leading=tokens['typography']['body']['fontSize'] * 1.5,
        ),
        'caption': ParagraphStyle(
            'BrandCaption',
            parent=styles['Normal'],
            fontName='Inter',
            fontSize=tokens['typography']['caption']['fontSize'],
            textColor=HexColor(tokens['color']['text']['secondary']),
            spaceAfter=4,
        ),
        'data': ParagraphStyle(
            'BrandData',
            parent=styles['Normal'],
            fontName='JetBrainsMono',
            fontSize=tokens['typography']['data']['fontSize'],
            textColor=HexColor(tokens['color']['text']['primary']),
            alignment=2,  # RIGHT
        ),
    }
    return brand_styles
```

### Table Rendering

```python
def create_branded_table(data, headers, tokens):
    """Create a reportlab Table with brand-book token styling."""
    table_data = [headers] + data
    t = Table(table_data, repeatRows=1)

    header_bg = HexColor(tokens['component']['table']['header']['background'])
    header_fg = HexColor(tokens['component']['table']['header']['text'])
    row_bg = HexColor(tokens['component']['table']['row']['background'])
    alt_bg = HexColor(tokens['component']['table']['rowAlt']['background'])
    border_color = HexColor(tokens['color']['border']['default'])

    style_cmds = [
        # Header
        ('BACKGROUND', (0, 0), (-1, 0), header_bg),
        ('TEXTCOLOR', (0, 0), (-1, 0), header_fg),
        ('FONTNAME', (0, 0), (-1, 0), 'Inter-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        # Body
        ('FONTNAME', (0, 1), (-1, -1), 'Inter'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        # Alternating rows
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [row_bg, alt_bg]),
        # Borders
        ('GRID', (0, 0), (-1, -1), 0.5, border_color),
        # Padding
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]

    t.setStyle(TableStyle(style_cmds))
    return t
```

### Document Assembly

```python
def generate_pdf(content, tokens, output_path):
    """Generate a complete branded PDF."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        topMargin=25*mm,
        bottomMargin=25*mm,
        leftMargin=20*mm,
        rightMargin=20*mm,
    )

    styles = create_brand_styles(tokens)
    story = []

    # Cover page (use Canvas for full-page background)
    # ... (implement via onFirstPage callback)

    story.append(PageBreak())

    # Content
    for section in content['sections']:
        story.append(Paragraph(section['title'], styles['h1']))
        story.append(Paragraph(section['body'], styles['body']))
        story.append(Spacer(1, 12))

    doc.build(story)
```

---

## Path 3: Presentation PDF

Export slide-master layouts as landscape PDF pages:

```javascript
async function generatePresentationPDF(slides, outputPath) {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();

  // Build HTML with one div per slide at 1920x1080 proportions
  const slidesHTML = slides.map((slide, i) => `
    <div class="${i > 0 ? 'page-break' : ''}"
         style="width: 100%; aspect-ratio: 16/9; position: relative;
                background: ${slide.background}; padding: 64px;
                display: flex; flex-direction: column;">
      ${slide.content}
    </div>
  `).join('');

  await page.setContent(wrapWithBrandCSS(slidesHTML));

  await page.pdf({
    path: outputPath,
    width: '338.67mm',     // 16:9 at A4-ish scale
    height: '190.5mm',
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
    printBackground: true,
    displayHeaderFooter: false,
  });

  await browser.close();
}
```

---

## Print Considerations

From `templates/document/page-masters.md` print section:

| Consideration | Guidance |
|--------------|----------|
| **Color space** | PDF output is sRGB by default. For professional printing, convert to CMYK via ICC profile post-processing (ghostscript or similar) |
| **Bleed** | Standard documents: no bleed needed. Cover pages with full-bleed color: add 3mm bleed on all sides |
| **Crop marks** | Only for professional print. Add via `reportlab` CropMarks flowable or post-processing |
| **Font embedding** | reportlab auto-embeds registered TTF fonts. Puppeteer PDFs embed all used fonts automatically |
| **Image resolution** | Minimum 150 DPI for print, 72 DPI sufficient for screen. Embedded images should be pre-scaled |
| **Transparency** | Avoid transparency in CMYK output. Flatten transparent elements before CMYK conversion |

---

## Accessibility (PDF/UA)

| Requirement | Path 1 (Puppeteer) | Path 2 (reportlab) |
|-------------|--------------------|--------------------|
| Tagged PDF | Add `<article>`, `<section>`, `<h1>-<h4>` to HTML; Puppeteer preserves tags | Use `reportlab.platypus.flowables` with `accessibilityTag` |
| Reading order | Follows DOM order in HTML | Follows story order in reportlab |
| Alt text | `<img alt="...">` in HTML | Set `AccessibleImage` flowable |
| Document language | `<html lang="en">` | Set `/Lang` in document info |
| Table headers | `<th scope="col">` in HTML | Use `TableStyle` with header row semantics |
| Bookmarks | Generate from heading hierarchy | `doc.build()` auto-generates from Paragraph bookmarkNames |
| Link text | Use descriptive `<a>` text | Use Paragraph with `<link>` tag |

**Note:** Full PDF/UA compliance requires post-processing with tools like Adobe Acrobat or veraPDF. The approaches above achieve basic accessibility structure.

---

## Feeding Questions

This export is fed by answers from:
- **Phase 0:** Material extraction (existing document styles, print materials)
- **Phase 2:** Typography (font families, sizes, weights, density)
- **Phase 3:** Layout (margins, spacing, grid, cover page style, document aspect)
- **Phase 4:** Components (table styling, callout style, logo placement, citation format)
- **Phase 6:** Logo (file paths, clear space, minimum size)
- **Phase 7:** Photography/imagery (image treatment, background patterns)

See `references/question-deliverable-map.md` for complete traceability.
