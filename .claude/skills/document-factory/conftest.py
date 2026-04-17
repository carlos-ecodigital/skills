"""Pytest configuration for Document Factory tests.

Adds --visual flag to opt into visual regression tests (require LibreOffice).
"""


def pytest_addoption(parser):
    parser.addoption(
        "--visual", action="store_true", default=False,
        help="Run visual regression tests (requires LibreOffice, slow)",
    )
