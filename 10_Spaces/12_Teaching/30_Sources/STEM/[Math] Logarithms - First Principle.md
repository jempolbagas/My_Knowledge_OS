---
title: "[Math] Logarithms - First Principle"
course: ""
tags: []
aliases: ["[Math] Logarithms - First Principle"]
created: "2026-05-13"
---
# Logarithms - First Principle

## 🏛️ 1. The Historical Intuition: Why Logarithms?
Before calculators, scientists (like Kepler and Newton) had to multiply massive numbers for astronomy. Multiplication is hard; addition is easy. 

John Napier invented logarithms to create a "bridge" where:
**Multiplication in the "Normal World" $\rightarrow$ Addition in the "Log World"**

By converting numbers into their logarithms, they could add the logs and then convert the result back to get the product. This shifted the cognitive load from multiplication to simple addition.

---

## 🧩 2. The Fundamental Definition
At its core, a logarithm is an **inverse operation**. If exponentiation asks *"What is the result of $b^x$?"*, the logarithm asks *"What exponent $x$ do I need to turn $b$ into $y$?"*

### The Mathematical Bridge
$$b^x = y \iff \log_b(y) = x$$

**Conditions:**
- $b > 0$ and $b \neq 1$ (The base must be positive and not one).
- $y > 0$ (You cannot take the log of a negative number or zero in the real number system).

**Example Walkthrough:**
- $\log_2(16) = 4$ because $2^4 = 16$
- $\log_5(125) = 3$ because $5^3 = 125$
- $\log_{10}(0.1) = -1$ because $10^{-1} = 0.1$

---

## 📜 3. The Laws of Logarithms (First Principle Derivations)
The laws of logarithms are simply the laws of exponents written "backwards."

### A. The Product Rule
$$\log_b(M \cdot N) = \log_b(M) + \log_b(N)$$
**Derivation:** 
Let $\log_b(M) = x \rightarrow b^x = M$
Let $\log_b(N) = y \rightarrow b^y = N$
Then $M \cdot N = b^x \cdot b^y = b^{x+y}$
Converting back to log: $\log_b(M \cdot N) = x + y = \log_b(M) + \log_b(N)$.

### B. The Quotient Rule
$$\log_b\left(\frac{M}{N}\right) = \log_b(M) - \log_b(N)$$
**Derivation:** 
Following the same logic, $\frac{M}{N} = \frac{b^x}{b^y} = b^{x-y}$.
Thus, $\log_b\left(\frac{M}{N}\right) = x - y = \log_b(M) - \log_b(N)$.

### C. The Power Rule
$$\log_b(M^k) = k \cdot \log_b(M)$$
**Derivation:** 
If $M = b^x$, then $M^k = (b^x)^k = b^{kx}$.
Thus, $\log_b(M^k) = kx = k \cdot \log_b(M)$.

---

## 🌟 4. Special Logarithms & The Natural Base

### Common Logarithm ($\log_{10}$)
When no base is written (e.g., $\log x$), it is usually assumed to be base 10. This is used widely in science for scales (pH, Richter, Decibels).

### The Natural Logarithm ($\ln$)
The Natural Log ($\ln$) uses the base $e$ (Euler's number $\approx 2.71828$).
$$\ln(x) = \log_e(x)$$
**Why $e$?** $e$ is the base of continuous growth. In calculus, the derivative of $e^x$ is $e^x$, making it the most "natural" base for describing growth and decay in the universe.

### Change of Base Formula
To calculate a log with any base using a standard calculator:
$$\log_b(a) = \frac{\ln(a)}{\ln(b)} \quad \text{or} \quad \frac{\log_{10}(a)}{\log_{10}(b)}$$

---

## 🛠️ 5. Strategy for Solving Logarithmic Equations
To solve for $x$, we generally use two main strategies:

### Strategy 1: Convert to Exponential Form
If the equation is simple: $\log_b(x) = a \rightarrow x = b^a$.
*Example:* $\log_3(x) = 2 \rightarrow x = 3^2 = 9$.

### Strategy 2: Use Log Properties to Condense
If there are multiple logs:
1. Use Product/Quotient/Power rules to combine all logs into one.
2. Solve using the exponential form.
*Example:* $\log_2(x) + \log_2(x-2) = 3$
$\log_2(x(x-2)) = 3$
$x^2 - 2x = 2^3$
$x^2 - 2x - 8 = 0 \rightarrow (x-4)(x+2) = 0$
*Check for validity:* $x=4$ (Valid), $x=-2$ (Invalid, since we can't take $\log$ of negative).

---

## ⚠️ 6. Common Pitfalls (The "Danger Zone")
Students often make these mistakes. **These are NOT true:**
- $\log(A + B) \neq \log A + \log B$ (Log of sum is NOT sum of logs)
- $\frac{\log A}{\log B} \neq \log(A - B)$ (Division of logs is NOT the quotient rule)
- $(\log A)^k \neq k \log A$ (The power must be on the argument $A$, not the whole log)

---

## 📈 7. Summary Table for Quick Reference

| Feature | Exponent Form | Logarithm Form | Key Insight |
| :--- | :--- | :--- | :--- |
| **Definition** | $b^x = y$ | $\log_b(y) = x$ | Log is the exponent. |
| **Product** | $b^m \cdot b^n = b^{m+n}$ | $\log(MN) = \log M + \log N$ | Multi $\rightarrow$ Add |
| **Quotient** | $b^m / b^n = b^{m-n}$ | $\log(M/N) = \log M - \log N$ | Div $\rightarrow$ Sub |
| **Power** | $(b^m)^n = b^{mn}$ | $\log(M^k) = k \log M$ | Power $\rightarrow$ Multi |
| **Natural** | $e^x = y$ | $\ln(y) = x$ | Continuous growth |
