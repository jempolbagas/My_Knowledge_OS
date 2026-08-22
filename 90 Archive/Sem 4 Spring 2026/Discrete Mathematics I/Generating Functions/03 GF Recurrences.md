---
title: GF 03 — Solving Recurrences with Generating Functions
course: Discrete Mathematics I
tags: ["discrete-mathematics", "generating-functions", "recurrences", "homogeneous", "non-homogeneous"]
aliases: ["GF 03 — Solving Recurrences with Generating Functions"]
created: "2026-05-24"
type: Note
topic: Generating Functions
subtopic: Recurrences
week: 11
---

# 03 · Solving Recurrences with Generating Functions

> **← Back to** [[02 GF Ordinary]] | **Next →** [[04 GF Applications]]

---

## 3.1 The Master Strategy

Solving a recurrence with GFs follows a **four-step pipeline** every time:

```
Step 1: TRANSLATE
  Write G(x) = Σ aₙ xⁿ and multiply both sides of the recurrence by xⁿ,
  then sum over all valid n.

Step 2: SIMPLIFY
  Express everything in terms of G(x) using shift identities.
  Use initial conditions to resolve boundary terms.

Step 3: SOLVE
  Solve the resulting algebraic equation for G(x).

Step 4: DECODE
  Use partial fractions / known GF pairs to extract aₙ = [xⁿ] G(x).
```

---

## 3.2 Homogeneous Recurrences

### 3.2.1 First-Order: $a_n = c \cdot a_{n-1}$

**Problem:** Solve $a_n = 2a_{n-1}$, with $a_0 = 1$.

**Step 1 — Translate:**
$$\sum_{n=1}^{\infty} a_n x^n = 2 \sum_{n=1}^{\infty} a_{n-1} x^n$$

$$G(x) - a_0 = 2x \cdot G(x)$$

**Step 2 — Simplify:**
$$G(x) - 1 = 2x G(x)$$

**Step 3 — Solve:**
$$G(x)(1 - 2x) = 1 \implies G(x) = \frac{1}{1-2x}$$

**Step 4 — Decode:**
$$[x^n]\frac{1}{1-2x} = 2^n \implies \boxed{a_n = 2^n}$$

---

### 3.2.2 Second-Order Homogeneous

**Problem:** Solve $a_n = 5a_{n-1} - 6a_{n-2}$, with $a_0 = 0$, $a_1 = 1$.

**Step 1 — Translate:** Multiply by $x^n$ and sum for $n \geq 2$:

**Step 1 — Translate:** Multiply by $x^n$ and sum for $n \geq 2$:

$$\sum_{n=2}^{\infty} a_n x^n = 5 \sum_{n=2}^{\infty} a_{n-1} x^n - 6 \sum_{n=2}^{\infty} a_{n-2} x^n$$

**Step 2 — De-mystify Shifting (Step-by-step expansion):**

To understand how each summation converts into $G(x) = \sum_{n=0}^{\infty} a_n x^n$, let's write out the terms of each sum explicitly:

*   **Left-Hand Side (LHS):**
    $$\sum_{n=2}^{\infty} a_n x^n = a_2 x^2 + a_3 x^3 + a_4 x^4 + \cdots$$
    Notice that this is just the entire generating function $G(x)$ missing its first two terms ($a_0$ and $a_1 x$). Thus:
    $$\sum_{n=2}^{\infty} a_n x^n = G(x) - a_0 - a_1 x$$
    Plugging in the initial conditions $a_0 = 0$ and $a_1 = 1$:
    $$\text{LHS} = G(x) - x$$

*   **First sum on the Right-Hand Side (RHS):**
    $$5 \sum_{n=2}^{\infty} a_{n-1} x^n = 5(a_1 x^2 + a_2 x^3 + a_3 x^4 + \cdots)$$
    We can pull out one factor of $x$ to match the power of $x$ to the index of $a$:
    $$= 5x (a_1 x^1 + a_2 x^2 + a_3 x^3 + \cdots)$$
    The expression in the parentheses is the entire generating function $G(x)$ missing its very first term $a_0$. Thus:
    $$= 5x(G(x) - a_0)$$
    Since $a_0 = 0$:
    $$\text{First Sum} = 5xG(x)$$

*   **Second sum on the RHS:**
    $$-6 \sum_{n=2}^{\infty} a_{n-2} x^n = -6(a_0 x^2 + a_1 x^3 + a_2 x^4 + \cdots)$$
    We can pull out $x^2$ to match the power of $x$ to the index of $a$:
    $$= -6x^2 (a_0 + a_1 x + a_2 x^2 + \cdots)$$
    The expression in the parentheses is exactly $G(x)$! Thus:
    $$\text{Second Sum} = -6x^2 G(x)$$

Plugging these back into the translated equation:
$$G(x) - x = 5xG(x) - 6x^2 G(x)$$

**Step 3 — Solve for $G(x)$:**
$$G(x) - 5xG(x) + 6x^2 G(x) = x$$
$$G(x)(1 - 5x + 6x^2) = x$$
$$G(x) = \frac{x}{1 - 5x + 6x^2} = \frac{x}{(1-2x)(1-3x)}$$

**Step 4 — Partial fractions:**
$$\frac{x}{(1-2x)(1-3x)} = \frac{A}{1-2x} + \frac{B}{1-3x}$$

Multiply both sides by $(1-2x)(1-3x)$ to get the polynomial equation:
$$x = A(1-3x) + B(1-2x)$$
- Set $x = \frac{1}{2}$ (to eliminate $B$):
  $$\frac{1}{2} = A\left(1 - \frac{3}{2}\right) \implies \frac{1}{2} = A\left(-\frac{1}{2}\right) \implies A = -1$$
- Set $x = \frac{1}{3}$ (to eliminate $A$):
  $$\frac{1}{3} = B\left(1 - \frac{2}{3}\right) \implies \frac{1}{3} = B\left(\frac{1}{3}\right) \implies B = 1$$

Substitute $A$ and $B$ back into the partial fractions:
$$G(x) = \frac{-1}{1-2x} + \frac{1}{1-3x} = -\sum_{n=0}^{\infty} 2^n x^n + \sum_{n=0}^{\infty} 3^n x^n$$

Extract the coefficient of $x^n$:
$$\boxed{a_n = 3^n - 2^n}$$

**Verification:** $a_0 = 3^0 - 2^0 = 0$ ✓, $a_1 = 3^1 - 2^1 = 1$ ✓, $a_2 = 9 - 4 = 5$. Check recurrence: $a_2 = 5a_1 - 6a_0 = 5(1) - 6(0) = 5$ ✓

---

### 3.2.3 The Fibonacci Sequence

**Problem:** Solve $F_n = F_{n-1} + F_{n-2}$, with $F_0 = 0$, $F_1 = 1$.

**Translate & Simplify:**
Following the same shifting steps as above for $n \geq 2$:
$$G(x) - F_0 - F_1 x = x(G(x) - F_0) + x^2 G(x)$$
$$G(x) - x = xG(x) + x^2 G(x)$$
$$G(x)(1 - x - x^2) = x$$
$$G(x) = \frac{x}{1 - x - x^2}$$

**Factoring the Denominator (Golden Ratio algebra):**
We want to factor $1 - x - x^2$ as $(1 - r_1 x)(1 - r_2 x) = 1 - (r_1 + r_2)x + r_1 r_2 x^2$. 
Comparing coefficients with $1 - x - x^2$:
- $r_1 + r_2 = 1$
- $r_1 r_2 = -1$

These roots $r_1$ and $r_2$ are the solutions to the quadratic equation $r^2 - r - 1 = 0$:
$$r = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(-1)}}{2} = \frac{1 \pm \sqrt{5}}{2}$$

Let $\phi = \frac{1+\sqrt{5}}{2}$ (the Golden Ratio $\approx 1.618$) and $\hat{\phi} = \frac{1-\sqrt{5}}{2}$ ($\approx -0.618$). 
Thus, our denominator factors perfectly as:
$$1 - x - x^2 = (1 - \phi x)(1 - \hat{\phi} x)$$

Now, we set up partial fractions:
$$G(x) = \frac{x}{(1 - \phi x)(1 - \hat{\phi} x)} = \frac{A}{1 - \phi x} + \frac{B}{1 - \hat{\phi} x}$$
Multiply by the denominator:
$$x = A(1 - \hat{\phi} x) + B(1 - \phi x)$$
- Set $x = \frac{1}{\phi}$:
  $$\frac{1}{\phi} = A\left(1 - \frac{\hat{\phi}}{\phi}\right) = A\left(\frac{\phi - \hat{\phi}}{\phi}\right) \implies 1 = A(\phi - \hat{\phi})$$
  Since $\phi - \hat{\phi} = \frac{1+\sqrt{5}}{2} - \frac{1-\sqrt{5}}{2} = \sqrt{5}$, we get $A = \frac{1}{\sqrt{5}}$.
- Set $x = \frac{1}{\hat{\phi}}$:
  $$\frac{1}{\hat{\phi}} = B\left(1 - \frac{\phi}{\hat{\phi}}\right) = B\left(\frac{\hat{\phi} - \phi}{\hat{\phi}}\right) \implies 1 = B(\hat{\phi} - \phi) = -B(\phi - \hat{\phi}) \implies B = -\frac{1}{\sqrt{5}}$$

So, the generating function is:
$$G(x) = \frac{1}{\sqrt{5}}\left(\frac{1}{1-\phi x} - \frac{1}{1-\hat{\phi} x}\right)$$

**Decode:**
Expand each term:
$$G(x) = \frac{1}{\sqrt{5}} \sum_{n=0}^{\infty} \phi^n x^n - \frac{1}{\sqrt{5}} \sum_{n=0}^{\infty} \hat{\phi}^n x^n$$

Extract the coefficient:
$$\boxed{F_n = \frac{\phi^n - \hat{\phi}^n}{\sqrt{5}} = \frac{\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n}{\sqrt{5}}}$$

This is **Binet's Formula** — derived purely and mechanically from generating functions! 🎉

---

## 3.3 Non-Homogeneous Recurrences

Non-homogeneous recurrences have the form:
$$a_n = f(a_{n-1}, a_{n-2}, \ldots) + g(n)$$
where $g(n) \neq 0$ is the non-homogeneous "forcing" term.

### 3.3.1 Constant Non-Homogeneous Term

**Problem:** Solve $a_n = 2a_{n-1} + 1$, with $a_0 = 0$.

**Step 1 — Translate:** Summing $a_n x^n$ for $n \geq 1$:
$$G(x) - a_0 = 2x G(x) + \sum_{n=1}^{\infty} 1 \cdot x^n$$
$$G(x) - 0 = 2x G(x) + \frac{x}{1-x}$$

**Step 3 — Solve:**
$$G(x)(1 - 2x) = \frac{x}{1-x} \implies G(x) = \frac{x}{(1-x)(1-2x)}$$

**Step 4 — Partial fractions:**
$$\frac{x}{(1-x)(1-2x)} = \frac{A}{1-x} + \frac{B}{1-2x}$$

$$x = A(1-2x) + B(1-x)$$
- Set $x=1$: $1 = A(-1) \implies A = -1$
- Set $x=\frac{1}{2}$: $\frac{1}{2} = B\left(\frac{1}{2}\right) \implies B = 1$

$$G(x) = \frac{-1}{1-x} + \frac{1}{1-2x} \implies \boxed{a_n = 2^n - 1}$$

Check: $a_0 = 0$ ✓, $a_1 = 2(0)+1 = 1$ ✓, $a_2 = 2(1)+1 = 3 = 4-1$ ✓

---

### 3.3.2 Linear Non-Homogeneous Term

**Problem:** Solve $a_n = 2a_{n-1} + n$, with $a_0 = 1$.

**Step 1 — Translate:**
Summing $a_n x^n$ for $n \geq 1$:
$$G(x) - a_0 = 2xG(x) + \sum_{n=1}^{\infty} n x^n$$
Since $a_0 = 1$ and $\sum_{n=1}^{\infty} n x^n = \frac{x}{(1-x)^2}$ (from Pattern P5):
$$G(x) - 1 = 2xG(x) + \frac{x}{(1-x)^2}$$

**Step 2 — Solve:**
$$G(x)(1-2x) = 1 + \frac{x}{(1-x)^2}$$
$$G(x) = \frac{1}{1-2x} + \frac{x}{(1-2x)(1-x)^2}$$

Let's combine these terms under a single denominator:
$$G(x) = \frac{(1-x)^2 + x}{(1-2x)(1-x)^2} = \frac{1 - 2x + x^2 + x}{(1-2x)(1-x)^2} = \frac{1 - x + x^2}{(1-2x)(1-x)^2}$$

**Step 3 — Partial Fraction Decomposition (Repeated Root):**
Because of the squared term $(1-x)^2$ in the denominator, our partial fraction template must include terms for both the first power and the second power:
$$\frac{1 - x + x^2}{(1-2x)(1-x)^2} = \frac{A}{1-2x} + \frac{B}{1-x} + \frac{C}{(1-x)^2}$$

Multiply both sides by $(1-2x)(1-x)^2$ to get the polynomial equation:
$$1 - x + x^2 = A(1-x)^2 + B(1-x)(1-2x) + C(1-2x)$$

Now we solve for the constants:
- **To find $C$:** Set $x = 1$ (eliminates $A$ and $B$):
  $$1 - 1 + 1^2 = A(0) + B(0) + C(1-2(1)) \implies 1 = -C \implies C = -1$$
- **To find $A$:** Set $x = \frac{1}{2}$ (eliminates $B$ and $C$):
  $$1 - \frac{1}{2} + \left(\frac{1}{2}\right)^2 = A\left(1-\frac{1}{2}\right)^2 \implies \frac{3}{4} = A\left(\frac{1}{4}\right) \implies A = 3$$
- **To find $B$:** Plug in any other convenient value, say $x = 0$, along with our known $A=3$ and $C=-1$:
  $$1 - 0 + 0^2 = 3(1-0)^2 + B(1-0)(1-2(0)) - 1(1-2(0))$$
  $$1 = 3 + B - 1 \implies 1 = 2 + B \implies B = -1$$

Substitute the constants back:
$$G(x) = \frac{3}{1-2x} - \frac{1}{1-x} - \frac{1}{(1-x)^2}$$

**Step 4 — Decode:**
Expand each term:
- $\frac{3}{1-2x} = 3 \sum_{n=0}^{\infty} 2^n x^n$
- $-\frac{1}{1-x} = - \sum_{n=0}^{\infty} x^n$
- $-\frac{1}{(1-x)^2} = - \sum_{n=0}^{\infty} (n+1) x^n$ (from Pattern P4)

Extracting the coefficient of $x^n$:
$$a_n = 3 \cdot 2^n - 1 - (n+1)$$
$$\boxed{a_n = 3 \cdot 2^n - n - 2}$$

**Verification:**
- $a_0 = 3 \cdot 2^0 - 0 - 2 = 1$ ✓
- $a_1 = 3 \cdot 2^1 - 1 - 2 = 3$. Recurrence: $2a_0 + 1 = 2(1) + 1 = 3$ ✓
- $a_2 = 3 \cdot 2^2 - 2 - 2 = 8$. Recurrence: $2a_1 + 2 = 2(3) + 2 = 8$ ✓

---

### 3.3.3 Exponential Non-Homogeneous Term

**Problem:** Solve $a_n = 3a_{n-1} + 2^n$, with $a_0 = 1$.

**Translate:** $G(x) - 1 = 3xG(x) + \sum_{n=1}^{\infty} 2^n x^n$

$\sum_{n=0}^{\infty} 2^n x^n = \frac{1}{1-2x}$, so $\sum_{n=1}^{\infty} 2^n x^n = \frac{1}{1-2x} - 1 = \frac{2x}{1-2x}$

**Solve:**
$$G(x) - 1 = 3xG(x) + \frac{2x}{1-2x}$$
$$G(x)(1-3x) = 1 + \frac{2x}{1-2x} = \frac{1-2x+2x}{1-2x} = \frac{1}{1-2x}$$
$$G(x) = \frac{1}{(1-2x)(1-3x)}$$

**Partial fractions:** (same pattern as before)
$$G(x) = \frac{-1}{1-2x} + \frac{2}{1-3x} \implies \boxed{a_n = -2^n + 2 \cdot 3^n}$$

Wait, check $a_0$: $-1 + 2 = 1$ ✓, $a_1$: $-2 + 6 = 4 = 3(1) + 2 = 5$? Let me recheck... $a_1 = 3(1) + 2^1 = 5$, but formula gives $4$. Let me recompute... 

Actually $a_0 = 1$, $a_1 = 3(1)+2 = 5$. Formula: $-2^1 + 2\cdot 3^1 = -2+6=4 \neq 5$. Something is off — redo the partial fractions carefully:

$\frac{1}{(1-2x)(1-3x)} = \frac{A}{1-2x} + \frac{B}{1-3x}$

$1 = A(1-3x) + B(1-2x)$
- $x=\frac{1}{2}$: $1 = A \cdot (-\frac{1}{2}) \Rightarrow A = -2$
- $x=\frac{1}{3}$: $1 = B \cdot (\frac{1}{3}) \Rightarrow B = 3$

$$G(x) = \frac{-2}{1-2x} + \frac{3}{1-3x} \implies a_n = -2 \cdot 2^n + 3 \cdot 3^n = 3^{n+1} - 2^{n+1}$$

Check: $a_0 = 3-2=1$ ✓, $a_1 = 9-4 = 5$ ✓ ✓

> **Lesson:** Always verify with initial conditions!

---

## 3.4 Summary: Recurrence → GF Translation Cheatsheet

| Recurrence Term | GF Contribution |
|----------------|----------------|
| $a_n$ | $G(x)$ |
| $a_{n-1}$ | $xG(x)$ (with $a_0$ correction) |
| $a_{n-2}$ | $x^2 G(x)$ (with $a_0, a_1$ corrections) |
| Constant $c$ | $\frac{cx}{1-x}$ (for $n \geq 1$) |
| $n$ | $\frac{x}{(1-x)^2}$ (for $n \geq 1$) |
| $n^2$ | $\frac{x(1+x)}{(1-x)^3}$ |
| $c^n$ | $\frac{cx}{1-cx}$ (for $n \geq 1$) |

### Correction Terms for Shifts

When shifting, you must subtract out the "extra" terms:

$$\sum_{n=k}^{\infty} a_{n-k} x^n = x^k G(x)$$

$$\sum_{n=k}^{\infty} a_n x^n = G(x) - a_0 - a_1 x - \cdots - a_{k-1} x^{k-1}$$

---

## 3.5 Practice Problems

> **Exercise 3.1** — Solve $a_n = 4a_{n-1} - 4a_{n-2}$, $a_0 = 1$, $a_1 = 4$.
>
> *(Hint: The denominator has a repeated root.)*
>
> <details><summary>Answer</summary>
>
> $G(x) = \frac{1}{(1-2x)^2}$, so $a_n = (n+1)2^n$
>
> Check: $a_0=1$ ✓, $a_1=4$ ✓, $a_2=4(4)-4(1)=12=3\cdot4$ ✓
>
> </details>

> **Exercise 3.2** — Solve $a_n = a_{n-1} + 2$, $a_0 = 3$.
>
> <details><summary>Answer</summary>
>
> Translate: $G(x) - 3 = xG(x) + \frac{2x}{1-x}$
>
> $G(x) = \frac{3}{1-x} + \frac{2x}{(1-x)^2}$
>
> Decode: $a_n = 3 + 2n$
>
> </details>

> **Exercise 3.3 ★** — Solve the Fibonacci recurrence with $F_0 = 1$, $F_1 = 1$.
>
> <details><summary>Hint</summary>Same recurrence, different initial conditions will shift the GF.</details>
> <details><summary>Answer</summary>
>
> $G(x) = \frac{1}{1-x-x^2}$
>
> This gives the "offset" Fibonacci: $1, 1, 2, 3, 5, 8, \ldots$
>
> </details>

---

*→ Continue to [[04 GF Applications]] for power series and Taylor series connections.*
