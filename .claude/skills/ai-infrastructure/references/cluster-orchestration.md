# AI Cluster Orchestration & Resource Management

## 1. Orchestration Landscape

### Two Paradigms

AI cluster orchestration splits into two fundamentally different approaches:

**1. SLURM (Simple Linux Utility for Resource Management):**
- HPC-native batch scheduler, dominant in AI training
- Job-centric: users submit jobs, SLURM allocates resources, job runs to completion or failure
- 30+ years of HPC heritage, rock-solid at scale
- NVIDIA's reference platform for DGX SuperPOD
- Best for: large training jobs, single-tenant or research clusters, maximum GPU utilization

**2. Kubernetes with GPU Operators:**
- Cloud-native container orchestration, dominant in inference serving
- Service-centric: long-running services with autoscaling, health checks, rolling updates
- 10 years of cloud heritage, massive ecosystem
- Best for: inference serving, mixed workloads, multi-tenant platforms, CI/CD integration

### DEC Colocation Implication
DEC provides physical infrastructure; tenants choose their own orchestration stack. However, DEC must understand both paradigms to:
1. Design facility infrastructure that supports either (power density, cooling, network topology)
2. Advise tenants on infrastructure requirements per workload type
3. Understand tenant monitoring/alerting needs that intersect with facility systems (power, cooling, network)

## 2. SLURM for AI Training

### Architecture

```
SLURM Controller (slurmctld)
  ├── SLURM Database (slurmdbd) → MariaDB/MySQL
  ├── Accounting & Fair-Share
  └── Job Queue
        ├── Partition: training-h100 (high-priority, 512 GPUs)
        ├── Partition: training-b200 (premium, 256 GPUs)
        ├── Partition: dev (preemptible, 64 GPUs)
        └── Partition: inference (low-priority, 128 GPUs)

Compute Nodes (slurmd per node)
  ├── GPU Resource: gres/gpu:h100:8
  ├── Network Resource: gres/nic:ib:8
  └── Storage Mount: /scratch (parallel FS)
```

### Key SLURM Features for AI

**GPU-Aware Scheduling (GRES):**
- `GresTypes=gpu` in slurm.conf
- Each GPU is a schedulable resource: `--gres=gpu:h100:8` requests 8 H100 GPUs
- GPU binding: `--gpu-bind=closest` ensures GPU-CPU NUMA affinity
- MIG (Multi-Instance GPU) support: schedule sub-GPU slices for inference/dev

**Topology-Aware Scheduling:**
- Critical for rail-optimized networks (see cluster-networking.md)
- `topology.conf` defines switch hierarchy: leaf → spine → super-spine
- `TopologyPlugin=topology/tree` enables topology-aware placement
- SLURM places multi-node jobs on nodes sharing the fewest switch hops
- Without topology awareness: 20-40% training performance degradation from cross-spine AllReduce

**Multi-Instance GPU (MIG) for Mixed Workloads:**
- H100 supports 7 MIG instances (up to 7 independent GPU slices)
- Useful for inference, development, small experiments
- SLURM GRES can schedule individual MIG instances
- Not applicable to NVL72 (NVLink domain requires full GPU allocation)

**Burst Buffer & I/O Staging:**
- `BurstBufferType=burst_buffer/lua` for checkpoint staging
- Pre-stage training data from parallel FS to local NVMe before job starts
- Stage-out checkpoints to parallel FS during job execution
- Reduces checkpoint I/O impact on training throughput

### SLURM at Scale — Operational Reality

| Cluster Size | Controller Nodes | Scheduling Latency | Key Challenge |
|---|---|---|---|
| <500 GPUs | 1 active + 1 standby | <1 sec | Straightforward |
| 500-5,000 GPUs | 2 active + 1 standby | 1-5 sec | Topology-aware placement complexity |
| 5,000-50,000 GPUs | Federated (multiple clusters) | 5-30 sec | Federation job routing, cross-cluster scheduling |
| >50,000 GPUs | Custom extensions (Meta, Google) | Minutes | SLURM hits limits; custom schedulers required |

**SLURM Alternatives at Extreme Scale:**
- Meta: custom scheduler for Grand Teton (>100K GPUs)
- Google: Borg (internal), not available externally
- xAI: custom for Colossus
- For DEC tenants (typically 500-10,000 GPUs): SLURM is appropriate

### SLURM Configuration for DEC Tenants

**Recommended slurm.conf Patterns:**

```
# GPU resource definition
GresTypes=gpu
NodeName=gpu[001-128] Gres=gpu:h100:8 CPUs=128 RealMemory=2048000

# Topology-aware scheduling
TopologyPlugin=topology/tree

# Fair-share (multi-user within tenant)
PriorityType=priority/multifactor
AccountingStorageType=accounting_storage/slurmdbd
PriorityWeightFairshare=10000
PriorityWeightAge=1000
PriorityWeightJobSize=500

# Health check (detect degraded GPUs)
HealthCheckProgram=/usr/local/bin/gpu_health_check.sh
HealthCheckInterval=300
HealthCheckNodeState=IDLE,MIXED

# Preemption for dev jobs
PreemptType=preempt/qos
PreemptMode=REQUEUE
```

## 3. Kubernetes for GPU Workloads

### NVIDIA GPU Operator Stack

```
Kubernetes Cluster
  └── NVIDIA GPU Operator (manages all GPU components)
        ├── NVIDIA Device Plugin (exposes GPUs to K8s scheduler)
        ├── NVIDIA Container Toolkit (GPU passthrough to containers)
        ├── NVIDIA DCGM Exporter (GPU metrics → Prometheus)
        ├── NVIDIA GFD (GPU Feature Discovery — labels nodes)
        ├── NVIDIA MPS Server (Multi-Process Service for inference)
        └── NVIDIA Network Operator (RDMA/InfiniBand for K8s pods)
```

### Key Kubernetes Features for AI

**Resource Requests and Limits:**
```yaml
resources:
  requests:
    nvidia.com/gpu: 8
    rdma/rdma_shared_device_a: 8
  limits:
    nvidia.com/gpu: 8
```

**Time-Slicing (Inference Density):**
- Multiple inference pods share a single GPU via time-slicing
- Lower latency than MIG (no hard partitioning), but no memory isolation
- Appropriate for inference workloads with variable load

**Multi-Instance GPU (MIG) in Kubernetes:**
- GFD discovers MIG profiles and labels nodes
- Pods request specific MIG profiles: `nvidia.com/mig-3g.40gb: 1`
- Provides memory isolation between inference workloads

**RDMA/InfiniBand in Kubernetes:**
- NVIDIA Network Operator manages RDMA device plugins
- Pods can request InfiniBand HCA access for training
- Requires host networking or macvlan for RDMA passthrough
- SR-IOV for multi-tenant InfiniBand access (limited adoption)

### Kubernetes Limitations for Training

1. **Scheduling granularity:** K8s scheduler is pod-centric, not job-centric — multi-node gang scheduling requires extensions (Volcano, Kueue)
2. **Topology awareness:** Native K8s scheduler is topology-unaware — requires custom scheduler or topology-aware plugins
3. **Checkpoint/restart:** No native support — requires integration with training framework (PyTorch elastic, DeepSpeed)
4. **GPU health management:** K8s doesn't natively handle degraded GPUs — requires custom node problem detector + drain automation

### Kubernetes for Training: Extensions

**Volcano (CNCF):**
- Gang scheduling: all pods in a job start together or none start
- Queue management with fair-share
- Topology-aware scheduling plugin
- Closest thing to "SLURM semantics on Kubernetes"

**Kueue (Kubernetes SIG):**
- Job queueing and admission control
- Resource quotas and fair-share across teams
- Integrates with JobSet for multi-node training
- Lighter weight than Volcano, Google-backed

**KubeFlow Training Operator:**
- Manages distributed training jobs (PyTorchJob, MPIJob, TFJob)
- Handles worker pod lifecycle, failure detection
- Integrates with Volcano/Kueue for scheduling

### DEC Recommendation: SLURM for Training, Kubernetes for Inference

**Training clusters:** SLURM
- Topology-aware scheduling is critical for training performance
- Gang scheduling is native (not an extension)
- GPU health management is mature
- NVIDIA's supported path for DGX/HGX systems

**Inference clusters:** Kubernetes
- Service-centric model matches inference serving pattern
- Autoscaling (HPA with GPU metrics) for variable inference load
- Rolling updates for model version deployment
- Rich ecosystem for API gateway, load balancing, monitoring

**Hybrid:** Some tenants run SLURM for training with Kubernetes on inference nodes in the same cluster. This is operationally complex but increasingly common. Run Kubernetes nodes as SLURM `--reservation` that K8s manages internally.

## 4. GPU Driver & Software Management

### NVIDIA Software Stack

```
Application (PyTorch, JAX, TensorFlow)
  └── NCCL (NVIDIA Collective Communications Library)
        └── cuDNN / cuBLAS / cuFFT
              └── CUDA Toolkit (compiler, runtime, libraries)
                    └── NVIDIA Driver (kernel module)
                          └── GPU Firmware
```

### Version Compatibility Matrix

**Critical principle:** The entire stack must be version-compatible. A driver/CUDA/NCCL mismatch is the #1 cause of mysterious training failures.

| Component | Update Frequency | Compatibility Window | Impact of Mismatch |
|---|---|---|---|
| GPU Firmware | Quarterly | Forward-compatible | Rare issues, but can cause ECC errors |
| NVIDIA Driver | Monthly | Must match CUDA minimum | Training crashes, silent data corruption |
| CUDA Toolkit | Quarterly | Must match driver + framework | Compilation failures, performance regression |
| NCCL | Quarterly | Must match CUDA + driver + topology | AllReduce hangs, deadlocks, performance collapse |
| cuDNN | Quarterly | Must match CUDA | Wrong results, performance regression |
| Framework (PyTorch) | Monthly | Must match CUDA + cuDNN | API breaks, operator failures |

### Driver Management Strategies

**1. Container-Based (Recommended for Multi-Tenant):**
- NVIDIA Container Toolkit mounts driver from host into container
- Tenant containers specify CUDA version; host driver must be compatible
- Driver updates require node drain + reboot
- Simplest for DEC tenants: "bring your own container, we provide driver-compatible hosts"

**2. Enroot + Pyxis (SLURM-Native Containers):**
- NVIDIA's container runtime for SLURM
- `srun --container-image=nvcr.io/nvidia/pytorch:24.01-py3 train.py`
- No Docker daemon required (security advantage)
- Better integration with SLURM than Docker/Podman

**3. Bare Metal + Environment Modules:**
- Traditional HPC approach: `module load cuda/12.4 nccl/2.20`
- Maximum performance (no container overhead, though overhead is minimal)
- Version conflict risk between users
- Appropriate for single-tenant research clusters

### GPU Health Management

**NVIDIA DCGM (Data Center GPU Manager):**
- Continuous GPU health monitoring: temperature, power, ECC errors, XID errors, NVLink status
- Policy engine: automatically drain nodes with degraded GPUs
- Integration with SLURM: mark nodes DRAIN when GPU health check fails
- Integration with Kubernetes: node problem detector triggers pod eviction

**Critical GPU Health Metrics:**

| Metric | Threshold | Action |
|---|---|---|
| GPU Temperature | >85°C sustained | Alert → investigate cooling |
| HBM Temperature | >95°C | Alert → reduce power cap or check CDU |
| ECC SRAM Errors (correctable) | >100/hour | Monitor → schedule maintenance |
| ECC SRAM Errors (uncorrectable) | Any | Immediate drain → RMA |
| NVLink CRC Errors | >10/minute | Drain → reseat/replace NVLink cable |
| XID 48 (DBE) | Any occurrence | Immediate drain → GPU reset or RMA |
| XID 79 (GPU fallen off bus) | Any occurrence | Reboot node → if recurring, RMA |
| PCIe Replay Count | Increasing | Monitor → reseat GPU or replace riser |

**DEC Relevance:** GPU health directly impacts facility operations:
- Degraded GPU = reduced power draw = reduced heat output = heat recovery variability
- Mass GPU failure (e.g., bad driver update) = sudden power drop = facility cooling overshoot
- DEC should monitor aggregate rack power as proxy for tenant cluster health

## 5. Multi-Tenant Resource Isolation

### Isolation Layers

| Layer | Technology | What It Isolates | DEC Responsibility |
|---|---|---|---|
| Physical | Separate racks/cages | Everything | Yes — DEC provides cages |
| Network | Separate IB subnets, VRF | Network traffic | DEC provides fiber; tenant provides switches |
| Compute | Separate SLURM/K8s clusters | Job scheduling, GPU allocation | Tenant responsibility |
| Storage | Separate namespaces/volumes | Data | Tenant responsibility |
| Power | Per-rack/per-cage metering | Energy billing | Yes — DEC meters and bills |
| Cooling | Per-rack CDU monitoring | Thermal SLA | Yes — DEC monitors facility water loop |

### DEC's Multi-Tenant Boundaries

**DEC provides:**
- Physical space (cages/halls) with power and cooling
- Structured cabling (fiber runs to tenant switches)
- Per-rack power metering (revenue-grade, see dc-engineering rack-power-metering)
- Facility water loop temperature/flow (CDU supply/return)
- Physical security (access control, CCTV)

**Tenant provides:**
- All active compute, network, and storage equipment
- Operating system, drivers, orchestration software
- Job scheduling, resource management, multi-user policies
- Application stack (frameworks, models, data)
- IT monitoring and alerting

**Shared/Negotiated:**
- Network meet-me room cross-connects (DEC provides MMR, tenant provides equipment)
- Carrier connectivity (DEC facilitates carrier access, tenant contracts directly)
- Emergency procedures (coordinated between DEC facility ops and tenant IT ops)

## 6. Monitoring & Observability Stack

### Tenant-Side Monitoring (Reference Architecture)

```
GPU Metrics:     DCGM Exporter → Prometheus → Grafana
                                              ↓
Node Metrics:    node_exporter → Prometheus → Grafana
                                              ↓
IB Metrics:      UFM → Prometheus adapter →  Grafana
                                              ↓
Job Metrics:     SLURM sacct / K8s metrics → Grafana
                                              ↓
Training Metrics: PyTorch/JAX callbacks →    Weights & Biases / MLflow / TensorBoard
                                              ↓
Alerting:        Prometheus Alertmanager →   PagerDuty / Slack / OpsGenie
```

### Key Dashboards

**1. Cluster Utilization:**
- GPU utilization % by node, partition, user
- GPU memory utilization (allocated vs used vs wasted)
- Job queue depth and wait time
- Fair-share balance across teams/users

**2. Training Health:**
- Iteration time (samples/sec) — trend should be flat; decline indicates degradation
- Loss curve — divergence indicates data/model/infrastructure issue
- AllReduce bandwidth per ring — should match theoretical peak within 10%
- Checkpoint duration and frequency

**3. Hardware Health:**
- GPU temperature heatmap (node × GPU)
- ECC error rate by node
- NVLink bandwidth and error rate
- Network link utilization and error rate
- Power consumption per rack (from DEC metering)

**4. Infrastructure (DEC-Facing):**
- Rack power consumption (kW) — real-time, per-tenant
- CDU supply/return temperature delta
- Facility water loop temperature and flow rate
- PUE calculation (real-time)

### DEC-Tenant Monitoring Interface

DEC and tenant monitoring systems must share specific data points:

| Data Point | Direction | Method | Purpose |
|---|---|---|---|
| Rack power (kW) | DEC → Tenant | API or dashboard | Tenant cost tracking |
| CDU water temp (°C) | DEC → Tenant | BMS API | Tenant thermal planning |
| GPU power (aggregate) | Tenant → DEC | Agreed API | DEC heat recovery planning |
| Planned maintenance | Both ways | Email/ticket | Coordination |
| Emergency shutdown | DEC → Tenant | Alerting system | Safety |

## Cross-References
- See [gpu-accelerator-hardware.md](gpu-accelerator-hardware.md) for GPU specifications, MIG capabilities, and thermal profiles
- See [cluster-networking.md](cluster-networking.md) for topology-aware scheduling requirements and multi-tenant network isolation
- See [training-workloads.md](training-workloads.md) for distributed training patterns that drive orchestration requirements
- See [inference-serving.md](inference-serving.md) for inference serving patterns and autoscaling requirements
- See [ai-storage-data.md](ai-storage-data.md) for storage integration with orchestration (burst buffer, data staging)
- See companion skill `dc-engineering`:
  - [electrical-power-systems.md] for rack power metering and PDU specifications
  - [data-hall-design.md] for cage/hall layout affecting tenant isolation
- See companion skill `site-development` for multi-tenant commercial model
