---
type: concept
title: "Activation Functions"
subject: "Artificial_Intelligence"
date_created: 2026-07-29
tags: [machine-learning, deep-learning, activation-functions, neural-networks, non-linearity]
source: "[[Activation_Functions_Explained]]"
source_hash: "f79b33ad105945a896c6978800b44b95"
---

## The idea (one clear statement)
An **activation function** is a mathematical formula applied to a neuron's output that introduces non-linearity, determining whether and how strongly the neuron fires based on its inputs.

## Why it matters / how it connects
*   **Enabler of Deep Learning:** It introduces non-linearity. Without it, stacking multiple neural network layers is mathematically equivalent to a single linear layer, limiting the model's capacity to drawing straight lines.
*   **Gradient Flow Control:** The choice of activation function determines the gradient magnitude during backpropagation, affecting issues like vanishing gradients (in Sigmoid/Tanh) or dying neurons (in ReLU).
*   **Task-Specific Outputs:** Different functions serve as output controllers: Sigmoid for binary probabilities, Softmax for multi-class probability distributions, and Linear for continuous values.

## Related concepts
- [[Model Parameters]]
- [[Post-Training Quantization]]
- [[Activation_Functions_Explained]]
