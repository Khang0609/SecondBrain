---
type: concept
tags:
  - art-direction
  - style-transfer
  - prompting
  - 2d-assets
  - indie-game
sources:
  - "[[claude-2d-character-animation-workflow]]"
updated: 2026-11-20
---

# Quantitative Style Measurement

**Quantitative Style Measurement** is the practice of instructing an AI coding agent to measure visual reference samples into **exact numerical ratios and parameters** rather than summarizing them with subjective adjectives (e.g., "cute", "clean", "minimalist").

## Core Technique: Unit Normalization (`D`)
Instead of hardcoding pixel dimensions that break when assets are resized, define a single anchor unit—such as `1 D = head width`—and express every other dimension as a multiple of `D`:
- **Proportions**: Total character height = `2.2 D`; torso height = `1.1 D`.
- **Line Weight**: Outer stroke = `0.045 D` (e.g., `9 px` on a `200 px` head).
- **Structural Rules**: Count recurring traits across a sample set (e.g., 12 images / 29 characters) to separate core style rules (no neck, cylindrical torso, 24/29 armless) from one-off quirks.
- **Color & Shading**: Sample exact RGB/hex values for skin tones and shadow ratios via scripts rather than guessing.

## Pairing Data with House Rules
Measured rules capture *how the reference style works*; **house rules** define *what makes your project yours* (e.g., 3/4 right-facing angle, floating hands only for props, mouth hidden except at emotional peaks, standardized 6-expression set).

## Visual Critique Over Verbal Critique
- **Avoid vague words**: Words like *"improve"* or *"make it look better"* are ambiguous and frequently push LLMs to over-engineer details.
- **Use tight image crops**: Crop directly around the flawed detail alongside a reference example (e.g., *"simplify hands to rounded Doraemon-style mittens like this crop"*).

## References
- [[claude-2d-character-animation-workflow]]
- Related: [[code-driven-2d-asset-pipeline]], [[claude-code]]
