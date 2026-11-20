---
type: concept
tags: [linear-algebra, linear-transformation, matrices, kernel, image]
sources: ["My Note My Life/6 - Full Note/Linear Transformation.md"]
updated: 2026-11-20
---

# Linear Transformation

A **linear transformation** $T: V \to W$ is a structure-preserving map between two vector spaces (such as [[euclidean-space|Euclidean spaces]]).

## 1. Core Anatomy & Linearity Criteria
- **Domain ($V$):** The input vector space.
- **Codomain ($W$):** The target space where outputs live.
- **Image / Range ($\operatorname{im} T$):** The set of all actual outputs $\{T(x) \mid x \in V\}$.
- **Preimage:** The set of all $x \in V$ satisfying $T(x) = y$ for a given $y \in W$.

A map $T$ is **linear** if and only if for all $u, v \in V$ and scalars $c, c_1, c_2$:
1. **Additivity:** $T(u + v) = T(u) + T(v)$
2. **Homogeneity:** $T(cu) = cT(u)$

Equivalently, $T(c_1 u + c_2 v) = c_1 T(u) + c_2 T(v)$.

## 2. Transformation Matrix
Relative to a domain basis $E = \{e_1, \dots, e_n\}$ and a codomain basis $F$, $T$ is compiled into a matrix $A_{FE}$:
$$A_{FE} = \begin{bmatrix} [T(e_1)]_F & [T(e_2)]_F & \cdots & [T(e_n)]_F \end{bmatrix}$$
Computing the image of any vector $x \in V$ reduces to matrix-vector multiplication:
$$[T(x)]_F = A_{FE} \cdot [x]_E$$

## 3. Kernel, Image, and Rank-Nullity
- **Kernel ($\ker T$):** The set of inputs mapped to $\mathbf{0}_W$, corresponding to the null space $\operatorname{Nul} A$ ($Ax = 0$). It captures information lost by $T$.
- **Image ($\operatorname{im} T$):** The reachable outputs in $W$, corresponding to the column space $\operatorname{Col} A$.
- **Injective (One-to-One):** $\ker T = \{\mathbf{0}_V\}$ (no collisions).
- **Surjective (Onto):** $\operatorname{im} T = W$ (every output is reachable).
- **Rank-Nullity Theorem (Conservation of Dimensions):**
  $$\dim(\ker T) + \dim(\operatorname{im} T) = \dim(V)$$

## 4. CS & Engineering Applications
- **Computer Graphics:** Translation, rotation, and scaling via $3 \times 3$ or $4 \times 4$ matrices; transformation composition corresponds to matrix multiplication ($T_{\text{total}} = T_{\text{rotate}} \cdot T_{\text{scale}} \cdot T_{\text{translate}}$).
- **Machine Learning:** Neural network layers apply an affine/linear map followed by a nonlinearity: $y = \sigma(Wx + b)$.
- **DSP & Hardware:** The Fast Fourier Transform (FFT) is a linear map from time to frequency domain; hardware accelerators optimize matrix-vector multiplication via Multiply-Accumulate (MAC) units.
- **Cryptography:** Linear ciphers (e.g., Hill cipher) operate over finite fields, with decryption given by $T^{-1}$ ($A^{-1}$).

## Related Concepts
- [[euclidean-space]]
