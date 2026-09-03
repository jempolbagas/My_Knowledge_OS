---
type: concept
title: "Scale Factor and Zero-Point"
subject: "Artificial_Intelligence"
date_created: 2026-08-02
tags: [quantization, deep-learning, math, int8]
source: "[[Post Training Quantization End to End Guide]]"
source_hash: "41e818cb181faf4fc06350273191d9c3"
---

## The idea (one clear statement)
The **Scale Factor ($s$)** and **Zero-Point ($z$)** define the linear affine transformation parameters that map a continuous floating-point interval $[x_{\min}, x_{\max}]$ onto a discrete integer grid $[q_{\min}, q_{\max}]$.

$$\text{Scale: } s = \frac{x_{\max} - x_{\min}}{q_{\max} - q_{\min}}, \qquad \text{Zero-Point: } z = \text{round}\left( q_{\min} - \frac{x_{\min}}{s} \right)$$

## Why it matters / how it connects
* **Affine Mapping:** Enables exact transformation from continuous FP32 values into INT8 integer indices via $x_q = \text{clamp}(\text{round}(x/s) + z)$ and reconstruction via $\hat{x} = s \cdot (x_q - z)$.
* **Exact Zero Preservation:** The zero-point $z$ ensures that real floating-point $0.0$ maps precisely to an integer bucket index $z$. This is critical for zero-padding in convolutions and sparsity in ReLU activations without introducing numerical bias.
* **Quantization Resolution:** The scale factor $s$ dictates the floating-point step size per integer bucket; smaller scale factors yield finer numerical precision.

## Related concepts
- [[Post-Training Quantization]]
- [[Quantization Calibration]]
- [[Symmetric vs Asymmetric Quantization]]
- [[Post Training Quantization End to End Guide]]
