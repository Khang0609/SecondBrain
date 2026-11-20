---
type: entity
tags:
  - graphics
  - vector-format
  - 2d-assets
  - indie-game
sources:
  - "[[claude-2d-character-animation-workflow]]"
updated: 2026-11-20
---

# SVG (Scalable Vector Graphics)

**SVG** is an XML-based, text-describable vector graphics format where shapes, curves, strokes, and layers are defined by coordinates and attributes.

## Why SVG Fits LLM-Generated Game Assets
- **Text-Native**: LLMs can write, parameterize, and refactor SVG geometry directly in code (e.g., via Python) without needing raster painting models.
- **Resolution-Independent**: Combined with normalized sizing (see [[quantitative-style-measurement]]), assets scale cleanly to any sprite resolution before rasterizing to PNG.
- **Composable**: Individual body parts, outfits, props, and facial expressions can be authored as separate functions and layered deterministically via `z-index` / DOM order.

## References
- [[claude-2d-character-animation-workflow]]
- Related: [[code-driven-2d-asset-pipeline]]
