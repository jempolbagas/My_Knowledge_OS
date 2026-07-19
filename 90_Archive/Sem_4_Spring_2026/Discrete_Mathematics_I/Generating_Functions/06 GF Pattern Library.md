---
title: "GF 06 — Pattern Library & Derivations"
course: Discrete Mathematics I
tags: ["discrete-mathematics", "generating-functions", "patterns", "derivations", "reference"]
aliases: ["GF 06 — Pattern Library & Derivations"]
created: "2026-05-24"
type: Note
topic: Generating Functions
subtopic: Pattern Library
---

# 06 · Pattern Library & Derivations

> **Home →** [[00 GF Index]]

> **How to use this note:** Every sequence→GF pattern used in this module is derived here from first principles. When you see a closed-form GF and wonder *"where did that come from?"*, this is where to look.

---

## The Foundation: One Identity to Rule Them All

Every pattern in this library is ultimately derived from a single identity:

$$\boxed{\sum_{n=0}^{\infty} x^n = \frac{1}{1-x}}$$

We obtain new patterns by applying four operations to this base:
1. **Substitution** — replace $x$ with something else
2. **Scaling** — multiply by a constant
3. **Shifting** — multiply by $x^k$
4. **Differentiation / Integration** — with respect to $x$

The table below summarizes all patterns. Each has a 🔗 link to its full derivation below.

---

## Quick Reference Table (with Derivation Links)

| #   | Sequence $a_n$                                  | GF $G(x) = \sum a_n x^n$  | Core Trick                                                                |
| --- | ----------------------------------------------- | ------------------------- | ------------------------------------------------------------------------- |
| P1  | $1$                                             | $\frac{1}{1-x}$           | [[#P1 — The Constant Sequence $a_n = 1$  \| Base Identity]]           |
| P2  | $c^n$                                           | $\frac{1}{1-cx}$          | [[#P2 — Powers of a Constant $a_n = c^n$  \| Substitution: x --> cx]] |
| P3  | $(-1)^n$                                        | $\frac{1}{1+x}$           | [[#P3 — Alternating Signs $a_n = (-1) n$ \| Substitution: x --> -x]] |
| P4  | $n+1$                                           | $\frac{1}{(1-x)^2}$       | [[#P4 — Counting Up $a_n = n+1$ \| Differentiation of P1]]|
| P5  | $n$                                             | $\frac{x}{(1-x)^2}$       | [[#P5 — Natural Numbers $a_n = n$  \| Shift P4 left by 1]]|
| P6  | $\binom{n+k-1}{k-1}$                            | $\frac{1}{(1-x)^k}$       | [[#P6 — Generalised Binomial Coefficients $a_n = binom{n+k-1}{k-1}$  \| Generalised binomial / k-fold product]]|
| P7  | $n \cdot c^{n-1}$                               | $\frac{1}{(1-cx)^2}$      | [[#P7 — Weighted Powers $a_n = n cdot c {n-1}$\|Differentiation of P2]]                                              |
| P8  | $n \cdot c^n$                                   | $\frac{cx}{(1-cx)^2}$     | [[#P8 — Scaled Weighted Powers $a_n = n cdot c n$ \|Scale P7 by cx]]                                                   |
| P9  | $0,0,\ldots,0,1,1,1,\ldots$ ($k$ leading zeros) | $\frac{x^k}{1-x}$         | [[#P9 — Delayed Constant $k$ Leading Zeros \|Right-shift P1 by k]]                                           |
| P10 | $1,0,1,0,1,\ldots$ (alternating 1,0)            | $\frac{1}{1-x^2}$         | [[#P10 — Every Other Term $a_n = 1$ if $n$ even, $0$ if $n$ odd \|Substitution: x --> x^2]]                                     |
| P11 | $\binom{n}{r}$ (fixed $r$)                      | $\frac{x^r}{(1-x)^{r+1}}$ | [[#P11 — Binomial Coefficients $a_n = binom{n}{r}$ (fixed $r$) \| Product of shifts]]|
| P12 | $F_n$ (Fibonacci)                               | $\frac{x}{1-x-x^2}$       | [[#P12 — Fibonacci Sequence $F_0=0, F_1=1, F_n = F_{n-1}+F_{n-2}$ \|Recurrence translation]]                                            |

---

## Full Derivations

---

### P1 — The Constant Sequence $a_n = 1$ 

$$\sum_{n=0}^{\infty} 1 \cdot x^n = 1 + x + x^2 + x^3 + \cdots = \frac{1}{1-x}$$

**Why this works:** Let $S = 1 + x + x^2 + \cdots$. Multiply by $x$:
$$xS = x + x^2 + x^3 + \cdots$$
Subtract: $S - xS = 1$, so $S(1-x) = 1$, giving $S = \frac{1}{1-x}$.

**Intuition:** An infinite geometric series with ratio $x$. This is the algebraic fact $\frac{1-x^n}{1-x} \to \frac{1}{1-x}$ as $n \to \infty$ (for $|x|<1$, but formally always).

$$\boxed{\sum_{n=0}^{\infty} x^n = \frac{1}{1-x}}$$

---

### P2 — Powers of a Constant: $a_n = c^n$ 

$$\sum_{n=0}^{\infty} c^n x^n = \sum_{n=0}^{\infty} (cx)^n = \frac{1}{1-cx}$$

**Derivation:** Simply substitute $cx$ in place of $x$ in P1:

$$\frac{1}{1-x}\bigg|_{x \mapsto cx} = \frac{1}{1-cx}$$

Since $\sum x^n = \frac{1}{1-x}$, replacing $x$ with $cx$ gives $\sum (cx)^n = \frac{1}{1-cx}$, and $(cx)^n = c^n x^n$.

**Intuition:** The sequence $1, c, c^2, c^3, \ldots$ is still a geometric series, just with ratio $c$ instead of $1$. The GF "encodes" the ratio $c$ by replacing $x$ with $cx$.

$$\boxed{\sum_{n=0}^{\infty} c^n x^n = \frac{1}{1-cx}}$$

**Examples:**

| Sequence | Substitution | GF |
|----------|-------------|-----|
| $2^n$ | $c=2$ | $\frac{1}{1-2x}$ |
| $3^n$ | $c=3$ | $\frac{1}{1-3x}$ |
| $\left(\frac{1}{2}\right)^n$ | $c=\frac{1}{2}$ | $\frac{1}{1-x/2} = \frac{2}{2-x}$ |

---

### P3 — Alternating Signs: $a_n = (-1)^n$ 

$$\sum_{n=0}^{\infty} (-1)^n x^n = \sum_{n=0}^{\infty} (-x)^n = \frac{1}{1+x}$$

**Derivation:** Substitute $x \mapsto -x$ in P1:

$$\frac{1}{1-(-x)} = \frac{1}{1+x}$$

and $(-x)^n = (-1)^n x^n$, so the coefficient of $x^n$ is $(-1)^n$.

**Intuition:** The $(-1)^n$ factor "flips the sign of $x$". Every odd-power term becomes negative.

$$\boxed{\sum_{n=0}^{\infty} (-1)^n x^n = \frac{1}{1+x}}$$

**Generalization:** $\sum (-c)^n x^n = \frac{1}{1+cx}$ by combining P2 and P3 (substitute $x \mapsto -cx$).

---

### P4 — Counting Up: $a_n = n+1$ 

$$\sum_{n=0}^{\infty} (n+1) x^n = \frac{1}{(1-x)^2}$$

**Derivation:** Differentiate P1 with respect to $x$:

$$\frac{d}{dx}\left[\frac{1}{1-x}\right] = \frac{1}{(1-x)^2}$$

$$\frac{d}{dx}\left[\sum_{n=0}^{\infty} x^n\right] = \sum_{n=1}^{\infty} n x^{n-1} = \sum_{n=0}^{\infty} (n+1) x^n$$

So both sides must be equal: $\frac{1}{(1-x)^2} = \sum_{n=0}^{\infty} (n+1) x^n$.

**Intuition:** When you differentiate a power series, you "bring down" the exponent as a multiplier. The exponent of $x^n$ is $n$, so differentiation multiplies each term by $n$ and reduces the power by 1. Re-indexing makes it $n+1$.

$$\boxed{\sum_{n=0}^{\infty} (n+1) x^n = \frac{1}{(1-x)^2}}$$

**Memory aid:** $\frac{1}{(1-x)^2}$ has a "squared" denominator → the sequence grows *linearly* (degree 1), one step faster than the constant sequence from $\frac{1}{1-x}$.

---

### P5 — Natural Numbers: $a_n = n$ 

$$\sum_{n=0}^{\infty} n \cdot x^n = \frac{x}{(1-x)^2}$$

**Derivation (Method 1 — shift P4):**

From P4: $\sum (n+1)x^n = \frac{1}{(1-x)^2}$

We want $\sum n \cdot x^n = \sum (n+1)x^n - \sum x^n = \frac{1}{(1-x)^2} - \frac{1}{1-x}$

$$= \frac{1 - (1-x)}{(1-x)^2} = \frac{x}{(1-x)^2}$$

**Derivation (Method 2 — multiply by $x$):**

From P4's derivation step: $\sum_{n=1}^{\infty} n x^{n-1} = \frac{1}{(1-x)^2}$

Multiply both sides by $x$: $\sum_{n=1}^{\infty} n x^n = \frac{x}{(1-x)^2}$

(The $n=0$ term is $0 \cdot x^0 = 0$, so it doesn't matter.)

**Intuition:** Multiplying a GF by $x$ shifts the sequence right (adds a leading zero). Since $n=0$ gives $a_0 = 0$, the sequence $0, 1, 2, 3, \ldots$ has a natural leading zero — the $x$ factor in the numerator captures this.

$$\boxed{\sum_{n=0}^{\infty} n \cdot x^n = \frac{x}{(1-x)^2}}$$

---

### P6 — Generalised Binomial Coefficients: $a_n = \binom{n+k-1}{k-1}$ 

$$\sum_{n=0}^{\infty} \binom{n+k-1}{k-1} x^n = \frac{1}{(1-x)^k}$$

**Derivation (by repeated differentiation):**

We know $\frac{1}{1-x} = \sum x^n$ (P1).

Differentiate once: $\frac{1}{(1-x)^2} = \sum (n+1)x^n$ (P4).

Differentiate again and divide by $2!$:
$$\frac{1}{(1-x)^3} = \sum_{n=0}^{\infty} \binom{n+2}{2} x^n$$

In general, differentiating $k-1$ times and dividing by $(k-1)!$:
$$\frac{1}{(1-x)^k} = \sum_{n=0}^{\infty} \binom{n+k-1}{k-1} x^n$$

**Derivation (via combinatorics — stars and bars):**

$\frac{1}{(1-x)^k} = \underbrace{\frac{1}{1-x} \cdot \frac{1}{1-x} \cdots \frac{1}{1-x}}_{k \text{ times}}$

Each factor $\frac{1}{1-x}$ represents choosing how many items go into one "bin". The product (convolution) counts the number of ways to put $n$ items into $k$ bins, which is $\binom{n+k-1}{k-1}$ by stars and bars.

**Intuition:** Each extra factor of $\frac{1}{1-x}$ in the denominator adds one more "degree of freedom" to the counting. The exponent $k$ directly tells you how many bins (or variables) you're distributing across.

$$\boxed{\sum_{n=0}^{\infty} \binom{n+k-1}{k-1} x^n = \frac{1}{(1-x)^k}}$$

**Special cases:**

| $k$ | $a_n$ | GF |
|-----|-------|-----|
| 1 | $1$ | $\frac{1}{1-x}$ |
| 2 | $n+1$ | $\frac{1}{(1-x)^2}$ |
| 3 | $\binom{n+2}{2} = \frac{(n+1)(n+2)}{2}$ | $\frac{1}{(1-x)^3}$ |
| 4 | $\binom{n+3}{3}$ | $\frac{1}{(1-x)^4}$ |

---

### P7 — Weighted Powers: $a_n = n \cdot c^{n-1}$ 

$$\sum_{n=0}^{\infty} n \cdot c^{n-1} x^n = \frac{1}{(1-cx)^2}$$

**Derivation:** Differentiate P2 with respect to $x$:

$$\frac{d}{dx}\left[\frac{1}{1-cx}\right] = \frac{c}{(1-cx)^2}$$

$$\frac{d}{dx}\left[\sum_{n=0}^{\infty} c^n x^n\right] = \sum_{n=1}^{\infty} n \cdot c^n x^{n-1} = \sum_{n=0}^{\infty} (n+1) c^{n+1} x^n$$

Wait — let me be precise. The left side after differentiating is $\sum n c^n x^{n-1}$, so:

$$\frac{c}{(1-cx)^2} = \sum_{n=1}^{\infty} n c^n x^{n-1}$$

Divide both sides by $c$:

$$\frac{1}{(1-cx)^2} = \sum_{n=1}^{\infty} n c^{n-1} x^{n-1} = \sum_{n=0}^{\infty} (n+1) c^n x^n$$

So actually $[x^n] \frac{1}{(1-cx)^2} = (n+1)c^n$. This is P4 composed with the $c$-substitution.

$$\boxed{\sum_{n=0}^{\infty} (n+1) c^n x^n = \frac{1}{(1-cx)^2}}$$

**Intuition:** This is just P4 with $x$ replaced by $cx$. The role of $c$ is to "weight" each term by $c^n$.

---

### P8 — Scaled Weighted Powers: $a_n = n \cdot c^n$ 

$$\sum_{n=0}^{\infty} n \cdot c^n x^n = \frac{cx}{(1-cx)^2}$$

**Derivation:** Differentiate P2 and multiply by $x$:

From P2: $\frac{1}{1-cx} = \sum c^n x^n$

Differentiate: $\frac{c}{(1-cx)^2} = \sum n c^n x^{n-1}$

Multiply by $x$: $\frac{cx}{(1-cx)^2} = \sum n c^n x^n$

**Alternative:** This equals $x \cdot \frac{d}{dx}\left[\frac{1}{1-cx}\right]$, using the rule that $x G'(x) = \sum n a_n x^n$.

$$\boxed{\sum_{n=0}^{\infty} n \cdot c^n x^n = \frac{cx}{(1-cx)^2}}$$

**Special case:** $c=1$ gives $\sum n x^n = \frac{x}{(1-x)^2}$, which is P5. ✓

---

### P9 — Delayed Constant: $k$ Leading Zeros 

$$a_n = \begin{cases} 0 & n < k \\ 1 & n \geq k \end{cases} \qquad \longleftrightarrow \qquad \frac{x^k}{1-x}$$

**Derivation:** The sequence starts at index $k$ instead of index $0$:

$$\sum_{n=k}^{\infty} x^n = x^k \sum_{m=0}^{\infty} x^m = x^k \cdot \frac{1}{1-x} = \frac{x^k}{1-x}$$

(Substitute $m = n - k$, so $n = m + k$.)

**Intuition:** Multiplying a GF by $x^k$ is a **right-shift by $k$** — it inserts $k$ zeros at the front of the sequence. This is because $x^k \cdot x^n = x^{n+k}$, which moves the $n$-th term to the $(n+k)$-th position.

$$\boxed{\frac{x^k}{1-x} \longleftrightarrow 0, 0, \ldots, 0, \underbrace{1, 1, 1, \ldots}_{k \text{ zeros before}}}$$

**Generalization:** $\frac{x^k}{1-cx}$ gives the sequence where $a_n = c^{n-k}$ for $n \geq k$, and $0$ otherwise.

---

### P10 — Every Other Term: $a_n = 1$ if $n$ even, $0$ if $n$ odd 

$$\sum_{n=0}^{\infty} x^{2n} = 1 + x^2 + x^4 + \cdots = \frac{1}{1-x^2}$$

**Derivation:** Substitute $x \mapsto x^2$ in P1:

$$\frac{1}{1-x^2} = \sum_{n=0}^{\infty} (x^2)^n = \sum_{n=0}^{\infty} x^{2n}$$

The coefficient of $x^m$ is $1$ if $m$ is even (i.e., $m = 2n$ for some integer $n$), and $0$ if $m$ is odd.

**Intuition:** Substituting $x \mapsto x^k$ "stretches" the sequence — it inserts $k-1$ zeros between each term. Here $k=2$, so the sequence $1, 1, 1, \ldots$ becomes $1, 0, 1, 0, 1, \ldots$.

$$\boxed{\frac{1}{1-x^2} \longleftrightarrow 1, 0, 1, 0, 1, 0, \ldots}$$

**Generalization:** $\frac{1}{1-x^k}$ gives a sequence with $1$ at every $k$-th position ($n = 0, k, 2k, \ldots$) and $0$ elsewhere.

---

### P11 — Binomial Coefficients: $a_n = \binom{n}{r}$ (fixed $r$) 

$$\sum_{n=r}^{\infty} \binom{n}{r} x^n = \frac{x^r}{(1-x)^{r+1}}$$

**Derivation (by right-shifting P6):**

From P6 with $k = r+1$: $\sum_{n=0}^{\infty} \binom{n+r}{r} x^n = \frac{1}{(1-x)^{r+1}}$

Substitute $m = n + r$ (i.e., $n = m - r$):
$$\sum_{m=r}^{\infty} \binom{m}{r} x^{m-r} = \frac{1}{(1-x)^{r+1}}$$

Multiply both sides by $x^r$:
$$\sum_{m=r}^{\infty} \binom{m}{r} x^m = \frac{x^r}{(1-x)^{r+1}}$$

**Derivation (from scratch, via differentiation):**

We know $\frac{1}{1-x} = \sum x^n$. Differentiating $r$ times and dividing by $r!$:

$$\frac{1}{(1-x)^{r+1}} = \frac{1}{r!} \cdot \frac{d^r}{dx^r}\left[\frac{1}{1-x}\right] = \sum_{n=0}^{\infty} \binom{n+r}{r} x^n$$

The right-shift by $r$ (multiplying by $x^r$) re-indexes to give $\binom{n}{r}$ for $n \geq r$.

$$\boxed{\sum_{n=0}^{\infty} \binom{n}{r} x^n = \frac{x^r}{(1-x)^{r+1}}}$$

**Special cases:**

| $r$ | $a_n$ | GF |
|-----|-------|----|
| 0 | $\binom{n}{0} = 1$ | $\frac{1}{1-x}$ |
| 1 | $\binom{n}{1} = n$ | $\frac{x}{(1-x)^2}$ |
| 2 | $\binom{n}{2} = \frac{n(n-1)}{2}$ | $\frac{x^2}{(1-x)^3}$ |

All consistent with P1, P5! ✓

---

### P12 — Fibonacci Sequence: $F_0=0, F_1=1, F_n = F_{n-1}+F_{n-2}$ 

$$\sum_{n=0}^{\infty} F_n x^n = \frac{x}{1-x-x^2}$$

**Derivation (via recurrence translation):**

Let $G(x) = \sum_{n=0}^{\infty} F_n x^n$.

The recurrence $F_n = F_{n-1} + F_{n-2}$ holds for $n \geq 2$. Multiply by $x^n$ and sum:

$$\sum_{n=2}^{\infty} F_n x^n = \sum_{n=2}^{\infty} F_{n-1} x^n + \sum_{n=2}^{\infty} F_{n-2} x^n$$

- LHS: $G(x) - F_0 - F_1 x = G(x) - x$
- First sum: $x \sum_{n=2}^{\infty} F_{n-1} x^{n-1} = x(G(x) - F_0) = xG(x)$
- Second sum: $x^2 \sum_{n=2}^{\infty} F_{n-2} x^{n-2} = x^2 G(x)$

So: $G(x) - x = xG(x) + x^2 G(x)$

$$G(x)(1 - x - x^2) = x \implies \boxed{G(x) = \frac{x}{1-x-x^2}}$$

**Intuition:** The denominator $1 - x - x^2$ is the *characteristic polynomial* of the Fibonacci recurrence, with $x$ shifted out front. This pattern generalises: any linear recurrence $a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k}$ gives a GF whose denominator is $1 - c_1 x - c_2 x^2 - \cdots - c_k x^k$.

---

## Derivation Strategy Summary

When you encounter an unfamiliar sequence→GF pair, try these strategies in order:

```
1. Is it a geometric series in disguise?
   → Try P2 (substitution x ↦ cx)

2. Does the sequence grow polynomially?
   → Try differentiating P1 repeatedly (P4, P6)

3. Does the sequence have a multiplicative factor of n?
   → Use x·G'(x) trick (P5, P8)

4. Does the sequence start with zeros?
   → Multiply by x^k to right-shift (P9)

5. Does the sequence skip terms (only even/odd indices)?
   → Try substituting x ↦ x^k (P10)

6. Is it defined by a recurrence?
   → Translate the recurrence directly (P12, see Note 03)

7. Is it a product of two known sequences?
   → Multiply their GFs (convolution)
```

---

*→ Return to [[00 GF Index]] | See these patterns in action in [[02 GF Ordinary]] and [[03 GF Recurrences]]*
