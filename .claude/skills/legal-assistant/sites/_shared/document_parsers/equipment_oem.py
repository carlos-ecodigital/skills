"""Equipment-OEM specification parser — CHP / BESS / Solar PV.

A single-parser dispatcher for the three equipment-class supporting
documents registered in the field-registry:

  - ``chp_commissioning_cert``       → ``_chp_kw_e``, ``_chp_kw_th``,
                                        ``_chp_age_years``.
  - ``bess_grid_sharing_agreement``  → ``_bess_mw``, ``_bess_mwh``,
                                        ``_bess_chemistry``.
  - ``solar_pv_yield_report``        → ``_pv_kwp``, ``_pv_annual_kwh``.

The parser detects the equipment type from terminology found in the
document text, then dispatches to the appropriate extraction routine.
If multiple types are detected with roughly equal signal strength, all
matching extractions run and a warning is emitted.

The registry ``verifies`` arrays for these supporting docs are empty
(chp_commissioning_cert verifies F1_chp_lease + F1a_chp_lease_fee, which
this parser does not extract — those are commercial fields set at HoT
contract time). This parser therefore populates OEM / technical
meta-fields (``_chp_*``, ``_bess_*``, ``_pv_*``).

Any unexpected failure is wrapped by the base class as ``CorruptDocError``.
"""

from __future__ import annotations

import re
from datetime import date
from typing import Any, Dict, List, Optional, Tuple

from .base import CorruptDocError, DocumentParser, UnreadableScanError


def _nl_to_float(raw: str) -> Optional[float]:
    """Convert a Dutch-formatted number string to float.

    Handles NL (``1.234,56``), US (``1,234.56``), plain-decimal
    (``16.5`` / ``16,5``), and all-dots-as-thousands (``1.425.000``).
    """
    s = raw.strip().replace("\u00a0", "").replace(" ", "")
    if not s:
        return None
    if "." in s and "," in s:
        # Ambiguous NL vs US — pick by position of the last separator.
        last_dot = s.rfind(".")
        last_comma = s.rfind(",")
        if last_comma > last_dot:
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        # Heuristic: NL decimal comma if there are 1-3 digits after the
        # comma. If the comma is a thousands separator (groups of 3),
        # strip it.
        tail = s.split(",")[-1]
        if len(tail) == 3 and s.count(",") >= 1 and "." not in s:
            s_no_comma = s.replace(",", "")
            try:
                float(s_no_comma)
                s = s_no_comma
            except ValueError:
                s = s.replace(",", ".")
        else:
            s = s.replace(",", ".")
    elif s.count(".") >= 2:
        # Multiple dots with no comma => NL thousands separators
        # (``1.425.000``). Strip them and parse as an integer.
        if all(len(part) == 3 for part in s.split(".")[1:]):
            s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


class EquipmentOEMParser(DocumentParser):
    """Multi-flavour OEM spec parser for CHP, BESS, and Solar PV."""

    doc_type = "equipment_oem"    # generic; auto-detects specifics
    parser_version = "0.1"
    populates_fields = [
        # CHP
        "_chp_kw_e",
        "_chp_kw_th",
        "_chp_age_years",
        # BESS
        "_bess_mw",
        "_bess_mwh",
        "_bess_chemistry",
        # Solar PV
        "_pv_kwp",
        "_pv_annual_kwh",
        # always present
        "_equipment_type",
    ]

    # Equipment-type detection patterns — each entry is a (name, list-of-regex).
    TYPE_PATTERNS: Dict[str, List[str]] = {
        "chp": [
            r"\bCHP\b",
            r"Combined\s+Heat\s+and\s+Power",
            r"warmtekrachtkoppeling",
            r"\bWKK\b",
            r"inbedrijfstellings?certificaat",
            r"commissioning\s+certificate",
        ],
        "bess": [
            r"\bBESS\b",
            r"Battery\s+Energy\s+Storage",
            r"batterij(?:systeem)?",
            r"grid[-\s]sharing",
            r"netdelings?overeenkomst",
        ],
        "solar_pv": [
            r"\bPV\b",
            r"\bSolar\b",
            r"zonnepanel(?:en)?",
            r"photovoltaic",
            r"opbrengstrapport",
            r"yield\s+report",
        ],
    }

    # -------- CHP patterns --------------------------------------------
    # "450 kWe", "450 kW_e", "450 kW e", "450 kWel"
    CHP_KW_E_RE = re.compile(
        r"(\d{1,5}(?:[.,]\d+)?)\s*kW[_\s]?e(?:l)?\b",
        re.IGNORECASE,
    )
    # "600 kWth", "600 kW_th", "600 kWt", "600 kW thermal", "600 kW thermisch"
    CHP_KW_TH_RE = re.compile(
        r"(\d{1,5}(?:[.,]\d+)?)\s*kW[_\s]?"
        r"(?:th|t|thermal|thermisch)\b",
        re.IGNORECASE,
    )
    # Commissioning date → used to derive age years.
    COMMISSIONING_RE = re.compile(
        r"(?:inbedrijfstelling|commissioning|commissioned|in\s+bedrijf\s+gesteld)"
        r"[^\n0-9]{0,30}"
        r"(?P<d>\d{1,2})[-/\.](?P<m>\d{1,2})[-/\.](?P<y>\d{4})",
        re.IGNORECASE,
    )
    COMMISSIONING_YEAR_RE = re.compile(
        r"(?:inbedrijfstelling|commissioning|commissioned|in\s+bedrijf\s+gesteld)"
        r"[^\n0-9]{0,30}(\d{4})\b",
        re.IGNORECASE,
    )

    # -------- BESS patterns -------------------------------------------
    BESS_MW_RE = re.compile(r"(\d{1,4}(?:[.,]\d+)?)\s*MW\b(?!h)", re.IGNORECASE)
    BESS_MWH_RE = re.compile(r"(\d{1,4}(?:[.,]\d+)?)\s*MWh\b", re.IGNORECASE)
    BESS_CHEMISTRY_RE = re.compile(
        r"\b(LFP|NMC|NCA|LTO|NiMH|LiFePO4|LiFePO\u2084)\b"
    )

    # -------- Solar PV patterns ---------------------------------------
    PV_KWP_RE = re.compile(r"(\d{1,5}(?:[.,]\d+)?)\s*kWp\b", re.IGNORECASE)
    # Annual yield: "jaarlijkse opbrengst 1.234.567 kWh" / "annual yield 1200 MWh".
    PV_ANNUAL_KWH_RE = re.compile(
        r"(?:jaarlijkse?\s+(?:opbrengst|productie)|annual\s+(?:yield|production)|"
        r"per\s+jaar|per\s+annum)"
        r"[^\n0-9]{0,40}"
        r"(\d{1,3}(?:[\.\, \u00a0]\d{3})*(?:[\.,]\d+)?)\s*(kWh|MWh)\b",
        re.IGNORECASE,
    )
    PV_ANNUAL_FALLBACK_RE = re.compile(
        r"(\d{1,3}(?:[\.\, \u00a0]\d{3})+)\s*(kWh|MWh)\b",
        re.IGNORECASE,
    )

    # ------------------------------------------------------------------
    def _detect_types(self, text: str) -> Tuple[List[str], Dict[str, int]]:
        """Return (detected_types, score_per_type).

        ``detected_types`` is sorted by score descending. A type is
        "detected" only if at least one pattern matches. This makes the
        auto-dispatch robust to a PV document that happens to mention
        "solar PV" only in boilerplate — at least one pattern match is
        necessary, but patterns are curated to be reasonably specific.
        """
        scores: Dict[str, int] = {}
        for t, patterns in self.TYPE_PATTERNS.items():
            score = 0
            for p in patterns:
                if re.search(p, text, re.IGNORECASE):
                    score += 1
            if score > 0:
                scores[t] = score
        ordered = sorted(scores, key=lambda k: scores[k], reverse=True)
        return ordered, scores

    # ------------------------------------------------------------------
    def _extract_chp(
        self, text: str, fields: Dict[str, Any], warnings: List[str]
    ) -> None:
        e_m = self.CHP_KW_E_RE.search(text)
        if e_m:
            v = _nl_to_float(e_m.group(1))
            if v is not None:
                fields["_chp_kw_e"] = v
        if "_chp_kw_e" not in fields:
            warnings.append("_chp_kw_e: no kWe value found")

        th_m = self.CHP_KW_TH_RE.search(text)
        if th_m:
            v = _nl_to_float(th_m.group(1))
            if v is not None:
                fields["_chp_kw_th"] = v
        if "_chp_kw_th" not in fields:
            warnings.append("_chp_kw_th: no kWth value found")

        today = date.today()
        age: Optional[int] = None
        dm = self.COMMISSIONING_RE.search(text)
        if dm:
            try:
                dd = int(dm.group("d"))
                mm = int(dm.group("m"))
                yy = int(dm.group("y"))
                commission_date = date(yy, mm, dd)
                age = today.year - commission_date.year
                # Correct by month/day.
                if (today.month, today.day) < (commission_date.month, commission_date.day):
                    age -= 1
            except ValueError:
                pass
        if age is None:
            ym = self.COMMISSIONING_YEAR_RE.search(text)
            if ym:
                try:
                    yy = int(ym.group(1))
                    age = today.year - yy
                except ValueError:
                    pass
        if age is not None and age >= 0:
            fields["_chp_age_years"] = age
        else:
            warnings.append("_chp_age_years: no commissioning date / year found")

    def _extract_bess(
        self, text: str, fields: Dict[str, Any], warnings: List[str]
    ) -> None:
        mw_m = self.BESS_MW_RE.search(text)
        if mw_m:
            v = _nl_to_float(mw_m.group(1))
            if v is not None:
                fields["_bess_mw"] = v
        if "_bess_mw" not in fields:
            warnings.append("_bess_mw: no MW value found")

        mwh_m = self.BESS_MWH_RE.search(text)
        if mwh_m:
            v = _nl_to_float(mwh_m.group(1))
            if v is not None:
                fields["_bess_mwh"] = v
        if "_bess_mwh" not in fields:
            warnings.append("_bess_mwh: no MWh value found")

        chem_m = self.BESS_CHEMISTRY_RE.search(text)
        if chem_m:
            raw = chem_m.group(1).upper()
            # Normalise LiFePO4 -> LFP.
            if raw.startswith("LIFEPO"):
                raw = "LFP"
            fields["_bess_chemistry"] = raw
        else:
            warnings.append(
                "_bess_chemistry: no recognised chemistry "
                "(LFP / NMC / NCA / LTO / NiMH) found"
            )

    def _extract_pv(
        self, text: str, fields: Dict[str, Any], warnings: List[str]
    ) -> None:
        kwp_m = self.PV_KWP_RE.search(text)
        if kwp_m:
            v = _nl_to_float(kwp_m.group(1))
            if v is not None:
                fields["_pv_kwp"] = v
        if "_pv_kwp" not in fields:
            warnings.append("_pv_kwp: no kWp value found")

        annual_m = self.PV_ANNUAL_KWH_RE.search(text)
        kwh_val: Optional[float] = None
        if annual_m:
            v = _nl_to_float(annual_m.group(1))
            unit = annual_m.group(2).lower()
            if v is not None:
                kwh_val = v * 1000 if unit == "mwh" else v
        if kwh_val is None:
            # Fallback: largest thousand-separated kWh / MWh number.
            candidates: List[float] = []
            for m in self.PV_ANNUAL_FALLBACK_RE.finditer(text):
                v = _nl_to_float(m.group(1))
                if v is None:
                    continue
                unit = m.group(2).lower()
                candidates.append(v * 1000 if unit == "mwh" else v)
            if candidates:
                kwh_val = max(candidates)
                warnings.append(
                    "_pv_annual_kwh: no labelled annual yield; took the "
                    f"largest kWh/MWh amount ({kwh_val})"
                )
        if kwh_val is not None:
            fields["_pv_annual_kwh"] = kwh_val
        else:
            warnings.append("_pv_annual_kwh: no annual-yield value found")

    # ------------------------------------------------------------------
    def _extract_fields(self) -> Tuple[Dict[str, Any], List[str], float]:
        try:
            import fitz  # PyMuPDF
        except ImportError as e:  # pragma: no cover — env sanity
            raise ImportError(
                "equipment_oem parser requires PyMuPDF (fitz). "
                "Install via `pip install pymupdf`."
            ) from e

        try:
            doc = fitz.open(str(self.doc_path))
        except Exception as e:
            raise CorruptDocError(f"cannot open PDF: {e}") from e

        text = ""
        page_count = doc.page_count
        for page in doc:
            text += page.get_text() or ""
        doc.close()

        if len(text.strip()) < 50:
            raise UnreadableScanError(
                f"{self.doc_path.name} has <50 chars extractable text; "
                "likely an image-only scan. OCR required (out of v0.1 scope)."
            )

        fields: Dict[str, Any] = {}
        warnings: List[str] = [
            "equipment_oem: registry `verifies` for chp_commissioning_cert "
            "names F1_chp_lease / F1a_chp_lease_fee (commercial contract "
            "fields); parser populates OEM technical meta-fields instead "
            "(_chp_*, _bess_*, _pv_*). bess_grid_sharing_agreement and "
            "solar_pv_yield_report have empty `verifies`."
        ]

        if page_count and len(text) / page_count < 200:
            warnings.append(
                f"low text density ({len(text) // page_count} chars/page); "
                "may be partial scan"
            )

        detected, scores = self._detect_types(text)

        if not detected:
            warnings.append(
                "_equipment_type: no CHP / BESS / Solar-PV terminology "
                "detected; nothing to extract"
            )
            fields["_equipment_type"] = None
            return fields, warnings, 0.1

        # Primary type = top-scoring; tie within 1 point ⇒ ambiguous.
        primary = detected[0]
        ambiguous_peers = [
            t for t in detected[1:] if scores[t] >= scores[primary] - 1
        ]
        fields["_equipment_type"] = primary
        if ambiguous_peers:
            fields["_equipment_type_candidates"] = [primary] + ambiguous_peers
            warnings.append(
                f"_equipment_type: ambiguous — multiple classes detected "
                f"with similar scores ({scores}); running all matching "
                f"extractors"
            )

        runners = [primary] + ambiguous_peers
        for t in runners:
            if t == "chp":
                self._extract_chp(text, fields, warnings)
            elif t == "bess":
                self._extract_bess(text, fields, warnings)
            elif t == "solar_pv":
                self._extract_pv(text, fields, warnings)

        # Confidence: proportion of runner-type specific fields populated.
        expected_by_type = {
            "chp": ["_chp_kw_e", "_chp_kw_th", "_chp_age_years"],
            "bess": ["_bess_mw", "_bess_mwh", "_bess_chemistry"],
            "solar_pv": ["_pv_kwp", "_pv_annual_kwh"],
        }
        expected: List[str] = []
        for t in runners:
            expected.extend(expected_by_type[t])
        populated = sum(1 for f in expected if f in fields)
        confidence = populated / len(expected) if expected else 0.1
        # Clamp.
        confidence = max(0.0, min(1.0, confidence))
        return fields, warnings, confidence
