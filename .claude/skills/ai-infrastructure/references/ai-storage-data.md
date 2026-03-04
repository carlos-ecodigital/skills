# AI Storage & Data Pipelines

## 1. Storage Architecture for AI Clusters

### Three-Tier Storage Hierarchy

Every AI cluster requires storage across three distinct performance tiers:

```
Tier 1: HOT STORAGE (Parallel File System)
  │  Purpose: Active training data, checkpoints, model artifacts
  │  Performance: 100+ GB/s aggregate read, 50+ GB/s write
  │  Capacity: 1-10 PB
  │  Technology: WEKA, VAST, Lustre, GPFS/Spectrum Scale
  │  Media: All-NVMe or NVMe + SSD hybrid
  │
Tier 2: WARM STORAGE (Object/NAS)
  │  Purpose: Datasets awaiting processing, older checkpoints, model archive
  │  Performance: 10-50 GB/s aggregate
  │  Capacity: 10-100 PB
  │  Technology: MinIO, Ceph, NetApp, Dell ECS
  │  Media: SSD or HDD
  │
Tier 3: COLD STORAGE (Object Store / Archive)
     Purpose: Raw data lake, compliance archive, disaster recovery
     Performance: 1-10 GB/s
     Capacity: 100 PB - EB
     Technology: S3 (AWS), GCS, Azure Blob, on-prem object store
     Media: HDD, tape, cloud
```

### Storage Network (Separate from Compute Fabric)

Storage traffic runs on the frontend Ethernet network, NOT on the InfiniBand compute fabric:
- Storage NICs: 100-400 GbE per node (separate from IB HCAs)
- Storage switches: standard Ethernet leaf/spine
- Protocol: NFS (legacy), S3 (object), POSIX (parallel FS client)
- DEC provides structured cabling; tenant provides storage switches and appliances

### Storage Sizing Rules of Thumb

**Training Data Storage:**
- Raw dataset: 5-50 TB for typical LLM training (tokenized text)
- Processed/tokenized: 1-10 TB (compact binary format)
- Multi-epoch training: full dataset must be accessible at GPU feeding rate

**Checkpoint Storage:**
- Per checkpoint: ~4× model parameter count (model + optimizer states)
- 70B model: ~560 GB per checkpoint
- Frequency: every 15 min to 2 hours depending on cluster size
- Retention: last 48 hours hot, last 30 days warm, everything cold

**Model Artifacts:**
- Trained model weights: 1-4× parameter count depending on format
- Multiple quantized versions per model (FP16, FP8, INT4)
- Fine-tuned variants: many versions per base model

### Capacity Planning Formula

```
Hot Storage Capacity =
  Training Data (active datasets)
  + Checkpoints (48-hour rolling window × checkpoint size × frequency)
  + Model Artifacts (current models × versions × quantization variants)
  + Working Space (scratch, temp files, logs) — typically 20% of above
  + Headroom (30% free space for performance)

Example: 1,024 H100 cluster training 70B model
  Training data: 5 TB
  Checkpoints: 48 hours × 2/hour × 560 GB = 53.8 TB
  Model artifacts: 5 TB
  Working space: 12.8 TB
  Headroom: 23 TB
  Total hot storage: ~100 TB (modest for this scale)

Example: 1,024 H100 cluster training 405B model
  Training data: 20 TB
  Checkpoints: 48 hours × 4/hour × 3.2 TB = 614 TB
  Model artifacts: 20 TB
  Working space: 131 TB
  Headroom: 236 TB
  Total hot storage: ~1 PB
```

## 2. Parallel File Systems

### Why Parallel File Systems for AI

Standard NFS/CIFS cannot sustain the I/O rates AI training requires:
- 1,024 GPUs each need to read training data simultaneously
- Checkpoint writes: entire cluster writes 560 GB - 3.2 TB in seconds
- Standard NFS: 2-10 GB/s per server → bottleneck at ~64 GPUs
- Parallel FS: 100-500+ GB/s aggregate → scales to thousands of GPUs

### WEKA (WekaIO)

**Position:** Leading software-defined parallel file system for AI. Dominant in new AI cluster deployments.

**Architecture:**
- Distributed NVMe-native file system
- Data striped across all nodes for maximum parallelism
- Tiering: NVMe (hot) → SSD (warm) → S3 (cold) — automatic
- POSIX-compatible (works with any training framework)
- S3 gateway for object access

**Key Specifications:**
- Throughput: 100+ GB/s per cluster (demonstrated at meta-scale)
- Latency: <200 µs read (NVMe tier)
- Scale: petabytes of capacity, thousands of clients
- Protocol: POSIX, NFS, SMB, S3

**Strengths:**
- Purpose-built for AI/ML workloads
- NVMe-native (not adapted from HDD-era design)
- Excellent small-file random I/O (important for data loading)
- NVIDIA DGX SuperPOD validated and recommended
- Active-active metadata (no single metadata bottleneck)

**Weaknesses:**
- Premium pricing (reflects performance)
- Smaller installed base than Lustre/GPFS
- Vendor lock-in (proprietary)

### VAST Data

**Position:** Universal storage platform with strong AI credentials. Competes with WEKA in new deployments.

**Architecture:**
- Disaggregated Shared Everything (DASE) architecture
- NVMe storage servers + QLC flash + optional HDD
- Global namespace across all data
- Native multi-protocol: NFS, SMB, S3

**Key Specifications:**
- Throughput: 80-200+ GB/s per cluster
- Latency: <250 µs read
- Scale: exabyte-class namespace
- Compression/dedup: inline, global, always-on

**Strengths:**
- Excellent data reduction (inline compression + dedup)
- Unified data lake approach (one namespace for all data)
- Strong multi-tenancy (QoS per tenant)
- Cost-effective at large capacity (QLC flash + dedup)

**Weaknesses:**
- Higher latency than WEKA for small random I/O
- Newer to pure AI workloads (heritage in enterprise/media)

### Lustre

**Position:** Open-source HPC parallel file system. 20+ year heritage, proven at extreme scale.

**Architecture:**
- Metadata Servers (MDS) + Object Storage Servers (OSS)
- Data striped across OSS nodes
- POSIX-compatible
- Open source with commercial support (DDN, HPE)

**Key Specifications:**
- Throughput: 1+ TB/s demonstrated at national labs
- Scale: exabyte class
- Installed base: majority of TOP500 supercomputers

**Strengths:**
- Proven at the largest scales on Earth
- Open source (no vendor lock-in)
- DDN EXAScaler provides hardened commercial distribution
- Lowest cost per TB at extreme capacity

**Weaknesses:**
- HDD-era architecture (not NVMe-native — bolt-on NVMe support)
- Metadata bottleneck at high file counts (single MDS, clustering improves this)
- Operational complexity (requires dedicated storage admin expertise)
- Less suited for mixed protocol (limited S3 support)

### IBM Storage Scale (GPFS / Spectrum Scale)

**Position:** Enterprise-grade parallel file system with AI workload support.

**Strengths:** Mature, production-proven, strong in regulated industries.
**Weaknesses:** Complex licensing, heavy operational overhead, IBM ecosystem dependency.

### DEC Storage Recommendation

**For DEC tenants (most common):**
1. **WEKA** for performance-focused training clusters (SuperPOD-validated, NVMe-native)
2. **VAST** for mixed training/inference with large dataset diversity (data reduction, multi-tenancy)
3. **Lustre (DDN EXAScaler)** for cost-sensitive large-capacity deployments

**DEC provides:** Physical space for storage racks, power, cooling, structured cabling. Storage is tenant-owned and tenant-managed.

**Storage placement:** Dedicated storage room adjacent to data hall (not inside data hall):
- Different cooling requirements (storage = air-cooled, lower density than GPU racks)
- Different power profile (steadier than GPU racks)
- Fiber connectivity to data hall via structured cabling

## 3. Data Pipeline Architecture

### Training Data Pipeline

```
Raw Data (internet, proprietary, licensed)
  │
  ▼
Data Ingestion (download, receive, ingest into object store)
  │  → Cold/Warm storage (Tier 2-3)
  │
  ▼
Data Processing (cleaning, dedup, filtering, quality scoring)
  │  → CPU cluster (not GPU) — can be same nodes or separate
  │  → Frameworks: Apache Spark, Ray Data, Dask, custom Python
  │
  ▼
Tokenization (text → token IDs, format for training)
  │  → CPU cluster
  │  → Output: binary files (memmap, Arrow, safetensors)
  │
  ▼
Data Staging (copy processed data to hot storage)
  │  → Parallel FS (WEKA, VAST, Lustre)
  │  → Pre-training: stage full dataset
  │
  ▼
Data Loading (feed data to GPUs during training)
     → PyTorch DataLoader with multi-worker prefetch
     → NVIDIA DALI (GPU-accelerated data loading pipeline)
     → Goal: GPU never waits for data (zero data stall)
```

### Data Loading Performance

**The bottleneck equation:**

```
Required read throughput = batch_size × sample_size × steps_per_second

Example: 1,024 GPU training, global batch size 4M tokens, sequence length 4K
  Micro-batch per GPU: ~4K tokens
  Sample size: 4K × 2 bytes = 8 KB per sample
  Steps per second: ~0.5 (2 seconds per step)
  Per-GPU read rate: 4 KB/s (trivial)
  Aggregate: 1,024 × 4 KB/s = 4 MB/s (trivial for text training)
```

**Text training is NOT storage-bandwidth-bound.** The bottleneck is compute and network, not data I/O.

**Multimodal training IS storage-bandwidth-bound:**
- Image tokens are much larger (256 KB - 2 MB per image)
- Video training: GB per sample
- Required aggregate read throughput: 10-100 GB/s

### Checkpoint Pipeline

```
GPU Memory (model + optimizer state)
  │
  ▼
CPU Memory (async copy from GPU, training continues)
  │
  ▼
Local NVMe (optional: write locally first for speed)
  │
  ▼
Parallel File System (durable checkpoint, all shards gathered)
  │
  ▼
Object Store (archive: older checkpoints moved to cold storage)
```

**Checkpoint I/O Requirements:**

| Model | Checkpoint Size | Write Duration Target | Required Write BW |
|---|---|---|---|
| 70B | 560 GB | <60 sec | ~10 GB/s |
| 405B | 3.2 TB | <120 sec | ~27 GB/s |
| 1T | 8 TB | <180 sec | ~45 GB/s |

These are aggregate write bandwidths across all storage nodes. Modern parallel file systems handle this comfortably.

## 4. Storage Networking

### Storage Network Design

```
GPU Nodes (128 nodes)          Storage Nodes (16 nodes)
  │ 100-400 GbE NICs              │ 100-400 GbE NICs
  │                                │
  └──── Ethernet Leaf ─────── Ethernet Leaf ────┘
              │                        │
              └─── Ethernet Spine ─────┘
```

**Key design decisions:**

**Bandwidth per GPU node:**
- Text training: 25 GbE per node sufficient (data loading is lightweight)
- Multimodal training: 100-400 GbE per node (high data throughput)
- Checkpoint-heavy workloads: 100 GbE per node minimum

**Storage-to-compute bandwidth ratio:**
- Rule of thumb: aggregate storage network bandwidth ≥ 10% of compute fabric bandwidth
- Example: 1,024 GPU cluster with 400 Gb/s IB per GPU = 400 Tb/s compute fabric → storage network ≥ 40 Tb/s = 100× 400 GbE links

**DEC structured cabling:**
- Separate cable tray for storage network (Ethernet) vs compute fabric (InfiniBand)
- Storage fiber from GPU racks to storage room: OM4 multimode sufficient for <100 m
- Pre-plan fiber count: 4-8 fibers per GPU node for storage (duplex LC or MPO)

## 5. Object Storage for AI

### S3-Compatible Object Storage

Even clusters with parallel file systems need object storage for:
- Raw data lake (pre-processing)
- Dataset versioning and lineage
- Model artifact registry
- Checkpoint archive (warm/cold tier)
- Multi-site replication and DR

### MinIO (Open Source / Commercial)

**Position:** Leading S3-compatible object store for on-premises AI.

**Key features:**
- Full S3 API compatibility
- Erasure coding for durability
- Bucket versioning, lifecycle policies
- Performance: 300+ GB/s demonstrated on NVMe
- Simple deployment (single binary, no JVM dependencies)

**When to use:** Default choice for on-prem S3-compatible storage. Proven at scale.

### Ceph (Open Source)

**Position:** Unified storage (block + file + object) for large-scale deployments.

**Key features:**
- S3-compatible (RadosGW)
- CephFS for POSIX file access
- RBD for block storage (VM images, etc.)
- Strong consistency, automatic rebalancing

**When to use:** When unified storage (file + object + block) is needed and operational complexity is acceptable.

## 6. Data Management for Multi-Tenant

### DEC Multi-Tenant Storage Considerations

**Physical isolation:**
- Each tenant has their own storage racks in their cage/room
- No shared storage infrastructure between tenants
- DEC provides power and cooling; tenant provides all storage equipment

**Shared storage (rare, only for managed services):**
- If DEC offers managed storage as a service → must provide:
  - Per-tenant QoS (IOPS, bandwidth, capacity quotas)
  - Data isolation (encryption at rest, separate namespaces)
  - Metering for billing (per-TB, per-IOPS)
- Most neocloud tenants will bring their own storage (they have opinions)

### Dataset Licensing and Sovereignty

**Data sovereignty considerations for NL-based DEC:**
- GDPR applies to personal data stored in EU
- Some tenants train on proprietary/licensed data — needs physical security guarantees
- Some tenants require data not to leave the EU (sovereign cloud requirements)
- NL has no additional data localization beyond GDPR (unlike DE, FR)

**DEC's role:** Provide physically secure cages with access control. Tenant responsible for all data management, encryption, compliance.

## 7. Emerging Storage Technologies

### CXL Memory Expansion

**Compute Express Link (CXL) 3.0:**
- Extends memory pool beyond GPU/CPU local memory
- Memory pooling: shared memory across multiple hosts
- Potential to replace some hot storage tier with CXL-attached memory
- Timeline: early products 2025-2026, mainstream 2027+

**AI relevance:**
- KV-cache expansion for inference (avoid model quantization)
- Checkpoint acceleration (write to CXL memory instead of NVMe)
- Disaggregated compute: separate memory pools from compute
- Broadcom and Samsung leading commercialization

### GPU-Direct Storage

**NVIDIA GPUDirect Storage:**
- DMA from NVMe/NFS directly to GPU memory (bypasses CPU bounce buffer)
- Reduces data loading latency by 2-5×
- Supported by WEKA, VAST, DDN, NVIDIA Magnum IO
- Requires cuFile library and compatible storage system

**When it matters:**
- Multimodal training (large images/video)
- Checkpoint writes (GPU → storage without CPU copy)
- NOT critical for text-only LLM training (data is tiny)

### Persistent Memory (PMem)

- Intel Optane PMem was promising but discontinued (2022)
- CXL-attached persistent memory may revive the concept
- Not a factor in current deployments

## 8. Storage Power and Thermal Characteristics

### Storage Power Profile

| Storage Type | Power per Rack | Cooling | Power Variability |
|---|---|---|---|
| All-NVMe (WEKA/VAST) | 15-25 kW | Air-cooled (standard) | Low (steady I/O pattern) |
| Hybrid NVMe + SSD | 10-20 kW | Air-cooled | Low |
| HDD-based (archive) | 5-15 kW | Air-cooled | Very low |
| GPU node NVMe (local) | Included in GPU rack power | Liquid-cooled (with GPU) | Follows GPU pattern |

**DEC Implication:**
- Storage racks are air-cooled (no liquid cooling needed)
- Lower power density than GPU racks → can be placed in conventional data hall areas
- Storage power is steady and predictable → minor contributor to heat recovery
- Storage room adjacent to data hall: separate air cooling, standard raised floor acceptable

### Storage Noise

Storage systems generate negligible noise compared to dry coolers or generators. Not a factor in acoustic engineering for DEC facilities.

## Cross-References
- See [gpu-accelerator-hardware.md](gpu-accelerator-hardware.md) for GPU memory specifications and GPUDirect Storage support
- See [cluster-networking.md](cluster-networking.md) for storage network design and bandwidth requirements
- See [cluster-orchestration.md](cluster-orchestration.md) for burst buffer integration with SLURM and data staging
- See [training-workloads.md](training-workloads.md) for checkpoint frequency, size, and data loading requirements
- See [inference-serving.md](inference-serving.md) for model artifact storage and serving requirements
- See companion skill `dc-engineering`:
  - [data-hall-design.md] for storage room adjacency and layout
  - [electrical-power-systems.md] for storage rack power delivery
  - [structured-cabling-connectivity.md] for storage network fiber routing
- See companion skill `site-development` for storage cost in financial modeling
