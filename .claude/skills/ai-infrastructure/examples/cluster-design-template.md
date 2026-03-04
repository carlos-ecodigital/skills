# AI Cluster Design Template — DEC Tenant Specification

## Purpose
Template for specifying an AI compute cluster deployment at a DEC colocation facility. Completed by tenant (or jointly with DEC) during onboarding. Informs facility infrastructure requirements (power, cooling, cabling, space).

---

## A. Tenant & Workload Overview

| Field | Value |
|---|---|
| Tenant Name | |
| Primary Contact (Technical) | |
| Deployment Target Date | |
| Contract Duration | |
| Primary Workload | [ ] Training [ ] Inference [ ] Mixed (___% training / ___% inference) |
| Model Family | (e.g., LLaMA-class, proprietary, MoE, multimodal) |
| Largest Model Size | ___B parameters |
| Training Duration (typical run) | ___ days/weeks |
| Inference SLA Requirement | TTFT: ___ms (p95), TPOT: ___ms (p95), Availability: ___% |

---

## B. GPU & Compute Hardware

### GPU Selection

| Field | Value |
|---|---|
| GPU Platform | [ ] H100 SXM [ ] H200 SXM [ ] B200 [ ] GB200 NVL72 [ ] Other: ___ |
| Total GPU Count | |
| GPUs per Node / Rack | (e.g., 8 per DGX node, 72 per NVL72 rack) |
| Total Nodes / Racks | |
| NVLink Domain Size | (e.g., 8 for DGX, 72 for NVL72) |
| CPU per Node | (e.g., 2× Intel Xeon, 2× AMD EPYC, Grace CPU) |
| RAM per Node | ___ GB |
| Local NVMe per Node | ___× ___ TB |

### Power & Thermal

| Field | Value |
|---|---|
| Power per Node / Rack | ___ kW |
| Total IT Power | ___ kW |
| Cooling Requirement | [ ] 100% Liquid (DTC) [ ] Liquid + Air Hybrid [ ] Immersion |
| CDU Supply Temperature (max acceptable) | ___°C |
| CDU Return Temperature (target) | ___°C |
| Air-Cooled Component Fraction | ___% of total heat |

**DEC Cross-Reference:** → dc-engineering [liquid-cooling-systems.md] for CDU specifications, [heat-recovery-integration.md] for thermal cascade

---

## C. Networking

### Compute Fabric (Backend)

| Field | Value |
|---|---|
| Technology | [ ] InfiniBand NDR 400G [ ] InfiniBand XDR 800G [ ] Ethernet RoCEv2 400G [ ] Ethernet RoCEv2 800G |
| Ports per GPU | ___ (typically 1) |
| Total HCA/NIC Ports | |
| Switch Vendor | [ ] NVIDIA Quantum-2 [ ] NVIDIA Quantum-X800 [ ] Arista [ ] Other: ___ |
| Topology | [ ] Fat-Tree (non-blocking) [ ] Fat-Tree (___:1 oversubscribed) [ ] Rail-Optimized |
| Total Leaf Switches | |
| Total Spine Switches | |
| SHARP (In-Network Reduction) | [ ] Yes [ ] No [ ] N/A (Ethernet) |

### Frontend / Storage / Management Network

| Field | Value |
|---|---|
| Storage Network Speed | [ ] 100 GbE [ ] 200 GbE [ ] 400 GbE per node |
| Management Network Speed | [ ] 25 GbE [ ] 100 GbE per node |
| Total Ethernet Switch Ports | |
| Internet / API Connectivity | ___ Gbps total, ___ diverse carriers |
| Peering | [ ] AMS-IX [ ] NL-ix [ ] Private peering: ___ |

### Cabling Requirements

| Field | Value |
|---|---|
| IB/Compute Cable Count | |
| IB Cable Type | [ ] DAC (≤3m) [ ] AOC (≤100m) [ ] Transceiver+Fiber |
| Ethernet Cable Count | |
| Fiber Type | [ ] OM4 Multimode [ ] OS2 Singlemode [ ] Both |
| Connector Type | [ ] MPO-12 [ ] MPO-16 [ ] LC Duplex |

**DEC Cross-Reference:** → ai-infrastructure [cluster-networking.md] for topology design, dc-engineering [structured-cabling-connectivity.md] for cable routing

---

## D. Storage

### Hot Storage (Parallel File System)

| Field | Value |
|---|---|
| Technology | [ ] WEKA [ ] VAST [ ] Lustre/DDN [ ] GPFS [ ] Other: ___ |
| Capacity | ___ TB / PB |
| Performance Target | ___ GB/s read, ___ GB/s write |
| Media | [ ] All-NVMe [ ] NVMe + SSD [ ] Hybrid |
| Storage Server Count | ___ servers, ___ rack units |

### Warm/Cold Storage

| Field | Value |
|---|---|
| Technology | [ ] MinIO [ ] Ceph [ ] Cloud S3 [ ] Other: ___ |
| Capacity | ___ TB / PB |
| Retention Policy | Checkpoints: ___ days hot, ___ days warm, ___ days cold |

### Storage Rack Requirements

| Field | Value |
|---|---|
| Storage Racks | ___ racks |
| Power per Storage Rack | ___ kW |
| Cooling | [ ] Air-cooled (standard) [ ] Liquid-cooled |

**DEC Cross-Reference:** → ai-infrastructure [ai-storage-data.md] for storage sizing, dc-engineering [data-hall-design.md] for storage room placement

---

## E. Orchestration & Software

| Field | Value |
|---|---|
| Job Scheduler | [ ] SLURM [ ] Kubernetes + GPU Operator [ ] Hybrid [ ] Other: ___ |
| Container Runtime | [ ] Enroot/Pyxis [ ] Docker [ ] containerd [ ] Singularity |
| NVIDIA Driver Version | ___ (or "latest stable") |
| CUDA Toolkit Version | ___ |
| Primary Framework | [ ] PyTorch [ ] JAX [ ] DeepSpeed [ ] Megatron-LM [ ] Other: ___ |
| Multi-User | [ ] Single-user [ ] Multi-user with fair-share [ ] Multi-tenant |

**DEC Cross-Reference:** → ai-infrastructure [cluster-orchestration.md] for scheduling and driver management

---

## F. Monitoring & Operations

| Field | Value |
|---|---|
| GPU Monitoring | [ ] DCGM [ ] nvidia-smi polling [ ] Custom |
| Metrics Pipeline | [ ] Prometheus + Grafana [ ] Datadog [ ] Custom |
| Alerting | [ ] PagerDuty [ ] OpsGenie [ ] Slack [ ] Custom |
| Training Tracking | [ ] Weights & Biases [ ] MLflow [ ] TensorBoard [ ] Custom |

### DEC-Tenant Monitoring Interface

| Data Point | Direction | Method | Agreed |
|---|---|---|---|
| Rack power (kW) | DEC → Tenant | [ ] API [ ] Dashboard [ ] SNMP | [ ] |
| CDU water temp (°C) | DEC → Tenant | [ ] BMS API [ ] Dashboard | [ ] |
| Aggregate GPU power | Tenant → DEC | [ ] API [ ] Manual report | [ ] |
| Planned maintenance | Both ways | [ ] Email [ ] Ticket system | [ ] |
| Emergency shutdown | DEC → Tenant | [ ] SMS [ ] Phone [ ] API | [ ] |

---

## G. Physical Requirements Summary

*Auto-populated from sections above; verified by DEC facility team.*

| Requirement | Value | DEC Verification |
|---|---|---|
| **Total Racks (GPU)** | | [ ] Confirmed |
| **Total Racks (Storage)** | | [ ] Confirmed |
| **Total Racks (Network)** | | [ ] Confirmed |
| **Total IT Power** | ___ kW | [ ] Confirmed |
| **Power per Rack (max)** | ___ kW | [ ] Confirmed |
| **Cooling Method** | | [ ] Confirmed |
| **CDU Supply Temp** | ___°C | [ ] Confirmed |
| **CDU Return Temp** | ___°C | [ ] Confirmed |
| **IB Cable Count** | | [ ] Confirmed |
| **Ethernet Cable Count** | | [ ] Confirmed |
| **Fiber Type / Connector** | | [ ] Confirmed |
| **External Connectivity** | ___ Gbps from ___ carriers | [ ] Confirmed |
| **Cage Size Required** | ___ m² | [ ] Confirmed |
| **Floor Loading** | ___ kN/m² (heaviest rack) | [ ] Confirmed |

---

## H. Heat Recovery Impact

*Completed by DEC facility team based on tenant specification.*

| Parameter | Value |
|---|---|
| Expected Average Thermal Output | ___ MW |
| Thermal Variability (daily range) | ±___% |
| Workload Type Impact | [ ] Steady (training) [ ] Variable (inference) [ ] Mixed |
| CDU Return Temperature | ___°C |
| Heat Recovery Viability | [ ] Excellent (>80% capture) [ ] Good (60-80%) [ ] Limited (<60%) |
| Greenhouse Heat Demand Match | [ ] Full year [ ] Winter only [ ] Supplementary |
| Buffer Tank Sizing Impact | ___ hours at ___ MWth |

**DEC Cross-Reference:** → dc-engineering [heat-recovery-integration.md], site-development [grower-thermal-interface.md]

---

## I. Permitting & Compliance Impact

*Completed by DEC permitting team based on tenant specification.*

| Item | Status | Notes |
|---|---|---|
| Power within existing grid connection capacity | [ ] Yes [ ] No — requires expansion | |
| Noise impact from additional cooling | [ ] Within Bal limits [ ] Requires reassessment | |
| Fire compartment impact | [ ] Within existing [ ] Requires modification | |
| BESS integration (if applicable) | [ ] N/A [ ] Requires PGS 37 assessment | |
| Stikstof impact (if backup generators added) | [ ] N/A [ ] Requires AERIUS update | |

**DEC Cross-Reference:** → netherlands-permitting, dc-engineering [acoustic-engineering.md], [fire-safety-suppression.md]

---

## Sign-Off

| Role | Name | Date | Signature |
|---|---|---|---|
| Tenant Technical Lead | | | |
| Tenant Procurement | | | |
| DEC Facility Engineering | | | |
| DEC Commercial | | | |
| DEC Heat Recovery Lead | | | |

---

## Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | | | Initial specification |
