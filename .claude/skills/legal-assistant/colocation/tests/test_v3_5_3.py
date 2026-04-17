"""v3.5.3 unit tests — Scope J (EP Recital D polish), Scope K (--migrate-check).

Discipline: every render-logic change ships with a unit test.
"""
import inspect
import sys
from unittest.mock import patch

import pytest

try:
    from generate_loi import LOI as DocBuilder, _migrate_check
except Exception:  # pragma: no cover
    DocBuilder = None
    _migrate_check = None


# -----------------------------------------------------------------------------
# Scope J — EP Recital D "may exchange" → "will exchange"
# -----------------------------------------------------------------------------

class TestEPRecitalDPolish:
    """The EP-specific Recital D text must say 'will exchange', not 'may exchange',
    for consistency with the other types' confidentiality framing."""

    def test_no_may_exchange_in_recitals_ep(self):
        import generate_loi
        src = inspect.getsource(generate_loi)
        # Find the EP recitals block
        assert "The Parties will exchange commercially sensitive" in src
        assert "The Parties may exchange commercially sensitive" not in src


# -----------------------------------------------------------------------------
# Scope K — --migrate-check CLI flag
# -----------------------------------------------------------------------------

class TestMigrateCheck:
    """Legacy v3.3 intake YAMLs can be inspected for missing source_map without
    running the full build. Non-blocking (exit 0) in all paths."""

    def test_migrate_check_callable(self):
        assert _migrate_check is not None
        assert callable(_migrate_check)

    def test_migrate_check_emits_snippet_for_missing_source_map(self, tmp_path, capsys):
        """A legacy YAML with no source_map should emit a ready-to-paste snippet."""
        yaml_path = tmp_path / "legacy_intake.yaml"
        yaml_path.write_text("""
type: EndUser
provider:
  legal_name: "Test Provider"
counterparty:
  name: "Test Co"
  description: "a test entity"
""".strip())
        result = _migrate_check(str(yaml_path))
        captured = capsys.readouterr()
        assert result == 0, "--migrate-check must be non-blocking (exit 0)"
        assert "source_map NOT SET" in captured.out
        assert "pillar_1:" in captured.out
        assert "[TBC]" in captured.out
        # The snippet should include all 5 pillars
        for p in ("pillar_1", "pillar_2", "pillar_3", "pillar_4", "pillar_5"):
            assert p in captured.out, f"snippet missing {p}"

    def test_migrate_check_reports_ok_for_populated_source_map(self, tmp_path, capsys):
        """A v3.4+ YAML with source_map already populated should report OK."""
        yaml_path = tmp_path / "v34_intake.yaml"
        yaml_path.write_text("""
type: EndUser
provider:
  legal_name: "Test Provider"
counterparty:
  name: "Test Co"
  description: "a test entity"
  source_map:
    pillar_1: "[TBC]"
    pillar_2: "[TBC]"
    pillar_3: "[TBC]"
    pillar_4: "inferred"
    pillar_5: "[TBC]"
""".strip())
        result = _migrate_check(str(yaml_path))
        captured = capsys.readouterr()
        assert result == 0
        assert "OK: counterparty.source_map present" in captured.out
        assert "pillar_1:" not in captured.out  # snippet NOT emitted

    def test_migrate_check_handles_missing_file(self, capsys):
        """Non-blocking: unreadable YAML should not raise."""
        result = _migrate_check("/nonexistent/path/intake.yaml")
        captured = capsys.readouterr()
        assert result == 0
        assert "Could not read" in captured.out


# -----------------------------------------------------------------------------
# Regression: v3.5.2 invariants still hold
# -----------------------------------------------------------------------------

class TestV352InvariantsStillHold:
    def test_parties_method_still_exists(self):
        assert hasattr(DocBuilder, "parties")

    def test_brand_rename_still_in_recital_a(self):
        from generate_loi import RECITAL_A_BODY
        assert "Digital Energy" in RECITAL_A_BODY
        assert "the Provider" not in RECITAL_A_BODY

    def test_entities_register_still_loadable(self):
        from generate_loi import load_entities_register
        r = load_entities_register()
        assert "de_nl" in r.get("entities", {})
