---
type: concept
tags: [linear-algebra, euclidean-space, orthogonality, orthogonal-complement]
sources: ["My Note My Life/6 - Full Note/Euclidean Space.md"]
updated: 2026-11-20
---

# Euclidean Space

**Euclidean space** ($\mathbb{R}^n$ equipped with the standard dot product) provides the geometric notions of length, angle, and perpendicularity underlying [[linear-transformation|linear transformations]].

## 1. Orthogonal Complements ($W^\perp$)
If $W$ is a subspace of $\mathbb{R}^n$, its **orthogonal complement** $W^\perp$ is the set of all vectors perpendicular to every vector in $W$:
$$W^\perp = \{\mathbf{z} \in V : \mathbf{z} \cdot \mathbf{v} = 0,\; \forall \mathbf{v} \in W\}$$

- **Basis Shortcut:** A vector $\mathbf{z}$ belongs to $W^\perp$ if and only if $\mathbf{z}$ is orthogonal to every vector in a basis $E = \{\mathbf{e}_1, \dots, \mathbf{e}_k\}$ of $W$ (since orthogonality extends to all linear combinations).
- **Subspace Property:** $W^\perp$ is always a subspace of $\mathbb{R}^n$ (contains $\mathbf{0}$ and is closed under addition and scalar multiplication).
- **Duality:** $(W^\perp)^\perp = W$.
- **Geometric Intuition in $\mathbb{R}^3$:**
  - If $W$ is a plane through the origin, $W^\perp$ is the line through the origin along its normal vector.
  - If $W$ is a line through the origin, $W^\perp$ is the plane perpendicular to it.

## 2. Orthogonal Sets
An **orthogonal set** $S = \{u_1, u_2, \dots, u_k\}$ is a collection of vectors that are pairwise perpendicular ($u_i \cdot u_j = 0$ for $i \ne j$).
- Every orthogonal set of nonzero vectors is **linearly independent** and therefore forms an orthogonal basis for the subspace $\operatorname{span}(S)$.

## Related Concepts
- [[linear-transformation]]
