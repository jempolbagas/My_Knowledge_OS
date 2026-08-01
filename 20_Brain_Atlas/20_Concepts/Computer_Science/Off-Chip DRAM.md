---
type: concept
title: "Off-Chip DRAM"
subject: "Computer_Science"
date_created: 2026-08-02
tags: [computer-science, hardware-architecture, memory, dram, machine-learning, model-optimization]
source: "[[Post_Training_Quantization_End_to_End_Guide]]"
---

## The idea (one clear statement)
**Off-Chip DRAM (Dynamic Random-Access Memory)** refers to main system memory (e.g., DDR, LPDDR, GDDR) located on a separate physical semiconductor silicon die from the primary processing unit (CPU, GPU, NPU), requiring data transfers across physical chip bus interconnects.

## Why it matters / how it connects
*   **Memory Bandwidth Bottleneck:** Fetching large parameter tensors from off-chip DRAM to processor caches/ALUs creates significant latency, often leaving compute units idle during neural network inference.
*   **Energy Overhead:** Transferring data across off-chip PCB traces consumes orders of magnitude ($100\times$–$1000\times$) more energy per byte than performing on-chip arithmetic operations.
*   **Quantization Catalyst:** Memory bandwidth and energy costs associated with off-chip DRAM access are the primary drivers for model quantization techniques (e.g., INT8/INT4 PTQ), which reduce data movement across the chip boundary.

## Related concepts
- [[Post-Training Quantization]]
- [[Post_Training_Quantization_End_to_End_Guide]]
- [[Single Board Computer]]
