---
title: GF 05 — Practice Problem Bank
course: Discrete Mathematics I
tags: ["discrete-mathematics", "generating-functions", "practice", "exam-prep", "problems"]
aliases: ["GF 05 — Practice Problem Bank"]
created: "2026-05-24"
type: Note
topic: Generating Functions
subtopic: Practice
---

# 05 · Practice Problem Bank

> **← Back to** [[04 GF Applications]] | **Home →** [[00 GF Index]]

> **How to use this note:** Cover the solutions and work each problem on paper first. The problems are ordered by increasing difficulty within each section. ★ = exam-level difficulty.

---

## Section A — Foundations (Warm-Up)

### A1. Sequence → GF

Find the OGF for each sequence. Simplify to a closed form.

| # | Sequence $a_n$ | GF |
|---|---------------|-----|
| A1.1 | $a_n = 4^n$ | ? |
| A1.2 | $a_n = (-3)^n$ | ? |
| A1.3 | $a_n = n$ | ? |
| A1.4 | $a_n = 2n + 1$ | ? |
| A1.5 | $a_n = 0$ for $n<3$; $1$ for $n \geq 3$ | ? |

<details><summary>Solutions A1</summary>

| # | GF |
|---|-----|
| A1.1 | $\frac{1}{1-4x}$ |
| A1.2 | $\frac{1}{1+3x}$ |
| A1.3 | $\frac{x}{(1-x)^2}$ |
| A1.4 | $\frac{2x}{(1-x)^2} + \frac{1}{1-x} = \frac{1+x}{(1-x)^2}$ |
| A1.5 | $\frac{x^3}{1-x}$ |

</details>

---

### A2. GF → Sequence

Find the sequence $a_n = [x^n] G(x)$.

| # | $G(x)$ | $a_n$ |
|---|--------|-------|
| A2.1 | $\frac{1}{1-5x}$ | ? |
| A2.2 | $\frac{2}{1+x}$ | ? |
| A2.3 | $\frac{1}{(1-x)^4}$ | ? |
| A2.4 | $\frac{x^3}{1-2x}$ | ? |
| A2.5 | $\frac{3}{(1-x)^2}$ | ? |

<details><summary>Solutions A2</summary>

| # | $a_n$ |
|---|-------|
| A2.1 | $5^n$ |
| A2.2 | $2(-1)^n$ |
| A2.3 | $\binom{n+3}{3}$ |
| A2.4 | $2^{n-3}$ for $n \geq 3$; $0$ otherwise |
| A2.5 | $3(n+1)$ |

</details>

---

## Section B — OGF Operations

### B1. Partial Fractions

Find $[x^n] G(x)$ using partial fractions.

**B1.1:** $G(x) = \dfrac{1}{(1-x)(1-3x)}$

<details><summary>Solution</summary>

$\frac{1}{(1-x)(1-3x)} = \frac{A}{1-x} + \frac{B}{1-3x}$

$1 = A(1-3x)+B(1-x)$: $A = -\frac{1}{2}$, $B = \frac{3}{2}$

$a_n = -\frac{1}{2} + \frac{3}{2} \cdot 3^n = \frac{3^{n+1}-1}{2}$

</details>

**B1.2:** $G(x) = \dfrac{2x-1}{(1-x)(1-4x)}$

<details><summary>Solution</summary>

$\frac{2x-1}{(1-x)(1-4x)} = \frac{A}{1-x} + \frac{B}{1-4x}$

$2x-1 = A(1-4x)+B(1-x)$
- $x=1$: $1=A(-3) \Rightarrow A=-\frac{1}{3}$
- $x=\frac{1}{4}$: $-\frac{1}{2} = B(\frac{3}{4}) \Rightarrow B = -\frac{2}{3}$

$a_n = -\frac{1}{3} - \frac{2}{3}\cdot 4^n$

</details>

**B1.3 ★:** $G(x) = \dfrac{1}{(1-x)^2(1-2x)}$

<details><summary>Solution</summary>

$\frac{1}{(1-x)^2(1-2x)} = \frac{A}{1-x} + \frac{B}{(1-x)^2} + \frac{C}{1-2x}$

$1 = A(1-x)(1-2x) + B(1-2x) + C(1-x)^2$
- $x=1$: $1=B(-1) \Rightarrow B=-1$
- $x=\frac{1}{2}$: $1=C(\frac{1}{4}) \Rightarrow C=4$
- $x=0$: $1=A+B+C=A-1+4 \Rightarrow A=-2$

$G(x) = \frac{-2}{1-x} + \frac{-1}{(1-x)^2} + \frac{4}{1-2x}$

$[x^n]: -2 - (n+1) + 4\cdot 2^n = 2^{n+2} - n - 3$

</details>

---

### B2. Operations on GFs

**B2.1:** Find the GF for $b_n = (n+2) \cdot 3^n$.

<details><summary>Solution</summary>

Start: $\frac{1}{1-3x} = \sum 3^n x^n$

Differentiate: $\frac{3}{(1-3x)^2} = \sum n \cdot 3^{n-1} x^{n-1}$

Multiply by $3x$: $\frac{9x}{(1-3x)^2} = \sum n \cdot 3^n x^n$

We want $\sum (n+2) 3^n x^n = \sum n \cdot 3^n x^n + 2 \sum 3^n x^n$:

$G(x) = \frac{9x}{(1-3x)^2} + \frac{2}{1-3x} = \frac{9x + 2(1-3x)}{(1-3x)^2} = \frac{2+3x}{(1-3x)^2}$

</details>

**B2.2 ★:** Find $[x^n]$ for $G(x) = \ln\left(\frac{1}{1-x}\right)$.

<details><summary>Solution</summary>

$-\ln(1-x) = \sum_{n=1}^{\infty} \frac{x^n}{n}$

So $[x^n] \ln\frac{1}{1-x} = \frac{1}{n}$ for $n \geq 1$, and $0$ for $n=0$.

</details>

---

## Section C — Recurrences

### C1. First-Order

**C1.1:** Solve $a_n = 5a_{n-1}$, $a_0 = 2$.

<details><summary>Answer</summary>$a_n = 2 \cdot 5^n$</details>

**C1.2:** Solve $a_n = -2a_{n-1} + 6$, $a_0 = 1$.

<details><summary>Solution</summary>

Translate: $G - 1 = -2xG + \frac{6x}{1-x}$

$G(1+2x) = 1 + \frac{6x}{1-x} = \frac{1+5x}{1-x}$

$G = \frac{1+5x}{(1-x)(1+2x)}$

Partial fractions: $\frac{A}{1-x} + \frac{B}{1+2x}$

$1+5x = A(1+2x)+B(1-x)$
- $x=1$: $6=3A \Rightarrow A=2$
- $x=-\frac{1}{2}$: $-\frac{3}{2}=\frac{3B}{2} \Rightarrow B=-1$

$a_n = 2 - (-2)^n$

</details>

---

### C2. Second-Order

**C2.1:** Solve $a_n = 6a_{n-1} - 9a_{n-2}$, $a_0 = 1$, $a_1 = 6$.

*(Hint: repeated root — use $\frac{A}{1-cx} + \frac{Bx}{(1-cx)^2}$ form)*

<details><summary>Solution</summary>

$G - 1 - 6x = 6x(G-1) - 9x^2 G$

$G(1 - 6x + 9x^2) = 1$

$G = \frac{1}{(1-3x)^2}$

$a_n = (n+1) 3^n$

Check: $a_0=1$ ✓, $a_1=2\cdot3=6$ ✓, $a_2 = 6(6)-9(1)=27=3\cdot9$ ✓

</details>

**C2.2 ★:** Solve $a_n = 4a_{n-1} - 3a_{n-2} + 2^n$, $a_0 = 0$, $a_1 = 1$.

<details><summary>Solution outline</summary>

Translate: $G - x = 4x(G) - 3x^2 G + \left(\frac{1}{1-2x}-1\right)$

Wait, be careful about the sum starting index. Sum for $n \geq 2$:

$G - a_0 - a_1 x = 4x(G - a_0) - 3x^2 G + \sum_{n=2}^{\infty} 2^n x^n$

$G - x = 4xG - 3x^2 G + \frac{4x^2}{1-2x}$

$G(1-4x+3x^2) = x + \frac{4x^2}{1-2x}$

$G = \frac{x}{(1-x)(1-3x)} + \frac{4x^2}{(1-2x)(1-x)(1-3x)}$

Apply partial fractions to each term (left as extended exercise).

</details>

---

### C3. Mixed Exam Problems

**C3.1 ★:** Let $a_0 = 1$ and $a_n = a_{n-1} + n$ for $n \geq 1$. Find a closed form for $a_n$.

<details><summary>Solution</summary>

$G - 1 = xG + \frac{x}{(1-x)^2}$

$G = \frac{1}{1-x} + \frac{x}{(1-x)^3}$

$[x^n]: 1 + [x^{n-1}]\frac{1}{(1-x)^3} = 1 + \binom{n+1}{2} = 1 + \frac{n(n+1)}{2} = \frac{n^2+n+2}{2}$

Check: $a_0=1$ ✓, $a_1=1+1=2=\frac{1+1+2}{2}=2$ ✓, $a_2=2+2=4=\frac{4+2+2}{2}=4$ ✓

</details>

**C3.2 ★★:** Find the number of sequences of $n$ coin flips (H/T) with no two consecutive heads.

<details><summary>Solution</summary>

Let $a_n$ = number of such sequences.

Recurrence: $a_n = a_{n-1} + a_{n-2}$ (if last flip is T, use $a_{n-1}$; if last is H, prev must be T, use $a_{n-2}$)

With $a_0=1$ (empty sequence), $a_1=2$ (H or T).

$G(x) = \frac{1+x}{1-x-x^2}$ → This is the Fibonacci sequence shifted: $a_n = F_{n+2}$

</details>

---

## Section D — Applications

**D1.** In how many ways can you make $n$ cents using coins of 1¢, 2¢, and 5¢? Write the GF (don't expand).

<details><summary>Answer</summary>

$G(x) = \frac{1}{(1-x)(1-x^2)(1-x^5)}$

</details>

**D2.** Find the coefficient of $x^{10}$ in $\frac{1}{(1-x)^3}$.

<details><summary>Answer</summary>

$[x^{10}]\frac{1}{(1-x)^3} = \binom{10+2}{2} = \binom{12}{2} = 66$

</details>

**D3 ★.** Prove using GFs: $\sum_{k=0}^{n} k \binom{n}{k} = n \cdot 2^{n-1}$

<details><summary>Solution</summary>

$(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$

Differentiate: $n(1+x)^{n-1} = \sum_{k=1}^n k\binom{n}{k} x^{k-1}$

Set $x=1$: $n \cdot 2^{n-1} = \sum_{k=0}^n k\binom{n}{k}$ ✓

</details>

**D4 ★★.** Using GFs, find a closed form for the $n$-th Catalan number $C_n$.

<details><summary>Solution</summary>

Catalan numbers satisfy $C_n = \sum_{k=0}^{n-1} C_k C_{n-1-k}$ with $C_0=1$.

Translates to: $C(x) = xC(x)^2 + 1$

Solve quadratic: $xC^2 - C + 1 = 0 \Rightarrow C = \frac{1 \pm \sqrt{1-4x}}{2x}$

Taking the $-$ branch (so $C(0)=1$): $C(x) = \frac{1-\sqrt{1-4x}}{2x}$

From the generalized binomial theorem:
$\sqrt{1-4x} = \sum_{n=0}^{\infty} \binom{1/2}{n}(-4x)^n$

After careful computation: $C_n = \frac{1}{n+1}\binom{2n}{n}$

</details>

---

## Exam Readiness Checklist

- [ ] I can construct a GF from a sequence (and vice versa)
- [ ] I can use shift, differentiation, and convolution operations
- [ ] I can apply partial fraction decomposition to rational GFs
- [ ] I can apply the 4-step pipeline to solve first-order recurrences
- [ ] I can apply the 4-step pipeline to solve second-order recurrences
- [ ] I can handle non-homogeneous terms (constant, linear, exponential)
- [ ] I can use GFs to count combinatorial objects
- [ ] I can connect GFs to power series (Taylor series, $e^x$, $\ln$)
- [ ] I can verify solutions by checking initial conditions and spot-checking terms
- [ ] I know the Fibonacci GF and can derive Binet's formula

---

*→ Return to [[00 GF Index]] for the full overview.*
