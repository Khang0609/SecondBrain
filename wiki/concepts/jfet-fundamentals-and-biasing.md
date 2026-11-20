---
type: concept
tags: [electronics, fet, jfet, semiconductor, analog-circuits]
sources: ["[[fet-english-co2037-lecture]]"]
updated: 2026-11-20
---

# JFET Fundamentals and Biasing

Theory, operating regions, and DC bias analysis for the **Junction Field-Effect Transistor (JFET)**, based on the CO2037 – Electronic Devices and Circuits lecture ([[fet-english-co2037-lecture]], slides 1–29).

---

## 1. Physical Nature and the FET Family

### 1.1. Overview of Field-Effect Transistors (FETs)
- **Voltage-controlled device:** The gate–source voltage $V_{GS}$ controls the drain current $I_D$.
- **Unipolar:** Current through the channel is carried by only one type of majority carrier (electrons in an n-channel, or holes in a p-channel), unlike the bipolar junction transistor (BJT), which relies on both electrons and holes.
- **Extremely high input resistance:** Under normal operation, the Gate–Channel P–N junction is always reverse-biased, so gate current is negligible:
  $$I_G \approx 0\text{ A} \implies R_{\text{in}} \ge 10^8\ \Omega \quad (\text{M}\Omega \text{ to G}\Omega\text{ range})$$
  By Kirchhoff's Current Law (KCL), this directly implies:
  $$I_D = I_S$$

### 1.2. Structure, Terminals, and Gate Arrow Convention
- Three terminals: **Drain (D)**, **Source (S)**, and **Gate (G)**.
- The conducting channel is an n-type or p-type semiconductor bar between D and S. The gate is formed by diffusing the opposite semiconductor type into the channel, creating a P–N junction.
- **Gate arrow convention:** The arrow always points in the forward P $\to$ N direction:
  - **n-channel JFET:** Arrow points **into** the channel ($P_{\text{gate}} \to N_{\text{channel}}$).
  - **p-channel JFET:** Arrow points **out of** the channel ($P_{\text{channel}} \to N_{\text{gate}}$).

```text
   n-channel JFET              p-channel JFET
        D                           D
        |                           |
     +--+--+                     +--+--+
   G |  |  |                   G |  |  |
  -->|  |  |                  <--|  |  |
     +--+--+                     +--+--+
        |                           |
        S                           S
  (Arrow points IN)          (Arrow points OUT)
```

### 1.3. JFET vs. BJT Comparison

| Characteristic | JFET | BJT |
|---|---|---|
| **Control quantity** | Voltage $V_{GS}$ | Current $I_B$ |
| **Output current law** | Nonlinear (quadratic): $I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2$ | Linear: $I_C = \beta_{DC} I_B$ |
| **Output current relation** | $I_D = I_S$ | $I_C \approx I_E,\quad I_E = I_C + I_B$ |
| **Input side** | $I_G \approx 0\text{ A}$ | $I_B \ne 0\text{ A}\ (V_{BE} \approx 0.7\text{ V})$ |
| **Input resistance ($R_{\text{in}}$)** | Very high ($\text{M}\Omega$ to $\text{G}\Omega$) | Moderate ($\text{k}\Omega$) |
| **Charge carriers** | Unipolar (electrons or holes only) | Bipolar (both electrons and holes) |
| **Thermal stability** | Better thermal stability (negative temperature coefficient at high current) | Prone to thermal runaway |

---

## 2. Operating Mechanism and Characteristic Regions

*(Detailed below for an n-channel JFET; for a p-channel JFET, all voltage polarities and current directions are reversed. See [[jfet-physical-mechanism]] for the first-principles depletion physics.)*

### 2.1. Channel Width Control via $V_{GS}$
- **Normal operation (Gate–Source reverse-biased, $V_{GS} \le 0\text{ V}$):**
  Making $V_{GS}$ more negative widens the depletion region into the channel, narrowing the effective conductive cross-section, increasing channel resistance $R_{\text{channel}}$, and reducing $I_D$.
- **Forbidden condition (Gate–Source forward-biased, $V_{GS} > 0\text{ V}$):**
  The P–N gate junction conducts like a forward-biased diode ($I_G \ne 0$), destroying the high input resistance and risking device damage.

### 2.2. Pinch-off vs. Cut-off

> [!IMPORTANT]
> **Pinch-off is NOT Cut-off.** These are fundamentally different physical states:
> - **Pinch-off:** Occurs when $V_{DS} \ge V_{DS(\text{sat})} = V_{GS} - V_P$ (for $V_{GS} = 0\text{ V}$, $V_{DS} = |V_P|$). The depletion regions meet only near the **Drain end** (where reverse bias $V_{GD} = V_{GS} - V_{DS}$ is largest). A strong electric field sweeps carriers across the pinched-off region, so **$I_D$ does not drop to zero—it saturates at a constant value** (at $V_{GS} = 0\text{ V}$, $I_D \approx I_{DSS}$).
> - **Cut-off:** Occurs when $V_{GS} \le V_{GS(\text{off})} = V_P$. The depletion regions close the entire length of the channel $\implies$ **$I_D = 0\text{ A}$**.

*Notation convention:*
$$V_P \equiv V_{GS(\text{off})} \quad (\text{n-channel: } V_P < 0;\quad \text{p-channel: } V_P > 0)$$

### 2.3. Three Regions on the Drain Characteristics ($I_D$ vs. $V_{DS}$)
1. **Ohmic (Triode) Region:**
   - Condition: $V_{DS} < V_{GS} - V_P$.
   - Behavior: Depletion regions have not met; the channel acts as a **voltage-controlled resistor**:
     $$r_{DS} \approx \frac{V_{DS}}{I_D}$$
2. **Saturation (Active) Region:**
   - Condition: $V_{DS} \ge V_{GS} - V_P$ and $V_P < V_{GS} \le 0$.
   - Boundary (pinch-off locus):
     $$V_{DS(\text{sat})} = V_{GS} - V_P$$
   - Behavior: $I_D$ is nearly independent of $V_{DS}$, acting as a $V_{GS}$-controlled current source used for linear amplification.
3. **Breakdown Region:**
   - When $V_{DS}$ exceeds the maximum reverse breakdown voltage of the P–N junction, $I_D$ rises sharply and uncontrollably (must be avoided in circuit design).

---

## 3. Shockley's Equation and the Transfer Curve

### 3.1. Shockley's Equation
In the saturation region ($V_{DS} \ge V_{GS} - V_P$), drain current follows a square-law relationship:
$$I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2$$

Where:
- $I_{DSS}$: Maximum drain saturation current with gate shorted to source ($V_{GS} = 0\text{ V}$).
- $V_P \equiv V_{GS(\text{off})}$: Pinch-off / cut-off voltage (negative for n-channel, positive for p-channel).
- $V_{GS}$: Applied gate–source voltage ($V_P \le V_{GS} \le 0$ for n-channel).

### 3.2. Four Quick Points for Sketching the Transfer Curve

| $V_{GS}$ | $I_D$ | Description |
|---|---|---|
| $0\text{ V}$ | $I_{DSS}$ | Vertical-axis intercept ($V_{GS} = 0$) |
| $0.3 V_P$ | $\approx 0.5 I_{DSS}$ | Half-current point ($I_D \approx I_{DSS}/2$) |
| $0.5 V_P$ | $0.25 I_{DSS}$ | Quarter-current point ($I_D = I_{DSS}/4$) |
| $V_P$ | $0\text{ A}$ | Horizontal-axis intercept (cut-off $V_{GS(\text{off})}$) |

---

## 4. Practical Testing and Identification

### 4.1. Identifying Pins and Channel Type with a Multimeter (Diode Mode)
Because Gate–Channel is a P–N junction and Drain–Source is a resistive semiconductor channel:
1. **Find the Gate (G):**
   - Measure between one pin and the other two. The pin that shows a diode drop ($\approx 0.6\text{–}0.75\text{ V}$) to **both** other pins in one polarity and `OL` (Open Loop) when probes are reversed is the **Gate**.
2. **Determine channel type:**
   - If the **red (+)** probe on the Gate gives the diode drop to both other pins $\implies$ Gate is P, Channel is N $\implies$ **n-channel JFET**.
   - If the **black (COM)** probe on the Gate gives the diode drop to both other pins $\implies$ Gate is N, Channel is P $\implies$ **p-channel JFET**.
3. **Identify D and S:**
   - Measuring between the remaining two pins shows a small, symmetric reading in both directions (e.g., $\approx 0.015\text{ V}$ in diode mode, or tens to hundreds of $\Omega$) representing the resistive channel between D and S. *(For symmetrical JFETs, D and S are interchangeable in DC circuits.)*

### 4.2. ON / OFF State Summary

| Channel Type | Fully ON Condition | Cut-off (OFF) Condition |
|---|---|---|
| **n-channel** | $V_{GS} = 0\text{ V} \implies I_D = I_{DSS}$ | $V_{GS} \le V_P \quad (V_{GS} \text{ more negative than } V_P) \implies I_D = 0$ |
| **p-channel** | $V_{GS} = 0\text{ V} \implies I_D = I_{DSS}$ | $V_{GS} \ge V_P \quad (V_{GS} \text{ more positive than } V_P) \implies I_D = 0$ |

---

## 5. Classic DC Biasing Circuits

> [!NOTE]
> Every JFET DC bias analysis begins with the fundamental assumption:
> $$I_G = 0\text{ A} \implies I_S = I_D$$

### 5.1. Fixed-Bias Configuration
Uses a separate negative DC supply $-V_{GG}$ connected to the Gate through $R_G$:
- **Gate loop:** $-V_{GG} - I_G R_G - V_{GS} = 0$. Since $I_G = 0$:
  $$V_{GSQ} = -V_{GG} = \text{const}$$
- **Drain current:** Substitute $V_{GSQ}$ directly into Shockley's equation:
  $$I_{DQ} = I_{DSS} \left(1 - \frac{V_{GSQ}}{V_P}\right)^2$$
- **Output loop:**
  $$V_{DS} = V_{DD} - I_D R_D$$

### 5.2. Self-Bias Configuration
Eliminates $V_{GG}$ by grounding the Gate through $R_G$ and placing a resistor $R_S$ at the Source. Current $I_D$ flowing through $R_S$ raises $V_S = I_D R_S$, making the Gate negative relative to the Source:
- **Node voltages:**
  $$V_G = 0\text{ V} \quad (I_G = 0), \qquad V_S = I_D R_S$$
- **Input bias line:**
  $$V_{GS} = V_G - V_S = -I_D R_S$$
- **Output equations:**
  $$V_D = V_{DD} - I_D R_D, \qquad V_{DS} = V_{DD} - I_D (R_D + R_S) = V_D - V_S$$

**Solving for the Q-point $(V_{GSQ}, I_{DQ})$:**
1. **Algebraic method:** Substitute $V_{GS} = -I_D R_S$ into Shockley's equation:
   $$I_D = I_{DSS} \left(1 + \frac{R_S}{V_P} I_D\right)^2$$
   Expanding yields a quadratic equation in $I_D$:
   $$\left(\frac{I_{DSS} R_S^2}{V_P^2}\right) I_D^2 + \left(\frac{2 I_{DSS} R_S}{V_P} - 1\right) I_D + I_{DSS} = 0$$
   Select the physically valid root satisfying $0 \le I_D \le I_{DSS}$ and $|V_{GS}| \le |V_P|$.
2. **Graphical method:** Plot Shockley's curve using the 4 quick points (Section 3.2), then plot the load line $V_{GS} = -I_D R_S$ through $(0, 0)$ and $( -I_{DSS} R_S, I_{DSS})$. The intersection is $Q(V_{GSQ}, I_{DQ})$.

### 5.3. Voltage-Divider Bias
A resistor divider $R_1\text{–}R_2$ from $V_{DD}$ sets a positive Gate voltage $V_G$:
- **Gate voltage** (unloaded divider since $I_G \approx 0$):
  $$V_G = V_{DD} \cdot \frac{R_2}{R_1 + R_2}$$
- **Input bias line:**
  $$V_S = I_D R_S \implies V_{GS} = V_G - I_D R_S \quad \left(\text{or } I_D = \frac{V_G - V_{GS}}{R_S}\right)$$
- **Output equations:**
  $$V_{DS} = V_{DD} - I_D (R_D + R_S), \qquad V_D = V_{DD} - I_D R_D$$

**Finding the Q-point:**
- **Graphical:** The bias line intercepts the horizontal axis ($I_D = 0$) at $V_{GS} = V_G$ (positive side) and the vertical axis ($V_{GS} = 0$) at $I_D = V_G / R_S$. Its intersection with the transfer curve in the second quadrant gives $Q(V_{GSQ}, I_{DQ})$.
- **Algebraic:** Substitute $V_{GS} = V_G - I_D R_S$ into Shockley's equation and solve the resulting quadratic.

---

## 6. Worked Examples

### Example 5: Self-Bias (Finding Voltages from Known $I_D$)
- **Given:** $V_{DD} = 20\text{ V}$, $R_D = 2\text{ k}\Omega$, $R_S = 1\text{ k}\Omega$, $R_G = 100\text{ M}\Omega$, $I_D = 6\text{ mA}$.
- **Solution:**
  1. $V_G = 0\text{ V}$ (since $I_G \approx 0$).
  2. $V_S = I_D R_S = 6\text{ mA} \times 1\text{ k}\Omega = 6\text{ V}$.
  3. $V_{GS} = V_G - V_S = 0 - 6\text{ V} = -6\text{ V}$.
  4. $V_D = V_{DD} - I_D R_D = 20 - (6\text{ mA} \times 2\text{ k}\Omega) = 8\text{ V}$.
  5. $V_{DS} = V_D - V_S = 8 - 6 = 2\text{ V}$ (equivalently, $V_{DS} = V_{DD} - I_D(R_D + R_S) = 20 - 6 \times 3 = 2\text{ V}$).

### Example 7: Self-Bias (Graphical Q-Point)
- **Given:** $I_{DSS} = 10\text{ mA}$, $V_P = -8\text{ V}$, $R_S = 470\ \Omega$. Find $(V_{GSQ}, I_{DQ})$.
- **Solution:**
  - Load line: $V_{GS} = -I_D R_S$ passes through $(0\text{ V}, 0\text{ mA})$ and at $I_D = I_{DSS} = 10\text{ mA} \implies V_{GS} = -(10\text{ mA})(470\ \Omega) = -4.7\text{ V}$.
  - Graphical intersection (exact analytical solution in parentheses):
    $$V_{GSQ} \approx -2.3\text{ V}\ (-2.35\text{ V}), \qquad I_{DQ} \approx 5.0\text{ mA}\ (4.99\text{ mA})$$

---

## 7. Operating Region Validation Check

After solving for $(V_{GSQ}, I_{DQ})$ and $V_{DSQ}$, always verify:
1. **Non-cutoff condition:**
   $$V_P < V_{GSQ} \le 0$$
2. **Saturation (active) condition:**
   $$V_{DSQ} \ge V_{GSQ} - V_P$$
   - If satisfied: the JFET operates in the saturation region (validating Shockley's equation).
   - If $V_{DSQ} < V_{GSQ} - V_P$: the JFET is in the ohmic region, and Shockley's equation does not apply.

---

## Related Notes
- [[fet-english-co2037-lecture]]
- [[jfet-physical-mechanism]]
- [[bjt-biasing-circuits]]
- [[electrical-circuit-fundamentals]]
