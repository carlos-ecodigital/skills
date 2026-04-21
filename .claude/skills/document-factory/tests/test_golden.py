"""Layer 1 — Golden byte-diff (after normalization) for every profile.

Regenerates each profile with the fixed fixtures in
`tests/golden/inputs/fixtures.py` and diffs the normalized extract against
the committed golden at `tests/golden/current/<profile>.xml.txt`.

When an intentional change lands:
    python3 tests/golden/refresh.py
then review the diff in the committed `.xml.txt` files in the PR.
"""
from __future__ import annotations

import difflib
import subprocess
import sys
from pathlib import Path

import pytest

_THIS = Path(__file__).resolve().parent
_FACTORY = _THIS.parent
_GENERATE = _FACTORY / "generate.py"
_NORMALIZE = _FACTORY / "tools" / "normalize_docx.py"
_CURRENT = _THIS / "golden" / "current"

sys.path.insert(0, str(_THIS / "golden" / "inputs"))
from fixtures import FIXTURES  # type: ignore[import-not-found]  # noqa: E402


@pytest.fixture(scope="module")
def tmp_out(tmp_path_factory):
    return tmp_path_factory.mktemp("golden_fresh")


@pytest.mark.parametrize("profile", sorted(FIXTURES.keys()))
def test_golden(profile: str, tmp_out: Path) -> None:
    """Every profile regenerates byte-identical to its golden (after normalization)."""
    docx_out = tmp_out / f"{profile}.docx"
    xml_out = tmp_out / f"{profile}.xml.txt"

    args = [sys.executable, str(_GENERATE)] + list(FIXTURES[profile]["cli_args"])
    args += ["--output", str(docx_out)]
    gen = subprocess.run(args, cwd=_FACTORY, capture_output=True, text=True)
    assert gen.returncode == 0, (
        f"generate.py failed for {profile}:\n"
        f"stdout: {gen.stdout}\nstderr: {gen.stderr}"
    )

    norm = subprocess.run(
        [sys.executable, str(_NORMALIZE), str(docx_out), "-o", str(xml_out)],
        cwd=_FACTORY,
        capture_output=True,
        text=True,
    )
    assert norm.returncode == 0, (
        f"normalize_docx.py failed for {profile}:\nstderr: {norm.stderr}"
    )

    golden_path = _CURRENT / f"{profile}.xml.txt"
    assert golden_path.exists(), (
        f"Golden missing for {profile}. Run: python3 tests/golden/refresh.py {profile}"
    )

    fresh = xml_out.read_text()
    golden = golden_path.read_text()

    if fresh != golden:
        # Produce a readable diff (first 80 lines of unified diff)
        diff = list(
            difflib.unified_diff(
                golden.splitlines(keepends=True),
                fresh.splitlines(keepends=True),
                fromfile=f"golden/{profile}.xml.txt",
                tofile=f"fresh/{profile}.xml.txt",
                n=3,
            )
        )
        excerpt = "".join(diff[:80])
        pytest.fail(
            f"{profile} diverges from golden. First 80 diff lines:\n{excerpt}\n"
            f"If this change is intentional, run:\n"
            f"  python3 tests/golden/refresh.py {profile}\n"
            f"and commit the updated golden."
        )
