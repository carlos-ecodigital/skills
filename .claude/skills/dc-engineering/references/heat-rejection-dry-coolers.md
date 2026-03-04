# Heat Rejection & Dry Cooler Systems for AI Data Centers

## 1. Heat Rejection in the Netherlands Context

### Climate Advantage
The Netherlands offers one of Europe's best climates for data center free cooling:
- **Annual average temperature:** 10.5°C (De Bilt, KNMI)
- **Design summer peak:** 33-35°C (T_wet bulb 21-23°C)
- **Hours below 15°C:** ~5,500-6,000 hours/year
- **Hours below 20°C:** ~7,000 hours/year
- **Free cooling potential:** With 35°C facility water return, mechanical cooling needed only ~1,500-2,500 hours/year

### Heat Rejection Budget for DEC
For a 40 MW IT load AI factory with 80% liquid cooling capture:
- **32 MW** captured by liquid cooling → feeds heat pump / heat recovery system
- **8 MW** residual air cooling → must be rejected via dry coolers or adiabatic systems
- **Plus heat pump condenser rejection:** If heat pump COP = 4.0, then for 32 MW source: 32 × (1 + 1/4) = 40 MW total condenser output. Of this, greenhouse absorbs heat demand (variable by season); surplus must be rejected.
- **Summer peak:** Greenhouse heat demand near zero → nearly all thermal output must be rejected

## 2. Technology Options

### Dry Coolers (Droge Koelers)
Finned-tube heat exchangers with fans. No water consumption. Heat rejected to ambient air.

**Advantages:**
- Zero water consumption (critical for NL water policy)
- No Legionella risk (no water contact with air)
- Low maintenance
- Simple permitting

**Disadvantages:**
- Performance degrades at high ambient temperatures
- Large footprint
- Significant fan noise (dominant noise source for DC facilities)
- Limited to ~5°C approach to ambient dry bulb

**Key Vendors:**
- **Güntner:** V-shape dry coolers (GFD/GFH series). Market leader in Europe. Best balance of capacity/footprint/noise. V-shape configuration reduces footprint 40% vs flat. German engineering, strong NL distribution.
- **Alfa Laval:** Flat and V-shape models. Strong in industrial applications. Good NL presence.
- **Kelvion (formerly GEA Heat Exchangers):** Industrial heritage. Competitive on large custom units.
- **Lu-Ve (Searle):** Italian manufacturer. Competitive pricing, good quality for standard sizes.

### Adiabatic Dry Coolers (Adiabatische Droge Koelers)
Dry coolers with adiabatic pre-cooling pads. Water sprayed on pads evaporates, pre-cooling the air entering the finned coil. Combines dry cooler simplicity with evaporative boost during peak.

**Advantages:**
- Best of both worlds: dry cooling 80%+ of hours, adiabatic boost during summer peaks
- 85-95% water savings compared to open cooling towers
- No Legionella risk (water doesn't contact recirculating loop)
- NL annual water consumption: 50-150 m3 per MW rejected (vs 2,000-4,000 m3 for open tower)
- Approaches wet bulb temperature during adiabatic operation

**Disadvantages:**
- Higher capital cost than pure dry coolers (+20-30%)
- Water treatment for adiabatic pads (mineral buildup)
- Pad replacement every 3-5 years
- Still noisy (fans same as dry coolers)

**Key Vendors:**
- **Güntner:** GFD with Hydrospray adiabatic module. Integrated system, factory-tested.
- **Baltimore Aircoil Company (BAC):** TrilliumSeries adiabatic cooler. Strong in mission-critical sector.
- **Evapco:** AT series. Good performance, competitive.
- **EcoBreeze (Schneider Electric):** Indirect evaporative cooling module. Designed specifically for DC.

### Open Cooling Towers (Koeltorens)
Evaporative cooling: water directly contacts air stream. Highest cooling efficiency but highest water consumption and Legionella risk.

**Advantages:**
- Highest capacity per unit footprint
- Approaches wet bulb temperature (21-23°C design in NL)
- Lower capital cost per kW than adiabatic

**Disadvantages:**
- Legionella liability (ISSO 55.3 compliance mandatory in NL)
- High water consumption (3,000-5,000 m3/year per MW)
- Water treatment chemicals
- Drift eliminators required
- NL provincial regulations may restrict cooling towers near woongebieden (residential areas)
- Bi-annual Legionella sampling, legionellabeheersplan (Legionella management plan) required

**DEC Position: NOT RECOMMENDED for primary heat rejection.** Legionella compliance burden and water consumption conflict with sustainability messaging and permitting simplicity. Use adiabatic dry coolers instead.

### Plate Heat Exchangers (PHE) for Free Cooling
Not a heat rejection system per se, but a critical component: plate HX enables direct free cooling bypass — when ambient temperature is low enough, facility water is cooled directly through PHX without running compressor or mechanical cooling.

**Key Vendors:**
- **Alfa Laval:** Market leader. M-series gasketed plate HX for HVAC. Well-established NL presence.
- **SWEP (Alfa Laval subsidiary):** Brazed plate HX for smaller applications.
- **Kelvion:** Competitive alternative.

**DEC Application:** A €50-100K plate HX installation can handle 70%+ of annual cooling hours in NL climate, avoiding compressor energy. This is the single highest-ROI energy efficiency measure in the thermal plant.

## 3. Legionella Compliance (NL-Specific)

### ISSO 55.3 (Legionellapreventie in Luchtwassers en Watergekoelde Koelinstallaties)
- Applies to ALL cooling systems where water contacts air (cooling towers, adiabatic coolers with recirculating water)
- Legionellabeheersplan (Legionella management plan) mandatory
- Bi-annual water sampling at minimum
- Temperature control: maintain water >60°C or <25°C (irrelevant for DC cooling)
- Chemical treatment or UV disinfection
- Drift eliminator maintenance
- Reporting to GGD (Gemeentelijke Gezondheidsdienst / Municipal Health Service)

### DEC Advantage of Adiabatic over Open Tower
Adiabatic dry coolers with fresh-water-spray-on-pad design (no recirculating water reservoir) have significantly reduced Legionella risk profile. Some designs are classified as "niet-legionellaplichtig" (not subject to Legionella obligation) if:
- Water is mains-supplied (no recirculation)
- No water reservoir >300 liters
- No aerosol generation into occupied spaces
- Consult with OD (Omgevingsdienst) on specific classification

## 4. Free Cooling Optimization

### NL Free Cooling Hours
Based on KNMI De Bilt weather data and 35°C facility return water:

| Cooling Mode | Hours/Year | % of Year | Conditions |
|---|---|---|---|
| Full free cooling (PHX only) | 4,500-5,500 | 51-63% | Ambient < 25°C |
| Partial free cooling (PHX + trim) | 1,500-2,000 | 17-23% | Ambient 25-30°C |
| Mechanical/adiabatic cooling | 1,200-2,000 | 14-23% | Ambient > 30°C |

### Annual Energy Savings
- PUE contribution of cooling: 0.03-0.08 (vs 0.20-0.40 for air-cooled traditional DC)
- Annual cooling energy: 50-100 kWh/kW IT (vs 400-800 kWh/kW for air-cooled)
- At €0.10/kWh and 40 MW IT: cooling energy cost €200K-400K/year (vs €1.6M-3.2M for air-cooled)

## 5. Noise Considerations

### Dry Coolers as Dominant Noise Source
Dry coolers and adiabatic coolers are typically the loudest outdoor equipment at a data center:
- Single large unit (e.g., Güntner GFD 065): 82-88 dB(A) at 1 m, full fan speed
- Array of 20-40 units for 40 MW facility: cumulative noise significant
- Low-frequency content from large axial fans travels further than high-frequency

### Bal Geluidhinder (Noise Nuisance) Limits
At nearest gevoelig gebouw (sensitive building, e.g., woning / residence):
- **Dag (day, 07-19):** LAr,LT ≤ 50 dB(A)
- **Avond (evening, 19-23):** LAr,LT ≤ 45 dB(A)
- **Nacht (night, 23-07):** LAr,LT ≤ 40 dB(A)

### Mitigation Strategies
- **Fan speed control:** Variable-speed drives (VFD/VSD) reduce speed and noise at partial load — most hours in NL
- **Low-noise fan selection:** EC fans with optimized blade geometry
- **Setback distance:** Every doubling of distance reduces noise ~6 dB(A)
- **Geluidschermen (noise barriers):** Absorptive barriers (Heblad, Van Campen) can achieve 10-15 dB(A) reduction
- **Equipment orientation:** Direct noise away from sensitive receptors
- **Nighttime fan speed caps:** Accept slightly higher facility water temperature at night to reduce fan noise

See [acoustic-engineering.md](acoustic-engineering.md) for detailed noise modeling methodology.

## 6. DEC Design Recommendations

### Primary System: Adiabatic Dry Coolers
- Güntner GFD V-shape with Hydrospray adiabatic pre-cooling
- N+1 redundancy (e.g., 9+1 units for 8 MW residual rejection)
- VFD on all fans for noise and energy optimization
- Low-noise EC fan option (adds ~10% capital cost, saves significant noise compliance cost)

### Free Cooling Bypass: Plate Heat Exchanger
- Alfa Laval M-series gasketed plate HX
- Sized for 80% of annual hours (full free cooling below 25°C ambient)
- Automatic changeover valve between free cooling and mechanical cooling paths

### Heat Pump Rejection: Dedicated Dry Coolers
- For summer surplus heat when greenhouse demand is zero
- Separate from IT residual cooling loop (different temperature regime)
- Can be identical equipment type but on separate hydraulic circuit

## Cross-References
- See [liquid-cooling-systems.md](liquid-cooling-systems.md) for CDU output temperatures feeding heat rejection
- See [heat-pumps-waste-heat.md](heat-pumps-waste-heat.md) for heat pump condenser rejection needs
- See [acoustic-engineering.md](acoustic-engineering.md) for noise modeling and barrier design
- See companion skill `netherlands-permitting` for Bal geluidhinder and Legionella permitting
