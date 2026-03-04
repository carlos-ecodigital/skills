# Distributed Training Workloads

## 1. Training Fundamentals

### What Happens During Training

At its core, LLM training is a massive iterative computation:

```
For each batch of training data:
  1. Forward pass: push data through model, compute predictions
  2. Loss computation: compare predictions to ground truth
  3. Backward pass: compute gradients (how to adjust each parameter)
  4. Gradient synchronization: average gradients across all GPUs (AllReduce)
  5. Optimizer step: update parameters using averaged gradients
  6. Repeat
```

Step 4 — gradient synchronization — is what makes training a distributed systems problem and what drives all networking, topology, and orchestration requirements.

### Scale of Modern Training

| Model | Parameters | Training Tokens | GPU-Hours | GPU Type | Est. Cost |
|---|---|---|---|---|---|
| GPT-3 (2020) | 175B | 300B | ~3.6M | V100 | ~$4.6M |
| LLaMA 2 70B (2023) | 70B | 2T | ~1.7M | A100 80GB | ~$3.4M |
| LLaMA 3 405B (2024) | 405B | 15T | ~30M | H100 | ~$60M+ |
| Frontier models (2025) | 1-10T | 10-30T | 50-200M | H100/B200 | $100M-$1B+ |

**DEC Implication:** A single training run on 1,024 H100 GPUs at 85% utilization produces:
- ~3.4 MW continuous power draw
- ~2.9 MW continuous heat output (recoverable)
- For 30-90 days continuously
- This is the ideal heat recovery scenario: steady, predictable, high-utilization

## 2. Parallelism Strategies

### The Parallelism Hierarchy

No single GPU can hold a frontier model. Parallelism is required at multiple levels:

```
Cluster Level:     Data Parallelism (DP)     — replicate model, split data
                         ↓
Node Level:        Tensor Parallelism (TP)    — split individual layers across GPUs
                         ↓
Pipeline Level:    Pipeline Parallelism (PP)   — split model layers across GPU groups
                         ↓
Sequence Level:    Sequence Parallelism (SP)   — split long sequences across GPUs
                         ↓
Expert Level:      Expert Parallelism (EP)     — MoE experts on different GPUs
```

### Data Parallelism (DP)

**How it works:** Each GPU holds a complete copy of the model. Training data is split across GPUs. After each forward/backward pass, gradients are averaged across all GPUs via AllReduce.

**Communication pattern:** AllReduce after every training step
- Volume: 2 × model_size × sizeof(parameter) per step
- Example: 70B model, bf16: 2 × 70B × 2 bytes = 280 GB per AllReduce
- At NDR 400 Gb/s: ~5.6 seconds per AllReduce (overlapped with compute in practice)

**When to use:** When model fits in single GPU memory (after activation checkpointing)
- Works well up to ~13B parameters on H100 80GB
- Beyond that: combine with TP/PP

**Variants:**
- **FSDP (Fully Sharded Data Parallel):** PyTorch native. Shards model parameters, gradients, and optimizer states across GPUs. Each GPU only holds 1/N of the model. Gathers full parameters just-in-time for forward/backward, then re-shards.
- **ZeRO (Zero Redundancy Optimizer):** DeepSpeed's equivalent to FSDP. Three stages: ZeRO-1 (shard optimizer states), ZeRO-2 (shard gradients), ZeRO-3 (shard parameters).

### Tensor Parallelism (TP)

**How it works:** Individual weight matrices are split across GPUs. Each GPU computes a portion of each layer, then results are combined via AllReduce.

**Communication pattern:** AllReduce within each transformer layer (2× per layer — after attention and after MLP)
- Very latency-sensitive: AllReduce is on the critical path of every layer
- Requires NVLink bandwidth (not feasible over InfiniBand — too slow)

**Constraint:** TP degree is limited to GPUs within a single NVLink domain:
- DGX H100: TP ≤ 8 (8 GPUs per NVLink domain)
- GB200 NVL72: TP ≤ 72 (72 GPUs per NVLink domain)

**NVL72 Impact:** The 72-GPU NVLink domain is transformative:
- 405B model with TP=72 needs no pipeline parallelism — entire model fits within one NVLink domain
- Eliminates pipeline bubble (see PP section below)
- This is why GB200 NVL72 is not just a faster GPU but a fundamentally different training architecture

### Pipeline Parallelism (PP)

**How it works:** Model layers are divided into stages, each stage on a different GPU group. Micro-batches flow through the pipeline.

**Communication pattern:** Point-to-point (send activations forward, send gradients backward)
- Lower bandwidth requirement than DP or TP
- Can run over InfiniBand (does not require NVLink)

**Pipeline bubble:** With naive PP, GPUs idle while waiting for earlier stages to complete. Techniques to reduce bubble:
- **1F1B (One Forward One Backward):** interleave forward and backward passes to keep pipeline full
- **Interleaved PP:** assign non-contiguous layers to each stage
- **Zero-bubble PP:** academic research (2024) achieving near-zero bubble at cost of complexity

**Typical bubble overhead:** 10-25% GPU utilization loss

**When to use:** When model doesn't fit in a single NVLink domain
- Example: 1T model on H100 DGX (8 GPU NVLink domain): TP=8, PP=16 (16 pipeline stages across 16 nodes), DP=remaining GPUs

### Sequence Parallelism (SP)

**How it works:** For very long sequences (>8K tokens), the sequence dimension is split across GPUs. Each GPU processes a portion of the sequence.

**Communication pattern:** AllGather before attention (each GPU needs full sequence for attention computation), ReduceScatter after
- Communication volume scales with sequence length
- Critical for context window >32K tokens

**When to use:** Training with long context windows (32K-128K+)

### Expert Parallelism (EP) — Mixture of Experts

**How it works:** In MoE models, different experts are placed on different GPUs. A router selects which experts process each token.

**Communication pattern:** All-to-All (tokens routed to specific expert GPUs, results routed back)
- Communication pattern is irregular (depends on router decisions)
- Load balancing is critical — imbalanced routing wastes GPU capacity

**Examples:** Mixtral 8×7B, GPT-4 (rumored MoE), DeepSeek V3

### Typical Parallelism Configuration

**70B model on 256 H100 GPUs (32 nodes × 8 GPU):**
- TP = 8 (within NVLink domain)
- PP = 1 (model fits in 8 GPUs with FSDP)
- DP = 32 (32 replicas across 32 nodes)
- Communication: AllReduce across 32 nodes per step (over InfiniBand)

**405B model on 1,024 H100 GPUs (128 nodes × 8 GPU):**
- TP = 8 (within NVLink domain)
- PP = 4 (4 pipeline stages, each stage = 8 GPUs)
- DP = 32 (32 replicas)
- Communication: AllReduce within each pipeline stage (IB), point-to-point between stages (IB)

**405B model on 1,008 GB200 NVL72 (14 racks × 72 GPU):**
- TP = 72 (entire model within one NVLink domain!)
- PP = 1 (no pipeline parallelism needed)
- DP = 14 (14 replicas across 14 racks)
- Communication: AllReduce across 14 racks (IB) — dramatically simpler than H100 configuration

## 3. Communication Patterns & Network Requirements

### AllReduce Deep Dive

AllReduce is the dominant communication pattern in data-parallel training:

**Ring AllReduce:**
- GPUs arranged in logical ring
- Each GPU sends/receives chunks to/from neighbors
- 2×(N-1)/N × data_size total traffic, in N-1 steps
- Bandwidth-optimal but latency scales with ring size

**Tree AllReduce:**
- Hierarchical reduction: intra-node (NVLink) → inter-node (InfiniBand)
- Lower latency than ring for small messages
- NCCL automatically selects ring vs tree based on message size

**SHARP (In-Network AllReduce):**
- InfiniBand switches perform partial reduction
- Reduces required bandwidth by 2-3x
- Only available on NVIDIA InfiniBand (Quantum-2+)
- This is the primary technical argument for InfiniBand over Ethernet for training

### Bandwidth Requirements by Model Size

| Model Size | AllReduce Volume/Step | Required BW (1% overhead target) | Recommended |
|---|---|---|---|
| 7B | 28 GB | 100 Gb/s | 1× NDR 400G (comfortable) |
| 70B | 280 GB | 400 Gb/s | 1× NDR 400G per GPU |
| 405B | 1.6 TB (with PP) | 400-800 Gb/s | 1× NDR/XDR per GPU |
| 1T+ | 4+ TB | 800 Gb/s+ | 1× XDR per GPU + SHARP |

### Communication-Computation Overlap

Modern training frameworks overlap communication with computation:
- While GPU computes backward pass for layer N, it simultaneously sends gradients for layer N+1
- Effective communication overhead can be 5-15% (not the full AllReduce time)
- Overlap efficiency depends on: gradient bucketing strategy, network bandwidth, compute-to-communication ratio

**DEC Relevance:** Higher network bandwidth → better overlap → higher effective GPU utilization → steadier power draw → more predictable heat output

## 4. Training Frameworks

### PyTorch (Dominant)

**PyTorch Distributed (torch.distributed):**
- NCCL backend for GPU communication (de facto standard)
- DistributedDataParallel (DDP) for simple data parallelism
- FSDP for sharded data parallelism
- DeviceMesh for multi-dimensional parallelism (TP + PP + DP)

**PyTorch 2.x Features:**
- `torch.compile` for kernel fusion and optimization
- `torch.distributed.checkpoint` for efficient distributed checkpointing
- `DTensor` for expressing tensor parallelism natively

### DeepSpeed (Microsoft)

- ZeRO stages 1/2/3 for memory optimization
- ZeRO-Infinity: offload to CPU/NVMe (extends to multi-trillion parameter models)
- DeepSpeed-MoE: optimized expert parallelism
- Widely used in research and some production training

### Megatron-LM (NVIDIA)

- NVIDIA's reference framework for large-scale training
- Native TP + PP + DP + SP + EP
- Optimized for NVIDIA hardware (NVLink, SHARP)
- Highest performance on NVIDIA DGX/HGX systems
- Less portable than PyTorch/DeepSpeed (NVIDIA-specific optimizations)

### JAX (Google)

- Functional programming model with automatic parallelism (pjit/shard_map)
- XLA compiler for hardware-specific optimization
- Dominant at Google (PaLM, Gemini trained on JAX + TPU)
- Growing adoption on GPU clusters
- More complex programming model but potentially higher performance

### DEC Tenant Framework Distribution (Estimated)

| Framework | Tenant Type | Prevalence |
|---|---|---|
| PyTorch + FSDP/DDP | Most tenants | 60-70% |
| Megatron-LM | NVIDIA-aligned, performance-focused | 15-20% |
| DeepSpeed | Research labs, Microsoft-ecosystem | 10-15% |
| JAX | Google-ecosystem, research | 5-10% |

## 5. Checkpointing & Fault Tolerance

### Why Checkpointing Matters

At scale, hardware failures are not exceptional — they are routine:

| Cluster Size | Mean Time Between GPU Failure | Checkpoint Frequency Needed |
|---|---|---|
| 64 GPUs | ~30 days | Every 4-8 hours |
| 512 GPUs | ~4 days | Every 1-2 hours |
| 4,096 GPUs | ~12 hours | Every 15-30 minutes |
| 32,768 GPUs | ~1.5 hours | Every 5-10 minutes |

**Without checkpointing:** A GPU failure at hour 23 of a 24-hour training segment loses all 23 hours of compute. At $2-3/GPU-hour, a 4,096 GPU cluster loses $200K-$300K per failure without checkpoints.

### Checkpoint Types

**1. Full Checkpoint:**
- Save all model parameters, optimizer state, learning rate schedule, RNG state, data loader position
- Size: ~4× model parameters (model + optimizer states)
- 70B model: ~560 GB per checkpoint
- 405B model: ~3.2 TB per checkpoint

**2. Sharded Checkpoint (Recommended):**
- Each GPU saves its shard of the model/optimizer
- Parallel I/O: all GPUs write simultaneously
- Reconstruct full checkpoint by gathering shards
- PyTorch `torch.distributed.checkpoint` or DeepSpeed checkpoint engine

**3. Async Checkpoint (Emerging Best Practice):**
- Copy GPU state to CPU memory, then write to storage asynchronously
- Training continues while checkpoint is being written
- Minimal training throughput impact (~1-3% vs 5-15% for synchronous)

### Checkpoint Storage Requirements

| Model | Checkpoint Size | Frequency | Daily Storage | 30-Day Training |
|---|---|---|---|---|
| 70B | 560 GB | Hourly | 13.4 TB | 403 TB |
| 405B | 3.2 TB | 30 min | 153 TB | 4.6 PB |
| 1T | 8 TB | 15 min | 768 TB | 23 PB |

**Checkpoint storage hierarchy:**
1. **Hot:** Local NVMe SSD (fastest write, limited capacity) — last 2-3 checkpoints
2. **Warm:** Parallel file system (WEKA, VAST, Lustre) — last 24-48 hours of checkpoints
3. **Cold:** Object storage (S3, MinIO) — all historical checkpoints

### Failure Recovery

**Elastic training (PyTorch Elastic / TorchElastic):**
- Detect node failure → exclude failed node → redistribute work → resume from last checkpoint
- Requires spare nodes (N+1 or N+2 allocation)
- Resume time: checkpoint load (minutes) + warmup (minutes) = 5-15 minutes typical

**SLURM integration:**
- `--requeue` flag: failed jobs automatically requeued
- `--checkpoint-dir`: SLURM manages checkpoint directory
- Pre-emption: lower-priority jobs checkpointed and requeued when higher-priority jobs arrive

**DEC Relevance to Fault Tolerance:**
- GPU failure → sudden rack power drop → CDU flow adjustment → heat recovery variability
- Mass failure (driver bug, network partition) → cluster-wide power drop → facility cooling must handle rapid transient
- DEC should understand: "when tenants tell us they're doing a driver update on 512 GPUs, expect 30 minutes of zero load followed by gradual ramp-up"

## 6. Power & Thermal Profiles During Training

### Training Power Characteristics

**Steady-State Training:**
- GPU utilization: 85-95% TDP
- Power draw: remarkably stable (±5% variation between training steps)
- Perfect for heat recovery: predictable, continuous thermal output
- Duration: days to months continuously

**Checkpoint Phase:**
- Brief GPU utilization dip to 30-50% during synchronous checkpoint
- Duration: 30-120 seconds per checkpoint
- If async checkpoint: no measurable dip

**Inter-Job Gaps:**
- Between training runs: GPUs idle (5-10% TDP)
- Duration: minutes to hours (job scheduling, data staging, configuration)
- DEC must handle these thermal transients (buffer tank sizing, see dc-engineering heat-recovery)

### Power Profile by Training Phase

```
Power (MW)
3.5 |                    ┌──────────────────────────────────────────┐
3.0 |                    │  Steady-state training (85-95% TDP)      │
2.5 |             ┌──────┘                                          │
2.0 |      ┌──────┘ Ramp-up                                        │
1.5 |      │ (NCCL init,                                            │
1.0 |      │  data loading)                    Checkpoint dips (─)  │
0.5 |──────┘                                                        └──
    └──────┬──────┬──────────────────────────────────────────────┬──────
           0    15min              Training duration              End
```

### Thermal Output Calculation

**For DEC heat recovery planning:**

```
Thermal output (MW) ≈ IT Power (MW) × GPU Utilization × (1 - cooling overhead)

Example: 1,024 H100 cluster
- IT Power: 128 nodes × 10.2 kW/node = 1,306 kW per node (incl. CPU, RAM, NIC, fans)
  Approximate total: ~4.0 MW (including networking switches, storage)
- Training utilization: 90% average
- Thermal output to liquid cooling: ~3.0-3.4 MW (75-85% captured by liquid cooling)
- Thermal output to air: ~0.4-0.6 MW (15-25% from CPUs, RAM, fans, cables)
- Recoverable heat for greenhouse: ~3.0-3.4 MW continuous during training
```

## 7. Training Optimization Techniques

### Mixed Precision Training

**BF16 (Brain Floating Point 16):**
- Standard for modern LLM training
- 8 exponent bits (same dynamic range as FP32), 7 mantissa bits
- Halves memory and doubles throughput vs FP32
- H100/B200 Tensor Cores optimized for bf16

**FP8 (8-bit Floating Point):**
- Emerging: Hopper (H100) introduced FP8 Tensor Cores
- 2× throughput vs bf16, 4× vs FP32
- Requires careful loss scaling and format selection (E4M3 for forward, E5M2 for backward)
- Not yet standard for pre-training; common for fine-tuning

### Gradient Accumulation

- Simulate larger batch sizes without more GPUs
- Accumulate gradients over K micro-batches before AllReduce
- Reduces communication frequency by K×
- Trade-off: reduces communication overhead but increases memory per GPU

### Activation Checkpointing

- Don't store all intermediate activations during forward pass
- Recompute activations during backward pass (trade compute for memory)
- Reduces activation memory from O(layers) to O(√layers)
- Standard practice for training models >13B parameters
- Increases compute by ~33% but enables training much larger models per GPU

### Flash Attention

- Fused attention kernel that avoids materializing N×N attention matrix
- Reduces attention memory from O(N²) to O(N) where N = sequence length
- 2-4× speedup for attention computation
- Standard in all modern training pipelines (Tri Dao, Princeton/Stanford)
- Flash Attention 3 (2024): further optimized for Hopper architecture

## Cross-References
- See [gpu-accelerator-hardware.md](gpu-accelerator-hardware.md) for GPU specifications, memory capacity, and NVLink topology that constrain parallelism choices
- See [cluster-networking.md](cluster-networking.md) for AllReduce bandwidth requirements, SHARP, and topology design
- See [cluster-orchestration.md](cluster-orchestration.md) for SLURM topology-aware scheduling and job management
- See [inference-serving.md](inference-serving.md) for how trained models are deployed for inference (different parallelism and communication patterns)
- See [ai-storage-data.md](ai-storage-data.md) for checkpoint storage architecture and data pipeline design
- See companion skill `dc-engineering`:
  - [heat-recovery-integration.md] for thermal output calculations and heat recovery from training workloads
  - [electrical-power-systems.md] for power delivery to training clusters
- See companion skill `energy-markets` for energy procurement strategies for continuous training loads
