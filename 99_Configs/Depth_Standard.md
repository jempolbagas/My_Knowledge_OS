# Depth Standard for Agent-Generated Content

**Applies to:** Generated Readings (always) and Library Source Notes where `notes_by: agent`.
**Does not apply to:** Concept Notes. Concepts stay atomic and short by design — that's what keeps Study Partner mode's "Concepts first" query cheap. Don't let this bar bleed into Concept notes.

## The bar
A "reading" is a real, self-contained treatment of the topic — something that could replace reading the source itself for someone who just needs to understand it, not a summary of a summary. If you could have written the note without actually reading the source in depth, it's too short.

**Reference example:** `20_Brain_Atlas/10_Library/Generated_Readings/Artificial_Intelligence/LLMWiki_Deep_Dive.md`. It has multiple `###` subsections (context, mechanism, a comparison table, trade-offs, why it matters to this vault specifically), explains mechanisms rather than labels ("GFs turn recurrences into algebra because shifting the index corresponds to multiplying by x," not "GFs convert recurrences to algebra"), and uses a table wherever the source has more than one axis to compare (see its Dynamic RAG vs. Compiled Knowledge table for the target shape).

**Common failure to avoid:** a "Key findings / notes" section that's 3–5 short bullets restating the source's headline claims. That's an abstract, not a reading. Same for a one-sentence "Why it matters" paragraph, or treating the template's headers as a form to fill in minimally rather than a skeleton to build a real document under.

## Per note type
- **Generated Reading** — `## The reading` should look like the reference example: numbered or thematic `###` subsections covering the topic from multiple angles. This is the default depth for every Generated Reading, not a special case.
- **Library Source Note (agent-authored)** — `## Key findings / notes` carries the same depth requirement. Walk through the source's actual structure/argument/methodology in your own words with real subsections, not 3 extracted takeaways. `## Why I'm reading this` and `## Quotes / snippets worth keeping` stay short as before.
- **Library Source Note (human-authored)** — unchanged, the user writes what they write.

## What doesn't change
- Copyright discipline still applies: depth comes from explaining the source's ideas in your own words at length, not from quoting more of it. `## Quotes / snippets worth keeping` stays a small, clearly-attributed set.
- The opening paragraph must still work as a standalone summary — `build_index.py`'s `extract_summary()` pulls the first paragraph for `vault_summary.json`. Lead with a real, informative paragraph, then go deep below it.
- Concept notes promoted from these readings stay atomic and short, unchanged in format or length.
