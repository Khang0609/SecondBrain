---
name: wiki-ingest
description: >-
  Ingest new sources (PDF, DOCX, PPTX, XLSX, images, local video, or YouTube URLs)
  into the Obsidian Wiki, extract knowledge in English, create cross-links, and
  update wiki/index.md and wiki/log.md.
---

# Wiki Ingest — Knowledge Ingestion Workflow

**Vault Root**: `E:\OneDrive\New_file\Obisidian\Second Brain` (use this root path even when invoked from another project).

When the user provides a file path in `raw/` (or elsewhere) or a YouTube URL, execute the following steps in order. All notes created or updated in `wiki/` **must be written in English**, even if the source in `raw/` is in Vietnamese or another language.

## 1. Preprocess the Source
- **GitHub Repository URL** (`github.com/<owner>/<repo>`):
  Delegate to the private sub-workflow at [references/github-repo.md](./references/github-repo.md) and follow it end-to-end (uses GitHub MCP to inspect `README.md`, repo structure, and manifests without cloning).
- **YouTube URL**:
  Run:
  ```powershell
  python "E:\OneDrive\New_file\Obisidian\Second Brain\.agents\skills\wiki-ingest\scripts\prepare_source.py" "<URL>"
  ```
  Read the generated `.srt` file in `raw/youtube/`. If the video has no subtitles or relies heavily on visuals, slides, or code on screen, re-run with `--download-video`:
  ```powershell
  python "E:\OneDrive\New_file\Obisidian\Second Brain\.agents\skills\wiki-ingest\scripts\prepare_source.py" "<URL>" --download-video
  ```
  Then inspect the downloaded `.mp4` directly.
- **`.docx`, `.pptx`, `.xlsx`**:
  Run:
  ```powershell
  python "E:\OneDrive\New_file\Obisidian\Second Brain\.agents\skills\wiki-ingest\scripts\prepare_source.py" "<file-path>"
  ```
  Read the extracted `.md` file in `raw/.extracted/`.
- **`.pdf`, images (`.png`, `.jpg`), local video (`.mp4`), audio, or `.md`**:
  Read and analyze directly using multimodal capabilities. For images and videos, describe key visual details (diagrams, architectures, slide figures).

## 2. Review Existing Knowledge
- Read `wiki/index.md` first to understand all existing `sources/`, `concepts/`, `entities/`, and `syntheses/`.

## 3. Update Wiki (Create & Cross-Link in English)
- **Source summary (`wiki/sources/<slug>.md`)**:
  Use a concise `kebab-case` slug **without** a date prefix (dates are tracked in `updated: YYYY-MM-DD` frontmatter). Include Dataview YAML frontmatter (`type: source`, `tags`, `sources`, `updated`), TL;DR, key arguments, evidence, and important timestamps (for videos).
- **Atomic notes (`wiki/concepts/` & `wiki/entities/`) & syntheses (`wiki/syntheses/`)**:
  Create or enrich related concept and entity pages using `[[Wikilinks]]` and bidirectional citations. If new material contradicts or updates an older claim, add a `## Contrasting Views / Updates` section citing both sources rather than silently overwriting.
- **Visuals & Diagrams**:
  - Embed important images/diagrams from `raw/media/` using `![[image-name.png]]` when helpful.
  - Use clean ` ```mermaid ` diagrams (Mermaid 12.1.0 / Pele in Obsidian 1.15+) for architectures, workflows, and relationships.

## 4. Update Index & Log
- **`wiki/index.md`**: Add or update entries under the appropriate category (`Sources`, `Concepts`, `Entities`, `Syntheses`) with `[[link]]` + 1-line description + updated date (`YYYY-MM-DD`).
- **`wiki/log.md`**: **Append** a new entry at the **bottom** of the file in this exact CLI-filterable format:
  ```markdown
  ## [YYYY-MM-DD] ingest | <Short Title>
  ```
  (Include concise bullet details underneath if helpful.)

## 5. Verify Touched Files & Report Concisely
- Verify **only the files created or updated in this ingest** (valid `type`/`tags`/`sources`/`updated` frontmatter, valid `[[wikilinks]]`, and `wiki/index.md` + `wiki/log.md` updated). Do **not** scan unrelated existing notes in `wiki/`; use `/wiki-lint` for full-vault audits.
- Summarize to the user: which source was read, which files in `wiki/` were created or updated, and any notable connections or contradictions discovered with existing knowledge.
