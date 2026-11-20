# Private Sub-Workflow: GitHub Repository Ingest

This reference is **private to `/wiki-ingest`** and is loaded only when the input URL matches `https://github.com/<owner>/<repo>` (or a subpath inside a GitHub repository).

## 1. Inspect the Repository (Read-Only)
Use the **`github`** MCP server tools (read their JSON schema in `C:\Users\PC\.gemini\antigravity-cli\mcp\github\` if needed before calling):
1. **Repo Overview & README**:
   - Call `get_file_contents` (`owner`, `repo`, `path: "README.md"`) and `path: ""` (root directory listing) to see project structure.
   - Optionally call `search_repositories` (`query: "repo:<owner>/<repo>"`) for stars, license, language, and description, or `get_latest_release` for the current version.
2. **Key Config / Entrypoints**:
   - Read 1–3 key manifest or entrypoint files (`pyproject.toml`, `package.json`, `Cargo.toml`, `Dockerfile`, or main source file) to verify real dependencies, hardware requirements, and CLI/API usage.
   - *(Fallback: If the `github` MCP server is unavailable in the current session, use `search_web` targeting `github.com/<owner>/<repo>`.)*

## 2. Extract & Cross-Link in English (`wiki/`)
Follow `GEMINI.md` rules (English-only, dateless `kebab-case.md`, Dataview YAML frontmatter):
1. **Source Page (`wiki/sources/<repo-slug>-repo.md`, `type: source`)**:
   - `sources: ["https://github.com/<owner>/<repo>"]`
   - Include: **TL;DR**, **Core Architecture / How It Works** (with a `mermaid` diagram if non-trivial), **Tech Stack & Requirements** (e.g., GPU/RAM, OS, license), **Quick-Start / Install Commands**, and **Why It's Interesting / Caveats**.
2. **Entity Page (`wiki/entities/<repo-slug>.md`, `type: entity`)**:
   - Concise profile of the tool/framework/library linking back to `[[<repo-slug>-repo]]`.
3. **Concept Pages (`wiki/concepts/`)** *(only if warranted)*:
   - Link to existing concepts in `wiki/index.md` or create a new atomic concept if the repo introduces a notable reusable pattern.

## 3. Update Index, Log & Verify
- Add new pages to `wiki/index.md` (`Sources`, `Entities`, `Concepts`) with `(updated: YYYY-MM-DD)`.
- **Append** to the bottom of `wiki/log.md`:
  ```markdown
  ## [YYYY-MM-DD] ingest | <owner>/<repo> (GitHub)
  ```
- Verify only the touched files (valid YAML frontmatter and `[[wikilinks]]`) and report concisely.
