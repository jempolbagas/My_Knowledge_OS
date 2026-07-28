---
title: "A Simple Introduction to Post-Training Quantization."
source: "https://medium.com/@peteragida/a-simple-introduction-to-post-training-quantization-42ecdc29938e"
author:
  - "[[Peter Agida]]"
published: 2025-01-29
created: 2026-07-28
description: "More"
tags:
  - "clippings"
---
The large size and scale of computational requirements required for deploying state-of-the-art models make them largely impractical for utilisation on applications and devices with limited resources (e.g. smartphones). Quantization is an optimisation technique employed to address these challenges. At its core, it attempts to reduce the precision of weights and activations without drastically impacting performance.

Quantization is primarily categorised into Quantization Aware Training (QAT) and Post Training Quantization. QAT is a widely adopted technique in machine learning engineering. It integrates quantization into the training process by simulating lower precision during training to minimize accuracy loss, making it ideal for models with rigorous performance requirements. This article though will be largely focused on introducing Post Training Quantization, its architecture and potential use cases.

Post-training quantization is a technique employed for the optimization of deep learning models, primarily to enhance reduction in size and computational requirements while minimizing overall loss in accuracy. Its value is predominantly identified during the deployment of models on resource-constrained devices (e.g. mobile phones or embedded systems).

At its core, post-training quantization entails the conversion of a pre-trained floating-point model into a quantized model with most weights (neural network parameters learned during training) and operations largely represented in lower precision formats. This is done to address several challenges like high computational cost; with floating point operations typically requiring more time and energy for inference, Memory Limitations; addressing the inherent inefficiency in the transfer process of large floating point weights, and Model Size; models with a large number of parameters can potentially be difficult to deploy on resourced constrained devices.

The are several types of Post-Training Quantization:

Full Integer Quantization; in this scenario, the weights and activations are converted to int8. This largely entails fine-tuning, accomplished by utilizing a small representative dataset to compute activation ranges.

Dynamic Range Quantization; here only the weights are quantized to 8-bit integers during storage. Weights are then converted back to floating-point at runtime. This technique provides moderate size reduction but is generally perceived as only providing limited performance improvement compared to other post-training quantization methods.

Mixed Precision Quantization; Here some layers stay in FP32 or FP16 format, while the rest are converted to int8. This is typically employed to address the problem of accuracy degradation in quantized layers.

During training, deep learning models are typically represented in floating point precision (32-bit floating point, or FP32), i.e. activations (intermediate values produced during inference when data is passed through the network), and weights are computed and stored with 32 bits per number. This typically offers high precision and helps capture subtle nuances of the learned parameters. However, this approach could offer potential problems during deployment due to several factors like high computational cost (requires more time and energy for inference), large model size (large models could sometimes be difficult to deploy on resource-constrained devices) and memory limitations.

The key components of post-training quantization;

- Precision Reduction: In Post-training quantization, the model’s activations and weights are converted to lower precision formats (e.g. int 8, FP16 and UINT 8).
- Scaling: Scaling largely involves the mapping of the range of values in the original floating point model to the range of the target format. This procedure is controlled by scaling factors, employed to preserve the relative information of the original values.
- Rounding: To address the potential problem of distortion during the conversion process, the floating point values are rounded to the nearest integer after scaling.

When converting from FP32 to INT8, scaling factors are applied that maps the FP32 values to the target int8 range. This can only be done efficiently after identifying the range of values in the FP32 model for weights and activations.

In Post-scaling (Post Training Quantization process for adjusting the scale of quantized tensors to retain numerical precision), the FP32 value is rounded to the nearest integer within the target range. Next, a representative dataset that approximates the spread of activation values at inference is utilized. The goal here is to calibrate the activation ranges and compute the relevant scaling factors.

A key challenge when employing post-training quantization is the potential problem of accuracy loss. Quantization essentially decreases the precision of activations and weights, which can potentially introduce errors in the model’s predictions. Minimizing this loss while maintaining substantial performance gains is the key goal of Post Training Quantization. To accomplish this, it is important to utilize optimal scaling factors to minimize the potential impact of rounding errors. Also finetuning the scaling factors for activations and weights with a small representative dataset can potentially help mitigate accuracy loss.

Several Machine Learning Libraries like Tensorflow lite (tflite\_converter) and Pytorch (torch.quantization) provide tools that allow for quantization implementation.

Post-Training quantization with Tensorflow Lite involves the conversion of a floating point model (FP32) into a more efficient Tensorflow Lite format with significantly lower precision (e.g. INT8 or FP16). All three commonly applied post-training quantization methods can be accomplished using.tflite: Full Integer Quantization (quantizes both weights and activations to INT8, utilizing a representative dataset for calibration), Dynamic Range Quantization (quantizes weights to INT8 without requiring quantization) and Float16 Quantization (reduces weights to FP16 for GPUs and hardware with FP16 support).

![[1*TzKA_rjU1tmlN2h6J0P1hw.png]]

An example of dynamic range quantization with TensorFlow (TFLiteConverter). The operation converter.optimizations = \[tf.lite.Optimize.Default\] facilitates the reduction of the model size by quantizing its weights from 32-bit floating-point to 8-bit integers while maintaining activations in their original FP32 precision. A representative dataset is not required in dynamic range quantization making it easy to implement.

![[1*It912TAeD18n7cZHkIxOpw.png]]

An example of Float 16 Quantization where the model weights are reduced from 32-bit floating point to 16 bit floating point by setting converter.target\_spec.supported\_types = \[tf.float16\]. Also, general optimization is enabled using converter.optimizations = \[tf.lite.Optimize.Default\]. The activations are maintained in FP32 format while the focus is predominantly on model size reduction and boosting inference performance on selected hardware (e.g. GPUs) that supports FP16 operations. The potential to offer faster computations coupled with minimal alteration in model accuracy makes this approach a great choice for maintaining balance in the precision and efficiency of compatible devices.

When selecting the appropriate quantization method, factors like accuracy requirements and hardware capabilities must be considered. if the selection process is handled appropriately, engineers and developers can attain significant improvements in model efficiency without the need for retraining. Whether employed for memory footprint reduction, boosting inference speed or enhancing model capabilities with edge accelerators, Post Training Quantization is a relevant tool in the machine learning development pipeline.