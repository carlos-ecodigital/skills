"""v3.8.0 — Recital B prescriptive slot template.

The prose Recital B field (`counterparty.description`) is replaced by a
typed 5-slot block (`counterparty.recital_b`). The engine renders a
deterministic boring sentence; freeform composition is gone. This test
file is the executable contract — RED-first per PRINCIPLES.md #4.

Plan: ~/.claude/plans/expressive-cooking-flamingo.md (v3.8 section).
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest


SALES_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SALES_DIR))

from recital_b_vocab import (  # noqa: E402
    LEGAL_FORM_ENUM,
    OPERATIONAL_VERB_ENUM,
    BANNED_PHRASES,
    url_tier,
    find_banned_phrases,
    validate_legal_form,
    validate_operational_verb,
    find_named_entities_in_text,
    render_recital_b_sentence,
)


# -----------------------------------------------------------------------------
# vocab — closed enums
# -----------------------------------------------------------------------------

class TestLegalFormEnum:

    def test_nl_accepts_bv(self):
        ok, _ = validate_legal_form("B.V.", "Netherlands")
        assert ok

    def test_nl_rejects_gmbh(self):
        ok, msg = validate_legal_form("GmbH", "Netherlands")
        assert not ok
        assert "B.V." in msg

    def test_unknown_jurisdiction_passes_with_warn(self):
        ok, msg = validate_legal_form("S.p.A.", "Italy")
        # Italy is in the enum, so let's pick something genuinely unknown.
        ok, msg = validate_legal_form("PJSC", "Tatarstan")
        assert ok
        assert "R-form-unknown" in msg

    def test_uk_accepts_ltd_and_plc(self):
        for form in ("Ltd", "PLC"):
            ok, _ = validate_legal_form(form, "United Kingdom")
            assert ok, form

    def test_us_rejects_bv(self):
        ok, _ = validate_legal_form("B.V.", "United States")
        assert not ok


class TestOperationalVerbEnum:

    def test_providing_accepted(self):
        ok, _ = validate_operational_verb("providing")
        assert ok

    def test_pioneering_rejected(self):
        ok, msg = validate_operational_verb("pioneering")
        assert not ok
        assert "OPERATIONAL_VERB_ENUM" in msg

    def test_leading_rejected(self):
        ok, _ = validate_operational_verb("leading")
        assert not ok

    def test_manufacturing_accepted(self):
        ok, _ = validate_operational_verb("manufacturing")
        assert ok


# -----------------------------------------------------------------------------
# vocab — banned-phrase regex
# -----------------------------------------------------------------------------

class TestBannedPhrases:

    @pytest.mark.parametrize("text", [
        "leading AI cloud platform",
        "world-class infrastructure",
        "cutting-edge GPU compute",
        "next-generation workloads",
        "frontier model workloads",
        "pioneering AI infrastructure",
    ])
    def test_marketing_puffery_blocked(self, text):
        findings = find_banned_phrases(text)
        assert findings
        assert any(cls == "marketing_puffery" for cls, _ in findings), findings

    def test_adjective_stack_blocked(self):
        findings = find_banned_phrases("AI-native fast-growing platform")
        classes = {cls for cls, _ in findings}
        assert "adjective_stacks" in classes

    def test_press_release_voice_blocked(self):
        findings = find_banned_phrases("reshaping the industry")
        assert any(cls == "press_release_voice" for cls, _ in findings)

    def test_powering_by_grid_allowed(self):
        # "powering by N MW grid connection" is factual, not pump.
        findings = find_banned_phrases("powering by 100MW grid connection from Liander")
        assert not any(cls == "press_release_voice" for cls, _ in findings)

    def test_powering_workloads_blocked(self):
        # "powering the workloads at OpenAI" is pump.
        findings = find_banned_phrases("powering the workloads at OpenAI")
        assert any(cls == "press_release_voice" for cls, _ in findings)

    def test_future_tense_blocked(self):
        findings = find_banned_phrases("plans to deploy 100MW")
        assert any(cls == "future_tense_ambition" for cls, _ in findings)

    def test_aspirational_scale_blocked(self):
        findings = find_banned_phrases("operating globally")
        assert any(cls == "aspirational_scale" for cls, _ in findings)

    def test_pump_frame_phrase_blocked(self):
        findings = find_banned_phrases("backed by tier-1 VCs")
        assert any(cls == "pump_frame_phrases" for cls, _ in findings)

    def test_clean_factual_text_passes(self):
        text = (
            "is a private limited liability company organised under the "
            "laws of the Netherlands, engaged in providing GPU computing "
            "services for AI-research customers, from its Amsterdam data "
            "centre"
        )
        findings = find_banned_phrases(text)
        assert findings == [], findings


# -----------------------------------------------------------------------------
# URL tier heuristic
# -----------------------------------------------------------------------------

class TestUrlTier:

    @pytest.mark.parametrize("url,tier", [
        ("https://www.sec.gov/Archives/edgar/data/...",        1),
        ("https://kvk.nl/orderstraat/...",                       1),
        ("https://www.handelsregister.de/...",                   1),
        ("https://news.microsoft.com/source/2025/...",           1),  # press path-hint
        ("https://www.reuters.com/business/article-id/",         2),
        ("https://www.ft.com/content/...",                       2),
        ("https://www.bloomberg.com/news/...",                   2),
        ("https://www.gartner.com/document/...",                 2),
        ("https://techcrunch.com/2025/05/01/some-startup",       2),
        ("https://example.com/",                                 3),
        ("https://medium.com/random-blog/post",                  3),
        ("https://twitter.com/handle/status/...",                3),
    ])
    def test_tier_classification(self, url, tier):
        assert url_tier(url) == tier


# -----------------------------------------------------------------------------
# Named-entity detection
# -----------------------------------------------------------------------------

class TestNamedEntityDetection:

    def test_microsoft_detected(self):
        names = find_named_entities_in_text(
            "with announced 12 MW capacity contracted with Microsoft"
        )
        assert "Microsoft" in names

    def test_geographic_allowed(self):
        names = find_named_entities_in_text(
            "with offices in Amsterdam, Berlin, and Zurich"
        )
        assert "Amsterdam" not in names
        assert "Berlin" not in names
        assert "Zurich" not in names

    def test_multi_word_company_detected(self):
        names = find_named_entities_in_text(
            "Series B led by Sequoia Capital"
        )
        assert any("Sequoia" in n for n in names)

    def test_clean_no_names(self):
        names = find_named_entities_in_text(
            "from its Amsterdam data centre"
        )
        # Only "Amsterdam" — which is allowlisted — should appear, hence empty.
        assert names == []


# -----------------------------------------------------------------------------
# Sentence rendering — deterministic concatenation
# -----------------------------------------------------------------------------

def _example_slots(*, fact=None) -> dict:
    slots = {
        "legal_identity": {
            "legal_form": "B.V.",
            "jurisdiction": "Netherlands",
            "registration": {"type": "KvK", "number": "12345678"},
        },
        "operational_verb": {
            "verb": "providing",
            "object": "GPU computing services",
        },
        "customer_use_case": {
            "category": "AI-research customers",
        },
        "material_asset": {
            "asset": "Amsterdam data centre",
        },
    }
    if fact:
        slots["bargain_relevant_fact"] = fact
    return slots


class TestSentenceRender:

    def test_four_slot_render(self):
        sentence = render_recital_b_sentence(
            _example_slots(),
            party_label="Customer",
            short_name="Acme",
        )
        assert sentence.startswith('(B) Acme (the "Customer") is a B.V.')
        assert "engaged in providing GPU computing services" in sentence
        assert "AI-research customers" in sentence
        assert "Amsterdam data centre" in sentence
        assert sentence.endswith(".")

    def test_five_slot_render(self):
        sentence = render_recital_b_sentence(
            _example_slots(fact={
                "claim": "with a 12 MW IT anchor contract with Microsoft",
                "named_entities": [{
                    "name": "Microsoft",
                    "relationship_type": "named_customer",
                    "materiality": "Largest disclosed revenue source affecting Cl. 4 capacity allocation",
                    "proof": {
                        "url": "https://news.microsoft.com/source/2025/11/10/...",
                        "dated": "2025-11-10",
                    },
                }],
                "source": {"tier": 1, "url": "https://news.microsoft.com/...", "retrieved": "2026-04-30"},
            }),
            party_label="Customer",
            short_name="Acme",
        )
        assert "with a 12 MW IT anchor contract with Microsoft." in sentence

    def test_rendered_sentence_is_R32_clean(self):
        sentence = render_recital_b_sentence(
            _example_slots(),
            party_label="Customer",
            short_name="Acme",
        )
        findings = find_banned_phrases(sentence)
        assert findings == [], (
            f"Rendered sentence contains banned phrases: {findings}\n"
            f"Sentence: {sentence}"
        )


# -----------------------------------------------------------------------------
# Engine integration (R-32 + R-DEPRECATED-FIELD via generate_loi.py::recitals)
# -----------------------------------------------------------------------------

@pytest.fixture
def base_intake() -> dict:
    """A minimal valid v3.8.0 intake using the slot block (no description)."""
    return {
        "type": "Wholesale",
        "provider": {
            "entity": "de_nl",
            "signatory_mode": "pre_msa",
        },
        "counterparty": {
            "name": "Acme Corp B.V.",
            "short": "Acme",
            "address": "Herengracht 1, 1015 BA Amsterdam, the Netherlands",
            "jurisdiction": "Netherlands",
            "reg_type": "KvK",
            "reg_number": "98580086",
            "contact_name": "Jane Doe",
            "contact_title": "CEO",
            "salutation": "Ms Doe",
            "signatory_name": "Jane Doe",
            "signatory_title": "Chief Executive Officer",
            "recital_b": {
                "legal_identity": {
                    "legal_form": "B.V.",
                    "jurisdiction": "Netherlands",
                    "registration": {"type": "KvK", "number": "98580086"},
                    "source": {
                        "tier": 1,
                        "url": "https://www.kvk.nl/handelsregister/...",
                        "retrieved": "2026-05-01",
                    },
                },
                "operational_verb": {
                    "verb": "providing",
                    "object": "GPU computing services",
                    "source": {
                        "tier": 1,
                        "url": "https://news.acme.com/about",
                        "retrieved": "2026-05-01",
                        "source_quote": "Acme provides GPU computing services to AI research labs.",
                    },
                },
                "customer_use_case": {
                    "category": "AI-research customers",
                    "source": {
                        "tier": 1,
                        "url": "https://news.acme.com/customers",
                        "retrieved": "2026-05-01",
                        "source_quote": "Acme serves AI-research customers across Europe.",
                    },
                },
                "material_asset": {
                    "asset": "Amsterdam data centre",
                    "source": {
                        "tier": 1,
                        "url": "https://news.acme.com/datacentre",
                        "retrieved": "2026-05-01",
                        "source_quote": "Acme operates from its Amsterdam data centre.",
                    },
                },
            },
        },
        "programme": {
            "platform_mw": 10,
            "site_count": 1,
            "recital_a_variant": "default",
        },
        "dates": {
            "loi_date": "1 May 2026",
            "validity_date": "1 May 2027",
        },
        "commercial": {},
        "protection": {},
        "choices": {},
    }


class TestEngineRejectsLegacyDescription:
    """`counterparty.description` field is removed in v3.8.0. Intakes
    that still use it must fail with R-DEPRECATED-FIELD pointing at the
    migration path."""

    def test_legacy_description_rejected(self, base_intake):
        intake = dict(base_intake)
        # Add legacy description alongside slot block — should still fail
        intake["counterparty"] = dict(base_intake["counterparty"])
        intake["counterparty"]["description"] = (
            "is an AI cloud platform building cutting-edge GPU infrastructure"
        )
        from generate_loi import validate_errors
        errors = validate_errors(intake)
        assert any("R-DEPRECATED-FIELD" in e for e in errors), (
            f"Expected R-DEPRECATED-FIELD in errors: {errors}"
        )

    def test_no_description_no_recital_b_fails(self, base_intake):
        intake = dict(base_intake)
        intake["counterparty"] = dict(base_intake["counterparty"])
        del intake["counterparty"]["recital_b"]
        from generate_loi import validate_errors
        errors = validate_errors(intake)
        assert any("recital_b" in e.lower() for e in errors), (
            f"Expected error citing missing recital_b: {errors}"
        )


class TestEngineRendersFromSlots:
    """The engine builds Recital B from the slot block. Check key
    invariants on the rendered output."""

    def test_recital_b_built_from_slots(self, base_intake, tmp_path):
        from generate_loi import LOI
        loi = LOI(base_intake)
        loi.build()
        text = "\n".join(p.text for p in loi.doc.paragraphs)
        assert '(B) Acme (the "Customer")' in text
        assert "engaged in providing GPU computing services" in text
        assert "AI-research customers" in text
        assert "Amsterdam data centre" in text

    def test_no_banned_phrases_in_rendered_recital(self, base_intake):
        from generate_loi import LOI
        loi = LOI(base_intake)
        loi.build()
        text = "\n".join(p.text for p in loi.doc.paragraphs)
        # Find recital B line
        recital_b_lines = [l for l in text.split("\n") if l.startswith("(B)")]
        assert recital_b_lines
        findings = find_banned_phrases(recital_b_lines[0])
        assert findings == [], (
            f"Rendered Recital B contains banned phrases: {findings}\n"
            f"Line: {recital_b_lines[0]}"
        )


class TestR32SlotValidation:
    """R-32 fires when a slot value contains a banned phrase or fails
    closed-enum check."""

    def test_banned_verb_fails_R32(self, base_intake):
        intake = dict(base_intake)
        intake["counterparty"] = {**base_intake["counterparty"]}
        intake["counterparty"]["recital_b"] = {
            **base_intake["counterparty"]["recital_b"],
            "operational_verb": {
                "verb": "pioneering",  # not in enum
                "object": "GPU compute",
                "source": base_intake["counterparty"]["recital_b"]["operational_verb"]["source"],
            },
        }
        from generate_loi import validate_errors
        errors = validate_errors(intake)
        assert any("R-32" in e or "OPERATIONAL_VERB_ENUM" in e for e in errors), (
            f"Expected R-32 / OPERATIONAL_VERB_ENUM in errors: {errors}"
        )

    def test_marketing_puffery_in_object_fails_R32(self, base_intake):
        intake = dict(base_intake)
        intake["counterparty"] = {**base_intake["counterparty"]}
        intake["counterparty"]["recital_b"] = {
            **base_intake["counterparty"]["recital_b"],
            "operational_verb": {
                "verb": "providing",
                "object": "world-class GPU compute",  # banned phrase
                "source": base_intake["counterparty"]["recital_b"]["operational_verb"]["source"],
            },
        }
        from generate_loi import validate_errors
        errors = validate_errors(intake)
        assert any("R-32" in e or "world-class" in e for e in errors), (
            f"Expected R-32 banned-phrase error: {errors}"
        )

    def test_legal_form_jurisdiction_mismatch_fails_R32(self, base_intake):
        intake = dict(base_intake)
        intake["counterparty"] = {**base_intake["counterparty"]}
        intake["counterparty"]["recital_b"] = {
            **base_intake["counterparty"]["recital_b"],
            "legal_identity": {
                "legal_form": "B.V.",
                "jurisdiction": "United States",  # wrong jurisdiction for B.V.
                "registration": {"type": "KvK", "number": "12345678"},
                "source": base_intake["counterparty"]["recital_b"]["legal_identity"]["source"],
            },
        }
        from generate_loi import validate_errors
        errors = validate_errors(intake)
        assert any("R-32" in e or "legal_form" in e for e in errors), (
            f"Expected R-32 legal_form mismatch error: {errors}"
        )


class TestSlot5OptionalWithInfo:

    def test_no_slot_5_renders_without_warn(self, base_intake):
        from generate_loi import LOI
        loi = LOI(base_intake)
        loi.build()
        # Should render fine without slot 5
        text = "\n".join(p.text for p in loi.doc.paragraphs)
        assert "(B) Acme" in text

    def test_slot_5_named_entity_without_proof_fails(self, base_intake):
        intake = dict(base_intake)
        intake["counterparty"] = {**base_intake["counterparty"]}
        intake["counterparty"]["recital_b"] = {
            **base_intake["counterparty"]["recital_b"],
            "bargain_relevant_fact": {
                "claim": "with announced anchor contract with Microsoft",
                # missing named_entities[] proof block
                "source": {"tier": 1, "url": "https://news.example.com/", "retrieved": "2026-05-01"},
            },
        }
        from generate_loi import validate_errors
        errors = validate_errors(intake)
        assert any("R-32" in e or "named_entities" in e for e in errors), (
            f"Expected R-32 missing named_entities proof: {errors}"
        )

    def test_slot_5_named_entity_with_proof_passes(self, base_intake):
        intake = dict(base_intake)
        intake["counterparty"] = {**base_intake["counterparty"]}
        intake["counterparty"]["recital_b"] = {
            **base_intake["counterparty"]["recital_b"],
            "bargain_relevant_fact": {
                "claim": "with announced anchor contract with Microsoft",
                "named_entities": [{
                    "name": "Microsoft",
                    "relationship_type": "named_customer",
                    "materiality": (
                        "Microsoft anchor represents counterparty's largest "
                        "disclosed revenue source and validates ramp ability."
                    ),
                    "proof": {
                        "url": "https://news.microsoft.com/source/2025/11/10/...",
                        "dated": "2025-11-10",
                    },
                }],
                "source": {"tier": 1, "url": "https://news.microsoft.com/", "retrieved": "2026-05-01"},
            },
        }
        from generate_loi import validate_errors
        errors = validate_errors(intake)
        # Should not have R-32 errors
        assert not any("R-32" in e for e in errors), (
            f"Unexpected R-32 errors on valid slot 5: {errors}"
        )
