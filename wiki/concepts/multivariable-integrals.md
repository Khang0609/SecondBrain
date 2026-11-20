---
type: concept
tags: [calculus, multivariable-calculus, line-integrals, triple-integrals, spherical-coordinates]
sources: ["My Note My Life/6 - Full Note/Line Integrals.md", "My Note My Life/6 - Full Note/Triple Integral.md", "My Note My Life/6 - Full Note/Surface Integrals.md"]
updated: 2026-11-20
---

# Multivariable Integrals

Multivariable integration extends single-variable integration to curves, 3D regions, and surfaces.

## 1. Line Integrals of the First Kind (Scalar Line Integrals)

### Parametric Curves
A curve $C$ in $\mathbb{R}^2$ is parameterized by $t \in [a, b]$:
$$\begin{cases} x = x(t) \\ y = y(t) \end{cases}, \qquad a \le t \le b$$
Common parameterizations ($0 \le t \le 2\pi$):
- **Circle** centered at $(a, b)$ with radius $R$: $x = a + R\sin t,\; y = b + R\cos t$.
- **Ellipse** with semi-axes $a, b$: $x = a\sin t,\; y = b\cos t$.

In $\mathbb{R}^3$, parameterize the 2D projection first (by eliminating one variable) and then express the eliminated variable in terms of $t$.

### Definition & Properties
The scalar line integral computes the area of the curtain between a curve $C$ in the $xy$-plane and $z = f(x, y)$:
$$\int_C f(x, y)\,ds = \lim_{\Delta s_i \to 0} \sum_{i=1}^n f(x_i, y_i)\,\Delta s_i$$

Key properties:
- **Orientation independence:** $\int_{AB} f(x,y)\,ds = \int_{BA} f(x,y)\,ds$
- **Arc length:** $\int_{AB} 1\,ds = \text{length of } AB$
- **Linearity & additivity:** $\int_C [\alpha f + \beta g]\,ds = \alpha \int_C f\,ds + \beta \int_C g\,ds$, and $\int_{C_1 \cup C_2} f\,ds = \int_{C_1} f\,ds + \int_{C_2} f\,ds$.

### Evaluation Formulas
- For a smooth parametric curve $C$:
  $$\int_C f(x, y)\,ds = \int_a^b f(x(t), y(t))\,\sqrt{(x'(t))^2 + (y'(t))^2}\,dt$$
- For an explicit curve $y = y(x)$ with $a \le x \le b$:
  $$\int_C f(x, y)\,ds = \int_a^b f(x, y(x))\,\sqrt{1 + (y'(x))^2}\,dx$$

## 2. Triple Integrals in Spherical Coordinates

Spherical coordinates locate a point in $\mathbb{R}^3$ using one radial distance and two angles:
- **$\rho$ (Rho — distance):** Straight-line distance from the origin ($\rho \ge 0$).
- **$\theta$ (Theta — polar/tilt angle):** Angle down from the positive $z$-axis ($0 \le \theta \le \pi$, where $\theta = 0$ is $+z$, $\theta = \pi/2$ is the $xy$-plane, and $\theta = \pi$ is $-z$). Consequently, $\sin\theta \ge 0$.
- **$\varphi$ (Phi — azimuthal/pan angle):** Rotation around the $z$-axis ($0 \le \varphi \le 2\pi$), as in polar and cylindrical coordinates.

### Conversion Formulas
$$\begin{aligned}
x &= \rho \sin\theta \cos\varphi \\
y &= \rho \sin\theta \sin\varphi \\
z &= \rho \cos\theta
\end{aligned}$$
Useful identities:
- $x^2 + y^2 + z^2 = \rho^2$
- $\sqrt{x^2 + y^2} = \rho \sin\theta$

## 3. Surface Integrals
*(Placeholder: `Surface Integrals.md` in the source vault currently contains no content beyond the heading and will be populated when surface integral notes are added.)*
