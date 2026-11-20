---
type: source
tags: [electronics, fet, jfet, mosfet, lecture, co2037]
sources: ["raw/docs/FET_English.pdf"]
updated: 2026-11-20
---

# CO2037 Lecture — Field-Effect Transistors (FET)

Lecture slide deck for **CO2037 – Electronic Devices and Circuits** (Faculty of Computer Science and Engineering, HCMUT), covering JFET, D-MOSFET, and E-MOSFET theory, characteristics, and DC bias analysis (46 slides).

---

## Coverage Summary

1. **Part 1 — Junction FET (JFET) (Slides 4–12):**
   - FET family classification (unipolar, voltage-controlled, $I_G \approx 0$).
   - JFET structure, circuit symbols, and gate arrow convention ($P \to N$).
   - Gate–channel reverse-bias control, **pinch-off vs. cut-off** distinction ($V_{DS(\text{sat})} = V_{GS} - V_P$ vs. $V_{GS(\text{off})} = V_P$).
   - Drain characteristic regions (ohmic/triode, saturation/active, breakdown), Shockley's equation $I_D = I_{DSS}(1 - V_{GS}/V_P)^2$, and JFET vs. BJT comparison.
2. **Part 2 — JFET Examples and Biasing (Slides 13–29):**
   - Depletion-region polarity checks, multimeter diode-mode pin identification, ON/OFF state switching, and LED switch example.
   - DC bias configurations: Fixed bias, Self-bias, and Voltage-divider bias, with worked Q-point examples (Examples 5–7 and homework).
3. **Part 3 — Depletion-Type MOSFET (D-MOSFET) (Slides 30–33):**
   - Physical doped channel with $\text{SiO}_2$-insulated gate ($I_G \approx 0$ for both polarities).
   - Operation in both **depletion mode** ($I_D < I_{DSS}$) and **enhancement mode** ($I_D > I_{DSS}$) governed by Shockley's equation.
4. **Part 4 — Enhancement-Type MOSFET (E-MOSFET) & Summary (Slides 34–46):**
   - Induced inversion channel above threshold voltage $V_T = V_{GS(\text{th})}$; square-law equation $I_D = k(V_{GS} - V_T)^2$ where $k = I_{D(\text{on})}/(V_{GS(\text{on})} - V_T)^2$.
   - Reading the 2N4351 n-channel E-MOSFET datasheet, MOSFET bias configurations (feedback and voltage divider), and general FET DC analysis recipe.

---

## Linked Concept Notes
- [[jfet-fundamentals-and-biasing]]
- [[jfet-physical-mechanism]]
