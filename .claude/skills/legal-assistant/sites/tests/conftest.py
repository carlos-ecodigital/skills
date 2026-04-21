"""Shared fixtures for sites-stream integration tests."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

# Expose all sites sub-packages on sys.path
_SITES = Path(__file__).resolve().parents[1]
for sub in ("_shared", "loi", "hot"):
    p = str(_SITES / sub)
    if p not in sys.path:
        sys.path.insert(0, p)

# document-factory too (siblings/colocation callers use it)
_FACTORY = _SITES.parents[1] / "document-factory"
if str(_FACTORY) not in sys.path:
    sys.path.insert(0, str(_FACTORY))


@pytest.fixture
def van_gog_deal():
    """Parse the reference van-gog fixture."""
    p = _SITES / "loi" / "examples" / "deal_van-gog.yaml"
    return yaml.safe_load(p.read_text())


@pytest.fixture
def registry():
    """Load field-registry.json via site_doc_base."""
    import site_doc_base
    return site_doc_base.load_registry()


@pytest.fixture
def fake_drive(tmp_path):
    """Simulated Drive base with a clean project tree."""
    base = tmp_path / "drive"
    base.mkdir()
    return base
