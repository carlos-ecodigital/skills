"""v3.5.2 unit tests — Scope Q (entities register), A''' (Parties Preamble),
brand-name rename ("Digital Energy"), and Scope 0 (new linter rules R-24/25/27/28).

Discipline: every render-logic change in v3.5.2 ships with a unit test.
"""
import os
import pytest

try:
    from generate_loi import (
        LOI as DocBuilder,
        load_entities_register,
        expand_provider_from_register,
        _FAIL_RULES,
        _WARN_RULES,
    )
except Exception:  # pragma: no cover
    DocBuilder = None
    load_entities_register = None
    expand_provider_from_register = None
    _FAIL_RULES = {}
    _WARN_RULES = {}


# -----------------------------------------------------------------------------
# Scope Q — entities register
# -----------------------------------------------------------------------------

class TestEntitiesRegister:
    def test_register_loads_de_nl_and_de_ag(self):
        r = load_entities_register()
        assert "entities" in r
        assert "de_nl" in r["entities"]
        assert "de_ag" in r["entities"]

    def test_de_nl_has_correct_legal_name(self):
        r = load_entities_register()
        assert r["entities"]["de_nl"]["legal_name"] == "Digital Energy Netherlands B.V."

    def test_de_nl_has_correct_kvk(self):
        r = load_entities_register()
        assert r["entities"]["de_nl"]["reg_number"] == "98580086"

    def test_de_nl_has_correct_address(self):
        r = load_entities_register()
        addr = r["entities"]["de_nl"]["address"]
        assert "Mijnsherenweg" in addr
        assert "Kudelstaart" in addr

    def test_de_nl_pre_msa_signatory_is_carlos_director(self):
        r = load_entities_register()
        sig = r["entities"]["de_nl"]["default_signatory_pre_msa"]
        assert sig["name"] == "Carlos Reuven"
        assert sig["title"] == "Director"

    def test_de_ag_has_correct_legal_name(self):
        r = load_entities_register()
        assert r["entities"]["de_ag"]["legal_name"] == "Digital Energy Group AG"

    def test_de_ag_has_zug_address(self):
        r = load_entities_register()
        assert "Zug" in r["entities"]["de_ag"]["address"]


class TestProviderExpansion:
    def _reg(self):
        return load_entities_register()

    def test_de_nl_pre_msa_expansion(self):
        data = {"provider": {"entity": "de_nl", "signatory_mode": "pre_msa"}}
        expanded = expand_provider_from_register(data, self._reg())
        p = expanded["provider"]
        assert p["legal_name"] == "Digital Energy Netherlands B.V."
        assert p["signatory_name"] == "Carlos Reuven"
        assert p["signatory_title"] == "Director"
        assert p["reg_number"] == "98580086"

    def test_de_nl_post_msa_expansion(self):
        data = {"provider": {"entity": "de_nl", "signatory_mode": "post_msa"}}
        expanded = expand_provider_from_register(data, self._reg())
        p = expanded["provider"]
        assert p["signatory_name"] == "Jelmer ten Wolde"
        assert p["signatory_title"] == "Chief Platform Officer"

    def test_de_ag_expansion(self):
        data = {"provider": {"entity": "de_ag"}}
        expanded = expand_provider_from_register(data, self._reg())
        p = expanded["provider"]
        assert p["legal_name"] == "Digital Energy Group AG"
        assert p["signatory_name"] == "Carlos Reuven"
        assert p["signatory_title"] == "Chief Executive Officer"

    def test_backward_compat_no_entity_key_unchanged(self):
        """If `provider.entity` is absent, the provider dict is unchanged."""
        data = {"provider": {"legal_name": "Custom Corp", "address": "Somewhere"}}
        expanded = expand_provider_from_register(data, self._reg())
        assert expanded["provider"] == {"legal_name": "Custom Corp", "address": "Somewhere"}

    def test_explicit_override_wins_over_register(self):
        """Intake values override register defaults."""
        data = {
            "provider": {
                "entity": "de_nl",
                "signatory_mode": "pre_msa",
                "signatory_name": "Custom Signer",
            }
        }
        expanded = expand_provider_from_register(data, self._reg())
        p = expanded["provider"]
        # Register-derived fields filled in
        assert p["legal_name"] == "Digital Energy Netherlands B.V."
        # Explicit override takes precedence
        assert p["signatory_name"] == "Custom Signer"
        # Title still from register since not overridden
        assert p["signatory_title"] == "Director"


# -----------------------------------------------------------------------------
# Scope A''' — Parties Preamble
# -----------------------------------------------------------------------------

class TestPartiesPreambleOutputContract:
    """Parties Preamble method must exist, be called from build() and _build_ep(),
    and include the required structural elements."""

    def _source(self):
        import inspect
        return inspect.getsource(DocBuilder.parties)

    def test_parties_method_exists(self):
        assert hasattr(DocBuilder, "parties"), "parties() method required by Scope A'''"

    def test_preamble_header_phrase(self):
        src = self._source()
        assert "THIS LETTER OF INTENT" in src, "Preamble must open with 'THIS LETTER OF INTENT'"

    def test_brand_name_defined_term(self):
        src = self._source()
        # The provider_term self-reference
        assert 'self.provider_term' in src
        # And in __init__, provider_term should be "Digital Energy"
        import inspect
        init_src = inspect.getsource(DocBuilder.__init__)
        assert '"Digital Energy"' in init_src

    def test_party_enumeration(self):
        src = self._source()
        assert "(1) " in src
        assert "(2) " in src

    def test_parties_definition(self):
        src = self._source()
        assert 'each a "Party"' in src
        assert 'together the "Parties"' in src


# -----------------------------------------------------------------------------
# Brand rename — body-wide "the Provider" → "Digital Energy"
# -----------------------------------------------------------------------------

class TestBrandRename:
    """Body-wide: 'the Provider' / 'The Provider' should no longer appear as
    rendered-string literals. Code identifiers (like `"provider"` as dict key)
    are not affected.
    """

    def test_no_the_provider_in_recital_a_constants(self):
        from generate_loi import RECITAL_A_BODY, RECITAL_A_TAIL_BY_TYPE
        assert "the Provider" not in RECITAL_A_BODY
        assert "The Provider" not in RECITAL_A_BODY
        for k, v in RECITAL_A_TAIL_BY_TYPE.items():
            assert "the Provider" not in v, f"{k} tail contains 'the Provider'"
            assert "The Provider" not in v, f"{k} tail contains 'The Provider'"

    def test_digital_energy_appears_in_recital_a(self):
        from generate_loi import RECITAL_A_BODY
        assert "Digital Energy" in RECITAL_A_BODY


# -----------------------------------------------------------------------------
# Scope 0 — R-24 / R-25 / R-27 linter rules
# -----------------------------------------------------------------------------

class TestR24InlineCitation:
    """R-24 (fail): inline bracket citation in Recital B."""

    def test_r24_in_fail_rules(self):
        assert "R-24" in _FAIL_RULES
        pattern, scope, msg = _FAIL_RULES["R-24"]
        assert scope == "Recital B"

    def test_r24_matches_polarise_eu_bracket(self):
        import re
        pattern, _, _ = _FAIL_RULES["R-24"]
        assert re.search(pattern, "[polarise.eu]")
        assert re.search(pattern, "[swi.com]")
        assert re.search(pattern, "[companyhouse.de]")

    def test_r24_does_not_match_legitimate_tbc(self):
        import re
        pattern, _, _ = _FAIL_RULES["R-24"]
        assert not re.search(pattern, "[TBC]")
        assert not re.search(pattern, "[TO BE CONFIRMED]")


class TestR25VanityFinancial:
    """R-25 (fail): vanity-financial claim in Recital B."""

    def test_r25_in_fail_rules(self):
        assert "R-25" in _FAIL_RULES

    def test_r25_matches_valuation_phrases(self):
        import re
        pattern, _, _ = _FAIL_RULES["R-25"]
        assert re.search(pattern, "at a EUR 500m valuation")
        assert re.search(pattern, "valuation of $1bn")

    def test_r25_matches_raise_language(self):
        import re
        pattern, _, _ = _FAIL_RULES["R-25"]
        assert re.search(pattern, "raised $150M")

    def test_r25_does_not_match_macquarie_backing(self):
        """Named-endorser financing should pass R-25. The regex is designed
        to catch vanity patterns only."""
        import re
        pattern, _, _ = _FAIL_RULES["R-25"]
        text = "backed by senior infrastructure financing from Macquarie"
        assert not re.search(pattern, text)


class TestR27SigBlockTbc:
    """R-27 (fail): [TBC] rendered literally in sig-block Name or Title."""

    def test_r27_in_fail_rules(self):
        assert "R-27" in _FAIL_RULES

    def test_r27_matches_literal_name_tbc(self):
        import re
        pattern, _, _ = _FAIL_RULES["R-27"]
        assert re.search(pattern, "Name: [TBC]")
        assert re.search(pattern, "Title: [TBC]")

    def test_r27_does_not_match_fillable_blank(self):
        import re
        pattern, _, _ = _FAIL_RULES["R-27"]
        assert not re.search(pattern, "Title: ____________________________")
        assert not re.search(pattern, "Name: Carlos Reuven")


# -----------------------------------------------------------------------------
# Cross-cutting: v3.5.2 changes don't break v3.5.1 invariants
# -----------------------------------------------------------------------------

class TestV351InvariantsStillHold:
    """Regression: v3.5.1 sig-block + footer + Schedule 1 fixes still in place."""

    def test_sig_block_still_uses_render_placeholder(self):
        import inspect
        src = inspect.getsource(DocBuilder.signature)
        assert "_render_placeholder" in src

    def test_sig_block_has_no_kvk_rendering(self):
        import inspect
        src = inspect.getsource(DocBuilder.signature)
        assert "KvK:" not in src

    def test_sig_block_has_no_acknowledged_header(self):
        import inspect
        src = inspect.getsource(DocBuilder.signature)
        # Allow the comment mentioning it was removed
        active = [ln for ln in src.splitlines() if not ln.strip().startswith("#")]
        active_txt = "\n".join(active)
        assert "ACKNOWLEDGED AND AGREED" not in active_txt.upper()

    def test_derive_footer_entity_still_maps_bv_to_nl(self):
        assert DocBuilder._derive_footer_entity("Digital Energy Netherlands B.V.") == "nl"
        assert DocBuilder._derive_footer_entity("Digital Energy Group AG") == "ag"


# -----------------------------------------------------------------------------
# v3.5 polish — provider_term from short_name + entity-key validation
# -----------------------------------------------------------------------------

class TestV35Polish:
    """Polish items added during v3.5 consolidation."""

    def test_provider_term_derives_from_short_name(self):
        """v3.5 polish: provider_term should come from provider.short_name
        with fallback to "Digital Energy" for backward compat."""
        data = {
            "type": "Wholesale",
            "provider": {"short_name": "Custom Brand"},
            "counterparty": {"name": "X", "short": "X", "description": "x"},
            "programme": {}, "dates": {"loi_date": "1 Jan 2026"},
            "commercial": {"indicative_mw": "1"},
        }
        builder = DocBuilder(data)
        assert builder.provider_term == "Custom Brand"

    def test_provider_term_fallback_when_short_name_missing(self):
        data = {
            "type": "Wholesale",
            "provider": {"legal_name": "Some Corp"},   # no short_name
            "counterparty": {"name": "X", "short": "X", "description": "x"},
            "programme": {}, "dates": {"loi_date": "1 Jan 2026"},
            "commercial": {"indicative_mw": "1"},
        }
        builder = DocBuilder(data)
        assert builder.provider_term == "Digital Energy"
