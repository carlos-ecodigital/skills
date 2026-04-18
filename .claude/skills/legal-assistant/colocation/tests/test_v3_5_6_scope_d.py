"""v3.5.6 Scope D unit tests.

Covers:
- D.1: pillar-match diagnostic (permissive any-pillar; emits attribution info)
- D.2: `[TBC]` sentence-boundary proximity (same-segment covers; cross-segment
       does not; trailing-`[TBC]` special case covers final-segment claims)
- D.3: hybrid override-reason validation (free-text ≥15 chars OR structured
       audit short-code; reject thin patterns)

Discipline: exercises static helpers / pure functions directly. No full
DocBuilder construction (PRINCIPLES.md #2).
"""
import pytest

try:
    from generate_loi import (
        _split_recital_b_sentences,
        _claim_is_tbc_covered,
        _pillar_with_urls,
        _validate_override_reason,
        _check_fabrication_gate,
        _R23_PILLAR_DIAGNOSTIC,
    )
except Exception:  # pragma: no cover
    _split_recital_b_sentences = None
    _claim_is_tbc_covered = None
    _pillar_with_urls = None
    _validate_override_reason = None
    _check_fabrication_gate = None
    _R23_PILLAR_DIAGNOSTIC = []


# -----------------------------------------------------------------------------
# D.2 — sentence-boundary splitting
# -----------------------------------------------------------------------------

class TestSentenceBoundarySplit:
    def test_empty_input(self):
        assert _split_recital_b_sentences("") == []

    def test_single_sentence(self):
        segs = _split_recital_b_sentences("This is one sentence.")
        assert len(segs) == 1
        assert "This is one sentence." in segs[0]

    def test_multiple_sentences(self):
        segs = _split_recital_b_sentences("First sentence. Second sentence. Third sentence.")
        assert len(segs) == 3

    def test_paragraph_break_splits(self):
        segs = _split_recital_b_sentences("First para.\n\nSecond para.")
        assert len(segs) == 2

    def test_question_and_exclamation(self):
        segs = _split_recital_b_sentences("A question? An exclamation! A statement.")
        assert len(segs) == 3


# -----------------------------------------------------------------------------
# D.2 — [TBC] sentence-boundary proximity
# -----------------------------------------------------------------------------

class TestTbcSentenceBoundaryProximity:
    def test_same_segment_tbc_covers_claim(self):
        """[TBC] in the same sentence as the claim → covered."""
        text = "Counterparty operates 60 MW of capacity [TBC]. Other content here."
        # Claim "60 MW" starts at offset ~21
        claim_start = text.find("60 MW")
        assert _claim_is_tbc_covered(claim_start, text) is True

    def test_different_segment_tbc_does_not_cover(self):
        """[TBC] in a different sentence → NOT covered (v3.4 bug: it did cover)."""
        text = "Counterparty operates 60 MW of capacity across Nordic sites. Other details [TBC]."
        claim_start = text.find("60 MW")
        # 60 MW is in sentence 1; [TBC] is in sentence 2 — should NOT cover
        assert _claim_is_tbc_covered(claim_start, text) is False

    def test_trailing_tbc_covers_final_segment(self):
        """Special case: `[TBC]` at end-of-Recital-B covers final-segment claims."""
        text = "First segment clean. Second segment also clean. Final segment 60 MW [TBC]"
        claim_start = text.find("60 MW")
        assert _claim_is_tbc_covered(claim_start, text) is True

    def test_trailing_tbc_does_not_cover_earlier_segment(self):
        """Trailing `[TBC]` ONLY covers final segment — earlier claims not covered."""
        text = "First segment has 40 MW. Second segment clean. [TBC]"
        claim_start = text.find("40 MW")
        # 40 MW is in segment 0; trailing [TBC] is in final segment
        # — should NOT retroactively cover earlier segments
        assert _claim_is_tbc_covered(claim_start, text) is False

    def test_paragraph_separated_tbc_does_not_cover(self):
        """`[TBC]` in a different paragraph → NOT covered."""
        text = "Counterparty operates 60 MW.\n\nSeparate paragraph with [TBC]."
        claim_start = text.find("60 MW")
        assert _claim_is_tbc_covered(claim_start, text) is False

    def test_to_be_confirmed_synonym_covers(self):
        """`[TO BE CONFIRMED]` is the documented alternative to `[TBC]`."""
        text = "Counterparty operates 60 MW [TO BE CONFIRMED]."
        claim_start = text.find("60 MW")
        assert _claim_is_tbc_covered(claim_start, text) is True

    def test_empty_text_returns_false(self):
        assert _claim_is_tbc_covered(0, "") is False


# -----------------------------------------------------------------------------
# D.1 — pillar-match diagnostic + permissive any-pillar attribution
# -----------------------------------------------------------------------------

class TestPillarWithUrls:
    def test_returns_none_for_empty_sourcemap(self):
        assert _pillar_with_urls({}) is None

    def test_returns_none_for_tbc_only(self):
        sm = {"pillar_1": "[TBC]", "pillar_2": "[TBC]"}
        assert _pillar_with_urls(sm) is None

    def test_returns_first_pillar_with_url_list(self):
        sm = {
            "pillar_1": "[TBC]",
            "pillar_3": ["https://example.com"],
        }
        assert _pillar_with_urls(sm) == "pillar_3"

    def test_returns_first_pillar_with_bare_url_string(self):
        sm = {"pillar_2": "https://example.com"}
        assert _pillar_with_urls(sm) == "pillar_2"

    def test_iteration_order_preserved(self):
        """The first pillar with URLs (by insertion order) should win."""
        sm = {
            "pillar_3": ["https://third.example"],
            "pillar_1": ["https://first.example"],
        }
        assert _pillar_with_urls(sm) == "pillar_3"


class TestFabricationGatePillarDiagnostic:
    def test_pass_emits_pillar_diagnostic(self):
        """On PASS path, _R23_PILLAR_DIAGNOSTIC is populated."""
        text = "Counterparty operates 60 MW across Nordic sites."
        sm = {"pillar_3": ["https://example.com"]}
        findings = _check_fabrication_gate(text, sm, set())
        assert findings == []
        assert len(_R23_PILLAR_DIAGNOSTIC) >= 1
        # All entries should be (claim_text, pillar_key) tuples
        for claim_text, pillar in _R23_PILLAR_DIAGNOSTIC:
            assert pillar in ("pillar_3", "TBC-covered")

    def test_fail_clears_pillar_diagnostic(self):
        """On FAIL path, diagnostic is cleared (reviewer focuses on failures)."""
        text = "Counterparty operates 60 MW across Nordic sites."
        sm = {}  # no URLs, no pillars
        findings = _check_fabrication_gate(text, sm, set())
        assert len(findings) == 1
        assert _R23_PILLAR_DIAGNOSTIC == []

    def test_tbc_covered_claim_marked_in_diagnostic(self):
        text = "Counterparty operates 60 MW [TBC] across Nordic sites."
        # Note: the [TBC] is in the only segment, so the 60 MW claim is covered
        sm = {}  # no URLs
        findings = _check_fabrication_gate(text, sm, set())
        # Claim is [TBC]-covered, no failures
        assert findings == []
        # Diagnostic should note TBC coverage
        assert any(p == "TBC-covered" for _, p in _R23_PILLAR_DIAGNOSTIC)

    def test_override_skips_entirely(self):
        text = "Counterparty operates 60 MW."
        findings = _check_fabrication_gate(text, {}, {"R-23"})
        assert findings == []
        # Diagnostic cleared when overridden (no work done)
        assert _R23_PILLAR_DIAGNOSTIC == []


# -----------------------------------------------------------------------------
# D.3 — hybrid override-reason validation
# -----------------------------------------------------------------------------

class TestOverrideReasonValidation:
    def test_none_rejected(self):
        ok, err = _validate_override_reason(None)
        assert ok is False
        assert "required" in err.lower()

    def test_empty_rejected(self):
        ok, err = _validate_override_reason("")
        assert ok is False

    def test_thin_ok_rejected(self):
        ok, err = _validate_override_reason("ok")
        assert ok is False
        assert "thin" in err.lower() or "15 characters" in err

    def test_thin_fine_rejected(self):
        ok, _ = _validate_override_reason("fine")
        assert ok is False

    def test_thin_yes_rejected(self):
        ok, _ = _validate_override_reason("yes")
        assert ok is False

    def test_thin_trust_me_rejected(self):
        # "trust me" is 8 chars, not a thin-pattern match, but below 15
        ok, err = _validate_override_reason("trust me")
        assert ok is False
        assert "15" in err  # length-based rejection

    def test_short_but_not_thin_rejected(self):
        ok, _ = _validate_override_reason("too short")  # 9 chars
        assert ok is False

    def test_fifteen_chars_exactly_accepted(self):
        reason = "pre-approved 4Q"  # 15 chars exactly
        ok, _ = _validate_override_reason(reason)
        assert ok is True

    def test_verbose_reason_accepted(self):
        reason = "pre-approved for Q3 batch per Jonathan memo 2026-04-17"
        ok, _ = _validate_override_reason(reason)
        assert ok is True

    def test_structured_short_code_ok_accepted(self):
        """`OK-YYYY-MM-DD INITIALS` pattern accepted regardless of length."""
        ok, _ = _validate_override_reason("OK-2026-04-17 JG")
        assert ok is True

    def test_structured_short_code_approved_accepted(self):
        ok, _ = _validate_override_reason("APPROVED-2026-04-17 CR")
        assert ok is True

    def test_structured_short_code_preapproved_accepted(self):
        ok, _ = _validate_override_reason("PREAPPROVED-2026-04-17 JGLD")
        assert ok is True

    def test_structured_short_code_fine_accepted(self):
        ok, _ = _validate_override_reason("FINE-2026-04-17 CR")
        assert ok is True

    def test_short_malformed_structured_code_rejected(self):
        """A short string that LOOKS like a structured code but fails the
        regex falls through to the length check — rejected if <15 chars.
        (A ≥15-char malformed-looking string is accepted as free-text —
        the hybrid rule is permissive by design.)"""
        # 12 chars, looks structured but bad date separator, too short for free-text
        ok, _ = _validate_override_reason("OK-26/04 JG")
        assert ok is False

    def test_no_initials_short_rejected(self):
        """Structured-looking but missing initials, also too short for free-text."""
        ok, _ = _validate_override_reason("OK-2026-04-17")  # 13 chars
        assert ok is False

    def test_structured_code_only_matches_uppercase_initials(self):
        """`OK-2026-04-17 jg` is 16 chars so accepted as free-text. The
        structured-code regex requires uppercase initials — documented
        limitation; free-text path catches the hybrid case."""
        ok, _ = _validate_override_reason("OK-2026-04-17 jg")
        # Accepted as ≥15-char free-text (not via structured regex)
        assert ok is True


# -----------------------------------------------------------------------------
# Regression: prior v3.5.x invariants still hold
# -----------------------------------------------------------------------------

class TestV35xInvariantsStillHold:
    def test_permissive_any_pillar_match_unchanged(self):
        """v3.5.x behaviour: ANY pillar with URLs passes R-23."""
        text = "Counterparty operates 60 MW."
        # URL in pillar_1 only — still passes (permissive any-pillar)
        sm = {"pillar_1": ["https://example.com"]}
        findings = _check_fabrication_gate(text, sm, set())
        assert findings == []

    def test_no_claims_no_findings(self):
        text = "Counterparty is a Dutch operator with sovereign-compute focus."
        findings = _check_fabrication_gate(text, {}, set())
        assert findings == []

    def test_override_r23_skips(self):
        text = "60 MW."
        findings = _check_fabrication_gate(text, {}, {"R-23"})
        assert findings == []
