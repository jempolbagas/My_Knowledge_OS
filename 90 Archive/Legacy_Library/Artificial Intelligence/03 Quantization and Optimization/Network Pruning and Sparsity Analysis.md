---
type: generated_reading
title: "Network Pruning and Sparsity Analysis"
topic: "Artificial_Intelligence"
requested_on: 2026-08-21
status: done
tags: [machine-learning, deep-learning, optimization, pruning, sparsity, taylor-expansion, optimal-brain-damage]
promoted_to:
  - "[[Model Pruning]]"
---

# Network Pruning and Sparsity Analysis

Network Pruning is a fundamental model compression technique designed to identify and eliminate redundant parameters (weights or entire neurons/channels) from deep neural networks while minimizing degradation to the empirical loss function $\mathcal{L}(W; \mathcal{D})$.

---

## 1. Mathematical Formulation & Constrained Optimization

Pruning can be formulated as a constrained optimization problem subject to an $L_0$-norm sparsity constraint:

$$\min_{W} \mathcal{L}(W; \mathcal{D}) \quad \text{subject to} \quad \|W\|_0 \leq \kappa$$

Where:
- $W$ represents the model parameters (weights).
- $\mathcal{D}$ is the training dataset.
- $\|W\|_0$ counts the number of non-zero elements.
- $\kappa$ is the target maximum number of active weights.

Because $L_0$-norm optimization is NP-hard, practical implementations use $L_1$ or $L_2$ regularization penalties during training:

$$\mathcal{L}_{\text{total}}(W) = \mathcal{L}(W; \mathcal{D}) + \lambda \|W\|_p \quad (p \in \{1, 2\})$$

The $L_1$ norm (Lasso regularization) inherently drives parameters toward exact zero values, facilitating threshold-based truncation.

---

## 2. Saliency Criteria & Taylor Expansion (Optimal Brain Damage)

To decide deterministically which weights to prune, we evaluate the change in loss $\delta \mathcal{L}$ caused by setting a weight $w_i \to 0$ ($\Delta w_i = -w_i$). 

Using a second-order Taylor series expansion around a converged local minimum $W^*$:

$$\delta \mathcal{L} \approx \sum_i g_i \Delta w_i + \frac{1}{2} \sum_i h_{ii} (\Delta w_i)^2 + \frac{1}{2} \sum_{i \neq j} h_{ij} \Delta w_i \Delta w_j$$

Where:
- $g_i = \frac{\partial \mathcal{L}}{\partial w_i}$ is the gradient vector component.
- $h_{ij} = \frac{\partial^2 \mathcal{L}}{\partial w_i \partial w_j}$ is the Hessian matrix component.

At convergence, the gradient vector $g_i \approx 0$. Assuming parameter independence (off-diagonal Hessian entries $h_{ij} = 0$), the saliency $S_i$ measuring the importance of parameter $w_i$ simplifies to:

$$S_i = \frac{1}{2} h_{ii} w_i^2$$

Weights with the lowest saliency $S_i$ are pruned first, ensuring the minimal increase in empirical loss $\delta \mathcal{L}$.

---

## 3. Unstructured vs. Structured Pruning

| Dimension | Unstructured Pruning | Structured Pruning |
| :--- | :--- | :--- |
| **Granularity** | Individual weight elements (sparse matrices). | Entire channels, filters, or layers. |
| **Theoretical Compression** | High (often 80%–90% parameters removed). | Moderate (30%–50% removed). |
| **Hardware Acceleration** | Requires custom sparse SIMD hardware kernels. | Direct speedups on standard dense GPUs/CPUs. |

---

## Related Generated Readings
- [[Fundamentals of Machine Learning Optimization and Compression]]
- [[Knowledge Distillation and Teacher Student Optimization]]
- [[Low Rank Factorization and LoRA Mechanics]]
- [[Post Training Quantization End to End Guide]]
