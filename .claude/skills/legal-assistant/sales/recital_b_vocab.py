"""Recital B controlled vocabulary — v3.8.0.

Source of truth for the 5-slot Recital B template. Closed enums and
banned-phrase regexes live here so they can be unit-tested directly and
reused across `generate_loi.py::recitals()`, `qa_lint()`, and the slot
interrogation flow surfaced in `SKILL.md::Phase 5`.

Slot template:
    1. legal_identity      — legal_form + jurisdiction + registration
    2. operational_verb    — verb + object
    3. customer_use_case   — category
    4. material_asset      — asset (single string; multi-location prose ok)
    5. bargain_relevant_fact — claim + named_entities[] + proof  (OPTIONAL)

References (see _shared/recital-b-reference.md):
- Adams, A Manual of Style for Contract Drafting (3rd ed.), Ch. 4
  ("Recitals state facts, not opinions, and reference is to be made only
   to facts material to the agreement.")
- ABA, Negotiated Acquisitions of Companies, Subsidiaries and Divisions,
  Ch. 6 — representation/recital alignment.
- Practical Law (Thomson Reuters): Recitals — template + commentary.
- Mellinkoff, Dictionary of American Legal Usage — verb register.
"""
from __future__ import annotations

import re
from typing import Iterable
from urllib.parse import urlparse


# -----------------------------------------------------------------------------
# Closed enums
# -----------------------------------------------------------------------------

# Legal-form vocabulary. Designed for DE's actual jurisdictional spread
# (NL/UK/US dominant; DE/HR occasional). New jurisdictions add entries
# here OR fall through to the freeform-with-warn path in
# `_validate_legal_form()`.
LEGAL_FORM_ENUM: dict[str, set[str]] = {
    # jurisdiction → set of accepted legal-form short tokens
    "Netherlands":      {"B.V.", "N.V.", "C.V.", "Stichting", "Coöperatie"},
    "United Kingdom":   {"Ltd", "Limited", "PLC", "LLP"},
    "England and Wales": {"Ltd", "Limited", "PLC", "LLP"},
    "United States":    {"LLC", "Inc", "Corp", "L.P.", "LLP"},
    "Delaware":         {"LLC", "Inc", "Corp", "L.P."},
    "Germany":          {"GmbH", "AG", "GmbH & Co. KG", "UG", "e.V."},
    "Croatia":          {"d.o.o.", "d.d.", "j.d.o.o."},
    "France":           {"SAS", "SARL", "SA", "SCI"},
    "Spain":            {"S.A.", "S.L.", "S.L.U."},
    "Switzerland":      {"AG", "GmbH", "SA"},
    "Ireland":          {"Ltd", "Limited", "DAC", "PLC"},
    "Luxembourg":       {"S.A.", "S.à r.l.", "SCS", "SCSp"},
}

# Operational-verb vocabulary — closed list. The intent: an active,
# present-tense verb describing what the entity does *operationally*.
# No marketing verbs (pioneering / disrupting / leading / revolutionising).
OPERATIONAL_VERB_ENUM: frozenset[str] = frozenset({
    "providing",
    "manufacturing",
    "developing",
    "operating",
    "distributing",
    "consulting",
    "licensing",
    "designing",
    "delivering",
    "supplying",
    "engineering",
    "constructing",
    "building",
    "researching",
    "publishing",      # for media / research orgs
    "advising",        # for advisory entities
    "integrating",     # for SI vendors
    "owning",          # for asset-holding cos
    "leasing",         # for asset-leasing cos
})


# -----------------------------------------------------------------------------
# Banned-phrase regex (the "marketing wrapper" blocklist — Layer 1)
# -----------------------------------------------------------------------------

# Each pattern targets a class of FRAMING (marketing wrapper). Named
# entities themselves are NOT banned — see Layer 2 (`named_entities` proof
# block in slot 5). Layer 1 catches the freeform-prose marketing pattern
# regardless of whether names are attached.
BANNED_PHRASES: dict[str, re.Pattern] = {
    "marketing_puffery": re.compile(
        r"\b(leading|world-class|innovative|industry-defining|cutting-edge|"
        r"next-generation|frontier|pioneering|disruptive|revolutionary|"
        r"game-changing)\b",
        re.IGNORECASE,
    ),
    "adjective_stacks": re.compile(
        r"\b(dynamic|fast-growing|AI-native|AI-powered|AI-first|"
        r"cloud-native|next-gen)\b",
        re.IGNORECASE,
    ),
    "press_release_voice": re.compile(
        # Verbs commonly used to wrap counterparty claims as marketing.
        # `powering` is allowed only when followed by "by" (factual:
        # "powered by 100MW grid connection").
        r"\b(reshaping|driving|unlocking|empowering|transforming|"
        r"revolutionis\w*|revolutioniz\w*|"
        r"powering(?!\s+by\b))\b",
        re.IGNORECASE,
    ),
    "pump_frame_phrases": re.compile(
        # STACKS of investor names without sourcing ("backed by Sequoia,
        # a16z, and NVentures"). Catches the comma-and pattern of three
        # or more proper-noun tokens preceded by a pump verb.
        r"\b(?:backed by|investors include|funded by\s+tier-?\s*\d\s+VCs?|"
        r"funded by\s+top-tier)\b",
        re.IGNORECASE,
    ),
    "future_tense_ambition": re.compile(
        r"\b(plans to|will\s+\w+\s+(?:deploy|operate|expand)|targeting|"
        r"aiming to|on track to|scaling to)\b",
        re.IGNORECASE,
    ),
    "aspirational_scale": re.compile(
        # Banned when used freeform; legitimate locations should be in
        # slot 4 with named places, not vague "globally / worldwide".
        r"\b(?:across (?:multiple|many) (?:regions|markets)|globally|worldwide)\b",
        re.IGNORECASE,
    ),
    "quoted_valuations_wo_filing": re.compile(
        r"\$\d+[\d,.]*\s*(M|B|bn|million|billion)\s+valuation",
        re.IGNORECASE,
    ),
    "vendor_adjectives": re.compile(
        r"\b(vertically integrated|end-to-end|full-stack|turnkey)\b",
        re.IGNORECASE,
    ),
    "founder_biography": re.compile(
        r"\b(founded by|co-founder of|"
        r"ex-(?:DeepMind|Google|Meta|OpenAI|Anthropic|McKinsey|Goldman))\b",
        re.IGNORECASE,
    ),
}


# -----------------------------------------------------------------------------
# Source-tier heuristic (URL-host based)
# -----------------------------------------------------------------------------

# Tier-1: government registries, regulator filings, primary press releases
# from the entity itself, court filings.
_TIER_1_HOSTS = {
    "sec.gov", "sec.report", "ec.europa.eu", "europa.eu",
    "kvk.nl", "find-and-update.company-information.service.gov.uk",
    "handelsregister.de", "online-handelsregister.de",
    "sudreg.pravosudje.hr", "rechtspraak.nl",
    "cnmv.es", "amf-france.org", "consob.it",
}
_TIER_1_PATH_HINTS = {"/press/", "/news/", "/newsroom/", "/investors/",
                      "/source/", "/announcement/", "/announcements/"}
_TIER_1_SUBDOMAIN_PREFIXES = {"news.", "press.", "newsroom.", "investors.",
                              "ir.", "media."}

# Tier-2: named-journalist outlets, named-analyst reports.
_TIER_2_HOSTS = {
    "reuters.com", "ft.com", "bloomberg.com", "wsj.com", "economist.com",
    "nytimes.com", "techcrunch.com",
    "gartner.com", "forrester.com", "idc.com",
    "datacenterdynamics.com", "globenewswire.com", "prnewswire.com",
    "businesswire.com",
    "spiegel.de", "handelsblatt.com",
}


def _normalize_host(url: str) -> str:
    """Return the bare host (no www., no port) for a URL."""
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        return ""
    if host.startswith("www."):
        host = host[4:]
    if ":" in host:
        host = host.split(":")[0]
    return host


def url_tier(url: str) -> int:
    """Infer source tier from URL host. Returns 1, 2, or 3."""
    host = _normalize_host(url)
    if not host:
        return 3
    # Exact host or any subdomain of a tier host
    for t1 in _TIER_1_HOSTS:
        if host == t1 or host.endswith("." + t1):
            return 1
    # Subdomain prefix indicates primary press / IR / newsroom on
    # counterparty's own domain (e.g., news.microsoft.com / press.tesla.com).
    for prefix in _TIER_1_SUBDOMAIN_PREFIXES:
        if host.startswith(prefix):
            return 1
    for t2 in _TIER_2_HOSTS:
        if host == t2 or host.endswith("." + t2):
            return 2
    # Path-hint check for primary press on counterparty's own domain
    # (can't pre-enumerate hosts; the path tells us)
    try:
        path = urlparse(url).path or ""
    except Exception:
        path = ""
    for hint in _TIER_1_PATH_HINTS:
        if hint in path:
            return 1
    return 3


# -----------------------------------------------------------------------------
# Validation primitives
# -----------------------------------------------------------------------------

def find_banned_phrases(text: str) -> list[tuple[str, str]]:
    """Return list of (class, matched_substring) for each banned phrase
    found in `text`. Empty list = clean.
    """
    if not isinstance(text, str) or not text:
        return []
    findings: list[tuple[str, str]] = []
    for cls, pat in BANNED_PHRASES.items():
        for m in pat.finditer(text):
            findings.append((cls, m.group(0)))
    return findings


def validate_legal_form(legal_form: str, jurisdiction: str) -> tuple[bool, str]:
    """Cross-check legal_form against jurisdiction's accepted enum.

    Returns (ok, message). ok=True means accepted; message empty on ok,
    or contains a warn/fail explanation otherwise.

    - Known jurisdiction with form in enum → ok.
    - Known jurisdiction with form NOT in enum → not ok (R-32 fail).
    - Unknown jurisdiction → ok with warn message ("R-form-unknown").
    """
    if not legal_form or not jurisdiction:
        return False, "legal_form and jurisdiction both required"
    accepted = LEGAL_FORM_ENUM.get(jurisdiction)
    if accepted is None:
        return True, (
            f"R-form-unknown: jurisdiction {jurisdiction!r} not in "
            f"LEGAL_FORM_ENUM; legal_form {legal_form!r} accepted as "
            f"freeform. Add to vocab if recurring."
        )
    if legal_form in accepted:
        return True, ""
    return False, (
        f"legal_form {legal_form!r} not accepted for jurisdiction "
        f"{jurisdiction!r}. Accepted: {sorted(accepted)}"
    )


def validate_operational_verb(verb: str) -> tuple[bool, str]:
    """Check operational_verb.verb is in the closed enum."""
    if not verb:
        return False, "operational_verb.verb required"
    if verb in OPERATIONAL_VERB_ENUM:
        return True, ""
    return False, (
        f"operational_verb.verb {verb!r} not in OPERATIONAL_VERB_ENUM. "
        f"Accepted: {sorted(OPERATIONAL_VERB_ENUM)}"
    )


# -----------------------------------------------------------------------------
# Named-entity detection in slot-5 claim text
# -----------------------------------------------------------------------------

# Regex finding capitalised proper-noun tokens that look like company /
# person names. Excludes leading-of-sentence capitalisation by requiring
# a non-sentence-start position, and excludes a small allowlist of
# geographic / generic terms.
_PROPER_NOUN_PATTERN = re.compile(
    r"(?<![A-Za-z])"                # not preceded by another letter
    r"([A-Z][A-Za-z0-9]+"           # first capitalised token
    r"(?:\s+[A-Z][A-Za-z0-9]+)*"    # additional capitalised tokens
    r")"
)

_GEOGRAPHIC_ALLOWLIST = frozenset({
    # Countries, regions, capital cities; safe to mention without being
    # treated as named-entity references.
    "Netherlands", "Germany", "France", "Spain", "Italy", "United States",
    "United Kingdom", "Croatia", "Poland", "Switzerland", "Ireland",
    "Luxembourg", "Belgium", "Austria", "Sweden", "Norway", "Denmark",
    "Finland", "Portugal", "Czech Republic", "Slovakia", "Slovenia",
    "Hungary", "Greece", "Romania", "Bulgaria", "Estonia", "Latvia",
    "Lithuania", "Iceland",
    "Amsterdam", "London", "Berlin", "Paris", "Madrid", "Rome", "Zagreb",
    "Vienna", "Brussels", "Helsinki", "Stockholm", "Copenhagen", "Oslo",
    "Dublin", "Frankfurt", "Munich", "Hamburg", "Zurich", "Geneva",
    "Luxembourg City", "Lisbon", "Prague", "Budapest", "Warsaw",
    "Cluj", "Houston", "Dallas", "San Francisco", "Seattle", "New York",
    "EU", "NATO",
    # Generic operating-context words that capitalize but aren't entities
    "MW", "GW", "MWh", "GWh", "TWh",
    "Wholesale", "Distributor", "EndUser", "StrategicSupplier", "EcosystemPartnership",
    "Customer", "Supplier", "Partner", "Provider", "Counterparty",
    "AI", "GPU", "CPU", "DEC", "MSA", "LOI", "NDA", "RFS", "SoW",
    "Mode A", "Mode B",
    # Calendar tokens
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December",
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
})


def find_named_entities_in_text(text: str) -> list[str]:
    """Return list of capitalised proper-noun tokens that look like
    named entities (companies / people), excluding the geographic /
    generic allowlist.

    Used by R-32 to verify slot-5 `claim` text whose named entities are
    documented in `bargain_relevant_fact.named_entities[]` proof block.
    """
    if not isinstance(text, str) or not text:
        return []
    candidates: list[str] = []
    for m in _PROPER_NOUN_PATTERN.finditer(text):
        token = m.group(1)
        if token in _GEOGRAPHIC_ALLOWLIST:
            continue
        # Skip single-token capitalisation that's likely a sentence start
        # (heuristic: short single tokens preceding a noun-phrase that
        # doesn't carry brand weight — e.g., "The" at sentence start).
        if " " not in token and len(token) <= 3:
            continue
        candidates.append(token)
    return candidates


# -----------------------------------------------------------------------------
# Sentence-rendering helper
# -----------------------------------------------------------------------------

def render_recital_b_sentence(slots: dict, party_label: str, short_name: str) -> str:
    """Render the Recital B sentence from the validated slot block.

    Deterministic concatenation. No prose generation. Caller must have
    already run `validate_recital_b_slots()` against this block.

    Output shape (4-slot or 5-slot):
        "(B) {short} (the "{party_label}") is a {legal_form} organised
        under the laws of {jurisdiction} (registered with the {reg_type}
        under number {reg_number}), engaged in {verb} {object} for
        {category}, from its {asset}{, {bargain_fact_claim}}."
    """
    li = slots["legal_identity"]
    ov = slots["operational_verb"]
    cu = slots["customer_use_case"]
    ma = slots["material_asset"]
    fact = slots.get("bargain_relevant_fact") or None

    # Slot 1 — legal identity
    legal_form = li["legal_form"]
    jurisdiction = li["jurisdiction"]
    reg = li.get("registration") or {}
    reg_type = reg.get("type")
    reg_number = reg.get("number")

    # Use article that matches the legal form's leading character.
    article = "an" if legal_form and legal_form[0].lower() in "aeiou" else "a"
    if reg_type and reg_number:
        identity_clause = (
            f"{article} {legal_form} organised under the laws of "
            f"{jurisdiction} (registered with the {reg_type} under "
            f"number {reg_number})"
        )
    else:
        identity_clause = (
            f"{article} {legal_form} organised under the laws of "
            f"{jurisdiction}"
        )

    # Slots 2 + 3 + 4
    activity_clause = f"engaged in {ov['verb']} {ov['object']} for {cu['category']}"
    location_clause = f"from its {ma['asset']}"

    sentence = (
        f'(B) {short_name} (the "{party_label}") is {identity_clause}, '
        f"{activity_clause}, {location_clause}"
    )

    if fact and fact.get("claim"):
        claim = fact["claim"].rstrip().rstrip(".")
        sentence += f", {claim}"

    sentence += "."
    return sentence


# -----------------------------------------------------------------------------
# Public surface
# -----------------------------------------------------------------------------

__all__ = [
    "LEGAL_FORM_ENUM",
    "OPERATIONAL_VERB_ENUM",
    "BANNED_PHRASES",
    "url_tier",
    "find_banned_phrases",
    "validate_legal_form",
    "validate_operational_verb",
    "find_named_entities_in_text",
    "render_recital_b_sentence",
]
