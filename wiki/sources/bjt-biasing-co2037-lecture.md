---
type: source
tags: [electronics, bjt, biasing, lecture, co2037]
sources: ["raw/docs/BJT_Biasing_English.pdf"]
updated: 2026-11-20
---

# CO2037 Lecture — BJT Biasing Circuits

Lecture slide deck for **CO2037 – Electronic Devices & Circuits** (Dr. Le Trong Nhan · HCMUT), covering the DC operating point (Q-point), DC load line, operating regions, and 10 worked biasing examples (33 slides).

---

## Coverage Summary

1. **Part 1 — The DC Operating Point (Slides 2–10):**
   - Definition of the quiescent point $Q = (V_{CEQ}, I_{CQ})$ and the DC load line ($V_{CE} = V_{CC} - I_C R_C$).
   - Cutoff, active (linear), and saturation regions, plus the quick saturation test ($\beta_{DC} I_B$ vs. $I_{C(\text{sat})}$).
   - Linear AC operation riding on $Q$, waveform clipping (saturation/cutoff/overdrive), and a **4-step bias analysis recipe** (Example 1: maximum undistorted base-current swing).
2. **Classic Bias Topologies & Worked Examples (Slides 11–32):**
   - **Base (fixed) bias** (Examples 2, 4) and **Base bias with emitter resistor $R_E$** (Example 3).
   - **Collector-feedback bias** with negative feedback stabilization (Example 5).
   - **Emitter bias (dual supply $+V_{CC}, -V_{EE}$)** (Examples 6–7).
   - **Voltage-divider bias** via Thévenin reduction, exact $I_E$ analysis, and collector load $R_L$ extension (Examples 8–10).
3. **Summary Comparison (Slide 33):**
   - Side-by-side formulas for $I_C$, $V_{CE}$, and Q-point stability, highlighting the $(\beta_{DC} + 1)R_E$ emitter-degeneration pattern.

---

## Linked Concept Notes
- [[bjt-biasing-circuits]]
