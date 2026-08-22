---
type: concept
title: "Per-Tensor vs Per-Channel Quantization"
subject: "Artificial_Intelligence"
date_created: 2026-08-02
tags: [quantization, deep-learning, int8, neural-networks]
source: "[[Post Training Quantization End to End Guide]]"
source_hash: "41e818cb181faf4fc06350273191d9c3"
---

## The idea (one clear statement)
**Per-Tensor Quantization** assigns a single scale factor $s$ and zero-point $z$ to an entire tensor, whereas **Per-Channel (Per-Axis) Quantization** assigns distinct scale factors $s_c$ and zero-points $z_c$ to each output channel or slice of a weight matrix.

## Why it matters / how it connects
* **Per-Tensor:** Memory overhead for scale/zero-point is minimal (one pair per layer), but accuracy degrades if different channels within a weight tensor have wide variations in dynamic magnitude ranges.
* **Per-Channel:** Essential for linear and convolutional weight matrices. It prevents high-magnitude channels from blowing up the scale factor $s$ and squashing precision in smaller-magnitude channels.

## Related concepts
- [[Post-Training Quantization]]
- [[Scale Factor and Zero-Point]]
- [[Post Training Quantization End to End Guide]]
