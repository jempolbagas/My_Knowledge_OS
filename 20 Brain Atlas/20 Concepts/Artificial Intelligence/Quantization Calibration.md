---
type: concept
title: "Quantization Calibration"
subject: "Artificial_Intelligence"
date_created: 2026-08-02
tags: [quantization, deep-learning, calibration, int8, tensorrt]
source: "[[Post Training Quantization End to End Guide]]"
source_hash: "41e818cb181faf4fc06350273191d9c3"
---

## The idea (one clear statement)
**Quantization Calibration** is the process of feeding a representative calibration dataset (100–500 samples) through a pre-trained model to record dynamic activation distributions and derive optimal dynamic range bounds $[x_{\min}, x_{\max}]$ for quantization without updating model weights.

## Why it matters / how it connects
* **Error Balance:** Manages the fundamental trade-off between **clipping loss** (truncating outlier activations outside the threshold) and **rounding loss** (resolution step size $s$).
* **Calibration Algorithms:**
  - **MinMax:** Uses absolute minimum and maximum values; zero clipping loss, but highly vulnerable to activation outliers.
  - **MSE Minimization:** Scans thresholds $\alpha$ to minimize $L_2$ reconstruction error $\| A - \hat{A}(\alpha) \|_2^2$.
  - **Entropy / KL-Divergence (TensorRT):** Minimizes information loss $D_{\text{KL}}(P_{\text{FP32}} \parallel Q_{\text{INT8}})$ between original and quantized activation distributions.

## Related concepts
- [[Post-Training Quantization]]
- [[Scale Factor and Zero-Point]]
- [[Post Training Quantization End to End Guide]]
