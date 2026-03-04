# Inference Serving & Optimization

## 1. Inference vs Training: Fundamental Differences

### Why Inference Is a Different Problem

| Dimension | Training | Inference |
|---|---|---|
| Objective | Maximize throughput (tokens/sec/GPU) | Minimize latency AND maximize throughput |
| Batch Size | Large (thousands of samples) | Small to medium (1-256 concurrent requests) |
| GPU Utilization | 85-95% sustained | 30-60% average, bursty |
| Duration | Days to months | Milliseconds to minutes per request |
| Communication | AllReduce-dominant (bandwidth-bound) | Minimal cross-GPU communication |
| Memory Bottleneck | Activation memory | KV-cache memory |
| Power Profile | Steady, predictable | Variable, follows request load |
| Economics | Cost per training run | Cost per token / cost per request |

### DEC Colocation Implication
Inference workloads create fundamentally different facility requirements than training:
- Variable power draw → variable heat output → harder to predict heat recovery
- Lower average GPU utilization → lower average power per rack → different electrical sizing
- Latency-sensitive → need low-latency network to end users (not just GPU-to-GPU)
- Higher tenant count per MW (more tenants running smaller inference clusters)

## 2. LLM Inference Mechanics

### Two Phases of LLM Inference

**Phase 1: Prefill (Prompt Processing)**
- Process all input tokens in parallel
- Compute-bound (matrix multiplications on full input)
- GPU utilization: 70-90%
- Duration: proportional to input length
- Similar to training forward pass

**Phase 2: Decode (Token Generation)**
- Generate tokens one at a time, autoregressively
- Memory-bandwidth-bound (reading full KV-cache for each new token)
- GPU utilization: 10-30% (most GPU compute is idle, waiting for memory)
- Duration: proportional to output length
- This is the fundamental bottleneck of LLM inference

### KV-Cache: The Memory Challenge

During decode, the model stores Key and Value tensors for all previous tokens. This KV-cache grows with:
- Sequence length (input + generated tokens)
- Number of attention heads
- Hidden dimension
- Number of layers

**KV-Cache Size Examples:**

| Model | Context | KV-Cache per Request | Max Concurrent (80 GB HBM) |
|---|---|---|---|
| LLaMA 70B | 4K tokens | ~2.5 GB | ~20 requests |
| LLaMA 70B | 32K tokens | ~20 GB | ~2-3 requests |
| LLaMA 405B (TP=8) | 4K tokens | ~1.8 GB per GPU | ~28 requests per GPU |
| LLaMA 405B (TP=8) | 128K tokens | ~58 GB per GPU | ~1 request per GPU |

**Key insight:** Long context windows dramatically reduce concurrent request capacity. A 405B model at 128K context can barely fit one request per GPU — completely impractical without optimization.

## 3. Inference Optimization Techniques

### Quantization

Reduce model precision to serve larger models or more concurrent requests:

| Technique | Precision | Model Size Reduction | Quality Impact | Speed Improvement |
|---|---|---|---|---|
| BF16 (baseline) | 16-bit | 1× | None | 1× |
| INT8 (W8A8) | 8-bit weights + activations | 2× | Minimal (<1% quality loss) | 1.5-2× |
| INT4 (W4A16) | 4-bit weights, 16-bit activations | 4× | Small (1-3% quality loss) | 2-3× |
| FP8 (W8A8) | 8-bit float | 2× | Negligible | 1.8-2.5× (with H100 FP8 cores) |
| GPTQ/AWQ | 4-bit weights (calibrated) | 4× | Small (calibration-dependent) | 2-3× |

**Recommendation for production serving:**
- FP8 on H100/B200: best quality/performance trade-off (hardware-native FP8 support)
- INT4 (AWQ) for cost-sensitive inference on older hardware
- Never serve in FP32 — pure waste of memory and compute

### PagedAttention (vLLM)

The single most important inference optimization of 2023-2024:

- Traditional KV-cache: contiguous memory allocation per request → massive memory fragmentation → 60-80% memory waste
- PagedAttention: allocate KV-cache in non-contiguous memory pages (like OS virtual memory)
- Result: near-zero memory waste → 2-4× more concurrent requests per GPU
- Enabled by vLLM (UC Berkeley), now standard in all major serving engines

### Continuous Batching

Traditional: wait until batch is full, process entire batch, return all results.
Continuous: as soon as one request finishes generating, immediately add a new request to the batch.

- Eliminates idle GPU time between batches
- 2-5× throughput improvement over static batching
- Standard in vLLM, TensorRT-LLM, SGLang

### Speculative Decoding

Use a small "draft" model to predict multiple tokens, then verify with the large model in parallel:
- Draft model generates K tokens quickly (small model → fast)
- Large model verifies all K tokens in one forward pass (parallel verification)
- If verified: K tokens generated in time of ~1 large-model forward pass
- If rejected: fall back to standard decode from rejection point

**Speedup:** 1.5-3× depending on draft model quality and acceptance rate.

### Prefix Caching

For applications with repeated system prompts or shared context:
- Cache KV-cache for common prefixes across requests
- First request with prefix: normal computation
- Subsequent requests with same prefix: skip prefill, reuse cached KV

**Use case:** Chatbot with system prompt (cached across all users), API with structured input format.

## 4. Inference Serving Engines

### vLLM (Open Source, UC Berkeley)

**Position:** De facto standard for open-source LLM inference serving.

**Key features:**
- PagedAttention (pioneered here)
- Continuous batching
- Tensor parallelism for multi-GPU serving
- OpenAI-compatible API
- Wide model support (LLaMA, Mixtral, Gemma, Qwen, etc.)
- Active community, rapid development

**When to use:** Default choice for most inference deployments. Extensive model compatibility, good performance, low operational complexity.

**Limitations:** Not the absolute fastest for NVIDIA-optimized models (TensorRT-LLM can be 10-30% faster for specific models).

### TensorRT-LLM (NVIDIA)

**Position:** NVIDIA's optimized inference engine, maximum performance on NVIDIA hardware.

**Key features:**
- TensorRT kernel fusion for NVIDIA GPUs
- FP8 quantization with hardware support
- In-flight batching (continuous batching)
- Paged KV-cache
- NVIDIA Triton Inference Server integration

**When to use:** Maximum throughput on NVIDIA hardware where operational complexity is acceptable. Largest deployments (cloud providers, AI API companies).

**Limitations:** NVIDIA-only, more complex to deploy than vLLM, slower model onboarding.

### SGLang (Stanford)

**Position:** Emerging high-performance engine focused on structured generation and program-level optimization.

**Key features:**
- RadixAttention (advanced prefix caching)
- Compressed FSM for structured output (JSON, regex-constrained)
- High throughput for structured generation workloads

**When to use:** Workloads requiring structured output (JSON APIs, function calling, constrained generation).

### Triton Inference Server (NVIDIA)

**Position:** Multi-framework model serving platform (not an LLM engine itself).

**Key features:**
- Hosts multiple models (LLM + embedding + vision) in one server
- Dynamic batching across models
- Model ensemble (chain multiple models)
- A/B testing, canary deployment
- Kubernetes integration (KServe)

**When to use:** Production inference platforms serving multiple model types, not just LLMs.

### Engine Comparison for DEC Tenants

| Engine | Performance | Ease of Use | Model Support | Best For |
|---|---|---|---|---|
| vLLM | Good (baseline) | Excellent | Widest | Most tenants, quick deployment |
| TensorRT-LLM | Best (10-30% over vLLM) | Moderate | NVIDIA-focused | High-volume API providers |
| SGLang | Good-Excellent | Good | Growing | Structured output workloads |
| Triton | Platform-level | Moderate | Multi-framework | Multi-model serving platforms |

## 5. Inference GPU Selection

### GPU Characteristics That Matter for Inference

| Feature | Why It Matters for Inference |
|---|---|
| HBM Bandwidth | Decode phase is memory-bandwidth-bound — more bandwidth = more tokens/sec |
| HBM Capacity | Determines max model size and concurrent request count |
| FP8 Performance | Quantized inference throughput |
| Power Efficiency | Cost per token (inference margins are thinner than training) |
| Cost per GPU | ROI at inference-level utilization (30-60% average) |

### GPU Comparison for Inference

| GPU | HBM Capacity | HBM BW | FP8 TFLOPS | TDP | Inference Strength |
|---|---|---|---|---|---|
| H100 SXM | 80 GB | 3.35 TB/s | 1,979 | 700 W | Strong general-purpose inference |
| H200 SXM | 141 GB | 4.8 TB/s | 1,979 | 700 W | Long context (more KV-cache capacity) |
| L40S | 48 GB | 864 GB/s | 733 | 350 W | Cost-effective for smaller models |
| B200 | 192 GB | 8 TB/s | 4,500 | 1,000 W | High-throughput inference at scale |
| GB200 NVL72 | 13.5 TB total | 576 TB/s total | ~300K total | 120-130 kW rack | Massive model serving, 72-GPU inference |
| MI300X | 192 GB | 5.3 TB/s | ~2,600 | 750 W | HBM capacity advantage, competitive |

### Inference Cluster Sizing

**Rule of Thumb:** Inference GPU count = model_parameters / (GPU_memory × quantization_compression × 0.6)
- 0.6 factor: 60% of HBM available after KV-cache and overhead

**Examples:**

| Model | Quantization | GPU Memory | GPUs Required | GPU Type |
|---|---|---|---|---|
| LLaMA 70B | FP8 | 80 GB | 2 | H100 SXM |
| LLaMA 70B | INT4 | 80 GB | 1 | H100 SXM |
| LLaMA 405B | FP8 | 80 GB | 8 | H100 SXM (1 node) |
| LLaMA 405B | FP8 | 192 GB | 4 | B200 |
| 1T MoE | FP8 | 80 GB | 16 | H100 SXM (2 nodes) |

### Inference Networking: Lighter Than Training

**Within a single inference instance (TP across GPUs in one node):**
- NVLink handles all inter-GPU communication
- No external network needed for single-node inference

**Across inference replicas:**
- No GPU-to-GPU communication between replicas
- Only load balancer → replica communication (standard Ethernet)
- 100 GbE sufficient for inference API traffic

**Multi-node inference (very large models requiring PP or TP across nodes):**
- InfiniBand or RoCEv2 for inter-node communication
- Lighter than training (no AllReduce, only activation passing)
- 200-400 Gb/s per node sufficient

**DEC Recommendation:** Inference halls use Ethernet (not InfiniBand) for all networking except multi-node inference instances. Cost savings of 50%+ on network infrastructure.

## 6. Inference SLA Design

### Key Metrics

| Metric | Definition | Typical Target (API) |
|---|---|---|
| TTFT (Time To First Token) | Latency from request to first generated token | <500 ms (p95) |
| TPOT (Time Per Output Token) | Inter-token latency during generation | <50 ms (p95) |
| E2E Latency | Total time from request to complete response | <5 sec for short responses |
| Throughput | Total tokens/sec across all requests | Maximize within latency SLA |
| Availability | Uptime percentage | 99.9% (3-nines) to 99.99% (4-nines) |
| Error Rate | % of requests that fail or timeout | <0.1% |

### Latency-Throughput Trade-off

**Fundamental tension:** Higher batch size = higher throughput but higher latency.

Inference operators must choose their operating point:
- **Latency-optimized:** Small batches, low utilization (30-40%), premium pricing
- **Throughput-optimized:** Large batches, high utilization (60-80%), competitive pricing
- **Balanced:** Dynamic batching that maintains latency SLA while maximizing throughput

### Inference Scaling

**Horizontal scaling (more replicas):**
- Linear throughput increase
- Load balancer distributes requests across replicas
- Kubernetes HPA (Horizontal Pod Autoscaler) with GPU utilization metric
- Autoscaling response time: 30-120 seconds (GPU node provisioning)

**Vertical scaling (larger GPUs or more GPUs per instance):**
- Reduces TTFT (faster prefill with more compute)
- Increases max context length
- More expensive per replica

## 7. Inference Power & Thermal Profiles

### Variable Load Characteristics

Unlike training (steady 85-95% TDP), inference load varies with request traffic:

```
Power (kW per rack)
120 |
100 |         ╱╲    ╱╲         Peak hours
 80 |     ╱──╱  ╲──╱  ╲╲
 60 |   ╱╱                ╲──    Off-peak
 40 | ╱╱                      ╲──
 20 |╱                            ╲    Night minimum
    └─────────────────────────────────
    0:00   6:00   12:00   18:00   24:00
```

**Typical daily power range for inference cluster:**
- Night minimum: 30-40% of peak
- Business hours: 70-90% of peak
- Peak (product launch, viral event): 95-100%
- Average: 50-65% of peak

### DEC Heat Recovery Impact

| Workload Type | Power Variability | Heat Recovery Predictability | Buffer Sizing |
|---|---|---|---|
| Training | ±5% steady | Excellent — plan for steady output | Minimal buffer needed |
| Inference (single tenant) | ±50% daily cycle | Moderate — follows request patterns | 4-6 hour buffer |
| Inference (multi-tenant) | ±30% daily cycle | Good — diversity smooths load | 2-4 hour buffer |
| Mixed training + inference | ±20% | Good — training provides base load | 2-3 hour buffer |

**Recommendation for DEC:** Mixed training + inference halls provide the best heat recovery profile. Training provides steady base load; inference adds variable top-up. Diversify tenant workload mix to minimize thermal variability.

## 8. Inference Economics

### Cost Per Token

| GPU | Model | Quantization | Throughput (tokens/sec) | Cost/GPU-hr | Cost per 1M Tokens |
|---|---|---|---|---|---|
| H100 SXM | LLaMA 70B | FP8 | ~4,000 output | $3.50 | ~$0.25 |
| H100 SXM | LLaMA 405B (8 GPU) | FP8 | ~1,200 output | $28.00 (8 GPU) | ~$6.50 |
| L40S | LLaMA 70B | INT4 | ~2,000 output | $1.50 | ~$0.21 |
| B200 | LLaMA 70B | FP8 | ~8,000 output | $5.00 | ~$0.17 |

*Costs are approximate and vary by provider, utilization, and contract terms.*

### Inference vs Training Revenue Per GPU

| Metric | Training | Inference |
|---|---|---|
| Typical utilization | 85-95% | 40-65% |
| Revenue model | Reserved capacity ($/GPU-hr) | Per-token or reserved |
| Gross margin | Higher (steady, predictable) | Lower (variable, competitive) |
| Contract duration | Months to years | On-demand to annual |
| DEC revenue impact | Predictable colocation revenue | Variable, depends on tenant success |

**DEC Strategy:** Prioritize training tenants for revenue predictability and heat recovery stability. Inference tenants provide diversity and lower vacancy risk. Ideal mix: 60-70% training capacity, 30-40% inference capacity.

## 9. Model Serving Patterns

### Single-Model Serving
- One model per GPU cluster
- Simplest deployment
- Most common for API providers

### Multi-Model Serving
- Multiple models on shared GPU pool
- Model multiplexing: load/unload models based on demand
- Triton Inference Server excels here
- Challenge: model loading latency (30-120 seconds for large models)

### Mixture-of-Experts Serving
- MoE models: only active experts need GPU memory
- Expert offloading: inactive experts on CPU/NVMe, loaded on demand
- Reduces effective GPU memory requirement
- Higher latency variance (expert loading)

### RAG (Retrieval-Augmented Generation) Pipeline
- Embedding model + vector DB + LLM in sequence
- Different GPU requirements per component:
  - Embedding: small model, high throughput, L40S or even CPU
  - Vector DB: CPU + SSD, not GPU-bound
  - LLM: standard inference requirements
- Total pipeline latency = embedding + retrieval + generation

## Cross-References
- See [gpu-accelerator-hardware.md](gpu-accelerator-hardware.md) for GPU specifications and inference-relevant features (HBM bandwidth, FP8 cores)
- See [cluster-networking.md](cluster-networking.md) for inference network requirements (Ethernet sufficient for most inference)
- See [cluster-orchestration.md](cluster-orchestration.md) for Kubernetes inference deployment and autoscaling
- See [training-workloads.md](training-workloads.md) for how trained models are produced (training → inference pipeline)
- See [ai-storage-data.md](ai-storage-data.md) for model artifact storage and serving
- See companion skill `dc-engineering`:
  - [heat-recovery-integration.md] for inference thermal variability impact on heat recovery
  - [data-hall-design.md] for mixed training/inference hall design
- See companion skill `energy-markets` for inference power variability impact on energy procurement
- See companion skill `site-development` for inference tenant mix strategy and financial modeling
