"""Tests for the parser base class — Phase B5 scaffolding."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import (  # noqa: E402
    CorruptDocError,
    DocumentParser,
    FieldNotFoundError,
    ParseResult,
    ParserError,
    SchemaMismatchError,
    UnreadableScanError,
)


class _OKParser(DocumentParser):
    doc_type = "ok"
    parser_version = "0.1"
    populates_fields = ["f1"]

    def _extract_fields(self):
        return {"f1": 42}, ["warn1"], 0.9


class _BrokenParser(DocumentParser):
    doc_type = "broken"
    parser_version = "0.1"
    def _extract_fields(self):
        raise RuntimeError("simulated failure")


class _SchemaMismatchParser(DocumentParser):
    doc_type = "mismatch"
    def _extract_fields(self):
        raise SchemaMismatchError("not the right doc type")


def test_exception_hierarchy():
    assert issubclass(CorruptDocError, ParserError)
    assert issubclass(UnreadableScanError, ParserError)
    assert issubclass(SchemaMismatchError, ParserError)
    assert issubclass(FieldNotFoundError, ParserError)


def test_missing_path_raises_filenotfound(tmp_path):
    p = _OKParser(tmp_path / "does-not-exist.pdf")
    with pytest.raises(FileNotFoundError):
        p.parse()


def test_hash_deterministic_for_same_content(tmp_path):
    a = tmp_path / "a.bin"
    b = tmp_path / "b.bin"
    a.write_bytes(b"hello world")
    b.write_bytes(b"hello world")
    assert _OKParser(a)._compute_hash() == _OKParser(b)._compute_hash()


def test_hash_differs_for_different_content(tmp_path):
    a = tmp_path / "a.bin"
    b = tmp_path / "b.bin"
    a.write_bytes(b"hello")
    b.write_bytes(b"world")
    assert _OKParser(a)._compute_hash() != _OKParser(b)._compute_hash()


def test_hash_matches_independent_sha256(tmp_path):
    p = tmp_path / "abc.bin"
    p.write_bytes(b"abc")
    assert _OKParser(p)._compute_hash() == hashlib.sha256(b"abc").hexdigest()


def test_parse_returns_parse_result_with_all_fields(tmp_path):
    p = tmp_path / "x.bin"
    p.write_bytes(b"xy")
    result = _OKParser(p).parse()
    assert isinstance(result, ParseResult)
    assert result.parser_name == "ok"
    assert result.parser_version == "0.1"
    assert result.doc_path == p
    assert result.fields_populated == {"f1": 42}
    assert result.warnings == ["warn1"]
    assert result.confidence == 0.9
    assert result.doc_hash  # non-empty


def test_parse_result_to_dict_is_serialisable(tmp_path):
    p = tmp_path / "x.bin"
    p.write_bytes(b"x")
    result = _OKParser(p).parse()
    d = result.to_dict()
    import json
    json.dumps(d)  # must be JSON-serialisable
    assert d["parser_name"] == "ok"


def test_unexpected_exception_wrapped_as_corrupt(tmp_path):
    p = tmp_path / "x.bin"
    p.write_bytes(b"x")
    with pytest.raises(CorruptDocError, match="simulated failure"):
        _BrokenParser(p).parse()


def test_schema_mismatch_not_wrapped(tmp_path):
    p = tmp_path / "x.bin"
    p.write_bytes(b"x")
    # ParserError subclasses must NOT be wrapped as CorruptDocError —
    # they're already domain-meaningful.
    with pytest.raises(SchemaMismatchError):
        _SchemaMismatchParser(p).parse()


def test_filenotfound_not_wrapped(tmp_path):
    # FileNotFoundError from within _extract_fields should propagate
    # without wrapping (FileNotFoundError != ParserError but special-cased).
    class _FNFParser(DocumentParser):
        doc_type = "fnf"
        def _extract_fields(self):
            raise FileNotFoundError("inner")
    p = tmp_path / "x.bin"
    p.write_bytes(b"x")
    with pytest.raises(FileNotFoundError):
        _FNFParser(p).parse()


def test_subclass_must_implement_extract_fields(tmp_path):
    class _Abstract(DocumentParser):
        pass
    p = tmp_path / "x.bin"
    p.write_bytes(b"x")
    with pytest.raises(CorruptDocError, match="must be overridden"):
        _Abstract(p).parse()


def test_parse_result_default_confidence_is_1():
    r = ParseResult(parser_name="p", parser_version="0.1",
                    doc_path=Path("/x"), doc_hash="h")
    assert r.confidence == 1.0
