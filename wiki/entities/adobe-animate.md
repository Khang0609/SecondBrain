---
type: entity
tags:
  - animation
  - tool
  - timing
  - 2d-assets
sources:
  - "[[claude-2d-character-animation-workflow]]"
updated: 2026-11-20
---

# Adobe Animate

**Adobe Animate** is a 2D vector animation tool widely used for frame-based cartoon and game animation (typically at 24 or 30 fps).

## Role in SecondBrain Knowledge
- In [[claude-2d-character-animation-workflow]], an Adobe Animate motion-preset plugin and a zipped Animate smoke-puff VFX file served as **quantitative motion references** rather than final production tools:
  - Extracted 24 fps keyframe spacings (5-frame stepped shake, `20°` 3-frame-hold nod, 20-frame double-bounce walk cycle).
  - Extracted a 30 fps 4-stroke smoke-puff loop (2 frames per drawing) and re-implemented it in code with matching ink outlines.

## References
- [[claude-2d-character-animation-workflow]]
- Related: [[code-driven-2d-asset-pipeline]]
