"""Pipeline B — preserving docx→docx rebrand.

Takes an existing .docx and applies DE branding (cover, headers, footers)
without re-authoring the body. Native numbering, lists, tables,
defined-term bolding, and tracked changes are preserved as-is.

When to use:
  - Bespoke deals already drafted in Word.
  - Outside-counsel or counterparty-supplied drafts we need to rebrand.
  - Documents that must preserve tracked changes.

When NOT to use:
  - New drafts we originate — use Pipeline A (legal-assistant or
    build_agreement) for deterministic, QA-validated output.

Architecture:
  1. Validate the RebrandSpec (reuses M2 validators — wrong inputs rejected
     at the spec boundary, same policy as Pipeline A).
  2. Build a DE shell via `profile_agreement()` — this gives us a
     python-docx document with the factory's cover, headers, footers, and
     styles already applied.
  3. Unpack shell + input via OfficeBridge.
  4. Merge input's `numbering.xml` into shell's with range-based remap —
     guaranteed collision-free (learned the hard way in the M-1 spike).
  5. Copy body content from input into shell, stripping:
       - The shell's `[Agreement content begins here…]` placeholder.
       - The input's old cover paragraphs (everything before UNDERSIGNED
         or recitals).
       - The `THE UNDERSIGNED` block itself (R-21 auto-fix — cover already
         carries parties).
       - Date prefix collapsed into the UNDERSIGNED line (multi-run aware).
     All copied paragraphs have `numId` references rewritten to match the
     remapped numbering.xml.
  6. Repack via OfficeBridge (includes OOXML validation).
  7. Caller may optionally run `audit_agreement()` on the output.

Covered by golden pairs (tests/test_rebrand.py):
  - Authored LOI with UNDERSIGNED + collapsed-date prefix.
  - Counsel-drafted binding MSA stub (RECITALS / AGREED TERMS,
    `(A)/(B)/(C)` recitals, EXECUTED AS A DEED signature block).
  - Counterparty-supplied non-binding NDA (no UNDERSIGNED / RECITALS /
    AGREED — exercises first-heading fallback in body-start detection).
  - Tracked-changes preservation (one `<w:ins>` + one `<w:del>` with
    `w:author` / `w:date` attributes, asserted to survive unmodified).

Deferred (future milestones):
  - No explicit style-merge step. We rely on shell styles (Inter + DE
    palette) resolving paragraph styles like `Heading 1`. This is fine
    when the input uses standard style names; fails when the input has a
    custom `Heading 1` definition colliding with shell's. A proper
    style merge (DE-wins with numbering-referenced IDs preserved) is
    still deferred.
  - Canonical shell is dynamically generated per rebrand rather than
    checked in as a static `.dotx`. The approved plan preferred static
    shells; dynamic is strictly simpler and reuses the M2-validated
    builder. Static shells can be added later if deterministic
    byte-level shell comparison becomes a requirement.
  - Known edge case in body-start detection: inputs with legitimate
    body content before the first Heading (jurisdictional qualifiers,
    implicit recitals without a RECITALS label) will see that content
    stripped as cover prelude. Mitigation when it surfaces: extend
    `_detect_body_start` with a new marker — do NOT widen the
    UNDERSIGNED regex to cover PARTIES. The R-21 rule intentionally
    scopes to the literal UNDERSIGNED heading.
"""
from __future__ import annotations

import argparse
import copy
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

from lxml import etree

# Make same-dir imports work when run as a script.
_THIS = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS))

from office_bridge import OfficeBridge  # noqa: E402
from validators import (  # noqa: E402
    AgreementValidationError,
    validate_agreement_inputs,
)


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"
NS = {"w": W_NS}


def _qn(tag: str) -> str:
    return f"{W}{tag}"


# ──────────────────────────────────────────────────────────────────────
# Spec


@dataclass(frozen=True)
class RebrandSpec:
    """Inputs for a docx→docx rebrand. Validated at construction time."""

    agreement_type: str
    client: str
    client_address: str
    entity: str = "nl"
    subject: Optional[str] = None
    date_str: Optional[str] = None      # "17 April 2026"; None → today
    version: int = 1
    formality: Optional[str] = None     # None → auto-detect
    client_reg_type: Optional[str] = None
    client_reg_number: Optional[str] = None
    reference: Optional[str] = None
    cover_title: Optional[str] = None

    def __post_init__(self) -> None:
        # Reuse M2 validator. Resolve formality the same way
        # profile_agreement does so the validator sees the effective value.
        from generate import _detect_formality
        resolved = (
            self.formality
            if self.formality is not None
            else _detect_formality(self.agreement_type)
        )
        validate_agreement_inputs(
            agreement_type=self.agreement_type,
            client=self.client,
            client_address=self.client_address,
            formality=resolved,
            client_reg_type=self.client_reg_type,
            client_reg_number=self.client_reg_number,
        )


# ──────────────────────────────────────────────────────────────────────
# UNDERSIGNED detection + body-start heuristic


# Non-anchored: matches 'THE UNDERSIGNED' anywhere in the paragraph text.
# Anchoring with `^` would miss inputs like '19 March 2026THE UNDERSIGNED:'
# where a cover date gets collapsed into the body paragraph.
_UNDERSIGNED_RE = re.compile(r"THE\s+UNDERSIGNED\b", re.IGNORECASE)

# A clause start: "1. Definitions", "2.1 ...", etc. Digits then period/space.
_CLAUSE_START_RE = re.compile(r"^\s*\d+(\.\d+)*\.?\s+[A-Z]")

# "HAVE AGREED AS FOLLOWS:" / "AGREED TERMS" — prelude to clauses.
# Counsel-drafted MSAs commonly use "AGREED TERMS" as a standalone heading.
_AGREED_RE = re.compile(
    r"^\s*(?:HAVE\s+AGREED\s+AS\s+FOLLOWS|AGREED\s+TERMS)\s*[:.]?\s*$",
    re.IGNORECASE,
)

# "RECITALS:" — standalone label that ends the UNDERSIGNED parties block
# and begins the recitals section.
_RECITALS_LABEL_RE = re.compile(r"^\s*RECITALS\s*[:.]?\s*$", re.IGNORECASE)

# Parenthetical recital lettering (A) / (B) / (C) at the start of a paragraph.
_RECITAL_LETTER_RE = re.compile(r"^\s*\([A-Z]\)\s+")

# Shell placeholder emitted by profile_agreement
_SHELL_PLACEHOLDER_RE = re.compile(
    r"^\s*\[Agreement content begins here\."
)


def _para_text(p_el: etree._Element) -> str:
    return "".join(
        (t.text or "") for t in p_el.iter(_qn("t"))
    )


def _is_heading(p_el: etree._Element) -> bool:
    """True if the paragraph has a pStyle with val starting 'Heading'."""
    pPr = p_el.find(_qn("pPr"))
    if pPr is None:
        return False
    pStyle = pPr.find(_qn("pStyle"))
    if pStyle is None:
        return False
    val = pStyle.get(_qn("val"), "")
    return val.startswith("Heading")


def _is_clause_start(p_el: etree._Element) -> bool:
    """Heuristic: heading-styled OR text matches clause-start regex."""
    if _is_heading(p_el):
        return True
    return bool(_CLAUSE_START_RE.match(_para_text(p_el)))


def _detect_body_start(input_body: etree._Element) -> int:
    """Return the child index at which body content starts.

    Priority (highest to lowest):
      1. UNDERSIGNED paragraph — body starts at the parties block (it
         will be stripped by the UNDERSIGNED-block handler).
      2. RECITALS label, AGREED TERMS, or HAVE AGREED AS FOLLOWS —
         body starts here; the label and following content are preserved.
         Handles counsel-drafted MSAs where there's no UNDERSIGNED
         marker but there IS a clear recitals section.
      3. First paragraph matching parenthetical recital lettering
         `(A) …` — body starts at the first recital.
      4. First heading-styled paragraph (fallback for NDAs and other
         shapes that jump straight into clauses without a recital
         preamble).
      5. Keep everything (return 0).
    """
    children = list(input_body)

    def _walk(predicate):
        for i, el in enumerate(children):
            if etree.QName(el).localname != "p":
                continue
            if predicate(el):
                return i
        return None

    # 1. UNDERSIGNED anywhere in paragraph text.
    idx = _walk(lambda el: bool(_UNDERSIGNED_RE.search(_para_text(el))))
    if idx is not None:
        return idx

    # 2. RECITALS / AGREED TERMS / HAVE AGREED AS FOLLOWS label.
    def _is_body_marker(el):
        txt = _para_text(el)
        return bool(_RECITALS_LABEL_RE.match(txt) or _AGREED_RE.match(txt))
    idx = _walk(_is_body_marker)
    if idx is not None:
        return idx

    # 3. First parenthetical recital lettering (A).
    idx = _walk(lambda el: bool(_RECITAL_LETTER_RE.match(_para_text(el))))
    if idx is not None:
        return idx

    # 4. First heading-styled paragraph.
    idx = _walk(_is_heading)
    if idx is not None:
        return idx

    # 5. Keep everything.
    return 0


def _is_undersigned_block_end(p_el: etree._Element) -> bool:
    """The UNDERSIGNED block ends when we hit a heading, a clause-start,
    the 'RECITALS:' label, a recital lettering like '(A)', or
    'HAVE AGREED AS FOLLOWS:'."""
    txt = _para_text(p_el)
    if _RECITALS_LABEL_RE.match(txt):
        return True
    if _AGREED_RE.match(txt):
        return True
    if _is_heading(p_el):
        return True
    if _CLAUSE_START_RE.match(txt):
        return True
    # Recital lettering (A) / (B) / (C)...
    if re.match(r"^\s*\([A-Z]\)\s+", txt):
        return True
    return False


def _strip_date_prefix_in_undersigned(p_el: etree._Element) -> None:
    """The input LOI sometimes collapses a cover date into the UNDERSIGNED
    paragraph: '19 March 2026THE UNDERSIGNED:'. Walk all `w:t` elements
    in document order; drop every one preceding (and including) the
    leading date fragment, keep from 'THE' onward.
    """
    t_elements = list(p_el.iter(_qn("t")))
    for i, t in enumerate(t_elements):
        text = t.text or ""
        m = _UNDERSIGNED_RE.search(text)
        if m:
            # Keep everything from 'THE' forward in this element.
            t.text = text[m.start():]
            # Drop all preceding text elements (they're the date prefix).
            for earlier in t_elements[:i]:
                earlier.text = ""
            return


# ──────────────────────────────────────────────────────────────────────
# Numbering merge (collision-free, range-based)


def _merge_numbering(
    shell_path: Path,
    input_path: Path,
) -> dict[int, int]:
    """Merge input's numbering.xml into shell's. Returns {old_numId: new_numId}.

    Range-based remap: input IDs are shifted to start at max(shell_id) + 1.
    This was proven collision-free in the M-1 spike (and fixed after the
    first naive implementation created duplicates).
    """
    if not input_path.exists():
        return {}
    input_tree = etree.parse(str(input_path))

    if not shell_path.exists():
        # No shell numbering; just copy input over wholesale.
        shutil.copyfile(input_path, shell_path)
        return {}
    shell_tree = etree.parse(str(shell_path))

    shell_root = shell_tree.getroot()
    input_root = input_tree.getroot()

    shell_abs_ids = {
        int(el.get(_qn("abstractNumId")))
        for el in shell_root.findall("w:abstractNum", NS)
    }
    shell_num_ids = {
        int(el.get(_qn("numId"))) for el in shell_root.findall("w:num", NS)
    }

    abs_base = max(shell_abs_ids, default=-1) + 1
    num_base = max(shell_num_ids, default=0) + 1

    abs_map: dict[int, int] = {}
    for offset, el in enumerate(input_root.findall("w:abstractNum", NS)):
        old = int(el.get(_qn("abstractNumId")))
        abs_map[old] = abs_base + offset

    num_map: dict[int, int] = {}
    for offset, el in enumerate(input_root.findall("w:num", NS)):
        old = int(el.get(_qn("numId")))
        num_map[old] = num_base + offset

    # Per OOXML schema, <w:abstractNum> must precede <w:num>. Insert after
    # the last existing abstractNum, or before the first num.
    last_abs = None
    for el in shell_root.findall("w:abstractNum", NS):
        last_abs = el
    first_num_idx = None
    for i, child in enumerate(shell_root):
        if etree.QName(child).localname == "num":
            first_num_idx = i
            break

    def _insert_abstract(new_el: etree._Element) -> None:
        if last_abs is not None:
            last_abs.addnext(new_el)
        elif first_num_idx is not None:
            shell_root.insert(first_num_idx, new_el)
        else:
            shell_root.append(new_el)

    for el in input_root.findall("w:abstractNum", NS):
        new_el = copy.deepcopy(el)
        old_abs = int(new_el.get(_qn("abstractNumId")))
        new_el.set(_qn("abstractNumId"), str(abs_map[old_abs]))
        _insert_abstract(new_el)

    for el in input_root.findall("w:num", NS):
        new_el = copy.deepcopy(el)
        old_num = int(new_el.get(_qn("numId")))
        new_el.set(_qn("numId"), str(num_map[old_num]))
        absref = new_el.find("w:abstractNumId", NS)
        if absref is not None:
            old_abs = int(absref.get(_qn("val")))
            if old_abs in abs_map:
                absref.set(_qn("val"), str(abs_map[old_abs]))
        shell_root.append(new_el)

    shell_tree.write(
        str(shell_path),
        xml_declaration=True,
        encoding="UTF-8",
        standalone=True,
    )
    return num_map


# ──────────────────────────────────────────────────────────────────────
# Body transfer


def _remap_num_refs(el: etree._Element, num_map: dict[int, int]) -> None:
    """Rewrite w:numId/@w:val in the subtree per num_map."""
    if not num_map:
        return
    for numId in el.iter(_qn("numId")):
        val = numId.get(_qn("val"))
        if val is None:
            continue
        try:
            ival = int(val)
        except ValueError:
            continue
        if ival in num_map:
            numId.set(_qn("val"), str(num_map[ival]))


@dataclass
class CopyStats:
    copied: int = 0
    stripped_cover: int = 0
    stripped_undersigned: int = 0
    stripped_shell_placeholder: int = 0
    date_prefix_fixed: bool = False


def _copy_body_into_shell(
    shell_doc_path: Path,
    input_doc_path: Path,
    num_map: dict[int, int],
) -> CopyStats:
    """Transfer input's body content into the shell's document.xml.

    Strips:
      - Shell's `[Agreement content begins here…]` placeholder paragraph.
      - Input's old cover (everything before UNDERSIGNED or first heading).
      - Input's `THE UNDERSIGNED` block (heading + subsequent body
        paragraphs until the next heading/clause/recital/AGREED line).
      - Date prefix collapsed into the UNDERSIGNED paragraph.

    Rewrites `w:numId` references in every copied element.
    """
    stats = CopyStats()

    shell_tree = etree.parse(str(shell_doc_path))
    input_tree = etree.parse(str(input_doc_path))
    shell_body = shell_tree.getroot().find("w:body", NS)
    input_body = input_tree.getroot().find("w:body", NS)
    shell_sectPr = shell_body.find("w:sectPr", NS)

    # 1. Strip shell placeholder paragraphs.
    for p in list(shell_body.findall("w:p", NS)):
        text = _para_text(p)
        if _SHELL_PLACEHOLDER_RE.match(text):
            shell_body.remove(p)
            stats.stripped_shell_placeholder += 1

    # 2. Find body-start in input; skip the old cover prelude.
    start_idx = _detect_body_start(input_body)
    stats.stripped_cover = start_idx  # paragraphs skipped before start

    # 3. Insert a page break before body content so it flows onto page 2.
    page_break_p = etree.SubElement(shell_body, _qn("p"))
    pr = etree.SubElement(page_break_p, _qn("r"))
    br = etree.SubElement(pr, _qn("br"))
    br.set(_qn("type"), "page")
    shell_body.remove(page_break_p)
    shell_sectPr.addprevious(page_break_p)

    # 4. Walk input body from start_idx, skipping the UNDERSIGNED block.
    in_undersigned = False
    children = list(input_body)
    first_para_after_start: Optional[etree._Element] = None

    for i, el in enumerate(children):
        if i < start_idx:
            continue
        local = etree.QName(el).localname
        if local == "sectPr":
            continue

        # UNDERSIGNED heuristic applies to paragraphs only
        if local == "p":
            txt = _para_text(el)
            if _UNDERSIGNED_RE.search(txt):
                in_undersigned = True
                stats.stripped_undersigned += 1
                continue
            if in_undersigned:
                if _is_undersigned_block_end(el):
                    in_undersigned = False
                    # fall through to copy this paragraph (it's the
                    # boundary — a heading / clause / recital / AGREED).
                else:
                    stats.stripped_undersigned += 1
                    continue

        copy_el = copy.deepcopy(el)

        # First copied paragraph may still have the date-prefix artifact
        # "19 March 2026THE UNDERSIGNED:" — we only skip the WHOLE
        # UNDERSIGNED paragraph when _UNDERSIGNED_RE matches anywhere, so
        # that case is already handled above. But if the input has the
        # date prefix on a DIFFERENT paragraph (rare), we don't touch it.
        # Kept for legacy inputs where the cover date bleeds into the
        # first retained paragraph:
        if first_para_after_start is None and local == "p":
            if _UNDERSIGNED_RE.search(_para_text(copy_el)):
                _strip_date_prefix_in_undersigned(copy_el)
                stats.date_prefix_fixed = True
            first_para_after_start = copy_el

        _remap_num_refs(copy_el, num_map)
        shell_sectPr.addprevious(copy_el)
        stats.copied += 1

    shell_tree.write(
        str(shell_doc_path),
        xml_declaration=True,
        encoding="UTF-8",
        standalone=True,
    )
    return stats


# ──────────────────────────────────────────────────────────────────────
# Public API


def _today_str() -> str:
    return date.today().strftime("%d %B %Y").lstrip("0")


def rebrand(
    input_path: str | Path,
    spec: RebrandSpec,
    *,
    stats_out: Optional[dict] = None,
) -> bytes:
    """Rebrand an existing .docx per spec. Returns output .docx bytes.

    `stats_out`, if provided, is populated with a dict describing what
    was stripped/copied — useful for tests and CLI output.
    """
    from generate import profile_agreement, save_doc, _fix_zoom

    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(input_path)

    bridge = OfficeBridge()

    with tempfile.TemporaryDirectory() as tmp_name:
        tmp = Path(tmp_name)
        shell_dir = tmp / "shell_unpacked"
        out_dir = tmp / "out_unpacked"
        shell_docx = tmp / "shell.docx"
        input_dir = tmp / "input_unpacked"
        out_docx = tmp / "out.docx"

        # 1. Build DE shell via Pipeline A's validated builder.
        doc = profile_agreement(
            agreement_type=spec.agreement_type,
            subject=spec.subject,
            client=spec.client,
            client_address=spec.client_address,
            client_reg_type=spec.client_reg_type,
            client_reg_number=spec.client_reg_number,
            date_str=spec.date_str or _today_str(),
            version=spec.version,
            formality=spec.formality,
            entity=spec.entity,
            reference=spec.reference,
            cover_title=spec.cover_title,
        )
        _fix_zoom(doc)
        save_doc(doc, str(shell_docx))

        # 2. Unpack both.
        bridge.unpack(str(shell_docx), str(shell_dir))
        bridge.unpack(str(input_path), str(input_dir))

        # The bridge copies the shell tree to out_dir to leave shell_dir
        # untouched — but office_bridge.pack takes unpacked_dir directly
        # and we're going to mutate shell_dir in place anyway, which
        # matches the spike.
        shutil.copytree(shell_dir, out_dir)

        # 3. Merge numbering.xml.
        num_map = _merge_numbering(
            out_dir / "word" / "numbering.xml",
            input_dir / "word" / "numbering.xml",
        )

        # 4. Copy body, stripping placeholder + old cover + UNDERSIGNED.
        copy_stats = _copy_body_into_shell(
            out_dir / "word" / "document.xml",
            input_dir / "word" / "document.xml",
            num_map,
        )

        # 5. Repack.
        bridge.pack(str(out_dir), str(out_docx), original=str(shell_docx))

        data = out_docx.read_bytes()

    if stats_out is not None:
        stats_out["copied_elements"] = copy_stats.copied
        stats_out["stripped_cover"] = copy_stats.stripped_cover
        stats_out["stripped_undersigned"] = copy_stats.stripped_undersigned
        stats_out["stripped_shell_placeholder"] = (
            copy_stats.stripped_shell_placeholder
        )
        stats_out["date_prefix_fixed"] = copy_stats.date_prefix_fixed
        stats_out["remapped_numIds"] = len(num_map)

    return data


# ──────────────────────────────────────────────────────────────────────
# CLI


def _parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Pipeline B — rebrand an existing .docx with DE cover + "
            "headers/footers, preserving the body."
        )
    )
    p.add_argument("input", help="Input .docx path")
    p.add_argument("--agreement-type", required=True)
    p.add_argument("--client", required=True)
    p.add_argument("--client-address", required=True)
    p.add_argument("--entity", choices=["ag", "nl"], default="nl")
    p.add_argument("--subject", default=None)
    p.add_argument("--date", default=None, help="DD Month YYYY; default: today")
    p.add_argument("--version", type=int, default=1)
    p.add_argument("--formality", choices=["binding", "non_binding"], default=None)
    p.add_argument("--client-reg-type", default=None)
    p.add_argument("--client-reg-number", default=None)
    p.add_argument("--reference", default=None)
    p.add_argument("--cover-title", default=None)
    p.add_argument("-o", "--output", required=True)
    p.add_argument(
        "--audit", action="store_true",
        help="Run audit_agreement on the output and report violations",
    )
    return p.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = _parse_args(argv or sys.argv[1:])
    try:
        spec = RebrandSpec(
            agreement_type=args.agreement_type,
            client=args.client,
            client_address=args.client_address,
            entity=args.entity,
            subject=args.subject,
            date_str=args.date,
            version=args.version,
            formality=args.formality,
            client_reg_type=args.client_reg_type,
            client_reg_number=args.client_reg_number,
            reference=args.reference,
            cover_title=args.cover_title,
        )
    except AgreementValidationError as e:
        print(f"Spec rejected: {e}", file=sys.stderr)
        return 2

    stats: dict = {}
    data = rebrand(args.input, spec, stats_out=stats)
    Path(args.output).write_bytes(data)
    print(f"Rebranded: {args.output}")
    print(
        f"  copied: {stats['copied_elements']} elements "
        f"| stripped: cover={stats['stripped_cover']}, "
        f"undersigned={stats['stripped_undersigned']}, "
        f"shell_placeholder={stats['stripped_shell_placeholder']} "
        f"| numIds remapped: {stats['remapped_numIds']}"
    )

    if args.audit:
        from docx import Document
        from audit_profiles import audit_agreement
        doc = Document(args.output)
        vios = audit_agreement(doc)
        if vios:
            print(f"\nAudit violations ({len(vios)}):")
            for v in vios:
                print(f"  - {v}")
            return 1
        print("\nAudit: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
