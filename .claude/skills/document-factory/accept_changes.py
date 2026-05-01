#!/usr/bin/env python3
"""
Accept Tracked Changes in .docx
================================

Removes all tracked changes (insertions, deletions, formatting marks) and
returns a clean document.

Two engines available:

    --engine word          Microsoft Word automation (canonical semantics).
                           Slower. May hang on macOS if Word has open docs.
                           Default on Windows. No fallback — clean error if
                           Word unavailable.

    --engine libreoffice   LibreOffice headless via Anthropic's docx skill.
                           Reliable, session-independent. Default on macOS
                           when Word is unavailable.

Usage:
    python3 accept_changes.py input.docx [-o output.docx] [--engine ENGINE]

Default engine: word on Windows, libreoffice on macOS/Linux.
"""

import argparse
import os
import platform
import subprocess
import sys


# ---------------------------------------------------------------------------
# Word engine — canonical semantics, but fragile on macOS
# ---------------------------------------------------------------------------

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


def _accept_with_word(src, dst):
    """Word-based acceptance. Errors clearly if Word is unavailable."""
    system = platform.system()
    if system == "Darwin":
        return _accept_with_word_macos(src, dst)
    if system == "Windows":
        return _accept_with_word_windows(src, dst)
    raise RuntimeError(
        f"Word engine requires macOS or Windows (got {system}). "
        "Use --engine libreoffice instead."
    )


# ---------------------------------------------------------------------------
# LibreOffice engine — via Anthropic's bundled skill (office_bridge)
# ---------------------------------------------------------------------------

def _accept_with_libreoffice(src, dst):
    """Acceptance via Anthropic's docx skill (LibreOffice macro)."""
    from office_bridge import OfficeBridge
    bridge = OfficeBridge()
    return bridge.accept_changes(src, dst)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def accept_changes(src, dst=None, engine=None):
    """Accept all tracked changes in a .docx.

    Args:
        src: input .docx path
        dst: output path (default: <src>_accepted.docx)
        engine: "word" | "libreoffice" | None.
                None auto-selects: libreoffice on macOS/Linux, word on Windows.

    Returns the output path. Raises RuntimeError if the chosen engine fails.
    """
    src = os.path.abspath(src)
    if not os.path.exists(src):
        raise FileNotFoundError(src)
    if dst is None:
        base, ext = os.path.splitext(src)
        dst = f"{base}_accepted{ext}"
    dst = os.path.abspath(dst)

    if engine is None:
        engine = "word" if platform.system() == "Windows" else "libreoffice"

    if engine == "word":
        return _accept_with_word(src, dst)
    if engine == "libreoffice":
        return _accept_with_libreoffice(src, dst)
    raise ValueError(f"Unknown engine: {engine!r}. Use 'word' or 'libreoffice'.")


def main():
    p = argparse.ArgumentParser(
        description="Accept all tracked changes in a .docx",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Usage:")[0].strip(),
    )
    p.add_argument("input", help="Input .docx path")
    p.add_argument("-o", "--output", default=None,
                   help="Output path (default: <input>_accepted.docx)")
    p.add_argument("--engine", choices=("word", "libreoffice"), default=None,
                   help="Acceptance engine (default: word on Windows, libreoffice elsewhere)")
    args = p.parse_args()
    try:
        out = accept_changes(args.input, args.output, args.engine)
        print(f"Accepted ({args.engine or 'auto'}): {out}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
