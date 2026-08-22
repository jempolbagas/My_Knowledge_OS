---
type: concept
title: WebAssembly vs Docker
subject: Web Development
date_created: 2026-07-28
tags:
  - webassembly
  - docker
  - containers
source:
source_hash:
---

## The idea (one clear statement)
WebAssembly and Docker containers operate at different layers of the infrastructure stack: Wasm provides ultra-fast, cross-platform in-process bytecode execution, while Docker provides container image packaging, orchestration, and OS virtualization that can host Wasm runtimes via containerd shims.

## Why it matters / how it connects
Rather than replacing Docker, Wasm complements containers by enabling sub-millisecond cold starts, multi-architecture hardware portability without multi-arch builds, and megabyte-scale OCI images for serverless and edge computing. Using custom containerd shims, Docker Engine can run Wasm modules side-by-side with standard Linux containers under a single unified developer workflow.

## Related concepts
- [[WebAssembly Sandboxing]]
