<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# What is the current stability of WasmEdge on Raspberry Pi 4 ARM64? Which version is recommended for production use?

WasmEdge does support Raspberry Pi 4 on ARM64, but the docs I found only explicitly mention Raspberry Pi 3/64-bit ARM support, not a special Pi 4 stability guarantee. Based on the available sources, it appears usable on Raspberry Pi 4 ARM64, but I couldn’t verify any official “stable on Pi 4” statement.[^1_1][^1_2]

## Production version

For production, the safest choice is generally the latest tagged release rather than a dev branch or source build, and the project’s release listings show active releases through 2025. The search results also surface distro packages around 0.14.1 and release artifacts like 0.16.3, so if you want the most conservative production option, pick the latest official stable release available for your platform from WasmEdge’s releases page.[^1_3][^1_4][^1_5]

## Practical recommendation

- Use a 64-bit OS on the Pi.
- Prefer an official release build over a GitHub `main` build.
- If you need maximum operational conservatism, pin to the latest non-prerelease stable tag and test it on your exact Pi 4 workload first.[^1_1][^1_3]

If you want, I can look up the latest exact WasmEdge release tag for ARM64 and tell you which download to use on Raspberry Pi 4.
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://wasmedge.org/docs/contribute/source/os/raspberrypi/

[^1_2]: https://wasmedge.org/docs/category/supported-platforms/

[^1_3]: https://github.com/WasmEdge/WasmEdge/releases

[^1_4]: https://packages.debian.org/unstable/web/wasmedge

[^1_5]: https://sourceforge.net/projects/wasmedge.mirror/files/0.16.3/

[^1_6]: https://wasmedge.org/book/en/contribute/build_from_src/raspberrypi

[^1_7]: https://wasmruntime.com/en/tutorials/wasmedge

[^1_8]: https://github.com/WasmEdge/WasmEdge/issues/1147

[^1_9]: https://github.com/WasmEdge/WasmEdge/blob/master/docs/book/zh/src/os/raspberrypi.md

[^1_10]: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/container-runtimes-wasmedge-arm

[^1_11]: https://github.com/wasmedge

[^1_12]: https://kevingzhang.github.io/posts/run-wasm-in-raspberry-pi-4-today/

[^1_13]: https://github.com/WasmEdge/docs/blob/main/docs/contribute/source/build_from_src.md

[^1_14]: https://sourceforge.net/projects/wasmedge.mirror/files/0.13.5/


---

# How to install and use WasmEdge WASI-NN with TFLite backend on ARM64? Is it available as pre-built binary or must be compiled from source?

WasmEdge can use the WASI-NN TensorFlow Lite backend by installing the `wasi_nn-tensorflowlite` plugin and then running a WASM app that loads the `.tflite` model. The example docs show `install.sh` with `--plugins wasi_nn-tensorflowlite`, plus the need to place the TensorFlow Lite shared libraries in `~/.wasmedge/lib`, and then execute the WASM module with `wasmedge ...`[^2_1][^2_2][^2_3]

## ARM64 availability

For ARM64, the evidence I found shows WasmEdge provides pre-built TensorFlow Lite dependencies for `android_aarch64`, but the example download in the docs is for `manylinux2014_x86_64`, not ARM64. That means the TFLite backend itself is supported conceptually, but I did not find an official pre-built Linux ARM64 plugin bundle in the surfaced docs.[^2_4][^2_1]

## Install path

Typical flow is:

1. Install WasmEdge.
2. Install the WASI-NN TFLite plugin.
3. Install the TensorFlow Lite shared libraries required by the plugin.
4. Build your app to `wasm32-wasip1` and run it with WasmEdge.[^2_2][^2_3][^2_5]

Example from the docs:

```bash
VERSION=0.13.1
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- -v $VERSION --plugins wasi_nn-tensorflowlite
```

Then run a WASI-NN example or your own module with `wasmedge`.[^2_1][^2_2]

## Pre-built or source

I found pre-built artifacts for some platforms and examples, but not a clear official ARM64 Linux pre-built WASI-NN TFLite package in the results above. So for ARM64 Linux, you should expect to compile from source or build the plugin/runtime yourself unless you find a matching release artifact for your exact platform.[^2_6][^2_4][^2_1]

## Practical recommendation

- If you are on ARM64 Linux, try the official installer first and check whether it downloads an ARM64 plugin for your version.[^2_5][^2_1]
- If not, build WasmEdge and the WASI-NN TFLite plugin from source for ARM64.
- Use the latest stable WasmEdge release compatible with the plugin version you need, and pin versions together to avoid ABI mismatches.[^2_3][^2_7][^2_5]

If you want, I can next give you a step-by-step ARM64 build/install command set for Raspberry Pi 4 or Ubuntu ARM64.
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://github.com/WasmEdge/wasmedge_hyper_demo/tree/main/server-tflite

[^2_2]: https://github.com/wasmedge/docs/blob/main/docs/develop/rust/wasinn/tensorflow_lite.md

[^2_3]: https://wasmedge.org/docs/develop/rust/wasinn/tf_plugin/

[^2_4]: https://github.com/WasmEdge/docs/blob/main/docs/contribute/source/os/android/cli.md

[^2_5]: https://wasmedge.org/docs/start/install/

[^2_6]: https://llamaedge.com/docs/ai-models/speech-to-text/quick-start-whisper/

[^2_7]: https://github.com/WasmEdge/WasmEdge/releases

[^2_8]: https://wasmedge.org/docs/contribute/source/plugin/wasi_nn/

[^2_9]: https://deepwiki.com/WasmEdge/WasmEdge/3.2-wasi-nn-plugin

[^2_10]: https://github.com/wasmedge/docs/blob/main/docs/develop/javascript/tensorflow.md

[^2_11]: https://github.com/second-state/WasmEdge-WASINN-examples

[^2_12]: https://wasmedge.org/

[^2_13]: https://deepwiki.com/second-state/WasmEdge-WASINN-examples/9-development-guide

[^2_14]: https://huggingface.co/juntaoyuan/llawa/raw/099298c938a6ab9e90662d01a361da52817ff9f0/README.md

[^2_15]: https://wasmruntime.com/en/tutorials/wasmedge

[^2_16]: https://sourceforge.net/projects/wasmedge.mirror/files/0.13.5/


---

# WasmEdge WASI-NN TFLite ARM64 known issues 2024 2025 — what breaks and what are the workarounds?

The main TFLite-side breakage I found for 2024–2025 is not ARM64-specific but API/package mismatch: WasmEdge’s TensorFlow/TFLite plug-in is **not** the same thing as the WASI-NN plug-in, and the docs explicitly warn that if you want the WASI-NN crate you should use the TensorFlow-Lite backend instead.[^3_1][^3_2]

## What breaks

- Using the TensorFlow plug-in as if it were WASI-NN, which fails because it is a different interface. The docs call this out directly.[^3_1]
- Treating TensorFlow models like TFLite models. For TensorFlow, the backend has issues around SavedModel paths, file layout, and pre-opening paths in WASI; the project’s own issue tracker lists this as a problem and explains why the TFLite backend is often the workaround.[^3_3]
- Expecting a clean ARM64 prebuilt plugin story on Linux. The surfaced docs show ARM64 examples and Android AArch64 dependencies, but not a clearly documented Linux ARM64 prebuilt TFLite/WASI-NN bundle.[^3_4][^3_5]


## Workarounds

- Prefer **TFLite** over TensorFlow when using WASI-NN; that is the project’s recommended workaround for the TensorFlow backend’s limitations.[^3_3]
- Use the WasmEdge TensorFlow-Lite plug-in and the `TFLiteSession` flow from the examples/docs rather than the plain WASI-NN crate if you are integrating directly in Rust.[^3_2][^3_1]
- Build from source on ARM64 if the installer does not provide a matching plugin binary for your platform/version. The install docs cover plugin installation, but the exact ARM64 Linux binary availability was not clear in the sources surfaced here.[^3_5][^3_6]


## Practical takeaway

For ARM64 in 2024–2025, the most reliable path is usually: use a TFLite model, pin compatible WasmEdge/plugin versions, and be prepared to compile the plugin/runtime from source if your target platform does not have a matching release artifact.[^3_6][^3_2][^3_5]

If you want, I can next dig into specific GitHub issues for ARM64 runtime failures, linker errors, or TFLite shared-library loading problems and summarize the exact fixes.
<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_15][^3_16][^3_17][^3_7][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://wasmedge.org/docs/develop/rust/wasinn/tf_plugin/

[^3_2]: https://github.com/wasmedge/docs/blob/main/docs/develop/rust/wasinn/tensorflow_lite.md

[^3_3]: https://github.com/WasmEdge/WasmEdge/issues/2339

[^3_4]: https://github.com/WasmEdge/docs/blob/main/docs/contribute/source/os/android/cli.md

[^3_5]: https://github.com/WasmEdge/wasmedge_hyper_demo/tree/main/server-tflite

[^3_6]: https://wasmedge.org/docs/start/install/

[^3_7]: https://github.com/WasmEdge/WasmEdge/issues/

[^3_8]: https://opencollective.ecosyste.ms/projects/548/issues?page=3\&per_page=100

[^3_9]: https://deepwiki.com/second-state/WasmEdge-WASINN-examples/12-troubleshooting-and-faq

[^3_10]: https://sourceforge.net/projects/wasmedge.mirror/files/0.14.0/

[^3_11]: https://newreleases.io/project/github/WasmEdge/WasmEdge/release/0.16.0

[^3_12]: https://newreleases.io/project/github/WasmEdge/WasmEdge/release/0.14.1-beta.1

[^3_13]: https://www.systemshardening.com/articles/wasm/wasmedge-security/

[^3_14]: https://europe2024.gosim.org/images/speakers/66425384dc4e6823eea75742_Hung-Ying_Tai-GOSIM-2024-Write_Once_Run_Anywhere_But_for_GPUs.pdf

[^3_15]: https://wasmedge.org/docs/contribute/source/plugin/wasi_nn/

[^3_16]: https://github.com/wasmedge/docs/blob/main/docs/develop/javascript/tensorflow.md

[^3_17]: https://wasmruntime.com/en/tutorials/wasmedge

