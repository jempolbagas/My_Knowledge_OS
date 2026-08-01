---
type: repo
title: Graphify
source_url: "https://github.com/Graphify-Labs/graphify"
author: "Graphify-Labs"
date_added: "2026-08-02"
status: done
notes_by: agent
tags:
  - knowledge-graph
  - code-analysis
  - tree-sitter
  - leiden-algorithm
  - ai-tools
promoted_to:
  - "[[Graphify]]"
---

## Why I'm reading this
Investigating **Graphify** (`Graphify-Labs/graphify`), an open-source, local-first engine that converts software codebases and technical documentation into structural knowledge graphs for AI coding assistants. Understanding its deterministic AST extraction, graph partitioning, and token-saving benefits over traditional vector RAG or text-based search.

## Key findings / notes

### 1. Architectural Paradigm: Deterministic AST Parsing vs. Vector RAG
Graphify replaces probabilistic text-embedding search (vector RAG) and naive file-by-file text searching (`grep`) with a local, deterministic AST-based pipeline. 
- **Tree-sitter Integration:** Graphify uses `tree-sitter` to parse code across 36+ programming languages (Python, TypeScript, Go, Rust, C/C++, Java, SQL, etc.). Parsing happens strictly on-device, incurring **zero LLM API calls** and maintaining complete code privacy.
- **Multimodal Support:** In addition to source code, Graphify ingests project documentation (Markdown, PDFs), schemas, images, and audio/video transcripts (transcribed locally), linking non-code context directly to code elements.
- **Deterministic vs. Inferred Edges:** Relationships in Graphify are strictly typed with explicit provenance tags:
  - `EXTRACTED`: Hard AST links verified directly from source code (e.g., function call sites, class inheritances, explicit imports).
  - `INFERRED`: Derived conceptual links assigned confidence scores based on co-occurrence or semantic heuristic analysis.

### 2. Knowledge Graph Construction & NetworkX Topology
Once files are parsed, Graphify builds a unified directed graph using `NetworkX`.
- **Node Taxonomy:** Represents discrete structural units including `File`, `Class`, `Function`, `Interface`, `Variable`, `DatabaseTable`, and `DocSection`.
- **Edge Taxonomy:** Maps precise structural interactions:
  - `CALLS`: Function/method execution targets.
  - `IMPORTS`: Cross-module dependencies.
  - `INHERITS_FROM`: Class/type hierarchy relationships.
  - `DEFINES`: Parent scope containment (e.g., File defining a Class or Function).
  - `REFERENCES`: Shared usage of data structures or global constants.
- **Auditability:** Every node and edge retains line-number spans and exact file paths, providing a transparent audit trail for AI reasoning.

### 3. Community Detection & God-Node Discovery (Leiden & Centrality)
Graphify goes beyond raw AST graphs by applying graph theory algorithms to discover macro-level architecture:
- **Leiden Algorithm:** Runs hierarchical community detection to partition the graph into tightly coupled semantic clusters. This groups related modules (e.g., authentication, database ORM, payment gateway) into high-level functional domains.
- **PageRank & Centrality Analysis:** Identifies **"God Nodes"**—heavily depended-upon structural bottlenecks, core utility hubs, or shared state managers. Identifying God Nodes prevents AI agents from making refactoring mistakes on critical system components.
- **Pathfinding Queries:** Enables structural reachability queries (e.g., tracing execution paths from an API route down to database mutations).

### 4. Output Artifacts (`graphify-out/`)
Running Graphify produces three main artifacts in the `graphify-out/` directory:
1. `graph.json`: The machine-readable, persistent knowledge graph consumed by AI coding agents across sessions without re-parsing files.
2. `graph.html`: An interactive, browser-based D3/3D visualization tool allowing human developers to explore codebase topology visually.
3. `GRAPH_REPORT.md`: An architectural summary report highlighting key functional communities, high-degree nodes, and critical dependency chains.

### 5. AI Assistant Integration & Skill Workflows
Graphify installs as a standardized skill across AI assistants including Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, and Aider.
- **Installation:** Package is distributed on PyPI as `graphifyy` (installed via `uv tool install graphifyy` or `pipx install graphifyy`).
- **Slash Commands & CLI:** Registered via `graphify install`. Executed via `/graphify .` or CLI commands (`graphify query "..."`, `graphify path A B`).
- **Token Efficiency:** Instead of loading thousands of code lines into the context window, AI assistants query `graph.json` or sub-graphs to read only the minimal necessary nodes and edges required to answer architectural queries.

### 6. Comparison: Graphify vs. Vector RAG vs. Lexical Grep

| Feature Axis | Lexical Grep | Vector RAG | Graphify |
| :--- | :--- | :--- | :--- |
| **Search Mechanism** | String exact/regex match | Vector embedding cosine similarity | Deterministic AST + Leiden Graph Traversal |
| **Contextual Scope** | Local text match only | Unstructured text chunks | Complete structural & dependency topology |
| **Precision & Auditability** | High precision, zero semantics | Variable (prone to hallucinations/false hits) | Exact AST links (`EXTRACTED`) + Auditable (`INFERRED`) |
| **Local Privacy** | 100% On-device | Often requires cloud embedding APIs | 100% On-device (Tree-sitter + NetworkX) |
| **AI Token Usage** | High (loads entire file contents) | Medium (loads chunk context) | Minimal (queries graph nodes/edges directly) |

## Quotes / snippets worth keeping
> "Graphify converts entire repositories into structured knowledge graphs, letting AI agents query exact AST relationships and community clusters rather than guessing via vector embeddings or grepping through text files." — *Graphify Overview*

## Concepts to extract
- [x] [[Graphify]]
