"""Golden-file integration tests — v3.5.8 PRINCIPLES.md tripwire #5.

For each intake YAML (6 examples + 4 regression fixtures), regenerate the
.docx, extract a deterministic fingerprint, and diff against a committed
golden under `tests/goldens/`. Mismatch → test fails with a human-readable
diff listing which paragraphs / tables / margins / footer elements
changed.

**Pattern — how operators intentionally update a golden:**

    # 1. Land the render-logic change on a branch
    # 2. Regenerate the affected goldens:
    pytest tests/test_golden_files.py --update-goldens
    # 3. Review the git diff on tests/goldens/*.json — the diff IS the
    #    record of how the render changed
    # 4. Commit the new goldens with the code change

CI runs without --update-goldens, so unexplained diffs fail the PR. This
is the structural regression gate that QA linter rules (R-1..R-28) cannot
provide: a pattern linter fires on known bad strings; the golden catches
any unexplained change to any part of the rendered document.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

try:
    from tests._fingerprint import fingerprint_docx, diff_fingerprints
except Exception:
    # When pytest invokes us from tests/, the module is importable as
    # `_fingerprint` directly.
    from _fingerprint import fingerprint_docx, diff_fingerprints  # type: ignore


_TESTS_DIR = Path(__file__).resolve().parent
_COLOCATION_DIR = _TESTS_DIR.parent
_GOLDENS_DIR = _TESTS_DIR / "goldens"
_EXAMPLES_DIR = _COLOCATION_DIR / "examples"
_REGRESSION_DIRS = [
    _COLOCATION_DIR / "regression" / "v3.5",
    _COLOCATION_DIR / "regression" / "v3.7",  # v3.7.2: 8 new fixtures
]


def _discover_intakes() -> list[tuple[str, Path]]:
    """Return list of (golden_name, intake_path) for parametrised tests.

    Example intakes → `example_<type>.json`
    Regression intakes → `regression_<slug>.json` (v3.5) or
                         `regression_v3_7_<slug>.json` (v3.7)
    """
    out: list[tuple[str, Path]] = []
    for p in sorted(_EXAMPLES_DIR.glob("intake_example_*.yaml")):
        # "intake_example_wholesale.yaml" → "example_wholesale"
        slug = p.stem.replace("intake_", "")
        out.append((slug, p))
    for reg_dir in _REGRESSION_DIRS:
        if not reg_dir.exists():
            continue
        # Include the version in the slug for the newer dirs so v3.5 + v3.7
        # fixtures don't collide (e.g., infrapartners_supplier in v3.5 vs
        # infrapartners_strategic_supplier_v6 in v3.7).
        ver_tag = "" if reg_dir.name == "v3.5" else f"_{reg_dir.name.replace('.', '_')}"
        for p in sorted(reg_dir.glob("*_intake.yaml")):
            # "cerebro_wholesale_intake.yaml" → "regression_v3_7_cerebro_wholesale"
            slug = f"regression{ver_tag}_" + p.stem.replace("_intake", "")
            out.append((slug, p))
    return out


def _regen_docx(intake_path: Path, out_dir: Path) -> Path:
    """Regenerate the .docx from an intake YAML into a temp directory.

    Runs the generator as a subprocess so we get the same PYTHONPATH /
    module resolution as a normal CLI invocation. Returns the path to the
    produced .docx. Raises RuntimeError on QA FAIL or any non-zero exit.
    """
    # Output path — predictable slug so we can locate the file without
    # regex-matching the generator's date-based naming.
    out_docx = out_dir / "regen.docx"
    cmd = [
        sys.executable,
        str(_COLOCATION_DIR / "generate_loi.py"),
        str(intake_path),
        "--output", str(out_docx),
    ]
    result = subprocess.run(
        cmd, cwd=_COLOCATION_DIR, capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"generate_loi.py failed on {intake_path.name} "
            f"(rc={result.returncode}):\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    if not out_docx.exists():
        raise RuntimeError(
            f"generate_loi.py did not produce {out_docx} for {intake_path.name}"
        )
    return out_docx


def _golden_path(slug: str) -> Path:
    return _GOLDENS_DIR / f"{slug}.json"


def _load_golden(slug: str) -> dict | None:
    p = _golden_path(slug)
    if not p.exists():
        return None
    with open(p) as f:
        return json.load(f)


def _save_golden(slug: str, fingerprint: dict) -> None:
    _GOLDENS_DIR.mkdir(parents=True, exist_ok=True)
    p = _golden_path(slug)
    with open(p, "w") as f:
        json.dump(fingerprint, f, indent=2, sort_keys=True)


@pytest.fixture(scope="session")
def update_goldens(request) -> bool:
    """v3.5.8 tripwire #5: `--update-goldens` flag registered in conftest."""
    return bool(request.config.getoption("--update-goldens"))


_INTAKES = _discover_intakes()


@pytest.mark.parametrize(
    "slug,intake_path",
    _INTAKES,
    ids=[slug for slug, _ in _INTAKES],
)
def test_golden_fingerprint(slug: str, intake_path: Path, update_goldens: bool, tmp_path: Path):
    """For each intake, regenerate and compare fingerprint to golden.

    On --update-goldens: write current fingerprint as the new golden and
    skip the diff check. Without the flag (CI default): any diff fails.
    """
    docx_path = _regen_docx(intake_path, tmp_path)
    current = fingerprint_docx(str(docx_path))

    if update_goldens:
        _save_golden(slug, current)
        pytest.skip(f"Golden updated for {slug}")
        return

    golden = _load_golden(slug)
    if golden is None:
        _save_golden(slug, current)
        pytest.skip(
            f"Golden for {slug} did not exist — seeded from current render. "
            f"Review tests/goldens/{slug}.json and commit."
        )
        return

    diffs = diff_fingerprints(golden, current)
    if diffs:
        diff_text = "\n".join(diffs)
        pytest.fail(
            f"Golden fingerprint mismatch for {slug} "
            f"({len(diffs)} difference(s)).\n\n"
            f"If this change is intentional, run:\n"
            f"  pytest tests/test_golden_files.py --update-goldens\n"
            f"and commit the diff in tests/goldens/{slug}.json with your PR.\n\n"
            f"Diff:\n{diff_text}"
        )
