"""Pytest configuration for legal-assistant sales tests.

Sets up sys.path so tests can import generate_loi from the sales
package without requiring an installed package layout.

v3.7.2: sets LOI_NO_NETWORK=1 by default so R-29 URL content
verification doesn't hit live URLs during test runs. Individual tests
that exercise R-29 explicitly pass verify_urls=True + url_fetcher=<fake>
to qa_lint().
"""
import os
import sys

# v3.7.2: mandatory for all test runs — disable live network fetches.
os.environ.setdefault("LOI_NO_NETWORK", "1")

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
