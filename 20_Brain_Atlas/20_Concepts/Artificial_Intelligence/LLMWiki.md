---
type: concept
title: LLMWiki
subject: "Artificial_Intelligence"
date_created: "2026-07-10"
tags: [pkm, dynamic-rag, knowledge-compounding]
source: "[[LLMWiki_Deep_Dive]]"
source_hash: "99450493c3529af5792554572de54c07"
---

## The idea (one clear statement)
Instead of retrieving raw snippets on-the-fly to answer user queries (traditional Retrieval-Augmented Generation or RAG), the **LLMWiki** design pattern utilizes an LLM agent to incrementally compile, structure, and maintain a persistent, interlinked collection of Markdown notes where personal knowledge can compound over time.

## Why it matters / how it connects
* **Knowledge Compounding**: Traditional RAG systems suffer from lack of continuity; every query re-analyzes raw materials from scratch. In an LLMWiki, the LLM integrates new information immediately into existing entity or concept pages, resolving conflicts and forming relationships.
* **Token Efficiency**: Because the knowledge is already pre-distilled, structured, and cross-referenced, future reasoning or queries only need to pull 1–3 highly refined, relevant concept notes rather than reading large files or speculative scans.
* **Human-in-the-Loop Curator**: The human controls the input (adding raw articles, video transcripts, or papers to an inbox) and reviews generated notes, while the agent handles structural tasks like updating wikilinks, generating backlinks, and maintaining metadata.
* **Operational Reality**: This exact PKM repository (`10_Knowledge_OS`) implements this pattern, using local scripts (linters, staleness checking, database indexing) alongside LLM interactions to maintain structure.

## Related concepts
- [[Dynamic RAG]]
- [[Knowledge Graphs]]
