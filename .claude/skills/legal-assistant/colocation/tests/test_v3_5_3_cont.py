"""v3.5.3-cont unit tests.

Scopes covered:
  - F   Recital B multi-paragraph extraction (regex fix)
  - J12 type_defaults auto-expansion (from config/entities.yaml)
  - E   R-22 regex narrowing + allowlist tests
  - J8  SKILL.md Phase 6 full Recital B (structural assert)
  - J9  SKILL.md Phase 5 redraft-as-first-class (structural assert)
  - H   tier-2 qualifier worked-example pattern in framework (structural assert)

Discipline: all logic tests exercise static helpers directly (no full
DocBuilder construction) — per PRINCIPLES.md principle #2.
"""
import os
import re
import pytest

try:
    from generate_loi import (
        load_entities_register,
        expand_provider_from_register,
        _FAIL_RULES,
        _WARN_RULES,
    )
except Exception:  # pragma: no cover
    load_entities_register = None
    expand_provider_from_register = None
    _FAIL_RULES = {}
    _WARN_RULES = {}


_HERE = os.path.dirname(os.path.abspath(__file__))
_COLOCATION = os.path.dirname(_HERE)
_LEGAL_ASSISTANT = os.path.dirname(_COLOCATION)
_SHARED = os.path.join(os.path.dirname(_LEGAL_ASSISTANT), "_shared")


# -----------------------------------------------------------------------------
# Scope F — Recital B multi-paragraph extraction
# -----------------------------------------------------------------------------

class TestRecitalBMultiParagraphExtraction:
    """The v3.4 regex stopped at the first `\\n\\n` (paragraph break). Any
    legitimately multi-paragraph Recital B (rare but possible for
    consortium / holdco-subsidiary disclosure) was partially scanned.

    The v3.5.3-cont regex extracts until the next recital marker `(C)` or
    `(D)` or a section header `\\n## ` or EOF — paragraph breaks inside
    Recital B are preserved.

    These tests encode the fix by replicating the production regex locally
    and asserting the behaviour on representative inputs; the production
    regex is the source of truth and changes to it must update these tests.
    """

    PATTERN = r"\(B\)\s*(.*?)(?=\(C\)\s|\(D\)\s|\n##\s|\Z)"

    def _extract(self, text):
        m = re.search(self.PATTERN, text, re.DOTALL)
        return m.group(1) if m else ""

    def test_single_paragraph_recital_b_unchanged(self):
        text = "(A) Provider recital.\n\n(B) Counterparty is a Dutch entity.\n\n(C) Parties wish."
        out = self._extract(text)
        assert "Counterparty is a Dutch entity" in out
        assert "(C)" not in out

    def test_multi_paragraph_recital_b_preserved(self):
        text = (
            "(A) Provider recital.\n\n"
            "(B) Counterparty is a Dutch consortium.\n\n"
            "Its members include A, B, and C — each with named tier-1 references.\n\n"
            "(C) Parties wish."
        )
        out = self._extract(text)
        assert "Counterparty is a Dutch consortium" in out
        # Second paragraph MUST be captured (the v3.4 bug would drop this)
        assert "Its members include A, B, and C" in out
        # Still stops at (C)
        assert "Parties wish" not in out

    def test_recital_b_ends_at_c_marker(self):
        text = "(B) claim.\n\n(C) next"
        out = self._extract(text)
        assert "claim" in out
        assert "next" not in out

    def test_recital_b_ends_at_d_marker_when_no_c(self):
        """Some LOI types (EP) skip (C) and go straight to (D)."""
        text = "(B) claim.\n\n(D) next"
        out = self._extract(text)
        assert "claim" in out
        assert "next" not in out

    def test_recital_b_ends_at_section_header(self):
        text = "(B) claim.\n\n## Definitions\n\ncontent"
        out = self._extract(text)
        assert "claim" in out
        assert "Definitions" not in out

    def test_recital_b_to_eof_when_no_marker(self):
        text = "(B) claim.\n\nmore claim content"
        out = self._extract(text)
        assert "claim" in out
        assert "more claim content" in out


# -----------------------------------------------------------------------------
# Scope J12 — type_defaults lookup
# -----------------------------------------------------------------------------

class TestTypeDefaultsLookup:
    """v3.5.3-cont: a minimal intake with only `type:` set should auto-
    expand the provider record from `config/entities.yaml::type_defaults`.

    This tests the happy path (no explicit entity → type_defaults fills in
    + expansion works), the explicit-override path (explicit entity wins),
    and the backward-compat path (explicit-fields intake unchanged).
    """

    def _reg(self):
        return load_entities_register()

    def test_minimal_wholesale_intake_expands_to_de_nl(self):
        """Minimal YAML with only `type: Wholesale` should populate de_nl
        (per type_defaults matrix) and expand into full provider record."""
        data = {"type": "Wholesale", "provider": {}}
        expanded = expand_provider_from_register(data, self._reg())
        p = expanded["provider"]
        assert p["legal_name"] == "Digital Energy Netherlands B.V."
        assert p["signatory_name"] == "Carlos Reuven"
        assert p["signatory_title"] == "Director"

    def test_minimal_strategic_supplier_intake_expands_to_de_ag(self):
        """Per type_defaults, StrategicSupplier → de_ag + ceo."""
        data = {"type": "StrategicSupplier", "provider": {}}
        expanded = expand_provider_from_register(data, self._reg())
        p = expanded["provider"]
        assert p["legal_name"] == "Digital Energy Group AG"
        assert p["signatory_title"] == "Chief Executive Officer"

    def test_explicit_entity_wins_over_type_default(self):
        """If intake sets `provider.entity`, type_defaults is ignored."""
        data = {
            "type": "Wholesale",  # would default to de_nl via type_defaults
            "provider": {"entity": "de_ag"},  # but user chose de_ag explicitly
        }
        expanded = expand_provider_from_register(data, self._reg())
        assert expanded["provider"]["legal_name"] == "Digital Energy Group AG"

    def test_backward_compat_explicit_fields_unchanged(self):
        """Intake YAMLs with explicit provider fields (pre-v3.5.2 pattern)
        should pass through unchanged — type_defaults is a fallback only."""
        data = {
            "type": "Wholesale",
            "provider": {
                "legal_name": "Custom Corp",
                "address": "Somewhere",
            },
        }
        expanded = expand_provider_from_register(data, self._reg())
        # Explicit fields preserved; no expansion happened
        assert expanded["provider"]["legal_name"] == "Custom Corp"
        assert expanded["provider"]["address"] == "Somewhere"
        # No signatory defaulted in
        assert "signatory_name" not in expanded["provider"]

    def test_minimal_intake_preserves_signatory_mode_override(self):
        """If intake specifies signatory_mode, it's respected even when
        type_defaults would suggest a different mode."""
        data = {
            "type": "Wholesale",  # type_defaults: pre_msa
            "provider": {"signatory_mode": "post_msa"},  # explicit override
        }
        expanded = expand_provider_from_register(data, self._reg())
        p = expanded["provider"]
        # entity still de_nl (from type_defaults since no explicit entity)
        assert p["legal_name"] == "Digital Energy Netherlands B.V."
        # signatory_mode respected: post_msa → Jelmer
        assert p["signatory_name"] == "Jelmer ten Wolde"


# -----------------------------------------------------------------------------
# Scope E — R-22 narrowing
# -----------------------------------------------------------------------------

class TestR22Narrowed:
    """v3.5.3-cont: R-22 patterns narrowed to reduce false positives.

    Old broad patterns caught legitimate operative clauses (e.g. bare
    "ability to" anywhere in body). Narrowed patterns require the meta-
    commentary verb context that only meta-commentary uses.
    """

    def _pattern(self):
        return _WARN_RULES["R-22"][0]

    def test_narrow_ability_to_secure_fires(self):
        """Meta-commentary form — still caught."""
        p = self._pattern()
        assert re.search(p, "Digital Energy's ability to secure financing")

    def test_bare_ability_to_deliver_does_not_fire(self):
        """Operational capability — MUST NOT fire (false positive fix)."""
        p = self._pattern()
        assert not re.search(p, "Digital Energy's ability to deliver the Services")

    def test_bare_ability_to_scale_does_not_fire(self):
        p = self._pattern()
        assert not re.search(p, "Digital Energy's ability to scale to 100 MW")

    def test_will_require_exchange_of_confidential_info_fires(self):
        p = self._pattern()
        assert re.search(p, "will require the exchange of Confidential Information")

    def test_will_require_exchange_of_information_does_not_fire(self):
        """Legitimate operative use — MUST NOT fire."""
        p = self._pattern()
        assert not re.search(p, "will require the exchange of information about delivery")

    def test_depends_in_part_on_fires(self):
        p = self._pattern()
        assert re.search(p, "depends in part on the Customer's performance")

    def test_bare_depends_on_does_not_fire(self):
        """Without 'in part' — legitimate."""
        p = self._pattern()
        assert not re.search(p, "depends on the MSA being executed")

    def test_is_intended_to_evidence_fires(self):
        p = self._pattern()
        assert re.search(p, "is intended to evidence the Parties' commitment")


# -----------------------------------------------------------------------------
# Scope J8 / J9 / H — structural asserts on markdown files
# -----------------------------------------------------------------------------

class TestSkillMdPhase5PromptJ9:
    """Phase 5 prompt must present the three-option redraft choice."""

    def _skill_md(self):
        path = os.path.join(_LEGAL_ASSISTANT, "SKILL.md")
        with open(path) as f:
            return f.read()

    def test_phase_5_offers_accept(self):
        src = self._skill_md()
        assert "(a) Accept" in src

    def test_phase_5_offers_redraft_with_notes(self):
        src = self._skill_md()
        assert "(b) Redraft with notes" in src

    def test_phase_5_offers_paste_replacement(self):
        src = self._skill_md()
        assert "(c) Paste replacement text" in src

    def test_phase_5_no_longer_just_accept_or_request(self):
        """The v3.4 two-option prompt is removed from LIVE prompt templates.
        (The string may still appear inside a v3.5.3-cont explanatory note
        that quotes the removed form — that's fine; the live prompt is what
        matters. Assert the live prompt template uses the new three-option
        form by checking the triple-backtick code fence block.)"""
        src = self._skill_md()
        # Find the Phase 5 prompt template block
        m = re.search(r"### Phase 5 —.*?### Phase 6", src, re.DOTALL)
        assert m is not None, "Phase 5 section not found"
        phase_5_block = m.group(0)
        # The live prompt (inside triple-backtick fence) must have (a)/(b)/(c)
        fence_m = re.search(r"```\n(.*?)```", phase_5_block, re.DOTALL)
        assert fence_m is not None, "Phase 5 prompt fence not found"
        live_prompt = fence_m.group(1)
        assert "(a) Accept" in live_prompt
        assert "(b) Redraft" in live_prompt
        assert "(c) Paste" in live_prompt


class TestSkillMdPhase6PromptJ8:
    """Phase 6 confirmation gate must show full Recital B, not a truncation."""

    def _skill_md(self):
        path = os.path.join(_LEGAL_ASSISTANT, "SKILL.md")
        with open(path) as f:
            return f.read()

    def test_phase_6_does_not_truncate_recital_b(self):
        """The v3.4 'first 60 chars...' anti-pattern is removed."""
        src = self._skill_md()
        # The old pattern had: `[first 60 chars...]`
        assert "first 60 chars" not in src

    def test_phase_6_shows_full_recital_b(self):
        src = self._skill_md()
        assert "full paragraph — verbatim, not truncated" in src

    def test_phase_6_surfaces_source_map_pillars(self):
        src = self._skill_md()
        assert "source_map pillars" in src


class TestFrameworkTier2PatternH:
    """Framework file must contain the tier-2 qualifier worked-example pattern."""

    def _framework(self):
        path = os.path.join(_SHARED, "counterpart-description-framework.md")
        with open(path) as f:
            return f.read()

    def test_tier_2_pattern_section_exists(self):
        src = self._framework()
        assert "Tier-2 qualifier pattern" in src

    def test_tier_2_pattern_documents_prose_form(self):
        src = self._framework()
        assert "as publicly reported by" in src

    def test_tier_2_pattern_documents_yaml_schema(self):
        src = self._framework()
        # The dict entry form: tier + qualifier fields
        assert "tier: 2" in src
        assert "qualifier:" in src

    def test_tier_2_rule_states_omission_over_fabrication(self):
        """Tier-2-only claims without tier-1 corroboration must be omitted."""
        src = self._framework()
        assert "must be" in src and "omitted" in src
