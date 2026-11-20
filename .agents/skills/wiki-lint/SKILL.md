---
name: wiki-lint
description: >-
  Audit the entire Obsidian Wiki (wiki/) for broken [[wikilinks]], orphan pages,
  missing Dataview YAML frontmatter, and unresolved contradictions. Use only when
  explicitly invoked (/wiki-lint) or asked to audit/clean up the whole wiki.
---

# Wiki Lint — Full-Vault Health Check

Run this workflow when the user invokes `/wiki-lint` or explicitly asks to audit or clean up the entire `wiki/`.

## 1. Check Broken `[[Wikilinks]]`
- Scan all `.md` files in `wiki/` (ignoring example links inside backticks or fenced code blocks) and verify every `[[target]]` resolves to an existing `.md` file in `wiki/`.

## 2. Check Orphan Pages
- Compare all `.md` files in `wiki/sources/`, `wiki/concepts/`, `wiki/entities/`, and `wiki/syntheses/` against `wiki/index.md`.
- Flag any page missing from `wiki/index.md` or lacking inbound `[[wikilinks]]` from other pages.

## 3. Validate Dataview YAML Frontmatter
- Ensure every content page in `wiki/` (excluding `index.md` and `log.md`) has valid YAML frontmatter containing:
  - `type` (`source | concept | entity | synthesis`)
  - `tags`
  - `sources`
  - `updated` (`YYYY-MM-DD`)

## 4. Flag Contradictions & Missing Atomic Pages
- Identify any unresolved contradictions across sources that need a `## Contrasting Views / Updates` section.
- Flag recurring concepts or entities mentioned across multiple notes that do not yet have their own atomic page.

## 5. Report, Fix & Log
- Report all findings clearly to the user.
- Apply safe fixes (e.g., adding missing `index.md` entries or frontmatter fields); ask for confirmation before deleting, merging, or renaming pages.
- **Append** an audit entry to the **bottom** of `wiki/log.md`:
  ```markdown
  ## [YYYY-MM-DD] lint | <Short Summary>
  ```
