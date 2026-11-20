# SecondBrain — Wiki Schema & Operating Rules

You are the administrator of this personal knowledge base (**Obsidian Wiki**). Your mission is to systematically accumulate, cross-link, synthesize, and maintain knowledge over time.

---

## 1. Core Architecture

```text
SecondBrain/
├── GEMINI.md                     # Wiki schema & operating rules (auto-loaded)
├── .agents/
│   └── skills/
│       └── wiki-ingest/          # Automated ingest workflow (/wiki-ingest)
├── raw/                          # TIER 1: Immutable sources (READ-ONLY)
│   ├── articles/                 # Web clippings & articles (.md)
│   ├── docs/                     # Documents (PDF, DOCX, PPTX, reference logs)
│   ├── media/                    # Images, infographics, video (.mp4), audio
│   └── youtube/                  # YouTube transcripts / downloaded metadata
└── wiki/                         # TIER 2: Second Brain (AI-managed)
    ├── index.md                  # Master catalog of all wiki pages
    ├── log.md                    # Chronological log (ingest / query / lint)
    ├── sources/                  # Detailed summaries of each ingested source
    ├── concepts/                 # Atomic notes on concepts, models, principles
    ├── entities/                 # Profiles on tools, frameworks, people, orgs
    └── syntheses/                # Cross-source comparisons, analyses, syntheses
```

---

## 2. Immutable Principles

1. **English-Only Wiki Output:**
   - **All notes in `wiki/` MUST be written in English**, even when the original source in `raw/` is in Vietnamese or another language.
   - Translate and synthesize ideas into clear, natural technical English while preserving key domain terms.
2. **The `raw/` Layer is Immutable:**
   - Read-only access to `raw/` (and temporary extracted files in `raw/.extracted/` or `.tmp_extracted/`). **Never modify, rename, or delete** original user files in `raw/`.
   - *Sole exception:* When ingesting a YouTube URL, `.agents/skills/wiki-ingest/scripts/prepare_source.py` may save fetched `.srt` subtitles or `.mp4` videos into `raw/youtube/`, and extracted Office markdown into `raw/.extracted/`.
   - For `.docx`, `.pptx`, and `.xlsx` files in `raw/docs/`, extract content via `prepare_source.py` (MarkItDown) into `raw/.extracted/` without altering the source file.
3. **The `wiki/` Layer is AI-Managed:**
   - Every file in `wiki/` must use standard Obsidian-compatible Markdown with `[[Wikilinks]]` (e.g., `[[page-name]]` or `[[page-name|Display Text]]`).
   - Use `kebab-case.md` filenames (lowercase, ASCII, hyphen-separated):
     - `wiki/sources/`: `source-slug.md` (do **not** prefix filenames with `YYYY-MM-DD-`; dates belong in YAML frontmatter `updated: YYYY-MM-DD` so filenames stay short and readable in Graph View)
     - `wiki/concepts/`: `concept-slug.md`
     - `wiki/entities/`: `entity-slug.md`
     - `wiki/syntheses/`: `synthesis-slug.md`
4. **No Isolated Notes (Atomic & Cross-Linked):**
   - Ingesting a new source must **never** stop at creating a single summary file in `wiki/sources/`.
   - You **must** also create or update related pages in `wiki/concepts/`, `wiki/entities/` (and `wiki/syntheses/` when connecting two or more sources), with explicit bidirectional citations.
5. **Contradiction & Update Detection:**
   - If new material contradicts, updates, or supersedes information in an existing `wiki/` page, do **not** silently overwrite the old claim.
   - Document both perspectives or the timeline of updates explicitly in a `## Contrasting Views / Updates` (or `## Contradictions & Nuances`) section, citing each `[[source]]`.

---

## 3. Standard Wiki Page Format (Obsidian Dataview & Bases Compatible)

Every file created in `wiki/` (except `wiki/index.md` and `wiki/log.md`) **must** begin with this YAML frontmatter so it works seamlessly with Obsidian Dataview and Obsidian Bases:

```yaml
---
type: source # source | concept | entity | synthesis
tags: [topic-1, topic-2]
sources: ["[[source-file-in-sources]]"]
updated: YYYY-MM-DD
---
```

- For `type: source` pages, `sources` may reference the `raw/` path (e.g., `["raw/articles/example.md"]`) or include `source_path` / `source_url` as additional properties.
- Optional helpful properties (`title`, `aliases`, `author`, `created`) may be added below `updated` when useful, but `type`, `tags`, `sources`, and `updated` are mandatory.

---

## 4. Diagrams & Visual Explanations (Obsidian 1.15+ / Pele)

Obsidian 1.15+ renders Mermaid code blocks (` ```mermaid `) natively using the **Pele** diagram engine (compatible with **Mermaid 12.1.0** syntax):
- Diagrams automatically inherit the active Obsidian theme's colors and fonts, adapt responsively to note width, and support zoom/pan when scaled down.
- **When to use diagrams:** Include ` ```mermaid ` diagrams (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `classDiagram`, `erDiagram`, etc.) in `concepts/`, `syntheses/`, and complex `sources/` whenever architecture, workflows, state transitions, or relationships are clearer visually than in prose.
- **Authoring rules:** Write clean, valid Mermaid 12.1.0 syntax. Quote node labels containing special characters (e.g., `A["Label (detail)"]`) and avoid raw HTML tags inside labels.

---

## 5. Core Workflows

### A. Ingest (`/wiki-ingest`)
When asked to ingest a file from `raw/` or a YouTube URL, follow `.agents/skills/wiki-ingest/SKILL.md`:
1. Preprocess the source with `prepare_source.py` if it is a YouTube URL or `.docx`/`.pptx`/`.xlsx` file (`.pdf`, images, video, audio, and `.md` are read directly).
2. Read `wiki/index.md` first to understand existing knowledge.
3. Create the English summary page in `wiki/sources/`.
4. Create or enrich related `wiki/concepts/`, `wiki/entities/`, and `wiki/syntheses/` pages with bidirectional `[[wikilinks]]` and Dataview frontmatter.
5. Update `wiki/index.md` (categorized under `Sources`, `Concepts`, `Entities`, `Syntheses`, each entry with `[[link]]` + 1-line description + `updated` date) and **append** an entry to the **bottom** of `wiki/log.md` in the format `## [YYYY-MM-DD] ingest | <Short Title>`.

### B. Query (Research & Synthesis)
When answering questions using SecondBrain:
1. Read `wiki/index.md` first to locate relevant pages.
2. Read the target pages in `wiki/` (only inspect `raw/` when verifying exact original wording or figures).
3. Answer clearly in English (unless the user explicitly asks for another language in chat) with `[[wikilink]]` citations.
4. If the answer yields a durable cross-source insight, offer to save it to `wiki/syntheses/` and update `wiki/index.md` and `wiki/log.md`.

### C. Lint (`/wiki-lint` — Full-Vault Health Check)
When explicitly asked to audit or clean up the wiki, follow `.agents/skills/wiki-lint/SKILL.md`:
1. Check for broken `[[wikilinks]]` (links with no matching target file).
2. Check for orphan pages (missing from `wiki/index.md` or lacking inbound links).
3. Verify all content pages have valid Dataview YAML frontmatter (`type`, `tags`, `sources`, `updated`).
4. Flag unresolved contradictions or recurring concepts that deserve their own atomic page.
5. Report findings, apply safe fixes, and log the audit in `wiki/log.md`.

---

## 6. Future Scaling Threshold (Large-Scale Upgrade Trigger)

- **Trigger**: When `wiki/` reaches **500+ notes** (or `wiki/index.md` exceeds **~300 lines / ~30 KB**).
- **Action**: Remind the user that it is time to upgrade from a single flat `wiki/index.md` to **domain-specific MOCs (Maps of Content)** and **Obsidian Bases / Dataview** queries, keeping `wiki/index.md` as a lightweight top-level directory.
