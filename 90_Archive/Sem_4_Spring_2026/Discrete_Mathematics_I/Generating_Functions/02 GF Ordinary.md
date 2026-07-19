---
title: GF 02 — Ordinary Generating Functions
course: Discrete Mathematics I
tags: ["discrete-mathematics", "generating-functions", "ogf", "combinatorics"]
aliases: ["GF 02 — Ordinary Generating Functions"]
created: "2026-05-24"
type: Note
topic: Generating Functions
subtopic: OGF Operations
week: "9-11"
---

# 02 · Ordinary Generating Functions

> **← Back to** [[01 GF Introduction]] | **Next →** [[03 GF Recurrences]]

---

## 2.1 OGF Operations Toolkit

The true power of generating functions is that **algebraic manipulations of the function correspond to structural operations on the sequence**. Instead of manipulating individual elements of an infinite list, we perform standard algebra on the function.

### The Operations Table

| Operation on Sequence | Effect on GF $G(x) = \sum a_n x^n$ | Description & Rationale |
|----------------------|--------------------------------------|-------------------------|
| **Scale:** $b_n = c \cdot a_n$ | $c \cdot G(x)$ | Multiply every term of the sequence by a constant $c$. |
| **Sum:** $c_n = a_n + b_n$ | $G(x) + H(x)$ | Add two sequences term-by-term. |
| **Shift right:** $b_n = a_{n-1}$ | $x \cdot G(x)$ | Move all terms one step to the right; prepend a $0$. |
| **Shift left:** $b_n = a_{n+1}$ | $\frac{G(x) - a_0}{x}$ | Move all terms one step to the left; discard $a_0$. |
| **Multiply by $n$:** $b_n = n \cdot a_n$ | $x \cdot G'(x)$ | Differentiate with respect to $x$ and multiply by $x$. |
| **Divide by $n+1$:** $b_n = \frac{a_n}{n+1}$ | $\frac{1}{x} \int_0^x G(t)\, dt$ | Integrate the series and divide by $x$. |
| **Substitute:** $b_n = c^n a_n$ | $G(cx)$ | Replace $x$ with $cx$ in the function. |

---

## 2.2 Shifting: The Most Important Operation

Shifting is the most common operation, especially when solving recurrence relations. Let's see exactly how and why it works by writing out the clothesline term-by-term.

### 1. Right Shift (Prepending Zeros)

If we multiply a generating function $G(x)$ by the symbol $x$, we multiply every term in its series by $x$:
$$\begin{aligned}
G(x) &= a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots \\
x \cdot G(x) &= x(a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots) \\
&= 0 + a_0 x + a_1 x^2 + a_2 x^3 + a_3 x^4 + \cdots
\end{aligned}$$

Look at the new coefficients:
- The constant term ($x^0$ hook) is now **$0$**.
- The coefficient of $x^1$ is now **$a_0$** (was $a_1$).
- The coefficient of $x^2$ is now **$a_1$** (was $a_2$).

Every coefficient has moved one slot to the right! 
- Sequence: $\langle a_0, a_1, a_2, a_3, \ldots \rangle$
- New Sequence: $\langle 0, a_0, a_1, a_2, \ldots \rangle$

> 💡 **Rule:** Multiplying by $x^k$ shifts the sequence right by $k$ slots, prepending $k$ zeros.

---

### 2. Left Shift (Removing First Terms)

What if we want to shift the sequence to the left (i.e. discard the first term $a_0$ and move everything else down)? 

1. First, we subtract $a_0$ to remove the first term from the clothesline:
   $$G(x) - a_0 = a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4 + \cdots$$
2. Now, every remaining term has at least one factor of $x$. We divide the entire expression by $x$ to pull every term down by one power:
   $$\frac{G(x) - a_0}{x} = \frac{a_1 x + a_2 x^2 + a_3 x^3 + \cdots}{x} = a_1 + a_2 x + a_3 x^2 + a_4 x^3 + \cdots$$

This leaves us with the sequence: $\langle a_1, a_2, a_3, \ldots \rangle$.

What if we want to shift left by **two** slots?
1. We must subtract both $a_0$ and $a_1 x$:
   $$G(x) - a_0 - a_1 x = a_2 x^2 + a_3 x^3 + a_4 x^4 + \cdots$$
2. Then, divide by $x^2$:
   $$\frac{G(x) - a_0 - a_1 x}{x^2} = a_2 + a_3 x + a_4 x^2 + \cdots$$

This leaves us with the sequence: $\langle a_2, a_3, a_4, \ldots \rangle$. This is the exact algebraic mechanism behind boundary conditions in recurrences!

---

### Worked Example

**Problem:** Find the generating function for the sequence: $\langle 0, 0, 1, 1, 1, 1, \ldots \rangle$.

**Solution:**
1. We know the constant sequence $\langle 1, 1, 1, 1, \ldots \rangle$ has the generating function $G(x) = \frac{1}{1-x}$.
2. The target sequence has two leading zeros, meaning it is the constant sequence shifted right by two slots.
3. Therefore, we multiply $G(x)$ by $x^2$:
   $$H(x) = x^2 \cdot G(x) = \frac{x^2}{1-x}$$
4. Let's verify by expanding:
   $$\frac{x^2}{1-x} = x^2 (1 + x + x^2 + x^3 + \cdots) = 0 + 0x + 1x^2 + 1x^3 + 1x^4 + \cdots$$
   The coefficients are exactly $0, 0, 1, 1, 1, \ldots$ ✓

---

## 2.3 Differentiation and Integration

### Differentiation → Multiply sequence by $n$

$$G'(x) = \sum_{n=1}^{\infty} n \cdot a_n \cdot x^{n-1}$$
$$x \cdot G'(x) = \sum_{n=0}^{\infty} n \cdot a_n \cdot x^n$$

**Example:** Starting from $\frac{1}{1-x} = \sum x^n$:

$$\frac{d}{dx}\left[\frac{1}{1-x}\right] = \frac{1}{(1-x)^2} = \sum_{n=0}^{\infty} (n+1) x^n$$

So $[x^n] \frac{1}{(1-x)^2} = n+1$. ✓

Multiply by $x$:
$$\frac{x}{(1-x)^2} = \sum_{n=0}^{\infty} n \cdot x^n = 0 + x + 2x^2 + 3x^3 + \cdots$$

### Integration → Divide sequence by $n+1$

$$\int_0^x G(t)\, dt = \sum_{n=0}^{\infty} \frac{a_n}{n+1} x^{n+1}$$

**Example:** $\int_0^x \frac{1}{1-t}\, dt = -\ln(1-x) = \sum_{n=1}^{\infty} \frac{x^n}{n}$

So $[x^n](-\ln(1-x)) = \frac{1}{n}$ for $n \geq 1$.

---

## 2.4 Convolution: The Product of Two GFs

When we multiply two generating functions, $G(x) = \sum a_n x^n$ and $H(x) = \sum b_n x^n$, what happens to the underlying sequences? 

Let's write out the multiplication of $G(x) \cdot H(x)$ term-by-term and collect terms by their power of $x$:
$$G(x) \cdot H(x) = (a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots)(b_0 + b_1 x + b_2 x^2 + b_3 x^3 + \cdots)$$

To see how the coefficient of each $x^n$ is formed, look at this multiplication grid:

| | $b_0$ | $b_1 x$ | $b_2 x^2$ | $b_3 x^3$ |
|---|---|---|---|---|
| **$a_0$** | $\mathbf{a_0 b_0}$ | $\mathbf{a_0 b_1 x}$ | $\mathbf{a_0 b_2 x^2}$ | $a_0 b_3 x^3$ |
| **$a_1 x$** | $\mathbf{a_1 b_0 x}$ | $\mathbf{a_1 b_1 x^2}$ | $a_1 b_2 x^3$ | $a_1 b_3 x^4$ |
| **$a_2 x^2$** | $\mathbf{a_2 b_0 x^2}$ | $a_2 b_1 x^3$ | $a_2 b_2 x^4$ | $a_2 b_3 x^5$ |
| **$a_3 x^3$** | $a_3 b_0 x^3$ | $a_3 b_1 x^4$ | $a_3 b_2 x^5$ | $a_3 b_3 x^6$ |

Look at the diagonals running from bottom-left to top-right:
- The **$x^0$** term is $a_0 b_0$.
- The **$x^1$** terms are $a_1 b_0 x + a_0 b_1 x = (a_1 b_0 + a_0 b_1) x$.
- The **$x^2$** terms are $a_2 b_0 x^2 + a_1 b_1 x^2 + a_0 b_2 x^2 = (a_2 b_0 + a_1 b_1 + a_0 b_2) x^2$.

In general, the coefficient of $x^n$ in $G(x) \cdot H(x)$ is:
$$c_n = a_0 b_n + a_1 b_{n-1} + a_2 b_{n-2} + \cdots + a_n b_0 = \sum_{k=0}^{n} a_k b_{n-k}$$

This operation is called the **convolution** of sequences $(a_n)$ and $(b_n)$.

### Combinatorial Meaning: The "Splitting" Principle

Whenever you see a product of two GFs, it corresponds to **splitting a choice into two independent parts**.
Suppose you want to choose a total of $n$ items. You can choose $k$ items of type A, and the remaining $n-k$ items of type B. 
- Number of ways to choose $k$ of type A is $a_k$ (encoded by $G(x)$).
- Number of ways to choose $n-k$ of type B is $b_{n-k}$ (encoded by $H(x)$).
- Total ways for a fixed $k$ is $a_k b_{n-k}$.
- Summing over all possible ways to split $n$ (from $k=0$ to $n$) gives $\sum_{k=0}^n a_k b_{n-k}$.

**Example:** How many ways can you distribute $n$ identical candies into 2 distinct bins?
- Bin 1 can take any number of candies $\geq 0$: OGF is $1 + x + x^2 + \cdots = \frac{1}{1-x}$.
- Bin 2 can take any number of candies $\geq 0$: OGF is $1 + x + x^2 + \cdots = \frac{1}{1-x}$.
- The combined GF is the product of the two: 
  $$G(x) \cdot H(x) = \frac{1}{1-x} \cdot \frac{1}{1-x} = \frac{1}{(1-x)^2}$$
- From our pattern library, we know $[x^n] \frac{1}{(1-x)^2} = n+1$.
- Let's check convolution directly: $c_n = \sum_{k=0}^n a_k b_{n-k} = \sum_{k=0}^n 1 \cdot 1 = n+1$ ways. Indeed, you can put $0$ in Bin 1 ($n$ in Bin 2), $1$ in Bin 1 ($n-1$ in Bin 2), ..., or $n$ in Bin 1 ($0$ in Bin 2). ✓

---

## 2.5 Partial Fractions (Critical Technique)

When we solve recurrences or counting problems, we often end up with a fractional GF like:
$$G(x) = \frac{P(x)}{Q(x)}$$
where $P(x)$ and $Q(x)$ are polynomials. To decode this back into a sequence, we use **Partial Fraction Decomposition** to break it into simple, recognizable terms of the form $\frac{A}{1-cx}$.

### The Mathematical Setup

Consider $G(x) = \frac{1}{(1-x)(1-2x)}$. We want to write this as:
$$\frac{1}{(1-x)(1-2x)} = \frac{A}{1-x} + \frac{B}{1-2x}$$

To solve for the constants $A$ and $B$, we multiply both sides by the entire denominator $(1-x)(1-2x)$:
$$\boxed{1 = A(1-2x) + B(1-x)}$$

### ⚠️ The "Plugging in Roots" Confusion

A common student question is:
> *"To find $A$, the notes tell me to set $x = 1$. But if I set $x = 1$ in the original equation $\frac{1}{(1-x)(1-2x)} = \frac{A}{1-x} + \frac{B}{1-2x}$, I am dividing by zero! How is this legal?"*

**The Resolution:** 
We are **not** plugging $x=1$ into the original rational equation. Instead, we are plugging it into the **polynomial equation** $1 = A(1-2x) + B(1-x)$. 
This polynomial equation must hold true for **every** value of $x$. Since it is an identity of polynomials, we are mathematically allowed to plug in *any* value of $x$ we like to solve for the coefficients. Plugging in the roots of the terms ($x = 1$ and $x = 1/2$) is just a clever trick to make one of the variables disappear so we can solve for the other.

- **To find $A$:** Set $x = 1$ (the value that makes $B$'s coefficient $1-x$ zero):
  $$1 = A(1 - 2(1)) + B(1 - 1) \implies 1 = A(-1) + 0 \implies A = -1$$
- **To find $B$:** Set $x = \frac{1}{2}$ (the value that makes $A$'s coefficient $1-2x$ zero):
  $$1 = A\left(1 - 2\left(\frac{1}{2}\right)\right) + B\left(1 - \frac{1}{2}\right) \implies 1 = 0 + B\left(\frac{1}{2}\right) \implies B = 2$$

Now we substitute these constants back into our partial fractions:
$$G(x) = \frac{-1}{1-x} + \frac{2}{1-2x}$$

### Decoding Step

We can now expand each term using the geometric series pattern ($P1$ and $P2$):
- $\frac{-1}{1-x} = -1 \sum_{n=0}^{\infty} x^n$
- $\frac{2}{1-2x} = 2 \sum_{n=0}^{\infty} (2x)^n = \sum_{n=0}^{\infty} 2 \cdot 2^n x^n = \sum_{n=0}^{\infty} 2^{n+1} x^n$

Combining them:
$$G(x) = \sum_{n=0}^{\infty} \left(2^{n+1} - 1\right) x^n$$

So, the $n$-th term of our sequence is:
$$\boxed{a_n = 2^{n+1} - 1}$$

Let's double-check the first few terms:
- $a_0 = 2^1 - 1 = 1$
- $a_1 = 2^2 - 1 = 3$
- $a_2 = 2^3 - 1 = 7$

Checking the expansion of $G(x) = (1+x+x^2+\cdots)(1+2x+4x^2+\cdots)$:
- Constant term: $1 \cdot 1 = 1$ ✓
- $x^1$ term: $1 \cdot 2 + 1 \cdot 1 = 3$ ✓
- $x^2$ term: $1 \cdot 4 + 1 \cdot 2 + 1 \cdot 1 = 7$ ✓

The algebra matches perfectly!

Check: $a_0 = 2-1 = 1$, $a_1 = 4-1 = 3$, $a_2 = 8-1 = 7$. Manual: $G(x) = (1+x+x^2+\cdots)(1+2x+4x^2+\cdots)$, and $[x^2] = 1\cdot4 + 1\cdot2 + 1\cdot1 = 7$. ✓

---

## 2.6 Combinatorial Applications

Generating functions shine in counting combinations with constraints. The key rule to remember is:
> **The Addition Rule in exponents matches the Addition of values in the real world.**
> When we write $x^m$, the exponent $m$ represents the *value* or *weight* of our choice. When we combine choices, we multiply the GFs, which adds their exponents: $x^a \cdot x^b = x^{a+b}$. The coefficient of $x^n$ counts how many ways we can get a total weight of $n$.

### 1. Make Change (Coins/Objects Distribution)

**Problem:** In how many ways can we make change for $n$ cents using pennies (1¢), nickels (5¢), and dimes (10¢)?

Let's break this down for each coin type:
- **Pennies (1¢):** We can use 0 pennies (value 0¢, encoded as $x^0 = 1$), 1 penny (value 1¢, encoded as $x^1$), 2 pennies (value 2¢, encoded as $x^2$), etc.
  $$\text{Pennies Factor} = 1 + x + x^2 + x^3 + \cdots = \frac{1}{1-x}$$
- **Nickels (5¢):** We can use 0 nickels (value 0¢, encoded as $x^0 = 1$), 1 nickel (value 5¢, encoded as $x^5$), 2 nickels (value 10¢, encoded as $x^{10}$), etc.
  $$\text{Nickels Factor} = 1 + x^5 + x^{10} + x^{15} + \cdots = \frac{1}{1-x^5}$$
- **Dimes (10¢):** We can use 0 dimes (value 0¢, encoded as $x^0 = 1$), 1 dime (value 10¢, encoded as $x^{10}$), 2 dimes (value 20¢, encoded as $x^{20}$), etc.
  $$\text{Dimes Factor} = 1 + x^{10} + x^{20} + x^{30} + \cdots = \frac{1}{1-x^{10}}$$

To find the number of ways to make change for $n$ cents, we multiply the three factors. Why? Because when we multiply:
$$(1 + x + x^2 + \cdots)(1 + x^5 + x^{10} + \cdots)(1 + x^{10} + x^{20} + \cdots)$$
every term in the expansion looks like $x^p \cdot x^{5k} \cdot x^{10d} = x^{p + 5k + 10d}$, where $p$ is pennies, $k$ is nickels, and $d$ is dimes. The exponent $p + 5k + 10d$ is exactly the total value in cents! The coefficient of $x^n$ counts how many combinations of $(p, k, d)$ add up to exactly $n$.

Combined GF:
$$G(x) = \frac{1}{(1-x)(1-x^5)(1-x^{10})}$$
The answer to our problem is $[x^n] G(x)$.

---

### 2. Selections with Repetition (Stars & Bars)

**Problem:** Choose $n$ items from a set of $k$ distinct types, with unlimited repetition.

For each type, we can choose 0 items ($x^0 = 1$), 1 item ($x^1$), 2 items ($x^2$), etc.
$$\text{Factor for each type} = 1 + x + x^2 + x^3 + \cdots = \frac{1}{1-x}$$

Since we have $k$ types, we multiply this factor by itself $k$ times:
$$G(x) = \left(\frac{1}{1-x}\right)^k = \frac{1}{(1-x)^k}$$

From the Extended Binomial Theorem (Pattern P6), the coefficient of $x^n$ is:
$$[x^n]\, G(x) = \binom{n+k-1}{k-1}$$
This is the exact same formula we derive using the combinatorial "Stars and Bars" method! The generating function handles it purely algebraically.

---

### 3. Selections with Constraints (The True Power of GFs)

**Problem:** Select $n$ books from 3 types:
- **Type A:** We must select at least 1 book.
- **Type B:** We must select exactly 2 books.
- **Type C:** We can select at most 3 books.

Let's translate each constraint directly into a polynomial factor:
- **Type A constraint (at least 1):** We can select 1, 2, 3, ... books. This corresponds to the terms:
  $$x + x^2 + x^3 + \cdots = x(1 + x + x^2 + \cdots) = \frac{x}{1-x}$$
- **Type B constraint (exactly 2):** We can only select 2 books. This corresponds to a single term:
  $$x^2$$
- **Type C constraint (at most 3):** We can select 0, 1, 2, or 3 books. This is a finite sequence:
  $$1 + x + x^2 + x^3 = \frac{1-x^4}{1-x}$$

Now, we multiply these factors together to represent the combined choice:
$$G(x) = \left(\frac{x}{1-x}\right) \cdot \left(x^2\right) \cdot \left(\frac{1-x^4}{1-x}\right) = \frac{x^3(1-x^4)}{(1-x)^2}$$

This is the generating function for the book selection. The coefficient $[x^n] G(x)$ gives the number of valid book combinations of size $n$. Let's analyze it:
$$G(x) = \frac{x^3 - x^7}{(1-x)^2} = (x^3 - x^7) \frac{1}{(1-x)^2}$$

Recall that $\frac{1}{(1-x)^2} = \sum_{n=0}^{\infty} (n+1) x^n$. Therefore:
$$G(x) = x^3 \sum_{n=0}^{\infty} (n+1) x^n - x^7 \sum_{n=0}^{\infty} (n+1) x^n = \sum_{n=3}^{\infty} (n-2) x^n - \sum_{n=7}^{\infty} (n-6) x^n$$

Thus, the number of ways $a_n$ is:
- $0$ for $n < 3$
- $n - 2$ for $3 \leq n < 7$
- $(n - 2) - (n - 6) = 4$ for $n \geq 7$

Let's double-check this for $n=5$ books:
- According to our formula, $a_5 = 5 - 2 = 3$ ways.
- Let's list the ways manually: We need $A + B + C = 5$ books. We know $B = 2$, so we need $A + C = 3$ books, with $A \geq 1$ and $0 \leq C \leq 3$.
  - Way 1: $A=1, B=2, C=2$
  - Way 2: $A=2, B=2, C=1$
  - Way 3: $A=3, B=2, C=0$
  There are exactly 3 ways! The math matches. This shows how generating functions can solve complex constraint problems automatically without manual list-making.

---

## 2.7 Common GF Pairs (Extended Reference)

$$\boxed{
\begin{array}{|l|l|l|}
\hline
\textbf{Sequence } a_n & \textbf{GF} & \textbf{Note} \\
\hline
1 & \frac{1}{1-x} & \text{Geometric} \\
n+1 & \frac{1}{(1-x)^2} & \text{Differentiation of above} \\
\binom{n+k-1}{k-1} & \frac{1}{(1-x)^k} & \text{Stars \& bars} \\
c^n & \frac{1}{1-cx} & \text{Substitution} \\
\binom{n}{r} & \frac{x^r}{(1-x)^{r+1}} & \text{Fixed } r \\
(-1)^n & \frac{1}{1+x} & \\
n \cdot c^{n-1} & \frac{1}{(1-cx)^2} & \\
\frac{1}{n!} & e^x & \text{EGF-style} \\
\hline
\end{array}
}$$

> 📖 **Want to know *why* each of these holds?** See [[06 GF Pattern Library]] for a full derivation of every pattern above, plus a strategy guide for deriving new ones.

---

## 2.8 Check Your Understanding

> **Exercise 2.1** — Find $[x^n]$ for $G(x) = \dfrac{3}{1-2x} - \dfrac{1}{1-x}$.
>
> <details><summary>Answer</summary>
>
> $a_n = 3 \cdot 2^n - 1$
>
> </details>

> **Exercise 2.2** — How many ways to distribute $n$ identical objects into 4 distinct bins (unlimited)?
>
> <details><summary>Answer</summary>
>
> GF: $\frac{1}{(1-x)^4}$, so $[x^n] = \binom{n+3}{3}$ ways.
>
> </details>

> **Exercise 2.3** — Use partial fractions to find $[x^n]$ for $\dfrac{1}{1-3x+2x^2}$.
>
> <details><summary>Hint</summary>Factor: $1-3x+2x^2 = (1-x)(1-2x)$. Same as the example!</details>
> <details><summary>Answer</summary>
>
> $a_n = 2^{n+1} - 1$ (same as Section 2.5)
>
> </details>

> **Exercise 2.4** — Find the GF for $a_n = n \cdot 2^n$.
>
> <details><summary>Hint</summary>Start from $\frac{1}{1-2x}$ and differentiate, then multiply by $x$.</details>
> <details><summary>Answer</summary>
>
> $G(x) = \dfrac{2x}{(1-2x)^2}$
>
> </details>

---

*→ Continue to [[03 GF Recurrences]] to solve recurrences with generating functions.*
