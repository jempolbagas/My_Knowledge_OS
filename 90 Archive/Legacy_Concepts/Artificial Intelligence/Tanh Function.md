---
type: concept
title: "Tanh Function"
subject: "Artificial_Intelligence"
date_created: 2026-07-29
tags: [machine-learning, deep-learning, activation-functions, tanh]
source: "[[Activation Functions Explained]]"
source_hash: "f79b33ad105945a896c6978800b44b95"
---

## The idea (one clear statement)
The **Tanh (Hyperbolic Tangent) function** is an S-shaped activation function that maps real-valued inputs to a range between \(-1\) and \(1\).

## Why it matters / how it connects
*   **Zero-Centered**: Unlike Sigmoid, its output is zero-centered (average output is close to zero), which makes training faster and optimization easier in hidden layers.
*   **Vanishing Gradient**: Like Sigmoid, it suffers from flatlining at extreme values, leading to vanishing gradients and stalling weight updates.

## Related concepts
- [[Activation Functions]]
- [[Sigmoid Function]]
- [[ReLU Function]]
