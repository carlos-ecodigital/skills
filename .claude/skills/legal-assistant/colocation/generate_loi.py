#!/usr/bin/env python3
"""
LOI/NCNDA v3.2 — Document Generation Script

Usage:
    python generate_loi.py intake.yaml [--output path/to/output.docx]
                                        [--override R-11,R-14]
                                        [--override-reason "..."]

Takes a YAML intake file and produces a complete, branded .docx ready to sign.
All clauses, conditionals, and schedules are generated from the intake data.

v3.2 changes (2026-04-16):
- Recital A is library-sourced (see _shared/loi-recital-a-library.md). Variants:
  default | sovereignty | integration | bespoke.
- Customer-facing "DEC Block" language removed. Capacity expressed in MW IT +
  Designated Sites. Deprecated YAML field: commercial.dec_block_count.
- "Minimum commitment term of 5 years" replaced with "approximately 5 years,
  indicative only".
- Cl. 4.2 "Revenue Chain" with Unicode arrows replaced with "Contractual
  Sequence" prose + numbered list.
- Closing line: hardcoded single-sentence "We look forward to working with you."
  Honors OPEN-1 (commit 2097f52) — bespoke_closing is not supported.
  choices.bespoke_closing in YAML is silently ignored for backward compat.
- Schedule 1 title no longer carries "(NON-BINDING)" suffix. Italic prefatory
  note on the schedule; authoritative binding/non-binding assignment in Cl. 5.1.
- Pre-save QA linter. Rules in _shared/loi-qa-gate.md. Severity: fail / warn /
  info. Overridable via --override / --override-reason.

Planned (not yet wired in this file): new types StrategicSupplier (DE-LOI-SS-v1.0)
and EcosystemPartnership (DE-LOI-EP-v1.0). See CHANGELOG.md.
"""

import sys
import os
import yaml
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.shared import Pt, Cm, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT

# Import shared cover page and branding from document-factory
# Script now lives under legal-assistant/colocation/, one level deeper than the
# original loi-generator/ layout, so resolve document-factory via parent.parent.
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR.parent.parent / "document-factory"))
from generate import (  # noqa: E402
    add_cover, Party,
    COBALT, SLATE, SLATE_800, SLATE_900, WHITE,
    setup_first_page_header, setup_cont_header,
    setup_first_footer, setup_cont_footer,
)


# ---------------------------------------------------------------------------
# Configuration -- LOI clause formatting (body text, not cover page)
# ---------------------------------------------------------------------------

FONT_NAME = "Inter"
FONT_BODY = Pt(10)
FONT_HEADING1 = Pt(13)
FONT_HEADING2 = Pt(11)
FONT_SMALL = Pt(8)
LINE_SPACING = 1.15

# Local aliases for clause body text (imported colors used for cover page)
NAVY = SLATE_900
BLACK = SLATE_800
GREY = SLATE


# ---------------------------------------------------------------------------
# YAML Loading + Validation
# ---------------------------------------------------------------------------

def load_intake(path: str) -> dict:
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    validate(data)
    return data


def validate(d: dict):
    """Validate intake YAML. Raises SystemExit on failure.

    v3.2: rule R-18 (fail) — deprecated field commercial.dec_block_count.
    """
    errors = []
    t = d.get("type", "")
    if t not in ("EndUser", "Distributor", "Wholesale",
                  "StrategicSupplier", "EcosystemPartnership"):
        errors.append(
            "type must be one of: EndUser, Distributor, Wholesale, "
            f"StrategicSupplier, EcosystemPartnership (got: {d.get('type')})"
        )
    for s in ("provider", "counterparty", "programme", "dates"):
        if s not in d:
            errors.append(f"Missing section: {s}")
    cp = d.get("counterparty", {})
    for f in ("name", "short", "description"):
        if not cp.get(f):
            errors.append(f"counterparty.{f} required")
    if not d.get("dates", {}).get("loi_date"):
        errors.append("dates.loi_date required")

    # R-18 — deprecated field migration error
    if "dec_block_count" in d.get("commercial", {}):
        errors.append(
            "[R-18] commercial.dec_block_count is deprecated in v3.2. "
            "Use commercial.indicative_mw instead. See CHANGELOG.md § Migration."
        )

    if t == "Distributor" and d.get("partnership_mode", "combined") == "combined":
        for f in ("partner_core_capability", "partner_contribution",
                   "combined_offering", "target_end_users", "partner_service_scope"):
            if not d.get("commercial", {}).get(f):
                errors.append(f"commercial.{f} required for Distributor Mode A")
    if t == "Wholesale":
        if not d.get("commercial", {}).get("indicative_mw"):
            errors.append("commercial.indicative_mw required for Wholesale (MW IT)")
    if t == "EndUser":
        if not d.get("commercial", {}).get("service_type"):
            errors.append("commercial.service_type required for EndUser")
    if t == "StrategicSupplier":
        supplier = d.get("supplier", {})
        if not supplier.get("capability_category"):
            errors.append("supplier.capability_category required for StrategicSupplier")
        if not supplier.get("core_capability"):
            errors.append("supplier.core_capability required for StrategicSupplier")
        purposes = supplier.get("strategic_purposes", [])
        if not purposes or not (1 <= len(purposes) <= 2):
            errors.append("supplier.strategic_purposes required for StrategicSupplier (1-2 items)")
        valid_purposes = {"capacity_lock_in", "pricing_volume",
                           "supply_chain_de_risking", "engineering_integration",
                           "pipeline_visibility"}
        for p in purposes:
            if p not in valid_purposes:
                errors.append(
                    f"supplier.strategic_purposes: invalid '{p}'. "
                    f"Valid: {sorted(valid_purposes)}"
                )
        if "capacity_lock_in" in purposes and not supplier.get("lead_time_target"):
            errors.append(
                "supplier.lead_time_target required when strategic_purposes "
                "includes capacity_lock_in"
            )
        if "pricing_volume" in purposes and not supplier.get("volume_indicative"):
            errors.append(
                "supplier.volume_indicative required when strategic_purposes "
                "includes pricing_volume"
            )
        if ("engineering_integration" in purposes
                and not d.get("choices", {}).get("joint_ip")):
            errors.append(
                "choices.joint_ip required when strategic_purposes "
                "includes engineering_integration (none | background | foreground)"
            )
    if t == "EcosystemPartnership":
        eco = d.get("ecosystem", {})
        if not eco.get("relationship_type"):
            errors.append("ecosystem.relationship_type required for EcosystemPartnership")
        valid_rel = {"standards_body", "university", "research_consortium",
                      "co_marketing", "industry_association", "policy_partner",
                      "other"}
        if eco.get("relationship_type") and eco.get("relationship_type") not in valid_rel:
            errors.append(
                f"ecosystem.relationship_type must be one of {sorted(valid_rel)}"
            )
        if not eco.get("collaboration_themes"):
            errors.append("ecosystem.collaboration_themes required for EcosystemPartnership")
        if not eco.get("joint_activity_categories"):
            errors.append("ecosystem.joint_activity_categories required for EcosystemPartnership")

    # Recital A variant validation
    variant = d.get("programme", {}).get("recital_a_variant", "default")
    if variant not in ("default", "sovereignty", "integration", "bespoke"):
        errors.append(
            f"programme.recital_a_variant must be one of: default, sovereignty, "
            f"integration, bespoke (got: {variant})"
        )
    if variant == "bespoke" and not d.get("programme", {}).get("recital_a_bespoke"):
        errors.append(
            "programme.recital_a_bespoke required when recital_a_variant=bespoke"
        )

    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Recital A variant library (v3.2)
# ---------------------------------------------------------------------------
# Source of truth is _shared/loi-recital-a-library.md. The variants below are
# copied in sync with that file. If the library file is updated, update these.
# Drift guard: QA linter warns if the variant strings diverge from the library.

RECITAL_A_VARIANTS = {
    "default": (
        '{prov} (the "Provider") develops and operates Digital Energy Centers '
        '("DECs"): purpose-built, liquid-cooled colocation facilities that '
        "integrate accelerated compute with on-site energy recycling, thermal "
        "recovery, and grid-flexible operation. The Provider is building an "
        "integrated sovereign AI infrastructure platform across European markets, "
        "structured for institutional project financing and designed to deliver "
        "compute capacity alongside heat and grid value from a single energy input."
    ),
    "sovereignty": (
        '{prov} (the "Provider") develops and operates Digital Energy Centers '
        '("DECs"): purpose-built, liquid-cooled colocation facilities for '
        "high-density accelerated compute workloads. The Provider operates a "
        "sovereign AI infrastructure platform on European soil, controlled by "
        "European operators, designed to serve European enterprises, institutions, "
        "and public-sector customers with compliance-grade data residency and "
        "independent supply-chain control. DECs integrate AI compute with energy "
        "recycling and grid-flexible operation, and the platform is structured "
        "for institutional project financing."
    ),
    "integration": (
        '{prov} (the "Provider") develops and operates Digital Energy Centers '
        '("DECs"): integrated energy infrastructure assets in which electricity '
        "entering a site powers accelerated compute, the resulting heat is "
        "recovered and upgraded for thermal offtake to greenhouses or "
        "district-heating networks, and residual grid and power-system value is "
        "captured through battery storage, flexible generation, and "
        "grid-balancing services. DECs turn energy into digital intelligence "
        "and capture heat, power, and grid value along the way."
    ),
}


def resolve_recital_a(d: dict) -> str:
    """Return the Recital A body (without the '(A) ' prefix).

    Looks up the variant key in RECITAL_A_VARIANTS and formats with provider
    short name. For variant='bespoke', returns the raw bespoke string; the
    QA linter will catch any forbidden patterns.
    """
    prov = d.get("provider", {}).get("short_name", "Digital Energy")
    variant = d.get("programme", {}).get("recital_a_variant", "default")
    if variant == "bespoke":
        bespoke = d.get("programme", {}).get("recital_a_bespoke", "")
        return bespoke or RECITAL_A_VARIANTS["default"].format(prov=prov)
    tmpl = RECITAL_A_VARIANTS.get(variant, RECITAL_A_VARIANTS["default"])
    return tmpl.format(prov=prov)


# ---------------------------------------------------------------------------
# Document Builder
# ---------------------------------------------------------------------------

_AGREEMENT_TYPE_BY_LOI = {
    "Distributor": "Letter of Intent and NCNDA",
    "Wholesale": "Letter of Intent and NCNDA",
    "EndUser": "Letter of Intent",
    "StrategicSupplier": "Letter of Intent and NCNDA",
    "EcosystemPartnership": "Letter of Intent",
}

_SUBJECT_BY_LOI = {
    "Distributor": "Strategic Infrastructure Partnership",
    "Wholesale": "Purpose-Built AI Colocation Capacity",
    "EndUser": "AI Compute Infrastructure Services",
    "StrategicSupplier": "Strategic Supply and Infrastructure Partnership",
    "EcosystemPartnership": "Strategic Ecosystem Collaboration",
}


class LOI:
    def __init__(self, data: dict):
        self.d = data
        self.t = data["type"]
        self.agreement_type = _AGREEMENT_TYPE_BY_LOI[self.t]
        self.subject = _SUBJECT_BY_LOI[self.t]
        self.doc = Document()
        self._setup()
        party_by_type = {
            "Distributor": "Partner",
            "StrategicSupplier": "Partner",
            "EcosystemPartnership": "Partner",
            "Wholesale": "Customer",
            "EndUser": "Customer",
        }
        self.party = party_by_type.get(self.t, "Customer")
        # QA linter accumulators (populated during build)
        self.overrides = set(self.d.get("_overrides", []))
        self.override_reason = self.d.get("_override_reason", "")
        self.qa_findings = []

    def _setup(self):
        style = self.doc.styles["Normal"]
        style.font.name = FONT_NAME
        style.font.size = FONT_BODY
        style.paragraph_format.space_after = Pt(3)
        style.paragraph_format.line_spacing = LINE_SPACING
        for s in self.doc.sections:
            s.page_width = Mm(210)
            s.page_height = Mm(297)
            s.top_margin = Mm(20)
            s.bottom_margin = Mm(35)
            s.left_margin = Mm(25)
            s.right_margin = Mm(20)
            s.different_first_page_header_footer = True

            # Shared header/footer from document-factory
            setup_first_page_header(s)
            setup_cont_header(s, title=self.agreement_type)
            setup_first_footer(s, classification="Confidential")
            setup_cont_footer(s, classification="Confidential")

    # --- Helpers ---

    def g(self, *keys, default=""):
        v = self.d
        for k in keys:
            v = v.get(k, default) if isinstance(v, dict) else default
        return v or default

    def choice(self, k):
        return bool(self.g("choices", k))

    def p(self, text, bold=False, italic=False, size=None, color=None, align=None, space_after=None):
        para = self.doc.add_paragraph()
        if align:
            para.alignment = align
        if space_after is not None:
            para.paragraph_format.space_after = Pt(space_after)
        run = para.add_run(text)
        run.font.name = FONT_NAME
        run.font.size = size or FONT_BODY
        run.bold = bold
        run.italic = italic
        if color:
            run.font.color.rgb = color
        return para

    def bp(self, label, text):
        """Bold label + normal text in one paragraph."""
        para = self.doc.add_paragraph()
        r1 = para.add_run(label)
        r1.bold = True
        r1.font.name = FONT_NAME
        r1.font.size = FONT_BODY
        r2 = para.add_run(text)
        r2.font.name = FONT_NAME
        r2.font.size = FONT_BODY
        return para

    def h(self, text, level=2):
        heading = self.doc.add_heading(text, level=level)
        for r in heading.runs:
            r.font.name = FONT_NAME
            r.font.color.rgb = NAVY

    def table(self, headers, rows):
        t = self.doc.add_table(rows=1 + len(rows), cols=len(headers))
        t.style = "Light Grid Accent 1"
        for i, h in enumerate(headers):
            cell = t.rows[0].cells[i]
            cell.text = h
            for p in cell.paragraphs:
                for r in p.runs:
                    r.bold = True
                    r.font.name = FONT_NAME
                    r.font.size = FONT_BODY
        for ri, row in enumerate(rows):
            for ci, val in enumerate(row):
                cell = t.rows[ri + 1].cells[ci]
                cell.text = str(val)
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.name = FONT_NAME
                        r.font.size = FONT_BODY
        return t

    def line(self):
        self.p("—" * 50, color=GREY, size=Pt(6), space_after=0)

    # --- Sections ---

    def letterhead(self):
        """Render IB-standard cover page via document-factory's add_cover()."""
        agreement_type = self.agreement_type
        subject = self.subject

        # Build Party objects from YAML data
        prov = self.d.get("provider", {})
        provider_party = Party(
            legal_name=prov.get("legal_name", ""),
            address=prov.get("address", ""),
            registration_type="KvK" if prov.get("kvk") else None,
            registration_number=prov.get("kvk"),
            parent=prov.get("parent"),
        )

        cp = self.d.get("counterparty", {})
        counterparty = Party(
            legal_name=cp.get("name", ""),
            address=cp.get("address", ""),
            registration_type=cp.get("reg_type"),
            registration_number=cp.get("reg_number"),
        )

        # Delegate to document-factory's shared cover page
        add_cover(
            self.doc,
            agreement_type=agreement_type,
            subject=subject,
            date_str=self.g("dates", "loi_date"),
            parties=[provider_party, counterparty],
            formality="non_binding",
            classification="Confidential",
        )

    def recitals(self):
        self.h("Recitals")
        cp = self.g("counterparty", "short")
        desc = self.g("counterparty", "description")

        # Recital A — library-sourced variant (v3.2)
        recital_a_body = resolve_recital_a(self.d)

        # Append type-specific strategic-fit tail to Recital A.
        # The library variants cover identity + platform framing; each type
        # adds one sentence that frames the counterparty relationship.
        tail_by_type = {
            "Distributor": (
                f" The Provider seeks qualified channel and integration partners to "
                f"extend its platform reach to end-user segments where the {self.party} "
                f"holds established customer relationships and domain expertise."
            ),
            "StrategicSupplier": (
                f" The Provider seeks qualified supply and engineering partners to "
                f"accelerate the delivery of its DEC platform, integrate complementary "
                f"infrastructure capability, and de-risk the supply chain supporting "
                f"the Provider's active development pipeline."
            ),
            "EcosystemPartnership": (
                f" The Provider participates in ecosystem initiatives that advance "
                f"sovereign AI infrastructure, sustainable datacentre design, and "
                f"European industrial policy alignment."
            ),
            "Wholesale": "",
            "EndUser": "",
        }
        recital_a_body += tail_by_type.get(self.t, "")
        self.p(f"(A) {recital_a_body}")

        self.p(f'(B) {cp} (the "{self.party}") {desc}.')

        if self.t == "Distributor":
            self.p(
                f"(C) The Parties wish to record their mutual interest in establishing a strategic "
                f"partnership under which the {self.party} would collaborate with the Provider to deliver "
                f"AI colocation services to end-user customers, on the indicative terms set out below. "
                f'This letter of intent and non-circumvention non-disclosure agreement (the "LOI") '
                f"reflects both Parties' strategic intent and is intended to form the basis for further "
                f"commercial negotiation toward a definitive partnership agreement or master services "
                f'agreement (the "MSA").'
            )
            self.p(
                "(D) The Parties recognise that the commercial discussions contemplated by this LOI "
                "will require the exchange of commercially sensitive and competitively valuable "
                "information, and wish to establish binding confidentiality and non-circumvention "
                "protections to facilitate those discussions."
            )
        elif self.t == "Wholesale":
            self.p(
                f"(C) The Parties wish to record their mutual interest in the Provider making available, "
                f"and the {self.party} procuring, dedicated AI colocation capacity at the Provider's DEC "
                f"facilities, on the indicative terms set out below. This letter of intent and "
                f'non-circumvention non-disclosure agreement (the "LOI") reflects both Parties\' strategic '
                f"intent to establish a long-term infrastructure partnership and is intended to form the "
                f"basis for further technical scoping and commercial negotiation toward a Master Services "
                f'Agreement (the "MSA").'
            )
            self.p(
                "(D) The Parties recognise that the commercial discussions contemplated by this LOI "
                "will require the exchange of commercially sensitive information, including site-specific "
                "data, pricing models, and infrastructure specifications, and wish to establish binding "
                "confidentiality and non-circumvention protections to facilitate those discussions."
            )
        elif self.t == "StrategicSupplier":
            self.p(
                f"(C) The Parties wish to record their mutual interest in establishing a strategic "
                f"supply partnership under which the {self.party} would contribute to the delivery of "
                f"the Provider's DEC platform, on the indicative terms set out below. This letter of "
                f'intent and non-circumvention non-disclosure agreement (the "LOI") reflects both '
                f"Parties' strategic intent and is intended to form the basis for further technical and "
                f"commercial negotiation toward a Framework Agreement and statements of work for named "
                f"Provider projects."
            )
            self.p(
                "(D) The Parties recognise that the discussions contemplated by this LOI will require "
                "the exchange of commercially sensitive and competitively valuable information, including "
                "site-specific information about Provider projects and Partner design and manufacturing "
                "methodology, and wish to establish binding confidentiality and non-circumvention "
                "protections to facilitate those discussions."
            )
        elif self.t == "EcosystemPartnership":
            themes_list = self.d.get("ecosystem", {}).get("collaboration_themes", [])
            themes_str = ", ".join(themes_list) if themes_list else "[COLLABORATION_THEMES]"
            self.p(
                f"(C) The Parties wish to record their mutual interest in a non-commercial ecosystem "
                f"collaboration focused on {themes_str}, on the framework set out in Clauses 3 through 5. "
                f'This letter of intent (the "LOI") reflects both Parties\' strategic intent to collaborate '
                f"on a non-commercial basis and does not contemplate any payment, capacity purchase, or "
                f"commercial commitment between the Parties."
            )
            self.p(
                "(D) The Parties recognise that the discussions and joint activities contemplated by "
                "this LOI may involve the exchange of commercially sensitive or non-public information "
                "in connection with research, policy, or programme activities, and wish to establish "
                "mutual confidentiality protections to facilitate that collaboration."
            )
        else:
            self.p(
                f"(C) The Parties wish to record their mutual interest in the {self.party} procuring AI "
                f"compute infrastructure services at the Provider's DEC facilities, on the indicative "
                f'terms set out below. This letter of intent (the "LOI") reflects both Parties\' intent '
                f"and is intended to form the basis for further technical scoping and commercial "
                f'negotiation toward a service agreement (the "MSA").'
            )

    def definitions(self):
        self.h("1. Definitions")
        self.p("1.1 In this LOI, unless the context requires otherwise:")

        defs = []
        defs.append(('"Affiliate"', 'means, in relation to a Party, any entity that directly or indirectly controls, is controlled by, or is under common control with that Party, where "control" means the ownership of more than 50% of the voting rights or equivalent ownership interest;'))

        if self.t in ("Distributor", "Wholesale", "StrategicSupplier"):
            ac_text = (
                '"Associated Counterparty" means, in relation to a Site Identifier, any of the following '
                "with whom the Provider has a contractual, commercial, or active non-public engagement "
                "in connection with that site: (a) landowners and land lessors; (b) greenhouse operators "
                "and agricultural partners; (c) heat offtake counterparties; (d) energy procurement "
                "counterparties; (e) engineering, procurement, and construction contractors engaged or "
                "under negotiation; and (f) grid connection holders and distribution system operators "
                "(to the extent of non-public engagement)."
            )
            if self.t == "Distributor":
                ac_text += (
                    " (g) government agencies, municipalities, and regulatory bodies with whom the "
                    "Provider has active non-public engagement (excluding general regulatory contacts "
                    "available to any market participant);"
                )
            else:
                ac_text += (
                    " For the avoidance of doubt, government agencies and regulatory bodies are "
                    "excluded unless the Provider has made a specific named introduction;"
                )
            defs.append(("", ac_text))

        defs.append(('"Business Day"', "means a day other than a Saturday, Sunday, or public holiday in the Netherlands;"))

        if self.t == "Distributor":
            defs.append(('"Competitor"', 'means any entity whose primary business includes the development, ownership, or operation of colocation facilities for high-density compute workloads, or the provision of AI infrastructure services, in the European Economic Area;'))

        ci_text = (
            '"Confidential Information" means all information (whether technical, commercial, financial, '
            "or otherwise) disclosed by a Party to the other in connection with the Purpose, whether in "
            "writing, orally, electronically, or by inspection, including any information that by its "
            "nature or the circumstances of disclosure would reasonably be understood to be confidential"
        )
        if self.t in ("Distributor", "Wholesale", "StrategicSupplier"):
            ci_text += ", and including metadata, EXIF data, digital artifacts, file names, folder names, and any derivative information"
        ci_text += ". The existence and contents of this LOI are Confidential Information;"
        defs.append(("", ci_text))

        defs.append(('"DEC"', "means a Digital Energy Center: a purpose-built colocation facility developed and operated by the Provider;"))
        # v3.2: "DEC Block" removed from customer-facing definitions. Capacity expressed in MW IT + Designated Sites.
        defs.append(('"Designated Site"', "means any DEC or DEC site designated by the Provider for the delivery of capacity to the " + self.party + ", as confirmed in the MSA;"))
        defs.append(('"Financing Party"', "means any bank, financial institution, fund, security trustee, or other entity providing or arranging " + ("debt, mezzanine, or structured " if self.t != "EndUser" else "") + "finance to the Provider or any of its Affiliates in connection with the development or operation of any DEC;"))

        if self.t == "StrategicSupplier":
            defs.append((
                '"Framework Agreement"',
                "means the definitive Framework Agreement and accompanying statements of work to be negotiated between the Parties, setting out the commercial and operational framework for the supply relationship;"
            ))

        if self.t == "Distributor":
            defs.append(('"MSA"', "means the definitive Master Services Agreement or partnership agreement to be negotiated between the Parties;"))
        elif self.t == "Wholesale":
            defs.append(('"MSA"', "means the definitive Master Services Agreement to be negotiated between the Parties, incorporating the Sales Order Form, SLA Schedule, and Pricing Framework;"))
        elif self.t == "EndUser":
            defs.append(('"MSA"', "means the definitive service agreement to be negotiated between the Parties;"))
        # StrategicSupplier uses Framework Agreement (above) — no MSA definition.

        if self.t == "Distributor":
            defs.append(('"Protected Business Information" or "PBI"', "means the Provider's proprietary methodologies, strategies, and frameworks including: (a) site-sourcing and land-acquisition methodology; (b) energy procurement and grid connection strategy; (c) regulatory and permitting playbook; (d) heat offtake and energy recycling commercial model; (e) financial and operational modelling frameworks; (f) DEC design specifications and engineering standards; and (g) colocation pricing methodology and deal economics;"))

        # SS: PBI only if engineering_integration in strategic purposes
        if self.t == "StrategicSupplier":
            purposes = set(self.d.get("supplier", {}).get("strategic_purposes", []))
            if "engineering_integration" in purposes:
                defs.append(('"Protected Business Information" or "PBI"', "means the Provider's proprietary design, engineering, and infrastructure integration methodologies, interface specifications, and technical reference architectures disclosed in connection with the design integration collaboration under Clause 3.7;"))

        if self.t == "Distributor":
            defs.append(('"Purpose"', "means evaluating, negotiating, and progressing toward the execution of an MSA for the Transaction, including all activities under any companion agreements between the Parties (such as a Referral Agreement);"))
        elif self.t == "Wholesale":
            defs.append(('"Purpose"', "means evaluating, negotiating, and progressing toward the execution of an MSA for the provision of AI colocation services;"))
        elif self.t == "StrategicSupplier":
            defs.append(('"Purpose"', "means evaluating, negotiating, and progressing toward the execution of a Framework Agreement and accompanying statements of work for the supply relationship;"))
        else:
            defs.append(('"Purpose"', "means evaluating, negotiating, and progressing toward the execution of an MSA;"))

        if self.t in ("Distributor", "Wholesale", "StrategicSupplier"):
            defs.append(('"Ready-for-Service" or "RFS"', "means the date on which a DEC (or a discrete capacity allocation within a DEC) has been commissioned and is available for the provision of colocation services;"))

        defs.append(('"Representatives"', "means, in relation to a Party, its Affiliates, and its and their respective directors, officers, employees, agents, and professional advisers;"))

        if self.t in ("Distributor", "Wholesale"):
            defs.append(('"Sales Order Form"', "means the document that will form the basis for each binding service order under the MSA" + (", setting out confirmed capacity, pricing, site allocation, and RFS date;" if self.t == "Wholesale" else ";")))

        if self.t == "Wholesale":
            defs.append(('"Services"', "means the AI colocation services to be provided by the Provider, comprising power supply and distribution, liquid cooling infrastructure, physical security, building management, and facility operations;"))
        elif self.t == "EndUser":
            defs.append(('"Services"', "means the AI compute infrastructure services to be provided by the Provider, the scope of which will depend on the service model selected under Clause 3.1."))

        if self.t in ("Distributor", "Wholesale", "StrategicSupplier"):
            defs.append(('"Site Identifier"', "means any information that identifies or could reasonably be used to identify a specific DEC location, including: address, GPS coordinates, cadastral reference, project codename, photographs, aerial imagery, file names, folder names, metadata, and any information derived from the foregoing;"))

        if self.t == "Distributor":
            defs.append(('"Transaction"', "means the proposed strategic partnership between the Parties as described in Clause 3;"))

        if self.t in ("Distributor", "Wholesale"):
            defs.append(('"Whitespace"', "means designated floor area within a DEC available for the deployment of IT hardware and supporting infrastructure."))

        for label, text in defs:
            if label:
                self.bp(label + " ", text)
            else:
                self.p(text)

    def clause2(self):
        self.h("2. Purpose and Scope")
        if self.t == "Distributor":
            self.p(f"2.1 This LOI records the Parties' mutual interest in establishing a strategic partnership under which the {self.party} would participate in the delivery of AI colocation services to end-user customers through the Provider's DEC platform, on the indicative terms set out in Clauses 3 and 4.")
        elif self.t == "Wholesale":
            self.p(f"2.1 This LOI records the Parties' mutual interest in the {self.party} procuring dedicated AI colocation capacity at the Provider's DEC facilities, on the indicative terms set out in Clauses 3 and 4.")
        elif self.t == "StrategicSupplier":
            self.p(f"2.1 This LOI records the Parties' mutual interest in establishing a strategic supply partnership under which the {self.party} would contribute to the delivery of the Provider's DEC platform, on the indicative terms set out in Clauses 3 and 4.")
        else:
            self.p(f"2.1 This LOI records the Parties' mutual interest in the {self.party} procuring AI compute infrastructure services at the Provider's DEC facilities, on the indicative terms set out in Clauses 3 and 4.")

        if self.t in ("Distributor", "Wholesale", "StrategicSupplier"):
            if self.t == "Distributor":
                scoping_phrase = "a framework for further commercial discussion and negotiation toward a definitive MSA"
            elif self.t == "Wholesale":
                scoping_phrase = "the basis for technical scoping and commercial negotiation toward a definitive MSA"
            else:  # StrategicSupplier
                scoping_phrase = "a framework for further technical and commercial discussion toward a definitive Framework Agreement"
            self.p(f"2.2 The Parties intend this LOI to provide {scoping_phrase}. The commercial terms in Clauses 3 and 4 are non-binding expressions of intent.")
            self.p("2.3 The confidentiality, non-circumvention, and general provisions in Clauses 5 through 8 are legally binding and enforceable from the date of execution.")
        else:
            self.p("2.2 The commercial terms in Clauses 3 and 4 are non-binding expressions of intent. The confidentiality and general provisions in Clauses 5 through 7 are legally binding and enforceable from the date of execution.")

    def clause3_ds(self):
        mode = self.d.get("partnership_mode", "combined")
        heading = "3. Partnership and Combined Offering" if mode == "combined" else "3. Partnership and Referral Arrangement"
        self.h(heading)
        comm = self.d.get("commercial", {})
        mode = self.d.get("partnership_mode", "combined")

        # 3.1
        self.bp("3.1 Partnership Overview. ",
                f"{self.g('counterparty', 'short')} provides {comm.get('partner_core_capability', '')}. "
                f"The Provider develops and operates purpose-built AI colocation facilities with secured "
                f"energy and grid access, liquid cooling, and full energy recovery infrastructure.")
        if mode == "combined":
            self.p(
                f"The Parties intend to combine the {self.party}'s {comm.get('partner_contribution', '')} "
                f"with the Provider's colocation platform to deliver {comm.get('combined_offering', '')} "
                f"to {comm.get('target_end_users', '')}."
            )
        else:
            self.p(
                f"The Parties intend to establish a referral arrangement under which the {self.party} "
                f"would introduce qualified end-user customers to the Provider's DEC platform, leveraging "
                f"the {self.party}'s established client relationships and market presence."
            )

        # 3.2
        if mode == "combined":
            self.bp("3.2 Combined Offering. ", "Under the envisaged partnership:")
            self.p("(a) the Provider would supply dedicated AI colocation capacity at its DEC facilities, including power distribution, liquid cooling, physical security, and facility operations;")
            self.p(f"(b) the {self.party} would contribute {comm.get('partner_service_scope', '')}; and")
            self.p(f"(c) the end-user customer would procure a single, integrated solution through the {self.party}, with the Provider's DEC platform as the infrastructure foundation.")
            self.p("The precise service boundaries, responsibility matrix, SLA allocation, and commercial terms of the combined offering will be defined in the MSA.")
        else:
            self.bp("3.2 Referral Arrangement. ",
                     f"The {self.party} would identify and introduce qualified end-user customers to the "
                     f"Provider's DEC platform, leveraging the {self.party}'s market presence, customer "
                     f"relationships, and domain credibility. The Provider would manage all commercial, "
                     f"technical, and contractual relationships with introduced customers directly. The "
                     f"{self.party}'s ongoing role following an introduction \u2014 including relationship "
                     f"support, account management, or technical liaison \u2014 will be agreed on a "
                     f"case-by-case basis and set out in the MSA or a separate Referral Agreement.")
            self.p("The economic terms of the referral arrangement, including qualifying introduction criteria, fee structure, payment terms, and duration, will be set out in a separate Referral Agreement between the Parties.")

        # 3.3
        territory = comm.get("territory", "")
        segments = comm.get("target_segments", "")
        mw = comm.get("indicative_mw", "")
        self.bp("3.3 Commercial Scope. ", "The Parties intend the partnership to address the following market:")
        self.p(f"(a) Territory: {territory};")
        self.p(f"(b) Target segments: {segments}; and")
        self.p(f"(c) Estimated capacity: The {self.party} has indicated an estimated annual capacity requirement of approximately {mw} MW IT across its end-user customer base. This estimate is non-binding and is provided to inform capacity planning.")

        # 3.4
        if self.choice("pricing"):
            self.bp("3.4 Indicative Economics. ", "Based on preliminary discussions, the Parties envisage the following indicative economic framework:")
            ch = self.d.get("choices", {})
            self.table(
                ["Parameter", "Indicative Terms"],
                [
                    ["Partner capacity rate", f"EUR {ch.get('partner_rate', '')} per kW per month"],
                    ["Commercial structure", ch.get("economics_description", "")],
                    ["Minimum annual commitment", f"{ch.get('min_commitment', '')} MW IT"],
                ]
            )
            self.p("All economic terms are indicative and subject to the terms of the MSA.")
        else:
            self.bp("3.4 Indicative Economics. ",
                     "The economic framework for the partnership will be determined during commercial scoping and set out in the MSA. The Provider will issue indicative terms upon agreement of partnership scope, capacity estimates, and contract structure.")

        # 3.5
        if self.choice("exclusivity"):
            scope = self.d.get("choices", {}).get("exclusivity_scope", "")
            self.bp("3.5 Preferred Partner. ",
                     f"Subject to execution of the MSA and achievement of the minimum capacity commitments set out therein, the Provider intends to designate the {self.party} as a preferred partner within the following scope: {scope}. This designation means the Provider will offer the {self.party} priority participation in opportunities within the defined scope before engaging other channel partners for the same opportunity. This LOI does not create any exclusivity obligation; the terms of any such designation will be agreed in the MSA.")
        else:
            self.bp("3.5 Non-Exclusivity. ", "The partnership contemplated by this LOI is non-exclusive. Both Parties retain the right to enter into similar arrangements with third parties.")

    def clause3_ws(self):
        self.h("3. Indicative Capacity and Commercial Terms")
        comm = self.d.get("commercial", {})
        ch = self.d.get("choices", {})
        mw = comm.get("indicative_mw", "")

        # v3.2: capacity expressed in MW IT + Designated Sites; no "DEC Block" customer-facing.
        self.bp("3.1 Indicative Capacity. ", f"The {self.party} has indicated interest in approximately {mw} MW IT of purpose-built, liquid-cooled AI colocation capacity, to be delivered across one or more Designated Sites. Site configuration, phasing, and delivery milestones will be set out in the MSA.")

        self.bp("3.2 Technical Specification. ", "All DEC facilities are designed for high-density AI compute workloads and are expected to include, at minimum: facility power supply and distribution, direct liquid cooling infrastructure supporting rack densities of 40 kW and above, building management, physical security, and 24/7 facility operations. The exact capacity, rack configuration, power density, and cooling requirements will be determined during the technical scoping phase following this LOI.")

        if self.choice("phasing"):
            self.bp("3.3 Deployment Phasing. ", f"The {self.party} has indicated the following high-level phasing interest:")
            phases = ch.get("phases", [])
            rows = [[f"Phase {i+1}", f"{p.get('mw', '')} MW IT", p.get("timeline", "")] for i, p in enumerate(phases)]
            self.table(["Phase", "Approximate Capacity", "Indicative Timeline"], rows)

        exp = comm.get("expansion_mw", "")
        self.bp("3.4 Expansion. ", f"The {self.party} has expressed interest in future expansion to approximately {exp} MW IT, subject to availability, commercial agreement, and the terms of the MSA. The Provider will use reasonable endeavours to accommodate expansion requirements within its DEC programme.")

        if self.choice("pricing"):
            self.bp("3.5 Indicative Pricing. ", f"Based on the {self.party}'s indicated capacity and term preferences, the Provider's indicative pricing is as follows:")
            self.table(
                ["Parameter", "Indicative Terms"],
                [
                    ["Base colocation fee", f"EUR {ch.get('base_price', '')} per kW per month"],
                    ["Contract term", f"{ch.get('term_years', '')} years"],
                    ["Power", "Metered IT Load (kWh) x PUE x Energy Rate (EUR/kWh) \u2014 billed additionally"],
                    ["Price escalation", "Subject to annual escalation, the mechanism for which will be agreed in the MSA"],
                    ["Indicative RFS", ch.get("target_rfs_date", "")],
                    ["Ramp schedule", ch.get("ramp_schedule", "")],
                ]
            )
            self.p(f"All commercial terms are indicative and subject to the outcome of the technical scoping phase, the {self.party}'s final capacity requirements, contract term, and credit profile.")
        else:
            self.bp("3.5 Indicative Pricing. ", f"Pricing for the Services will be determined following the technical scoping phase and set out in the Sales Order Form. The Provider will provide indicative pricing upon completion of the {self.party}'s capacity, density, and term requirements.")

        term = comm.get("min_term", "")
        # v3.2: "minimum commitment term" replaced with "approximately X, indicative only".
        self.bp("3.6 Indicative Term. ", f"The {self.party} anticipates a commitment term of approximately {term}, indicative only and subject to confirmation in the MSA. Actual term may be longer or shorter depending on final commercial terms. The {self.party} acknowledges that the Provider intends the MSA to include take-or-pay provisions commensurate with the committed capacity, the terms of which will be negotiated in good faith.")

        self.bp("3.7 Credit Assessment. ", f"The Provider will complete a credit assessment of the {self.party} (or the entity that will execute the MSA) as part of the commercial process. The {self.party} agrees to cooperate with such assessment, which may include provision of audited financial statements, credit references, evidence of parent company support, or other financial information as reasonably requested. Where the {self.party} does not hold an investment-grade credit rating (or equivalent), the Parties will discuss appropriate credit support mechanisms, which may include a parent company guarantee, security deposit, or letter of credit.")

        self.bp("3.8 Site Allocation. ", f"The Provider is developing DEC facilities across multiple locations. The Provider will allocate capacity to the {self.party} based on the DEC(s) best suited to the {self.party}'s requirements, taking into account development readiness, grid availability, RFS timeline, and the {self.party}'s latency and connectivity needs. Site allocation will be confirmed during the technical scoping phase and formalised in the Sales Order Form.")

    def clause3_eu(self):
        self.h("3. Service Requirements")
        comm = self.d.get("commercial", {})
        types = comm.get("service_type", [])

        self.bp("3.1 Service Model. ", f"The {self.party} has indicated interest in the following service model:")

        descs = {
            "bare_metal": (
                "Bare Metal Colocation \u2014 Dedicated, liquid-cooled rack space within a DEC, supporting "
                "densities of 40 kW per rack and above. The Provider supplies power distribution, direct "
                "liquid cooling, physical security, and 24/7 facility operations. The Customer deploys and "
                "manages its own hardware and software. The demarcation point is at the rack: everything "
                "below (facility infrastructure) is the Provider's responsibility; everything above (compute "
                "hardware, operating system, workloads) is the Customer's. Billed monthly on a per-kW basis "
                "with a committed term."
            ),
            "shared_cloud": (
                "Shared Cloud \u2014 Managed GPU compute capacity hosted on sovereign European infrastructure "
                "at the Provider's DEC facilities. The Customer accesses reserved or on-demand compute "
                "resources without procuring, deploying, or managing hardware. The Provider or a designated "
                "delivery partner operates the compute platform, including hardware lifecycle, scheduling, "
                "and platform software. The Customer manages workloads, data, and application layers. Billed "
                "on reserved capacity or metered usage, with a committed term or minimum spend."
            ),
            "tokens": (
                "Token-Based GPU Access \u2014 Flexible, on-demand access to GPU compute measured in GPU-hours "
                "or equivalent units. The Customer purchases compute tokens \u2014 pre-paid or pay-as-you-go "
                "\u2014 redeemable against available capacity across the Provider's DEC network. No dedicated "
                "hardware allocation or minimum infrastructure commitment. The Provider or a designated "
                "delivery partner manages all infrastructure and scheduling. The Customer submits workloads "
                "and consumes capacity as needed. Lowest entry threshold; designed for variable or exploratory "
                "workloads."
            ),
        }
        for st in types:
            if st in descs:
                self.p(descs[st])

        if any(st in ("shared_cloud", "tokens") for st in types):
            self.p("For Shared Cloud and Token-Based models: the Provider may deliver these services in partnership with a qualified delivery partner. The specific delivery partner, platform, and commercial terms will be confirmed in the MSA.", italic=True)

        cap = comm.get("indicative_capacity", "")
        self.bp("3.2 Indicative Capacity. ", f"The {self.party} has indicated interest in approximately {cap} of compute capacity. The exact capacity, configuration, and technical requirements will be determined during the technical scoping phase.")

        self.bp("3.3 Technical Requirements. ", f"The Provider's DEC facilities support rack densities of 40 kW and above with direct liquid cooling, designed for GPU-intensive training and inference workloads. The {self.party}'s specific requirements \u2014 including GPU type, rack density, network connectivity, and data sovereignty needs \u2014 will be confirmed during technical scoping and formalised in the MSA.")

        if self.choice("pricing"):
            ch = self.d.get("choices", {})
            self.bp("3.4 Indicative Pricing. ", "Based on preliminary discussions, the Provider's indicative pricing is as follows:")
            self.table(
                ["Parameter", "Indicative Terms"],
                [
                    ["Service rate", f"EUR {ch.get('base_price', '')} {ch.get('pricing_unit', 'per kW per month')}"],
                    ["Contract term", ch.get("term_years", "")],
                    ["Indicative RFS", ch.get("target_rfs_date", "")],
                ]
            )
            self.p(f"All terms are indicative and subject to the outcome of technical scoping and the {self.party}'s final requirements.")
        else:
            self.bp("3.4 Indicative Pricing. ", f"Pricing will be determined following the technical scoping phase and set out in the MSA. The Provider will provide indicative pricing upon agreement of the {self.party}'s capacity, density, and service model requirements.")

        term = comm.get("min_term", "")
        # v3.2: indicative, not "minimum commitment"
        self.bp("3.5 Indicative Term. ", f"The {self.party} anticipates a commitment term of approximately {term}, indicative only and subject to confirmation in the MSA.")

    def clause3_ss(self):
        """v3.3: Strategic Supplier Cl. 3 — Partnership Scope.

        3.1 Capability Contribution (ALWAYS). Then 3.2-3.8 are purpose-driven:
        - capacity_lock_in       -> 3.2 Capacity Reservation, 3.3 Lead-Time Targets
        - pricing_volume         -> 3.4 Pricing Framework, 3.5 Volume Tiers
        - supply_chain_de_risking-> 3.6 Dual-Source + Continuity
        - engineering_integration-> 3.7 Design Integration + IP Allocation
        - pipeline_visibility    -> 3.8 Preferred-Supplier / ROFR
        """
        self.h("3. Partnership Scope")
        supplier = self.d.get("supplier", {})
        purposes = set(supplier.get("strategic_purposes", []))

        # 3.1 Capability Contribution (ALWAYS)
        self.bp(
            "3.1 Capability Contribution. ",
            "Under the envisaged partnership:"
        )
        self.p(
            "(a) the Provider would contribute the site, energy procurement, grid "
            "connection, land and regulatory compliance, long-term operational "
            "responsibility, and integration into the Provider's broader DEC "
            "platform for each Designated Site; and"
        )
        self.p(
            f"(b) the {self.party} would contribute "
            f"{supplier.get('core_capability', '[CAPABILITY DESCRIPTION TO BE CONFIRMED]')}."
        )
        self.p(
            "The precise scope boundaries, responsibility matrix, and commercial "
            "terms will be defined in the Framework Agreement and accompanying "
            "statements of work."
        )

        # 3.2 Capacity Reservation — IF capacity_lock_in
        if "capacity_lock_in" in purposes:
            lead_time = supplier.get("lead_time_target", "[LEAD TIME TO BE CONFIRMED]")
            self.bp(
                "3.2 Capacity Reservation. ",
                f"The Provider has indicated a projected demand across its active "
                f"development pipeline. Subject to commercial agreement, the "
                f"{self.party} will reserve capacity in its manufacturing or "
                f"service-delivery plan to support the Provider's indicative "
                f"pipeline, with specific volumes and delivery windows set out in "
                f"the Framework Agreement."
            )
            # 3.3 Lead-Time Targets — same trigger
            self.bp(
                "3.3 Lead-Time Targets. ",
                f"The {self.party} targets {lead_time}. The Framework Agreement "
                f"will set the binding lead-time commitments, performance "
                f"measurement, and remedies for delay."
            )

        # 3.4 Pricing Framework — IF pricing_volume
        if "pricing_volume" in purposes:
            volume = supplier.get("volume_indicative", "[VOLUME TO BE CONFIRMED]")
            self.bp(
                "3.4 Pricing Framework. ",
                "The pricing framework will be structured as cost-plus, unit "
                "economics, or volume-tier model as appropriate to the supply "
                "category. Specific pricing, volume thresholds, and escalation "
                "mechanisms will be set out in the Framework Agreement."
            )
            # 3.5 Volume Tiers — same trigger
            self.bp(
                "3.5 Volume Tiers. ",
                f"Indicative volume contemplated: {volume}. The Framework "
                f"Agreement will set out final volume tiers and the commercial "
                f"principles applicable at each tier. All volumes and pricing "
                f"in this LOI are non-binding."
            )

        # 3.6 Dual-Source and Continuity — IF supply_chain_de_risking
        if "supply_chain_de_risking" in purposes:
            self.bp(
                "3.6 Dual-Source and Continuity Commitments. ",
                f"The {self.party} acknowledges the Provider's requirement for "
                f"supply-chain resilience. The Parties will discuss, and document "
                f"in the Framework Agreement: (a) component substitution and "
                f"second-source provisions; (b) continuity commitments, including "
                f"obligations to provide advance notice of discontinuation and to "
                f"support orderly transition; and (c) delivery service-level "
                f"commitments and remedies for failure to meet them."
            )

        # 3.7 Design Integration and IP Allocation — IF engineering_integration
        if "engineering_integration" in purposes:
            joint_ip = self.g("choices", "joint_ip", default="background").lower()
            if joint_ip == "none":
                ip_clause = (
                    "no foreground IP is contemplated as a deliverable of the "
                    "collaboration, and any IP developed will remain with the "
                    "Party that created it;"
                )
            elif joint_ip == "foreground":
                ip_clause = (
                    "foreground IP developed jointly in the course of the "
                    "collaboration will be jointly owned, with cross-licences on "
                    "terms to be agreed in the Framework Agreement;"
                )
            else:  # background (default)
                ip_clause = (
                    "each Party retains all right, title, and interest in its "
                    "background IP; any foreground IP developed jointly will be "
                    "allocated per the principles set out in the Framework Agreement;"
                )
            self.bp(
                "3.7 Design Integration and IP Allocation. ",
                f"The Parties will collaborate on design integration across the "
                f"specified interfaces between the Provider's DEC platform and "
                f"the {self.party}'s contribution. IP allocation: (a) {ip_clause} "
                f"(b) no Party assigns pre-existing IP by reason of this LOI or "
                f"any discussions under it; and (c) the full IP framework will be "
                f"set out in the Framework Agreement."
            )

        # 3.8 Preferred-Supplier / ROFR — IF pipeline_visibility
        if "pipeline_visibility" in purposes:
            self.bp(
                "3.8 Preferred-Supplier and Right of First Refusal. ",
                f"Subject to commercial agreement in the Framework Agreement, the "
                f"Provider intends to grant the {self.party} a right of first "
                f"refusal on the procurement of the supply scope set out in "
                f"Clause 3.1(b) across the Provider's active development pipeline. "
                f"The right of first refusal requires the {self.party} to submit "
                f"a compliant proposal within 20 Business Days of the Provider's "
                f"invitation. This LOI does not create any binding right of first "
                f"refusal; the terms will be set out in the Framework Agreement."
            )

    def clause4_ss(self):
        """v3.3: Strategic Supplier Cl. 4 — Pipeline Engagement.

        4.2 Contractual Sequence, 4.4 Change of Control, 4.6 Implementation
        Roadmap are ALWAYS. Others are purpose-driven.
        """
        self.h("4. Pipeline Engagement")
        purposes = set(self.d.get("supplier", {}).get("strategic_purposes", []))

        # 4.1 Project Introduction Process — IF pipeline_visibility
        if "pipeline_visibility" in purposes:
            self.bp(
                "4.1 Project Introduction Process. ",
                f"Following execution of this LOI, the Provider intends to "
                f"maintain a pipeline register of Designated Sites. The "
                f"{self.party} will be invited to participate in named project "
                f"opportunities on the cadence and criteria set out in the "
                f"Framework Agreement."
            )

        # 4.2 Contractual Sequence (ALWAYS) — mirrors WS Cl. 4.2 pattern
        self.bp(
            "4.2 Contractual Sequence. ",
            "The Parties acknowledge the intended progression of commercial instruments:"
        )
        self.p("(a) this LOI, setting out non-binding commercial intent and binding confidentiality and non-circumvention;")
        self.p("(b) a Framework Agreement, setting out the definitive commercial and operational framework for the supply relationship;")
        self.p("(c) one or more Statements of Work for named Provider projects, each executed under the Framework Agreement; and")
        self.p("(d) site-specific deliverables, schedules, or operational annexes executed under each Statement of Work.")
        self.p(
            "Each stage is designed to provide increasing commercial certainty "
            "and to support the Provider's project finance activities."
        )

        # 4.3 Joint-Development Governance — IF engineering_integration
        if "engineering_integration" in purposes:
            self.bp(
                "4.3 Joint-Development Governance. ",
                "The Parties intend to establish a joint design and engineering "
                "working group to coordinate interfaces, design reviews, and "
                "lifecycle decisions. The governance structure, decision rights, "
                "and escalation paths will be set out in the Framework Agreement."
            )

        # 4.4 Change of Control (ALWAYS)
        self.bp(
            "4.4 Change of Control. ",
            f"If, during the term of this LOI, a direct competitor of the "
            f"Provider (as determined by reference to its primary business being "
            f"the development, ownership, or operation of colocation facilities "
            f"for high-density compute workloads) acquires Control of the "
            f"{self.party}, the Provider may terminate this LOI by written notice "
            f"with immediate effect. Upon such termination, the confidentiality "
            f"and non-circumvention obligations in Clauses 6 and 7 shall "
            f"continue for their stated survival periods."
        )

        # 4.5 Exclusivity — IF capacity_lock_in AND choices.exclusivity
        if "capacity_lock_in" in purposes and self.choice("exclusivity"):
            self.bp(
                "4.5 Exclusivity. ",
                "Subject to execution of the Framework Agreement and achievement "
                "of the reservation commitments set out therein, the Parties "
                "intend to agree a scope of mutual exclusivity. This LOI does "
                "not create any exclusivity; the terms will be agreed in the "
                "Framework Agreement."
            )

        # 4.6 Implementation Roadmap (ALWAYS)
        self.bp(
            "4.6 Implementation Roadmap. ",
            "Following execution of this LOI, the Parties intend to proceed as follows:"
        )
        self.p("(a) Technical and commercial scoping (target: 30 days post-LOI) — detailed discovery on scope, capability, lead times, pricing framework, and IP allocation.")
        self.p("(b) Draft Framework Agreement (target: 60 days post-LOI) — the Provider will issue a draft Framework Agreement incorporating the agreed terms.")
        self.p("(c) Framework Agreement negotiation and execution (target: 90 days post-LOI) — the Parties will negotiate and execute the Framework Agreement.")
        self.p("These timelines are indicative and non-binding.")

    def clause4(self):
        if self.t == "Distributor":
            self.h("4. Relationship Structure and Protection")
            pbi = self.g("protection", "pbi_survival", default="10 years")
            self.bp("4.1 Protected Business Information. ",
                     f"The {self.party} acknowledges that the Provider's competitive position depends on the confidentiality of its Protected Business Information as defined in Clause 1. The {self.party} agrees that, for a period of {pbi} from the date of this LOI, it shall not directly or indirectly use any PBI to replicate, reverse-engineer, or independently develop any material element of the Provider's business model, site-sourcing methodology, energy procurement strategy, or commercial framework, whether for itself or for any third party. This obligation survives termination or expiry of this LOI and of any MSA.")
            self.bp("4.2 Change of Control. ",
                     f"If, during the term of this LOI, a Competitor acquires Control (as defined in Clause 1.1, \u201cAffiliate\u201d) of the {self.party}, the Provider may terminate this LOI by written notice with immediate effect. Upon such termination, the confidentiality and non-circumvention obligations in Clauses 6 and 7 shall continue for their stated survival periods.")
            self.bp("4.3 Associated Counterparties. ",
                     f"The {self.party} acknowledges that the Provider maintains relationships with Associated Counterparties at each DEC site. The sharing of any Site Identifier by the Provider shall be deemed an introduction of all Associated Counterparties for that site for the purposes of Clause 7.")
            self.bp("4.4 Governance. ", "The Parties intend to establish a joint steering committee or equivalent governance mechanism, the terms of which will be set out in the MSA.")
            self.bp("4.5 Implementation Roadmap. ", "Following execution of this LOI, the Parties intend to proceed as follows:")
            self.p("(a) Commercial scoping (target: 30 days post-LOI) \u2014 The Parties will define the partnership scope, target customer segments, capacity estimates, and economic framework.", bold=False)
            self.p("(b) Draft Partnership Agreement (target: 60 days post-LOI) \u2014 The Provider will issue a draft MSA or partnership agreement incorporating the agreed commercial terms.")
            self.p("(c) MSA negotiation and execution (target: 90 days post-LOI) \u2014 The Parties will negotiate and execute the MSA.")
            self.p("These timelines are indicative and non-binding.")

        elif self.t == "Wholesale":
            self.h("4. Relationship Structure and Next Steps")
            self.bp("4.1 MSA Structure. ", "The Parties intend to execute a Master Services Agreement incorporating: (a) a Pricing Framework setting out the commercial terms for the Services; (b) Sales Order Forms for each capacity commitment; and (c) an SLA Schedule defining availability, performance, and remediation commitments. The MSA will be the sole binding commercial agreement between the Parties.")
            # v3.2: Cl. 4.2 arrows replaced with institutional prose + numbered list.
            self.bp("4.2 Contractual Sequence. ", "The Parties acknowledge the intended progression of commercial instruments:")
            self.p("(a) this LOI, setting out non-binding commercial intent;")
            self.p("(b) a Sales Order Form or equivalent binding capacity commitment with indicative pricing;")
            self.p("(c) the Master Services Agreement (MSA), containing definitive commercial terms; and")
            self.p("(d) site-specific deliverables, schedules, or operational annexes executed under the MSA.")
            self.p("Each stage is designed to provide increasing commercial certainty and to support the Provider's project finance activities.")
            self.bp("4.3 Direct Agreement Willingness. ", f"The {self.party} confirms its willingness, subject to commercially reasonable terms, to enter into a direct agreement with the Provider's Financing Parties if requested under Clause 5.3. The {self.party} acknowledges that its cooperation in this regard materially supports the Provider's ability to deliver the committed capacity on the indicative timeline.")
            self.bp("4.4 Expansion and Priority. ", f"The Provider will offer the {self.party} priority access to additional capacity within the DEC(s) allocated to the {self.party}, subject to availability. Expansion terms will be governed by the MSA.")
            self.bp("4.5 Implementation Roadmap. ", "Following execution of this LOI, the Parties intend to proceed as follows:")
            self.p("(a) Technical scoping (target: 30 days post-LOI) \u2014 Detailed technical discovery to determine exact capacity, rack layout, power distribution, cooling specifications, and connectivity requirements.")
            self.p(f"(b) Credit assessment (target: 30 days post-LOI, concurrent with technical scoping) \u2014 The Provider will complete a credit assessment of the {self.party} or the entity that will execute the MSA.")
            self.p("(c) Sales Order Form (target: 60 days post-LOI) \u2014 Upon completion of technical scoping, the Provider will issue a Sales Order Form setting out confirmed commercial terms, facility specifications, and service level framework.")
            self.p("(d) MSA negotiation and execution (target: 90 days post-LOI) \u2014 The Parties will negotiate and execute the MSA.")
            self.p("These timelines are indicative and non-binding.")
            self.bp("4.6 No Capacity Reservation. ", "This LOI does not reserve capacity at any DEC. Capacity allocation is on a first-come, first-served basis and will only be confirmed upon execution of the MSA.")

        else:  # EndUser
            self.h("4. Next Steps")
            self.p("4.1 Following execution of this LOI, the Parties intend to proceed as follows:")
            self.p("(a) Technical scoping (target: 30 days post-LOI) \u2014 Detailed discovery to determine capacity, configuration, connectivity, and service model requirements.")
            self.p("(b) Commercial proposal (target: 60 days post-LOI) \u2014 The Provider will issue a commercial proposal setting out confirmed pricing, service scope, and SLA framework.")
            self.p("(c) MSA negotiation and execution (target: 90 days post-LOI) \u2014 The Parties will negotiate and execute the MSA.")
            self.p("These timelines are indicative and non-binding.")
            self.p("4.2 This LOI does not reserve capacity at any DEC. Capacity allocation will be confirmed upon execution of the MSA.")

    def clause5(self):
        self.h("5. Project Finance and Assignment (BINDING)")
        self.bp("5.1 Revenue Bankability. ", "The Parties acknowledge that the Provider intends to finance the development and operation of its DEC programme through a combination of equity investment and non-recourse project finance. The Provider's ability to secure favourable financing terms depends in part on demonstrating contracted or committed revenue streams. This LOI, while non-binding in its commercial terms, is intended to evidence the Parties' genuine commercial intent and to support the Provider's financing activities.")
        self.bp("5.2 Assignment. ", f"Neither Party may assign its rights or obligations under this LOI without the prior written consent of the other Party, except that:")
        self.p("(a) the Provider may assign this LOI, or any rights under it, to any Financing Party or security trustee as security for project finance obligations; and")
        self.p(f"(b) the Provider may assign this LOI to any Affiliate or special-purpose vehicle within its corporate group without the {self.party}'s consent, provided the Provider remains liable for the performance of the assignee's obligations.")
        self.bp("5.3 Lender Acknowledgment. ", f"The {self.party} acknowledges and agrees that, upon the Provider's written request, the {self.party} shall negotiate in good faith and execute a direct agreement (or lender acknowledgment letter) with the Provider's Financing Party within 30 Business Days of such request. Such direct agreement may include, as is customary in project finance transactions: (a) step-in rights for the Financing Party upon a Provider default; (b) cure periods in favour of the Financing Party; and (c) information rights enabling the Financing Party to monitor the commercial relationship. The terms of any such direct agreement shall be commercially reasonable and consistent with market practice for project finance transactions.")

    def clause6(self):
        self.h(f"6. Confidentiality {'and Non-Disclosure ' if self.t != 'EndUser' else ''}(BINDING)")
        existing = self.choice("existing_nda")

        if existing:
            nda_date = self.g("choices", "nda_date")
            transaction_suffix = " and the Transaction." if self.t == "Distributor" else (" and the proposed transaction." if self.t == "Wholesale" else ".")
            self.p(f'6.1 The Non-Disclosure Agreement between the Parties dated {nda_date} (the "NDA") remains in full force and effect and applies to all information exchanged in connection with this LOI{transaction_suffix}')
            self.p("6.2 The existence and contents of this LOI shall be treated as Confidential Information under the NDA.")
            if self.t != "EndUser":
                self.p("6.3 To the extent of any conflict between the NDA and this LOI, the provisions of this LOI shall prevail.")
                transaction_ref = "the Transaction" if self.t == "Distributor" else "the proposed transaction"
                self.p(f"6.4 Neither Party shall make any public announcement regarding this LOI or {transaction_ref} without the prior written consent of the other Party, except as required by applicable law.")
            else:
                self.p("6.3 Neither Party shall make any public announcement regarding this LOI without the prior written consent of the other Party, except as required by applicable law.")
        else:
            surv = self.g("protection", "confidentiality_survival", default="3 years")
            if self.t == "EndUser":
                # Tier A — 8 clauses
                self.p(f"6.1 Each Party shall keep confidential all Confidential Information received from the other Party and shall use such information solely for the Purpose.")
                self.p("6.2 Each Party may disclose Confidential Information only to its Representatives who have a genuine need to know for the Purpose and who are bound by confidentiality obligations no less restrictive than this Clause 6.")
                self.p("6.3 The obligations in Clauses 6.1 and 6.2 do not apply to information that the receiving Party can demonstrate: (a) is or becomes publicly available through no fault of the receiving Party; (b) was already in the receiving Party's possession without restriction; (c) was independently developed without use of the Confidential Information; or (d) was received from a third party without breach of any confidentiality obligation.")
                self.p("6.4 A Party may disclose Confidential Information to the extent required by applicable law, regulation, or court order, provided that (where legally permitted) the disclosing Party gives the other Party prior written notice and discloses only the minimum required.")
                self.p("6.5 Upon written request or expiry of this LOI, the receiving Party shall promptly return or destroy all Confidential Information and certify such return or destruction in writing. The receiving Party may retain copies required by applicable law or internal compliance policies, subject to continued confidentiality.")
                self.p("6.6 Neither Party shall make any public announcement regarding this LOI without the prior written consent of the other Party, except as required by applicable law.")
                self.p(f"6.7 The obligations in this Clause 6 shall survive for {surv} from the date of termination or expiry of this LOI. Obligations in respect of trade secrets shall continue indefinitely.")
                self.p("6.8 Each Party acknowledges that a breach of this Clause 6 may cause irreparable harm for which damages would not be an adequate remedy. The disclosing Party shall be entitled to seek injunctive or other equitable relief without the need to prove actual loss.")
            else:
                # Tier B — 16 clauses
                self.bp("6.1 Purpose Limitation. ", "Each Party shall use the other Party's Confidential Information solely for the Purpose and for no other purpose.")
                self.bp("6.2 Non-Disclosure. ", "Each Party shall keep confidential all Confidential Information received from the other Party and shall not disclose such information to any person except as permitted under this Clause 6.")
                self.bp("6.3 Standard of Care. ", "Each Party shall apply no less than reasonable care to protect the other Party's Confidential Information, and no less than the care it applies to its own confidential information of a similar nature.")
                self.bp("6.4 Permitted Disclosures. ", "A Party may disclose Confidential Information to:")
                self.p("(a) its Representatives who have a genuine need to know for the Purpose and who are bound by confidentiality obligations no less restrictive than this Clause 6 (whether by professional duty or written undertaking);")
                self.p("(b) its bona fide Financing Parties and potential co-investors, provided they are bound by confidentiality obligations no less restrictive than this Clause 6; and")
                self.p("(c) to the extent required by applicable law, regulation, court order, or the rules of any relevant regulatory authority or stock exchange, provided that (where legally permitted) the disclosing Party: (i) gives the other Party prior written notice as soon as reasonably practicable; (ii) consults with the other Party regarding the scope and manner of disclosure; and (iii) discloses only the minimum information required to comply.")
                self.bp("6.5 Liability for Representatives. ", "Each Party shall be responsible for any breach of this Clause 6 by its Representatives.")
                self.bp("6.6 Exclusions. ", "The obligations in Clauses 6.1 through 6.3 do not apply to information that the receiving Party can demonstrate:")
                self.p("(a) is or becomes publicly available through no fault of the receiving Party or its Representatives;")
                self.p("(b) was already in the lawful possession of the receiving Party before disclosure, without restriction as to use or disclosure;")
                self.p("(c) was independently developed by the receiving Party without use of or reference to the Confidential Information; or")
                self.p("(d) was received from a third party who was not, to the receiving Party's knowledge, under any obligation of confidentiality in respect of that information.")
                self.bp("6.7 No Implied Rights. ", "No licence or right is granted under this LOI to the receiving Party in respect of any intellectual property rights of the disclosing Party. All Confidential Information remains the property of the disclosing Party.")
                self.bp("6.8 Return and Destruction. ", "Upon the earlier of: (a) the disclosing Party's written request, or (b) the expiry or termination of this LOI, the receiving Party shall promptly return or destroy all documents, materials, and tangible items containing Confidential Information and certify such return or destruction in writing within 15 Business Days. The receiving Party may retain copies to the extent required by applicable law or its internal compliance policies, provided such retained copies remain subject to this Clause 6.")
                self.bp("6.9 Onward-Sharing Controls. ", "If the receiving Party receives an inquiry from any third party regarding the disclosing Party's Confidential Information, the receiving Party shall: (a) not respond to such inquiry without the disclosing Party's prior written consent; and (b) promptly notify the disclosing Party of such inquiry. The receiving Party shall not further distribute or re-disclose Confidential Information beyond the persons authorised under Clause 6.4 without the disclosing Party's prior written consent.")
                self.bp("6.10 Compliance Confirmation. ", "Upon the disclosing Party's reasonable written request (not more than once per calendar year), the receiving Party shall confirm in writing its compliance with the obligations in this Clause 6.")
                self.bp("6.11 Breach Notification. ", "Each Party shall notify the other Party in writing within 72 hours of becoming aware of any actual or suspected breach of this Clause 6, and shall take all reasonable steps to mitigate the effects of such breach.")
                self.bp("6.12 Disclaimer. ", 'All Confidential Information is disclosed "as is." The disclosing Party makes no representation or warranty, express or implied, as to the accuracy, completeness, or reliability of any Confidential Information. The receiving Party shall be solely responsible for its own assessment and due diligence.')
                self.bp("6.13 Metadata Protection. ", "Confidential Information includes metadata, EXIF data, geolocation data, timestamps, file names, folder names, and any digital artifacts associated with or derived from disclosed materials. The receiving Party shall not extract, analyse, or use such metadata except as necessary for the Purpose.")
                surv_text = f"6.14 Survival. The obligations in this Clause 6 shall survive termination or expiry of this LOI for a period of {surv} from the date of termination or expiry. Obligations in respect of information that constitutes a trade secret under applicable law shall continue indefinitely."
                if self.t == "Distributor":
                    surv_text += " Obligations in respect of Protected Business Information shall survive for the period specified in Clause 4.1."
                self.bp("6.14 Survival. ", surv_text.replace("6.14 Survival. ", ""))
                transaction_ref = "the Transaction" if self.t == "Distributor" else "the proposed transaction"
                self.bp("6.15 Announcements. ", f"Neither Party shall make any public announcement regarding this LOI or {transaction_ref} without the prior written consent of the other Party, except as required by applicable law.")
                self.bp("6.16 Remedies. ", "Each Party acknowledges that a breach of this Clause 6 may cause the disclosing Party irreparable harm for which damages would not be an adequate remedy. The disclosing Party shall be entitled to seek injunctive or other equitable relief from any court of competent jurisdiction, without the need to prove actual loss and without prejudice to any other rights or remedies.")

    def clause7_nc(self):
        if self.t == "EndUser" or self.t == "EcosystemPartnership":
            return  # No NC for End Users or Ecosystem Partnerships

        self.h("7. Non-Circumvention (BINDING)")
        nc_dur = self.g("protection", "nc_duration", default="24 months")

        # v3.3: for SS, downstream agreement is "Framework Agreement"; otherwise "MSA".
        downstream = "Framework Agreement" if self.t == "StrategicSupplier" else "MSA"

        self.p(f"7.1 The {self.party} shall not, directly or indirectly, without the prior written consent of the Provider:")

        if self.t == "Distributor":
            self.p(f"(a) contact, solicit, deal with, or enter into any business relationship with any Associated Counterparty introduced by the Provider in connection with the Purpose or the Transaction;")
            self.p(f"(b) circumvent, avoid, or bypass the Provider in order to deal directly or indirectly with any Associated Counterparty; or")
            self.p(f"(c) attempt to divert or appropriate any business opportunity disclosed by the Provider in connection with the Purpose or the Transaction.")
        elif self.t == "StrategicSupplier":
            self.p(f"(a) contact, solicit, deal with, or enter into any business relationship with any Associated Counterparty introduced by the Provider in connection with this LOI or any Provider project; or")
            self.p(f"(b) circumvent, avoid, or bypass the Provider in order to deal directly or indirectly with any Associated Counterparty in connection with the development, ownership, or operation of colocation or energy infrastructure on or adjacent to a site identified by the Provider.")
        else:  # Wholesale — lighter scope
            self.p(f"(a) contact, solicit, deal with, or enter into any business relationship with any Associated Counterparty introduced by the Provider in connection with this LOI or the Services; or")
            self.p(f"(b) circumvent, avoid, or bypass the Provider in order to deal directly or indirectly with any Associated Counterparty in connection with the development, ownership, or operation of colocation or energy infrastructure on or adjacent to a site identified by the Provider.")

        self.bp("7.2 Duration. ", f"The obligations in this Clause 7 shall continue for {nc_dur} after the earlier of: (a) the expiry or termination of this LOI; or (b) the expiry or termination of the {downstream}, if one is executed.")
        self.bp("7.3 Deemed Introduction. ", f"The Provider's sharing of any Site Identifier with the {self.party} shall constitute a deemed introduction of all Associated Counterparties for that site. The Provider is not required to separately name each Associated Counterparty.")

        if self.t == "Distributor":
            self.bp("7.4 Scope \u2014 Private and Public Bodies. ", "The non-circumvention obligations in Clause 7.1 apply to:")
            self.p("(a) Private Associated Counterparties (landowners, greenhouse operators, heat offtakers, energy counterparties, EPCs): in all cases where the Provider has introduced or disclosed their identity or involvement; and")
            self.p("(b) Public Bodies (government agencies, municipalities, regulatory bodies, distribution system operators): only where the Provider has made a specific, named introduction to an individual or department within that body. General knowledge that the Provider engages with a public body does not trigger non-circumvention protection.")
        elif self.t == "StrategicSupplier":
            self.bp("7.4 Scope Limitation. ", f"The non-circumvention obligations in this Clause 7 are limited to the Provider's supply-side relationships (site partners, energy counterparties, and infrastructure providers). Nothing in this Clause 7 restricts the {self.party} from conducting its own business with its existing or future customers, including other colocation operators, cloud service providers, or enterprise customers.")
        else:
            self.bp("7.4 Scope Limitation. ", f"The non-circumvention obligations in this Clause 7 are limited to the Provider's supply-side relationships (site partners, energy counterparties, and infrastructure providers). Nothing in this Clause 7 restricts the {self.party} from conducting its own business with its existing or future end-user customers, cloud service customers, or compute buyers.")

        self.bp("7.5 Independent Knowledge Exception. ", f"The obligations in Clause 7.1 do not apply to any Associated Counterparty with whom the {self.party} can demonstrate, by contemporaneous written evidence, that it had an existing business relationship or substantive commercial contact before the date of this LOI or before the Provider's disclosure.")
        self.bp(f"7.6 {downstream} Supersession. ", f"If the Parties execute a {downstream}, the non-circumvention provisions of the {downstream} shall replace this Clause 7 upon execution of the {downstream}, except that the survival period in Clause 7.2 shall apply to any introduction made before the {downstream} effective date that is not separately covered by the {downstream}.")

    def clause_general(self):
        cl = "8" if self.t != "EndUser" else "7"
        self.h(f"{cl}. General Provisions (BINDING)")
        val_date = self.g("dates", "validity_date")
        if not val_date:
            val_date = "[12 months from LOI date]"

        # v3.3: SS refers to "Framework Agreement" as downstream binding document.
        downstream = "Framework Agreement" if self.t == "StrategicSupplier" else "MSA"

        self.bp(f"{cl}.1 Non-Binding Status. ", "")
        if self.t != "EndUser":
            self.p(f"(a) Non-binding provisions. Clauses 2 through 4 and Schedule 1 of this LOI are non-binding expressions of the Parties' current intentions. They do not create legally enforceable obligations and are subject to the negotiation and execution of the {downstream}.")
            self.p(f"(b) Binding provisions. Clauses 5 (Project Finance and Assignment), 6 (Confidentiality), 7 (Non-Circumvention), and {cl} (General Provisions) are legally binding and enforceable obligations.")
        else:
            self.p("(a) Non-binding provisions. Clauses 2 through 4 of this LOI are non-binding expressions of the Parties' current intentions. They do not create legally enforceable obligations and are subject to the negotiation and execution of the MSA.")
            self.p(f"(b) Binding provisions. Clauses 5 (Project Finance and Assignment), 6 (Confidentiality), and {cl} (General Provisions) are legally binding and enforceable obligations.")

        scoping_phrase = "commercial scoping and negotiation" if self.t == "Distributor" else "technical scoping and commercial negotiation"
        self.bp(f"{cl}.2 Good Faith. ", f"The Parties agree to engage in the {scoping_phrase} process in good faith (te goeder trouw) and in accordance with the principles of reasonableness and fairness (redelijkheid en billijkheid) as contemplated by Article 6:248 of the Dutch Civil Code (Burgerlijk Wetboek). " + ("" if self.t == "EndUser" else "For the avoidance of doubt, t") + ("T" if self.t == "EndUser" else "t") + f"he good faith obligation does not oblige either Party to enter into the {downstream}. Either Party may discontinue negotiations at any time, provided it does so in good faith. Any liability arising from a breach of this good faith obligation shall be limited to verifiable reliance damages (negatief contractsbelang)" + ("." if self.t == "EndUser" else " and shall not extend to loss of profit or expectation damages (positief contractsbelang)."))

        survive = "Clauses 5.2, 5.3, 6, and 7" if self.t != "EndUser" else "Clauses 5.2, 5.3, and 6"
        self.bp(f"{cl}.3 Validity. ", f"This LOI shall remain valid until {val_date}, after which it shall lapse automatically unless extended by mutual written agreement. Upon lapse, {survive} shall survive for their respective stated periods.")
        self.bp(f"{cl}.4 Costs. ", "Each Party shall bear its own costs in connection with this LOI" + (f" and the negotiation of the {downstream}." if self.t != "EndUser" else "."))
        self.bp(f"{cl}.5 Counterparts. ", "This LOI may be executed in counterparts, including by electronic signature within the meaning of the eIDAS Regulation (EU) No 910/2014." + (" Each counterpart constitutes an original." if self.t != "EndUser" else ""))
        self.bp(f"{cl}.6 Notices. ", "All notices under this LOI shall be in writing (including email) and addressed to the contact details in the preamble. A notice is effective upon receipt." + (" Each Party shall promptly notify the other of any change to its contact details." if self.t != "EndUser" else ""))
        self.bp(f"{cl}.7 Governing Law. ", "This LOI shall be governed by and construed in accordance with the laws of the Netherlands. The United Nations Convention on Contracts for the International Sale of Goods (CISG) is expressly excluded.")
        self.bp(f"{cl}.8 Jurisdiction. ", "The courts of Amsterdam (Rechtbank Amsterdam) shall have exclusive jurisdiction over any dispute arising out of or in connection with the binding provisions of this LOI.")

        if self.t != "EndUser":
            if self.t == "Distributor":
                transaction_ref = "the Transaction"
            elif self.t == "StrategicSupplier":
                transaction_ref = "the proposed supply relationship"
            else:
                transaction_ref = "the proposed transaction"
            self.bp(f"{cl}.9 Entire Agreement. ", f"This LOI, together with any NDA referenced in Clause 6 (ALT-A), constitutes the entire agreement between the Parties in relation to its subject matter and supersedes all prior negotiations, representations, and agreements relating to {transaction_ref}. Nothing in this Clause limits liability for fraud.")
            self.bp(f"{cl}.10 Partnership Disclaimer. ", "Nothing in this LOI shall be construed as creating a partnership, joint venture, agency, or employment relationship between the Parties. Neither Party has authority to bind the other or to incur any obligation on the other's behalf.")
        else:
            self.bp(f"{cl}.9 Entire Agreement. ", "This LOI constitutes the entire agreement between the Parties in relation to its subject matter and supersedes all prior negotiations, representations, and agreements. Nothing in this Clause limits liability for fraud.")

    def signature(self):
        self.line()
        # v3.3: honours OPEN-1 (commit 2097f52) — bespoke_closing removed.
        # Operational near-signature content belongs in the letter body, not
        # the closing line. Hardcoded single-sentence closing matches main.
        # If choices.bespoke_closing is present in YAML, it is silently ignored
        # for backward compatibility.
        self.p("We look forward to working with you.")
        self.p("")
        self.p("Yours faithfully,")
        self.p("")

        prov = self.d.get("provider", {})
        self.p(f"For and on behalf of {prov.get('legal_name', '')}", bold=True)
        self.p(f"KvK: {prov.get('kvk', '')}")
        self.p("")
        self.p("Signature: ____________________________")
        self.p(f"Name: {prov.get('signatory_name', '')}")
        self.p(f"Title: {prov.get('signatory_title', '')}")
        self.p("Date: ____________________________")

        self.p("")
        self.line()
        self.p("")
        self.p("ACKNOWLEDGED AND AGREED:", bold=True)
        self.p("")

        cp = self.d.get("counterparty", {})
        self.p(f"For and on behalf of {cp.get('name', '')}", bold=True)
        rt = cp.get("reg_type", "")
        rn = cp.get("reg_number", "")
        if rt and rn:
            self.p(f"{rt}: {rn}")
        self.p("")
        self.p("Signature: ____________________________")
        self.p(f"Name: {cp.get('signatory_name', '')}")
        self.p(f"Title: {cp.get('signatory_title', '')}")
        self.p("Date: ____________________________")

    def schedule(self):
        # Schedule starts on its own page.
        # v3.2: schedule titles no longer carry "(NON-BINDING)" suffix. Italic
        # prefatory note carries the non-binding signal. Authoritative
        # binding/non-binding assignment lives in Cl. 5.1 / Cl. 8.1.
        self.doc.add_page_break()
        prefatory = ("This schedule expresses the Parties' current intentions "
                      "and is non-binding, in accordance with Clause 5.1.")
        if self.t == "Distributor":
            self.line()
            self.h("Schedule 1 \u2014 Partnership Details")
            self.p(prefatory, italic=True, color=GREY, size=FONT_SMALL)
            comm = self.d.get("commercial", {})
            self.table(
                ["Item", "Detail"],
                [
                    ["Partnership Mode", self.d.get("partnership_mode", "combined").title()],
                    ["Target Customer Segments", comm.get("target_segments", "")],
                    ["Geographic Scope", comm.get("territory", "")],
                    ["Estimated Annual Capacity", f"{comm.get('indicative_mw', '')} MW IT"],
                    ["Commercial scoping complete", f"{self.g('dates', 'loi_date')} + 30 days"],
                    ["Draft MSA issued", f"{self.g('dates', 'loi_date')} + 60 days"],
                    ["MSA executed", f"{self.g('dates', 'loi_date')} + 90 days"],
                ]
            )
        elif self.t == "StrategicSupplier":
            self.line()
            self.h("Schedule 1 \u2014 Scope and Capability Matrix")
            self.p(prefatory, italic=True, color=GREY, size=FONT_SMALL)
            supplier = self.d.get("supplier", {})
            purposes = supplier.get("strategic_purposes", [])
            rows = [
                ["Capability Category", supplier.get("capability_category", "")],
                ["Core Capability", supplier.get("core_capability", "")],
                ["Strategic Purposes", ", ".join(purposes)],
                ["Geographic Coverage", supplier.get("geographic_coverage", "")],
            ]
            if "capacity_lock_in" in purposes:
                rows.append(["Lead-Time Target", supplier.get("lead_time_target", "")])
            if "pricing_volume" in purposes:
                rows.append(["Indicative Volume", supplier.get("volume_indicative", "")])
            if "engineering_integration" in purposes:
                rows.append(["Joint IP Allocation", self.g("choices", "joint_ip", default="background")])
            rows += [
                ["Scoping complete", f"{self.g('dates', 'loi_date')} + 30 days"],
                ["Framework Agreement issued", f"{self.g('dates', 'loi_date')} + 60 days"],
                ["Framework Agreement executed", f"{self.g('dates', 'loi_date')} + 90 days"],
            ]
            self.table(["Item", "Detail"], rows)
        elif self.t == "Wholesale":
            self.line()
            self.h("Schedule 1 \u2014 Capacity and Technical Requirements")
            self.p(prefatory, italic=True, color=GREY, size=FONT_SMALL)
            comm = self.d.get("commercial", {})
            # v3.2: no DEC Block count; MW IT + Designated Sites only.
            self.table(
                ["Item", "Detail"],
                [
                    ["Indicative Capacity", f"{comm.get('indicative_mw', '')} MW IT"],
                    ["Designated Sites", "To be confirmed during technical scoping"],
                    ["GPU / Accelerator Type", "[To be confirmed during technical scoping]"],
                    ["Target Rack Density", "[To be confirmed]"],
                    ["Cooling Requirement", "Direct liquid cooling"],
                    ["Technical scoping complete", f"{self.g('dates', 'loi_date')} + 30 days"],
                    ["Credit assessment complete", f"{self.g('dates', 'loi_date')} + 30 days"],
                    ["Sales Order Form issued", f"{self.g('dates', 'loi_date')} + 60 days"],
                    ["MSA executed", f"{self.g('dates', 'loi_date')} + 90 days"],
                    ["Expansion Target", f"{comm.get('expansion_mw', '')} MW IT"],
                ]
            )
        else:  # EndUser
            self.line()
            self.h("Schedule 1 \u2014 Service Requirements")
            self.p(prefatory, italic=True, color=GREY, size=FONT_SMALL)
            comm = self.d.get("commercial", {})
            types = comm.get("service_type", [])
            type_str = ", ".join(t.replace("_", " ").title() for t in types)
            self.table(
                ["Item", "Detail"],
                [
                    ["Service Model", type_str],
                    ["Indicative Capacity", comm.get("indicative_capacity", "")],
                    ["GPU / Accelerator Type", "[To be confirmed during technical scoping]"],
                    ["Data Sovereignty", "[To be confirmed]"],
                    ["Technical scoping complete", f"{self.g('dates', 'loi_date')} + 30 days"],
                    ["Commercial proposal issued", f"{self.g('dates', 'loi_date')} + 60 days"],
                    ["MSA executed", f"{self.g('dates', 'loi_date')} + 90 days"],
                ]
            )

    def footer(self):
        # Real Word footers are set up in _setup(). Add version reference at end of body.
        self.p("")
        # v3.3: version string per-type. New types (SS, EP) are v1.0.
        version_by_type = {
            "EndUser": "v3.2",
            "Distributor": "v3.2",
            "Wholesale": "v3.2",
            "StrategicSupplier": "v1.0",
            "EcosystemPartnership": "v1.0",
        }
        vsn = version_by_type.get(self.t, "v3.2")
        self.p(
            f"DE-LOI-{self.t}-{vsn}",
            italic=True, size=FONT_SMALL, color=GREY
        )

    # ----- EP (Ecosystem Partnership) clause builders -----
    # v3.3: EP uses a dedicated, lighter structure. No Cl. 5 Project Finance,
    # no Cl. 7 NC. Cl. 5 is IP & Deliverables. Cl. 6 is Tier A mutual light
    # (7 sub-clauses). Cl. 7 is General (11 sub-clauses).

    def definitions_ep(self):
        self.h("1. Definitions")
        self.p("1.1 In this LOI, unless the context requires otherwise:")
        self.bp(
            '"Confidential Information" ',
            "means all information (whether technical, commercial, financial, or "
            "otherwise) disclosed by a Party to the other in connection with the "
            "Collaboration, whether in writing, orally, electronically, or by "
            "inspection, including any information that by its nature or the "
            "circumstances of disclosure would reasonably be understood to be "
            "confidential. The existence and contents of this LOI are Confidential "
            "Information."
        )
        self.bp(
            '"Collaboration" ',
            "means the ecosystem activities and joint work contemplated by this "
            "LOI as described in Clause 3."
        )
        self.bp(
            '"Representatives" ',
            "means, in relation to a Party, its Affiliates and its and their "
            "respective directors, officers, employees, agents, and professional "
            "advisers."
        )

    def clause2_ep(self):
        self.h("2. Purpose and Scope")
        eco = self.d.get("ecosystem", {})
        themes = ", ".join(eco.get("collaboration_themes", [])) or "[COLLABORATION_THEMES]"
        self.p(
            f"2.1 This LOI records the Parties' mutual interest in a "
            f"non-commercial ecosystem collaboration around {themes}."
        )
        self.p(
            "2.2 The collaboration is strictly non-commercial. No Party shall be "
            "entitled to any fee, payment, capacity, discount, or commercial "
            "benefit from the other Party by reason of this LOI or any activity "
            "under it."
        )
        self.p(
            "2.3 The commercial implications of any future activity \u2014 including "
            "any joint offering, research licensing, commercialisation of joint "
            "output, or provision of services by either Party to the other \u2014 shall "
            "be the subject of a separate agreement and are expressly outside the "
            "scope of this LOI."
        )
        self.p(
            "2.4 The confidentiality and general provisions in Clauses 6 and 7 "
            "are legally binding and enforceable from the date of execution. "
            "Clauses 3 through 5 are non-binding expressions of collaborative intent."
        )

    def clause3_ep(self):
        self.h("3. Collaboration Scope")
        eco = self.d.get("ecosystem", {})
        themes = eco.get("collaboration_themes", [])
        categories = eco.get("joint_activity_categories", [])

        self.bp("3.1 Collaboration Themes. ", "The Parties intend to collaborate on the following themes:")
        if themes:
            for theme in themes:
                self.p(f"\u2014 {theme}")
        else:
            self.p("\u2014 [THEMES TO BE CONFIRMED]")

        self.bp(
            "3.2 Joint Activity Categories. ",
            "Subject to resources and mutual agreement, the Parties intend to "
            "engage in one or more of the following categories of activity:"
        )
        if categories:
            cat_labels = {
                "publications": "publications (joint white papers, research articles, reports)",
                "events": "events (conferences, roundtables, workshops)",
                "pilots": "pilots (joint demonstrations, proofs of concept)",
                "advocacy": "advocacy (policy input, consultation responses)",
                "working_groups": "working groups (standards and technical coordination)",
            }
            for cat in categories:
                self.p(f"(\u2014) {cat_labels.get(cat, cat)}")
        else:
            self.p("\u2014 [ACTIVITY CATEGORIES TO BE CONFIRMED]")

        self.bp(
            "3.3 Governance and Cadence. ",
            "The Parties intend to establish a lightweight governance mechanism "
            "\u2014 typically an initial set-up meeting and quarterly check-ins \u2014 to "
            "review activity, align on priorities, and resolve any coordination "
            "issues. No binding governance structure is created by this LOI."
        )
        self.bp(
            "3.4 Working-Group Participation. ",
            "Where either Party hosts or convenes a working group relevant to the "
            "collaboration themes, the other Party shall have a standing "
            "invitation to participate on mutually agreed terms."
        )
        self.bp(
            "3.5 Non-Exclusivity. ",
            "The collaboration contemplated by this LOI is non-exclusive. Both "
            "Parties retain the right to enter into similar or competing "
            "collaborations with third parties."
        )

    def clause4_ep(self):
        self.h("4. Announcements and Branding")
        announcement = self.g("choices", "announcement_protocol", default="mutual_approval")
        logo_use = self.g("choices", "logo_use", default="reciprocal")

        if announcement == "notify_only":
            self.bp(
                "4.1 Announcement Protocol. ",
                "Each Party shall give the other Party reasonable prior notice "
                "(target: 5 Business Days) before making any public announcement "
                "referring to the collaboration. Consent is not required."
            )
        else:  # mutual_approval (default)
            self.bp(
                "4.1 Announcement Protocol. ",
                "Any public announcement, press release, published article, or "
                "social media post referring to the collaboration, the other "
                "Party, or joint activity under this LOI shall require the prior "
                "written consent of the other Party. Consent shall not be "
                "unreasonably withheld."
            )

        if logo_use == "none":
            self.bp(
                "4.2 Logo Use. ",
                "Neither Party shall use the other Party's name, logo, or trade "
                "mark in any public context without the prior written consent of "
                "the other Party."
            )
        elif logo_use == "one_way":
            self.bp(
                "4.2 Logo Use. ",
                "One-way logo use is contemplated between the Parties; the "
                "Party, scope, and terms will be specified in a separate "
                "schedule or letter."
            )
        else:  # reciprocal (default)
            self.bp(
                "4.2 Logo Use. ",
                "Each Party grants the other a limited, non-exclusive, revocable "
                "licence to use its name and logo solely in the context of the "
                "collaboration and subject to the branding guidelines each Party "
                "provides. No other use is permitted."
            )

        self.bp(
            "4.3 Attribution. ",
            "Where either Party refers to the collaboration in any public "
            "context, it shall: (a) describe the collaboration accurately and "
            "without overstatement; (b) refrain from implying any commercial "
            "relationship, endorsement, or joint venture; and (c) include the "
            "other Party's preferred attribution language when supplied."
        )

    def clause5_ep(self):
        self.h("5. Intellectual Property and Deliverables")
        self.bp(
            "5.1 Background IP. ",
            "Each Party retains all right, title, and interest in its background "
            "intellectual property. Nothing in this LOI transfers or licenses any "
            "intellectual property between the Parties except as expressly set "
            "out in Clause 4.2."
        )
        self.bp(
            "5.2 Joint Deliverables. ",
            "Any intellectual property jointly developed by the Parties in the "
            "course of the collaboration (including joint publications, "
            "working-group outputs, and jointly authored materials) shall be "
            "governed by a separate agreement to be executed before the joint "
            "activity produces any material output."
        )
        self.bp(
            "5.3 No Assignment by Participation. ",
            "Nothing in this LOI or in any activity conducted under it shall be "
            "construed as an assignment, licence, or transfer of intellectual "
            "property."
        )
        self.bp(
            "5.4 Publication. ",
            "Each Party retains the right to publish, present, and disseminate "
            "its own work, subject to the confidentiality provisions in Clause 6."
        )

    def clause6_ep(self):
        self.h("6. Confidentiality (BINDING)")
        surv = self.g("protection", "confidentiality_survival", default="2 years")
        self.p(
            "6.1 Each Party shall keep confidential all Confidential Information "
            "received from the other Party and shall use such information solely "
            "for the Collaboration."
        )
        self.p(
            "6.2 Each Party may disclose Confidential Information only to its "
            "Representatives who have a genuine need to know for the "
            "Collaboration and who are bound by confidentiality obligations no "
            "less restrictive than this Clause 6."
        )
        self.p(
            "6.3 The obligations in Clauses 6.1 and 6.2 do not apply to "
            "information that the receiving Party can demonstrate: (a) is or "
            "becomes publicly available through no fault of the receiving Party; "
            "(b) was already in the receiving Party's possession without "
            "restriction; (c) was independently developed without use of the "
            "Confidential Information; or (d) was received from a third party "
            "without breach of any confidentiality obligation."
        )
        self.p(
            "6.4 A Party may disclose Confidential Information to the extent "
            "required by applicable law, regulation, or court order, provided "
            "that (where legally permitted) the disclosing Party gives the other "
            "Party prior written notice and discloses only the minimum required."
        )
        self.p(
            "6.5 Upon written request or expiry of this LOI, the receiving Party "
            "shall promptly return or destroy all Confidential Information and "
            "certify such return or destruction in writing. Copies required by "
            "applicable law or internal compliance policies may be retained, "
            "subject to continued confidentiality."
        )
        self.p(
            "6.6 Public statements about this LOI are governed by Clause 4."
        )
        self.p(
            f"6.7 The obligations in this Clause 6 shall survive for {surv} from "
            f"the date of termination or expiry of this LOI."
        )

    def clause7_ep_general(self):
        self.h("7. General Provisions (BINDING)")
        val_date = self.g("dates", "validity_date") or "[12 months from LOI date]"

        self.bp("7.1 Non-Binding Status. ", "")
        self.p(
            "(a) Non-binding provisions. Clauses 2, 3, 4, and 5 of this LOI are "
            "non-binding expressions of collaborative intent."
        )
        self.p(
            "(b) Binding provisions. Clauses 6 (Confidentiality) and 7 (General "
            "Provisions) are legally binding and enforceable obligations."
        )
        self.bp(
            "7.2 No Commercial Commitment. ",
            "Nothing in this LOI creates any obligation on either Party to pay, "
            "purchase, supply, or grant anything of commercial value to the "
            "other. Any such arrangement requires a separate agreement."
        )
        self.bp(
            "7.3 Non-Exclusivity. ",
            "As per Clause 3.5."
        )
        self.bp(
            "7.4 Term and Validity. ",
            f"This LOI shall remain valid until {val_date}, after which it shall "
            f"lapse automatically unless extended by mutual written agreement. "
            f"Upon lapse, Clause 6 (Confidentiality) shall survive for its "
            f"stated period."
        )
        self.bp(
            "7.5 Costs. ",
            "Each Party shall bear its own costs in connection with this LOI "
            "and the Collaboration."
        )
        self.bp(
            "7.6 Counterparts. ",
            "This LOI may be executed in counterparts, including by electronic "
            "signature within the meaning of the eIDAS Regulation (EU) No 910/2014."
        )
        self.bp(
            "7.7 Notices. ",
            "All notices under this LOI shall be in writing (including email) "
            "and addressed to the contact details in the preamble. A notice is "
            "effective upon receipt."
        )
        self.bp(
            "7.8 Governing Law. ",
            "This LOI shall be governed by the laws of the Netherlands. The "
            "United Nations Convention on Contracts for the International Sale "
            "of Goods (CISG) is expressly excluded."
        )
        self.bp(
            "7.9 Jurisdiction. ",
            "The courts of Amsterdam (Rechtbank Amsterdam) shall have exclusive "
            "jurisdiction over any dispute arising out of or in connection with "
            "the binding provisions of this LOI."
        )
        self.bp(
            "7.10 Entire Agreement. ",
            "This LOI constitutes the entire agreement between the Parties in "
            "relation to its subject matter and supersedes all prior "
            "negotiations, representations, and agreements. Nothing in this "
            "Clause limits liability for fraud."
        )
        self.bp(
            "7.11 Partnership Disclaimer. ",
            "Nothing in this LOI shall be construed as creating a partnership, "
            "joint venture, agency, or employment relationship between the "
            "Parties. Neither Party has authority to bind the other or to incur "
            "any obligation on the other's behalf."
        )

    def schedule_ep(self):
        """v3.3: Optional Joint Activity Plan schedule for EP.
        Only rendered if intake provides ecosystem.joint_activity_plan (list of
        dicts with keys: activity, category, lead, target_date).
        """
        plan = self.d.get("ecosystem", {}).get("joint_activity_plan", [])
        if not plan:
            return
        self.doc.add_page_break()
        self.line()
        self.h("Schedule 1 \u2014 Joint Activity Plan")
        self.p(
            "This schedule expresses the Parties' current intentions and is "
            "non-binding, in accordance with Clause 2.4.",
            italic=True, color=GREY, size=FONT_SMALL,
        )
        rows = []
        for item in plan:
            rows.append([
                item.get("activity", ""),
                item.get("category", ""),
                item.get("lead", ""),
                item.get("target_date", ""),
            ])
        self.table(["Activity", "Category", "Lead", "Target Date"], rows)

    def build(self) -> Document:
        # v3.3: EP uses its own clause builders (will be added next); until wired,
        # fall back to partial engine output.
        if self.t == "EcosystemPartnership":
            return self._build_ep()

        self.letterhead()
        # add_cover() already ends with page break
        self.recitals()
        self.definitions()
        self.clause2()

        if self.t == "Distributor":
            self.clause3_ds()
        elif self.t == "Wholesale":
            self.clause3_ws()
        elif self.t == "StrategicSupplier":
            self.clause3_ss()
        else:
            self.clause3_eu()

        if self.t == "StrategicSupplier":
            self.clause4_ss()
        else:
            self.clause4()

        self.clause5()
        self.clause6()
        self.clause7_nc()
        self.clause_general()
        self.signature()
        self.schedule()
        self.footer()
        return self.doc

    def _build_ep(self) -> Document:
        """v3.3: Ecosystem Partnership build pipeline.
        Different structure: no Cl. 5 Project Finance, no Cl. 7 NC.
        Cl. 5 is IP & Deliverables, Cl. 6 is Tier A light mutual, Cl. 7 is General.
        """
        self.letterhead()
        self.recitals()
        self.definitions_ep()
        self.clause2_ep()
        self.clause3_ep()
        self.clause4_ep()
        self.clause5_ep()
        self.clause6_ep()
        self.clause7_ep_general()
        self.signature()
        # Schedule 1 is optional for EP — only rendered if the intake provides one.
        if self.d.get("ecosystem", {}).get("joint_activity_plan"):
            self.schedule_ep()
        self.footer()
        return self.doc


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

import re  # noqa: E402 — used below by qa_lint


# v3.2 QA linter. Rules in sync with _shared/loi-qa-gate.md.

_ARROW_CHARS = "\u2192\u21D2\u279C\u27F6\u21A6\u27F9\u21E8"

_FAIL_RULES = {
    "R-1": (r"minimum commitment term of 5 years", "body",
            "'minimum commitment term of 5 years' banned; use 'approximately 5 years, indicative only'"),
    "R-2": (r"\b\d+\s+identified\s+sites\b", "Recital A",
            "Fixed site-count language in Recital A"),
    "R-3": (r"12 months of commercial commitment", "Recital A",
            "'12 months of commercial commitment' banned in Recital A"),
    "R-5": (r"We are confident that", "closing",
            "'We are confident that' banned"),
    "R-7": (f"[{_ARROW_CHARS}]", "body",
            "Unicode arrow detected in body"),
    "R-8": (r"Schedule \d+ [^\n]*\(NON-BINDING\)", "schedule-title",
            "'(NON-BINDING)' suffix in schedule title — use italic prefatory note instead"),
    "R-10": (r"4\.2 Revenue Chain", "Cl. 4.2",
             "Cl. 4.2 heading must be 'Contractual Sequence', not 'Revenue Chain'"),
    "R-20": (r"programme spans \d+", "Recital A",
             "'programme spans N...' language regression"),
}

_WARN_RULES = {
    "R-11": (r"\bISO \d{4,5}\b", "Recital B",
             "ISO certification in Recital B (set choices.cert_relevant=true to suppress)"),
    "R-14": (r"\b(leading|innovative|cutting-edge|world-class|best-in-class)\b", "Recital B",
             "Salesy adjective in Recital B"),
    "R-15": (r"positioning (its|itself) as", "body",
             "'positioning (its|itself) as' — formulaic"),
    "R-19": (r"^\s*\d+(?:\.\d+)?\s+[^\n]*\(NON-BINDING\)", "heading",
             "'(NON-BINDING)' in a clause heading — v3.2 style regression"),
}


def _extract_text(doc) -> str:
    """Extract all paragraph text from a python-docx Document, including tables."""
    lines = []
    for p in doc.paragraphs:
        lines.append(p.text)
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    lines.append(p.text)
    return "\n".join(lines)


def qa_lint(doc, data: dict, builder_findings: list, overrides: set,
            override_reason: str):
    """Run QA rules over the built Document. Returns (status, report_lines).

    status: "PASS" | "PASS_WITH_WARN" | "FAIL"
    """
    text = _extract_text(doc)
    lines = [
        "LOI QA Report",
        f"Counterparty: {data.get('counterparty', {}).get('short', 'Unknown')}",
        f"Generated: {datetime.now().isoformat()}Z",
        f"Variant: programme.recital_a_variant={data.get('programme', {}).get('recital_a_variant', 'default')}",
        f"Overrides: {','.join(sorted(overrides)) if overrides else 'none'}",
    ]
    if override_reason:
        lines.append(f"Override reason: {override_reason}")
    lines.append("")
    lines.append("Findings:")

    fail_count = 0
    warn_count = 0

    for rule, scope, msg in builder_findings:
        if rule in overrides:
            lines.append(f"  [OVRD] {rule}  {scope}   {msg}")
        else:
            lines.append(f"  [FAIL] {rule}  {scope}   {msg}")
            fail_count += 1

    for rid, (pattern, scope, msg) in _FAIL_RULES.items():
        if re.search(pattern, text, re.MULTILINE):
            if rid in overrides:
                lines.append(f"  [OVRD] {rid}  {scope}   {msg}")
            else:
                lines.append(f"  [FAIL] {rid}  {scope}   {msg}")
                fail_count += 1

    for rid, (pattern, scope, msg) in _WARN_RULES.items():
        if re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
            if rid == "R-11" and data.get("choices", {}).get("cert_relevant"):
                continue
            lines.append(f"  [WARN] {rid}  {scope}   {msg}")
            warn_count += 1

    if not data.get("programme", {}).get("recital_a_variant"):
        lines.append("  [INFO] R-16  YAML   Recital A variant not set, used 'default'")
    if not data.get("choices", {}).get("bespoke_closing"):
        lines.append("  [INFO] R-17  YAML   No bespoke_closing, used default single-sentence")

    lines.append("")
    if fail_count > 0:
        status = "FAIL"
    elif warn_count > 0:
        status = "PASS_WITH_WARN"
    else:
        status = "PASS"
    lines.append(f"Status: {status} (warnings: {warn_count}, failures: {fail_count})")
    return status, lines


def _parse_arg(flag: str) -> str:
    if flag in sys.argv:
        idx = sys.argv.index(flag)
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_loi.py <intake.yaml>")
        print("  [--output path.docx]")
        print("  [--override R-11,R-14]")
        print("  [--override-reason \"...\"]")
        sys.exit(1)

    data = load_intake(sys.argv[1])

    override_str = _parse_arg("--override")
    if override_str:
        data["_overrides"] = [r.strip() for r in override_str.split(",") if r.strip()]
    override_reason = _parse_arg("--override-reason")
    if override_reason:
        data["_override_reason"] = override_reason

    output = _parse_arg("--output")

    if not output:
        loi_date = data.get("dates", {}).get("loi_date", "")
        try:
            dt = datetime.strptime(loi_date, "%d %B %Y")
            date_str = dt.strftime("%Y%m%d")
        except ValueError:
            date_str = datetime.now().strftime("%Y%m%d")
        cp = data.get("counterparty", {}).get("short", "Unknown")
        output = f"{date_str}_DEG_LOI-{data['type']}_{cp}_(DRAFT).docx"

    loi = LOI(data)
    doc = loi.build()

    qa_report_path = output.replace(".docx", "_qa.txt")
    qa_status, qa_lines = qa_lint(doc, data, loi.qa_findings, loi.overrides,
                                   loi.override_reason)
    with open(qa_report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(qa_lines) + "\n")

    if qa_status == "FAIL":
        print("QA FAIL — build blocked. Findings:")
        for line in qa_lines:
            if "[FAIL]" in line:
                print(f"  {line}")
        print(f"\nFull QA report: {qa_report_path}")
        print("To override: --override R-xx,R-yy --override-reason \"...\"")
        sys.exit(2)

    doc.save(output)

    print(f"Generated: {output}")
    print(f"Type: DE-LOI-{data['type']}-v3.2")
    print(f"Counterparty: {data.get('counterparty', {}).get('name', 'Unknown')}")
    print(f"QA: {qa_status} ({qa_report_path})")
    print(f"Clauses: ALL (full document)")


if __name__ == "__main__":
    main()
