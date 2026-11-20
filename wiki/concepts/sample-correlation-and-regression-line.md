---
type: concept
tags: [statistics, correlation, regression-line, bivariate-data]
sources: ["[[simple-linear-regression-and-correlation-lecture]]"]
updated: 2026-11-20
---

# Sample Correlation & Regression Line

When paired observations $(X, Y)$ of total size $n$ are summarized in a **Sample Correlation Table** with joint counts $n_{ij}$ (row totals $n_i = \sum_j n_{ij}$, column totals $m_j = \sum_i n_{ij}$), both linear association and conditional-mean trends can be computed directly.

## 1. Sample Correlation Coefficient ($r_{XY}$)
Using sample moments $\bar{x} = \frac{1}{n}\sum_i x_i n_i$, $\bar{y} = \frac{1}{n}\sum_j y_j m_j$, $\overline{xy} = \frac{1}{n}\sum_{i,j} n_{ij} x_i y_j$, $\hat{s}_X^2 = \overline{x^2} - (\bar{x})^2$, and $\hat{s}_Y^2 = \overline{y^2} - (\bar{y})^2$:
$$r_{XY} = \frac{\overline{xy} - \bar{x}\cdot\bar{y}}{\hat{s}_X \cdot \hat{s}_Y}$$
- **Range**: $-1 \le r_{XY} \le 1$.
- **Interpretation**:
  - $r_{XY} = 0$: no linear relationship.
  - $r_{XY} \approx \pm 1$: near-exact linear relationship.
  - $r_{XY} > 0$: positive linear correlation; $r_{XY} < 0$: negative linear correlation.

## 2. Sample Regression Line
For each level $x_i$ ($i = 1, \dots, k$), the conditional sample mean of $Y$ is:
$$\bar{Y}_{x_i} = (\bar{Y} \mid X = x_i) = \frac{1}{n_i}\sum_{j=1}^h n_{ij} y_j$$
Connecting consecutive points $(x_i, \bar{Y}_{x_i})$ forms the piecewise **sample regression line of $Y$ on $X$**.

## 3. Sample Linear Regression Line ($y = A + Bx$)
The straight line closest to the piecewise sample regression line—minimizing $Q(A, B) = \sum_{i=1}^k n_i \left[\bar{Y}_{x_i} - (A + Bx_i)\right]^2$—has coefficients:
$$B = \frac{\overline{xy} - \bar{x}\cdot\bar{y}}{\hat{s}_X^2}, \qquad A = \bar{y} - B\bar{x}$$
When $|r_{XY}|$ is sufficiently strong, $y_0 = A + B x_0$ provides simple point predictions for $Y$ at $X = x_0$.

## References
- [[simple-linear-regression-and-correlation-lecture]]
- Related: [[simple-linear-regression-ols]]
