"""Tests for ``site_doc_base.normalise_placeholder``.

The canonical placeholder normaliser for the Sites stream. Engines route
every rendered value through this before it reaches python-docx so that:
  - missing values (None, empty, author TODO markers) collapse to [TBC]
  - real data (ints, floats, False, 0) renders literally — never silently
    treated as "missing"
  - structured values (dict) return [TBC] rather than a raw ``str(dict)``
    dump that would leak field keys into the document
"""

from __future__ import annotations

from site_doc_base import TBC_TOKEN, normalise_placeholder


# ---------------------------------------------------------------------------
# Missing-value branches → [TBC]
# ---------------------------------------------------------------------------

def test_none_returns_tbc():
    assert normalise_placeholder(None) == TBC_TOKEN


def test_empty_string_returns_tbc():
    assert normalise_placeholder("") == TBC_TOKEN


def test_whitespace_only_string_returns_tbc():
    assert normalise_placeholder("   \t\n ") == TBC_TOKEN


def test_todo_marker_returns_tbc():
    assert normalise_placeholder("TODO(kadaster_enrichment)") == TBC_TOKEN


def test_tbd_slot_token_returns_tbc():
    assert normalise_placeholder("[TBD_Phase_B5]") == TBC_TOKEN


def test_already_canonical_tbc_returns_tbc():
    """Idempotent — feeding [TBC] back through returns [TBC]."""
    assert normalise_placeholder(TBC_TOKEN) == TBC_TOKEN


def test_empty_list_returns_tbc():
    assert normalise_placeholder([]) == TBC_TOKEN


def test_empty_dict_returns_tbc():
    assert normalise_placeholder({}) == TBC_TOKEN


# ---------------------------------------------------------------------------
# Real-data branches → render literally (do NOT collapse to [TBC])
# ---------------------------------------------------------------------------

def test_zero_integer_renders_literally():
    """A real zero (e.g. export_mw=0 for a load-only partner) must render
    as "0", not [TBC]. The prior string-coerce trick would have caught
    this because ``str(0).strip() = "0"`` is truthy, but exercise the
    explicit int branch to lock in the contract."""
    assert normalise_placeholder(0) == "0"


def test_negative_integer_renders_literally():
    assert normalise_placeholder(-1) == "-1"


def test_float_renders_literally():
    assert normalise_placeholder(3.14) == "3.14"


def test_false_bool_renders_literally():
    """False is a meaningful value (e.g. 'kvk_present': False), not a
    missing marker — must render as 'False' not [TBC]."""
    assert normalise_placeholder(False) == "False"


def test_true_bool_renders_literally():
    assert normalise_placeholder(True) == "True"


# ---------------------------------------------------------------------------
# List / tuple → comma-joined
# ---------------------------------------------------------------------------

def test_list_returns_comma_joined():
    assert normalise_placeholder(["a", "b", "c"]) == "a, b, c"


def test_tuple_returns_comma_joined():
    assert normalise_placeholder(("a", "b")) == "a, b"


# ---------------------------------------------------------------------------
# Dict → [TBC] (structured value should never reach a rendered cell)
# ---------------------------------------------------------------------------

def test_nonempty_dict_returns_tbc():
    """A dict of parser fields accidentally assigned to a scalar cell must
    collapse to [TBC] rather than leak ``{'a': 1, 'b': 2}`` into the doc."""
    assert normalise_placeholder({"a": 1, "b": 2}) == TBC_TOKEN


# ---------------------------------------------------------------------------
# Happy path — regular strings
# ---------------------------------------------------------------------------

def test_regular_string_returned_unchanged():
    assert normalise_placeholder("Van Gog kwekerijen Grubbenvorst B.V.") == (
        "Van Gog kwekerijen Grubbenvorst B.V."
    )


def test_string_is_stripped():
    assert normalise_placeholder("  hello  ") == "hello"


# ---------------------------------------------------------------------------
# Custom fallback
# ---------------------------------------------------------------------------

def test_custom_fallback_used_when_missing():
    assert normalise_placeholder(None, fallback="[PENDING]") == "[PENDING]"


def test_custom_fallback_is_idempotent():
    """Feeding the custom fallback back through still returns it."""
    assert normalise_placeholder("[PENDING]", fallback="[PENDING]") == "[PENDING]"
