---
type: repo
title: Quartz
source_url: "https://github.com/jackyzha0/quartz"
author: "Jacky Zhao (jackyzha0)"
date_added: "2026-08-08"
status: done
notes_by: agent
tags:
  - obsidian
  - static-site-generator
  - typescript
  - digital-garden
  - web-development
promoted_to:
  - "[[Quartz]]"
---

## Why I'm reading this
Investigating **Quartz** (`jackyzha0/quartz`), an open-source static site generator framework written in TypeScript that converts Obsidian vaults and Markdown personal knowledge bases into fast, accessible web pages and digital gardens.

## Key findings / notes

### 1. Architectural Overview & Shift to TypeScript (v4)
Quartz v4 is a complete ground-up rewrite of Quartz in TypeScript. Unlike v3 (Hugo-based), v4 provides a modular plugin-based architecture executing directly via Node.js/npx.
- **Parsing Engine:** Transforms Obsidian-flavored Markdown (Wikilinks, block transclusions, callouts, latex math, popover previews) into static HTML/JS pages.
- **Battery-Included Features:** Built-in full-text search, interactive knowledge graph visualizer (D3 canvas), backlink explorer, breadcrumb navigation, and dark/light theme toggle.
- **Extensibility:** Custom components, transformers, filters, and emitters allow fine-grained customization without patching core files.

### 2. Project Layout & Directory Structure
Quartz enforces a clear separation between personal configurations, note contents, and core framework code:
- `quartz/`: Core engine source code (should not be modified directly to allow smooth upstream git updates).
- `quartz-custom/`: User-space for custom TypeScript components, SCSS styles, and plugin extensions.
- `quartz.config.ts`: Central configuration file managing global site metadata, themes, typography, and active plugin pipelines.
- `quartz.layout.ts`: Defines page composition across slots (`beforeBody`, `left`, `right`, `footer`).
- `content/`: Working directory or symlink pointing to the target Obsidian vault Markdown files.

### 3. Pipeline Processing: Transformers, Filters, Emitters
Quartz processes content using a 3-stage plugin architecture:
1. **Transformers:** Parse and mutate raw AST nodes (e.g., `ObsidianFlavoredMarkdown`, `Latex`, `SyntaxHighlighting`, `CrawlLinks`).
2. **Filters:** Selectively allow or exclude pages from build output (e.g., `ExplicitPublish` to publish notes with `publish: true` frontmatter tag).
3. **Emitters:** Output static assets and HTML routes (e.g., `ContentPage`, `FolderPage`, `TagPage`, `Assets`, `ComponentResources`).

### 4. Hosting & Continuous Deployment Workflow
- **Git Integration:** Typically combined with `Obsidian Git` plugin to commit vault updates to GitHub.
- **Continuous Integration:** GitHub Actions, Cloudflare Pages, Vercel, or Netlify automatically run `npx quartz build` on push and deploy static HTML output to edge CDN networks.

## Quotes / snippets worth keeping
> "Quartz is a set of tools that helps you publish your digital garden and notes as a website for free." — *Quartz Documentation*

## Concepts to extract
- [x] [[Quartz]]
