---
type: generated_reading
subject: Cybersecurity
source_url: "https://doi.org/10.1007/s11277-023-10315-5"
source_hash: "1380dde6540ae949ff00e2dfb902853d"
date_created: 2026-08-10
status: done
user_baseline: "Beginner (Step-by-step Lagrange & Finite Field Arithmetic)"
promoted_to:
  - "[[Shamir Secret Sharing]]"
  - "[[Modified Shamir Scheme]]"
---

# Deep Dive: Shamir's Secret Sharing Scheme & The Modified Shamir Algorithm in Pande et al. (2023)

## 1. Executive Summary & Fundamental Intuition

In classical cryptography, protecting a secret usually relies on holding a single private key. However, single-point-of-failure storage creates massive operational risks: if the keyholder loses the key, the secret is permanently lost; if an adversary compromises the keyholder, the secret is fully breached. 

**Secret Sharing Schemes (SSS)** resolve this dilemma by dividing a secret $S$ into $n$ distinct pieces called **shares** (or shadows), distributed among $n$ participants. Under a $(k, n)$-threshold access structure:
1. **Reconstruction Condition**: Any $k$ or more participants can collaborate to perfectly reconstruct the original secret $S$.
2. **Information-Theoretic Security Condition**: Any subset of fewer than $k$ participants (even $k-1$ colluding entities with infinite computing power) obtains **zero mathematical information** about the secret $S$.

![[diagram cybersecurity shamir polynomial interpolation.webp]]

### Intuition: The Geometric Property of Polynomials
The intuition behind Adi Shamir’s 1979 breakthrough scheme is rooted in elementary geometry:
- $1$ point is insufficient to define a line; infinitely many lines pass through a single point. But **$2$ distinct points** uniquely define a straight line (degree $1$ polynomial: $f(x) = a_1 x + a_0$).
- **$3$ distinct points** uniquely define a parabola (degree $2$ polynomial: $f(x) = a_2 x^2 + a_1 x + a_0$).
- In general, **$k$ distinct points** uniquely determine a polynomial of degree at most $k - 1$.

By encoding the secret $S$ as the constant term $f(0) = a_0$ of a degree $k-1$ random polynomial, and giving each participant $i$ a coordinate pair $(x_i, f(x_i))$, Shamir turned secret recovery into a polynomial interpolation problem.

---

## 2. Rigorous Mathematics: Shamir's $(k, n)$ Scheme

### 2.1 The Need for Finite Field Arithmetic ($\mathbb{GF}(p)$)
In real-number coordinate geometry ($\mathbb{R}$), an adversary holding $k-1$ points could eliminate many candidate polynomials and gain probabilistic information about $f(0)$. Furthermore, real-number operations suffer from floating-point rounding errors and unbounded values.

To achieve **perfect information-theoretic security** (in the sense of Claude Shannon), all calculations are performed over a **Finite Field** (Galois Field $\mathbb{GF}(p)$), where $p$ is a prime number strictly greater than both the secret $S$ and the number of participants $n$ ($p > \max(S, n)$).

In $\mathbb{GF}(p)$:
- All arithmetic operations (addition, subtraction, multiplication, division) are performed modulo $p$.
- Division by $b$ is executed as multiplication by the **modular multiplicative inverse** $b^{-1} \pmod p$, where $b \cdot b^{-1} \equiv 1 \pmod p$.
- Over $\mathbb{GF}(p)$, every element in $\{0, 1, \dots, p-1\}$ is equally likely to be the secret when fewer than $k$ shares are known, guaranteeing zero leakage.

### 2.2 Share Generation Protocol
To share a secret integer $S \in \mathbb{GF}(p)$ among $n$ participants with threshold $k$:

1. Choose a prime $p > \max(S, n)$.
2. Select $k-1$ random coefficients $a_1, a_2, \dots, a_{k-1}$ uniformly at random from $\mathbb{GF}(p)$, setting $a_0 = S$.
3. Construct the random degree $k-1$ polynomial:
   \[
   f(x) = S + a_1 x + a_2 x^2 + \dots + a_{k-1} x^{k-1} \pmod p
   \]
4. Evaluate $f(x)$ at $n$ distinct non-zero evaluation points $x_1, x_2, \dots, x_n \in \mathbb{GF}(p) \setminus \{0\}$.
5. Distribute share $(x_i, y_i)$ to participant $i$, where $y_i = f(x_i) \pmod p$.

### 2.3 Secret Reconstruction via Lagrange Interpolation
Given $k$ shares $(x_1, y_1), (x_2, y_2), \dots, (x_k, y_k)$, the unique polynomial $f(x)$ of degree $k-1$ is reconstructed using **Lagrange Interpolation Basis Polynomials** $\ell_j(x)$:

\[
\ell_j(x) = \prod_{\substack{m=1 \\ m \neq j}}^{k} \frac{x - x_m}{x_j - x_m} \pmod p
\]

Notice that $\ell_j(x_j) = 1$ and $\ell_j(x_m) = 0$ for all $m \neq j$. Thus, the polynomial $f(x)$ is given by:

\[
f(x) = \sum_{j=1}^{k} y_j \cdot \ell_j(x) \pmod p
\]

Since we only need the secret $S = f(0)$, we evaluate the Lagrange basis polynomials at $x = 0$:

\[
\ell_j(0) = \prod_{\substack{m=1 \\ m \neq j}}^{k} \frac{0 - x_m}{x_j - x_m} = \prod_{\substack{m=1 \\ m \neq j}}^{k} \frac{-x_m}{x_j - x_m} \pmod p
\]

The secret $S$ is recovered directly as:

\[
S = f(0) = \sum_{j=1}^{k} y_j \cdot \ell_j(0) \pmod p
\]

---

## 3. The Modified Shamir Scheme in Pande et al. (2023)

In paper s11277-023-10315-5 (*Dinesh Pande, Arjun Singh Rawat, Maroti Deshmukh, Maheep Singh*, 2023), the authors present a hybrid image encryption and secret sharing framework combining **Reverse Chinese Remainder Theorem (RCRT)**, a **Modified Shamir Scheme**, and **Bitwise XOR operations**.

![[diagram cybersecurity pande modified shamir pipeline.webp]]

### 3.1 Key Architectural Shift: Deterministic Coefficients
In standard Shamir SSS:
- The secret is $a_0 = S$.
- Coefficients $a_1, \dots, a_{k-1}$ are **random junk values** discarded after share generation.

In **Pande et al.’s Modified Shamir Scheme**:
- There are **no random junk coefficients**.
- Instead, the polynomial coefficients **ARE** the $n$ primary shares $\{PS_1, PS_2, \dots, PS_n\}$ obtained from applying Reverse CRT on the secret image $I$ with a coprime set $\{P_1, P_2, \dots, P_n\}$.

Specifically, for each pixel location, the authors construct a polynomial $F(P)$ of degree $n-1$:

\[
F(P) = PS_1 + PS_2 \cdot P + PS_3 \cdot P^2 + \dots + PS_n \cdot P^{n-1} \pmod{251}
\]

### 3.2 Share Generation Pipeline Steps
1. **Reverse CRT Step (Primary Share Generation)**:
   Given a secret pixel intensity $I$ and coprime set $P = \{P_1, P_2, \dots, P_n\}$, generate $n$ primary shares:
   \[
   PS_i = I \pmod{P_i} \quad \forall i \in \{1, 2, \dots, n\}
   \]
2. **Modified Shamir Step (Intermediate Share Generation)**:
   Evaluate the polynomial $F(P)$ at the coprime values $P_1, P_2, \dots, P_n$ modulo $251$ (a prime close to 255 for 8-bit pixels):
   \[
   IS_i = F(P_i) = \left( \sum_{m=1}^{n} PS_m \cdot P_i^{m-1} \right) \pmod{251} \quad \forall i \in \{1, 2, \dots, n\}
   \]
3. **Randomized Image & XOR Phase**:
   Compute a randomized mask image $R$ by XORing all intermediate shares:
   \[
   R = IS_1 \oplus IS_2 \oplus \dots \oplus IS_n
   \]
   Finally, construct the final encrypted shares $S_i$ by XORing $IS_i$ with the transpose of the randomized image $R^T$:
   \[
   S_i = IS_i \oplus R^T \quad \forall i \in \{1, 2, \dots, n\}
   \]

### 3.3 Reconstruction Protocol
1. Reconstruct $R$ by XORing all final shares: $R = S_1 \oplus S_2 \oplus \dots \oplus S_n$.
2. Recover intermediate shares: $IS_i = S_i \oplus R^T$.
3. Compute Lagrange basis polynomials $Z_i(P)$ over coprimes $P_1, \dots, P_n$:
   \[
   Z_i(P) = \prod_{\substack{j=1 \\ j \neq i}}^{n} \frac{P - P_j}{P_i - P_j}
   \]
   Reconstruct the full polynomial $F(P) = \sum_{i=1}^n IS_i \cdot Z_i(P)$.
4. Extract the coefficients of $F(P)$, which yield the recovered primary shares $\{PS_1, PS_2, \dots, PS_n\}$.
5. Apply standard CRT on $\{PS_1, \dots, PS_n\}$ and $\{P_1, \dots, P_n\}$ to reconstruct the original secret pixel $I$.

---

## 4. Step-by-Step Worked Numerical Example

Let's work through a complete, verifiable numerical example step-by-step.

### Step A: Classical Shamir $(2, 3)$ Example
- Secret $S = 42$. Prime modulus $p = 97$.
- Threshold $k = 2$, Participants $n = 3$.
- Choose 1 random coefficient: $a_1 = 15$.
- Polynomial: $f(x) = (42 + 15x) \pmod{97}$.

**Share Generation**:
- $x_1 = 1 \implies y_1 = (42 + 15(1)) \bmod 97 = 57$. Share 1 = $(1, 57)$.
- $x_2 = 2 \implies y_2 = (42 + 15(2)) \bmod 97 = 72$. Share 2 = $(2, 72)$.
- $x_3 = 3 \implies y_3 = (42 + 15(3)) \bmod 97 = 87$. Share 3 = $(3, 87)$.

**Secret Reconstruction using Shares 1 & 3 ($(1, 57)$ and $(3, 87)$)**:
We evaluate $\ell_1(0)$ and $\ell_3(0)$ modulo $97$:
1. $\ell_1(0) = \frac{0 - x_3}{x_1 - x_3} = \frac{-3}{1 - 3} = \frac{-3}{-2} = \frac{3}{2} \pmod{97}$.
   - Modular inverse of $2 \pmod{97}$: Since $2 \times 49 = 98 \equiv 1 \pmod{97}$, $2^{-1} \equiv 49 \pmod{97}$.
   - $\ell_1(0) = (3 \times 49) \bmod 97 = 147 \bmod 97 = 50$.
2. $\ell_3(0) = \frac{0 - x_1}{x_3 - x_1} = \frac{-1}{3 - 1} = \frac{-1}{2} \pmod{97}$.
   - $\ell_3(0) = (-1 \times 49) \bmod 97 = -49 \equiv 48 \pmod{97}$.
3. Reconstruct $S = f(0)$:
   \[
   S = (y_1 \cdot \ell_1(0) + y_3 \cdot \ell_3(0)) \bmod 97
   \]
   \[
   S = (57 \times 50 + 87 \times 48) \bmod 97 = (2850 + 4176) \bmod 97 = 7026 \bmod 97
   \]
   $7026 = 72 \times 97 + 42 \implies 7026 \bmod 97 = \mathbf{42}$.
   **The secret $S = 42$ is reconstructed perfectly!**

---

## 5. Production-Grade Python Implementation

Below is a complete, runnable Python 3 script demonstrating both classic Shamir Secret Sharing over $\mathbb{GF}(p)$ and the Pande et al. (2023) Modified Shamir pipeline.

```python
import random
from typing import List, Tuple

# Helper: Extended Euclidean Algorithm for Modular Inverse
def mod_inverse(a: int, m: int) -> int:
    def egcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    a = a % m
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"Modular inverse for {a} mod {m} does not exist.")
    return x % m

# ---------------------------------------------------------
# Part 1: Classic Shamir (k, n) Secret Sharing Scheme
# ---------------------------------------------------------
class ClassicShamir:
    def __init__(self, k: int, n: int, prime: int = 251):
        self.k = k
        self.n = n
        self.prime = prime

    def split_secret(self, secret: int) -> List[Tuple[int, int]]:
        if secret >= self.prime:
            raise ValueError("Secret must be less than prime modulus.")
        
        # Random coefficients a1 ... a_{k-1}
        coeffs = [secret] + [random.randint(1, self.prime - 1) for _ in range(self.k - 1)]
        
        shares = []
        for x in range(1, self.n + 1):
            y = 0
            for power, coeff in enumerate(coeffs):
                y = (y + coeff * (x ** power)) % self.prime
            shares.append((x, y))
        return shares

    def recover_secret(self, shares: List[Tuple[int, int]]) -> int:
        if len(shares) < self.k:
            raise ValueError(f"At least {self.k} shares required for reconstruction.")
        
        shares = shares[:self.k]
        secret = 0
        
        for j, (xj, yj) in enumerate(shares):
            numerator = 1
            denominator = 1
            for m, (xm, _) in enumerate(shares):
                if m != j:
                    numerator = (numerator * (-xm)) % self.prime
                    denominator = (denominator * (xj - xm)) % self.prime
            
            lagrange_coeff = (numerator * mod_inverse(denominator, self.prime)) % self.prime
            secret = (secret + yj * lagrange_coeff) % self.prime
            
        return secret

# ---------------------------------------------------------
# Part 2: Pande et al. (2023) Modified Shamir Scheme Engine
# ---------------------------------------------------------
def modified_shamir_encode(primary_shares: List[int], coprimes: List[int], mod: int = 251) -> List[int]:
    """
    Evaluates polynomial F(P) = PS1 + PS2*P + PS3*P^2 + ... + PSn*P^(n-1) mod 251
    at points P_1, P_2, ... P_n.
    """
    n = len(primary_shares)
    intermediate_shares = []
    
    for p_i in coprimes:
        val = 0
        for idx, ps in enumerate(primary_shares):
            val = (val + ps * (p_i ** idx)) % mod
        intermediate_shares.append(val)
        
    return intermediate_shares

def modified_shamir_decode(intermediate_shares: List[int], coprimes: List[int], mod: int = 251) -> List[int]:
    """
    Reconstructs polynomial F(P) via Lagrange Interpolation over field mod 251,
    extracting coefficients [PS1, PS2, ..., PSn].
    """
    n = len(intermediate_shares)
    recovered_coefficients = [0] * n
    
    # Lagrange polynomial reconstruction
    for j in range(n):
        xj = coprimes[j]
        yj = intermediate_shares[j]
        
        # Build basis polynomial l_j(P)
        # l_j(P) = prod_{m!=j} (P - xm) / (xj - xm)
        poly = [1]
        denom = 1
        for m in range(n):
            if m != j:
                xm = coprimes[m]
                denom = (denom * (xj - xm)) % mod
                # Multiply current poly by (P - xm)
                new_poly = [0] * (len(poly) + 1)
                for deg, c in enumerate(poly):
                    new_poly[deg] = (new_poly[deg] - c * xm) % mod
                    new_poly[deg + 1] = (new_poly[deg + 1] + c) % mod
                poly = new_poly
                
        inv_denom = mod_inverse(denom, mod)
        scaled_poly = [(c * inv_denom * yj) % mod for c in poly]
        
        for deg in range(len(scaled_poly)):
            recovered_coefficients[deg] = (recovered_coefficients[deg] + scaled_poly[deg]) % mod
            
    return recovered_coefficients

# Demonstration Test
if __name__ == "__main__":
    print("=== Testing Classic Shamir (2, 3) Scheme ===")
    shamir = ClassicShamir(k=2, n=3, prime=97)
    secret_val = 42
    shares = shamir.split_secret(secret_val)
    print(f"Original Secret: {secret_val}")
    print(f"Generated Shares: {shares}")
    reconstructed = shamir.recover_secret(shares[:2])
    print(f"Reconstructed Secret (using 2 shares): {reconstructed}\n")
    
    print("=== Testing Pande et al. (2023) Modified Shamir Core ===")
    primary_shares = [12, 45, 78] # Primary shares from Reverse CRT
    coprimes = [3, 5, 7]           # Coprime evaluation points
    
    inter_shares = modified_shamir_encode(primary_shares, coprimes)
    print(f"Primary Shares (Coefficients): {primary_shares}")
    print(f"Coprimes (Points): {coprimes}")
    print(f"Intermediate Shares: {inter_shares}")
    
    recovered_ps = modified_shamir_decode(inter_shares, coprimes)
    print(f"Recovered Primary Shares: {recovered_ps}")
    assert primary_shares == recovered_ps, "Reconstruction failed!"
    print("SUCCESS: Modified Shamir reconstruction mathematically verified!")
```

---

## 6. Trade-offs, Edge Cases & Failure Modes

| Metric / Dimension | Classic Shamir SSS | Pande et al. (2023) Modified Shamir |
| :--- | :--- | :--- |
| **Threshold Access Structure** | Flexible $(k, n)$-threshold ($k \le n$) | Strict $(n, n)$-threshold (All $n$ shares required) |
| **Polynomial Degree** | $k - 1$ | $n - 1$ |
| **Coefficients** | $a_0 = S$, $a_1 \dots a_{k-1}$ random junk | $a_0 \dots a_{n-1}$ are primary shares $PS_1 \dots PS_n$ |
| **Share Randomness** | High (random polynomial) | Extremely High (hybrid RCRT + Modified Shamir + $R^T$ XOR) |
| **Computation Complexity** | $O(k^2)$ per pixel | $O(n^2)$ per pixel + RCRT/CRT cost |
| **Fault Tolerance** | Can tolerate up to $n - k$ lost or corrupted shares | **Zero fault tolerance** (Missing 1 share prevents degree $n-1$ polynomial recovery) |

### Key Limitation & Strategic Pivot for KTI Gemastik
1. **The $(n,n)$ Bottleneck in Pande et al.**:
   Because Pande et al. use all $n$ primary shares $PS_1 \dots PS_n$ as coefficients of a degree $n-1$ polynomial, **Lagrange interpolation requires all $n$ distinct points $(P_i, IS_i)$** to solve for the $n$ unknown coefficients. If even a single share is destroyed or missing, the linear system is underdetermined, and recovery fails completely.
2. **KTI Research Opportunity (The Pivot)**:
   For the Gemastik KTI paper, the research objective is to **upgrade Pande et al.'s framework from an $(n, n)$ single-secret scheme into a flexible $(k, n)$ multi-secret sharing scheme**, combining the lightweight performance of CRT/XOR with robust threshold fault tolerance.

---

## 7. Complete Source Map & Citations

1. **Pande, D., Rawat, A. S., Deshmukh, M., & Singh, M. (2023)**. *Single Secret Sharing Scheme Using Chinese Remainder Theorem, Modified Shamir’s Scheme and XOR Operation*. Wireless Personal Communications, 130(2), 957–985. DOI: [10.1007/s11277-023-10315-5](https://doi.org/10.1007/s11277-023-10315-5).
2. **Shamir, A. (1979)**. *How to share a secret*. Communications of the ACM, 22(11), 612–613.
3. **ZKDocs Protocol Primitives**: *Shamir's Secret Sharing Scheme Specification*. URL: `https://www.zkdocs.com/docs/zkdocs/protocol-primitives/shamir/`
4. **Decentralized Thoughts**: *Polynomial Secret Sharing and the Lagrange Basis*. URL: `https://decentralizedthoughts.github.io/2020-07-17-polynomial-secret-sharing-and-the-lagrange-basis/`
5. **Horcrux Implementation Guide**: *Implementing Shamir's Secret Sharing in Rust*. URL: `https://gendignoux.com/blog/2021/11/01/horcrux-1-math.html`
