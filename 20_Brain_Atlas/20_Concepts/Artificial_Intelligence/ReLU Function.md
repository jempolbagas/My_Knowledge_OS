---
type: concept
title: "ReLU Function"
subject: "Artificial_Intelligence"
date_created: 2026-07-29
tags: [machine-learning, deep-learning, activation-functions, relu]
source: "[[Activation_Functions_Explained]]"
source_hash: "f79b33ad105945a896c6978800b44b95"
---

## The idea (one clear statement)
The **ReLU (Rectified Linear Unit) function** is an activation function that outputs \(0\) for negative inputs and passes positive inputs directly unchanged.

## Why it matters / how it connects
*   **Default Choice**: The standard activation function for hidden layers in modern deep neural networks.
*   **Fast and Efficient**: Extremely simple to compute (requires only a threshold comparison at zero).
*   **No Vanishing Gradient (Positive Domain)**: The slope is always \(1.0\) for positive inputs, avoiding gradient shrinkage.
*   **Dying ReLU Problem**: If a neuron is updated such that it only receives negative inputs, its output and slope remain \(0\). The neuron "dies" and stops learning permanently.

## Related concepts
- [[Activation Functions]]
- [[Leaky ReLU Function]]
- [[Tanh Function]]
