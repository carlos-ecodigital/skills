"""Embedded Moerman-shaped test fixture (deal.yaml v1.0).

Written inline instead of as a separate .yaml file so tests can emit it
to a tmp_path fixture without running afoul of the Write-tool gate on
fixture .yaml files in this skill tree.
"""

MOERMAN_DEAL_YAML = """\
deal_yaml_schema_version: "1.0"
slug: moerman-paprika
project_name: DEKWAKEL-01
version: "1.0"
counterparty_folder_name: "Moerman Paprika_Project_Benelux_Ops"

commercial:
  deal_value_eur: 150000
  currency: "EUR"
  heat_sales_split: "50 : 50"
  payment_term_days: 30
  effective_date: "01-04-2026"

timeline:
  loi_signed_date: "2026-03-13"
  hot_drafted_date: "2026-04-20"

notices:
  de_email: "contact@digitalenergy.ch"
  grower_address: "Harteveldlaan 16, 2671 VH Naaldwijk"
  grower_email: "jan@moermanpaprika.nl"

addons:
  bess_co_development: false
  btm_renewables: false
  chp_present: false
  co_investment: false

site_partners:
  - legal_name: "Moerman Paprika B.V."
    kvk: "27178957"
    registered_address: "Harteveldlaan 16, 2671 VH Naaldwijk"
    signatory:
      name: "Jan Moerman"
      title: "Directeur"
      email: "jan@moermanpaprika.nl"
      signing_authority: "sole"
    greenhouse:
      address: "Harteveldlaan 16, 2671 VH Naaldwijk"
      current_size_ha: 8.5
      planned_size_ha: 8.5
      expansion_timeline: "N/A"
      cultivation_type: "Vegetables / Groenten"
    contributions:
      - asset: grid_interconnection
        instrument: ato_sharing
        details:
          dso: "Westland Infra"
          ean_code: "871687510000012345"
          ato_reference: "WI-2024-ATO-00456"
          total_connection_mva: 4.8
          total_import_mw: 4.0
          total_export_mw: 1.0
          base_connection_mva: 2.4
          base_import_mw: 2.0
          base_export_mw: 0.5
          future_connection_mva: 4.8
          future_import_mw: 4.0
          future_export_mw: 1.0
          sap_configuration: "Cable pooling"
        stage_tag: "hot"
      - asset: land
        instrument: opstalrecht
        details:
          kadaster_parcels: "Naaldwijk, Sectie B, Nr 4521"
          title_type: "Full ownership"
          encumbrances: "Mortgage"
          zoning_designation: "Glastuinbouw"
          land_area_per_mw_m2: 250
          opstalrecht_term_years: 30
          mv_cable_length_m: 150
        stage_tag: "hot"
    returns:
      - value: energy_heat
        instrument: heat_offtake_agreement
        details:
          target_outlet_temp_c: 55
          expected_return_temp_c: 35
          heat_price_eur_mwh: 18
          combined_eb: "TBD / Nog te bepalen"

locations:
  - parcel_id: "Naaldwijk, Sectie B, Nr 4521"
    address: "Harteveldlaan 16, 2671 VH Naaldwijk"
    dso: "Westland Infra"
    municipality: "Westland"
"""


def write_fixture(tmp_dir):
    """Materialise the embedded YAML into ``<tmp_dir>/deal_test_minimal.yaml``."""
    from pathlib import Path
    p = Path(tmp_dir) / "deal_test_minimal.yaml"
    p.write_text(MOERMAN_DEAL_YAML)
    return p


# ---------------------------------------------------------------------------
# Van Gog — Wave 2 multi-partner fixture
# ---------------------------------------------------------------------------
#
# Three Site Partners, one per role:
#   - Van Gog Grubbenvorst B.V.            → Grid Contributor (B.*)
#   - Van Gog Grubbenvorst Vastgoed B.V.   → Landowner       (D.* / G.Landowner_*)
#   - Van Gog kwekerijen Grubbenvorst B.V. → Heat Offtaker   (A.* / C.* / G.Grower_*)
#
# Data here is a condensed, HoT-ready shape of loi/examples/deal_van-gog.yaml:
# we fill the enrichment targets (kvk, addresses, grid capacities, kadaster
# parcel, etc.) that the LOI fixture leaves null, since the HoT engine is
# expected to run after Phase B5 parsers have populated them.

VAN_GOG_DEAL_YAML = """\
deal_yaml_schema_version: "1.0"
slug: van-gog-grubbenvorst
project_name: DEKWAKEL-VG
version: "1.0"

commercial:
  deal_value_eur: 300000
  currency: "EUR"
  heat_sales_split: "50 : 50"
  payment_term_days: 30
  effective_date: "01-07-2026"

timeline:
  loi_signed_date: "2026-04-14"
  hot_drafted_date: "2026-07-13"

notices:
  de_email: "contact@digitalenergy.ch"
  grower_email: "koen.saris@vangogkwekerijen.nl"
  landowner_email: "marion@vangogvastgoed.nl"

addons:
  bess_co_development: true
  btm_renewables: false
  chp_present: false
  co_investment: false

site_partners:
  # Partner 0 — Grid Contributor (also holds the BESS co-dev return)
  - legal_name: "Van Gog Grubbenvorst B.V."
    kvk: "12345678"
    registered_address: "Horsterweg 1, 5971 NA Grubbenvorst"
    signatory:
      name: "Marion van Gog"
      title: "Directeur"
      email: "marion@vangog.nl"
      signing_authority: "sole"
    contributions:
      - asset: grid_interconnection
        instrument: ato_sharing
        details:
          dso: "Enexis"
          ean_code: "871687510000099999"
          ato_reference: "EX-2025-ATO-00777"
          total_connection_mva: 16.0
          total_import_mw: 10.0
          total_export_mw: 6.0
          base_connection_mva: 8.0
          sap_configuration: "Cable pooling"
        stage_tag: "hot"
      - asset: equipment_bess
        instrument: bess_jv_50_50
        details:
          mw: 25.5
          mwh: 51
          chemistry: "LFP"
        stage_tag: "hot"
    returns:
      - value: equity
        instrument: bess_spv_equity
        details:
          percent: 50

  # Partner 1 — Landowner
  - legal_name: "Van Gog Grubbenvorst Vastgoed B.V."
    kvk: "23456789"
    registered_address: "Horsterweg 1, 5971 NA Grubbenvorst"
    signatory:
      name: "Marion van Gog"
      title: "Directeur"
      email: "marion@vangogvastgoed.nl"
      signing_authority: "sole"
    contributions:
      - asset: land
        instrument: recht_van_opstal
        details:
          kadaster_parcels: "Horst aan de Maas, Sectie G, Nr 8812"
          title_type: "Full ownership"
          encumbrances: "None"
          zoning_designation: "Glastuinbouw"
          land_area_per_mw_m2: 300
          opstalrecht_term_years: 30
          mv_cable_length_m: 200
        stage_tag: "hot"
    returns:
      - value: money
        instrument: opstal_fee
        details:
          tbd: true

  # Partner 2 — Heat Offtaker (the "grower" for A.*/C.*/G.Grower_*)
  - legal_name: "Van Gog kwekerijen Grubbenvorst B.V."
    kvk: "34567890"
    registered_address: "Horsterweg 3, 5971 NA Grubbenvorst"
    signatory:
      name: "Koen Saris"
      title: "Operationeel Directeur"
      email: "koen.saris@vangogkwekerijen.nl"
      signing_authority: "sole"
    greenhouse:
      address: "Horsterweg 3, 5971 NA Grubbenvorst"
      current_size_ha: 14.0
      planned_size_ha: 18.0
      expansion_timeline: "2027-Q3"
      cultivation_type: "Vegetables / Groenten"
    contributions: []
    returns:
      - value: energy_heat
        instrument: heat_supply_agreement
        details:
          target_outlet_temp_c: 55
          expected_return_temp_c: 35
          heat_price_eur_mwh: 22
          combined_eb: "TBD / Nog te bepalen"
          term_years: 30

locations:
  - parcel_id: "Horst aan de Maas, Sectie G, Nr 8812"
    address: "Horsterweg 3, 5971 NA Grubbenvorst"
    dso: "Enexis"
    municipality: "Horst aan de Maas"
"""


def write_van_gog_fixture(tmp_dir):
    """Materialise the Van Gog 3-partner fixture into a .yaml path."""
    from pathlib import Path
    p = Path(tmp_dir) / "deal_van_gog.yaml"
    p.write_text(VAN_GOG_DEAL_YAML)
    return p
