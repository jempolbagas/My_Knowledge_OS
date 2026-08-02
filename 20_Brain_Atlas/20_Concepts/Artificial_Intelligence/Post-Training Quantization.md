---
type: concept
title: "Post-Training Quantization"
subject: "Artificial_Intelligence"
date_created: 2026-08-02
tags: [quantization, deep-learning, machine-learning, model-optimization, inference]
source: "[[Post_Training_Quantization_End_to_End_Guide]]"
source_hash: "41e818cb181faf4fc06350273191d9c3"
---

## The idea (one clear statement)
**Post-Training Quantization (PTQ)** is a model compression method that converts trained high-precision floating-point parameters and layer activations (e.g., FP32/FP16) into lower-precision discrete integer formats (e.g., INT8/INT4) using scale factors and zero-points derived post-hoc or via calibration datasets, without requiring full model retraining or gradient backpropagation.

## Why it matters / how it connects
* **Deployment Efficiency:** Cuts model VRAM/RAM footprint by $75\%$ (FP32 to INT8) or up to $87.5\%$ (FP32 to INT4) and enables integer hardware acceleration (SIMD/NPU/Tensor Cores) for low-latency inference.
* **Zero Retraining Friction:** Operates on frozen parameters using a small calibration dataset (100–500 input samples), avoiding the compute costs of full re-training required by Quantization-Aware Training (QAT).
* **Memory Bandwidth Speedup:** Speeds up memory-bound inference workloads (e.g., LLM token decoding) by reducing data transfer traffic between DRAM and processing units by $4\times$.

## Related concepts
- [[Scale Factor and Zero-Point]]
- [[Quantization Calibration]]
- [[Symmetric vs Asymmetric Quantization]]
- [[Per-Tensor vs Per-Channel Quantization]]
- [[Post_Training_Quantization_End_to_End_Guide]]
