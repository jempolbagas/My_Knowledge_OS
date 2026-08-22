---
title: "Browser Sandbox & Security Boundaries"
source: "https://www.webassembly-wasm.com/webassembly-core-concepts-browser-runtime/browser-sandbox-security-boundaries/"
author:
published:
created: 2026-07-28
description: "How the WebAssembly browser sandbox works — capability-based imports, bounds-checked linear memory, control-flow integrity, COOP/COEP isolation, Spectre mitigations, and CSP."
tags:
  - "clippings"
---
## Browser Sandbox & Security Boundaries

A WebAssembly module is one of the most tightly confined things a browser will run: it starts with zero ambient authority — no DOM, no network, no filesystem, no clock beyond what JavaScript hands it — and every byte it can touch lives inside a single bounds-checked buffer. This guide explains the machinery that enforces that confinement, where the trust boundary actually sits, and the handful of HTTP headers and policies you must get right so the sandbox stays intact when you start sharing memory across threads.

## Prerequisites

- A modern engine with the relevant features: Chrome/Edge 119+, Firefox 120+, or Safari 17+
- `wabt` ≥ 1.0.34 for `wasm-validate` and `wasm-objdump` (`brew install wabt` / `apt install wabt`)
- A local server you can set response headers on (the `crossOriginIsolated` checks below need them)
- Familiarity with the [stack-based execution model](https://www.webassembly-wasm.com/webassembly-core-concepts-browser-runtime/stack-vs-heap-execution-model/) and how `linear memory` is addressed
- DevTools open, Console tab — every verification step below runs from there

## The trust boundary: capabilities granted through the import object

The single idea that makes WebAssembly safe is *capability-based* execution. A compiled module cannot name a syscall, dereference a host pointer, or reach `document` directly. It can only call functions that JavaScript explicitly placed in the `import object` at instantiation time. If you never import a function that calls `fetch`, the module physically cannot make a network request — the capability does not exist in its world. This is the inverse of the ambient-authority model native processes use, where code inherits every privilege of the user running it.

<svg viewBox="0 0 880 330" role="img" aria-label="The JavaScript host holds full authority while the Wasm instance has none, and the import object is the only channel between them" style="max-width:100%;height:auto" xmlns="http://www.w3.org/2000/svg"><title>Zero ambient authority, one explicit channel</title> <desc>The host page can reach the DOM, the network and the file system. A Wasm instance can reach none of them. Everything it can do arrives through the import object the host chose to pass, and its memory is a bounds-checked buffer the host also owns.</desc> <rect x="0" y="0" width="880" height="330" fill="#FAFAFF"></rect><rect x="16" y="40" width="250" height="230" rx="8" fill="#E8F0FF" stroke="#2563EB" stroke-width="1.5"></rect><text x="141" y="66" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="12.5" font-weight="700" fill="#1A1035">JavaScript host</text> <text x="141" y="86" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">full ambient authority</text> <rect x="40" y="102" width="202" height="34" rx="4" fill="#FFFFFF" stroke="#D5CCFF" stroke-width="1"></rect><text x="141" y="124" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#3D1A8E">document / window</text> <rect x="40" y="144" width="202" height="34" rx="4" fill="#FFFFFF" stroke="#D5CCFF" stroke-width="1"></rect><text x="141" y="166" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#3D1A8E">fetch / WebSocket</text> <rect x="40" y="186" width="202" height="34" rx="4" fill="#FFFFFF" stroke="#D5CCFF" stroke-width="1"></rect><text x="141" y="208" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#3D1A8E">File System Access</text> <text x="141" y="248" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">whatever the origin already had</text> <rect x="316" y="90" width="220" height="130" rx="8" fill="#FFF6E5" stroke="#F59E0B" stroke-width="1.5"></rect><text x="426" y="116" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="12.5" font-weight="700" fill="#1A1035">import object</text> <text x="426" y="136" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">the only channel in</text> <rect x="336" y="150" width="180" height="28" rx="4" fill="#FFFFFF" stroke="#F59E0B" stroke-width="1"></rect><text x="426" y="169" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#3D1A8E">env.log</text> <rect x="336" y="182" width="180" height="28" rx="4" fill="#FFFFFF" stroke="#F59E0B" stroke-width="1"></rect><text x="426" y="201" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#3D1A8E">env.now</text> <rect x="592" y="40" width="272" height="230" rx="8" fill="#F0EDFF" stroke="#5E35B1" stroke-width="1.5"></rect><text x="728" y="66" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="12.5" font-weight="700" fill="#1A1035">Wasm instance</text> <text x="728" y="86" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">zero ambient authority</text> <rect x="616" y="102" width="224" height="50" rx="4" fill="#FFFFFF" stroke="#D5CCFF" stroke-width="1"></rect><text x="728" y="122" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#3D1A8E">linear memory</text> <text x="728" y="140" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#5B5570">bounds-checked, host-owned</text> <rect x="616" y="160" width="224" height="50" rx="4" fill="#FFFFFF" stroke="#D5CCFF" stroke-width="1"></rect><text x="728" y="180" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#3D1A8E">exported functions</text> <text x="728" y="198" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#5B5570">the only channel out</text> <text x="728" y="240" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">no syscalls, no globals, no DOM</text> <line x1="266" y1="155" x2="312" y2="155" stroke="#5B5570" stroke-width="1.6" marker-end="url(#sb-a)"></line><text x="289" y="146" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="9.5" fill="#5B5570">grants</text> <line x1="536" y1="155" x2="588" y2="155" stroke="#5B5570" stroke-width="1.6" marker-end="url(#sb-a)"></line><line x1="266" y1="119" x2="588" y2="105" stroke="#DB2777" stroke-width="1.3" stroke-dasharray="6 5"></line><text x="426" y="66" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#DB2777">not reachable directly — no path exists to draw</text> <text x="16" y="306" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">A Wasm module cannot escape this shape; it can only misuse what you handed it. Auditing the import object is auditing the capability set.</text><defs><marker id="sb-a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#5B5570"></path></marker></defs></svg>

Everything the module is allowed to affect in the outside world passes through that doorway. Nothing crosses it implicitly. The deeper interop mechanics of how data — not just authority — moves through this channel are covered in [JS/Wasm interop & memory management](https://www.webassembly-wasm.com/js-wasm-interop-memory-management/), but for security the rule is simpler: **the import object is the entire attack surface you grant.**

## Bounds-checked linear memory

A module’s heap is a single contiguous `ArrayBuffer` called `linear memory`, sized in 64 KiB `page` units. Every `load` and `store` the module executes carries an `i32` offset into that buffer, and the engine bounds-checks every one of them. An access past `memory.byteLength` does not read adjacent host memory or crash the tab — it deterministically raises a `trap`, which surfaces in JavaScript as a `WebAssembly.RuntimeError`. A pointer in Wasm is just an index into this buffer; it can never name an address the engine did not allocate, so a buffer overflow inside the module stays inside the module.

```wat
(module
  (memory (export "memory") 1)              ;; exactly one 64 KiB page
  (func (export "peek") (param $off i32) (result i32)
    (i32.load (local.get $off)))            ;; off >= 65536 traps, never escapes
)
```

You should still cap growth explicitly. An unbounded `WebAssembly.Memory` can be grown by a misbehaving or malicious module until the tab is OOM-killed, so set a hard `maximum` at construction:

```js
const memory = new WebAssembly.Memory({
  initial: 2,    // 128 KiB to start
  maximum: 64,   // 4 MiB hard ceiling — memory.grow past this fails, returns -1
});
```

This is the same isolation that makes pointer hand-offs across the boundary safe: the value stack and `linear memory` heap are addressed separately, so an overflow in one cannot reach the other, and every offset you receive from JavaScript should still be treated as untrusted and re-validated.

There is a subtlety worth internalizing: bounds checking protects the *host*, not your application logic. A module cannot read past its own memory, but nothing stops it from reading the wrong part of its own memory if your glue code hands it a bad offset. Security at the boundary is therefore a shared responsibility — the engine guarantees the module cannot escape the buffer, and you guarantee the offsets and lengths flowing across the boundary actually describe the data you intend. Most real-world Wasm “security” bugs are this second kind: a confused-deputy mistake in the JavaScript glue, not a sandbox escape. Validate every `(ptr, len)` pair against the current `memory.byteLength` before constructing a view, and treat any length you did not compute yourself as hostile.

<svg viewBox="0 0 860 280" role="img" aria-label="A pointer past the end of linear memory traps deterministically instead of reading adjacent process memory" style="max-width:100%;height:auto" xmlns="http://www.w3.org/2000/svg"><title>What an out-of-bounds access can and cannot reach</title> <desc>Inside the module, a buffer overrun can corrupt other data in the same linear memory — a real bug. What it cannot do is read outside the buffer: any access past the current size traps immediately, so the engine's own structures and the rest of the process stay unreachable.</desc> <rect x="0" y="0" width="860" height="280" fill="#FAFAFF"></rect><rect x="20" y="52" width="520" height="120" rx="8" fill="#F0EDFF" stroke="#5E35B1" stroke-width="1.5"></rect><text x="280" y="40" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#3D1A8E">linear memory — one ArrayBuffer, offset 0 to size</text> <rect x="44" y="78" width="140" height="68" rx="4" fill="#FFFFFF" stroke="#D5CCFF" stroke-width="1"></rect><text x="114" y="108" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#3D1A8E">static data</text> <rect x="196" y="78" width="140" height="68" rx="4" fill="#FFE8F5" stroke="#DB2777" stroke-width="1"></rect><text x="266" y="102" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#1A1035">buffer A</text> <text x="266" y="124" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#5B5570">overrun lands here</text> <rect x="348" y="78" width="170" height="68" rx="4" fill="#FFFFFF" stroke="#D5CCFF" stroke-width="1"></rect><text x="433" y="108" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#3D1A8E">buffer B — corruptible</text> <line x1="266" y1="146" x2="400" y2="146" stroke="#DB2777" stroke-width="1.5" marker-end="url(#bx-a)"></line><text x="336" y="164" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#DB2777">a real memory-safety bug, inside the sandbox</text> <rect x="600" y="52" width="240" height="120" rx="8" fill="#E6F7EE" stroke="#15803D" stroke-width="1.5"></rect><text x="720" y="82" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#1A1035">everything else</text> <text x="720" y="106" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">engine internals · JS heap</text> <text x="720" y="126" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">other instances · the process</text> <text x="720" y="152" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#15803D">unreachable by construction</text> <line x1="540" y1="112" x2="596" y2="112" stroke="#DB2777" stroke-width="1.6" stroke-dasharray="6 4" marker-end="url(#bx-b)"></line><text x="568" y="200" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#DB2777">trap</text> <text x="20" y="234" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">Every load and store is bounds-checked against the current size, so the failure mode is a deterministic RuntimeError, not silent memory disclosure.</text> <text x="20" y="256" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">This is the key distinction: Wasm contains memory-safety bugs, it does not eliminate them.</text><defs><marker id="bx-a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#DB2777"></path></marker><marker id="bx-b" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#DB2777"></path></marker></defs></svg>

## Control-flow integrity

Native exploitation usually pivots on corrupting a return address or jumping into the middle of an instruction. WebAssembly makes both impossible structurally. The call stack and return addresses live in protected engine state the module cannot address — they are *not* in `linear memory`, so no overflow can overwrite them. Branches can only target labels that the validator proved exist, and indirect calls go through a `table` of typed function references: an `i32.const` index into that table, with the engine checking the callee’s type signature against the call site at runtime. A type mismatch traps. There are no computed jumps into arbitrary code, no executable data pages, and no way to forge a function pointer out of an integer. The structural validation that guarantees this happens before any code runs, as detailed in the [Wasm binary format deep dive](https://www.webassembly-wasm.com/webassembly-core-concepts-browser-runtime/wasm-binary-format-deep-dive/).

The practical upshot for an engineer is that a whole class of bugs that are catastrophic in C — stack smashing, return-oriented programming, jumping to shellcode planted in a data buffer — are not just mitigated but *unrepresentable* in the WebAssembly execution model. The corresponding native bug usually turns into a `trap`: a deterministic, recoverable error you can catch in JavaScript, rather than silent memory corruption. That changes how you triage. A crash report from a Wasm module is almost always a logic error or an out-of-bounds access that the engine caught, not a foothold for an attacker.

## How the Wasm sandbox compares to a native process

It helps to place this model against the isolation a native process gets from the operating system. A native process is confined by the MMU and the kernel’s syscall boundary: it can do anything its user account permits, and the OS only stops it at page-fault and privilege-ring boundaries. A WebAssembly instance is confined far more tightly. It has no syscalls at all — only the functions you imported — and its entire addressable world is one `ArrayBuffer`, not a sparse virtual address space full of mapped libraries, the stack, and the heap. There is no `ptrace`, no `/proc`, no shared mutable global state with other instances unless you deliberately wire it up. Two modules instantiated on the same page are as isolated from each other as two browser tabs, because each owns a private `linear memory` and neither can name the other’s. This is why running an untrusted plugin as a Wasm module is a fundamentally stronger position than running it as a native shared library loaded into your process: the sandbox is the default, and every capability is opt-in rather than opt-out.

## Cross-origin isolation: COOP, COEP, and the timer problem

Single-threaded WebAssembly needs none of this. The moment you want threads, you need a `SharedArrayBuffer` so multiple Web Workers can see the same `linear memory` — and a `SharedArrayBuffer` re-enables the high-resolution, shared-state timing primitives that Spectre-class side-channel attacks depend on. Browsers therefore gate it behind **cross-origin isolation**: your top-level document must be served with two response headers, and only then is `SharedArrayBuffer` constructable and `crossOriginIsolated` true.

```text
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

`COOP: same-origin` severs the `window.opener` relationship so cross-origin documents cannot share a browsing-context group with yours. `COEP: require-corp` forces every subresource you load to explicitly opt in (via `Cross-Origin-Resource-Policy` or CORS), so no unconsented cross-origin data lands in your now-isolated process. Together they let the browser put your page in its own process where a leaked high-resolution timer reveals nothing it should not. The full threading model that depends on this lives under [SharedArrayBuffer, Atomics & threading](https://www.webassembly-wasm.com/js-wasm-interop-memory-management/sharedarraybuffer-atomics-threading/), and the exact local-server header setup is in [configuring COOP/COEP headers](https://www.webassembly-wasm.com/compilation-pipelines-toolchain-setup/local-development-server-configurations/configuring-coop-coep-headers-for-sharedarraybuffer/).

Even with isolation enabled, treat shared memory as a privilege you scope tightly. Browsers also clamp `performance.now()` resolution and add jitter outside isolated contexts precisely so that timing a memory read cannot be turned into a cache-probe oracle.

## Spectre and the timer side channel

Spectre-class attacks do not break the sandbox’s correctness — bounds checks still hold — they break its *confidentiality* by inferring secret bytes from how long an operation takes. Speculative execution can transiently access data past a bounds check before the check resolves, leaving a footprint in the CPU cache that an attacker reads back by timing subsequent accesses. The exploit therefore needs two things: a high-resolution clock and a way to share state with the victim. Browsers attack both. Outside a cross-origin-isolated context, `performance.now()` is coarsened (to ~100 µs in several engines) and deliberately jittered, and the precise multi-threaded timer you could build from a `SharedArrayBuffer` counter is simply unavailable because `SharedArrayBuffer` is gated off. This is the real reason the COOP and COEP dance exists: enabling shared memory hands back the timing precision an attacker needs, so the browser will only do it once your page has provably isolated itself into its own process where the secrets worth stealing are your own. The defensive posture for application code is straightforward — do not treat cross-origin isolation as a feature flag to flip casually, and never load secret-bearing cross-origin content into an isolated context where a co-resident module could time it.

## CSP for WebAssembly: wasm-unsafe-eval

Content Security Policy treats compiling a `.wasm` module as a form of code generation. Under a strict policy, `WebAssembly.compile` and `instantiate` are blocked unless you add the `'wasm-unsafe-eval'` source to `script-src`. This keyword is deliberately narrower than `'unsafe-eval'`: it permits WebAssembly compilation **without** re-enabling JavaScript `eval()` and `new Function()`, so you keep the strong JS protection while allowing Wasm.

```text
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'wasm-unsafe-eval';
  object-src 'none';
```

Pair this with Subresource Integrity on the loader script and a hash check on the binary itself (shown below) so only the exact module you shipped can run.

## Workflow: build a least-privilege loader

Follow these steps to instantiate a module with the smallest possible capability set and verify the sandbox held.

1. **Decide the capability budget.** List every host function the module genuinely needs. If it only logs, it gets `log` and nothing else — no `fetch`, no DOM accessor, no `eval` wrapper.
2. **Compile with hardening flags** so the binary itself is minimal and validated:
	```bash
	# Rust
	wasm-pack build --target web --release
	# C/C++
	emcc main.c -O3 -s ASSERTIONS=0 -s EXPORTED_FUNCTIONS="['_process']" -o out.js
	```
3. **Validate structure before shipping** and strip metadata that widens the attack surface:
	```bash
	wasm-validate out.wasm
	wasm-opt out.wasm -Oz --strip-debug --strip-producers -o out.opt.wasm
	```
4. **Verify the binary hash, then instantiate from the verified bytes** with a restrictive import object (full code in the next section).
5. **Audit the imports the module actually declares** so it cannot demand a capability you did not vet:
	```js
	const mod = await WebAssembly.compileStreaming(fetch("/out.opt.wasm"));
	WebAssembly.Module.imports(mod).forEach(i =>
	  console.log(\`${i.module}.${i.name} : ${i.kind}\`));
	// Reject if anything outside your allowlist appears
	```

## A restrictive import object

This loader grants exactly one capability — bounded logging — verifies the binary’s SHA-256 before instantiating, and exposes nothing else. Note that `instantiateStreaming` consumes the response body, so to hash the bytes you fetch them once into an `ArrayBuffer` and instantiate from that buffer.

```js
async function loadSandboxed(url, expectedHashB64) {
  const res = await fetch(url, { credentials: "same-origin" });
  if (!res.ok || res.headers.get("content-type") !== "application/wasm") {
    throw new Error("bad response or wrong MIME type");
  }
  const bytes = await res.arrayBuffer();

  // Integrity gate: refuse anything but the exact module we shipped
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  const got = btoa(String.fromCharCode(...new Uint8Array(digest)));
  if (got !== expectedHashB64) throw new Error("SRI mismatch — refusing to run");

  // The entire granted capability set — one function, length-clamped
  const importObject = {
    env: {
      log(ptr, len) {
        const mem = new Uint8Array(instance.exports.memory.buffer, ptr, Math.min(len, 4096));
        console.log("[wasm]", new TextDecoder().decode(mem));
      },
    },
  };

  const { instance } = await WebAssembly.instantiate(bytes, importObject);
  return instance;
}
```

There is no `fetch`, no `document`, no `eval` reachable from inside the module — and because the `log` length is clamped, a hostile module cannot coax the host into reading 4 GiB out of `linear memory`.

<svg viewBox="0 0 860 290" role="img" aria-label="A least-privilege import object grants only the capabilities a module needs, narrowing each one at the boundary" style="max-width:100%;height:auto" xmlns="http://www.w3.org/2000/svg"><title>Narrowing a capability at the boundary</title> <desc>A convenient import passes the raw capability straight through — an arbitrary fetch or an unbounded log. A least-privilege import wraps it: fixed origin, size limits, rate limits and validation, so the module receives a capability that cannot be misused beyond its purpose.</desc> <rect x="0" y="0" width="860" height="290" fill="#FAFAFF"></rect><text x="20" y="32" font-family="Inter, system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#DB2777">convenient — the capability passes through unchanged</text> <rect x="20" y="46" width="240" height="46" rx="6" fill="#FFE8F5" stroke="#DB2777" stroke-width="1.3"></rect><text x="140" y="74" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#1A1035">{ env: { fetch } }</text> <line x1="260" y1="69" x2="330" y2="69" stroke="#DB2777" stroke-width="1.4" marker-end="url(#lp-a)"></line><rect x="336" y="46" width="300" height="46" rx="6" fill="#F0EDFF" stroke="#5E35B1" stroke-width="1.3"></rect><text x="486" y="74" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#1A1035">the module can now call any URL your origin can</text> <text x="20" y="140" font-family="Inter, system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#15803D">least privilege — the host narrows it first</text> <rect x="20" y="154" width="240" height="76" rx="6" fill="#E6F7EE" stroke="#15803D" stroke-width="1.3"></rect><text x="140" y="178" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#1A1035">fetchTile(x, y)</text> <text x="140" y="198" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#5B5570">fixed origin · validated args</text> <text x="140" y="216" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#5B5570">rate limited · size capped</text> <line x1="260" y1="192" x2="330" y2="192" stroke="#15803D" stroke-width="1.4" marker-end="url(#lp-b)"></line><rect x="336" y="154" width="300" height="76" rx="6" fill="#F0EDFF" stroke="#5E35B1" stroke-width="1.3"></rect><text x="486" y="182" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#1A1035">the module can fetch map tiles</text> <text x="486" y="204" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#1A1035">and nothing else</text> <rect x="672" y="46" width="168" height="184" rx="8" fill="#FFF6E5" stroke="#F59E0B" stroke-width="1.3"></rect><text x="756" y="76" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="11" font-weight="700" fill="#1A1035">the review question</text> <text x="756" y="104" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">for each import:</text> <text x="756" y="128" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">what is the worst</text> <text x="756" y="148" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">a hostile module</text> <text x="756" y="168" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">could do with it?</text> <text x="756" y="200" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#C2410C">that is your blast radius</text> <text x="20" y="268" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="#5B5570">The sandbox is only as tight as the import object — it is the one part of the boundary you design rather than inherit.</text><defs><marker id="lp-a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#DB2777"></path></marker><marker id="lp-b" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#15803D"></path></marker></defs></svg>

## Gotchas & failure modes

- **`crossOriginIsolated` is `false` even though headers are “set.”** A single subresource without a `Cross-Origin-Resource-Policy` header (a font, an image from a CDN) fails the `COEP: require-corp` check and silently disables isolation for the whole page. `SharedArrayBuffer` is then `undefined`.
- **`CompileError: WebAssembly.instantiate(): Wasm code generation disallowed by embedder`.** Your CSP lacks `'wasm-unsafe-eval'` in `script-src`. Adding `'unsafe-eval'` also works but needlessly re-enables JavaScript `eval` — use the narrow keyword.
- **A `RuntimeError` you never see.** Wasm traps surface as rejected promises or thrown `RuntimeError` s. If your call site swallows them, an out-of-bounds access looks like a “nothing happened” bug. Wrap exported calls and report traps to your error boundary.
- **Trusting a length field from JavaScript.** Bounds checking protects the *module’s* memory; it does not stop your own glue from reading the wrong region. Always clamp any `(ptr, len)` you receive before building a view — never assume the caller is honest.

## Verification

Confirm the boundary holds with three checks straight from the Console.

```js
// 1. Cross-origin isolation is genuinely on
console.log(crossOriginIsolated, typeof SharedArrayBuffer);
// expect: true "function"   (false / "undefined" means your COOP/COEP failed)

// 2. An out-of-bounds load deterministically traps, not corrupts
try {
  instance.exports.peek(1 << 30);          // far past one page
} catch (e) {
  console.log(e instanceof WebAssembly.RuntimeError, e.message);
  // expect: true "memory access out of bounds"
}

// 3. The module imports only what you granted
const mod = await WebAssembly.compileStreaming(fetch("/out.opt.wasm"));
console.log(WebAssembly.Module.imports(mod));
// expect: exactly [{ module: "env", name: "log", kind: "function" }]
```

`wasm-objdump -x out.opt.wasm` from the CLI gives the same import list and confirms the memory section’s declared `maximum`, so you can gate CI on both.

## In this guide

- **[Is WebAssembly faster than JavaScript for DOM manipulation?](https://www.webassembly-wasm.com/webassembly-core-concepts-browser-runtime/browser-sandbox-security-boundaries/is-webassembly-faster-than-javascript-for-dom-manipulation/)** — why the sandbox boundary makes JS the faster choice for DOM work, with benchmarks.
- **[Security implications of Wasm in enterprise apps](https://www.webassembly-wasm.com/webassembly-core-concepts-browser-runtime/browser-sandbox-security-boundaries/security-implications-of-wasm-in-enterprise-apps/)** — threat modeling, `.wasm` supply chain, CSP, SRI, and sandboxing third-party modules.

## Frequently Asked Questions

Can a WebAssembly module access the DOM or network on its own?

No. A module has no ambient authority. It can only call functions you place in the `import object` at instantiation. If you do not import a function that touches `document` or `fetch`, the module has no way to reach them — the capability simply does not exist inside the sandbox.

What happens on an out-of-bounds memory access?

The engine raises a `trap`, surfaced in JavaScript as a `WebAssembly.RuntimeError` with the message “memory access out of bounds.” It never reads or writes host memory outside the module’s `linear memory` buffer, so a logic bug stays contained instead of becoming a memory-safety exploit.

Why do I need COOP and COEP headers?

They enable cross-origin isolation, which is the precondition for `SharedArrayBuffer`. Shared memory re-introduces the high-resolution timing signals Spectre attacks exploit, so the browser only allows it once your document has provably isolated itself from cross-origin content with these two headers.

Is 'wasm-unsafe-eval' dangerous like 'unsafe-eval'?

No. `'wasm-unsafe-eval'` permits only WebAssembly compilation and leaves JavaScript `eval()` and `new Function()` blocked. It is the minimal CSP relaxation needed to run Wasm under a strict policy and is strictly safer than `'unsafe-eval'`.

Does the sandbox protect me from a malicious third-party.wasm?

It protects the *host*: the module cannot escape memory or call ungranted capabilities. It does not protect *you* from a module that abuses the capabilities you did grant. Vet the supply chain, pin a hash, and scope imports — see the enterprise security guide above.

## Related

- [Stack vs heap execution model](https://www.webassembly-wasm.com/webassembly-core-concepts-browser-runtime/stack-vs-heap-execution-model/) — how `linear memory` and the protected value stack are addressed.
- [Wasm binary format deep dive](https://www.webassembly-wasm.com/webassembly-core-concepts-browser-runtime/wasm-binary-format-deep-dive/) — the structural validation that runs before any code executes.
- [SharedArrayBuffer, Atomics & threading](https://www.webassembly-wasm.com/js-wasm-interop-memory-management/sharedarraybuffer-atomics-threading/) — the threading model that cross-origin isolation unlocks.
- [Configuring COOP/COEP headers](https://www.webassembly-wasm.com/compilation-pipelines-toolchain-setup/local-development-server-configurations/configuring-coop-coep-headers-for-sharedarraybuffer/) — getting isolation working on your local server.