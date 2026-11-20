---
type: concept
tags: [probability, statistics, gamma-distribution, erlang-distribution, poisson-process]
sources: ["[[inference-on-the-variances-lecture]]"]
updated: 2026-11-20
---

# Gamma and Erlang Distributions

The **Erlang** and **Gamma** distributions model positive continuous waiting times and generalize the exponential distribution.

## 1. Erlang Distribution
If $X$ is the waiting time until the $r$-th event ($r \in \{1, 2, \dots\}$) occurs in a Poisson process with rate $\lambda > 0$:
- **Tail probability** (equivalent to observing at most $r-1$ Poisson events by time $x$):
  $$P(X > x) = \sum_{k=0}^{r-1} \frac{e^{-\lambda x} (\lambda x)^k}{k!}$$
- **Probability Density Function (PDF)**:
  $$f(x) = \frac{\lambda^r x^{r-1} e^{-\lambda x}}{(r-1)!}, \qquad x > 0$$

## 2. The Gamma Function
$$\Gamma(r) = \int_0^\infty x^{r-1} e^{-x}\,dx, \qquad r > 0$$
Key properties:
1. $\Gamma(r)$ is finite for all $r > 0$.
2. $\Gamma(r) = (r-1)\Gamma(r-1)$ (recurrence).
3. $\Gamma(r) = (r-1)!$ when $r$ is a positive integer.
4. $\Gamma(1) = 0! = 1$.
5. $\Gamma(1/2) = \sqrt{\pi}$.

## 3. Gamma Distribution
Replacing $(r-1)!$ with $\Gamma(r)$ extends the shape parameter to any real $r > 0$:
$$f(x) = \frac{\lambda^r x^{r-1} e^{-\lambda x}}{\Gamma(r)}, \qquad x > 0, \; \lambda > 0, \; r > 0$$
- **Parameters**: $\lambda$ is the **rate** parameter; $r$ is the **shape** parameter.
- **Mean and Variance**:
  $$\mu = E(X) = \frac{r}{\lambda}, \qquad \sigma^2 = V(X) = \frac{r}{\lambda^2}$$
- **Special Cases**:
  - $r = 1$: Exponential distribution.
  - $r \in \mathbb{N}$: Erlang distribution.
  - $\lambda = 1/2$ and $r = k/2$ ($k \in \mathbb{N}$): [[chi-square-variance-inference|Chi-Square distribution]] with $k$ degrees of freedom.

## References
- [[inference-on-the-variances-lecture]]
