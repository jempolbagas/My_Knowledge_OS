<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Can a WebAssembly module call a native process on the host system? What are the mechanisms — WASI sockets, stdin/stdout, shared memory?

A WebAssembly module generally **cannot directly call an arbitrary native process** on the host. It can only do so indirectly through host-provided capabilities such as WASI, custom imports, or by communicating with a separate host process that the runtime starts or exposes.[^1_1][^1_2]

## What it can do

- **stdin/stdout/stderr:** The most common mechanism for a WASI module to exchange data with the host is standard I/O, just like a Unix program. The host runtime maps these streams to the module’s file descriptors and moves bytes through the module’s linear memory.[^1_2][^1_3][^1_4]
- **Sockets:** With WASI sockets, the module can talk over TCP/UDP to a service on the host or elsewhere. That still isn’t “calling a process” directly; it’s network communication with something the host exposes.[^1_5][^1_1]
- **Shared memory:** WebAssembly linear memory can be shared with the host runtime, and the host can read/write it. This is useful for passing buffers efficiently, but it is not the same as invoking a native process; it’s just shared data exchange.[^1_6][^1_1]


## Bottom line

If you mean “can Wasm spawn or invoke an OS process like `ls` or `git` itself?”, the answer is **no, not by default**. If you mean “can Wasm ask the host to do something, or communicate with a native program the host provides?”, **yes** — via WASI I/O, sockets, or custom host imports.[^1_1][^1_2]

If you want, I can also sketch the difference between **WASI**, **custom imports**, and **embedding Wasm inside a native app**.
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://salivity.github.io/wasm/article/how-webassembly-handles-system-calls-and-file-io

[^1_2]: https://www.cs.unb.ca/~bremner/teaching/cs2613/books/nodejs-api/wasi/

[^1_3]: https://petermalmgren.com/serverside-wasm-data/

[^1_4]: https://salivity.github.io/wasm/article/how-webassembly-handles-stdin-stdout-and-stderr

[^1_5]: https://wippy.ai/en/wasm/hosts

[^1_6]: https://edadma.github.io/wasm/wasi/syscalls/

[^1_7]: https://wa.dev/wasi:cli

[^1_8]: https://docs.wasmtime.dev/api/wasmtime_wasi/struct.WasiCtxBuilder.html

[^1_9]: https://docs.wasmtime.dev/api/wasmtime_wasi/p2/index.html

[^1_10]: https://deepwiki.com/bytecodealliance/wasm-micro-runtime/5.1-wasi-implementation

[^1_11]: https://github.com/WebAssembly/WASI/pkgs/container/wasi%2Fsockets

[^1_12]: https://developer.mozilla.org/en-US/docs/WebAssembly/Guides/Loading_and_running

[^1_13]: https://www.webassembly-wasm.com/webassembly-core-concepts-browser-runtime/browser-sandbox-security-boundaries/

[^1_14]: https://k33g.hashnode.dev/wasi-communication-between-nodejs-and-wasm-modules-another-way-with-stdin-and-stdout

[^1_15]: https://www.secondstate.io/articles/call-native-functions-from-javascript/


---

# WasmEdge + ONNX Runtime hybrid architecture — running inference outside the Wasm sandbox via IPC

Yes — that architecture is plausible, but it’s not “Wasm calling a native process directly.” It’s usually **WasmEdge running a Wasm module that offloads inference to an out-of-sandbox host service** over IPC, sockets, or a host function boundary. The clean design is: the Wasm module handles control flow and preprocessing, while the native ONNX Runtime service does the heavy inference work outside the sandbox.[^2_1][^2_2]

## Typical layout

- **Wasm module:** receives input, validates it, preprocesses/postprocesses, and sends tensors or serialized requests to the host.
- **Native host service:** runs ONNX Runtime and exposes a local API over IPC, Unix domain sockets, TCP, or a custom embedding API.
- **Result path:** the service returns outputs; the module consumes them and continues execution. This matches ONNX Runtime’s general model of delegating execution to a specialized backend via partitioned execution/provider boundaries, though in your case the boundary is the host process rather than an execution provider inside the same process.[^2_1]


## How the communication usually works

| Mechanism | Fits this design? | Notes |
| :-- | --: | :-- |
| stdin/stdout | Yes | Simple for request/response, but clunky for streaming and multiplexing. [^2_3][^2_4] |
| WASI sockets | Yes | Better for persistent bidirectional communication with a local inference daemon. [^2_5][^2_6] |
| Shared memory | Sometimes | Good for large tensors, but you still need a control channel; shared memory alone does not invoke anything. [^2_7] |
| Custom host imports | Yes | Fastest integration if you control the WasmEdge embedding/runtime side. [^2_8] |

## Practical recommendation

For ONNX inference outside the sandbox, the most robust pattern is **WASI sockets or a Unix-domain-socket IPC service**. Use a thin wire format such as flat buffers, protobuf, or raw tensor bytes, and keep the Wasm side stateless except for request assembly and response parsing. If you need maximum throughput, pair IPC with shared-memory buffers; if you need simplest integration, use stdin/stdout.[^2_3][^2_5][^2_7]

## Caveat

If your goal is just “run ONNX inside WasmEdge,” that’s a different pattern: WasmEdge also has native AI/WASI-NN paths for in-sandbox inference, which avoids IPC overhead. But if your goal is isolation or a separate model-serving process, IPC is the right abstraction.[^2_2]

If you want, I can sketch a concrete **WasmEdge + host ORT IPC protocol** or a **Rust/C++ process boundary design** next.
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_20][^2_21][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://onnxruntime.ai/docs/reference/high-level-design.html

[^2_2]: https://wasmedge.org/docs/category/ai-inference/

[^2_3]: https://petermalmgren.com/serverside-wasm-data/

[^2_4]: https://salivity.github.io/wasm/article/how-webassembly-handles-stdin-stdout-and-stderr

[^2_5]: https://salivity.github.io/wasm/article/how-webassembly-handles-system-calls-and-file-io

[^2_6]: https://www.cs.unb.ca/~bremner/teaching/cs2613/books/nodejs-api/wasi/

[^2_7]: https://edadma.github.io/wasm/wasi/syscalls/

[^2_8]: https://wippy.ai/en/wasm/hosts

[^2_9]: https://learn.microsoft.com/ja-jp/azure/iot-operations/develop-edge-apps/howto-wasm-onnx-inference

[^2_10]: https://learn.microsoft.com/en-us/azure/iot-operations/develop-edge-apps/howto-wasm-onnx-inference

[^2_11]: https://devtechtools.org/en/blog/edge-inference-real-time-personalization-wasm-onnx-runtime

[^2_12]: https://learn.microsoft.com/ko-kr/azure/iot-operations/develop-edge-apps/howto-wasm-onnx-inference

[^2_13]: https://www.youngju.dev/blog/culture/2026-03-22-webassembly-wasm-2025-server-side-edge.en

[^2_14]: https://learn.microsoft.com/pl-pl/azure/iot-operations/develop-edge-apps/howto-wasm-onnx-inference

[^2_15]: https://onnxruntime.ai/docs/tutorials/web/

[^2_16]: https://learn.microsoft.com/id-id/azure/iot-operations/develop-edge-apps/howto-wasm-onnx-inference

[^2_17]: https://wasmedge.org/docs/contribute/source/build_from_src/

[^2_18]: https://wjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-1832.pdf

[^2_19]: https://wasmruntime.com/en/tutorials/wasmedge

[^2_20]: https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/

[^2_21]: https://stackoverflow.com/questions/79706140/unable-to-run-inference-in-onnxruntime-web-wasm-backend-proxy-mode-with-multi

