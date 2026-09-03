---
type: concept
title: "Sigmoid Function"
subject: "Artificial_Intelligence"
date_created: 2026-07-29
tags: [machine-learning, deep-learning, activation-functions, sigmoid]
source: "[[Activation Functions Explained]]"
source_hash: "f79b33ad105945a896c6978800b44b95"
---

## The idea (one clear statement)
The **Sigmoid function** is an S-shaped activation function that maps any real-valued number to a probability value between \(0\) and \(1\).

## Why it matters / how it connects
*   **Probability Output**: Ideal for the output layer of binary classification models (e.g. predicting a Yes/No outcome).
*   **Vanishing Gradient Problem**: Its main drawback is that it flatlines at extreme positive or negative inputs, causing its derivative (slope) to approach zero. This halts weight updates during gradient descent and stalls learning.

## Related concepts
- [[Activation Functions]]
- [[Model Parameters]]
- [[Tanh Function]]
