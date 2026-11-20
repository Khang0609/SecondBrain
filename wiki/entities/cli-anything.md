---
type: entity
tags: [ai-agents, cli, python, tool, open-source]
sources: ["[[cli-anything-repo]]"]
updated: 2026-11-20
---

# CLI-Anything

**CLI-Anything** (`HKUDS/CLI-Anything`) is an open-source (Apache-2.0) toolkit and registry (`CLI-Hub`) that bridges GUI/desktop software and AI coding agents by wrapping applications in structured, JSON-capable Python `click` CLIs paired with auto-generated `SKILL.md` files.

## Key Capabilities
- **CLI-Hub (`cli-anything-hub`)**: `pip`-installable package manager for 50+ software harnesses (e.g., Obsidian, Blender, Godot, GIMP, Krita, Audacity, Draw.io, LibreOffice, RenderDoc, n8n, Zotero).
- **7-Phase Harness Generator**: Automated pipeline (`/cli-anything`) that analyzes a codebase, designs command groups, implements Click + REPL + JSON output, writes unit/E2E `pytest` suites, and publishes to `PATH`.
- **Agent-Native Design**: Structured `--json` output, self-describing `--help`, and unified `skills/` installation via `npx skills add HKUDS/CLI-Anything`.

## References
- [[cli-anything-repo]]
- Related: [[skill-driven-agent-workflows]], [[claude-code]]
