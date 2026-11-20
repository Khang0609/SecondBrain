# SecondBrain — AI Agent + Obsidian Knowledge Base

A two-tier **LLM-managed Personal Knowledge Base (Obsidian Wiki)** built with **Antigravity CLI + Obsidian 1.15+**. Drop raw articles, PDFs, Office docs, YouTube links, or GitHub repos in—your AI agent extracts, translates, cross-links, diagrams, and maintains structured English notes automatically.

---

## Architecture

```text
SecondBrain/
├── README.md                     # This guide + one-shot setup prompt
├── GEMINI.md                     # Wiki schema & operating rules (auto-loaded per session)
├── .gitignore                    # Ignores Obsidian workspace state, .extracted/, & large videos
├── .obsidian/
│   └── graph.json                # Pre-colored Graph View groups + hub filter (-file:index -file:log)
├── .agents/
│   └── skills/
│       ├── wiki-ingest/
│       │   ├── SKILL.md          # /wiki-ingest workflow (articles, PDFs, YouTube, Office, GitHub)
│       │   ├── references/
│       │   │   └── github-repo.md  # Private sub-workflow for GitHub repo ingestion
│       │   └── scripts/
│       │       └── prepare_source.py  # Preprocesses YouTube (.srt/.mp4) & Office (.docx/.pptx/.xlsx)
│       └── wiki-lint/
│           └── SKILL.md          # /wiki-lint on-demand full-vault health audit
├── raw/                          # TIER 1: Immutable sources (AI READ-ONLY)
│   ├── articles/                 # Web clippings & markdown articles
│   ├── docs/                     # PDFs, DOCX, PPTX, XLSX
│   ├── media/                    # Images, diagrams, video, audio
│   └── youtube/                  # Downloaded YouTube subtitles (.srt/.vtt) or 480p .mp4
└── wiki/                         # TIER 2: AI-managed knowledge base (English-only)
    ├── index.md                  # Master catalog (Sources, Concepts, Entities, Syntheses)
    ├── log.md                    # Append-only chronological log (ingest / query / lint)
    ├── sources/                  # Detailed source summaries
    ├── concepts/                 # Atomic concept notes
    ├── entities/                 # Tool, framework, repo, and people profiles
    └── syntheses/                # Cross-source comparisons & syntheses
```

### Key Design Principles
- **Immutable `raw/` vs. AI-Managed `wiki/`**: Original files in `raw/` are never modified or deleted.
- **English-Only `wiki/`**: Notes in `wiki/` are synthesized in clean technical English even when `raw/` sources are in Vietnamese or other languages.
- **Dateless `kebab-case.md` Filenames**: Keeps Obsidian Graph View readable; dates live in YAML frontmatter (`updated: YYYY-MM-DD`).
- **Dataview & Obsidian Bases Ready**: Every content note starts with `type`, `tags`, `sources`, and `updated` in YAML frontmatter.
- **Obsidian 1.15+ Native Diagrams (Pele / Mermaid 12.1.0)**: Clean `mermaid` diagrams render natively with theme colors, responsive sizing, and zoom/pan.
- **Pre-Configured Graph View (`.obsidian/graph.json`)**:
  - **Blue**: `wiki/sources` | **Green**: `wiki/concepts` | **Amber**: `wiki/entities` | **Purple**: `wiki/syntheses` | **Slate**: `raw/`
  - Default filter `-file:index -file:log` hides the two catalog hubs so topic clusters separate cleanly.

---

## Prerequisites

- **Obsidian** (1.15+ recommended for native Pele Mermaid rendering & Bases)
- **An AI Coding Agent** with workspace rules/skills support (built on **Antigravity CLI**, `agy`)
- **Python 3.10+** with:
  ```bash
  pip install yt-dlp markitdown
  ```
- *(Optional)* **GitHub MCP** configured in your agent if you want `/wiki-ingest https://github.com/<owner>/<repo>` to inspect repos directly via API.

---

## Quick Setup (Manual)

1. **Clone the repository** and open the folder as an **Obsidian Vault**:
   ```bash
   git clone https://github.com/Khang0609/SecondBrain.git
   ```
   *(If you want a fresh empty vault, clear `raw/` and `wiki/` content pages while keeping `GEMINI.md`, `.agents/`, `.obsidian/graph.json`, `wiki/index.md`, and `wiki/log.md`.)*

2. **Install Python preprocessing dependencies**:
   ```bash
   pip install yt-dlp markitdown
   ```

3. **Enable Global Skills (Optional — Use From Any Project)**:
   - **`~/.gemini/config/skills/wiki-ingest/SKILL.md`**: Point to `<VAULT_PATH>/.agents/skills/wiki-ingest/SKILL.md` so `/wiki-ingest` works from any repo.
   - **`~/.gemini/config/skills/wiki-query/SKILL.md`**: Point to `<VAULT_PATH>/wiki/index.md` so `/wiki-query <topic>` acts like a local Context7 for your personal notes.

4. **Enable One-Shot Terminal Command (`brain ingest`, Windows)**:
   Create `~/.local/bin/brain.cmd` (ensure `~/.local/bin` is on your `PATH`):
   ```bat
   @echo off
   setlocal
   set "VAULT=PATH\TO\YOUR\SecondBrain"

   if /I "%~1"=="ingest" (
       if "%~2"=="" (
           echo Usage: brain ingest ^<YouTube-URL-or-file^> [--download-video]
           exit /b 1
       )
       pushd "%VAULT%"
       if "%~3"=="" (
           agy -p "/wiki-ingest %~2" --mode auto
       ) else (
           agy -p "/wiki-ingest %~2 %~3" --mode auto
       )
       set "EXIT_CODE=%ERRORLEVEL%"
       popd
       exit /b %EXIT_CODE%
   )

   echo Usage: brain ingest ^<YouTube-URL-or-file^> [--download-video]
   exit /b 1
   ```

---

## One-Shot Setup Prompt (For Any Frontier AI Agent)

Want an AI agent to set this entire environment up for you automatically after cloning? Paste this prompt into **Antigravity CLI** (or another coding agent) inside your cloned folder:

```text
Set up this SecondBrain Obsidian + Agent Wiki environment for me on my machine:
1. Read GEMINI.md and .agents/skills/wiki-ingest/SKILL.md to understand the vault structure and VAULT_ROOT (use the current repository path as VAULT_ROOT).
2. Install `yt-dlp` and `markitdown` in Python, and verify `.agents/skills/wiki-ingest/scripts/prepare_source.py --help` runs cleanly.
3. Update VAULT_ROOT paths in `.agents/skills/wiki-ingest/SKILL.md` to match my local repository path.
4. Set up global skills in `~/.gemini/config/skills/`:
   - `wiki-ingest/SKILL.md` pointing to `<VAULT_ROOT>/.agents/skills/wiki-ingest/SKILL.md`
   - `wiki-query/SKILL.md` that reads `<VAULT_ROOT>/wiki/index.md` first, loads only relevant notes, and answers with `[[wikilink]]` citations (a local Context7).
5. Create a `brain` CLI wrapper in `~/.local/bin/` (`brain.cmd` on Windows or `brain` on macOS/Linux) so `brain ingest "<URL-or-file>" [--download-video]` runs `agy -p "/wiki-ingest <target>" --mode auto` inside `<VAULT_ROOT>` and exits.
6. Verify `.obsidian/graph.json` has color groups for `wiki/sources`, `wiki/concepts`, `wiki/entities`, `wiki/syntheses`, `raw`, and `-file:index -file:log` filter, then report back.
```

---

## Daily Usage

| Command | Where | What It Does |
| :--- | :--- | :--- |
| `/wiki-ingest <file-or-URL>` | Any project in `agy` | Ingests PDFs, DOCX/PPTX/XLSX, images, YouTube URLs, or GitHub repos into `wiki/` |
| `/wiki-query <topic>` | Any project in `agy` | Searches `wiki/index.md` first, reads only matching notes, and answers with `[[wikilinks]]` |
| `/wiki-lint` | Inside `SecondBrain` | Full-vault audit for broken links, orphans, missing frontmatter, and contradictions |
| `brain ingest "<URL-or-file>"` | Any terminal | Runs `/wiki-ingest` non-interactively in one shot and exits |
