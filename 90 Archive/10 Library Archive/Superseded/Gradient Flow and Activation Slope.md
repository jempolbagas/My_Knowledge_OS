---
type: generated_reading
title: "Gradient Flow and Activation Slope"
topic: "Artificial_Intelligence"
requested_on: 2026-07-29
prompt: "Why does the slope of the activation function matter to the weight updates during training, and why does a zero slope stall learning?"
status: archived
archived_reason: "Superseded by master guide 'Comprehensive Guide to Activation Functions and Gradient Flow.md'"
tags: [machine-learning, deep-learning, gradient-descent, backpropagation, calculus]
promoted_to: []
---

## The reading

In deep learning, neural networks learn by tweaking their weights to minimize prediction errors. This adjustment is guided by calculus—specifically, derivatives. The slope of the activation function acts as a critical gateway for this error signal during training. If this slope vanishes, the learning process stalls completely.

### 1. The Optimization Goal: Minimizing Loss
$$\frac{\partial L}{\partial w} \approx \frac{\Delta \text{ Loss}}{\Delta \text{ Weight}}$$

### 2. The Mechanics of the Weight Update
$$w_{\text{new}} = w_{\text{old}} - \eta \cdot \frac{\partial L}{\partial w}$$

### 3. Backpropagation and the Chain Rule
$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w} = \frac{\partial L}{\partial a} \cdot \sigma'(z) \cdot x$$

### 4. Why Zero Slope Stalls Learning
When $\sigma'(z) = 0$, $\frac{\partial L}{\partial w} = 0$, causing $w_{\text{new}} = w_{\text{old}}$ and stalling learning.

---

## Related Generated Readings
- [[Comprehensive Guide to Activation Functions and Gradient Flow]]
