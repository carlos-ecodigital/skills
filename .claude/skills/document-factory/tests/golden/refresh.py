#!/usr/bin/env python3
"""Regenerate goldens for all profiles.

Run this when intentional changes land and the PR reviewer will see the
diff in the committed `.xml.txt` extracts.

Usage:
    python3 tests/golden/refresh.py              # all profiles
    python3 tests/golden/refresh.py letter       # one profile
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

_THIS = Path(__file__).resolve().parent
_FACTORY = _THIS.parent.parent  # document-factory/
_GENERATE = _FACTORY / "generate.py"
_NORMALIZE = _FACTORY / "tools" / "normalize_docx.py"
_CURRENT = _THIS / "current"

sys.path.insert(0, str(_THIS / "inputs"))
from fixtures import FIXTURES  # noqa: E402


def refresh(profile: str) -> None:
    if profile not in FIXTURES:
        raise SystemExit(f"Unknown profile: {profile}. Known: {list(FIXTURES)}")

    _CURRENT.mkdir(parents=True, exist_ok=True)
    docx_out = _CURRENT / f"{profile}.docx"
    xml_out = _CURRENT / f"{profile}.xml.txt"

    args = list(FIXTURES[profile]["cli_args"])
    args += ["--output", str(docx_out)]

    # Run from factory dir so relative imports work
    result = subprocess.run(
        [sys.executable, str(_GENERATE), *args],
        cwd=_FACTORY,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(
            f"generate.py failed for {profile}:\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )

    # Normalize to xml.txt
    norm = subprocess.run(
        [sys.executable, str(_NORMALIZE), str(docx_out), "-o", str(xml_out)],
        cwd=_FACTORY,
        capture_output=True,
        text=True,
    )
    if norm.returncode != 0:
        raise SystemExit(
            f"normalize_docx.py failed for {profile}:\n"
            f"stderr: {norm.stderr}"
        )
    print(f"refreshed: {docx_out.name} + {xml_out.name}")


def main() -> int:
    profiles = sys.argv[1:] or list(FIXTURES)
    for p in profiles:
        refresh(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
