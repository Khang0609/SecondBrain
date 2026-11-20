---
type: concept
tags: [statistics, variance-inference, chi-square, confidence-interval, hypothesis-testing]
sources: ["[[inference-on-the-variances-lecture]]"]
updated: 2026-11-20
---

# Chi-Square Distribution & One-Sample Variance Inference

The **Chi-Square ($\chi^2$) distribution** is the foundational sampling distribution for estimating and testing the variance $\sigma^2$ of a single normal population.

## 1. Definition (Special Case of Gamma)
A random variable $X$ follows a chi-square distribution with $k \in \mathbb{N}$ degrees of freedom when it is a [[gamma-and-erlang-distributions|Gamma distribution]] with $\lambda = 1/2$ and $r = k/2$:
$$f(x) = \frac{x^{k/2 - 1} e^{-x/2}}{2^{k/2}\Gamma(k/2)}, \qquad x > 0$$

## 2. Pivotal Quantity for Normal Sample Variance
Let $X_1, \dots, X_n$ be a random sample from $N(\mu, \sigma^2)$ with sample variance $S^2$. Then:
$$X^2 = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$

## 3. $100(1-\alpha)\%$ Confidence Intervals for $\sigma^2$
- **Two-sided CI**:
  $$\frac{(n-1)s^2}{\chi^2_{\alpha/2,\, n-1}} \le \sigma^2 \le \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,\, n-1}}$$
- **One-sided CIs**:
  - Lower bound (left-bounded): $\sigma^2 \ge \frac{(n-1)s^2}{\chi^2_{\alpha,\, n-1}}$
  - Upper bound (right-bounded): $\sigma^2 \le \frac{(n-1)s^2}{\chi^2_{1-\alpha,\, n-1}}$

## 4. Hypothesis Testing ($H_0: \sigma^2 = \sigma_0^2$)
Compute the test statistic:
$$\chi_0^2 = \frac{(n-1)s^2}{\sigma_0^2}$$

| Alternative ($H_1$) | Rejection Region ($W_\alpha$) |
| :--- | :--- |
| $\sigma^2 \ne \sigma_0^2$ | $\chi_0^2 > \chi^2_{\alpha/2,\, n-1}$ or $\chi_0^2 < \chi^2_{1-\alpha/2,\, n-1}$ |
| $\sigma^2 > \sigma_0^2$ | $\chi_0^2 > \chi^2_{\alpha,\, n-1}$ |
| $\sigma^2 < \sigma_0^2$ | $\chi_0^2 < \chi^2_{1-\alpha,\, n-1}$ |

> **Assumption sensitivity**: Unlike $t$-tests for means, $\chi^2$ variance inference relies strongly on the population being normally distributed.

## References
- [[inference-on-the-variances-lecture]]
- Related: [[gamma-and-erlang-distributions]], [[f-distribution-variance-test]]
