#!/usr/bin/env python3
"""Normalize a .docx into a deterministic text extract for golden diffing.

Strips volatile attributes (rsid* revision-save IDs, run IDs, document GUIDs,
created/modified timestamps) that vary across otherwise-identical saves.
Produces a single text stream concatenating normalized XML for every part,
with per-part markers, stable element attribute ordering, and pretty-printed
indentation.

Usage (CLI):
    python3 normalize_docx.py INPUT.docx             # prints to stdout
    python3 normalize_docx.py INPUT.docx -o OUT.txt  # writes to file

Usage (import):
    from normalize_docx import normalize
    text = normalize("path/to/doc.docx")

This is the basis of the Layer 1 golden byte-diff: goldens are committed as
`*.xml.txt` files. CI runs `normalize()` on freshly-generated .docx and
string-diffs against golden.
"""
from __future__ import annotations

import argparse
import io
import re
import sys
import zipfile
from pathlib import Path

from lxml import etree

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# Attribute names that vary across saves. We strip them before serialization.
# Names are local (namespace-stripped) because lxml attribute matching on full
# QName is verbose; we match by localname after splitting.
VOLATILE_ATTRS_LOCAL = frozenset({
    "rsid",        # w:rsid on runs/paragraphs
    "rsidR",
    "rsidRPr",
    "rsidP",
    "rsidRDefault",
    "rsidTr",
    "rsidDel",
    "rsidSect",
    "rsidRoot",
})

# Elements (by full QName) whose content is a timestamp or GUID and should be
# replaced with a placeholder.
VOLATILE_ELEMENT_TEXT = {
    "{http://purl.org/dc/terms/}created": "[NORMALIZED-TIMESTAMP]",
    "{http://purl.org/dc/terms/}modified": "[NORMALIZED-TIMESTAMP]",
    "{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}"
    "TotalTime": "[NORMALIZED-TOTALTIME]",
}

# Parts we include in the normalized extract. Order is stable (sorted).
INCLUDED_PREFIXES = (
    "word/",
    "docProps/",
    "[Content_Types].xml",
    "_rels/.rels",
)


def _strip_volatile_attrs(root: etree._Element) -> None:
    """Remove rsid-family attributes everywhere in the tree, in place."""
    for el in root.iter():
        # Iterate over a list copy since we mutate attrib.
        for qname in list(el.attrib.keys()):
            local = etree.QName(qname).localname
            if local in VOLATILE_ATTRS_LOCAL:
                del el.attrib[qname]


def _normalize_volatile_text(root: etree._Element) -> None:
    """Replace timestamp/GUID element text with placeholders."""
    for el in root.iter():
        if el.tag in VOLATILE_ELEMENT_TEXT and el.text:
            el.text = VOLATILE_ELEMENT_TEXT[el.tag]


def _canonicalize_xml(xml_bytes: bytes) -> str:
    """Parse, strip volatile content, serialize with stable formatting."""
    try:
        tree = etree.fromstring(xml_bytes)
    except etree.XMLSyntaxError as e:
        # Not valid XML (e.g., binary image ref); return empty — caller decides.
        return f"<!-- XML PARSE ERROR: {e} -->\n"

    _strip_volatile_attrs(tree)
    _normalize_volatile_text(tree)

    # Serialize with pretty printing. We parse again through a parser that
    # removes blank text so pretty_print produces stable indentation
    # regardless of input whitespace.
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.fromstring(etree.tostring(tree), parser)

    return etree.tostring(
        tree,
        pretty_print=True,
        xml_declaration=True,
        encoding="UTF-8",
        standalone=True,
    ).decode("utf-8")


def _should_include(name: str) -> bool:
    return any(name == p or name.startswith(p) for p in INCLUDED_PREFIXES)


def normalize(docx_path: str | Path) -> str:
    """Return a stable, deterministic text extract of the .docx.

    The extract concatenates, in lexicographic part order:
        ==== <part_name> ====
        <normalized XML>

    for every XML part matching the INCLUDED_PREFIXES filter.
    """
    docx_path = Path(docx_path)
    if not docx_path.exists():
        raise FileNotFoundError(docx_path)

    parts: list[tuple[str, str]] = []
    with zipfile.ZipFile(docx_path) as zf:
        for name in sorted(zf.namelist()):
            if not _should_include(name):
                continue
            if not name.endswith(".xml") and not name.endswith(".rels"):
                # Skip binaries (images, fonts embedded, etc.) — they're not
                # what goldens are about.
                continue
            raw = zf.read(name)
            parts.append((name, _canonicalize_xml(raw)))

    buf = io.StringIO()
    for name, xml_text in parts:
        buf.write(f"==== {name} ====\n")
        buf.write(xml_text)
        if not xml_text.endswith("\n"):
            buf.write("\n")
    return buf.getvalue()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("docx", help="Input .docx path")
    p.add_argument("-o", "--output", help="Output file (default: stdout)")
    args = p.parse_args()

    text = normalize(args.docx)
    if args.output:
        Path(args.output).write_text(text)
        print(f"wrote {args.output} ({len(text):,} chars)", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
