<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# What is the current status of ONNX Runtime on ARM64 Raspberry Pi 4? Which versions have pre-built wheels and which require building from source?

ONNX Runtime on ARM64 Raspberry Pi 4 is **supported, but pre-built wheel availability is limited by Python version and release channel**. The official docs say the Arm64/Linux build is supported, and the Arm learning path notes that prebuilt wheels exist only for specific Python versions, with Python 3.10 recommended and Python 3.12 not yet supported on Arm platforms in that guide.[^1_1][^1_2]

## What is pre-built

- `pip install onnxruntime` is the standard official CPU package, and the install docs list it as the Python CPU package for official builds.[^1_3]
- The docs also say the general install matrix supports Arm64, and the inference build table notes that other variants can be built from source when needed.[^1_2][^1_3]


## What usually requires source builds

- If you are on a Raspberry Pi 4 with **ARM64 Linux** and a Python version that does not have a matching wheel, you need to build from source or use a custom build.[^1_4][^1_1]
- The build docs explicitly describe building ONNX Runtime for Arm devices, including ARM64, and note that the wheel can be built and then deployed to the device.[^1_2]
- Community Raspberry Pi guides also state that ARM packages were historically not provided as binaries and had to be built from source on the Pi.[^1_5]


## Practical version guidance

- **Most likely to have pre-built wheels:** official release builds for Arm64 on **supported Python versions**; the Arm learning path specifically calls out Python 3.10 as tested/recommended, and warns that Python 3.12 is not yet supported there.[^1_1]
- **Likely to require building from source:** older or newer Python versions without matching Arm64 wheels, custom ONNX Runtime builds, or special feature variants.[^1_4][^1_1]


## Bottom line

If you want the simplest path on a Raspberry Pi 4 ARM64, use a supported 64-bit OS and a supported Python version, then install `onnxruntime` from pip. If pip says “no matching distribution,” that means you’ll need to build ONNX Runtime from source for your specific Python/ARM64 combination.[^1_1][^1_2]
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/onnx/02_setup/

[^1_2]: https://onnxruntime.ai/docs/build/inferencing.html

[^1_3]: https://onnxruntime.ai/docs/install/

[^1_4]: https://onnxruntime.ai/docs/build/

[^1_5]: https://qiita.com/linyixian/items/bd7b8378da8c1fc9d24d

[^1_6]: https://github.com/cansik/onnxruntime-silicon

[^1_7]: https://github.com/maulingajjar/onnx-wheels

[^1_8]: https://github.com/PINTO0309/onnxruntime4raspberrypi

[^1_9]: https://github.com/edgeimpulse/onnxruntime-qnn-linux-aarch64

[^1_10]: https://github.com/microsoft/onnxruntime-genai/issues/1417

[^1_11]: https://github.com/nknytk/built-onnxruntime-for-raspberrypi-linux/blob/master/BUILD.md

[^1_12]: https://github.com/nknytk/built-onnxruntime-for-raspberrypi-linux

[^1_13]: https://onnxruntime.ai/docs/genai/howto/build-from-source.html

[^1_14]: https://github.com/microsoft/onnxruntime/issues/19162

[^1_15]: https://pypi.org/project/onnxruntime/


---

# How to run INT8 quantized ONNX models on Raspberry Pi 4 using onnxruntime? What are the inference latency benchmarks?

To run INT8 ONNX models on a Raspberry Pi 4, use ONNX Runtime’s CPU execution provider and make sure the model is quantized in a supported format. ONNX Runtime supports INT8 quantization via `quantize_dynamic()` or `quantize_static()`, and on CPU it can run U8U8, U8S8, and S8S8 formats; the docs recommend S8S8 with QDQ as the default choice.[^2_1]

## How to run it

1. Install a Raspberry Pi 4 compatible ONNX Runtime build.
2. Load the INT8 ONNX model with `InferenceSession(..., providers=["CPUExecutionProvider"])`.
3. Feed NumPy inputs and run `session.run(...)` as usual.

Example:

```python
import onnxruntime as ort

session = ort.InferenceSession(
    "model_quantized.onnx",
    providers=["CPUExecutionProvider"],
)
outputs = session.run(None, inputs_dict)
```

For quantization itself, ONNX Runtime recommends static quantization for CNNs and dynamic quantization more often for RNNs/transformers.[^2_1]

## Latency benchmarks

Published Raspberry Pi 4 benchmarks are highly model-dependent, but one study on a Raspberry Pi 4B using ONNX Runtime reported these MobileNetV2 latencies for ONNX:

- Single-stream: FP32 102.8 ms, INT8-SQ 138.8 ms, INT8-DQ 174.4 ms.[^2_2]
- Multi-stream: FP32 800.2 ms, INT8-SQ 997.9 ms, INT8-DQ 1520.9 ms.[^2_2]
- Offline throughput: FP32 16.5 images/s, INT8-SQ 12.4 images/s, INT8-DQ 7.4 images/s.[^2_2]

That same paper found ONNX quantization on Raspberry Pi 4 did **not** improve performance for MobileNetV2, while PyTorch/TFLite did better on that hardware for some models.[^2_2]

## What to expect

INT8 does **not** automatically mean faster on a Raspberry Pi 4. ONNX Runtime’s own quantization docs say older hardware may lack the instructions needed for efficient INT8 inference, so quantization can even be slower due to quantize/dequantize overhead.[^2_1]

## Practical takeaway

If your goal is best latency on Pi 4:

- Try **static INT8 QDQ** first for CNNs.[^2_1]
- Benchmark against FP32 on your exact model, because gains vary a lot by architecture.[^2_1][^2_2]
- Don’t assume ONNX Runtime INT8 will beat FP32 on Raspberry Pi 4; in at least one published benchmark it did not.[^2_2]

If you want, I can also give you a minimal Python benchmark script for Raspberry Pi 4 that measures FP32 vs INT8 ONNX Runtime latency.
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_20][^2_21][^2_3][^2_4][^2_5][^2_6][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html

[^2_2]: https://par.nsf.gov/servlets/purl/10428367

[^2_3]: https://dev.to/syamaner/part-4-edge-deployment-of-an-86m-parameter-audio-transformer-1821

[^2_4]: https://github.com/MeghaaVerse/onnx-int8-quantization-pipeline

[^2_5]: https://advances.vsb.cz/uploads/early-access-articles/ONNX-based Architectures for Post-Training Quantization Face Detection on Edge Devices.pdf

[^2_6]: https://github.com/microsoft/onnxruntime/issues/6732

[^2_7]: https://huggingface.co/Makatia/TinyLlama_TinyLlama-1.1B-Chat-v1.0_onnx/blob/d1de69a29ac5a98d3bcfab1a8982dd7e4c00f2b0/README.md

[^2_8]: https://openaccess.thecvf.com/content/ICCV2025W/AIM/papers/Yoon_LiteRT-Optimized_INT8_LLM_for_Raspberry_Pi4_Deployment_ICCVW_2025_paper.pdf

[^2_9]: https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/Quantizing-ONNX-Models-using-Intel-Neural-Compressor/post/1355237

[^2_10]: https://deepwiki.com/rolyantrauts/bcresnet/6.2-raspberry-pi-and-desktop-deployment

[^2_11]: https://www.reddit.com/r/computervision/comments/1ixm3qk/struggling_to_get_int8_quantisation_working_from/

[^2_12]: https://www.jobpreparena.com/blog/deploying-quantized-models-to-the-edge-a-guide-to-onnx-runtime-on-arm64

[^2_13]: https://deepwiki.com/k2-fsa/sherpa/7.3-performance-optimization

[^2_14]: https://www.samy101.com/edge-ai-26/projects/plant-disease-detection/

[^2_15]: https://www.youtube.com/watch?v=XdoHYgdIFrQ

[^2_16]: https://www.youtube.com/watch?v=WDww8ce12Mc

[^2_17]: https://www.youtube.com/watch?v=l9gyN1J5CCM

[^2_18]: https://www.youtube.com/watch?v=ClM9nE1LnTM

[^2_19]: https://www.youtube.com/watch?v=BEDEscDQFxk

[^2_20]: https://www.youtube.com/watch?v=WEqzbBDqs2I

[^2_21]: https://www.youtube.com/watch?v=1XFa2L7tBGM


---

# What are the limitations of ONNX Runtime on ARM64 compared to x86? Any known issues with quantized models?

ONNX Runtime on ARM64 is generally usable, but compared with x86 it can have fewer optimized kernels, less mature packaging, and more performance variability on edge devices. Quantized models are especially sensitive because speedups depend on the exact operator mix and whether the ARM64 kernel path is well optimized.[^3_1][^3_2]

## Main ARM64 limitations

- Performance can lag x86 for the same model, because optimization coverage is not identical across architectures and some mobile/edge scenarios show worse latency on ARM32 than ARM64, indicating kernel maturity matters.[^3_1]
- Official prebuilt support is narrower on some ARM targets, so users often end up building from source or relying on device-specific packages.[^3_3][^3_4]
- Memory and deployment constraints are more noticeable on small ARM boards, which can make model loading and inference less forgiving.[^3_5]


## Quantized model issues

- Quantized models can be **slower** than FP32 on some hardware, due to quantize/dequantize overhead and weak INT8 instruction support; ONNX Runtime explicitly warns that older hardware may not benefit much from INT8.[^3_2]
- There are reports of **different inference results** between x86_64 and aarch64 CPU runs for quantized models, which suggests cross-architecture numerical or kernel-path differences.[^3_6]
- Some ARM64 mobile deployments report **INT8 load failures** or runtime errors with certain execution providers or model/export combinations.[^3_7]


## Practical implications

- If a quantized model behaves oddly on ARM64, check whether the issue is model export, operator support, or an architecture-specific kernel difference rather than assuming quantization itself is broken.[^3_2][^3_6]
- For CPU-only ARM64, INT8 is not guaranteed to outperform FP32; benchmark both on the target device.[^3_8][^3_2]
- If you need best ARM64 performance, use a model/export path known to work well on ARM64 and test with the exact ONNX Runtime version you plan to ship.[^3_4][^3_1]


## Bottom line

The biggest ARM64-vs-x86 gaps are **kernel maturity, packaging breadth, and quantized-model consistency/performance**. Quantized models may run slower, fail to load in some setups, or produce slightly different outputs on aarch64 compared with x86.[^3_6][^3_7][^3_2]

If you want, I can also give you a checklist for diagnosing a quantized ONNX model that runs on x86 but fails or slows down on ARM64.
<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_15][^3_16][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://github.com/microsoft/onnxruntime/issues/16426

[^3_2]: https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html

[^3_3]: https://github.com/microsoft/onnxruntime/issues/19162

[^3_4]: https://onnxruntime.ai/docs/build/

[^3_5]: https://ask.csdn.net/questions/8705331

[^3_6]: https://github.com/microsoft/onnxruntime/issues/20479

[^3_7]: https://github.com/microsoft/onnxruntime/issues/25507

[^3_8]: https://github.com/microsoft/onnxruntime/issues/6732

[^3_9]: https://polyglottos.app/blog/onnx-quantization-mobile/

[^3_10]: https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html

[^3_11]: https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX/discussions/17

[^3_12]: https://huggingface.co/mrsladoje/CodeRankEmbed-onnx-int8?library=transformers

[^3_13]: https://ulopenaccess.com/papers/ULETE_V01I02/ULETE20240102_015.pdf

[^3_14]: https://github.com/microsoft/onnxruntime/issues/25631

[^3_15]: https://quark.docs.amd.com/latest/onnx/onnx_faq.html

[^3_16]: https://www.jobpreparena.com/blog/deploying-quantized-models-to-the-edge-a-guide-to-onnx-runtime-on-arm64



---

## 🔗 Keterkaitan & Navigasi Riset
- [[Riset Index]]
- [[Cetak Biru KTI]]
- [[WebAssembly_vs_Docker]]
- [[WebAssembly_Sandboxing]]
- [[Post-Training Quantization]]
- [[Single Board Computer]]
