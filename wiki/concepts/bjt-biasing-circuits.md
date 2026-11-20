---
type: concept
tags: [electronics, bjt, transistor, analog-circuits, biasing]
sources: ["[[bjt-biasing-co2037-lecture]]"]
updated: 2026-11-20
---

# BJT Biasing Circuits

Bipolar Junction Transistor (BJT) biasing circuits use DC supplies and resistor networks to establish a stable quiescent operating point (**Q-point**) in the **active (linear) region**, allowing AC signals to be amplified without waveform clipping or distortion (based on [[bjt-biasing-co2037-lecture]]).

---

## 1. The Q-Point and DC Load Line

### 1.1. Quiescent Operating Point (Q-Point)
The Q-point is defined by a coordinate pair on the output characteristic plane $(V_{CE}, I_C)$:
$$Q = (V_{CEQ}, I_{CQ})$$
- $I_{BQ}$: DC base current, set by the base (input) loop.
- $I_{CQ} = \beta_{DC} I_{BQ}$: DC collector current (valid in the active region).
- $V_{CEQ}$: DC collector–emitter voltage, set by the collector (output) loop.

### 1.2. DC Load Line
Applying Kirchhoff's Voltage Law (KVL) around the collector loop (for a basic circuit without $R_E$):
$$V_{CC} - I_C R_C - V_{CE} = 0 \implies V_{CE} = V_{CC} - I_C R_C$$

- **Vertical intercept (Saturation end, $V_{CE} \approx 0$):** $I_{C(\text{sat})} = \frac{V_{CC}}{R_C}$
- **Horizontal intercept (Cutoff end, $I_C = 0$):** $V_{CE(\text{off})} = V_{CC}$
- The Q-point is the intersection of the DC load line with the transistor curve for $I_B = I_{BQ}$. Changing $I_B$ slides $Q$ along the load line; changing $V_{CC}$ or $R_C$ shifts or tilts the load line itself.

---

## 2. Operating Regions and Quick Saturation Test

| Operating Region | B–E & B–C Junction States | Voltage & Current Relations | Equivalent Behavior |
|---|---|---|---|
| **Cutoff** | B–E reverse-biased<br>B–C reverse-biased | $I_B \approx 0,\quad I_C \approx 0$<br>$V_{CE} \approx V_{CC}$ | Open switch |
| **Active (Linear)** | B–E forward-biased ($V_{BE} \approx 0.7\text{ V}$)<br>B–C reverse-biased | $I_C = \beta_{DC} I_B$<br>$0 < V_{CE} < V_{CC}$ | Linear amplifier |
| **Saturation** | B–E forward-biased<br>B–C forward-biased | $V_{CE} \approx V_{CE(\text{sat})} \approx 0.2\text{ V}$ (ideal $\approx 0\text{ V}$)<br>$I_C = I_{C(\text{sat})} < \beta_{DC} I_B$ | Closed switch |

### Quick Test for Saturation
1. Compute the collector current "demanded" by the base: $I_{\text{demand}} = \beta_{DC} I_B$.
2. Compute the maximum current the collector loop can supply: $I_{C(\text{sat})}$.
3. **Compare:**
   - If $\beta_{DC} I_B < I_{C(\text{sat})} \implies$ **Active region** ($I_C = \beta_{DC} I_B$).
   - If $\beta_{DC} I_B \ge I_{C(\text{sat})} \implies$ **Saturation** ($I_C$ is clamped at $I_{C(\text{sat})}$, no longer $\beta_{DC} I_B$).

---

## 3. Standard 4-Step Bias Analysis Recipe

1. **Step 1 — Base Loop (Input Loop):**
   Write KVL through the B–E junction (assume $V_{BE} = 0.7\text{ V}$ for silicon unless stated otherwise), using $I_E = (\beta_{DC} + 1)I_B$, and solve for $I_B$.
2. **Step 2 — Collector Current ($I_C$):**
   Assume active-region operation temporarily: $I_C = \beta_{DC} I_B$.
3. **Step 3 — Collector Loop (Output Loop):**
   Write KVL through C–E and solve for $V_{CE}$ to obtain $Q = (V_{CEQ}, I_{CQ})$.
4. **Step 4 — Load Line & Verification:**
   Find $I_{C(\text{sat})}$ (at $V_{CE} = 0$) and $V_{CE(\text{off})}$ (at $I_C = 0$), and verify $I_{CQ} < I_{C(\text{sat})}$.

---

## 4. Five Classic Biasing Topologies

> [!TIP]
> **The Golden Pattern (Emitter Degeneration):**
> Any resistor $R_E$ in the emitter path appears in the base-loop KVL multiplied by $(\beta_{DC} + 1)$. When $(\beta_{DC} + 1)R_E$ dominates the base-loop resistance, $\beta_{DC}$ cancels between numerator and denominator, making the Q-point thermally stable.

```text
                   BJT BIAS TOPOLOGIES
        ┌───────────────────┴───────────────────┐
  Single Supply (+Vcc)                   Dual Supply (±V)
 ┌──────┴─────────────────────────┐             │
 │                                │             │
Base-bias                 Collector-feedback  Emitter-bias
 ├─ No RE (Fixed)          (Negative feedback)
 ├─ With RE
 └─ Voltage-divider
```

### 4.1. Base Bias (Fixed Bias)
- **Base loop:** $V_{CC} - I_B R_B - V_{BE} = 0 \implies I_B = \frac{V_{CC} - V_{BE}}{R_B}$
- **Collector current:** $I_C = \beta_{DC} \frac{V_{CC} - V_{BE}}{R_B}$
- **Collector–emitter voltage:** $V_{CE} = V_{CC} - I_C R_C$
- **Load-line intercepts:** $I_{C(\text{sat})} = \frac{V_{CC}}{R_C},\quad V_{CE(\text{off})} = V_{CC}$
- **Stability:** Poor—$I_C$ is directly proportional to $\beta_{DC}$, which drifts significantly with temperature and device variation.

### 4.2. Base Bias with Emitter Resistor ($R_E$)
- **Base loop:** $V_{CC} - I_B R_B - V_{BE} - (\beta_{DC} + 1) I_B R_E = 0 \implies I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta_{DC} + 1) R_E}$
- **Collector–emitter voltage:** $V_{CE} = V_{CC} - I_C R_C - I_E R_E \approx V_{CC} - I_C (R_C + R_E)$
- **Load-line intercepts:** $I_{C(\text{sat})} = \frac{V_{CC}}{R_C + R_E},\quad V_{CE(\text{off})} = V_{CC}$

### 4.3. Collector-Feedback Bias
$R_B$ connects to the Collector instead of $V_{CC}$, so $R_C$ carries $I_C + I_B = (\beta_{DC} + 1) I_B$.
- **Base loop:** $V_{CC} = (\beta_{DC} + 1) I_B R_C + I_B R_B + V_{BE} \implies I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta_{DC} + 1) R_C}$
- **Collector current:** $I_C = \beta_{DC} I_B$
- **Collector–emitter voltage:** $V_{CE} = V_{CC} - (I_C + I_B) R_C \approx V_{CC} - I_C R_C$
- **Load-line intercepts:** $I_{C(\text{sat})} \approx \frac{V_{CC}}{R_C},\quad V_{CE(\text{off})} = V_{CC}$
- **Stabilization mechanism:** Negative feedback ($I_C \uparrow \implies V_C \downarrow \implies I_B \downarrow \implies I_C \downarrow$).

### 4.4. Emitter Bias (Dual Supply: $+V_{CC}$ and $-V_{EE}$)
The negative supply $-V_{EE}$ forward-biases the B–E junction while the Base sits near $0\text{ V}$ through $R_B$.
- **Base–emitter loop:** $0 - I_B R_B - V_{BE} - (\beta_{DC} + 1) I_B R_E - (-V_{EE}) = 0$
  $$I_C = \beta_{DC} \cdot \frac{V_{EE} - V_{BE}}{R_B + (\beta_{DC} + 1) R_E}$$
- **Collector–emitter loop:** Total supply span is $V_{CC} + V_{EE}$:
  $$V_{CE} = (V_{CC} + V_{EE}) - I_C R_C - I_E R_E \approx (V_{CC} + V_{EE}) - I_C (R_C + R_E)$$
- **Load-line intercepts:** $I_{C(\text{sat})} = \frac{V_{CC} + V_{EE}}{R_C + R_E},\quad V_{CE(\text{off})} = V_{CC} + V_{EE}$
- **$\beta_{DC}$-independent condition:** When $R_E \gg \frac{R_B}{\beta_{DC}}$ and $V_{EE} \gg V_{BE} \implies I_C \approx \frac{V_{EE}}{R_E}$.

### 4.5. Voltage-Divider Bias (Most Widely Used)
An $R_1\text{–}R_2$ divider biases the Base from a single supply $V_{CC}$.
- **Thévenin equivalent at the Base:**
  $$V_{TH} = V_{CC} \cdot \frac{R_2}{R_1 + R_2}, \qquad R_{TH} = R_1 \parallel R_2 = \frac{R_1 \cdot R_2}{R_1 + R_2}$$
- **Exact base current:**
  $$I_B = \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta_{DC} + 1) R_E}$$
- **Collector current & voltage:** $I_C = \beta_{DC} I_B$, $V_{CE} \approx V_{CC} - I_C (R_C + R_E)$
- **Stiff divider ($\beta_{DC}$-independent) condition:**
  $$\text{If } R_E \gg \frac{R_{TH}}{\beta_{DC}} \quad (\text{or } \beta_{DC} R_E \ge 10 R_2) \implies I_C \approx \frac{V_{TH} - V_{BE}}{R_E}$$

---

## 5. Extension: Collector Load Resistor ($R_L$)

When a load resistor $R_L$ is connected from the Collector to ground:
1. $R_L$ **does not affect the base loop**: compute $I_B$ and $I_C$ normally using Thévenin analysis.
2. **Apply KCL at the Collector node:**
   $$I_{RC} = I_C + I_{RL} \implies \frac{V_{CC} - V_C}{R_C} = I_C + \frac{V_C}{R_L}$$
3. Solve for the collector node voltage $V_C$:
   $$V_C = \frac{\frac{V_{CC}}{R_C} - I_C}{\frac{1}{R_C} + \frac{1}{R_L}}$$
4. Compute $V_E = I_E R_E \approx I_C R_E$, then $V_{CE} = V_C - V_E$.

---

## 6. Maximum Undistorted Swing and Waveform Clipping

When an AC input rides on the DC Q-point:
- **$Q$ too close to saturation ($V_{CEQ}$ small):** Negative peaks of $v_{ce}$ are clipped.
- **$Q$ too close to cutoff ($V_{CEQ}$ near $V_{CC}$):** Positive peaks of $v_{ce}$ are clipped.
- **Input amplitude too large:** Both positive and negative peaks are clipped.

### Maximum Undistorted Peak Swing
Distance from $I_{CQ}$ to each end of the load line:
$$\Delta I_{\text{sat}} = I_{C(\text{sat})} - I_{CQ}, \qquad \Delta I_{\text{cutoff}} = I_{CQ} - 0 = I_{CQ}$$

The maximum peak AC collector current is limited by the **smaller** margin:
$$I_{c(\text{peak})} = \min(\Delta I_{\text{sat}}, \Delta I_{\text{cutoff}}) \implies I_{b(\text{peak})} = \frac{I_{c(\text{peak})}}{\beta_{DC}}$$

> For maximum symmetrical undistorted swing, design the Q-point at the **midpoint of the DC load line**:
> $$I_{CQ} = \frac{I_{C(\text{sat})}}{2}, \qquad V_{CEQ} = \frac{V_{CE(\text{off})}}{2}$$

---

## Related Notes
- [[bjt-biasing-co2037-lecture]]
- [[jfet-fundamentals-and-biasing]]
- [[electrical-circuit-fundamentals]]
