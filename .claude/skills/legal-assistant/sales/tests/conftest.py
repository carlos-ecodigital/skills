"""Pytest configuration for legal-assistant colocation tests.

Sets up sys.path so tests can import generate_loi from the colocation
package without requiring an installed package layout.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_COLOCATION = os.path.dirname(_HERE)
_LEGAL_ASSISTANT = os.path.dirname(_COLOCATION)
_SKILLS_ROOT = os.path.dirname(_LEGAL_ASSISTANT)

# Make `generate_loi` importable directly when tests run via pytest.
for p in (_COLOCATION, _LEGAL_ASSISTANT, _SKILLS_ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)


# --- v3.5.8 tripwire #5: golden-file pytest option ---

def pytest_addoption(parser):
    """Register `--update-goldens` flag for test_golden_files.py."""
    parser.addoption(
        "--update-goldens",
        action="store_true",
        default=False,
        help="Regenerate golden fingerprints from current generator output "
             "(v3.5.8 tripwire #5). Review the git diff before committing.",
    )
