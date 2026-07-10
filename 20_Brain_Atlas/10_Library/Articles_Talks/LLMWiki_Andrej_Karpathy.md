---
type: article
title: LLMWiki - Karpathy's Compiled Knowledge Base Pattern
source_url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
author: "Andrej Karpathy"
date_added: "2026-07-10"
status: done
notes_by: agent
tags: [pkm, llm-agents, rag, knowledge-os]
promoted_to: ["[[LLMWiki]]"]
---

## Why I'm reading this
This note documents the "LLMWiki" design pattern proposed by Andrej Karpathy in April 2026. This pattern outlines a paradigm shift in how we manage personal knowledge using LLMs, moving from dynamic RAG queries to compiled, persistent knowledge bases. 

Interestingly, the system hosting this note (`10_Knowledge_OS`) is a direct, operational implementation of the LLMWiki pattern.

## Key findings / notes
* **RAG vs. Compiled Knowledge**: Conventional RAG systems retrieve raw, unstructured chunks on-the-fly and synthesize them for every query. LLMWiki advocates for a "pre-compiled" approach where an LLM agent processes incoming sources immediately, updating a structured, interlinked wiki.
* **Knowledge Compounding**: By committing distilled knowledge to interlinked markdown files, information is not lost or trapped in chat histories. It continuously updates existing pages, strengthens cross-references, and flags logical contradictions.
* **The "Librarian" Agent**: The human acts as a curator (providing sources and direction), while the AI agent functions as a librarian, handling routine filing, metadata updates, and formatting rules.
* **Hybrid Automation**: To maintain integrity as the wiki scales, deterministic code (linters, SQLite indexes, staleness trackers) runs in the background. This ensures the system remains accurate and prevents the LLM from executing costly full-vault scans.

## Quotes / snippets worth keeping
> "Instead of dynamic RAG where the LLM has to re-derive insights from raw materials for every query, use the LLM to proactively compile and maintain a structured, interlinked markdown wiki where knowledge compounds over time."
> *(Paraphrased concept from Karpathy's Gist and community discussions)*

## Concepts to extract
- [x] [[LLMWiki]]
