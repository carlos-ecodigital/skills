#!/usr/bin/env python3
"""
Convert .docx → .pdf via Microsoft Word — standalone CLI
=========================================================

Usage:
    python3 docx_to_pdf.py input.docx [-o output.pdf]

Word-only (no LibreOffice fallback). On macOS uses AppleScript via docx2pdf;
on Windows uses COM automation. Exits non-zero with install instructions if
docx2pdf or Word is unavailable.

Works for any .docx — not just files produced by document-factory.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from document_factory import docx_to_pdf


def main():
    p = argparse.ArgumentParser(description="Convert .docx to .pdf via Microsoft Word")
    p.add_argument("input", help="Input .docx path")
    p.add_argument("-o", "--output", default=None,
                   help="Output .pdf path (default: <input>.pdf)")
    args = p.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    try:
        out = docx_to_pdf(args.input, args.output)
        print(f"PDF: {out}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
