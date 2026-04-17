"""Fixed inputs for golden tests.

One entry per profile. `cli_args` is passed verbatim to generate.py.
`date` is always fixed so output is reproducible; all other flags that
could introduce volatility (version, reference, classification) are
pinned.

The markdown profile uses a static markdown fixture committed alongside.
"""
from __future__ import annotations

from pathlib import Path

_THIS = Path(__file__).parent
FIXED_DATE = "2026-04-17"
MD_FIXTURE = _THIS / "sample.md"

FIXTURES = {
    "letter": {
        "cli_args": [
            "--profile", "letter",
            "--date", FIXED_DATE,
            "--version", "1",
        ],
    },
    "agreement": {
        "cli_args": [
            "--profile", "agreement",
            "--agreement-type", "Letter of Intent",
            "--subject", "for AI Infrastructure Services",
            "--client", "Acme Test B.V.",
            "--client-address", "123 Test Straat, 1000 AA Amsterdam, the Netherlands",
            "--entity", "nl",
            "--date", FIXED_DATE,
            "--version", "1",
        ],
    },
    "seed_memo": {
        "cli_args": [
            "--profile", "seed_memo",
            "--client", "Test Seed Fund",
            "--date", FIXED_DATE,
            "--version", "1",
        ],
    },
    "investor_memo": {
        "cli_args": [
            "--profile", "investor_memo",
            "--client", "Test Infrastructure Partners",
            "--date", FIXED_DATE,
            "--version", "1",
        ],
    },
    "exec_summary": {
        "cli_args": [
            "--profile", "exec_summary",
            "--title", "Test Executive Summary",
            "--date", FIXED_DATE,
            "--version", "1",
        ],
    },
    "markdown": {
        "cli_args": [
            "--md", str(MD_FIXTURE),
            "--title", "Test Markdown Report",
            "--date", FIXED_DATE,
        ],
    },
}
