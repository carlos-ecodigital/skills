# Cluster Networking for AI Training and Inference

## 1. Network Architecture for GPU Clusters

### Two Distinct Networks

Every large AI cluster has two physically separate networks:

**1. Compute Fabric (Backend Network):**
- GPU-to-GPU communication for training collectives (AllReduce, AllGather, ReduceScatter)
- Low latency, high bandwidth, RDMA-capable
- InfiniBand or RoCEv2 Ethernet
- Dedicated switches, dedicated NICs (HCA/NIC per GPU or per node)
- NOT shared with storage or management traffic

**2. Frontend / Storage / Management Network:**
- Storage I/O (NFS, POSIX, S3 to storage cluster)
- Management (SSH, IPMI/BMC, monitoring, logging)
- Tenant internet access (API endpoints, model serving)
- Standard Ethernet (100-400 GbE)
- Can be shared across functions with VLANs/VRFs

### DEC Colocation Implication
DEC provides the physical layer (fiber, cable tray, meet-me room, structured cabling). Tenants provide their own switches, NICs, and network configuration. DEC's design must accommodate the massive fiber density that AI clusters require (see cabling section below).

## 2. InfiniBand

### Technology Overview
InfiniBand is a high-performance networking standard designed for HPC and now dominant in AI training:

| Generation | Per-Port Speed | Encoding | Cable | Year |
|---|---|---|---|---|
| EDR | 100 Gb/s | 64b/66b | Copper / OM4 fiber | 2014 |
| HDR | 200 Gb/s | 64b/66b | Copper / OM4 fiber | 2020 |
| NDR | 400 Gb/s | PAM4 + FEC | Copper (short) / OM4-SM fiber | 2023 |
| XDR | 800 Gb/s | PAM4 + FEC | Active copper / SM fiber | 2025 |

### NVIDIA InfiniBand Products

**Host Channel Adapters (HCAs):**
- ConnectX-7: NDR 400 Gb/s, PCIe Gen5 x16
- ConnectX-8: XDR 800 Gb/s, PCIe Gen6 x16 (expected 2025-2026)
- BlueField-3 DPU: ConnectX-7 + ARM cores for smart NIC / infrastructure offload

**Switches:**
- Quantum-2 (QM9700): NDR 400G, 64 ports per switch
- Quantum-X800 (QM9790): XDR 800G, 64 ports per switch (expected 2025)
- Managed by NVIDIA UFM (Unified Fabric Manager) software

### InfiniBand Advantages for Training
1. **RDMA Native:** Remote Direct Memory Access is the fundamental transport — zero-copy, kernel-bypass, sub-microsecond latency
2. **Adaptive Routing:** Hardware-level adaptive routing avoids congestion without software intervention
3. **SHARP (Scalable Hierarchical Aggregation and Reduction Protocol):** In-network compute — AllReduce operations partially executed in switches, reducing GPU communication overhead by 2-3x
4. **Lossless Fabric:** Credit-based flow control prevents packet drops without complex ECN/DCQCN tuning
5. **Proven at Scale:** NVIDIA DGX SuperPOD, Meta Grand Teton, xAI Colossus — all InfiniBand

### InfiniBand Disadvantages
1. **Vendor lock-in:** NVIDIA (formerly Mellanox) is the only meaningful vendor
2. **Cost:** 2-3x per-port cost compared to Ethernet
3. **Operational expertise:** Smaller talent pool than Ethernet networking
4. **Subnet manager:** Centralized fabric management (OpenSM or UFM) — different operational model than distributed Ethernet
5. **Limited ecosystem:** Few third-party tools compared to Ethernet

## 3. Ethernet for AI (RoCEv2)

### RDMA over Converged Ethernet (RoCEv2)
RoCEv2 provides RDMA semantics over standard Ethernet:
- Uses UDP/IP encapsulation → routable across L3 networks
- Requires lossless Ethernet: PFC (Priority Flow Control) + ECN (Explicit Congestion Notification) + DCQCN (or equivalent)
- Supported by same NVIDIA ConnectX NICs (dual-mode IB/Ethernet)

### Ethernet Advantages
1. **Lower cost:** Standard Ethernet switches from multiple vendors (Arista, Cisco, Juniper, Broadcom)
2. **Larger talent pool:** Every network engineer knows Ethernet
3. **Multi-vendor:** Not locked to NVIDIA for switches
4. **Converged infrastructure:** Can carry storage + management + compute on same fabric with QoS
5. **Ultra Ethernet Consortium (UEC):** Industry effort to optimize Ethernet for AI (Intel, AMD, Arista, Broadcom, Cisco, Meta, Microsoft) — aims to close gap with IB

### Ethernet Disadvantages
1. **Congestion control complexity:** PFC + ECN tuning is fragile — misconfiguration causes headroom buffer exhaustion, PFC storms, or packet drops
2. **No SHARP equivalent:** AllReduce must happen entirely at GPU level — no in-network reduction
3. **Higher tail latency:** Under congestion, Ethernet tail latency is 5-10x higher than InfiniBand
4. **Operational burden:** Lossless Ethernet requires careful configuration of every switch hop — one misconfigured switch can cause cluster-wide performance collapse

### Ethernet Switch Vendors for AI

| Vendor | Platform | Port Count/Speed | AI-Specific Features |
|---|---|---|---|
| **Arista** | 7800R3 | 400G/800G | BGP-based fabric, DANZ for monitoring |
| **Cisco** | Nexus 9000 | 400G | ACI for policy-based automation |
| **Juniper** | QFX5220/5230 | 400G | Apstra for intent-based networking |
| **Broadcom** | Memory Fabric (OEM) | 800G | CXL integration, Memory Fabric for disaggregated compute |

### DEC Recommendation: InfiniBand for Training, Ethernet for Everything Else

**Compute fabric (training):** InfiniBand NDR/XDR
- SHARP provides 2-3x improvement in AllReduce — real performance difference, not theoretical
- Lossless by design — no PFC tuning nightmares
- NVIDIA GPU + NVIDIA NIC + NVIDIA switch = integrated, supported, debuggable
- 95%+ of DEC's neocloud tenants training at scale will specify InfiniBand

**Compute fabric (inference):** Ethernet 400G/800G RoCEv2
- Inference communication patterns are lighter (no AllReduce at training scale)
- Ethernet's cost advantage matters for inference (lower margin per GPU-hour)
- Multi-vendor flexibility for inference-focused tenants

**Storage / management / frontend:** Ethernet 100-400 GbE
- Standard, well-understood, appropriate for non-latency-critical traffic

## 4. Network Topology

### Fat-Tree (Clos Network)

Traditional HPC/AI cluster topology:
```
        Spine Switches (Layer 2)
       /     |      |      \
      /      |      |       \
    Leaf    Leaf   Leaf    Leaf   (Layer 1)
    / \     / \    / \     / \
  GPU GPU GPU GPU GPU GPU GPU GPU  (Endpoints)
```

- Full bisection bandwidth: any GPU can communicate with any other at full line rate
- Oversubscription ratio: 1:1 (non-blocking) or 2:1/3:1 (oversubscribed)
- Requires many spine switches — cost scales quadratically with cluster size

**Fat-Tree Pros:**
- Maximum flexibility — any workload placement works
- No topology-aware scheduling required
- Proven architecture (20+ years in HPC)

**Fat-Tree Cons:**
- Expensive at scale (many spine switches)
- Overprovisioned for training workloads (training communication is structured, not random)
- High cabling complexity at spine layer

### Rail-Optimized Topology

Emerging topology specifically for AI training:
```
     Rail 0 switches  Rail 1 switches  Rail 2 switches  ...  Rail 7 switches
         |                |                |                       |
    GPU0 of each     GPU1 of each    GPU2 of each          GPU7 of each
    node connects    node connects   node connects         node connects
    to Rail 0        to Rail 1       to Rail 2             to Rail 7
```

Each "rail" is a separate network connecting all GPUs at the same position across nodes (all GPU 0s, all GPU 1s, etc.). AllReduce is performed independently on each rail.

**Rail-Optimized Pros:**
- ~40-60% fewer switches than equivalent fat-tree
- Lower cabling complexity
- Matches AllReduce communication pattern exactly
- NVIDIA's recommended topology for DGX SuperPOD and GB200 NVL72

**Rail-Optimized Cons:**
- Less flexible — workload placement must be topology-aware
- Not ideal for mixed workloads or inference (different communication patterns)
- Requires topology-aware scheduler (SLURM with topology plugin)

**DEC Recommendation: Rail-Optimized for Training Halls, Fat-Tree for Mixed/Inference Halls**
- Training-dedicated halls: rail-optimized (cost savings, performance match)
- Mixed/inference halls: fat-tree (flexibility for diverse tenant workloads)
- DEC's multi-tenant model may require different topology per hall based on tenant workload mix

### SuperPOD Architecture (NVIDIA Reference)

NVIDIA DGX SuperPOD is the reference architecture for large-scale AI clusters:
- **Compute Unit (CU):** 1 DGX node (8 GPUs)
- **Scalable Unit (SU):** 8 CUs = 64 GPUs per SU, connected via leaf switches
- **SuperPOD:** 8+ SUs = 512+ GPUs, connected via spine switches
- **Multi-SuperPOD:** multiple SuperPODs connected via super-spine

For GB200 NVL72:
- 1 rack = 72 GPUs (NVLink-connected domain)
- Multiple racks connected via InfiniBand XDR switches
- NVIDIA's reference: 576 GPUs per SuperPOD (8 racks of NVL72)

## 5. Fabric Sizing

### Bandwidth per GPU

**Rule of Thumb for Training:**
Network bandwidth per GPU should be ≥1/8 of GPU memory bandwidth for efficient AllReduce.

| GPU | Memory BW | Recommended Network BW | Recommended Technology |
|---|---|---|---|
| H100 | 3.35 TB/s | 400 Gb/s per GPU | NDR 400G IB (1 port/GPU) |
| B200 | 8 TB/s | 800 Gb/s per GPU | XDR 800G IB (1 port/GPU) |
| GB200 (NVL72) | 8 TB/s per GPU, 1,800 GB/s NVLink | 400-800 Gb/s per GPU (inter-rack) | NDR/XDR IB for inter-rack |

**NVL72 Nuance:** Within the NVL72 rack, all 72 GPUs communicate via NVLink (1,800 GB/s) — no external network needed. The InfiniBand network only carries INTER-rack traffic (AllReduce across multiple NVL72 racks). This dramatically reduces the required InfiniBand port count compared to 8-GPU-per-node architectures.

### Switch and Cable Count Example

**1,024 GPU Cluster (H100 SXM, 8 GPU/node, Fat-Tree NDR 400G):**
- 128 nodes × 8 GPUs = 1,024 GPUs
- 128 nodes × 8 HCAs = 1,024 HCA ports
- Leaf switches: 32 (Quantum-2 QM9700, 64 ports each, 32 downlinks + 32 uplinks)
- Spine switches: 32 (Quantum-2, 32 downlinks from all leaves)
- Total switches: 64
- Total cables: ~2,048 (leaf-to-node: 1,024 + leaf-to-spine: 1,024)

**1,008 GPU Cluster (GB200 NVL72, 14 racks, Rail-Optimized NDR 400G):**
- 14 racks × 72 GPUs = 1,008 GPUs
- Inter-rack HCAs: 14 racks × 18 HCAs per rack = 252 HCA ports (NOT 1,008 — NVLink handles intra-rack)
- Leaf switches: ~8 (rail switches, 32 ports each)
- Spine switches: ~4 (if any — small cluster may be leaf-only)
- Total switches: ~12
- Total cables: ~264
- **80% fewer switches and cables than equivalent 8-GPU-per-node fat-tree**

## 6. Optics and Cabling

### Cable Types

| Type | Distance | Speed | Application |
|---|---|---|---|
| **DAC (Direct Attach Copper)** | ≤3 m | 400G/800G | Within rack, short ToR connections |
| **ACC (Active Copper Cable)** | 3-7 m | 400G | Short inter-rack |
| **AOC (Active Optical Cable)** | 7-100 m | 400G/800G | Intra-data-hall inter-rack |
| **Transceiver + fiber** | 100 m - 10 km | 400G/800G | Long runs, cross-building, external |

### Fiber Types for AI Clusters

| Fiber | Core Size | Typical Distance (400G) | Application |
|---|---|---|---|
| OM4 multimode | 50 µm | ≤100 m (SR4/SR8) | Intra-building, data hall interconnect |
| OM5 multimode | 50 µm | ≤150 m (SR4) | Extended intra-building |
| OS2 single-mode | 9 µm | ≤10 km (DR4/FR4) | Inter-building, backbone, external |

### Connector Types

| Connector | Fibers | Speed | Trend |
|---|---|---|---|
| LC duplex | 2 | Up to 400G (FR4) | Legacy, still used for SM backbone |
| MPO-12 | 12 | 400G (SR4 = 4×100G) | Current standard for short-reach |
| MPO-16 | 16 | 800G (SR8 = 8×100G) | Emerging for 800G |
| MPO-32 | 32 | High-density 400G+ | Reduced cable count |

### Cabling Density for AI Clusters

AI clusters generate extraordinary cabling density compared to enterprise data centers:

**Example: 1,024 GPU H100 cluster (128 nodes) in single data hall:**
- 1,024 IB cables (compute fabric) + 128-256 Ethernet cables (storage/management) + power cables
- Total: ~1,300+ cables in cable tray
- Each IB cable: ~5 mm diameter × up to 30 m length
- Cable tray capacity: allocate 100-150 mm² per cable × 1,300 = 130,000-195,000 mm² cross-section
- **This is 2-3x the cable tray density of a traditional enterprise DC at the same rack count**

**DEC Design Implication:**
- Cable tray sizing: specify 50% fill ratio at maximum cluster density (allows future additions)
- Pre-plan cable routes from each rack to spine/leaf switch locations
- Fiber patch panels in end-of-row or top-of-rack locations
- Dedicated structured cabling team during tenant deployment (see dc-engineering data-hall-design.md)

## 7. Multi-Tenant Network Isolation

### The Challenge
DEC's multi-tenant colocation model means multiple independent tenants' GPU clusters share the same building but must be completely isolated:

**Physical Isolation (Strongest):**
- Separate switches, separate fiber runs, separate meet-me room cross-connects
- No shared infrastructure at Layer 1-3
- **DEC recommendation for compute fabric:** Each tenant has physically separate IB fabric — no shared IB switches between tenants (IB subnet manager manages one trust domain)

**Logical Isolation (Acceptable for Frontend/Storage):**
- Shared Ethernet switches with VRF (Virtual Routing and Forwarding) and VLAN isolation
- Each tenant in separate VRF — routing isolated at control plane level
- Shared physical infrastructure, logically separated
- Acceptable for management and storage networks if tenants agree

### Network Security
- DEC provides: physical fiber, structured cabling, MMR, carrier cross-connects
- Tenant provides: all active networking equipment (switches, NICs, firewalls)
- DEC does NOT inspect, monitor, or manage tenant network traffic
- Physical security (locked cages) prevents unauthorized fiber access
- DEC's management network (BMS, CCTV, access control) is completely air-gapped from tenant networks

## 8. Monitoring and Observability

### Network Monitoring for AI Clusters

**InfiniBand Monitoring:**
- NVIDIA UFM (Unified Fabric Manager): fabric-wide visibility, health monitoring, event logging
- Performance counters: port counters (Tx/Rx bytes, errors, discards), latency histograms
- SHARP telemetry: in-network reduction statistics
- Cable health: BER (Bit Error Rate) monitoring per link

**Ethernet Monitoring:**
- Standard SNMP/gNMI/streaming telemetry from switches
- PFC/ECN counters: critical for detecting congestion and lossless fabric health
- sFlow/NetFlow for traffic analysis

**AI-Specific Metrics (Tenant Responsibility):**
- NCCL debug logging: AllReduce timing, bandwidth utilization per ring/tree
- GPU-to-GPU latency matrix: detect degraded links before they cause training slowdowns
- Collective communication profiling: NVIDIA Nsight Systems, PyTorch profiler

### DEC's Network Monitoring Scope
DEC monitors physical layer only:
- Fiber link status (up/down) for structured cabling
- Environmental monitoring in MMR (temperature, humidity)
- Physical security (MMR access logs)
- DEC does NOT monitor tenant's IB or Ethernet active equipment — that is tenant's responsibility

## Cross-References
- See [gpu-accelerator-hardware.md](gpu-accelerator-hardware.md) for NVLink specifications and GPU interconnect requirements
- See [cluster-orchestration.md](cluster-orchestration.md) for topology-aware scheduling
- See [training-workloads.md](training-workloads.md) for AllReduce communication patterns and bandwidth requirements
- See [inference-serving.md](inference-serving.md) for inference network requirements (lighter than training)
- See [ai-storage-data.md](ai-storage-data.md) for storage network design
- See companion skill `dc-engineering`:
  - [data-hall-design.md] for cable tray capacity and structured cabling infrastructure
  - [electrical-power-systems.md] for network switch power requirements
- See companion skill `site-development` for meet-me room design and carrier connectivity strategy
