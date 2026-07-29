---
type: concept
title: "Scale Factor and Zero-Point"
subject: "Artificial_Intelligence"
date_created: 2026-07-29
tags: [machine-learning, deep-learning, quantization, scale-factor, zero-point, model-compression]
source: "[[Scale_Factor_and_Zero_Point_in_Quantization]]"
source_hash: "42839293822885af053254b55dea6858"
---

## The idea (one clear statement)
The **scale factor ($s$)** and **zero-point ($z$)** are mathematical mapping parameters that define a linear affine relationship to project continuous real-valued floats (FP32) onto a discrete grid of low-precision integers (INT8/INT4).

## Why it matters / how it connects
*   **Quantization Engine:** They enable the conversion ($x_q = \text{clamp}(\text{round}(x/s) + z)$) and approximation retrieval ($\hat{x} = s(x_q - z)$) of model weights and layer activations.
*   **Zero Representation:** Zero-point ($z$) forces the real float value $0.0$ to map to an exact integer. This prevents numerical bias in zero-padding and preserves structural activation thresholds (like in ReLU).
*   **Symmetry and Efficiency:** Enforcing a symmetric quantization scheme where $z = 0$ simplifies runtime matrix multiplications on target NPUs or Tensor Cores by eliminating scalar zero-point correction offset calculations.

## Related concepts
- [[Post-Training Quantization]]
- [[Activation Functions]]
- [[Scale_Factor_and_Zero_Point_in_Quantization]]
