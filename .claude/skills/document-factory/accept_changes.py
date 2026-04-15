#!/usr/bin/env python3
"""
Accept Tracked Changes in .docx — Microsoft Word only
======================================================

Usage:
    python3 accept_changes.py input.docx [-o output.docx]

Word is the canonical .docx engine on the team's machines. This script drives
Word via AppleScript (macOS) or COM (Windows). There is no LibreOffice
fallback — LibreOffice's tracked-changes semantics diverge from Word and
silent drift is worse than a clean error.

Exits non-zero with install instructions if Word is not available.
"""

import argparse
import os
import platform
import subprocess
import sys


def _accept_with_word_macos(src, dst):
    """Drive Word.app on macOS via AppleScript."""
    script = f'''
    with timeout of 300 seconds
    tell application "Microsoft Word"
        open POSIX file "{src}"
        delay 2
        tell document 1
            repeat while (count of revisions) > 0
                try
                    accept revision 1
                on error
                    exit repeat
                end try
            end repeat
            save as file name "{dst}" file format format document
            close saving no
        end tell
    end tell
    end timeout
    '''
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True, text=True, timeout=180,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Word (AppleScript) failed: {result.stderr.strip()}\n"
            "Ensure Microsoft Word is installed and AppleScript automation is permitted "
            "(System Settings → Privacy & Security → Automation)."
        )
    if not os.path.exists(dst):
        raise RuntimeError("Word did not produce output file.")
    return dst


def _accept_with_word_windows(src, dst):
    """Drive Word on Windows via COM automation."""
    try:
        import win32com.client  # type: ignore
    except ImportError:
        raise RuntimeError("pywin32 not installed. Run: pip install pywin32")
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(os.path.abspath(src))
        doc.AcceptAllRevisions()
        doc.SaveAs(os.path.abspath(dst), FileFormat=16)  # wdFormatXMLDocument
        doc.Close(False)
    finally:
        word.Quit()
    return dst


def accept_changes(src, dst=None):
    """Accept all tracked changes in a .docx via Microsoft Word.

    Returns the output path. Raises RuntimeError if Word is unavailable or fails.
    """
    src = os.path.abspath(src)
    if not os.path.exists(src):
        raise FileNotFoundError(src)
    if dst is None:
        base, ext = os.path.splitext(src)
        dst = f"{base}_accepted{ext}"
    dst = os.path.abspath(dst)

    system = platform.system()
    if system == "Darwin":
        return _accept_with_word_macos(src, dst)
    if system == "Windows":
        return _accept_with_word_windows(src, dst)
    raise RuntimeError(
        f"Unsupported platform: {system}. This script requires Microsoft Word "
        "(macOS or Windows)."
    )


def main():
    p = argparse.ArgumentParser(description="Accept all tracked changes in a .docx (Word-only)")
    p.add_argument("input", help="Input .docx path")
    p.add_argument("-o", "--output", default=None,
                   help="Output path (default: <input>_accepted.docx)")
    args = p.parse_args()
    try:
        out = accept_changes(args.input, args.output)
        print(f"Accepted: {out}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
