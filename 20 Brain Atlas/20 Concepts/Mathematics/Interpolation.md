---
type: concept
subject: Mathematics
source_hash: e17f7d1421f20d6fdbf92e34360e2a2a
created: 2026-08-19
---

# Interpolation

**Interpolation** is the method of estimating unknown intermediate data points within the boundary of a discrete set of known data points.

## Core Principle
Given $n+1$ discrete data points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$, interpolation finds a continuous function $f(x)$ such that:

$$f(x_i) = y_i \quad \text{for } i = 0, 1, \dots, n$$

This function $f(x)$ is then evaluated at unknown locations $x$ inside the range $[x_0, x_n]$.

## Common Techniques
1. **Nearest-Neighbor Interpolation:** Assigns the value of the nearest known point (step function, zero-order).
2. **Linear Interpolation (Lerp):** Connects adjacent points with straight line segments:
   $$f(x) = y_0 + (x - x_0) \frac{y_1 - y_0}{x_1 - x_0}$$
3. **Polynomial Interpolation:** Fits a single polynomial of degree $\le n$ through all points (e.g., [[Lagrange Interpolation]]).
4. **Spline Interpolation:** Fits piecewise low-degree polynomials (e.g., Cubic Splines) between neighboring pairs, preserving continuous derivatives and avoiding [[Runges Phenomenon|Runge's phenomenon]].
5. **Bilinear / Bicubic Interpolation:** Extends 1D interpolation to 2D grids (e.g., pixel sampling in image scaling).

## Interpolation vs. Extrapolation
- **Interpolation:** Estimates values *within* the known range $[x_0, x_n]$. Reliable because it stays bounded by known behavior.
- **Extrapolation:** Estimates values *outside* the known range ($x < x_0$ or $x > x_n$). Unreliable as non-linear trends can diverge rapidly.

## Key Applications
- **Computer Graphics & Game Dev:** Resizing images, smooth animation tweening (`lerp`, `slerp`).
- **Digital Signal Processing:** Resampling audio or downscaling time-series data.
- **Cryptography:** Polynomial secret reconstruction in [[Shamir Secret Sharing]].
- **Numerical Analysis:** Approximating solutions to differential equations and integration.
