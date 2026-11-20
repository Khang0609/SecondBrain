---
type: concept
tags: [chemistry, thermodynamics, enthalpy, entropy, gibbs-free-energy]
sources: ["[[chapter-4-thermochemistry-source]]", "My Note My Life/6 - Full Note/Chemical Thermodynamics.md"]
updated: 2026-11-20
---

# Chemical Thermodynamics

**Chemical thermodynamics** studies energy transformations in physical and chemical processes to determine heat flow and predict whether a reaction is spontaneous.

## 1. Enthalpy ($\Delta H$)

### Standard Enthalpy of Formation ($\Delta H_f^\circ$)
- The enthalpy change when **one mole** of a substance is formed from its constituent elements in their standard states ($1\text{ atm}$, $25^\circ\text{C} / 298\text{ K}$).
- For any element in its standard state (e.g., $\text{H}_2(g)$, $\text{O}_2(g)$), $\Delta H_f^\circ = 0$.
- Reaction enthalpy from formation data:
  $$\Delta H^\circ_{\text{rxn}} = \sum n\,\Delta H_f^\circ(\text{products}) - \sum m\,\Delta H_f^\circ(\text{reactants})$$

### Standard Heat of Combustion ($\Delta H_c^\circ$)
- Heat released when one mole of a compound undergoes complete combustion with $\text{O}_2$.
- Reaction enthalpy from combustion data reverses the subtraction order:
  $$\Delta H^\circ_{\text{rxn}} = \sum m\,\Delta H_c^\circ(\text{reactants}) - \sum n\,\Delta H_c^\circ(\text{products})$$
- Non-combustible species such as $\text{O}_2$, $\text{CO}_2$, and $\text{H}_2\text{O}(l)$ have $\Delta H_c^\circ = 0$.
- Note: $\Delta H_f^\circ$ and $\Delta H_c^\circ$ are properties of individual substances, whereas $\Delta H^\circ_{\text{rxn}}$ applies to a full reaction.

## 2. Entropy ($S$) & The Second Law
**Entropy ($S$)** measures molecular disorder or randomness. Entropy increases ($\Delta S > 0$) when:
- Large molecules break down into smaller fragments.
- Phase transitions move toward greater freedom ($\text{solid} \to \text{liquid} \to \text{gas}$).
- The total number of moles of gas increases.

Standard reaction entropy change:
$$\Delta S^\circ_{\text{rxn}} = \sum n\,S^\circ(\text{products}) - \sum m\,S^\circ(\text{reactants})$$

**Second Law of Thermodynamics:** In any spontaneous process, the total entropy of the universe increases:
$$\Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}} > 0$$
(For a reversible process in an isolated/insulated system, $\Delta S_{\text{univ}} = 0$.)

## 3. Gibbs Free Energy ($G$)
At constant temperature and pressure, **Gibbs free energy** combines enthalpy and entropy into a single spontaneity criterion:
$$\Delta G = \Delta H - T\Delta S$$
- **$\Delta G < 0$:** Forward reaction is **spontaneous**.
- **$\Delta G = 0$:** System is at [[chemical-equilibrium|equilibrium]].
- **$\Delta G > 0$:** Forward reaction is **non-spontaneous** (requires external work).

*(Note: In gas-phase mixtures, **partial pressure** is the pressure exerted by an individual component, whereas **total pressure** is the sum across all components.)*

## References & Related Concepts
- [[chapter-4-thermochemistry-source]]
- [[chemical-equilibrium]]
- [[chemical-kinetics]]
