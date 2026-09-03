---
type: concept
title: "Model Parameters"
subject: "Artificial_Intelligence"
date_created: 2026-07-29
tags: [machine-learning, deep-learning, parameters, weights, biases]
source: "[[Model Parameters Explained]]"
source_hash: "fd87257535fdd537e62e654d287bfb30"
---

## The idea (one clear statement)
**Model parameters** are the internal numeric variables (specifically weights and biases) that a machine learning model learns and refines from training data in order to map inputs to correct predictions.

## Why it matters / how it connects
*   **Predictive Engine:** They represent the actual "learned knowledge" or "memory" of a trained model.
*   **Optimization Targets:** During training, optimization algorithms (like gradient descent) iteratively adjust parameter values using gradients computed via backpropagation to minimize a loss function.
*   **Deployment Footprint:** The size of a model is directly proportional to its parameter count, making techniques like [[Post-Training Quantization]] crucial to reduce storage and memory bandwidth during edge deployment.
*   **Distinction from Hyperparameters:** Unlike hyperparameters (e.g., learning rate, layers), parameters are learned automatically by the model from the data rather than configured manually by the developer.

## Related concepts
- [[Machine Learning Roadmap]]
- [[Post-Training Quantization]]
- [[Model Parameters Explained]]
