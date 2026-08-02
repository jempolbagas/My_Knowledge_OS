---
type: concept
title: "Symmetric vs Asymmetric Quantization"
subject: "Artificial_Intelligence"
date_created: 2026-08-02
tags: [quantization, deep-learning, int8, hardware]
source: "[[Post_Training_Quantization_End_to_End_Guide]]"
source_hash: "41e818cb181faf4fc06350273191d9c3"
---

## The idea (one clear statement)
**Asymmetric Quantization** maps an arbitrary range $[x_{\min}, x_{\max}]$ using both a scale factor $s$ and a non-zero integer zero-point $z$, whereas **Symmetric Quantization** forces the range to be symmetric $[-R, R]$ with zero-point rigidly fixed at $z = 0$.

## Why it matters / how it connects
* **Asymmetric ($z \neq 0$):** Utilizes full integer range $[0, 255]$ or $[-128, 127]$, ideal for asymmetric activation functions (e.g., ReLU outputting $[0, x_{\max}]$). However, matrix multiplication requires computing zero-point cross-term scalar offsets.
* **Symmetric ($z = 0$):** Forces $z=0$, simplifying affine dot-products $A_q W_q$ directly into native hardware SIMD/Tensor Core integer instructions (`dp4a`, VNNI) without offset adjustments.

## Related concepts
- [[Post-Training Quantization]]
- [[Scale Factor and Zero-Point]]
- [[Post_Training_Quantization_End_to_End_Guide]]
