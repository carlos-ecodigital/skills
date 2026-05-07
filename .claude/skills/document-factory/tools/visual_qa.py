#!/usr/bin/env python3
"""Visual regression QA for Document Factory.

Closed-loop pipeline: markdown → docx → audit → pdf → page PNGs → perceptual
hash → HTML report.

Golden baseline storage:
  - Hashes committed to git: tests/visual/golden.json
  - PNGs archived in Drive: {BASE}/QA/visual_golden/{YYYY-MM-DD}/
  - Local scratch: /tmp/docfactory_qa/ (gitignored)

Commands:
    doctor       Pre-flight check: Word/LibreOffice, Python deps, corpus.
    generate     Render all corpus documents (md → docx → pdf → png).
    report       Produce HTML report of current state.
    approve      Promote current snapshots: write golden.json + archive PNGs to Drive.
    diff         Compare current hashes vs golden.json, show changed pages.
    all          doctor + generate + report (default).

Requires: pymupdf, pillow, imagehash. PDF conversion uses office_bridge
(Word primary, LibreOffice fallback).

Usage:
    python3 tools/visual_qa.py [command] [--corpus FILE] [--output PATH]
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

# Make `generate` + `office_bridge` importable regardless of cwd
_THIS = Path(__file__).resolve()
_SKILL = _THIS.parent.parent
sys.path.insert(0, str(_SKILL))


# ---------------------------------------------------------------------------
# Corpus — which markdown files to test against
# ---------------------------------------------------------------------------

_BASE_DRIVE = ("/Users/crmg/Library/CloudStorage/GoogleDrive-carlos@ecodigital.group"
               "/Shared drives/NEW_Ops/Projects Benelux_Ops/Digital Energy")

DEFAULT_CORPUS = [
    ("{BASE}/DE_External_Consultants/Arco Vreugdenhil/20260414_DENL_SAR_Term_Sheet_Arco_Vreugdenhil_v2.0.md",
     "01_sar_term_sheet"),
    ("{BASE}/DE_External_Consultants/Arco Vreugdenhil/20260414_DENL_Advisory_Agreement_Arco_Vreugdenhil_v1.0.md",
     "02_advisory_agreement"),
    ("{BASE}/DE_External_Consultants/Arco Vreugdenhil/20260414_DENL_SAR_Grant_Agreement_Arco_Vreugdenhil_v1.0.md",
     "03_sar_grant_agreement"),
    ("{BASE}/DE_Corporate/SAR_Program/20260414_DENL_SAR_Program_Policy_v1.0.md",
     "04_sar_program_policy"),
    ("{BASE}/DE_Corporate/SAR_Program/20260414_DENL_Board_Resolution_SAR_Program_Adoption_v1.0.md",
     "05_board_sar_adoption"),
    ("{BASE}/DE_Corporate/SAR_Program/20260414_DENL_Board_Resolution_HAB_Establishment_v1.0.md",
     "06_board_hab_establishment"),
    ("{BASE}/DE_Corporate/SAR_Program/20260414_DENL_HAB_Terms_of_Reference_v1.0.md",
     "07_hab_terms_of_reference"),
    ("{BASE}/DE_Corporate/Advisory_Boards/20260414_DENL_Board_Resolution_Horticulture_Advisory_Board_v1.0.md",
     "08_board_horticulture"),
]

GOLDEN_JSON = _SKILL / "tests/visual/golden.json"
DRIVE_GOLDEN_BASE = Path(_BASE_DRIVE) / "QA/visual_golden"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class DocResult:
    slug: str
    title: str
    md_path: str
    docx_path: str
    pdf_path: str
    page_pngs: list[str] = field(default_factory=list)
    page_hashes: list[str] = field(default_factory=list)  # pHash per page (hex str)
    audit_violations: list[str] = field(default_factory=list)
    error: str | None = None
    # After diff: map page_idx (1-based) → hash distance (int 0..64)
    diff_distances: dict[str, int] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Pipeline steps
# ---------------------------------------------------------------------------

def resolve_corpus(corpus_arg: str | None) -> list[tuple[str, str]]:
    """Resolve corpus: default, or loaded from JSON file."""
    if not corpus_arg:
        return DEFAULT_CORPUS
    data = json.loads(Path(corpus_arg).read_text())
    # Accept either a list of [path, slug] pairs or list of {path, slug} dicts
    out = []
    for item in data:
        if isinstance(item, dict):
            out.append((item["path"], item["slug"]))
        else:
            out.append(tuple(item))
    return out


def render_docx(md_path: Path, docx_path: Path) -> tuple[str, list[str]]:
    """Generate docx from markdown. Returns (title, audit_violations).

    Uses save_doc without strict mode so we capture violations for the report
    rather than crashing.
    """
    from document_factory import md_to_docx, save_doc, _fix_zoom, audit_document
    md_text = md_path.read_text()
    doc = md_to_docx(md_text, cover=True)
    _fix_zoom(doc)
    violations = audit_document(doc)
    docx_path.parent.mkdir(parents=True, exist_ok=True)
    # strict=False → save regardless, no stderr noise (we've already captured violations)
    save_doc(doc, str(docx_path), strict=False)
    return (doc.core_properties.title or md_path.stem), violations


def docx_to_pdf(docx_path: Path, pdf_path: Path) -> None:
    """Convert .docx → .pdf for visual QA.

    Prefers LibreOffice headless — reliable, session-independent, runs in
    seconds. Word automation via docx2pdf is unreliable for pipeline work
    because it depends on Word's session state (open docs, modal dialogs,
    AppleScript permissions) and frequently times out.

    This is pipeline-specific — for final user-facing PDFs, generate.docx_to_pdf()
    still uses Word (canonical rendering).
    """
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    # Use soffice directly for max reliability
    outdir = pdf_path.parent
    cmd = [
        "soffice", "--headless", "--convert-to", "pdf",
        "--outdir", str(outdir), str(docx_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        raise RuntimeError(f"LibreOffice conversion failed: {result.stderr}")
    # soffice names the output after the input stem; rename if needed
    produced = outdir / f"{docx_path.stem}.pdf"
    if produced != pdf_path and produced.exists():
        produced.rename(pdf_path)
    if not pdf_path.exists() or pdf_path.stat().st_size == 0:
        raise RuntimeError(f"PDF conversion produced no output: {pdf_path}")


def pdf_to_pngs(pdf_path: Path, output_dir: Path, dpi: int = 120) -> list[Path]:
    """Rasterize each PDF page to a PNG. Returns list of page image paths."""
    import fitz  # pymupdf
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Clear stale PNGs so page count changes don't leave orphans
    for old in output_dir.glob("page_*.png"):
        old.unlink()
    pngs: list[Path] = []
    with fitz.open(str(pdf_path)) as pdf:
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        for page_idx, page in enumerate(pdf, start=1):
            pix = page.get_pixmap(matrix=mat, alpha=False)
            out = output_dir / f"page_{page_idx:03d}.png"
            pix.save(str(out))
            pngs.append(out)
    return pngs


def phash(image_path: Path) -> str:
    """Perceptual hash of an image, hex string (16 chars = 64 bits)."""
    import imagehash
    from PIL import Image
    with Image.open(image_path) as img:
        # imagehash.phash is invariant to slight color/antialiasing shifts
        return str(imagehash.phash(img))


def hash_distance(a: str, b: str) -> int:
    """Hamming distance between two hex pHash strings (0 = identical, 64 = max)."""
    import imagehash
    ha = imagehash.hex_to_hash(a)
    hb = imagehash.hex_to_hash(b)
    return ha - hb


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def run_pipeline(corpus: list[tuple[str, str]], output_dir: Path,
                 skip_pdf: bool = False) -> list[DocResult]:
    """Full pipeline per document: md → docx → audit → pdf → pngs → hashes."""
    results: list[DocResult] = []
    (output_dir / "docx").mkdir(parents=True, exist_ok=True)
    (output_dir / "pdf").mkdir(parents=True, exist_ok=True)
    (output_dir / "pages").mkdir(parents=True, exist_ok=True)

    for md_template, slug in corpus:
        md_path = Path(md_template.format(BASE=_BASE_DRIVE))
        docx_path = output_dir / "docx" / f"{slug}.docx"
        pdf_path = output_dir / "pdf" / f"{slug}.pdf"
        page_dir = output_dir / "pages" / slug

        result = DocResult(
            slug=slug, title="",
            md_path=str(md_path), docx_path=str(docx_path), pdf_path=str(pdf_path),
        )

        try:
            if not md_path.exists():
                result.error = f"Source markdown not found: {md_path}"
                results.append(result)
                continue

            title, violations = render_docx(md_path, docx_path)
            result.title = title
            result.audit_violations = violations
            print(f"  [{slug}] {title} — audit: {len(violations)} violations",
                  flush=True)

            if skip_pdf:
                results.append(result)
                continue

            docx_to_pdf(docx_path, pdf_path)
            pngs = pdf_to_pngs(pdf_path, page_dir)
            result.page_pngs = [str(p) for p in pngs]
            result.page_hashes = [phash(p) for p in pngs]
            print(f"    → {len(pngs)} pages rendered + hashed", flush=True)

        except Exception as e:
            result.error = f"{type(e).__name__}: {e}"
            print(f"  [{slug}] ERROR: {result.error}", file=sys.stderr, flush=True)

        results.append(result)
    return results


def compare_to_golden(results: list[DocResult], golden: dict,
                      threshold: int = 5) -> list[tuple[str, int, int]]:
    """Compare current hashes vs golden.json hashes.

    golden: {"slug": {"1": "hexhash", "2": "hexhash", ...}, ...}
    threshold: max hash distance (0-64) before flagging as changed.
    Returns list of (slug, page_idx, distance) for pages that exceed threshold.
    """
    changes = []
    for r in results:
        golden_pages = golden.get(r.slug, {})
        for idx, current_hash in enumerate(r.page_hashes, start=1):
            golden_hash = golden_pages.get(str(idx))
            if golden_hash is None:
                r.diff_distances[str(idx)] = 64
                changes.append((r.slug, idx, 64))
                continue
            d = hash_distance(golden_hash, current_hash)
            r.diff_distances[str(idx)] = d
            if d > threshold:
                changes.append((r.slug, idx, d))
        # Detect pages that exist in golden but not in current (page count change)
        for idx_str in golden_pages:
            idx = int(idx_str)
            if idx > len(r.page_hashes):
                r.diff_distances[idx_str] = 64
                changes.append((r.slug, idx, 64))
    return changes


def build_golden_json(results: list[DocResult]) -> dict:
    """Extract per-page hashes from results for storage in golden.json."""
    return {
        r.slug: {str(i): h for i, h in enumerate(r.page_hashes, start=1)}
        for r in results
        if r.page_hashes
    }


# ---------------------------------------------------------------------------
# HTML report
# ---------------------------------------------------------------------------

_REPORT_CSS = """
* { box-sizing: border-box; }
body { font: 14px/1.5 -apple-system, "Segoe UI", system-ui, sans-serif; margin: 0; background: #0f172a; color: #e2e8f0; }
header { position: sticky; top: 0; background: #0f172a; border-bottom: 1px solid #1e293b; padding: 14px 24px; z-index: 10; }
h1 { margin: 0; font-size: 18px; font-weight: 600; }
.summary { font-size: 12px; color: #94a3b8; margin-top: 4px; }
.summary .ok { color: #22c55e; }
.summary .fail { color: #ef4444; }
main { padding: 24px; }
.doc { background: #1e293b; border-radius: 8px; padding: 18px; margin-bottom: 18px; }
.doc h2 { margin: 0 0 4px 0; font-size: 16px; display: flex; align-items: center; gap: 10px; }
.doc .slug { font-family: SF Mono, Consolas, monospace; font-size: 12px; color: #64748b; }
.status { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; }
.status.pass { background: #14532d; color: #86efac; }
.status.fail { background: #7f1d1d; color: #fca5a5; }
.status.diff { background: #7c2d12; color: #fdba74; }
.violations { background: #0f172a; border: 1px solid #7f1d1d; border-radius: 4px; padding: 10px 14px; margin: 10px 0; font-family: SF Mono, monospace; font-size: 12px; color: #fca5a5; }
.violations ul { margin: 4px 0; padding-left: 18px; }
.pages { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; margin-top: 12px; }
.page { background: #0f172a; border: 1px solid #334155; border-radius: 4px; overflow: hidden; cursor: pointer; position: relative; }
.page img { width: 100%; height: auto; display: block; }
.page .label { padding: 4px 8px; font-size: 11px; color: #94a3b8; display: flex; justify-content: space-between; }
.page.changed { border-color: #f97316; }
.page.changed::after { content: attr(data-diff); position: absolute; top: 4px; right: 4px; background: #f97316; color: #000; font-size: 10px; padding: 2px 5px; border-radius: 3px; font-weight: 600; }
.modal { position: fixed; inset: 0; background: rgba(0,0,0,.92); display: none; align-items: center; justify-content: center; z-index: 100; padding: 20px; }
.modal.open { display: flex; }
.modal img { max-width: 100%; max-height: 100%; }
.error { background: #7f1d1d; color: #fecaca; padding: 10px 14px; border-radius: 4px; margin: 10px 0; font-family: monospace; font-size: 12px; }
"""

_REPORT_JS = """
document.querySelectorAll('.page img').forEach(img => {
    img.addEventListener('click', () => {
        const modal = document.getElementById('modal');
        const modalImg = document.getElementById('modal-img');
        modalImg.src = img.src;
        modal.classList.add('open');
    });
});
document.getElementById('modal').addEventListener('click', e => {
    if (e.target.id === 'modal') e.currentTarget.classList.remove('open');
});
"""


def _esc(s: str) -> str:
    """Minimal HTML escaping."""
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def build_report(results: list[DocResult], output_html: Path,
                 mode: str = "current", threshold: int = 5) -> None:
    """Build an HTML report showing all rendered pages, audit violations, and diffs."""
    n_docs = len(results)
    n_pass = sum(1 for r in results if not r.error and not r.audit_violations)
    n_violations = sum(len(r.audit_violations) for r in results)
    n_changed = sum(
        sum(1 for d in r.diff_distances.values() if d > threshold)
        for r in results
    )

    parts = [
        "<!DOCTYPE html><html><head><meta charset='utf-8'>",
        "<title>Document Factory — Visual QA</title>",
        f"<style>{_REPORT_CSS}</style>",
        "</head><body>",
        "<header>",
        "<h1>Document Factory — Visual QA</h1>",
        "<div class='summary'>",
        f"{n_docs} documents · ",
        f"<span class='{'ok' if n_pass == n_docs else 'fail'}'>{n_pass}/{n_docs} clean</span>",
        f" · {n_violations} audit violations",
    ]
    if mode == "diff":
        parts.append(f" · <span class='{'ok' if n_changed == 0 else 'fail'}'>{n_changed} pages changed vs golden</span>")
    parts.append("</div></header><main>")

    for r in results:
        status = "pass" if not r.error and not r.audit_violations else "fail"
        n_changed_doc = sum(1 for d in r.diff_distances.values() if d > threshold)
        if mode == "diff" and n_changed_doc > 0 and status == "pass":
            status = "diff"
        status_label = {
            "pass": "CLEAN", "fail": "VIOLATIONS",
            "diff": f"{n_changed_doc} PAGES CHANGED"
        }[status]

        parts.append("<div class='doc'>")
        parts.append("<h2>")
        parts.append(f"<span class='status {status}'>{status_label}</span>")
        parts.append(_esc(r.title or r.slug))
        parts.append(f"<span class='slug'>{_esc(r.slug)}</span>")
        parts.append("</h2>")

        if r.error:
            parts.append(f"<div class='error'>ERROR: {_esc(r.error)}</div>")

        if r.audit_violations:
            parts.append(f"<div class='violations'><strong>{len(r.audit_violations)} audit violations:</strong><ul>")
            for v in r.audit_violations:
                parts.append(f"<li>{_esc(v)}</li>")
            parts.append("</ul></div>")

        if r.page_pngs:
            parts.append("<div class='pages'>")
            for idx, png in enumerate(r.page_pngs, start=1):
                rel = os.path.relpath(png, output_html.parent)
                d = r.diff_distances.get(str(idx), 0)
                changed_cls = " changed" if d > threshold else ""
                diff_attr = f" data-diff='Δ {d}'" if d > threshold else ""
                parts.append(f"<div class='page{changed_cls}'{diff_attr}>")
                parts.append(f"<img src='{_esc(rel)}' loading='lazy'>")
                parts.append(f"<div class='label'><span>Page {idx}</span>")
                if d > threshold:
                    parts.append(f"<span>Δ {d}/64</span>")
                parts.append("</div></div>")
            parts.append("</div>")

        parts.append("</div>")

    parts.extend([
        "</main>",
        "<div id='modal' class='modal'><img id='modal-img'></div>",
        f"<script>{_REPORT_JS}</script>",
        "</body></html>",
    ])

    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text("\n".join(parts))


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def save_results(results: list[DocResult], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([asdict(r) for r in results], indent=2))


def load_results(path: Path) -> list[DocResult]:
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    return [DocResult(**d) for d in data]


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_doctor(args) -> int:
    """Pre-flight check. Returns 0 on all-green, 1 on any failure."""
    problems = []

    # Python deps
    for pkg in ("fitz", "PIL", "imagehash"):
        try:
            __import__(pkg if pkg != "PIL" else "PIL.Image")
        except ImportError:
            problems.append(f"Missing Python package: {pkg}")

    # Generate module
    try:
        from document_factory import md_to_docx, audit_document, save_doc  # noqa: F401
    except Exception as e:
        problems.append(f"Cannot import document_factory module: {e}")

    # LibreOffice (soffice) — required for PDF rasterization pipeline
    if shutil.which("soffice") is None:
        problems.append(
            "LibreOffice (soffice) not found. Install with:\n"
            "    brew install --cask libreoffice"
        )

    # Corpus files
    corpus = resolve_corpus(args.corpus)
    for md_template, slug in corpus:
        p = Path(md_template.format(BASE=_BASE_DRIVE))
        if not p.exists():
            problems.append(f"Corpus file missing: {slug} → {p}")

    if problems:
        print("Pre-flight FAILED:", file=sys.stderr)
        for p in problems:
            print(f"  ✗ {p}", file=sys.stderr)
        return 1
    print("Pre-flight OK: Python deps, generate, office_bridge, corpus all present")
    return 0


def cmd_generate(args) -> list[DocResult]:
    output = Path(args.output)
    corpus = resolve_corpus(args.corpus)
    print(f"Generating visual QA artifacts in {output}/ ...")
    results = run_pipeline(corpus, output, skip_pdf=args.skip_pdf)
    save_results(results, output / "results.json")
    print(f"Done. {len(results)} documents processed.")
    return results


def cmd_report(args) -> None:
    output = Path(args.output)
    results = load_results(output / "results.json")
    if not results:
        print("No results found. Run 'generate' first.", file=sys.stderr)
        sys.exit(1)
    # Load golden hashes if available, for Δ annotation
    if GOLDEN_JSON.exists():
        golden = json.loads(GOLDEN_JSON.read_text())
        compare_to_golden(results, golden, threshold=args.threshold)
        mode = "diff"
    else:
        mode = "current"
    report_path = output / "report.html"
    build_report(results, report_path, mode=mode, threshold=args.threshold)
    print(f"Report: file://{report_path}")
    if args.open:
        subprocess.run(["open", str(report_path)])


def cmd_approve(args) -> None:
    """Promote current run to golden baseline.

    1. Compute hashes from current results → write golden.json (in git).
    2. Archive PNGs to Drive: DRIVE_GOLDEN_BASE/YYYY-MM-DD/
    3. Print commit reminder.
    """
    output = Path(args.output)
    results = load_results(output / "results.json")
    if not results:
        print("No results to approve. Run 'generate' first.", file=sys.stderr)
        sys.exit(1)

    # Refuse to approve if any doc has errors or audit violations
    problems = [r for r in results if r.error or r.audit_violations]
    if problems and not args.force:
        print("Refusing to approve — documents have errors/violations:", file=sys.stderr)
        for r in problems:
            if r.error:
                print(f"  ✗ {r.slug}: {r.error}", file=sys.stderr)
            if r.audit_violations:
                print(f"  ✗ {r.slug}: {len(r.audit_violations)} violation(s)", file=sys.stderr)
        print("\nRe-run 'generate' after fixing, or pass --force to override.", file=sys.stderr)
        sys.exit(1)

    # 1. Write golden.json
    golden = build_golden_json(results)
    GOLDEN_JSON.parent.mkdir(parents=True, exist_ok=True)
    GOLDEN_JSON.write_text(json.dumps(golden, indent=2, sort_keys=True) + "\n")
    print(f"Wrote: {GOLDEN_JSON} ({sum(len(p) for p in golden.values())} page hashes)")

    # 2. Archive PNGs to Drive
    today = date.today().isoformat()
    archive_dir = DRIVE_GOLDEN_BASE / today
    if archive_dir.exists() and not args.force:
        print(f"Archive already exists for today: {archive_dir}", file=sys.stderr)
        print("Pass --force to overwrite, or wait until tomorrow.", file=sys.stderr)
        sys.exit(1)
    if archive_dir.exists():
        shutil.rmtree(archive_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)
    for r in results:
        if not r.page_pngs:
            continue
        doc_dir = archive_dir / r.slug
        doc_dir.mkdir(exist_ok=True)
        for png_str in r.page_pngs:
            png = Path(png_str)
            if png.exists():
                shutil.copy2(png, doc_dir / png.name)
    print(f"Archived PNGs to: {archive_dir}")

    # 3. Reminder
    print("")
    print("Next steps:")
    print(f"  1. Review the archive in Drive: {archive_dir}")
    print(f"  2. git add {GOLDEN_JSON.relative_to(_SKILL.parent.parent)}")
    print(f"  3. git commit -m 'chore: update visual golden baseline {today}'")


def cmd_diff(args) -> None:
    output = Path(args.output)
    if not GOLDEN_JSON.exists():
        print(f"No golden baseline at {GOLDEN_JSON}. Run 'approve' first.",
              file=sys.stderr)
        sys.exit(1)
    results = load_results(output / "results.json")
    if not results:
        print("No current results. Run 'generate' first.", file=sys.stderr)
        sys.exit(1)
    golden = json.loads(GOLDEN_JSON.read_text())
    changes = compare_to_golden(results, golden, threshold=args.threshold)

    report_path = output / "diff_report.html"
    build_report(results, report_path, mode="diff", threshold=args.threshold)

    print(f"Diff report: file://{report_path}")
    print(f"{len(changes)} page(s) changed beyond threshold {args.threshold}/64")
    for slug, idx, d in changes[:20]:
        print(f"  {slug} page {idx}: Δ {d}/64")
    if len(changes) > 20:
        print(f"  ... +{len(changes) - 20} more")
    if args.open:
        subprocess.run(["open", str(report_path)])
    sys.exit(1 if changes else 0)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Visual regression QA for Document Factory.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("command",
                    choices=["doctor", "generate", "report", "approve", "diff", "all"],
                    nargs="?", default="all")
    ap.add_argument("--output", default="/tmp/docfactory_qa",
                    help="Working directory for current artifacts")
    ap.add_argument("--corpus", default=None,
                    help="Path to JSON corpus file (default: DEFAULT_CORPUS)")
    ap.add_argument("--open", action="store_true",
                    help="Open report in browser")
    ap.add_argument("--force", action="store_true",
                    help="Skip safety checks (overwrite archives, approve dirty results)")
    ap.add_argument("--threshold", type=int, default=5,
                    help="Hash-distance threshold 0..64 for regression (default 5)")
    ap.add_argument("--skip-pdf", action="store_true",
                    help="Skip PDF rendering (audit only)")
    args = ap.parse_args()

    if args.command == "doctor":
        sys.exit(cmd_doctor(args))
    if args.command in ("generate", "all"):
        if args.command == "all":
            rc = cmd_doctor(args)
            if rc != 0:
                sys.exit(rc)
        cmd_generate(args)
    if args.command in ("report", "all"):
        cmd_report(args)
    if args.command == "approve":
        cmd_approve(args)
    if args.command == "diff":
        cmd_diff(args)


if __name__ == "__main__":
    main()
