# GPU & Accelerator Hardware for AI Data Centers

## 1. The GPU Landscape (2025-2027)

### NVIDIA Dominance
NVIDIA controls ~80-90% of AI training accelerator market by revenue. The CUDA software ecosystem is the moat — not the silicon. Every major AI framework (PyTorch, JAX, TensorFlow) is optimized for CUDA first, everything else second.

### Platform Comparison

| Platform | GPU | Memory | TDP per GPU | Interconnect | Form Factor | Training | Inference | DEC Relevance |
|---|---|---|---|---|---|---|---|---|
| **NVIDIA H100 SXM** | Hopper | 80 GB HBM3 | 700W | NVLink 4.0 (900 GB/s) | SXM5 baseboard, 8-GPU per node | Excellent | Good | Current workhorse, abundant supply |
| **NVIDIA H200 SXM** | Hopper (updated) | 141 GB HBM3e | 700W | NVLink 4.0 (900 GB/s) | SXM5, drop-in H100 upgrade | Excellent (larger models) | Better (more KV cache) | Preferred over H100 for new orders |
| **NVIDIA B200** | Blackwell | 192 GB HBM3e | 1,000W | NVLink 5.0 (1,800 GB/s) | SXM6 baseboard, 8-GPU per node | Superior | Superior | Next-gen, available 2025+ |
| **NVIDIA GB200 NVL72** | Grace + Blackwell | 192 GB HBM3e per GPU | ~1,200W per GPU (rack) | NVLink 5.0 (1,800 GB/s), 72 GPUs in single domain | Liquid-cooled rack (120-130 kW) | Best-in-class | Best-in-class | THE target platform for DEC — defines facility thermal design |
| **NVIDIA GB300 NVL72** | Grace + Blackwell Ultra | 288 GB HBM3e per GPU | ~1,400W per GPU (rack) | NVLink 5.0 (1,800 GB/s) | Liquid-cooled rack | Next frontier | Next frontier | 2026+ — facility must be designed to handle this power density |
| **NVIDIA L40S** | Ada Lovelace | 48 GB GDDR6X | 350W | PCIe Gen4 x16 | PCIe card, air-cooled | Limited | Good (inference) | Low-cost inference option for multi-tier tenant deployment |
| **AMD MI300X** | CDNA 3 | 192 GB HBM3 | 750W | Infinity Fabric (896 GB/s peer) | OAM baseboard, 8-GPU per node | Competitive | Competitive | Alternative for cost-sensitive tenants, ROCm maturity improving |
| **AMD MI325X** | CDNA 3 (updated) | 256 GB HBM3e | 750W | Infinity Fabric | OAM | Improved | Improved | More memory for larger models |
| **AMD MI350** | CDNA 4 | TBD | ~750-1,000W | TBD | OAM/SXM compatible | TBD | TBD | 2025-2026 generation, competes with Blackwell |
| **Intel Gaudi 3** | Gaudi | 128 GB HBM2e | 900W | 24x 200G Ethernet RoCEv2 | OAM or PCIe | Moderate | Moderate | Budget option, Intel ecosystem integration |

### GB200 NVL72: The Facility-Defining Platform

The NVIDIA GB200 NVL72 is a liquid-cooled, rack-scale system that fundamentally changes data center design:

**Key Specifications:**
- 72 Blackwell GPUs + 36 Grace CPUs in a single rack
- Total rack power: 120-130 kW (liquid-cooled)
- NVLink domain: all 72 GPUs interconnected at 1,800 GB/s per GPU
- Liquid cooling: mandatory — 80%+ heat removed via direct-to-chip (DTC) liquid cooling
- CDU supply temperature: 32-35°C recommended (see dc-engineering liquid-cooling-systems.md)
- Rack dimensions: 2,200 mm height × 600 mm width × 1,200 mm depth, ~2,500 kg loaded

**Why GB200 NVL72 Defines DEC's Facility:**
- Power density (120+ kW/rack) determines electrical distribution design
- Liquid cooling requirement eliminates air-cooled facility options
- CDU return temperature (42-45°C) feeds directly into heat recovery design
- Weight (2,500 kg) determines floor loading capacity
- Depth (1,200 mm) determines aisle width and data hall geometry

## 2. Thermal Profiles by Workload

### GPU Power Draw Variability

GPU power consumption varies significantly by workload type:

| Workload | Typical Power Draw (% of TDP) | Pattern | Thermal Implication |
|---|---|---|---|
| **LLM Training (dense model)** | 85-95% TDP | Sustained, very stable | Steady heat load — ideal for heat recovery |
| **LLM Training (MoE model)** | 70-85% TDP | Moderate variation (expert routing) | Slightly variable but still predictable |
| **Pre-training (data-intensive)** | 80-90% TDP | Sustained with periodic I/O pauses | Brief dips during data loading — minimal cooling impact |
| **Fine-tuning (LoRA, RLHF)** | 60-80% TDP | More variable, shorter runs | Moderate variability |
| **Inference (high batch)** | 50-75% TDP | Varies with request rate | Can be highly variable — demand-driven |
| **Inference (low latency)** | 30-60% TDP | Bursty, unpredictable | Most variable — hardest for cooling and heat recovery |
| **Idle / standby** | 15-25% TDP | Baseline | Still significant heat at AI density |

**DEC Heat Recovery Implication:**
Training-dominant facilities provide the most predictable and valuable heat source. Inference-dominant facilities produce more variable heat. DEC's financial model for heat revenue should be based on minimum guaranteed heat (worst-case idle + inference variability) not peak training heat.

### Thermal Envelope per Platform

| Platform | TDP per GPU | Min Power (idle) | Typical Training | Rack Total (8-GPU node) | Rack Total (NVL72) |
|---|---|---|---|---|---|
| H100 SXM | 700W | 120W | 600-660W | ~5.5-6.0 kW (8 GPU + CPU + NIC) | N/A |
| H200 SXM | 700W | 120W | 600-660W | ~5.5-6.0 kW | N/A |
| B200 SXM | 1,000W | 150W | 850-950W | ~8.0-9.0 kW | N/A |
| GB200 NVL72 | ~1,200W (GPU equiv.) | ~200W | 1,000-1,100W | N/A | 120-130 kW total rack |
| MI300X OAM | 750W | 130W | 640-700W | ~6.0-6.5 kW | N/A |

## 3. Memory Systems

### HBM (High Bandwidth Memory)

HBM is THE enabler for large language models. GPU compute speed is often not the bottleneck — memory bandwidth and capacity are.

| HBM Generation | Bandwidth per Stack | Capacity per Stack | GPU Integration |
|---|---|---|---|
| HBM2e | 460 GB/s | 16 GB | Intel Gaudi 3 |
| HBM3 | 819 GB/s | 16-24 GB | NVIDIA H100, AMD MI300X |
| HBM3e | 1,218 GB/s | 24-36 GB | NVIDIA H200, B200, GB200, AMD MI325X |
| HBM4 (expected 2026) | ~2,000 GB/s | 36-48 GB | Next-gen platforms |

**Memory Capacity vs Model Size:**
| Model Size | Minimum GPU Memory (FP16 weights only) | With KV Cache + Optimizer (Training) | Practical GPU Count (H200) |
|---|---|---|---|
| 7B parameters | 14 GB | ~60 GB | 1 GPU |
| 70B parameters | 140 GB | ~600 GB | 4-8 GPUs |
| 405B parameters | 810 GB | ~3.4 TB | 32-64 GPUs |
| 1T+ parameters | 2+ TB | ~10+ TB | 128-512+ GPUs |
| MoE (e.g., Mixtral 8x22B) | ~352 GB (all experts) | ~1.5 TB | 8-32 GPUs |

**DEC Relevance:** Neocloud tenants training frontier models (100B+) need multi-node clusters with high-bandwidth interconnect. Single-GPU or small-cluster inference is fine for PCIe cards (L40S, T4). The facility's GPU mix determines interconnect, power, and cooling requirements.

## 4. Interconnect Technology

### NVLink

NVIDIA's proprietary GPU-to-GPU interconnect:

| Generation | Bandwidth (bidirectional per GPU) | Topology | Platform |
|---|---|---|---|
| NVLink 3.0 | 600 GB/s | NVSwitch within node (8 GPU) | A100 |
| NVLink 4.0 | 900 GB/s | NVSwitch within node (8 GPU) | H100, H200 |
| NVLink 5.0 | 1,800 GB/s | NVSwitch, 72-GPU domain (NVL72) | B200, GB200 |

NVLink is 5-20x faster than PCIe for GPU-to-GPU communication. For training large models with tensor parallelism, NVLink is essential.

### PCIe

| Generation | Bandwidth per Lane | x16 Total | Application |
|---|---|---|---|
| PCIe Gen4 | 2 GB/s | 32 GB/s | L40S, older inference GPUs |
| PCIe Gen5 | 4 GB/s | 64 GB/s | H100 PCIe, B200 PCIe, CPU-GPU |
| PCIe Gen6 | 8 GB/s | 128 GB/s | Expected 2026+ |

PCIe is sufficient for: inference (single-GPU or small-cluster), CPU-GPU data transfer, storage I/O. NOT sufficient for large-scale training tensor parallelism.

### CXL (Compute Express Link)

Emerging technology for memory pooling and disaggregation:
- CXL 3.0 enables shared memory pools across GPUs and CPUs
- Potential to expand effective GPU memory beyond HBM capacity
- Still early — few production deployments for AI workloads
- Samsung, Micron, and Intel leading CXL memory development
- **DEC relevance:** Architect facility with CXL-capable networking infrastructure (Ethernet-based, same physical layer) for future flexibility. Not required for Phase 1.

## 5. Custom AI Accelerators

### Cerebras (Wafer Scale Engine — WSE)
- Single wafer-scale chip: 900,000 cores, 44 GB SRAM (on-chip), no HBM
- CS-3 system: single WSE-3 chip per unit
- MemoryX: external memory disaggregation for large models
- Strengths: eliminates memory bandwidth bottleneck for certain workloads, massive on-chip SRAM
- Weaknesses: software ecosystem is proprietary (not CUDA), limited multi-chip scaling, niche market
- **DEC relevance:** Unlikely to see Cerebras as tenant hardware in Phase 1 — too specialized

### Groq (LPU — Language Processing Unit)
- Deterministic inference accelerator — no caches, no variable-length pipelines
- Very low latency, very high throughput per chip for inference
- Single-chip inference only — not for training
- Strengths: predictable latency, low power per inference
- Weaknesses: training not supported, narrow workload applicability
- **DEC relevance:** Possible inference tenant in future — low power, air-cooled, different facility requirements than GPU training

### Google TPU
- Available only through Google Cloud (GCP) — NOT available for colocation
- TPU v5p and Trillium are competitive with H100/B200 for training within Google's ecosystem
- **DEC relevance:** None for colocation — Google deploys TPUs exclusively in own data centers

### Custom Silicon Trend
Hyperscalers (AWS Trainium, Google TPU, Microsoft Maia, Meta MTIA) are all building custom AI silicon to reduce NVIDIA dependency. This silicon stays within their own clouds.

For the colocation market (DEC's market), NVIDIA and AMD are the only viable options. Custom silicon tenants are possible but would be single-tenant with highly specific facility requirements.

## 6. GPU Supply Chain & Procurement

### Lead Times (2025 Landscape)
| Platform | Typical Lead Time | Supply Status | Notes |
|---|---|---|---|
| H100 SXM | 4-8 weeks | Readily available | Supply has normalized after 2023-2024 shortage |
| H200 SXM | 8-16 weeks | Moderate availability | Ramping production |
| B200 SXM | 12-24 weeks | Constrained | New platform, high demand |
| GB200 NVL72 | 16-30+ weeks | Very constrained | Production ramp ongoing, Compal/Foxconn assembly |
| MI300X | 8-16 weeks | Available | AMD competing on availability |
| L40S | 4-8 weeks | Readily available | Lower demand segment |

### Procurement Channels
- **NVIDIA direct:** For large orders (1,000+ GPUs), NVIDIA's enterprise sales team
- **OEM partners:** Supermicro, Dell, HPE, Lenovo, ASUS, Gigabyte — sell complete servers with NVIDIA GPUs
- **NVL72 rack integrators:** Limited to NVIDIA-certified partners: Supermicro, Foxconn/Hon Hai, Wiwynn, QCT
- **Cloud marketplace:** CoreWeave, Lambda, Voltage Park — rent GPU capacity (relevant for DEC's neocloud tenants who may prefer to rent through these intermediaries)

### DEC Colocation Model
DEC does NOT typically procure GPUs — tenants (neoclouds) bring their own hardware. DEC provides:
- Facility (power, cooling, physical space, connectivity)
- Landlord power and cooling SLA
- Heat recovery integration (transparent to tenant)

Exception: DEC may procure GPUs for a "GPU-as-a-Service" or managed colocation offering in future phases.

## 7. Power Efficiency & Carbon

### GPU Efficiency Trends

| Metric | H100 | B200 | GB200 | Unit |
|---|---|---|---|---|
| Training FLOPS (FP8) | 3,958 TFLOPS | 9,000 TFLOPS | ~10,000 TFLOPS | TFLOPS |
| TDP | 700W | 1,000W | ~1,200W (equiv.) | Watts |
| FLOPS per Watt (FP8) | 5.7 | 9.0 | ~8.3 | TFLOPS/W |

Each GPU generation is more efficient per FLOP but consumes more total power (because more transistors, more FLOPS). This is why power per rack keeps climbing even as efficiency improves.

### Carbon Accounting for GPU Compute
- Scope 2 emissions: electricity consumption × grid emission factor
- NL grid emission factor (2024): ~0.28 kg CO2/kWh (declining as renewable share increases)
- GPU training carbon: dominated by electricity (80%+), not hardware embodied carbon
- DEC advantage: if heat recovery displaces gas heating in greenhouse, net carbon is significantly reduced (heat recovery carbon credit)
- See companion skill `energy-markets` for carbon accounting and CSRD compliance

## Cross-References
- See [cluster-networking.md](cluster-networking.md) for NVLink/InfiniBand/Ethernet topology design
- See [training-workloads.md](training-workloads.md) for power draw profiles by workload type
- See [inference-serving.md](inference-serving.md) for inference GPU mix and SLA requirements
- See companion skill `dc-engineering` for thermal design driven by GPU specifications:
  - [liquid-cooling-systems.md] for CDU temperature targets driven by GPU thermal specs
  - [electrical-power-systems.md] for power distribution driven by GPU power density
  - [data-hall-design.md] for rack layout driven by GPU rack dimensions
- See companion skill `energy-markets` for carbon accounting and power procurement
- See companion skill `site-development` for GPU-hour unit economics in financial model
