---
type: concept
title: "Post-Training Quantization"
subject: "Artificial_Intelligence"
date_created: 2026-07-28
tags: [quantization, deep-learning, machine-learning, model-optimization, inference]
source: "[[Post_Training_Quantization_Explained]]"
source_hash: "64aa69bfe02449ec9f1894d8e0a05361"
---

## The idea (one clear statement)
**Post-Training Quantization (PTQ)** is a model compression method that converts trained floating-point weights and layer activations (e.g., FP32/FP16) into lower-precision discrete formats (e.g., INT8/INT4) using scale factors and zero-points derived offline or via calibration, without requiring full model retraining.

## Why it matters / how it connects
*   **Deployment Efficiency:** Reduces memory footprint by up to $75\%$ (FP32 to INT8) or $87.5\%$ (FP32 to INT4) and enables integer hardware acceleration (NPU/GPU Tensor Cores) for ultra-low latency inference on mobile and edge devices.
*   **Low Friction Workflow:** Unlike Quantization-Aware Training (QAT), PTQ operates on pre-trained models with minimal compute overhead and only requires a small calibration dataset (100–500 samples).
*   **LLM Scalability:** Advanced techniques like SmoothQuant, GPTQ, and AWQ extend PTQ to multi-billion parameter LLMs, mitigating activation outlier issues while preserving model accuracy.

## Related concepts
- [[Machine Learning Roadmap]]
- [[Vectorization in NumPy]]
- [[Post_Training_Quantization_Explained]]
- [[A_Simple_Introduction_to_Post_Training_Quantization]]
- [[Post_Training_Quantization_End_to_End_Guide]]
