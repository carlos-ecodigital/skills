# XLSX/CSV Generation Spec

Agent-readable instructions for generating branded spreadsheets and CSV data exports using brand-book design tokens.

## Library Selection

| Language | Library | Install | Notes |
|----------|---------|---------|-------|
| Python | `openpyxl` | `pip install openpyxl` | Recommended. Full styling, charts, conditional formatting |
| Node.js | `exceljs` | `npm install exceljs` | Alternative. Good streaming support for large datasets |

**Default:** Use `openpyxl` unless the agent is already operating in a Node.js context.

---

## Two Use Cases

### Use Case 1: Token System Export
Export the brand-book token system itself as a reference spreadsheet for designers, stakeholders, or non-technical team members to review.

### Use Case 2: Branded Data Export
Apply brand-book tokens to any data table being exported (pipeline reports, financial models, comparison matrices, audit results).

---

## Token System Export (Use Case 1)

Export all 3 token tiers as a multi-sheet workbook:

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, NamedStyle
from openpyxl.utils import get_column_letter
import json

def export_token_reference(brand_book_path, output_path):
    """Export the full token system as a branded reference spreadsheet."""
    wb = Workbook()

    # Load tokens
    with open(f'{brand_book_path}/tokens/primitives.tokens.json') as f:
        primitives = json.load(f)
    with open(f'{brand_book_path}/tokens/semantic.tokens.json') as f:
        semantic = json.load(f)
    with open(f'{brand_book_path}/tokens/component.tokens.json') as f:
        components = json.load(f)

    # --- Sheet 1: Cover ---
    ws_cover = wb.active
    ws_cover.title = 'Brand Tokens'
    ws_cover['A1'] = 'Brand Design Token Reference'
    ws_cover['A1'].font = Font(name='Inter', size=24, bold=True, color='1B365D')
    ws_cover['A3'] = 'Generated from brand-book skill'
    ws_cover['A4'] = f'Primitives: 200+ tokens | Semantic: 90+ tokens | Components: ~440 tokens'
    ws_cover['A6'] = 'Sheet Guide:'
    ws_cover['A7'] = 'Primitives - Raw values (colors, fonts, spacing, motion)'
    ws_cover['A8'] = 'Semantic - Purpose-mapped tokens (brand, surface, text, feedback)'
    ws_cover['A9'] = 'Components - UI specs with states (buttons, cards, tables)'

    # --- Sheet 2: Primitives ---
    ws_prim = wb.create_sheet('Primitives')
    write_token_sheet(ws_prim, primitives, 'primitive')

    # --- Sheet 3: Semantic ---
    ws_sem = wb.create_sheet('Semantic')
    write_token_sheet(ws_sem, semantic, 'semantic')

    # --- Sheet 4: Components ---
    ws_comp = wb.create_sheet('Components')
    write_token_sheet(ws_comp, components, 'component')

    # Apply brand styling to all sheets
    apply_brand_styling(wb)

    wb.save(output_path)
```

### Token Sheet Writer

```python
def write_token_sheet(ws, tokens, tier):
    """Write a flat token table with columns: Path, Value, Type, Description."""
    headers = ['Token Path', 'Value', 'Type', 'Description']
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = Font(name='Inter', size=10, bold=True, color='FFFFFF')
        cell.fill = PatternFill('solid', fgColor='1B365D')
        cell.alignment = Alignment(horizontal='left', vertical='center')

    row = 2
    for path, token in flatten_tokens(tokens):
        ws.cell(row=row, column=1, value=path)
        ws.cell(row=row, column=2, value=token.get('$value', ''))
        ws.cell(row=row, column=3, value=token.get('$type', ''))
        ws.cell(row=row, column=4, value=token.get('$description', ''))

        # Color swatch for color tokens
        if token.get('$type') == 'color' and isinstance(token.get('$value'), str):
            hex_val = token['$value'].lstrip('#')
            if len(hex_val) == 6:
                ws.cell(row=row, column=2).fill = PatternFill('solid', fgColor=hex_val)
                # Use white text on dark colors
                luminance = int(hex_val[0:2], 16) * 0.299 + int(hex_val[2:4], 16) * 0.587 + int(hex_val[4:6], 16) * 0.114
                text_color = 'FFFFFF' if luminance < 128 else '000000'
                ws.cell(row=row, column=2).font = Font(name='JetBrains Mono', size=9, color=text_color)

        row += 1

    # Column widths
    ws.column_dimensions['A'].width = 40
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 50

    # Freeze header row
    ws.freeze_panes = 'A2'
```

### Token Flattener

```python
def flatten_tokens(obj, prefix=''):
    """Recursively flatten nested token JSON to (path, token) tuples."""
    results = []
    for key, value in obj.items():
        if key.startswith('$'):
            continue  # Skip metadata keys at this level
        path = f'{prefix}.{key}' if prefix else key
        if isinstance(value, dict) and '$value' in value:
            results.append((path, value))
        elif isinstance(value, dict):
            results.extend(flatten_tokens(value, path))
    return results
```

---

## Branded Data Export (Use Case 2)

### Named Styles from Tokens

Create reusable Excel styles mapped from semantic typography tokens:

```python
def create_brand_named_styles(wb, tokens):
    """Create NamedStyles from brand-book semantic typography tokens."""
    styles = {}

    # Header style (from component.table.header)
    header_style = NamedStyle(name='BrandHeader')
    header_style.font = Font(
        name=tokens['fontFamily']['heading'],
        size=10,
        bold=True,
        color='FFFFFF',
    )
    header_style.fill = PatternFill('solid', fgColor=tokens['color']['brand']['primary'].lstrip('#'))
    header_style.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    header_style.border = Border(
        bottom=Side(style='thin', color=tokens['color']['border']['default'].lstrip('#'))
    )
    wb.add_named_style(header_style)
    styles['header'] = header_style

    # Body style (from typography.body)
    body_style = NamedStyle(name='BrandBody')
    body_style.font = Font(
        name=tokens['fontFamily']['body'],
        size=10,
        color=tokens['color']['text']['primary'].lstrip('#'),
    )
    body_style.alignment = Alignment(vertical='center', wrap_text=True)
    wb.add_named_style(body_style)
    styles['body'] = body_style

    # Data style (from typography.data -- right-aligned, monospace)
    data_style = NamedStyle(name='BrandData')
    data_style.font = Font(
        name=tokens['fontFamily']['mono'],
        size=10,
        color=tokens['color']['text']['primary'].lstrip('#'),
    )
    data_style.alignment = Alignment(horizontal='right', vertical='center')
    data_style.number_format = '#,##0'
    wb.add_named_style(data_style)
    styles['data'] = data_style

    # Caption style
    caption_style = NamedStyle(name='BrandCaption')
    caption_style.font = Font(
        name=tokens['fontFamily']['body'],
        size=9,
        color=tokens['color']['text']['secondary'].lstrip('#'),
    )
    wb.add_named_style(caption_style)
    styles['caption'] = caption_style

    # Currency style
    currency_style = NamedStyle(name='BrandCurrency')
    currency_style.font = Font(
        name=tokens['fontFamily']['mono'],
        size=10,
        color=tokens['color']['text']['primary'].lstrip('#'),
    )
    currency_style.alignment = Alignment(horizontal='right', vertical='center')
    currency_style.number_format = '#,##0.00'
    wb.add_named_style(currency_style)
    styles['currency'] = currency_style

    # Percentage style
    pct_style = NamedStyle(name='BrandPercent')
    pct_style.font = Font(
        name=tokens['fontFamily']['mono'],
        size=10,
        color=tokens['color']['text']['primary'].lstrip('#'),
    )
    pct_style.alignment = Alignment(horizontal='right', vertical='center')
    pct_style.number_format = '0.0%'
    wb.add_named_style(pct_style)
    styles['percent'] = pct_style

    return styles
```

### Branded Table Writer

```python
def write_branded_table(ws, data, headers, column_types, tokens, start_row=1):
    """Write a branded data table with header styling and alternating rows.

    Args:
        column_types: list of 'text' | 'data' | 'currency' | 'percent' | 'date'
    """
    alt_fill = PatternFill('solid', fgColor=tokens['color']['surface']['subtle'].lstrip('#'))
    border_color = tokens['color']['border']['default'].lstrip('#')
    thin_border = Border(
        bottom=Side(style='thin', color=border_color),
        left=Side(style='thin', color=border_color),
        right=Side(style='thin', color=border_color),
    )

    # Headers
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=start_row, column=col, value=header)
        cell.style = 'BrandHeader'

    # Data rows
    for row_idx, row_data in enumerate(data):
        excel_row = start_row + 1 + row_idx
        for col, value in enumerate(row_data, 1):
            cell = ws.cell(row=excel_row, column=col, value=value)

            # Apply column-specific style
            col_type = column_types[col - 1] if col - 1 < len(column_types) else 'text'
            style_map = {
                'text': 'BrandBody',
                'data': 'BrandData',
                'currency': 'BrandCurrency',
                'percent': 'BrandPercent',
            }
            cell.style = style_map.get(col_type, 'BrandBody')

            # Alternating row shading
            if row_idx % 2 == 1:
                cell.fill = alt_fill

            cell.border = thin_border

    # Auto-fit column widths (approximate)
    for col in range(1, len(headers) + 1):
        max_len = max(len(str(headers[col - 1])), max((len(str(r[col - 1])) for r in data), default=0))
        ws.column_dimensions[get_column_letter(col)].width = min(max_len + 4, 40)

    # Freeze header row
    ws.freeze_panes = ws.cell(row=start_row + 1, column=1).coordinate
```

### Chart Styling

Map `component.chart.*` and `semantic.color.data.*` tokens to Excel charts:

```python
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.series import DataPoint

def create_branded_chart(ws, data_range, categories_range, title, tokens):
    """Create a branded bar chart using data.series tokens."""
    chart = BarChart()
    chart.title = title
    chart.type = 'col'
    chart.y_axis.title = None
    chart.x_axis.title = None

    # Brand font
    chart.title.txPr = None  # Reset, then set font
    # (openpyxl chart font styling is limited; set via XML if needed)

    # Data series colors from semantic.color.data.series-1 through series-6
    series_colors = [
        tokens['color']['data']['series-1'].lstrip('#'),
        tokens['color']['data']['series-2'].lstrip('#'),
        tokens['color']['data']['series-3'].lstrip('#'),
        tokens['color']['data']['series-4'].lstrip('#'),
        tokens['color']['data']['series-5'].lstrip('#'),
        tokens['color']['data']['series-6'].lstrip('#'),
    ]

    data = Reference(ws, **data_range)
    categories = Reference(ws, **categories_range)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)

    # Apply brand colors to series
    for i, series in enumerate(chart.series):
        color_hex = series_colors[i % len(series_colors)]
        series.graphicalProperties.solidFill = color_hex

    # Grid lines from component.chart.grid
    chart.y_axis.majorGridlines.spPr.ln.solidFill = tokens['color']['border']['subtle'].lstrip('#')

    return chart
```

### Conditional Formatting

Map feedback tokens to conditional format rules:

```python
from openpyxl.formatting.rule import CellIsRule

def apply_branded_conditional_formatting(ws, cell_range, tokens):
    """Apply conditional formatting using feedback tokens."""
    # Success (positive values)
    success_fill = PatternFill('solid', fgColor=tokens['color']['feedback']['success']['bg'].lstrip('#'))
    success_font = Font(color=tokens['color']['feedback']['success']['fg'].lstrip('#'))

    # Warning
    warning_fill = PatternFill('solid', fgColor=tokens['color']['feedback']['warning']['bg'].lstrip('#'))
    warning_font = Font(color=tokens['color']['feedback']['warning']['fg'].lstrip('#'))

    # Error (negative values)
    error_fill = PatternFill('solid', fgColor=tokens['color']['feedback']['error']['bg'].lstrip('#'))
    error_font = Font(color=tokens['color']['feedback']['error']['fg'].lstrip('#'))

    ws.conditional_formatting.add(cell_range,
        CellIsRule(operator='greaterThan', formula=['0'], fill=success_fill, font=success_font))
    ws.conditional_formatting.add(cell_range,
        CellIsRule(operator='lessThan', formula=['0'], fill=error_fill, font=error_font))
    ws.conditional_formatting.add(cell_range,
        CellIsRule(operator='equal', formula=['0'], fill=warning_fill, font=warning_font))
```

---

## Cover Sheet

Branded first sheet with logo, title, metadata:

```python
def create_cover_sheet(wb, brand_config, doc_title, tokens):
    """Create a branded cover sheet."""
    ws = wb.active
    ws.title = 'Overview'

    # Merge cells for title area
    ws.merge_cells('A1:F1')
    ws['A1'] = brand_config['brand_name']
    ws['A1'].font = Font(name=tokens['fontFamily']['heading'], size=20, bold=True,
                         color=tokens['color']['brand']['primary'].lstrip('#'))

    ws.merge_cells('A3:F3')
    ws['A3'] = doc_title
    ws['A3'].font = Font(name=tokens['fontFamily']['heading'], size=14,
                         color=tokens['color']['text']['primary'].lstrip('#'))

    # Accent stripe (row background)
    for col in range(1, 7):
        ws.cell(row=2, column=col).fill = PatternFill('solid',
            fgColor=tokens['color']['brand']['secondary'].lstrip('#'))
    ws.row_dimensions[2].height = 4  # Thin stripe

    # Metadata
    metadata = [
        ('Generated', 'Auto-generated from brand-book tokens'),
        ('Date', '{{current_date}}'),
        ('Confidentiality', 'Confidential'),
    ]
    for i, (key, value) in enumerate(metadata, 5):
        ws.cell(row=i, column=1, value=key).font = Font(name=tokens['fontFamily']['body'], size=9, bold=True,
            color=tokens['color']['text']['secondary'].lstrip('#'))
        ws.cell(row=i, column=2, value=value).font = Font(name=tokens['fontFamily']['body'], size=9,
            color=tokens['color']['text']['primary'].lstrip('#'))
```

---

## CSV Fallback

When XLSX formatting isn't needed (data pipelines, imports, simple exports):

| Aspect | Convention |
|--------|-----------|
| Encoding | UTF-8 with BOM (`utf-8-sig`) for Excel compatibility |
| Delimiter | Comma (`,`) default; semicolon (`;`) for EU locales |
| Header row | Always include; use token path names for token exports |
| Quoting | Quote fields containing commas, newlines, or quotes |
| Date format | ISO 8601 (`YYYY-MM-DD`) |
| Number format | No thousands separator; period decimal |
| Boolean | `true`/`false` (lowercase) |

```python
import csv

def export_csv(data, headers, output_path, delimiter=','):
    """Export data as branded CSV (UTF-8 with BOM)."""
    with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow(headers)
        writer.writerows(data)
```

---

## Feeding Questions

This export is fed by answers from:
- **Phase 0:** Material extraction (existing spreadsheet styles)
- **Phase 1:** Color identity (brand colors, data viz palette, audience accents)
- **Phase 2:** Typography (font families, number formatting preference)
- **Phase 3:** Layout (table styling preference)
- **Phase 4:** Components (chart styling, badge style for conditional formatting)

See `references/question-deliverable-map.md` for complete traceability.
