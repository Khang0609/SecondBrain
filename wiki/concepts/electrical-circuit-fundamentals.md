---
type: concept
tags: [electronics, circuits, fundamentals, signal-integrity]
sources:
  - "My Note My Life/6 - Full Note/Electrical Theory.md"
  - "My Note My Life/6 - Full Note/Resistance & their Circuits.md"
  - "My Note My Life/6 - Full Note/Resistive Circuits & Circuit Laws.md"
  - "My Note My Life/6 - Full Note/Electrical Electronic Circuits.md"
  - "My Note My Life/6 - Full Note/crosstalk.md"
updated: 2026-11-20
---

# Electrical Circuit Fundamentals

Core concepts and foundational inquiry notes on electrical conduction, resistance, circuit laws, waveforms, power control, and signal integrity.

---

## 1. Charge Carriers, Current, and Conductivity

- **Free electrons and conductivity:** Materials with a higher density of free electrons exhibit higher electrical conductivity.
- **Nature and measurability of current ($I$):** Current is a macroscopic abstraction representing the net rate of charge flow ($I = \frac{dQ}{dt}$) rather than a single physical particle. Even as an aggregate quantity, it is directly measurable through its physical effects—the magnetic field it generates (Hall-effect / clamp meters), thermal dissipation ($I^2 R$), or the voltage drop across a known shunt resistor ($V = I R_{\text{shunt}}$).

---

## 2. Resistance and Ohm's Law

- **Physical meaning:** Resistance ($R$) is always positive and opposes the flow of electric charge.
- **Material geometry:** A conductor's resistance is determined by its material resistivity $\rho$, length $l$, and cross-sectional area $S$:
  $$R = \rho \frac{l}{S}$$
  Even when no current flows ($I = 0$), the physical resistance $R$ of the component still exists as a material property; only the voltage drop across it ($V = IR$) becomes zero.
- **Voltage drop across a component ("Ohm's Law"):** Passing current $I$ through a resistive element $R$ produces a potential drop $\Delta V = I R$.
  - **Series connection** (same $I$, voltages add):
    $$V_{\text{total}} = I R_1 + I R_2 + \dots = I R_{\text{eq}} \implies R_{\text{eq}} = \sum_i R_i$$
  - **Parallel connection** (same $V$, currents add):
    $$I_{\text{total}} = \frac{V}{R_1} + \frac{V}{R_2} + \dots = \frac{V}{R_{\text{eq}}} \implies \frac{1}{R_{\text{eq}}} = \sum_i \frac{1}{R_i}$$

---

## 3. Waveforms, Power Control, and Safety Notes

- **Duty cycle (PWM):** Varying the duty cycle of a digital pulse train controls average power/voltage, serving as a bridge from digital switching signals to analog-level control.
- **DC vs. AC hazard:** Direct current (DC) can be more hazardous than alternating current (AC) at comparable levels because continuous DC causes sustained muscular contraction (tetany), making it harder to release a live conductor.
- **Open study questions on periodic waveforms:**
  - Derivation of $A_{\text{RMS}}$ and $A_{\text{AVG}}$ from integral definitions.
  - Relationship between $V_{\max}$ and $V_{\text{DC}}$ for half-wave and full-wave rectified waveforms.
  - Definitions and formulas for **form factor** ($k_f = V_{\text{RMS}} / V_{\text{AVG}}$) and **ripple factor**.
  - Generation and mathematical formulas for triangular and sawtooth waveforms.

---

## 4. Signal Integrity: Crosstalk

- **Crosstalk:** Unwanted electromagnetic interference (capacitive or inductive coupling) where a signal on one circuit, trace, or device induces noise onto an adjacent circuit or conductor.

---

## Related Notes
- [[bjt-biasing-circuits]]
- [[jfet-fundamentals-and-biasing]]
- [[pid-controller]]
