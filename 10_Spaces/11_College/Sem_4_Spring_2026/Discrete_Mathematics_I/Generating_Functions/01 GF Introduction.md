---
title: "GF 01 — Introduction & Foundations"
course: Discrete Mathematics I
tags: ["discrete-mathematics", "generating-functions", "formal-power-series", "sequences"]
aliases: ["GF 01 — Introduction & Foundations"]
created: "2026-05-24"
type: Note
topic: Generating Functions
subtopic: Introduction
week: 9
---

# 01 · Introduction & Foundations

> **← Back to** [[00 GF Index]] | **Next →** [[02 GF Ordinary]]

---

## 1.1 Motivation — Why Generating Functions?

Imagine you are handed a bag of loose numbers: $\langle 0, 1, 5, 14, 30, 55, \ldots \rangle$. These numbers represent a sequence $a_n$. If you want to study this sequence—find a formula for the $n$-th term, sum them up, or see how they relate to other sequences—working with them as a list is difficult. 

Generating functions give us a way to "package" this infinite sequence into a single algebraic object.

> 🧺 **The Clothesline Metaphor (by Herbert Wilf):**
> Think of a generating function as a **clothesline**, and the terms of your sequence $a_0, a_1, a_2, \ldots$ as **socks**. 
> - On their own, the socks are scattered on the floor. 
> - To display them in order, we hang them up on a clothesline.
> - The clothesline has hooks labeled $1, x, x^2, x^3, x^4, \ldots$
> - We hang $a_0$ on the hook $1$, $a_1$ on the hook $x$, $a_2$ on the hook $x^2$, and so on.
> 
> The result is the algebraic expression:
> $$G(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots$$
> 
> The symbol $x^n$ is **not a number** we are trying to calculate. It is simply the **hook** (or index) that tells us: "The term hanging here is the $n$-th term of our sequence."

---

## 1.2 What is a "Formal" Power Series?

To understand generating functions, you must unlearn a habit from calculus. In calculus, when you see an infinite sum like $\sum a_n x^n$, your first question is: *Does this converge? For what values of $x$ does it add up to a real number?*

In discrete mathematics, we treat $G(x)$ as a **formal power series**.

### 1. What does "formal" mean?
It means we treat $x$ purely as an **algebraic symbol**, a placeholder. 
- We **do not** plug numbers into $x$.
- We **do not** worry about whether the sum converges.
- The series is simply an alternative way of writing the sequence. The sequence $\langle a_0, a_1, a_2, \ldots \rangle$ and the expression $a_0 + a_1 x + a_2 x^2 + \ldots$ contain the exact same information.

For example, the series:
$$S(x) = 0! + 1! x + 2! x^2 + 3! x^3 + 4! x^4 + \cdots$$
diverges for every single real number $x$ except $0$. In calculus, this function is useless. In discrete math, it is a perfectly valid and useful formal power series because it successfully encodes the factorial sequence.

### 2. How do we do algebra on a clothesline?
Since these are formal symbols, we define the operations of addition and multiplication using simple polynomial rules:

*   **Addition (Term-by-term matching):**
    If we want to add two clotheslines, we just add the socks on corresponding hooks:
    $$(a_0 + a_1 x + a_2 x^2 + \cdots) + (b_0 + b_1 x + b_2 x^2 + \cdots) = (a_0+b_0) + (a_1+b_1)x + (a_2+b_2)x^2 + \cdots$$
    
*   **Multiplication (Distributive Law / Convolution):**
    To multiply two clotheslines, we distribute the terms just like we do with finite polynomials $(x+2)(x+3)$. To find the coefficient of $x^n$ in the product, we collect all combinations of terms that multiply to $x^n$:
    $$(a_0 + a_1 x + a_2 x^2 + \cdots)(b_0 + b_1 x + b_2 x^2 + \cdots) = (a_0 b_0) + (a_0 b_1 + a_1 b_0)x + (a_0 b_2 + a_1 b_1 + a_2 b_0)x^2 + \cdots$$
    Notice that the coefficient of $x^n$ is:
    $$c_n = a_0 b_n + a_1 b_{n-1} + a_2 b_{n-2} + \cdots + a_n b_0$$
    This is called the **convolution** of the two sequences. It arises naturally from basic polynomial multiplication.

### Notation

We write $[x^n]\, G(x) = a_n$ to mean "the coefficient of the $x^n$ term in the series $G(x)$." 

**Example:** If $G(x) = 5 + 3x - 9x^2 + 0x^3 + 7x^4 + \cdots$, then:
- $[x^0]\, G(x) = 5$ (the constant term)
- $[x^1]\, G(x) = 3$
- $[x^2]\, G(x) = -9$
- $[x^3]\, G(x) = 0$

---

## 1.3 The Fundamental Engine: The Geometric Series

The most important identity in generating functions is:

$$\sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \cdots = \frac{1}{1-x}$$

This is the bridge between an infinite series (left) and a compact, closed-form function (right). 

### Step-by-Step Derivation

How do we prove $1 + x + x^2 + \cdots = \frac{1}{1-x}$ without using calculus or limits? We do it purely with formal algebra.

1. Let $S$ represent our infinite clothesline:
   $$S = 1 + x + x^2 + x^3 + x^4 + \cdots$$
2. Let's multiply $S$ by the symbol $x$. This distributes $x$ to every term:
   $$xS = x(1 + x + x^2 + x^3 + x^4 + \cdots) = x + x^2 + x^3 + x^4 + x^5 + \cdots$$
3. Now, let's write these two series right next to each other and subtract them:
   $$\begin{aligned}
   S  &= 1 + x + x^2 + x^3 + x^4 + \cdots \\
   xS &= \phantom{1 + } x + x^2 + x^3 + x^4 + \cdots
   \end{aligned}$$
4. Subtracting the second equation from the first:
   $$S - xS = (1 - 0) + (x - x) + (x^2 - x^2) + (x^3 - x^3) + \cdots$$
   All terms cancel out except the very first term, $1$:
   $$S(1 - x) = 1$$
5. Divide both sides by $(1-x)$ to solve for $S$:
   $$S = \frac{1}{1-x}$$

This proof is algebraically rigorous for formal power series because addition, multiplication by a variable, and subtraction are defined term-by-term and behave exactly this way. We call $\frac{1}{1-x}$ the **closed form** of the sequence $\langle 1, 1, 1, 1, \ldots \rangle$.

---

## 1.4 Building GFs from Sequences

### Step-by-Step: Sequence → GF

| Sequence | Write out terms | GF |
|----------|----------------|----|
| $1, 1, 1, 1, \ldots$ | $1 + x + x^2 + \cdots$ | $\dfrac{1}{1-x}$ |
| $1, 2, 4, 8, \ldots$ (powers of 2) | $1 + 2x + 4x^2 + \cdots = \sum 2^n x^n$ | $\dfrac{1}{1-2x}$ |
| $0, 1, 2, 3, \ldots$ (natural numbers) | $0 + x + 2x^2 + 3x^3 + \cdots$ | $\dfrac{x}{(1-x)^2}$ |
| $1, -1, 1, -1, \ldots$ | $1 - x + x^2 - x^3 + \cdots$ | $\dfrac{1}{1+x}$ |

> 📖 **Why do these closed forms work?** Each one uses a specific trick (substitution, differentiation, or shifting). See [[06 GF Pattern Library]] for step-by-step derivations of all patterns.

### Example 1: Constant Sequence

Sequence: $2, 2, 2, 2, \ldots$ (i.e., $a_n = 2$ for all $n$)

$$G(x) = \sum_{n=0}^{\infty} 2 \cdot x^n = 2 \sum_{n=0}^{\infty} x^n = \frac{2}{1-x}$$

### Example 2: Powers of a Constant

Sequence: $1, c, c^2, c^3, \ldots$ (i.e., $a_n = c^n$)

$$G(x) = \sum_{n=0}^{\infty} c^n x^n = \sum_{n=0}^{\infty} (cx)^n = \frac{1}{1-cx}$$

### Example 3: Finite Sequence

Sequence: $1, 1, 1, 0, 0, 0, \ldots$ (only first 3 terms are 1)

$$G(x) = 1 + x + x^2 = \frac{1 - x^3}{1-x}$$

> 💡 Finite sequences have *polynomial* generating functions.

---

## 1.5 GF → Sequence (Decoding)

Going the other direction: given a GF, find the sequence.

### Example 4: Decode a Fraction

Find the sequence with GF $G(x) = \dfrac{1}{1-3x}$.

**Solution:**
$$\frac{1}{1-3x} = \sum_{n=0}^{\infty} (3x)^n = \sum_{n=0}^{\infty} 3^n x^n$$

So the sequence is $a_n = 3^n$, i.e., $1, 3, 9, 27, \ldots$ ✓

### Example 5: Decode with a Shift

Find the sequence with GF $G(x) = \dfrac{x^2}{1-x}$.

**Solution:**
$$\frac{x^2}{1-x} = x^2 \cdot \frac{1}{1-x} = x^2 \sum_{n=0}^{\infty} x^n = \sum_{n=0}^{\infty} x^{n+2} = \sum_{n=2}^{\infty} x^n$$

So $a_n = 1$ for $n \geq 2$, and $a_0 = a_1 = 0$. Sequence: $0, 0, 1, 1, 1, 1, \ldots$ ✓

---

## 1.6 The Binomial Theorem (Extended)

The **extended binomial theorem** is critical:

$$(1+x)^n = \sum_{k=0}^{n} \binom{n}{k} x^k$$

For *negative* integer exponents (generalized):

$$(1-x)^{-r} = \sum_{n=0}^{\infty} \binom{n+r-1}{r-1} x^n$$

Key special cases:

| GF | Closed Form | Coefficient $[x^n]$ |
|----|------------|---------------------|
| $\dfrac{1}{(1-x)^2}$ | $(1-x)^{-2}$ | $n+1$ |
| $\dfrac{1}{(1-x)^3}$ | $(1-x)^{-3}$ | $\binom{n+2}{2}$ |
| $\dfrac{1}{(1-x)^k}$ | $(1-x)^{-k}$ | $\binom{n+k-1}{k-1}$ |

**Derivation of $\dfrac{1}{(1-x)^2}$:**

Differentiate $\dfrac{1}{1-x} = \sum_{n=0}^{\infty} x^n$ with respect to $x$:

$$\frac{1}{(1-x)^2} = \sum_{n=1}^{\infty} n x^{n-1} = \sum_{n=0}^{\infty} (n+1) x^n$$

So $[x^n] \dfrac{1}{(1-x)^2} = n+1$. ✓

---

## 1.7 Quick Reference Table

$$\boxed{
\begin{array}{|l|l|}
\hline
\textbf{Sequence } a_n & \textbf{GF } G(x) = \sum a_n x^n \\
\hline
1 & \frac{1}{1-x} \\
n+1 & \frac{1}{(1-x)^2} \\
\binom{n+k-1}{k-1} & \frac{1}{(1-x)^k} \\
c^n & \frac{1}{1-cx} \\
\binom{n}{k} \text{ (fixed } k) & \frac{x^k}{(1-x)^{k+1}} \\
\hline
\end{array}
}$$

---

## 1.8 Check Your Understanding

> **Exercise 1.1** — Find the GF for $a_n = 5 \cdot 3^n$.
>
> <details><summary>Hint</summary>Factor out the constant and use $\sum (3x)^n$.</details>
> <details><summary>Answer</summary>
>
> $G(x) = \sum 5 \cdot 3^n x^n = 5 \sum (3x)^n = \dfrac{5}{1-3x}$
>
> </details>

> **Exercise 1.2** — What sequence does $G(x) = \dfrac{1}{1-x^2}$ encode?
>
> <details><summary>Hint</summary>Substitute $x^2$ for $x$ in the geometric series.</details>
> <details><summary>Answer</summary>
>
> $\dfrac{1}{1-x^2} = \sum (x^2)^n = \sum x^{2n}$. So $a_n = 1$ if $n$ is even, $a_n = 0$ if $n$ is odd. Sequence: $1, 0, 1, 0, 1, 0, \ldots$
>
> </details>

> **Exercise 1.3** — Find $[x^5]$ in $G(x) = \dfrac{1}{(1-x)^3}$.
>
> <details><summary>Answer</summary>
>
> $[x^n] \dfrac{1}{(1-x)^3} = \binom{n+2}{2}$, so $[x^5] = \binom{7}{2} = 21$.
>
> </details>

---

*→ Continue to [[02 GF Ordinary]] for OGF operations and combinatorial interpretations.*
