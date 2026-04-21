"""Registry enum normaliser — maps parser bare tokens to registry
enum values (slash-combined bilingual strings).

Source of truth: ``sites/hot/field-registry.json`` field-level ``options``
arrays. This module maintains a static per-field TOKEN_MAP whose **target**
values are cross-checked against the registry the first time the module is
called with a registry — drift there raises ``EnumNormaliserError``.

Parsers emit bare tokens that reflect raw extracted source-document text
(e.g. KvK parser → ``"Sole"`` / ``"Joint"``; Kadaster parser → ``"Eigendom"``
/ ``"Erfpacht"``; Kadaster D3 encumbrances → ``True``/``False``).  The
registry v1.1 expects slash-combined bilingual strings
(``"Sole / Zelfstandig bevoegd"`` etc.).  This layer sits between the
parsers and the HoT engine so the XML form-fill receives exactly what the
registry enumerates.

TODO(registry-maintainer): as new enum fields land in field-registry.json,
extend TOKEN_MAP below.  The registry cross-check enforces that every
target value already exists as a registry option — it does NOT enforce
that every enum field has a TOKEN_MAP entry, because a growing number of
fields arrive in the deal.yaml already-canonical (e.g. ``B1_dso``,
``A11_cultivation_type``).  Audit via :func:`audit_enum_coverage`.
"""

from __future__ import annotations

from typing import Any, Dict, Hashable, List, Optional, Tuple


class EnumNormaliserError(ValueError):
    """Raised when a value cannot be normalised (no match in registry enum)."""


# ---------------------------------------------------------------------------
# Static token map
# ---------------------------------------------------------------------------
#
# Keys are registry field IDs (the internal keys used in registry['sections']
# [sec]['fields'], NOT the display IDs like "A.6").  Each inner dict maps a
# parser token (or a value already in canonical form, for idempotence) to a
# registry enum string.

TOKEN_MAP: Dict[str, Dict[Hashable, str]] = {
    "A6_signing_authority": {
        # KvK parser bare tokens
        "Sole": "Sole / Zelfstandig bevoegd",
        "Joint": "Joint / Gezamenlijk bevoegd",
        # NL-only variants (e.g. manual deal.yaml authoring)
        "Zelfstandig bevoegd": "Sole / Zelfstandig bevoegd",
        "Gezamenlijk bevoegd": "Joint / Gezamenlijk bevoegd",
        # Canonical passthrough
        "Sole / Zelfstandig bevoegd": "Sole / Zelfstandig bevoegd",
        "Joint / Gezamenlijk bevoegd": "Joint / Gezamenlijk bevoegd",
    },
    "D2_title_type": {
        # Kadaster parser bare tokens
        "Eigendom": "Full ownership / Vol eigendom",
        "Full ownership": "Full ownership / Vol eigendom",
        "Vol eigendom": "Full ownership / Vol eigendom",
        "Erfpacht": "Erfpacht / Leasehold",
        "Leasehold": "Erfpacht / Leasehold",
        # "Recht van opstal" is not a first-class registry enum — maps to
        # "Other / Anders" with the understanding that SAL review should
        # confirm the appropriate opstal treatment manually.
        "Recht van opstal": "Other / Anders",
        "Opstalrecht": "Other / Anders",
        # Canonical passthrough
        "Full ownership / Vol eigendom": "Full ownership / Vol eigendom",
        "Erfpacht / Leasehold": "Erfpacht / Leasehold",
        "Other / Anders": "Other / Anders",
    },
    "D3_encumbrances": {
        # Kadaster parser boolean — v1 simplification: True → Mortgage.
        # (The Kadaster parser currently treats any hypotheek/beslag/
        # kwalitatieve verplichting marker as True; "Mortgage" is the most
        # common downstream label — SAL review verifies.)
        True: "Mortgage / Hypotheek",
        False: "None / Geen",
        # Token variants
        "Mortgage": "Mortgage / Hypotheek",
        "Hypotheek": "Mortgage / Hypotheek",
        "None": "None / Geen",
        "Geen": "None / Geen",
        "Other": "Other / Anders",
        "Anders": "Other / Anders",
        # Canonical passthrough
        "None / Geen": "None / Geen",
        "Mortgage / Hypotheek": "Mortgage / Hypotheek",
        "Other / Anders": "Other / Anders",
    },
}


# ---------------------------------------------------------------------------
# Registry helpers
# ---------------------------------------------------------------------------

def _registry_field(registry: dict, field_id: str) -> Optional[dict]:
    """Locate a field spec by registry field key (e.g. ``A6_signing_authority``)."""
    for sec in registry.get("sections", {}).values():
        if not isinstance(sec, dict):
            continue
        fields = sec.get("fields") or {}
        if field_id in fields:
            return fields[field_id]
    return None


def _registry_options(registry: dict, field_id: str) -> Optional[List[str]]:
    spec = _registry_field(registry, field_id)
    if not spec:
        return None
    if spec.get("type") not in ("select", "multi_select"):
        return None
    return spec.get("options") or []


# ---------------------------------------------------------------------------
# Registry cross-check (runs lazily on first normalise call with a registry)
# ---------------------------------------------------------------------------

def _validate_token_map_against_registry(registry: dict) -> None:
    """Verify every TOKEN_MAP target value exists in the registry's
    ``options`` array for that field.  Raises ``EnumNormaliserError`` on
    any drift — the normaliser is worthless if its targets don't match
    the registry.
    """
    errors: List[str] = []
    for field_id, mapping in TOKEN_MAP.items():
        opts = _registry_options(registry, field_id)
        if opts is None:
            errors.append(
                f"{field_id}: TOKEN_MAP entry present but registry has "
                f"no enum options (field missing or not select/multi_select)"
            )
            continue
        for source_token, target in mapping.items():
            if target not in opts:
                errors.append(
                    f"{field_id}: TOKEN_MAP target {target!r} "
                    f"(from token {source_token!r}) not in registry "
                    f"options {opts!r}"
                )
    if errors:
        raise EnumNormaliserError(
            "TOKEN_MAP drifted from registry:\n  - "
            + "\n  - ".join(errors)
        )


# ---------------------------------------------------------------------------
# Core API
# ---------------------------------------------------------------------------

def normalise_field(
    field_id: str,
    value: Any,
    registry: dict,
) -> Optional[str]:
    """Normalise a raw parser token to a registry-valid enum value.

    - Returns ``None`` if the field has no enum options in the registry
      (i.e. type is not ``select``/``multi_select``) — caller should
      treat the original value as-is.
    - Returns the canonical slash-combined string if the token is in
      TOKEN_MAP **or** already equal to a registry option (idempotent).
    - Raises :class:`EnumNormaliserError` if the field has enum options
      but the value cannot be mapped.

    The registry argument exists so the cross-check can fire once per
    process without requiring a global registry import.
    """
    # Lazy one-shot validation per registry identity.
    _ensure_validated(registry)

    opts = _registry_options(registry, field_id)
    if opts is None:
        # Field isn't an enum — normalisation is a no-op.
        return None

    mapping = TOKEN_MAP.get(field_id, {})

    # Try exact key (handles bool True/False + strings).
    if value in mapping:
        return mapping[value]

    # Strings: case-insensitive / trimmed retry.
    if isinstance(value, str):
        stripped = value.strip()
        if stripped in mapping:
            return mapping[stripped]
        # Idempotence: value already matches a canonical option verbatim.
        if stripped in opts:
            return stripped
        # Case-insensitive last-chance match against canonical options.
        lc = stripped.lower()
        for opt in opts:
            if opt.lower() == lc:
                return opt
        # Case-insensitive match against map keys
        for k, v in mapping.items():
            if isinstance(k, str) and k.lower() == lc:
                return v

    raise EnumNormaliserError(
        f"cannot normalise {field_id}={value!r}: not in TOKEN_MAP "
        f"and not a registry canonical option. Registry options: {opts!r}"
    )


def normalise_parse_result(
    parse_result: dict,
    registry: dict,
) -> dict:
    """Normalise every field in a parser's ``fields_populated`` dict.

    Non-enum fields pass through unchanged.  Enum fields are normalised
    to the registry canonical value.  Returns a **new** dict — does not
    mutate the input.
    """
    out: Dict[str, Any] = {}
    for field_id, value in (parse_result or {}).items():
        normalised = _try_normalise(field_id, value, registry)
        out[field_id] = normalised if normalised is not None else value
    return out


def normalise_deal_yaml(deal: dict, registry: dict) -> dict:
    """Walk a deal.yaml structure and normalise every field that maps to a
    registry enum.

    Targets two known places where enum tokens land in deal.yaml:

    - ``deal['site_partners'][*]['signatory']['signing_authority']``
      (A6 equivalent — populated from KvK enrichment)
    - ``deal['site_partners'][*]['contributions'][*]['details']['title_type']``
      (D2 equivalent — populated from Kadaster enrichment)
    - ``deal['site_partners'][*]['contributions'][*]['details']['encumbrances']``
      (D3 equivalent — populated from Kadaster enrichment, bool)

    Mutates ``deal`` in place and returns it for chaining.
    """
    _ensure_validated(registry)

    for partner in deal.get("site_partners") or []:
        sig = partner.get("signatory") or {}
        if "signing_authority" in sig:
            try:
                new = normalise_field(
                    "A6_signing_authority", sig["signing_authority"], registry
                )
                if new is not None:
                    sig["signing_authority"] = new
            except EnumNormaliserError:
                # Leave unchanged — caller can validate separately.
                pass
        for contrib in partner.get("contributions") or []:
            details = contrib.get("details") or {}
            if "title_type" in details:
                try:
                    new = normalise_field(
                        "D2_title_type", details["title_type"], registry
                    )
                    if new is not None:
                        details["title_type"] = new
                except EnumNormaliserError:
                    pass
            if "encumbrances" in details:
                try:
                    new = normalise_field(
                        "D3_encumbrances", details["encumbrances"], registry
                    )
                    if new is not None:
                        details["encumbrances"] = new
                except EnumNormaliserError:
                    pass
    return deal


# ---------------------------------------------------------------------------
# Audit helper
# ---------------------------------------------------------------------------

def audit_enum_coverage(registry: dict) -> Dict[str, List[str]]:
    """Return a report of enum-field coverage.

    Keys:
    - ``mapped``     : enum fields with a TOKEN_MAP entry.
    - ``passthrough``: enum fields with **no** TOKEN_MAP entry (caller is
      assumed to supply canonical values; any non-canonical value will
      raise at normalisation time).

    Use for audit output during HoT engine startup.
    """
    mapped: List[str] = []
    passthrough: List[str] = []
    for sec in registry.get("sections", {}).values():
        if not isinstance(sec, dict):
            continue
        for fid, spec in (sec.get("fields") or {}).items():
            if spec.get("type") not in ("select", "multi_select"):
                continue
            if fid in TOKEN_MAP:
                mapped.append(fid)
            else:
                passthrough.append(fid)
    return {"mapped": mapped, "passthrough": passthrough}


# ---------------------------------------------------------------------------
# Internal — one-shot validation per registry object
# ---------------------------------------------------------------------------

#: Cache of id() → bool.  Registry dicts are typically loaded once; re-
#: validation is harmless but wasteful.  We key by ``id()`` so fresh
#: registries (including tampered ones in tests) re-validate.
_VALIDATED: Dict[int, bool] = {}


def _ensure_validated(registry: dict) -> None:
    key = id(registry)
    if _VALIDATED.get(key):
        return
    _validate_token_map_against_registry(registry)
    _VALIDATED[key] = True


def _try_normalise(field_id: str, value: Any, registry: dict) -> Optional[str]:
    """normalise_field wrapper that returns ``None`` for non-enum fields
    without raising for unknown tokens.  Used by ``normalise_parse_result``
    which must not blow up on non-enum passthrough values."""
    opts = _registry_options(registry, field_id)
    if opts is None:
        return None
    return normalise_field(field_id, value, registry)
