---
type: concept
subject: Computer_Science
source: "[[Model Context Protocol Architecture]]"
source_hash: "7f4c9a8b1d2e3f5a6b7c8d9e0f1a2b3c"
date_created: 2026-08-02
status: atomic
tags:
  - mcp
  - concept
---

# Model Context Protocol

The **Model Context Protocol (MCP)** is an open standard designed to decouple AI host applications from external tool implementations. It establishes a standardized client-server architecture using [[JSON-RPC 2.0]] over **stdio** or **SSE** transports, enabling AI models to safely access tools, read resources, and execute prompt workflows without bespoke integration code.
