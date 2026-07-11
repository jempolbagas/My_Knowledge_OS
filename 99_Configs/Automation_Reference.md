# Automation Reference

Background framework in `.automation/` (hidden from Obsidian), run persistently via the `knowledge-os-watcher.service` systemd user service.

## Components

| Script | Role | Output |
|---|---|---|
| `build_index.py` | Walks `10_Spaces/`, `20_Brain_Atlas/`, `00_Inbox/`; rebuilds the SQLite relational map (nodes + edges) from scratch every run | `.automation/db/vault_index.db` |
| `linter.py` | Flags broken wikilinks, orphan pages, and missing/invalid frontmatter from the index | `.automation/reports/linter_report.{json,md}` |
| `staleness_checker.py` | Compares each Concept's stored `source_hash` against a fresh MD5 of its linked Markdown/text source (skips `.pdf` targets) | `.automation/reports/stale_concepts.{json,md}` |
| `generate_summary.py` | Builds the token-efficient digest read at the start of every agent session | `.automation/reports/vault_summary.json` |
| `watcher.sh` | Runs the four scripts above on startup, then again on every vault change after a 5-second quiet period (via `inotifywait`, excluding `.automation/.obsidian/.git/.trash`) | — |
| `git_sync.sh` | Commits and pushes the vault as a backup (`vault backup: <timestamp>`). Not agent-triggered — runs on its own schedule, separate from the watcher loop. | — |

## Trigger model
- **Deterministic** (indexer, linter, staleness checker, summary generator): file-watcher triggered via `inotifywait` + 5s debounce. No agent involvement, no judgment calls.
- **Semantic** (contradiction/gap review, merge suggestions, promotion calls): agent-scheduled, not file-triggered. This is deliberate — these need judgment, not a cron job.

## MD5 snapshot protocol
When generating or updating a Concept note from a Markdown/text library source:
1. Compute the MD5 hash of the source file.
2. Store it in the Concept's frontmatter as `source_hash: "<hash>"`.
3. This resets the staleness flag for that pair. Never set `source_hash` if the source is a `.pdf` — staleness checking is deferred for PDFs until direct PDF access is revisited.

## Known gaps (flag if asked to review/extend automation)
- `vault_summary.json`'s `health_score` is computed across the **whole vault**, including `10_Spaces/` — which was never meant to carry `type:` frontmatter or dense interlinking. A low score currently reflects normal coursework, not a real Atlas problem. Treat it as noise until it's rescoped to `20_Brain_Atlas/` only (or split into separate Atlas/Spaces scores).
- The linter's orphan check doesn't distinguish zones: an isolated homework file in `10_Spaces/` is expected and not a defect, but an isolated Concept or Reference note in `20_Brain_Atlas/` is. Don't "fix" orphan status on `10_Spaces/` files just because the linter flagged them.
- The wikilink parser in `build_index.py` resolves anchors (`[[Note#Heading]]`) as part of the link target rather than splitting them — this can produce false "broken link" entries for same-note or cross-note heading references. Cross-check against the actual note before treating a linter-flagged anchor link as genuinely broken.
