---
type: concept
tags: [electronics, fet, jfet, semiconductor-physics]
sources: ["[[fet-english-co2037-lecture]]"]
updated: 2026-11-20
---

# JFET Physical Mechanism and Channel Conductivity

A first-principles exploration of how the depletion region forms at the Gate–Channel P–N junction and how $V_{GS}$ modulates channel conductivity in a JFET (companion to [[jfet-fundamentals-and-biasing]]).

---

## 1. Origin of the Depletion Region

- **Diffusion across the P–N junction:**
  At the boundary between a $p$-type region (excess holes) and an $n$-type region (excess free electrons), a steep carrier concentration gradient drives diffusion: free electrons diffuse from $n$ into $p$ and recombine with holes, and vice versa.
- **Immobile ion cores left behind:**
  - When a free electron leaves a donor impurity atom in the $n$-region, it leaves behind a **fixed positive ion** locked in the crystal lattice.
  - When a hole is filled in the $p$-region by an acceptor impurity atom, it leaves behind a **fixed negative ion**.
  - Because these ions are bound to the crystal lattice, they cannot move to conduct current.
- **Mental model (Ice pillars in a stream):**
  Think of flowing electrons as water moving through a riverbed. The fixed lattice ions act like **frozen pillars of ice** forming along the banks. As more carriers diffuse and recombine, these ice pillars thicken into a solid barrier stripped of free charge carriers—the **depletion region** (a region depleted of mobile carriers).

---

## 2. Why the Depletion Region Blocks Current and Raises Channel Resistance

Current flowing from Drain to Source ($I_D$) is the drift of electrons through the conducting $n$-channel sandwiched between two depletion regions.

From the geometric resistance law of a uniform conductor:
$$R = \rho \frac{l}{A}$$

Where:
- $\rho$ ($\Omega\cdot\text{m}$): Resistivity of the semiconductor (determined by doping concentration and carrier mobility).
- $l$ ($\text{m}$): Effective channel length from Drain to Source.
- $A$ ($\text{m}^2$): Effective conductive cross-sectional area ($A = w \cdot d$, where $w$ is channel depth and $d$ is the gap remaining between the two depletion regions).

**Physical consequence:**
1. As the depletion regions expand inward, the conductive gap $d$ shrinks, causing the effective cross-sectional area **$A$ to decrease ($A \to 0$)**.
2. Because $R \propto \frac{1}{A}$:
   $$\lim_{A \to 0} R_{\text{channel}} = \lim_{A \to 0} \left(\rho \frac{l}{A}\right) = +\infty$$
3. The channel turns into a high-resistance bottleneck, choking off carrier flow.

---

## 3. How $V_{GS}$ Controls Depletion Width

- **Gate–Channel P–N junction:**
  The $p$-type Gate and $n$-type Channel form a P–N diode junction. Normal JFET operation requires $V_{GS} \le 0\text{ V}$ (reverse bias).
- **Reverse-bias mechanism:**
  - Connecting the negative terminal of $V_{GS}$ to the $p$-type Gate and the positive (or higher-potential) side to the $n$-type Channel pulls majority carriers away from the metallurgical junction.
  - Consequently, the space-charge region of immobile ions **widens on both sides**—extending especially deep into the more lightly doped $n$-channel.
- **Cut-off threshold ($V_{GS(\text{off})} = V_P$):**
  When $|V_{GS}|$ becomes negative enough to reach $V_P$, the opposing depletion boundaries meet along the entire length of the channel ($A \to 0 \implies R_{\text{channel}} \to \infty$), completely closing the channel and driving $I_D = 0\text{ A}$.

---

## 4. Key Insight: External vs. Built-in Electric Field

> [!WARNING]
> **Do not confuse the external gate bias field with a current-driving field.**
> Reverse-biasing $V_{GS}$ does not "push" drain current directly. Instead, it reinforces the built-in electric field $E_{\text{bi}}$ at the P–N junction, widening the potential barrier and sweeping mobile carriers away from the boundary. Thus, switching and amplification in a JFET work by **voltage-controlled modulation of the channel's conductive geometry**.

---

## 5. Open Questions for Further Inquiry

- When $V_{DS} > 0$, why is the reverse bias at the Drain end ($V_{GD} = V_{GS} - V_{DS}$) larger than at the Source end ($V_{GS}$), giving the depletion region a **wedge-shaped** profile?
- Why does $I_D$ saturate at $I_{DSS}$ rather than dropping to zero when the depletion regions first touch at the Drain end (pinch-off)? *(See [[jfet-fundamentals-and-biasing#2.2. Pinch-off vs. Cut-off]].)*

---

## Related Notes
- [[jfet-fundamentals-and-biasing]]
- [[bjt-biasing-circuits]]
- [[fet-english-co2037-lecture]]
