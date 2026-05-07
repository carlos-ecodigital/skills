# OOXML Numbering Reference

> Concise reference for maintaining Document Factory's list numbering system.
> For formatting rules, see `formatting-standards.md`.

## Architecture

Word's numbering engine has three layers:

```
w:abstractNum (format definition)
    └── w:num (instance, points to abstractNum)
         └── w:numPr (on paragraph, assigns numId + indent level)
```

### `w:abstractNum` — Format Definition

Defines how a list looks: number format, level text, indentation.

```xml
<w:abstractNum w:abstractNumId="100">
  <w:lvl w:ilvl="0">
    <w:start w:val="1"/>
    <w:numFmt w:val="lowerLetter"/>
    <w:lvlText w:val="(%1)"/>
    <w:lvlJc w:val="left"/>
    <w:pPr>
      <w:ind w:left="720" w:hanging="360"/>
    </w:pPr>
  </w:lvl>
</w:abstractNum>
```

| Field | Purpose |
|-------|---------|
| `abstractNumId` | Unique identifier. Template uses 0–9; we use 100+ |
| `w:numFmt` | `lowerLetter` = a,b,c; `lowerRoman` = i,ii,iii; `decimal` = 1,2,3 |
| `w:lvlText` | Display template. `(%1)` → `(a)`, `(i)`, etc. |
| `w:ind` | `left` = total indent from margin; `hanging` = how far the number hangs back |

### `w:num` — Instance

Points to an `abstractNum` and optionally overrides the start value. Each separate list block in a document gets its own `w:num`.

```xml
<w:num w:numId="10">
  <w:abstractNumId w:val="100"/>
  <w:lvlOverride w:ilvl="0">
    <w:startOverride w:val="1"/>
  </w:lvlOverride>
</w:num>
```

| Field | Purpose |
|-------|---------|
| `numId` | Unique instance ID, referenced by paragraphs |
| `abstractNumId` | Which format to use |
| `w:startOverride` | Restart at 1 for each new list block |

### `w:numPr` — Paragraph Assignment

Applied to a paragraph to make it a list item:

```xml
<w:pPr>
  <w:numPr>
    <w:ilvl w:val="0"/>
    <w:numId w:val="10"/>
  </w:numPr>
</w:pPr>
```

## Document Factory Custom Definitions

| abstractNumId | numFmt | lvlText | Hanging indent | Purpose |
|--------------|--------|---------|----------------|---------|
| 100 | `lowerLetter` | `(%1)` | 360 twips | `(a)`, `(b)`, `(c)` sub-clauses |
| 101 | `lowerRoman` | `(%1)` | 480 twips | `(i)`, `(ii)`, `(iii)` sub-sub-clauses |

Roman gets wider hanging indent (480 vs 360) because `(viii)` and `(ix)` are wider than `(z)`.

## Element Ordering Rules

**CRITICAL:** `w:abstractNum` elements MUST precede all `w:num` elements in `w:numbering`. Insert via:

```python
first_num = numbering_el.find(qn('w:num'))
if first_num is not None:
    first_num.addprevious(abstractNum_el)
else:
    numbering_el.append(abstractNum_el)
```

**CRITICAL:** `w:numPr` must appear in correct position within `w:pPr` — after `widowControl`, before `suppressLineNumbers`. Use `_apply_numbering()` helper, never `SubElement`.

## Key Functions in `document_factory.py`

| Function | Purpose |
|----------|---------|
| `_setup_custom_numbering(doc)` | Creates abstractNum 100 + 101. Called once at start of `md_to_docx()` |
| `_new_list_instance(doc, abstract_id)` | Creates a new `w:num` pointing to the abstract, with startOverride=1 |
| `_apply_numbering(para, num_id, ilvl)` | Sets `w:numPr` in correct schema position on a paragraph |

## Troubleshooting

- **Items all show (a):** Each item got its own `w:num` with `startOverride=1`. Fix: share one `numId` across all items in a contiguous list.
- **Numbering disappears in Word:** `w:numPr` placed after `w:spacing` in `w:pPr` — out of schema order. Word silently strips it. Fix: use `_apply_numbering()`.
- **Wrong format (numbers instead of letters):** Paragraph points to wrong `abstractNumId`. Verify `numId` → `abstractNumId` chain.
- **Indent wrong:** Check `w:ind` on the `w:lvl`. `left=720` + `hanging=360` = text at 720tw, number at 360tw.
