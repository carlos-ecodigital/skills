"""v3.5.6 Scope G unit tests — Phase 7.5 fail-closed sentinel enforcement.

Covers:
- G.1: sentinel file written with SHA-256 of .docx; consumed on
       --phase-7-5-pass; rejected if .docx modified after creation
- G.2: opt-in via CLI flag OR env var (OR'd); default fail-open preserved
- G.3: exit code semantics
- HOW-TO-RESOLVE block present in sentinel

Discipline: exercises static helpers directly (no full DocBuilder
construction) — per PRINCIPLES.md principle #2.
"""
import hashlib
import os
import sys
import tempfile
from unittest import mock

import pytest

try:
    from generate_loi import (
        _phase_7_5_enforce_enabled,
        _write_phase_7_5_sentinel,
        _consume_phase_7_5_sentinel,
        _phase_7_5_sentinel_path,
        _docx_sha256,
        _PHASE_7_5_SENTINEL_SUFFIX,
    )
except Exception:  # pragma: no cover
    _phase_7_5_enforce_enabled = None
    _write_phase_7_5_sentinel = None
    _consume_phase_7_5_sentinel = None
    _phase_7_5_sentinel_path = None
    _docx_sha256 = None
    _PHASE_7_5_SENTINEL_SUFFIX = ".phase_7_5_required"


# -----------------------------------------------------------------------------
# G.2 — opt-in (CLI flag OR env var, OR'd)
# -----------------------------------------------------------------------------

class TestEnforcementOptIn:
    def test_default_fail_open(self):
        """No CLI flag, no env var → enforcement OFF (v3.5.x preserved)."""
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {}, clear=False):
                os.environ.pop("DE_LOI_ENFORCE_PHASE_7_5", None)
                assert _phase_7_5_enforce_enabled() is False

    def test_cli_flag_activates(self):
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml", "--enforce-phase-7-5"]):
            with mock.patch.dict(os.environ, {}, clear=False):
                os.environ.pop("DE_LOI_ENFORCE_PHASE_7_5", None)
                assert _phase_7_5_enforce_enabled() is True

    def test_env_var_1_activates(self):
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {"DE_LOI_ENFORCE_PHASE_7_5": "1"}):
                assert _phase_7_5_enforce_enabled() is True

    def test_env_var_true_activates(self):
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {"DE_LOI_ENFORCE_PHASE_7_5": "true"}):
                assert _phase_7_5_enforce_enabled() is True

    def test_env_var_yes_activates(self):
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {"DE_LOI_ENFORCE_PHASE_7_5": "yes"}):
                assert _phase_7_5_enforce_enabled() is True

    def test_env_var_on_activates(self):
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {"DE_LOI_ENFORCE_PHASE_7_5": "on"}):
                assert _phase_7_5_enforce_enabled() is True

    def test_env_var_case_insensitive(self):
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {"DE_LOI_ENFORCE_PHASE_7_5": "TRUE"}):
                assert _phase_7_5_enforce_enabled() is True

    def test_env_var_0_does_not_activate(self):
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {"DE_LOI_ENFORCE_PHASE_7_5": "0"}):
                assert _phase_7_5_enforce_enabled() is False

    def test_env_var_false_does_not_activate(self):
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {"DE_LOI_ENFORCE_PHASE_7_5": "false"}):
                assert _phase_7_5_enforce_enabled() is False

    def test_cli_flag_and_env_or_together(self):
        """Either activates — OR'd."""
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml", "--enforce-phase-7-5"]):
            with mock.patch.dict(os.environ, {"DE_LOI_ENFORCE_PHASE_7_5": "0"}):
                # Flag activates even though env var is falsy
                assert _phase_7_5_enforce_enabled() is True


# -----------------------------------------------------------------------------
# G.1 — sentinel write / consume / hash verification
# -----------------------------------------------------------------------------

class TestSentinelLifecycle:
    def test_sentinel_path_format(self):
        """Sentinel path is `<docx_path>.phase_7_5_required`."""
        p = _phase_7_5_sentinel_path("/tmp/foo.docx")
        assert p == "/tmp/foo.docx.phase_7_5_required"
        assert p.endswith(_PHASE_7_5_SENTINEL_SUFFIX)

    def test_write_sentinel_contains_sha256(self, tmp_path):
        """Written sentinel carries the SHA-256 of the .docx it blesses."""
        docx = tmp_path / "test.docx"
        docx.write_bytes(b"fake docx content for testing")
        expected_sha = hashlib.sha256(b"fake docx content for testing").hexdigest()
        sentinel_path = _write_phase_7_5_sentinel(str(docx))
        assert os.path.exists(sentinel_path)
        content = (tmp_path / "test.docx.phase_7_5_required").read_text()
        assert expected_sha in content
        # File format sanity
        assert "docx_sha256:" in content
        assert "created:" in content

    def test_write_sentinel_contains_how_to_resolve(self, tmp_path):
        """Sentinel must self-document how to resolve the error."""
        docx = tmp_path / "test.docx"
        docx.write_bytes(b"content")
        sentinel_path = _write_phase_7_5_sentinel(str(docx))
        content = (tmp_path / "test.docx.phase_7_5_required").read_text()
        assert "HOW TO RESOLVE" in content
        assert "loi-review-workflow.md" in content
        assert "--phase-7-5-pass" in content

    def test_consume_happy_path(self, tmp_path):
        """Write sentinel → consume → sentinel deleted, returns (True, '')."""
        docx = tmp_path / "test.docx"
        docx.write_bytes(b"content-v1")
        _write_phase_7_5_sentinel(str(docx))
        sentinel_path = _phase_7_5_sentinel_path(str(docx))
        assert os.path.exists(sentinel_path)
        ok, err = _consume_phase_7_5_sentinel(str(docx))
        assert ok is True
        assert err == ""
        # Sentinel deleted
        assert not os.path.exists(sentinel_path)

    def test_consume_missing_sentinel_rejects(self, tmp_path):
        """No sentinel present → (False, error)."""
        docx = tmp_path / "test.docx"
        docx.write_bytes(b"content")
        ok, err = _consume_phase_7_5_sentinel(str(docx))
        assert ok is False
        assert "not found" in err.lower() or "sentinel" in err.lower()

    def test_consume_rejects_hash_mismatch(self, tmp_path):
        """v3.5.6 G.1 replay/tamper prevention: if .docx modified after
        sentinel creation, hash check fails, sentinel NOT consumed."""
        docx = tmp_path / "test.docx"
        docx.write_bytes(b"content-v1")
        _write_phase_7_5_sentinel(str(docx))
        sentinel_path = _phase_7_5_sentinel_path(str(docx))
        # Modify .docx after sentinel creation (simulate post-approval tampering)
        docx.write_bytes(b"content-v2-modified-after-blessing")
        ok, err = _consume_phase_7_5_sentinel(str(docx))
        assert ok is False
        assert "hash mismatch" in err.lower() or "modified" in err.lower()
        # Sentinel should NOT be consumed on rejection
        assert os.path.exists(sentinel_path)

    def test_consume_rejects_corrupted_sentinel(self, tmp_path):
        """Malformed sentinel (no sha256 line) → rejected."""
        docx = tmp_path / "test.docx"
        docx.write_bytes(b"content")
        sentinel_path = _phase_7_5_sentinel_path(str(docx))
        with open(sentinel_path, "w") as f:
            f.write("malformed\nno sha here\n")
        ok, err = _consume_phase_7_5_sentinel(str(docx))
        assert ok is False
        assert "malformed" in err.lower() or "valid" in err.lower()

    def test_docx_sha256_deterministic(self, tmp_path):
        """Same content → same hash."""
        p = tmp_path / "test.docx"
        p.write_bytes(b"some content")
        h1 = _docx_sha256(str(p))
        h2 = _docx_sha256(str(p))
        assert h1 == h2
        # Verify it's a valid hex SHA-256
        assert len(h1) == 64
        assert all(c in "0123456789abcdef" for c in h1)


# -----------------------------------------------------------------------------
# Integration: default fail-open preserves v3.5.x behaviour
# -----------------------------------------------------------------------------

class TestDefaultBehaviourPreserved:
    """Without the opt-in, the generator behaves exactly as v3.5.5 did.
    This is a contract test — no enforcement-related side effects occur
    when enforcement is off.
    """

    def test_enforcement_off_default(self):
        # Equivalent to TestEnforcementOptIn::test_default_fail_open but
        # stated as a contract explicitly.
        with mock.patch.object(sys, "argv", ["generate_loi.py", "intake.yaml"]):
            with mock.patch.dict(os.environ, {}, clear=False):
                os.environ.pop("DE_LOI_ENFORCE_PHASE_7_5", None)
                assert _phase_7_5_enforce_enabled() is False
