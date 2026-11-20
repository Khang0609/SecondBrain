---
type: concept
tags: [probability, statistics, random-variables, pmf, pdf, cdf, expectation, variance]
sources: ["[[random-variables-source]]", "My Note My Life/6 - Full Note/Random Variables.md", "My Note My Life/6 - Full Note/Probability.md"]
updated: 2026-11-20
---

# Random Variables and Probability

A **random variable** $X$ is a function that maps outcomes from a random experiment's sample space into real numbers so they can be analyzed mathematically (e.g., mapping the six faces of a die to $\{1, 2, 3, 4, 5, 6\}$).

## 1. Discrete vs. Continuous Random Variables
- **Discrete Random Variables:** Take countable values; probabilities and expectations are computed using **summations** ($\sum$).
- **Continuous Random Variables:** Take values over continuous intervals; summations are replaced by **integrals** ($\int$).

## 2. Distribution Functions (PMF, PDF, CDF)
- **Probability Mass Function (PMF):** Gives the exact probability at a single discrete value, $p(x) = P(X = x)$.
- **Probability Density Function (PDF):** For a continuous random variable, the probability at any single exact point is $0$, so $f(x)$ measures probability density and probabilities are computed over intervals:
  $$P(a \le X \le b) = \int_a^b f(x)\,dx$$
- **Cumulative Distribution Function (CDF):** Accumulates probability up to a threshold $x$:
  $$F(x) = P(X \le x)$$

## 3. Expected Value, Variance, and Standard Deviation
- **Expected Value $E(X)$:** The probability-weighted mean of $X$ (analogous to the sample average, but weighted by theoretical probabilities rather than observed frequencies).
- **Variance $V(X)$:** Measures the spread or instability of the distribution (higher variance indicates greater dispersion):
  $$V(X) = E(X^2) - [E(X)]^2$$
- **Standard Deviation ($\sigma = \sqrt{V(X)}$):** Shares the same physical units as $X$ (unlike variance, which is in squared units), making it more intuitive for interpreting spread.

## References & Related Concepts
- [[random-variables-source]]
- [[gamma-and-erlang-distributions]]
- [[chi-square-variance-inference]]
- [[f-distribution-variance-test]]
- [[simple-linear-regression-ols]]
