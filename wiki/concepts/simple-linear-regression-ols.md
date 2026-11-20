---
type: concept
tags: [statistics, linear-regression, ols, anova, hypothesis-testing, r-squared]
sources: ["[[simple-linear-regression-and-correlation-lecture]]"]
updated: 2026-11-20
---

# Simple Linear Regression (OLS)

**Simple Linear Regression** models a non-deterministic linear relationship between one independent variable $x$ and a response $Y$:
$$Y = \beta_0 + \beta_1 x + \varepsilon, \qquad E(\varepsilon) = 0, \quad V(\varepsilon) = \sigma^2$$

## 1. Ordinary Least Squares (OLS) Estimators
Minimizing the residual sum of squares $L = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$ produces the normal equations and estimators:
$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}}, \qquad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$
where:
$$S_{xx} = \sum_{i=1}^n x_i^2 - \frac{\left(\sum_{i=1}^n x_i\right)^2}{n}, \qquad S_{xy} = \sum_{i=1}^n x_i y_i - \frac{\left(\sum_{i=1}^n x_i\right)\left(\sum_{i=1}^n y_i\right)}{n}$$
The fitted line is $\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$, with residuals $e_i = y_i - \hat{y}_i$.

## 2. Error Variance & Variation Decomposition
- **Unbiased estimator of $\sigma^2$** (since $E(SS_E) = (n-2)\sigma^2$):
  $$\hat{\sigma}^2 = \frac{SS_E}{n - 2} = \frac{SS_T - \hat{\beta}_1 S_{xy}}{n - 2}$$
- **Sum of Squares Identity**:
  $$SS_T = SS_R + SS_E$$
  where $SS_T = \sum (y_i - \bar{y})^2$ (total variation), $SS_R = \sum (\hat{y}_i - \bar{y})^2 = \hat{\beta}_1 S_{xy}$ (explained by regression), and $SS_E = \sum (y_i - \hat{y}_i)^2$ (unexplained error).
- **Coefficient of Determination ($R^2$)**:
  $$R^2 = \frac{SS_R}{SS_T}, \qquad 0 \le R^2 \le 1$$

## 3. Inference for $\beta_1$ and $\beta_0$ ($\varepsilon \sim N(0, \sigma^2)$)
Both $\hat{\beta}_0$ and $\hat{\beta}_1$ are unbiased and normally distributed:
- $\text{SE}(\hat{\beta}_1) = \sqrt{\frac{\hat{\sigma}^2}{S_{xx}}}$, with $T_0 = \frac{\hat{\beta}_1 - b_1}{\text{SE}(\hat{\beta}_1)} \sim t_{n-2}$ and $100(1-\alpha)\%$ CI: $\hat{\beta}_1 \pm t^{n-2}_{\alpha/2}\,\text{SE}(\hat{\beta}_1)$.
- $\text{SE}(\hat{\beta}_0) = \sqrt{\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right)\hat{\sigma}^2}$, with $T_0 = \frac{\hat{\beta}_0 - b_0}{\text{SE}(\hat{\beta}_0)} \sim t_{n-2}$ and $100(1-\alpha)\%$ CI: $\hat{\beta}_0 \pm t^{n-2}_{\alpha/2}\,\text{SE}(\hat{\beta}_0)$.

## References
- [[simple-linear-regression-and-correlation-lecture]]
- Related: [[sample-correlation-and-regression-line]], [[chi-square-variance-inference]]
