---
title: GF 07 — The Binomial Theorem
course: Discrete Mathematics I
tags: ["discrete-mathematics", "generating-functions", "binomial-theorem", "combinations", "newton"]
aliases: ["GF 07 — The Binomial Theorem"]
created: "2026-06-09"
type: Note
topic: Generating Functions
subtopic: Binomial Theorem
week: 9
---

# 07 · The Binomial Theorem & Newton's Generalization

> **← Back to** [[00 GF Index]]

---

## 7.1 Introduction — What is the Binomial Theorem?

The **Binomial Theorem** is one of the most famous results in algebra. It tells us how to expand any expression of the form $(x+y)^n$ where $n$ is a non-negative integer.

$$\boxed{(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k}$$

Expanding this for the first few powers of $n$:
- $(x+y)^0 = 1$
- $(x+y)^1 = 1x + 1y$
- $(x+y)^2 = 1x^2 + 2xy + 1y^2$
- $(x+y)^3 = 1x^3 + 3x^2y + 3xy^2 + 1y^3$
- $(x+y)^4 = 1x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + 1y^4$

Notice that the coefficients of the terms match the numbers in **Pascal's Triangle**. But *why* do these coefficients match combinations (i.e. $\binom{n}{k}$)?

---

## 7.2 The "Choosing Box" Metaphor (Combinatorial Proof)

Let's demystify why $\binom{n}{k}$ appears in the expansion. We will expand $(x+y)^3$ term-by-term.

1. First, let's write out the product as three separate boxes:
   $$(x+y)^3 = \underbrace{(x+y)}_{\text{Box 1}} \cdot \underbrace{(x+y)}_{\text{Box 2}} \cdot \underbrace{(x+y)}_{\text{Box 3}}$$
2. When we multiply these out using the distributive law, every single term in the final sum is formed by **picking exactly one symbol** (either $x$ or $y$) from each of the three boxes.
   For example, if we pick $x$ from Box 1, $x$ from Box 2, and $y$ from Box 3, we get the term:
   $$x \cdot x \cdot y = x^2 y$$
3. What are all the possible terms we can form?
   - Pick $y$ from 0 boxes (so $x$ from 3 boxes) $\rightarrow x^3$
   - Pick $y$ from 1 box (so $x$ from 2 boxes) $\rightarrow x^2y$
   - Pick $y$ from 2 boxes (so $x$ from 1 box) $\rightarrow xy^2$
   - Pick $y$ from 3 boxes (so $x$ from 0 boxes) $\rightarrow y^3$
4. Now, **how many ways** can we form the term $x^2y$?
   To get $x^2y$, we must select exactly **one box** to contribute $y$ (the other two must contribute $x$).
   - We can choose Box 1 to contribute $y$ $\rightarrow yxx = x^2y$
   - We can choose Box 2 to contribute $y$ $\rightarrow xyx = x^2y$
   - We can choose Box 3 to contribute $y$ $\rightarrow xxy = x^2y$
   The number of ways to choose 1 box out of 3 is:
   $$\binom{3}{1} = 3 \text{ ways}$$
   Therefore, the term $x^2y$ must appear exactly 3 times in the expansion, meaning its coefficient is $\binom{3}{1} = 3$.

### Generalizing to $(x+y)^n$

If we expand $(x+y)^n$, we have $n$ boxes:
$$(x+y)^n = \underbrace{(x+y)(x+y)\cdots(x+y)}_{n \text{ boxes}}$$
- To form the term $x^{n-k} y^k$, we must choose exactly **$k$ boxes** out of the $n$ boxes to contribute a $y$ (the remaining $n-k$ boxes will automatically contribute $x$).
- The number of ways to choose $k$ boxes out of $n$ is:
  $$\binom{n}{k}$$
- Therefore, the coefficient of $x^{n-k} y^k$ in the expanded polynomial is exactly $\binom{n}{k}$.

This is a beautiful, rigorous combinatorial proof that explains the formula without any complex algebra!

---

## 7.3 Pascal's Triangle & Pascal's Identity

The coefficients $\binom{n}{k}$ are arranged in a triangular grid called **Pascal's Triangle**:

```
         1           n = 0
       1   1         n = 1
     1   2   1       n = 2
   1   3   3   1     n = 3
 1   4   6   4   1   n = 4
```

Each number in the triangle is the sum of the two numbers directly above it. This recursive property is stated as **Pascal's Identity**:

$$\boxed{\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}}$$

Let's prove this identity using two different methods.

### 1. Combinatorial Proof (The Star Player Story)

Suppose you are a coach forming a committee of $k$ students from a group of $n$ candidates. The number of ways to do this is $\binom{n}{k}$.

Now, let's pick one specific candidate, say **Sarah**, and split the problem into two mutually exclusive cases:
- **Case 1: Sarah is selected for the committee.**
  Since Sarah is already on the committee, we must choose the remaining $k-1$ members from the other $n-1$ candidates. 
  $$\text{Ways for Case 1} = \binom{n-1}{k-1}$$
- **Case 2: Sarah is NOT selected for the committee.**
  Since Sarah is excluded, we must choose all $k$ members of our committee from the other $n-1$ candidates.
  $$\text{Ways for Case 2} = \binom{n-1}{k}$$

Since these two cases cover all possibilities and do not overlap, the total number of ways to form the committee is the sum of the two cases:
$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k} \quad \text{Q.E.D.}$$

---

### 2. Algebraic Proof (Common Denominator)

Let's prove the same identity using the factorial definition of combinations: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.

$$\text{RHS} = \binom{n-1}{k-1} + \binom{n-1}{k} = \frac{(n-1)!}{(k-1)!(n-k)!} + \frac{(n-1)!}{k!(n-1-k)!}$$

To add these fractions, we find a common denominator. 
- The first denominator has $(k-1)!$ and $(n-k)!$.
- The second denominator has $k!$ (which is $k \cdot (k-1)!$) and $(n-1-k)!$ (which is $\frac{(n-k)!}{n-k}$).

We multiply the first fraction by $\frac{k}{k}$ and the second fraction by $\frac{n-k}{n-k}$:
$$= \frac{k \cdot (n-1)!}{k \cdot (k-1)!(n-k)!} + \frac{(n-k) \cdot (n-1)!}{k!(n-k) \cdot (n-1-k)!}$$
$$= \frac{k \cdot (n-1)!}{k!(n-k)!} + \frac{(n-k) \cdot (n-1)!}{k!(n-k)!}$$

Now that the denominators are identical, we combine the numerators:
$$= \frac{k \cdot (n-1)! + (n-k) \cdot (n-1)!}{k!(n-k)!}$$
Factor out $(n-1)!$ from the numerator:
$$= \frac{(n-1)! [k + n - k]}{k!(n-k)!} = \frac{(n-1)! [n]}{k!(n-k)!}$$
$$= \frac{n!}{k!(n-k)!} = \binom{n}{k} = \text{LHS} \quad \text{Q.E.D.}$$

Both proofs are valid, but the combinatorial proof explains *why* the relationship exists, while the algebraic proof verifies that the symbol mechanics work.

---

## 7.4 Deriving Famous Binomial Identities

The Binomial Theorem is a powerful tool for generating mathematical identities. By plugging in different values for $x$ and $y$, we get immediate results.

### 1. Sum of Binomial Coefficients
$$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$

**Proof:** Set $x = 1$ and $y = 1$ in the Binomial Theorem:
$$(1+1)^n = \sum_{k=0}^{n} \binom{n}{k} 1^{n-k} 1^k \implies 2^n = \sum_{k=0}^{n} \binom{n}{k}$$
*Intuition:* The sum of all subsets of a set of size $n$ is $2^n$.

### 2. Alternating Sum of Binomial Coefficients
$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$$

**Proof:** Set $x = 1$ and $y = -1$ in the Binomial Theorem:
$$(1-1)^n = \sum_{k=0}^{n} \binom{n}{k} 1^{n-k} (-1)^k \implies 0 = \sum_{k=0}^{n} (-1)^k \binom{n}{k}$$
*Intuition:* For any set of size $n \geq 1$, the number of subsets of even size is exactly equal to the number of subsets of odd size.

### 3. Weighted Sum of Binomial Coefficients
$$\sum_{k=0}^{n} k \binom{n}{k} = n 2^{n-1}$$

**Proof:** Start with the single-variable binomial expansion:
$$(1+x)^n = \sum_{k=0}^{n} \binom{n}{k} x^k$$
Differentiate both sides with respect to $x$:
$$n(1+x)^{n-1} = \sum_{k=0}^{n} k \binom{n}{k} x^{k-1}$$
Now, set $x = 1$:
$$n(1+1)^{n-1} = \sum_{k=0}^{n} k \binom{n}{k} 1^{k-1} \implies n 2^{n-1} = \sum_{k=0}^{n} k \binom{n}{k}$$

---

## 7.5 Newton's Extended Binomial Theorem

In generating functions, we frequently encounter expressions like $(1-x)^{-2}$ or $(1-x)^{-r}$. How do we expand these when the exponent is negative?

Isaac Newton generalized the Binomial Theorem to any real exponent $\alpha$ (negative integers, fractions, etc.):

$$(1+x)^\alpha = \sum_{n=0}^{\infty} \binom{\alpha}{n} x^n$$

### 1. The Generalized Binomial Coefficient

For a negative or fractional exponent, we cannot use factorials because factorials are only defined for non-negative integers. Instead, we use the falling factorial definition:

$$\boxed{\binom{\alpha}{n} = \frac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)}{n!}}$$

Notice that there are exactly $n$ factors in the numerator.

**Example:** Calculate $\binom{1/2}{3}$ (used in deriving Catalan numbers):
$$\binom{1/2}{3} = \frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\left(\frac{1}{2}-2\right)}{3!} = \frac{\frac{1}{2}\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)}{6} = \frac{\frac{3}{8}}{6} = \frac{1}{16}$$

---

### 2. Demystifying Negative Exponents (The Sign-Flipping Proof)

Let's expand $(1-x)^{-r}$ where $r$ is a positive integer. According to Newton's formula:
$$(1-x)^{-r} = \sum_{n=0}^{\infty} \binom{-r}{n} (-x)^n = \sum_{n=0}^{\infty} \binom{-r}{n} (-1)^n x^n$$

Let's expand the generalized binomial coefficient $\binom{-r}{n}$ and simplify it:
$$\binom{-r}{n} = \frac{(-r)(-r-1)(-r-2)\cdots(-r-n+1)}{n!}$$

1. In the numerator, there are exactly $n$ terms, and every single one is negative. Let's pull out a factor of $(-1)$ from each of the $n$ terms:
   $$\binom{-r}{n} = (-1)^n \frac{r(r+1)(r+2)\cdots(r+n-1)}{n!}$$
2. Look at the product in the numerator: $r(r+1)(r+2)\cdots(r+n-1)$. 
   This is an ascending product. We can write this in terms of standard factorials:
   $$r(r+1)\cdots(r+n-1) = \frac{(r+n-1)!}{(r-1)!}$$
3. Substitute this back into our coefficient expression:
   $$\binom{-r}{n} = (-1)^n \frac{(r+n-1)!}{n! (r-1)!}$$
4. Notice that $\frac{(r+n-1)!}{n! (r-1)!}$ is exactly the definition of the combination $\binom{n+r-1}{r-1}$:
   $$\binom{-r}{n} = (-1)^n \binom{n+r-1}{r-1}$$

Now, let's plug this coefficient back into our binomial expansion:
$$(1-x)^{-r} = \sum_{n=0}^{\infty} \left[ (-1)^n \binom{n+r-1}{r-1} \right] (-1)^n x^n$$
Since $(-1)^n \cdot (-1)^n = (-1)^{2n} = 1$ (the signs cancel out completely!):

$$\boxed{(1-x)^{-r} = \sum_{n=0}^{\infty} \binom{n+r-1}{r-1} x^n}$$

This is one of the most important formulas in generating functions. Now you know exactly where the signs go and why the coefficient is $\binom{n+r-1}{r-1}$ (which represents Stars and Bars)!

---

## 7.6 Practice Problems

### Problem 1: Specific Term Expansion
Find the coefficient of $x^6$ in the expansion of $\left(2x^2 - \frac{1}{x}\right)^9$.

<details><summary>Solution</summary>

Using the Binomial Theorem, the general term in the expansion is:
$$T_k = \binom{9}{k} (2x^2)^{9-k} \left(-\frac{1}{x}\right)^k = \binom{9}{k} 2^{9-k} x^{18-2k} (-1)^k x^{-k}$$
$$T_k = \binom{9}{k} 2^{9-k} (-1)^k x^{18-3k}$$

We want the term containing $x^6$, so we set the exponent equal to $6$:
$$18 - 3k = 6 \implies 3k = 12 \implies k = 4$$

Now, substitute $k = 4$ into the general term coefficient:
$$\text{Coefficient} = \binom{9}{4} 2^{9-4} (-1)^4 = \binom{9}{4} 2^5 (1)$$
$$\binom{9}{4} = \frac{9 \cdot 8 \cdot 7 \cdot 6}{4 \cdot 3 \cdot 2 \cdot 1} = 126$$
$$\text{Coefficient} = 126 \cdot 32 = 4032$$

So, the coefficient of $x^6$ is **$4032$** ✓

</details>

### Problem 2: Evaluate a Sum
Find the exact value of the sum:
$$\sum_{k=0}^{n} 3^k \binom{n}{k}$$

<details><summary>Solution</summary>

Compare this sum to the expansion in the Binomial Theorem:
$$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k$$

If we set $x = 1$ and $y = 3$:
$$(1+3)^n = \sum_{k=0}^{n} \binom{n}{k} 1^{n-k} 3^k = \sum_{k=0}^{n} 3^k \binom{n}{k}$$
Therefore:
$$\sum_{k=0}^{n} 3^k \binom{n}{k} = 4^n \quad \text{✓}$$

</details>

---

*→ Return to [[00 GF Index]] for the full overview.*
