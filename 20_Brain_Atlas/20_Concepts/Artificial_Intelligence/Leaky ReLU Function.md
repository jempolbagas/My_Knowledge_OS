---
type: concept
title: "Leaky ReLU Function"
subject: "Artificial_Intelligence"
date_created: 2026-07-29
tags: [machine-learning, deep-learning, activation-functions, leaky-relu]
source: "[[Activation_Functions_Explained]]"
source_hash: "f79b33ad105945a896c6978800b44b95"
---

## The idea (one clear statement)
The **Leaky ReLU function** is a variation of ReLU that allows a tiny, non-zero slope (usually \(0.01\)) for negative inputs.

## Why it matters / how it connects
*   **Dying ReLU Solution**: By introducing a small negative slope, it ensures the gradient is never exactly zero for negative inputs. This keeps neurons active and capable of updating their weights.
*   **GANs and Deep Networks**: Frequently used in architectures like Generative Adversarial Networks (GANs) where dead neurons severely limit performance.

## Related concepts
- [[Activation Functions]]
- [[ReLU Function]]
