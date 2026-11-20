---
type: concept
tags: [discrete-math, logic, propositional-logic, predicate-logic]
sources: ["[[ch2-logics-source]]", "My Note My Life/6 - Full Note/Logics.md"]
updated: 2026-11-20
---

# Propositional and Predicate Logic

**Propositional logic** and **predicate logic** form the formal foundation for reasoning about truth values, mathematical statements, and hardware/software correctness.

## 1. Propositions & Bound Variables
A **proposition** is a declarative statement that is either **true** or **false**, but not both (it cannot contain free variables or vague/unbounded context).
- *Not a proposition:* $n > 10 \rightarrow 2^n > 100$ (contains free variable $n$).
- *Proposition (quantified):* $\forall n,\; n > 10 \rightarrow 2^n > 100$ ($n$ is bound by the universal quantifier $\forall$).

## 2. Logical Connectives
Beyond standard Boolean operators ($\neg, \land, \lor, \oplus$):
- **Implication ($p \rightarrow q$):** A one-sided contract where $p$ is the hypothesis (assumption) and $q$ is the conclusion. It is false **only** when $p$ is true and $q$ is false; if $p$ is false, $p \rightarrow q$ is vacuously true regardless of $q$.
- **Biconditional ($p \iff q$):** A two-sided contract requiring $p$ and $q$ to share the exact same truth value.

### Contrapositive vs. Converse
Given $A \rightarrow B$:
- **Contrapositive ($\neg B \rightarrow \neg A$):** Logically equivalent to $A \rightarrow B$:

| $A$ | $B$ | $A \rightarrow B$ | $\neg B \rightarrow \neg A$ |
| --- | --- | --- | --- |
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

- **Converse ($B \rightarrow A$):** Equivalent to the inverse ($\neg A \rightarrow \neg B$), **not** to $A \rightarrow B$.

## 3. Classification & Equivalence
- **Tautology:** Always true (e.g., $p \lor \top$, or $p \lor \neg p$).
- **Contradiction:** Always false (e.g., $p \land \bot$, or $p \land \neg p$).
- **Contingency:** Neither a tautology nor a contradiction (e.g., $p \lor q$).

> [!IMPORTANT]
> **$\iff$ vs. $\equiv$:** The biconditional $\iff$ is a logical connective that combines two propositions into a new proposition. Logical equivalence $\equiv$ is a meta-statement asserting that two propositions have identical truth tables (so $p \equiv q$ is not itself a proposition).

Key transformations:
- $p \rightarrow q \equiv \neg p \lor q$
- $p \iff q \equiv (p \rightarrow q) \land (q \rightarrow p)$

## References
- [[ch2-logics-source]]
- [[sets-and-functions]]
