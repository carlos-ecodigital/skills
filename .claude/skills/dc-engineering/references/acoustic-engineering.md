# Acoustic Engineering for Data Centers in the Netherlands

## 1. Why Acoustics is a Permit-Killer

### The Dutch Context
The Netherlands has some of the strictest environmental noise regulations in Europe. Under the Omgevingswet (Environment and Planning Act), industrial noise (industrielawaai) from data centers — specifically dry coolers, generators, transformers, and HVAC — is subject to quantitative limits at the nearest gevoelig gebouw (sensitive building / receptor).

**The problem for DEC:** Data centers co-located with greenhouses are typically in mixed agricultural/rural zones where ambient noise is low (30-35 dB(A) at night) and the nearest woning (dwelling) may be 200-500 m away. Acoustic design determines whether the omgevingsvergunning (environmental permit) is granted or refused. Without a competent geluidadviseur (acoustic advisor), gemeente (municipality) rejects the permit application on acoustic grounds post-design — forcing expensive retrofits or project abandonment.

### The Cost of Getting It Wrong
- Geluidscherm (noise barrier): €500-€2,000 per linear meter, 3-6 m high
- Attenuated dry cooler: €30,000-€80,000 per unit (vs €15,000-€40,000 without attenuation)
- Low-noise generators: 30-50% premium over standard units
- Project delay: 3-6 months for acoustic redesign and permit resubmission
- **Design-stage acoustic modeling costs €15,000-€40,000 — a fraction of retrofit costs**

## 2. Dutch Noise Regulations Under Omgevingswet

### Bal (Besluit activiteiten leefomgeving — Activities Decree)

**Article 4.17-4.21: Geluid door activiteiten (Noise from Activities)**

Applicable if the facility is a milieubelastende activiteit (environmentally impactful activity) — which all data centers are.

**Standaard geluidnormen (Standard Noise Limits) per Bal:**

| Period | Limit at Gevoelig Gebouw (Sensitive Building) | Notes |
|---|---|---|
| Dag (Day): 07:00-19:00 | 50 dB(A) LAr,LT | Rated sound level, long-term average |
| Avond (Evening): 19:00-23:00 | 45 dB(A) LAr,LT | 5 dB stricter than day |
| Nacht (Night): 23:00-07:00 | 40 dB(A) LAr,LT | **THE binding constraint** for 24/7 DC operations |

**Piekgeluid (Peak Sound Level):**

| Period | Limit at Gevoelig Gebouw | Notes |
|---|---|---|
| Dag | 70 dB(A) LAmax | Single event maximum |
| Avond | 65 dB(A) LAmax | |
| Nacht | 60 dB(A) LAmax | Generator start = peak event |

**Key Terms:**
- **LAr,LT (Langtijdgemiddeld Beoordelingsniveau — Long-term Average Rated Sound Level):** Time-averaged sound level including tonality and impulse corrections, per Handleiding Meten en Rekenen Industrielawaai (HMRI)
- **Gevoelig gebouw (Sensitive Building):** Woningen (dwellings), scholen (schools), ziekenhuizen (hospitals), verzorgingstehuizen (care homes). Greenhouses (kassen) are NOT gevoelige gebouwen — but greenhouse worker rest areas (personeelsruimten) might be
- **Maatwerkvoorschrift (Custom Rule):** Gemeente can set stricter OR more lenient limits than Bal standard via maatwerkvoorschrift. In noise-sensitive areas, expect stricter. In industrial zones (bedrijventerrein), expect standard or more lenient

### Bkl (Besluit kwaliteit leefomgeving — Environmental Quality Decree)

**Omgevingswaarden geluid (Environmental Quality Standards for Noise):**
- Sets maximum acceptable noise level at facades of gevoelige gebouwen from all sources combined
- Relevant when cumulative noise from DC + other industrial sources may exceed environmental quality standards
- Gemeente must assess cumulative impact in omgevingsplan (zoning plan)

### Omgevingsvergunning Geluid (Noise Permit)

If the facility cannot meet Bal standard limits:
- Apply for omgevingsvergunning milieubelastende activiteit with geluidrapport (noise report)
- Geluidrapport must demonstrate: source characterization, propagation modeling, assessment at all relevant receptors, comparison with limits, mitigation measures if needed
- Bevoegd gezag (gemeente/omgevingsdienst) reviews geluidrapport and may impose maatwerkvoorschriften
- Veiligheidsregio may be consulted (generator noise during emergencies)

## 3. Noise Sources in AI Data Centers

### Source Characterization

| Source | Sound Power Level (Lw) | Operating Pattern | Key Frequencies | Notes |
|---|---|---|---|---|
| **Dry cooler (droger)** | 85-100 dB(A) per unit | Continuous, 24/7, variable speed | Broadband with 250-500 Hz fan tone | **#1 source for DEC** — many units, always running |
| **Generator (noodstroomaggregaat)** | 95-110 dB(A) | Test: 1 hr/week or month; emergency: intermittent | 63-125 Hz exhaust, 500-1000 Hz casing | Piekgeluid trigger during start, low-frequency propagation |
| **Transformer (transformator)** | 60-80 dB(A) per unit | Continuous, 24/7, load-dependent | 100 Hz hum (2× mains frequency) + harmonics at 200/300/400 Hz | Low-frequency, tonal — difficult to attenuate |
| **DRUPS** | 85-95 dB(A) in diesel mode | Normal: flywheel only (quiet). Test/emergency: diesel engine | 63-500 Hz exhaust + mechanical | Similar to generator when in diesel mode |
| **Heat pump (warmtepomp)** | 75-90 dB(A) | Continuous, variable speed | Compressor tone 125-250 Hz, fan broadband | Ammonia screw compressor is dominant component |
| **CDU pumps** | 65-75 dB(A) per pump | Continuous | Broadband | Usually indoor — minimal external impact |
| **HVAC (luchtbehandeling)** | 70-85 dB(A) per AHU | Continuous | Fan tone, broadband | Moderate contributor if rooftop units |
| **Loading/deliveries** | 75-85 dB(A) | Intermittent daytime | Broadband + reversing alarms | Piekgeluid assessment, not continuous |

### DEC-Specific Source Considerations

**Dry Coolers as Dominant Source:**
At 40 MW IT load with adiabatic dry cooling:
- Approximately 40-80 dry cooler units (depending on size/model)
- Total installed sound power: 100-105 dB(A) combined
- Mounted outdoors on roof or at grade — direct line-of-sight to receptors
- Fan speed varies with ambient temperature — worst case: summer night (high cooling demand + nighttime 40 dB(A) limit)

**Generator Test Runs:**
- Monthly or bi-weekly test runs (1-2 hours each)
- Typically scheduled during daytime (50 dB(A) limit) — but some tests must be at night for realistic loading
- Single generator start: 95+ dB(A) at 1 m → piekgeluid assessment at nearest woning
- Multiple simultaneous generators during failover test: even louder
- **DEC recommendation:** Schedule all generator tests during daytime. If night testing required for IST Level 5 (see commissioning-handover.md), obtain temporary maatwerkvoorschrift from gemeente

**Ammonia Heat Pump Compressor:**
- Large ammonia screw compressors (Oilon, GEA) generate significant low-frequency noise
- Installed in enclosed plant room with sound-attenuating walls — but ventilation openings create noise paths
- Compressor isolation mounts (trillingsisolatie) critical to prevent structure-borne noise transmission

## 4. Noise Modeling Methodology

### ISO 9613-2: Attenuation of Sound During Propagation Outdoors

Standard calculation method for environmental noise assessment:

**Key Parameters:**
- Source sound power level (Lw) per octave band (63 Hz - 8 kHz)
- Distance attenuation (geometric divergence): -6 dB per doubling of distance (point source)
- Ground absorption (Agr): depends on ground type (hard/soft) and geometry
- Atmospheric absorption (Aatm): temperature and humidity dependent, significant at high frequencies
- Screening by barriers (Abar): natural terrain, buildings, purpose-built geluidschermen
- Reflections from buildings and hard surfaces

### Dutch-Specific: Handleiding Meten en Rekenen Industrielawaai (HMRI)

The HMRI (Handbook for Measurement and Calculation of Industrial Noise) is THE reference for NL industrial noise assessment:
- Specifies calculation methodology aligned with ISO 9613-2 but with NL-specific corrections
- Tonality correction (Kt): +5 dB if source contains audible tonal component (transformer hum, compressor whine)
- Impulse correction (Ki): +5 dB if source contains impulsive character (pile driving during construction)
- Meteorological correction (Cm): accounts for favorable propagation conditions (wind direction, temperature inversion)

### Modeling Software

| Software | Developer | Strengths | NL Market Share |
|---|---|---|---|
| **SoundPLAN** | SoundPLAN GmbH (Germany) | Comprehensive, ISO 9613-2 compliant, 3D terrain modeling | ~40% (most used) |
| **CadnaA** | DataKustik (Germany) | User-friendly, strong visualization, Dutch module | ~30% |
| **iNoise** | DGMR (Netherlands) | Dutch-developed, Bal/HMRI compliant by design, fast | ~20% |
| **Predictor** | Brüel & Kjær | Measurement-integrated, good for validation | ~10% |

**DEC Recommendation: iNoise or SoundPLAN.** iNoise is Dutch-developed and natively implements HMRI methodology. SoundPLAN is more versatile for complex 3D terrain but requires explicit HMRI configuration.

## 5. Mitigation Measures

### Source-Level Mitigation (Most Cost-Effective)

**Low-Noise Dry Coolers:**
- Variable speed EC fans with reduced tip speed (lagere tipsnelheid)
- Acoustic enclosure option available from Güntner, Baltimore Aircoil, EWK, Alfa Laval
- Night-mode fan speed reduction: accept slightly higher coolant temperature at night (CDU can compensate)
- **Noise reduction:** 5-10 dB(A) per unit vs standard models
- **Cost premium:** 20-40% per unit
- **DEC recommendation:** Specify low-noise models from design stage — retrofit is much more expensive

**Generator Acoustic Enclosure:**
- Factory-supplied acoustic canopy (geluidsoverkappping): 25-35 dB(A) insertion loss
- Exhaust silencer (uitlaatdemper): residential-grade = 25-35 dB(A) insertion loss, critical-grade = 35-45 dB(A)
- Intake/radiator silencer: 15-25 dB(A)
- **Vendors:** Cummins, Caterpillar/Pon Power, MTU all offer factory acoustic packages
- **DEC recommendation:** Specify residential-grade (woonwijk-klasse) acoustic enclosure for ALL generators

**Transformer Enclosure:**
- Indoor installation in sound-insulated room (Rw 40-50 dB)
- Outdoor: concrete enclosure or purpose-built acoustic housing
- Low-noise transformer specification: request noise class per IEC 60076-10 (one class below standard = ~5 dB reduction)

**Heat Pump Plant Room:**
- Enclosed plant room with Rw 45+ dB walls
- Floating floor (zwevende vloer) on spring isolators for compressor vibration isolation
- Ventilation openings: silenced with splitter attenuators (splitterdempers)
- **Critical:** Ammonia safety ventilation (PGS 13) requires large air openings — these must be acoustically attenuated without restricting emergency ventilation flow

### Path-Level Mitigation

**Geluidscherm (Noise Barrier / Sound Screen):**
- Concrete, steel, or composite barrier between source and receptor
- Insertion loss: depends on height and length relative to source-receptor geometry
- Typical: 5-15 dB(A) insertion loss for well-designed barrier
- Height: 3-6 m above grade (higher = more effective but visually intrusive)
- **Key vendors (NL):** Heblad, Van Campen, Rockdelta, Icopal (acoustic barriers), KOKOWALL (NL — sustainable, timber-concrete hybrid)
- **DEC consideration:** Geluidscherm can double as landscape screening (beeldkwaliteit) — design for both functions. Combine with groen (vegetation planting) for visual integration per gemeentelijke welstandseisen (municipal aesthetic requirements)

**Building Orientation and Layout:**
- Place noisy equipment (dry coolers, generators) on side of building AWAY from nearest woningen
- Use DC building as natural barrier between sources and receptors
- Stack noise-sensitive areas (offices, NOC) on receptor side; equipment yards on opposite side
- **Free mitigation** — costs nothing but requires acoustic input at master plan stage (see site-development skill)

**Terrain and Landscaping:**
- Earth berm (grondwal): 2-4 m high earth mound provides 5-10 dB attenuation plus visual screening
- Dense planting (dichte beplanting): minimal acoustic benefit (<1 dB per 10 m depth) but perceived reduction is significant — human perception weights visual screening
- Water features: no acoustic benefit but mask noise perception (rarely practical for industrial sites)

### Receptor-Level Mitigation (Last Resort)

Not typical for DEC context — receptor-level mitigation (facade insulation) is for existing buildings in noise zones, not for new industrial development. Mentioned for completeness:
- Facade insulation (gevelisolatie): Rw 30-40 dB at nearest woning — gemeente may require as condition if maatwerkvoorschrift grants higher limits at facade
- NEN 5077 (Geluidwering van gebouwen — Sound Insulation of Buildings) applies

## 6. Construction Noise (Bouwgeluid)

### Temporary Construction Activities

Pile driving (heien) is the loudest construction activity and the most common source of neighbor complaints in NL.

**Bal Construction Noise Provisions:**
- Construction noise is separately regulated from operational noise
- Standard limits are more lenient (recognizing temporary nature)
- Bal Art. 7.21-7.26: Bouwwerkzaamheden (construction activities) noise provisions
- Gemeente can set additional conditions via maatwerkvoorschrift

**Construction Noise Limits (Typical Gemeentelijke APV / Local Ordinance):**

| Period | Typical Limit | Notes |
|---|---|---|
| Dag (07:00-19:00) | 80 dB(A) at facade nearest woning | Most construction permitted |
| Avond (19:00-23:00) | 60-65 dB(A) | Restricted — no pile driving |
| Nacht (23:00-07:00) | Not permitted | Exception only by dispensation |
| Saturday | 60-65 dB(A), hours restricted | Typically 08:00-17:00 |
| Sunday/holidays | Not permitted | Exception only by dispensation |

**Pile Driving Noise:**
- Impact hammer: 100-115 dB(A) at 10 m
- Vibratory hammer: 85-100 dB(A) at 10 m
- CFA/auger piling: 75-85 dB(A) at 10 m
- **Vibration:** SBR-A Trillingsrichtlijn (Vibration Guideline Part A — Building Damage) limits at nearby structures

**DEC Mitigation for Construction Noise:**
- Use CFA or screw piles if nearest woning <200 m (avoids impact driving noise and vibration)
- Pre-construction trillingsnulmeting (zero measurement vibration survey) at neighboring buildings
- Continuous vibration monitoring during piling per SBR-A
- Neighbor communication plan (omgevingsmanagement) — notify surrounding residents/businesses before piling starts
- **Stikstof during construction:** Electric piling rigs are quieter AND zero-emission — double benefit

## 7. Operational Monitoring

### Post-Construction Validation

After facility is operational, geluidrapport predictions must be validated by measurement:

**Measurement Standard:** NEN-EN-ISO 3744 / 3746 (sound power) and HMRI (receptor measurement)

**Measurement Points:**
- At nearest gevoelig gebouw (facade measurement)
- At site boundary (as reference)
- Near each major source (source verification)

**Measurement Conditions:**
- Representative operating conditions (full cooling load, generators idle)
- Worst-case scenario (all dry coolers at maximum speed, night period)
- Meteorological: low wind (<5 m/s), no rain, no strong temperature inversion (or correct for Cm)

**Continuous Monitoring Option:**
For DEC's complex source situation (40-80 dry coolers + heat pumps + generators):
- Permanent noise monitoring station at nearest receptor boundary
- Real-time LAeq and Lden logging with alert thresholds
- Correlate with SCADA (dry cooler fan speed, heat pump status) for source identification
- **Vendors:** Cesva, Brüel & Kjær, 01dB, Svantek

### Compliance Reporting
- Annual geluidrapport to bevoegd gezag if required by maatwerkvoorschrift
- Demonstrate compliance with all Bal limits (dag/avond/nacht LAr,LT and LAmax)
- Include meteorological conditions and operating state during measurement

## 8. NL Acoustic Consultancies

### Recommended Firms

| Firm | HQ | Strengths | Notes |
|---|---|---|---|
| **Peutz** | Mook (NL) | Largest NL acoustic consultant, DC experience, comprehensive building + environmental acoustics | Market leader for complex industrial projects |
| **DGMR** | Den Haag (NL) | Developer of iNoise software, strong Omgevingswet expertise, regulatory interpretation | Strong relationship with regulators |
| **LBP\|SIGHT** | Nieuwegein (NL) | Environmental consulting with strong acoustic practice, Bal/Bkl expertise | Good balance of acoustic + environmental |
| **Cauberg-Huygen** | Maastricht (NL) | Building acoustics + sustainability | Strong on building physics, less on environmental |
| **dBvision** | Utrecht (NL) | Specialized acoustic consultancy | Smaller but focused |
| **Level Acoustics & Vibration** | Eindhoven (NL) | Vibration and low-frequency expertise | Good for transformer/compressor issues |

**DEC Recommendation:** Engage Peutz or DGMR at concept design stage (RIBA Stage 2 / VO fase). Their input at master plan level prevents the most expensive acoustic problems. Budget €15,000-€40,000 for full geluidrapport + modeling + permit support.

## Cross-References
- See [heat-rejection-dry-coolers.md](heat-rejection-dry-coolers.md) for dry cooler noise specifications and Bal night limits
- See [heat-pumps-waste-heat.md](heat-pumps-waste-heat.md) for ammonia compressor noise and PGS 13 ventilation requirements
- See [electrical-power-systems.md](electrical-power-systems.md) for generator acoustic enclosure and transformer noise
- See [civil-works-netherlands.md](civil-works-netherlands.md) for construction noise (pile driving) and SBR-A vibration
- See [data-hall-design.md](data-hall-design.md) for building wall sound insulation
- See [fire-safety-suppression.md](fire-safety-suppression.md) for acoustic performance of fire-rated walls
- See [commissioning-handover.md](commissioning-handover.md) for post-construction noise validation measurement
- See companion skill `netherlands-permitting` for omgevingsvergunning geluid procedure, Bal/Bkl interpretation, maatwerkvoorschrift process
- See companion skill `site-development` for building orientation and master plan acoustic strategy
