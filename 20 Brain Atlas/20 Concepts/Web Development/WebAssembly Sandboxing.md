---
type: concept
title: WebAssembly Sandboxing
subject: Web Development
date_created: 2026-07-28
tags:
  - webassembly
  - security
  - sandboxing
source:
source_hash:
---

## The idea (one clear statement)
WebAssembly sandboxing enforces absolute isolation with zero ambient authority by confining module memory access to a single bounds-checked buffer (`linear memory`) and restricting host interactions strictly to explicitly granted capabilities.

## Why it matters / how it connects
Unlike traditional OS process isolation that depends on kernel rings and hardware MMUs, Wasm uses Software Fault Isolation (SFI) and Control-Flow Integrity (CFI) to run untrusted bytecode safely across browsers, cloud microservices, and edge nodes. It eliminates classic native exploits like buffer overflows escaping to host memory or ROP/JOP attacks, while shifting security responsibility to capability validation at the host boundary.

## Related concepts
- [[WebAssembly vs Docker]]
