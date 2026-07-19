---
title: "GF 04 — Applications & Power Series"
course: Discrete Mathematics I
tags: ["discrete-mathematics", "generating-functions", "power-series", "taylor-series", "applications"]
aliases: ["GF 04 — Applications & Power Series"]
created: "2026-05-24"
type: Note
topic: Generating Functions
subtopic: Applications
week: 13
---

# 04 · Applications & Power Series

> **← Back to** [[03 GF Recurrences]] | **Next →** [[05 GF Practice]]

---

## 4.1 Connecting GFs to Power Series

So far, we have treated generating functions as **formal** algebraic objects (ignoring whether the infinite sum converges). But generating functions have a dual nature: they are also **analytic functions** that you can study using calculus.

### The Two Perspectives

*   **The Formal Algebraic View (Discrete Math):**
    We treat $x$ as a structural hook. Operations like shifting, adding, and multiplying are defined purely as rules for manipulating the coefficients. The sum does not need to converge.
*   **The Analytical View (Calculus):**
    We treat $x$ as a real or complex number. If we restrict $x$ to be in a specific interval (called the **interval of convergence**), the infinite sum converges to a specific numerical value. In this interval, the series is equal to an actual function $f(x)$ (like $\sin x$ or $e^x$).

### Bridging the Gap: Why can we mix them?

The wonderful fact of mathematics is that **if a formal identity holds algebraically, it also holds analytically for any value of $x$ where the series converges**. 

This means we can use calculus techniques—like Taylor series expansions, derivatives, integrals, and limits—to manipulate our generating functions, and then "decode" the result back into coefficients! 

For example, when we set $x=1$ in $e^x = \sum \frac{x^n}{n!}$ to get $e = \sum \frac{1}{n!}$, we are allowed to do this because $x=1$ lies within the interval of convergence (which for $e^x$ is all real numbers). However, setting $x=2$ in $\frac{1}{1-x} = \sum x^n$ to get $-1 = 1 + 2 + 4 + \cdots$ is **not** valid, because $x=2$ lies outside the interval of convergence ($|x| < 1$).

### Key Power Series (Memorize These)

Here are the most common power series expansions from calculus. You will use them constantly to transition between closed forms and sequences.

*   **Geometric Series:**
    $$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \cdots \quad (\text{for } |x| < 1)$$
*   **Exponential Function:**
    $$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \quad (\text{for all } x)$$
*   **Natural Logarithm:**
    $$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} x^n = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots \quad (\text{for } -1 < x \leq 1)$$
*   **Sine Function:**
    $$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots \quad (\text{for all } x)$$
*   **Cosine Function:**
    $$\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots \quad (\text{for all } x)$$
*   **Generalized Binomial Series:**
    $$(1+x)^\alpha = \sum_{n=0}^{\infty} \binom{\alpha}{n} x^n \quad (\text{for } |x| < 1, \text{ any real } \alpha)$$
    where $\binom{\alpha}{n} = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}$ is the generalized binomial coefficient.

---

## 4.2 The Exponential Function — A Special GF

The sequence $a_n = \frac{1}{n!}$ has GF:
$$G(x) = \sum_{n=0}^{\infty} \frac{x^n}{n!} = e^x$$

This leads to the concept of **Exponential Generating Functions (EGF)**:
$$\hat{G}(x) = \sum_{n=0}^{\infty} a_n \frac{x^n}{n!}$$

EGFs are used when order matters (permutations), while OGFs are used when order doesn't matter (combinations).

| Type | Form | Used for |
|------|------|----------|
| OGF | $\sum a_n x^n$ | Combinations, unlabeled structures |
| EGF | $\sum a_n \frac{x^n}{n!}$ | Permutations, labeled structures |

### Example: Derangements (EGF)

A **derangement** $D_n$ is a permutation with no fixed points.

EGF: $\hat{D}(x) = \frac{e^{-x}}{1-x}$

From this: $D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$

For large $n$: $D_n \approx \frac{n!}{e}$

---

## 4.3 Combinatorial Identities via GFs

GFs provide elegant proofs of combinatorial identities.

### Vandermonde's Identity

$$\sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$$

**Proof via GFs:**
- $(1+x)^m = \sum_k \binom{m}{k} x^k$ and $(1+x)^n = \sum_j \binom{n}{j} x^j$
- Multiply: $(1+x)^{m+n} = \sum_r \left[\sum_k \binom{m}{k}\binom{n}{r-k}\right] x^r$ (convolution)
- But $(1+x)^{m+n} = \sum_r \binom{m+n}{r} x^r$
- Comparing $[x^r]$ gives the identity. ✓

### Hockey Stick Identity

$$\sum_{k=0}^{n} \binom{k+r}{r} = \binom{n+r+1}{r+1}$$

**GF proof:** Use $\frac{1}{(1-x)^{r+1}} = \sum_k \binom{k+r}{r} x^k$ and partial sums.

---

## 4.4 GFs and Mathematical Constants

### Computing $e$

From $e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$, set $x=1$:
$$e = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \cdots = \sum_{n=0}^{\infty} \frac{1}{n!}$$

### Computing $\ln 2$

From $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$, set $x=1$:
$$\ln 2 = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$$

### Computing $\pi$

From $\arctan x = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} x^{2n+1}$, set $x=1$:
$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots$$
$$\pi = 4\left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots\right)$$

> 💡 These are beautiful connections: combinatorics meets analysis!

---

## 4.5 Counting Lattice Paths and Catalan Numbers

Generating functions are incredibly useful for counting paths on grids and finding formulas for recursive geometric patterns.

### 1. Simple Lattice Paths

**Problem:** How many paths are there from $(0,0)$ to $(n,n)$ using only right steps $R = (1,0)$ and up steps $U = (0,1)$?

- To get from $(0,0)$ to $(n,n)$, we must take exactly $n$ right steps and $n$ up steps, for a total of $2n$ steps.
- The choice of path corresponds to choosing which of the $2n$ steps are right steps.
- Therefore, the number of paths is:
  $$a_n = \binom{2n}{n}$$

**The Generating Function:**
If we write the generating function for the sequence $a_n = \binom{2n}{n}$, it turns out to be:
$$G(x) = \sum_{n=0}^{\infty} \binom{2n}{n} x^n = \frac{1}{\sqrt{1-4x}} = (1-4x)^{-1/2}$$
This closed form is derived using the Generalized Binomial Theorem with exponent $\alpha = -1/2$ (see [[06 GF Pattern Library]] for the detailed derivation).

---

### 2. Catalan Numbers: Paths under the Diagonal

**Problem:** How many paths from $(0,0)$ to $(n,n)$ using steps $R$ and $U$ **never go above the diagonal** $y = x$?

These are the **Catalan Numbers**, denoted $C_n$. The first few terms are:
$$C_0 = 1, \; C_1 = 1, \; C_2 = 2, \; C_3 = 5, \; C_4 = 14, \; C_5 = 42, \ldots$$

#### The Recurrence Relation (Convolution in Action)

Any valid path from $(0,0)$ to $(n,n)$ that stays below the diagonal must touch the diagonal again for the first time at some point $(k+1, k+1)$, where $0 \leq k \leq n-1$. 
1. **The First Segment (to the first touch):** The path must start with a Right step ($R$) and end with an Up step ($U$) to touch the diagonal. Between these two steps, the path must stay strictly below the diagonal. This is structurally identical to a Catalan path of size $k$. There are $C_k$ ways to form this segment.
2. **The Remaining Segment:** Once it touches $(k+1, k+1)$, the remaining path to $(n,n)$ is simply another independent Catalan path of size $n - 1 - k$. There are $C_{n-1-k}$ ways to form this segment.

Multiplying these two independent choices, we get $C_k \cdot C_{n-1-k}$ paths that touch the diagonal for the first time at $(k+1, k+1)$. Summing over all possible first-touch positions $k$:
$$C_n = C_0 C_{n-1} + C_1 C_{n-2} + C_2 C_{n-3} + \cdots + C_{n-1} C_0 = \sum_{k=0}^{n-1} C_k C_{n-1-k}$$

This sum is a perfect **sequence convolution**!

#### Deriving the Catalan Generating Function

Let $C(x) = \sum_{n=0}^{\infty} C_n x^n$. Let's write the recurrence in terms of $C(x)$:
$$C(x) = C_0 + \sum_{n=1}^{\infty} \left(\sum_{k=0}^{n-1} C_k C_{n-1-k}\right) x^n$$

Notice that the sum on the right is exactly the product $C(x) \cdot C(x)$ shifted right by one power of $x$ (multiplied by $x$):
$$C(x) = 1 + x [C(x)]^2$$

This is a **quadratic equation** in terms of the function $C(x)$! We can solve for $C(x)$ using the quadratic formula:
$$x [C(x)]^2 - C(x) + 1 = 0$$
$$C(x) = \frac{1 \pm \sqrt{1-4x}}{2x}$$

**Choosing the Sign:**
How do we know whether to use the $+$ or the $-$ sign? 
- If we take the limit as $x \to 0$ for the positive branch $C(x) = \frac{1 + \sqrt{1-4x}}{2x}$, the numerator approaches $2$ while the denominator approaches $0$, so the function diverges to infinity.
- If we take the limit for the negative branch $C(x) = \frac{1 - \sqrt{1-4x}}{2x}$, we get a $0/0$ form. Using L'Hôpital's rule:
  $$\lim_{x \to 0} \frac{1 - \sqrt{1-4x}}{2x} = \lim_{x \to 0} \frac{-\frac{1}{2\sqrt{1-4x}}(-4)}{2} = \lim_{x \to 0} \frac{2}{2\sqrt{1-4x}} = 1$$
  This matches our initial condition $C_0 = 1$.

Therefore, the generating function for Catalan numbers is:
$$\boxed{C(x) = \frac{1 - \sqrt{1-4x}}{2x}}$$

Expanding this using the Generalized Binomial Theorem (worked out in Note 06) yields Binet's form for Catalan numbers:
$$\boxed{C_n = \frac{1}{n+1} \binom{2n}{n}}$$

---

## 4.6 The Partition Function

**Problem:** In how many ways can we write an integer $n$ as a sum of positive integers, where the order of the terms does not matter?

For example, the partitions of $n = 4$ are:
1. $4$
2. $3 + 1$
3. $2 + 2$
4. $2 + 1 + 1$
5. $1 + 1 + 1 + 1$

So the partition number is $p(4) = 5$. 

### The Generating Function (Euler's Product Formula)

Euler discovered that the generating function $P(x) = \sum p(n) x^n$ is given by an infinite product:

$$P(x) = \prod_{k=1}^{\infty} \frac{1}{1-x^k} = \left(\frac{1}{1-x^1}\right) \left(\frac{1}{1-x^2}\right) \left(\frac{1}{1-x^3}\right) \left(\frac{1}{1-x^4}\right) \cdots$$

This formula looks complicated, but it has a beautifully simple combinatorial meaning. Let's expand each factor using the geometric series:

$$P(x) = \left(1 + x^1 + x^2 + x^3 + x^4 + \cdots\right) \left(1 + x^2 + x^4 + x^6 + x^8 + \cdots\right) \left(1 + x^3 + x^6 + x^9 + x^{12} + \dots\right) \cdots$$

When we multiply these infinite polynomials together, we choose exactly one term from each set of parentheses:
- From the **first factor** ($1-x^1$), we choose a term $x^{1 \cdot a}$. The exponent tells us **how many 1s** we use in our sum (e.g. $x^3$ means we use three 1s).
- From the **second factor** ($1-x^2$), we choose a term $x^{2 \cdot b}$. The exponent tells us **how many 2s** we use in our sum (e.g. $x^6 = x^{2 \cdot 3}$ means we use three 2s).
- From the **third factor** ($1-x^3$), we choose a term $x^{3 \cdot c}$. The exponent tells us **how many 3s** we use in our sum.

When we multiply the chosen terms together, we add their exponents:
$$x^{1\cdot a} \cdot x^{2\cdot b} \cdot x^{3\cdot c} \cdots = x^{a + 2b + 3c + \cdots}$$

The exponent $a + 2b + 3c + \cdots$ represents the total value of our partition! The coefficient of $x^n$ counts exactly how many ways we can select combinations of 1s, 2s, 3s, etc., that add up to exactly $n$.

**Example check for $n=4$:**
How can we get $x^4$ from the product? Let's look at the combinations of terms that multiply to $x^4$:
1. $x^4$ from the 1s factor, $1$ from the rest: $x^{1\cdot 4} \implies 1+1+1+1$
2. $x^1$ from the 1s factor, $x^3$ from the 3s factor: $x^{1\cdot 1} \cdot x^{3\cdot 1} \implies 3+1$
3. $x^2$ from the 1s factor, $x^2$ from the 2s factor: $x^{1\cdot 2} \cdot x^{2\cdot 1} \implies 2+1+1$
4. $1$ from the 1s factor, $x^4$ from the 2s factor: $x^{2\cdot 2} \implies 2+2$
5. $1$ from the 1s, 2s factors, $x^4$ from the 4s factor: $x^{4\cdot 1} \implies 4$

This gives exactly 5 ways! The algebraic expansion performs the partition counting for us automatically.

| $n$ | $p(n)$ |
|-----|--------|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 5 |
| 5 | 7 |
| 6 | 11 |
| 7 | 15 |

---

## 4.7 Solving Summations with GFs

GFs can evaluate difficult sums.

### Example: Sum of Squares

**Evaluate:** $\sum_{k=0}^{n} k^2$

We know $\sum_{n=0}^{\infty} n x^n = \frac{x}{(1-x)^2}$.

Differentiate: $\sum_{n=0}^{\infty} n^2 x^{n-1} = \frac{d}{dx}\left[\frac{x}{(1-x)^2}\right] = \frac{1+x}{(1-x)^3}$

So $\sum_{n=0}^{\infty} n^2 x^n = \frac{x(1+x)}{(1-x)^3}$

At $x=1$ (carefully, using limits): $\sum_{k=0}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$ ✓

---

## 4.8 Transfer Matrix Method (Advanced)

For problems with **state transitions**, represent as a matrix. If $T$ is the transfer matrix and $\mathbf{v}_0$ is the initial state vector, then:

$$\mathbf{v}_n = T^n \mathbf{v}_0$$

The GF is: $\sum_{n=0}^{\infty} \mathbf{v}_n x^n = (I - xT)^{-1} \mathbf{v}_0$

**Application:** Counting binary strings of length $n$ with no two consecutive 1s.

States: $S_0$ (last bit was 0), $S_1$ (last bit was 1)

$$T = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$

This gives the Fibonacci sequence! (Which also counts such strings — beautiful correspondence.)

---

## 4.9 Quick Reference: Important GF Results

| Result | GF |
|--------|-----|
| $p(n)$ (partitions) | $\prod_{k \geq 1} \frac{1}{1-x^k}$ |
| $C_n$ (Catalan) | $\frac{1-\sqrt{1-4x}}{2x}$ |
| $\binom{2n}{n}$ | $\frac{1}{\sqrt{1-4x}}$ |
| $D_n$ (derangements, EGF) | $\frac{e^{-x}}{1-x}$ |
| $F_n$ (Fibonacci) | $\frac{x}{1-x-x^2}$ |
| $n!$ (EGF) | $\frac{1}{1-x}$ |

---

## 4.10 Check Your Understanding

> **Exercise 4.1** — Use the GF for $e^x$ to find $\sum_{n=0}^{\infty} \frac{(-1)^n}{n!}$.
>
> <details><summary>Answer</summary>
>
> Set $x = -1$ in $e^x = \sum \frac{x^n}{n!}$: $\sum \frac{(-1)^n}{n!} = e^{-1} = \frac{1}{e}$
>
> </details>

> **Exercise 4.2** — Using the GF $\frac{x}{1-x-x^2}$, verify that $F_6 = 8$.
>
> <details><summary>Answer</summary>
>
> Expand: $\frac{x}{1-x-x^2} = x + x^2 + 2x^3 + 3x^4 + 5x^5 + 8x^6 + \cdots$
>
> So $[x^6] = 8 = F_6$ ✓
>
> </details>

> **Exercise 4.3 ★** — Prove that $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ using generating functions.
>
> <details><summary>Answer</summary>
>
> $(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$. Set $x = 1$: $2^n = \sum_{k=0}^n \binom{n}{k}$ ✓
>
> </details>

> **Exercise 4.4 ★** — Find the number of ways to tile a $1 \times n$ board with $1 \times 1$ and $1 \times 2$ tiles, using GFs.
>
> <details><summary>Hint</summary>Let $a_n$ = number of tilings. What's the recurrence? (It's Fibonacci!)</details>
> <details><summary>Answer</summary>
>
> $a_n = a_{n-1} + a_{n-2}$, $a_0=1$, $a_1=1$ → Same as Fibonacci.
>
> GF: $\frac{1}{1-x-x^2}$, so $a_n = F_{n+1}$ (Fibonacci shifted by 1)
>
> </details>

---

*→ Continue to [[05 GF Practice]] for comprehensive exam practice.*
