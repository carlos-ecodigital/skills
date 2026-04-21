# Test Markdown Report

This is the fixed markdown fixture used by the `markdown` golden test.
It exercises a representative set of markdown features so regressions in
the renderer are caught.

## Section One

Plain paragraph with **bold** and *italic* inline formatting.

- Bullet one
- Bullet two with `inline code`
- Bullet three

## Section Two — Numbered

1. First numbered item
2. Second numbered item
3. Third numbered item

## Section Three — Table

| Metric | Q1 2026 | Target |
|---|---|---|
| Revenue | €1.2M | €1.5M |
| Pipeline | €4.5M | €5.0M |
| Headcount | 12 | 15 |

## Section Four — Blockquote

> This is a blockquote used to verify italic + left indent rendering.

## Section Five — Alphabetic sub-list

The agreement includes:

(a) first condition
(b) second condition
(c) third condition

with the following roman sub-clauses:

(i) sub-condition one
(ii) sub-condition two
