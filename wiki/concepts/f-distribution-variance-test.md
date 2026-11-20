---
type: concept
tags: [statistics, variance-inference, f-distribution, hypothesis-testing, two-sample-test]
sources: ["[[inference-on-the-variances-lecture]]"]
updated: 2026-11-20
---

# F-Distribution & Two-Sample Variance Test

The **$F$-distribution** models the ratio of two independent scaled [[chi-square-variance-inference|chi-square]] random variables and is used to test whether two independent normal populations have equal variances.

## 1. Definition & Moments
If $W \sim \chi^2_u$ and $Y \sim \chi^2_v$ are independent, then
$$F = \frac{W/u}{Y/v} \sim F_{u, v}$$
with PDF ($x > 0$):
$$f(x) = \frac{\Gamma\!\left(\frac{u+v}{2}\right)\left(\frac{u}{v}\right)^{u/2} x^{(u/2)-1}}{\Gamma\!\left(\frac{u}{2}\right)\Gamma\!\left(\frac{v}{2}\right)\left[\left(\frac{u}{v}\right)x + 1\right]^{(u+v)/2}}$$
- **Mean**: $\mu = \frac{v}{v-2}$ (for $v > 2$)
- **Variance**: $\sigma^2 = \frac{2v^2(u+v-2)}{u(v-2)^2(v-4)}$ (for $v > 4$)
- **Reciprocal Quantile Property** (useful when tables only list upper tails):
  $$f_{1-\alpha,\, u,\, v} = \frac{1}{f_{\alpha,\, v,\, u}}$$

## 2. Two-Sample Variance Ratio Statistic
Given independent random samples of sizes $n_1, n_2$ from $N(\mu_1, \sigma_1^2)$ and $N(\mu_2, \sigma_2^2)$ with sample variances $S_1^2, S_2^2$:
$$F = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} \sim F_{n_1 - 1,\, n_2 - 1}$$

## 3. Hypothesis Testing ($H_0: \sigma_1^2 = \sigma_2^2$)
Under $H_0$, the test statistic simplifies to:
$$F_0 = \frac{S_1^2}{S_2^2}$$

| Alternative ($H_1$) | Rejection Region |
| :--- | :--- |
| $\sigma_1^2 \ne \sigma_2^2$ | $f_0 > f_{\alpha/2,\, n_1-1,\, n_2-1}$ or $f_0 < f_{1-\alpha/2,\, n_1-1,\, n_2-1}$ |
| $\sigma_1^2 > \sigma_2^2$ | $f_0 > f_{\alpha,\, n_1-1,\, n_2-1}$ |
| $\sigma_1^2 < \sigma_2^2$ | $f_0 < f_{1-\alpha,\, n_1-1,\, n_2-1}$ |

## References
- [[inference-on-the-variances-lecture]]
- Related: [[chi-square-variance-inference]]
