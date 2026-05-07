# Legal Document Patterns

> Catalog of patterns the Document Factory parser recognizes in markdown source files.
> Each pattern maps to a specific rendering strategy in `document_factory.py`.

## Clause Numbering (Hierarchical Decimal)

**Pattern:** `1.`, `1.1`, `1.1.1`, `2.`, `2.1`
**Rendering:** Headings (H2–H4 depending on depth), not list items.
**Detection:** `re.match(r'^\d+(\.\d+)*\.?\s+', line)` — handled by the heading detector in `md_to_docx()`.

Example:
```
## 1. Definitions
### 1.1 "Advisor" means...
### 1.2 "Company" means...
## 2. Engagement
```

## Sub-Clause Lists (Alphabetic)

**Pattern:** `(a)`, `(b)`, `(c)` through `(z)`
**Rendering:** Native Word numbered list using abstractNum 100 (`lowerLetter`, `(%1)`)
**Detection:** `_alpha_re = re.compile(r'^[\s]*\([a-z]\)\s+')`
**Blank-line handling:** Look-ahead skips blank lines between items. List continues until a non-blank, non-matching line.

Example (Advisory Agreement §4.3):
```
(a) Strategic guidance on market positioning...

(b) Introductions to potential partners...

(c) Review and feedback on business plans...
```

## Sub-Sub-Clause Lists (Roman)

**Pattern:** `(i)`, `(ii)`, `(iii)` through `(x)`
**Rendering:** Native Word numbered list using abstractNum 101 (`lowerRoman`, `(%1)`)
**Detection:** `_roman_re = re.compile(r'^[\s]*\((i{1,3}|iv|v|vi{0,3}|ix|x)\)\s+')`
**Ambiguity:** `(i)` alone is ambiguous. If next item is `(ii)` → roman. If `(j)` → alphabetic. Default: alphabetic.

## Bullet Lists

**Pattern:** `- item`, `* item`, `+ item`
**Rendering:** `style='List Bullet'` (level 1) or `style='List Bullet 2'` (indented with 2+ spaces)
**Detection:** `re.match(r'^[\s]*[-*+]\s+', line)`

## Numbered Lists

**Pattern:** `1. item`, `2) item`
**Rendering:** `style='List Number'` (level 1) or `style='List Number 2'` (indented)
**Detection:** `re.match(r'^[\s]*\d+[.)]\s+', line)`

## Definitions

**Pattern:** `"**Term**" means...` or `**"Term"** means...`
**Rendering:** Body paragraph with inline bold on the defined term. No special style.
**Detection:** Handled by inline markdown parser (`_add_inline()`).

## Signature Blocks

### Section Mode (primary)

**Trigger:** Heading matching `_SIG_HEADING_RE`:
```python
re.compile(r'(signatures?|counter[- ]?signatures?|execution|signature\s*page)', re.IGNORECASE)
```

**Exit:** Next heading that does NOT match the pattern (e.g., "## Drafting Notes").

**Structure within section:**
- **Intro paragraph:** "By counter-signing below, the Parties confirm..." → body formatting + `keep_with_next`
- **Party blocks:** Separated by 2+ blank lines
- **Party name:** `**DIGITAL ENERGY NETHERLANDS B.V.**` → bold, `keep_with_next + keep_together`
- **Sig lines:** `By:`, `Name:`, `Title:`, `Signature:`, `Date:`, `___` → `keep_together + keep_with_next`
- **Last line of last party:** `keep_with_next = False`

### Fallback Mode (for documents without ## Signatures heading)

**Detection:** Line-by-line regex `sig_line_re`:
```python
re.compile(r'^(_{3,}|.*\b(Name|Title|Signature|Date|Signed|By)\s*:)', re.IGNORECASE)
```
Applies `keep_together` to matching lines.

### Multi-party layouts

| Layout | Example | Handling |
|--------|---------|----------|
| Single signer | Board resolutions | One party block |
| Dual authority | Company + recipient | Two blocks, 18pt gap |
| Multi-party | Term sheet (3 parties) | Three blocks, 18pt gaps |

## Tables

**Pattern:** Pipe-delimited markdown tables:
```
| Header 1 | Header 2 |
|----------|----------|
| Data 1   | Data 2   |
```

**Detection:** `line.strip().startswith('|') and '|' in line[1:]`
**Rendering:** Full Word table with Cobalt headers, alternating row shading, fixed layout, exact content width.

## Blockquotes

**Pattern:** `> quoted text`
**Rendering:** Body paragraph with `left_indent = Mm(10)`, italic.

## Cross-References

**Pattern:** "Section 7.2", "Article 3", "Schedule A"
**Rendering:** Plain text. No special handling (no hyperlinks or bookmarks).

## Recitals (NOT YET IMPLEMENTED)

**Pattern:** `(A)`, `(B)`, `(C)` or `WHEREAS, ...`
**Status:** Not present in current document corpus. Would need uppercase letter numbering (`upperLetter` numFmt). Flagged as future work.

## Review Markers

**Pattern:** `[REVIEW REQUIRED: explanation text]`
**Rendering:** Stripped from output. Count reported to stderr.
**Future:** Convert to Word comments (deferred).
