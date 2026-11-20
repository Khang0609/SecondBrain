---
type: concept
tags: [discrete-math, set-theory, functions, relations]
sources: ["My Note My Life/6 - Full Note/Sets.md", "My Note My Life/6 - Full Note/Functions.md"]
updated: 2026-11-20
---

# Sets and Functions

**Sets** and **functions** are the foundational building blocks of discrete mathematics and computer science, underpinning [[propositional-and-predicate-logic|formal logic]], graphs, automata, and type systems.

## 1. Sets & Set Properties
A **set** is an unordered collection of distinct objects (elements).
- **Order & multiplicity invariance:** Repeating or reordering elements does not change a set: $\{2, 1, 6, 0\} = \{2, 1, 6, 0, 0\} = \{1, 2, 0, 6\}$.
- **Membership table:** A truth-table-like matrix using `0` and `1` to track whether elements belong to given sets and verify set identities.

## 2. Heterogeneous Sets & Formal Structures
A **heterogeneous set** contains elements of different types or levels of abstraction (e.g., $B = \{1, \{2, 3\}, \emptyset\}$). This enables formalizing complex mathematical and computational structures purely in set theory:
- **Graphs:** $G = (V, E)$ combines a vertex set $V$ and an edge set $E$, encoded as an ordered pair $\{\{V\}, \{V, E\}\}$.
- **Formal Automata:** A finite state machine or Turing machine $M = (Q, \Sigma, \delta, q_0, F)$ bundles states, alphabet symbols, a transition function, a start state, and accept states.
- **Power Sets & Inductive Constructions:**
  - $\mathcal{P}(\emptyset) = \{\emptyset\}$ and $\mathcal{P}(\{\emptyset\}) = \{\emptyset, \{\emptyset\}\}$.
  - For $A = \{1, 2\}$, $\mathcal{P}(A) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$.
  - In Zermelo–Fraenkel set theory, natural numbers are built via nested sets (von Neumann ordinals, e.g., $2 = \{0, 1\} = \{\emptyset, \{\emptyset\}\}$).
- **Computing Data Structures:** Structs, records, and JSON objects draw from Cartesian products of distinct domains ($\text{ID} \times \text{Name} \times \text{Active}$), while Abstract Syntax Trees (ASTs) hold mixed tokens, literals, and subtrees.

## 3. Cartesian Product
The **Cartesian product** $A \times B$ is the set of all ordered pairs $(a, b)$ with $a \in A$ and $b \in B$.
- **Non-commutativity:** In general, $A \times B \ne B \times A$ (since ordered pairs distinguish position).

## 4. Functions
A **function** $f: A \to B$ maps each element in the domain $A$ to **exactly one** element in the codomain $B$.
- **Range (Image) vs. Codomain:** The range $\{f(a) \mid a \in A\}$ is always a subset of the codomain $B$.

## Related Concepts
- [[propositional-and-predicate-logic]]
- [[linear-transformation]]
