---
type: concept
tags: [statistics, anova, f-test, experimental-design, fishers-lsd, multiple-comparisons]
sources: ["[[analysis-of-variance-anova-lecture]]"]
updated: 2026-11-20
---

# Single-Factor ANOVA & Fisher's LSD

**Single-Factor Analysis of Variance (ANOVA)** tests whether $a \ge 2$ treatment levels of a single factor have equal population means in a completely randomized experiment.

## 1. Linear Statistical Model & Assumptions
$$Y_{ij} = \mu + \tau_i + \varepsilon_{ij} = \mu_i + \varepsilon_{ij}, \qquad i = 1, \dots, a; \; j = 1, \dots, n$$
where $\mu$ is the overall mean, $\tau_i$ is the $i$-th treatment effect, and:
1. Errors $\varepsilon_{ij} \stackrel{\text{iid}}{\sim} N(0, \sigma^2)$ (normality & constant common variance $\sigma^2$).
2. Observations are randomly and independently sampled.
3. $\sum_{i=1}^a \tau_i = 0$.

**Hypotheses**:
$$H_0: \tau_1 = \tau_2 = \dots = \tau_a = 0 \quad (\mu_1 = \dots = \mu_a) \qquad \text{vs.} \qquad H_1: \tau_i \ne 0 \text{ for at least one } i$$

## 2. Sum-of-Squares & Degrees-of-Freedom Partitioning
For a balanced design ($N = a \times n$):
$$\underbrace{\sum_{i=1}^a \sum_{j=1}^n (y_{ij} - \bar{y}_{\cdot\cdot})^2}_{SS_T} = \underbrace{n \sum_{i=1}^a (\bar{y}_{i\cdot} - \bar{y}_{\cdot\cdot})^2}_{SS_{Tr}\text{ (Between Groups)}} + \underbrace{\sum_{i=1}^a \sum_{j=1}^n (y_{ij} - \bar{y}_{i\cdot})^2}_{SS_E\text{ (Within Groups)}}$$
$$df_T = an - 1 = (a - 1) + a(n - 1) = df_{Tr} + df_E$$

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
| :--- | :---: | :---: | :---: | :---: |
| **Treatments** | $SS_{Tr}$ | $a - 1$ | $MS_{Tr} = \frac{SS_{Tr}}{a - 1}$ | $F_0 = \frac{MS_{Tr}}{MSE}$ |
| **Error** | $SS_E$ | $a(n - 1)$ | $MSE = \frac{SS_E}{a(n - 1)}$ | |
| **Total** | $SS_T$ | $an - 1$ | | |

- **Expected Mean Squares**: $E(MSE) = \sigma^2$, while $E(MS_{Tr}) = \sigma^2 + \frac{n\sum_{i=1}^a \tau_i^2}{a - 1}$.
- **Rejection Rule**: Under $H_0$, $F_0 \sim F_{a-1,\, a(n-1)}$ (see [[f-distribution-variance-test]]). Reject $H_0$ when $F_0 > f_{\alpha,\, a-1,\, a(n-1)}$.

*(For unbalanced designs with group sizes $n_i$ and $N = \sum_{i=1}^a n_i$, compute $SS_T$ and $SS_{Tr}$ across $n_i$ and obtain $SS_E = SS_T - SS_{Tr}$.)*

## 3. Post-Hoc Multiple Comparisons: Fisher's LSD
When $H_0$ is rejected, ANOVA shows *at least one* mean differs, not *which* pairs differ. **Fisher's Least Significant Difference (LSD)** compares every pair $H_0: \mu_i = \mu_j$ using:
$$T = \frac{(\bar{Y}_{i\cdot} - \bar{Y}_{j\cdot}) - (\mu_i - \mu_j)}{\sqrt{\frac{2\,MSE}{n}}} \sim t_{a(n-1)}$$
- **Rejection threshold**: Reject $\mu_i = \mu_j$ if $|\bar{y}_{i\cdot} - \bar{y}_{j\cdot}| > \text{LSD}$, where
  $$\text{LSD} = t_{\alpha/2,\, a(n-1)} \sqrt{\frac{2\,MSE}{n}}$$
- **$100(1-\alpha)\%$ CI for $\mu_i - \mu_j$**: $(\bar{y}_{i\cdot} - \bar{y}_{j\cdot}) \pm \text{LSD}$.

## References
- [[analysis-of-variance-anova-lecture]]
- Related: [[f-distribution-variance-test]], [[simple-linear-regression-ols]]
