---
type: generated_reading
title: LLMWiki Deep Dive
topic: "LLMWiki (Compiled Personal Knowledge Bases)"
requested_on: "2026-07-10"
prompt: "Find out about a repository/project/concept/framework called LLMWiki that are popularized by Andrej Karpathy"
status: done
tags: [pkm, llm-agents, rag, knowledge-compounding]
promoted_to: ["[[LLMWiki]]"]
---

## The reading

### 1. Introduction: The Compiling of Knowledge
The term **LLMWiki** refers to a design pattern for personal knowledge management (PKM) popularized by AI researcher Andrej Karpathy in early 2026. At its core, the pattern suggests treating personal knowledge bases (like an Obsidian vault or a directory of Markdown files) not as passive document stores, but as **compiled databases** that are actively maintained, refactored, and interlinked by an AI agent acting as a persistent "Librarian."

Rather than querying raw source files at search time, the LLM proactively synthesizes incoming materials upon ingestion, writing the resulting insights directly into clean, structured, and modular concept notes.

---

### 2. Paradigm Shift: Dynamic RAG vs. Compiled Knowledge (LLMWiki)

Traditional Retrieval-Augmented Generation (RAG) relies on dynamic chunks. When a user asks a question, a vector database returns the top-K chunks of raw, unformatted text, and the LLM must synthesize an answer from scratch. 

| Feature | Traditional Dynamic RAG | Compiled Knowledge (LLMWiki) |
| :--- | :--- | :--- |
| **Ingestion** | Simple chunking and vector indexing of raw files. | Synthesis, editing, and integration into target notes. |
| **Query Latency** | High (must retrieve, read, and summarize raw chunks). | Low (reads pre-synthesized, atomic concept notes). |
| **Token Cost** | High per query (repetitive processing of raw texts). | Low per query (highly condensed and structured notes). |
| **Knowledge Growth** | Flat (no historical memory of concepts or linkages). | Compounding (new entries update and link to existing ones). |
| **Data Integrity** | Prone to noise, duplication, and stale retrieval. | Maintained via automated linters and merge checks. |

---

### 3. Core Architectural Pillars
A typical LLMWiki implementation consists of four major components:

1. **The Raw Inbox:** A folder where the user drops raw materials (e.g., article bookmarks, YouTube transcripts, PDFs, or raw thoughts).
2. **The Markdown Wiki:** A structured folder containing two main note types:
   * **Library Source Notes:** Documentation of external resources (repos, articles, papers) with metadata and key takeaways.
   * **Concept Notes:** Atomic, timeless, and reusable ideas (one clear idea per note).
3. **The Agent Librarian:** An LLM agent (configured with a system ruleset like `CLAUDE.md` or `GEMINI.md`) that has permission to write, edit, rename, and link files.
4. **Deterministic Validation (The Compiler/Linter):** Background scripts that maintain index health. Because LLMs are prone to hallucinating links or creating duplicate pages, a deterministic validator (e.g., Python scripts running via file watchers) builds database indexes, checks for broken links, and tracks content staleness.

---

### 4. How Knowledge Compounds
In a traditional notes folder, notes remain isolated unless a human manually links them. In an LLMWiki, the Agent Librarian performs continuous maintenance:
* **Entity Resolution:** When a new article mentions a concept, the agent finds the existing Concept Note and appends the new context or references.
* **Semantic Merging:** If two raw notes describe the same underlying idea under different names, the agent identifies the overlap and merges them into a single atomic Concept Note.
* **Backlink Cultivation:** The agent ensures that if a Concept links to a Source, the Source links back to the Concept, keeping Obsidian's graph view and backlinks pane highly accurate and navigable.

---

### 5. Challenges & Design Trade-offs
While highly efficient for queries, the LLMWiki pattern has specific trade-offs:
* **High Ingestion Cost:** Processing every new file through an LLM to update a wiki requires write operations, edits, and re-indexing, which is computationally more expensive during ingestion than simple vector database inserts.
* **Agent Drift & Contradictions:** As the wiki grows, the agent may introduce contradictory info or write style drift. This requires strict template rules and linting checks.
* **The "Librarian's Paradox":** If the LLM reorganizes files too aggressively, the human owner may feel disconnected from their own knowledge base. Clear division of active roles (e.g., spaces for college/teaching vs. timeless brain atlas concepts) is necessary.

---

## Concepts to extract
- [x] [[LLMWiki]]
