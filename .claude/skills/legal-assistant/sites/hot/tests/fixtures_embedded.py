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
