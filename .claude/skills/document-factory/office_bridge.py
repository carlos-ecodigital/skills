#!/usr/bin/env python3
"""
Office Bridge — Runtime discovery of Anthropic's office-skills toolchain
========================================================================

Discovers and wraps Anthropic's bundled docx/pdf/xlsx/pptx skill scripts
at runtime. These scripts live in session-scoped directories managed by
Claude Code and update automatically with each Anthropic release.

Document Factory owns CREATION (python-docx, branded output).
This bridge adds VALIDATION, EDITING, and CONVERSION capabilities
from Anthropic's toolchain without forking or copying their code.

Usage:
    from office_bridge import OfficeBridge

    bridge = OfficeBridge()

    # Validate a .docx before sending externally
    bridge.validate("output.docx")

    # Convert .docx to PDF via LibreOffice (fallback when Word unavailable)
    bridge.to_pdf("output.docx", "output.pdf")

    # Unpack .docx for XML editing (tracked changes, comments)
    bridge.unpack("output.docx", "unpacked/")

    # Repack after editing
    bridge.pack("unpacked/", "output_edited.docx", original="output.docx")

    # Insert comments
    bridge.add_comment("unpacked/", comment_id=0, text="Review this clause")

    # Convert legacy .doc to .docx
    bridge.doc_to_docx("legacy.doc")

    # PDF operations
    bridge.pdf_to_images("input.pdf", "pages/")
    bridge.fill_pdf_form("template.pdf", {"field": "value"}, "filled.pdf")

Design principles:
    - NEVER copy Anthropic scripts into this repo. Discover at runtime.
    - Fail gracefully: if scripts aren't found, raise clear error with
      instructions (not silent failure, not crash).
    - Session path changes every time Claude Code starts. Discovery must
      be dynamic, not hardcoded.
    - Document Factory's document_factory.py remains the SOLE creation engine.
      This bridge adds post-creation capabilities only.
"""

import glob
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional, List


class OfficeBridgeError(Exception):
    """Raised when Anthropic skill scripts are not available."""
    pass


class OfficeBridge:
    """Runtime discovery and wrapper for Anthropic's office-skills toolchain."""

    # Glob pattern to find Anthropic's skill scripts.
    # Structure: ~/Library/Application Support/Claude/local-agent-mode-sessions/
    #            skills-plugin/*/1ae798b7-*/skills/{docx,pdf,xlsx,pptx}/scripts/
    DISCOVERY_BASE = os.path.expanduser(
        "~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin"
    )
    # The inner UUID is stable across sessions (it's the skill-set ID, not session ID)
    SKILL_SET_PATTERN = "*/1ae798b7-*/skills"

    def __init__(self):
        self._cache = {}  # skill_name -> resolved path
        self._discover()

    def _discover(self):
        """Find the latest session's skill scripts."""
        base = self.DISCOVERY_BASE
        if not os.path.exists(base):
            return  # Not in a Claude Code session — bridge unavailable

        # Find all skill directories, sort by modification time (newest first)
        pattern = os.path.join(base, self.SKILL_SET_PATTERN)
        matches = sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)

        if not matches:
            return

        skills_root = matches[0]  # Most recent session's skills

        for skill_name in ("docx", "pdf", "xlsx", "pptx"):
            skill_path = os.path.join(skills_root, skill_name)
            if os.path.isdir(skill_path):
                self._cache[skill_name] = skill_path

    @property
    def available_skills(self) -> List[str]:
        """List which Anthropic skills are available in this session."""
        return list(self._cache.keys())

    def _script(self, skill: str, *path_parts: str) -> str:
        """Resolve a script path within an Anthropic skill."""
        if skill not in self._cache:
            raise OfficeBridgeError(
                f"Anthropic '{skill}' skill not found. "
                f"This feature requires a Claude Code session with the {skill} skill loaded. "
                f"Searched: {self.DISCOVERY_BASE}/{self.SKILL_SET_PATTERN}/{skill}/"
            )
        full_path = os.path.join(self._cache[skill], "scripts", *path_parts)
        if not os.path.exists(full_path):
            raise OfficeBridgeError(
                f"Script not found: {full_path}. "
                f"Anthropic may have restructured the {skill} skill. "
                f"Check for updates."
            )
        return full_path

    def _run(self, script: str, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        """Run a Python script with arguments."""
        cmd = [sys.executable, script, *args]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if check and result.returncode != 0:
            raise OfficeBridgeError(
                f"Script failed: {os.path.basename(script)}\n"
                f"stderr: {result.stderr}\n"
                f"stdout: {result.stdout}"
            )
        return result

    # ── DOCX Operations ─────────────────────────────────────────

    def validate(self, docx_path: str) -> str:
        """Validate .docx against OOXML schema. Returns validation output."""
        script = self._script("docx", "office", "validate.py")
        result = self._run(script, docx_path)
        return result.stdout

    def unpack(self, docx_path: str, output_dir: str, merge_runs: bool = True) -> str:
        """Unpack .docx to XML for editing."""
        script = self._script("docx", "office", "unpack.py")
        args = [docx_path, output_dir]
        if not merge_runs:
            args.extend(["--merge-runs", "false"])
        result = self._run(script, *args)
        return result.stdout

    def pack(self, unpacked_dir: str, output_path: str,
             original: Optional[str] = None, validate: bool = True) -> str:
        """Repack edited XML into .docx."""
        script = self._script("docx", "office", "pack.py")
        args = [unpacked_dir, output_path]
        if original:
            args.extend(["--original", original])
        if not validate:
            args.extend(["--validate", "false"])
        result = self._run(script, *args)
        return result.stdout

    def add_comment(self, unpacked_dir: str, comment_id: int, text: str,
                    parent: Optional[int] = None, author: str = "Digital Energy") -> str:
        """Add a comment to an unpacked .docx."""
        script = self._script("docx", "comment.py")
        args = [unpacked_dir, str(comment_id), text, "--author", author]
        if parent is not None:
            args.extend(["--parent", str(parent)])
        result = self._run(script, *args)
        return result.stdout

    def accept_changes(self, docx_path: str, output_path: Optional[str] = None) -> str:
        """Accept all tracked changes in a .docx via LibreOffice.

        Wraps Anthropic's docx/scripts/accept_changes.py. LibreOffice is required.
        For Word-based acceptance (canonical semantics, slower, less reliable on
        macOS), use the standalone accept_changes.py CLI with --engine=word.

        Returns the path of the cleaned output file.
        """
        if output_path is None:
            base, ext = os.path.splitext(os.path.abspath(docx_path))
            output_path = f"{base}_accepted{ext}"
        script = self._script("docx", "accept_changes.py")
        result = self._run(script, os.path.abspath(docx_path), os.path.abspath(output_path))
        # Anthropic's script writes to output_path; return that, not stdout
        return output_path

    def to_pdf_word(self, docx_path: str, pdf_path: Optional[str] = None) -> str:
        """Convert .docx to PDF via Microsoft Word (canonical fidelity).

        Uses docx2pdf (AppleScript on macOS, COM on Windows). Slower; may hang
        if Word has open documents on macOS. Raises RuntimeError on failure;
        does NOT auto-fallback. Callers wanting fallback should use to_pdf().
        """
        docx_path = os.path.abspath(docx_path)
        if not os.path.exists(docx_path):
            raise FileNotFoundError(docx_path)
        if pdf_path is None:
            pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
        pdf_path = os.path.abspath(pdf_path)

        try:
            from docx2pdf import convert as _word_convert
        except ImportError:
            raise RuntimeError(
                "docx2pdf not installed. Run: pip install docx2pdf\n"
                "Also requires Microsoft Word."
            )
        try:
            _word_convert(docx_path, pdf_path)
        except Exception as e:
            raise RuntimeError(
                f"Word conversion failed: {e}\n"
                "On macOS: ensure Word is installed and AppleScript is permitted; "
                "close other Word documents if it hangs."
            )
        if not os.path.exists(pdf_path):
            raise RuntimeError("docx2pdf ran but produced no output file.")
        return pdf_path

    def to_pdf_libreoffice(self, docx_path: str, pdf_path: Optional[str] = None) -> str:
        """Convert .docx to PDF via LibreOffice (reliable, headless).

        Fast and session-independent. Used by visual_qa pipeline and as the
        default fallback when Word automation fails.
        """
        script = self._script("docx", "office", "soffice.py")
        args = ["--headless", "--convert-to", "pdf", docx_path]
        if pdf_path:
            outdir = os.path.dirname(os.path.abspath(pdf_path))
            args.extend(["--outdir", outdir])
        result = self._run(script, *args)
        if pdf_path:
            stem = os.path.splitext(os.path.basename(docx_path))[0]
            produced = os.path.join(os.path.dirname(os.path.abspath(pdf_path)), f"{stem}.pdf")
            if produced != os.path.abspath(pdf_path) and os.path.exists(produced):
                os.replace(produced, pdf_path)
            return pdf_path
        return result.stdout.strip() or os.path.splitext(docx_path)[0] + ".pdf"

    def to_pdf(self, docx_path: str, pdf_path: Optional[str] = None,
               prefer: str = "word") -> str:
        """Convert .docx to PDF with automatic fallback.

        prefer:
            "word" (default) — tries Word first, falls back to LibreOffice on
            failure. Best for user-facing output (canonical rendering).

            "libreoffice" — uses LibreOffice directly (faster, more reliable
            for pipeline / batch / CI work where Word session state is fragile).
        """
        if prefer == "libreoffice":
            return self.to_pdf_libreoffice(docx_path, pdf_path)
        try:
            return self.to_pdf_word(docx_path, pdf_path)
        except (ImportError, RuntimeError, FileNotFoundError):
            return self.to_pdf_libreoffice(docx_path, pdf_path)

    def doc_to_docx(self, doc_path: str) -> str:
        """Convert legacy .doc to .docx via LibreOffice."""
        script = self._script("docx", "office", "soffice.py")
        args = ["--headless", "--convert-to", "docx", doc_path]
        result = self._run(script, *args)
        return result.stdout

    # ── PDF Operations ──────────────────────────────────────────

    def pdf_to_images(self, pdf_path: str, output_dir: str) -> str:
        """Convert PDF pages to images."""
        script = self._script("pdf", "convert_pdf_to_images.py")
        result = self._run(script, pdf_path, output_dir)
        return result.stdout

    def check_pdf_form(self, pdf_path: str) -> str:
        """Check if PDF has fillable form fields."""
        script = self._script("pdf", "check_fillable_fields.py")
        result = self._run(script, pdf_path, check=False)
        return result.stdout

    def extract_form_fields(self, pdf_path: str) -> str:
        """Extract form field information from PDF."""
        script = self._script("pdf", "extract_form_field_info.py")
        result = self._run(script, pdf_path)
        return result.stdout

    def fill_pdf_form(self, pdf_path: str, field_values: dict,
                      output_path: Optional[str] = None) -> str:
        """Fill PDF form fields programmatically."""
        script = self._script("pdf", "fill_fillable_fields.py")
        # Build args from field_values dict
        args = [pdf_path]
        if output_path:
            args.extend(["-o", output_path])
        for key, value in field_values.items():
            args.extend(["--field", f"{key}={value}"])
        result = self._run(script, *args)
        return result.stdout

    # ── XLSX Operations ─────────────────────────────────────────

    def validate_xlsx(self, xlsx_path: str) -> str:
        """Validate .xlsx against schema."""
        script = self._script("xlsx", "office", "validate.py")
        result = self._run(script, xlsx_path)
        return result.stdout

    def recalc_xlsx(self, xlsx_path: str) -> str:
        """Recalculate formulas in .xlsx."""
        script = self._script("xlsx", "recalc.py")
        result = self._run(script, xlsx_path)
        return result.stdout

    # ── PPTX Operations ─────────────────────────────────────────

    def validate_pptx(self, pptx_path: str) -> str:
        """Validate .pptx against schema."""
        script = self._script("pptx", "office", "validate.py")
        result = self._run(script, pptx_path)
        return result.stdout

    # ── Utility ─────────────────────────────────────────────────

    def status(self) -> dict:
        """Report bridge status — which skills available, paths resolved."""
        return {
            "available": self.available_skills,
            "discovery_base": self.DISCOVERY_BASE,
            "resolved_paths": dict(self._cache),
            "python": sys.executable,
        }


# ── CLI ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    import json
    bridge = OfficeBridge()
    if len(sys.argv) < 2:
        print(json.dumps(bridge.status(), indent=2))
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    try:
        if cmd == "status":
            print(json.dumps(bridge.status(), indent=2))
        elif cmd == "validate" and args:
            print(bridge.validate(args[0]))
        elif cmd == "unpack" and len(args) >= 2:
            print(bridge.unpack(args[0], args[1]))
        elif cmd == "pack" and len(args) >= 2:
            original = args[2] if len(args) > 2 else None
            print(bridge.pack(args[0], args[1], original=original))
        elif cmd == "to-pdf" and args:
            print(bridge.to_pdf_libreoffice(args[0]))
        elif cmd == "doc-to-docx" and args:
            print(bridge.doc_to_docx(args[0]))
        elif cmd == "pdf-images" and len(args) >= 2:
            print(bridge.pdf_to_images(args[0], args[1]))
        else:
            print(f"Unknown command or missing args: {cmd} {args}")
            print("Commands: status, validate, unpack, pack, to-pdf, doc-to-docx, pdf-images")
            sys.exit(1)
    except OfficeBridgeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
