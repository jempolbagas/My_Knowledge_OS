---
type: concept
title: "Softmax Function"
subject: "Artificial_Intelligence"
date_created: 2026-07-29
tags: [machine-learning, deep-learning, activation-functions, softmax]
source: "[[Activation_Functions_Explained]]"
source_hash: "f79b33ad105945a896c6978800b44b95"
---

## The idea (one clear statement)
The **Softmax function** is an activation function that converts a vector of raw numerical scores into a probability distribution that sums to exactly \(1.0\).

## Why it matters / how it connects
*   **Multi-Class Classification**: Used in the final output layer of classification tasks with three or more classes (e.g., Cat, Dog, or Bird) so the outputs compete with one another.
*   **Probability Interpretation**: Unlike applying Sigmoid individually, Softmax guarantees the outputs are mutually exclusive and collectively exhaustive probabilities.

## Related concepts
- [[Activation Functions]]
- [[Sigmoid Function]]
