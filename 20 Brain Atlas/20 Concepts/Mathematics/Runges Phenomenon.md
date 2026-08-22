---
type: concept
subject: Mathematics
source_hash: c78a2e1d03429bc4892e87a9120bc129
created: 2026-08-19
---

# Fenomena Runge (Runge's Phenomenon)

**Fenomena Runge** adalah keterbatasan utama dalam interpolasi polinomial di mana kurva interpolasi berderajat tinggi mengalami **osilasi ekstrem di dekat ujung interval** ketika titik-titik sampel berjarak sama (*equidistant nodes*).

## Penyebab Matematik

Untuk $n+1$ titik data, error interpolasi $E(x) = f(x) - P_n(x)$ dirumuskan sebagai:

$$E(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod_{i=0}^{n} (x - x_i)$$

Ketika $n \to \infty$ pada titik sampel ekuidistan:
1. Suku produk $\prod_{i=0}^{n} (x - x_i)$ tumbuh sangat cepat mendekati batas interval ($x \to x_0$ atau $x \to x_n$).
2. Turunan ke-$(n+1)$ dari fungsi $f(x)$ dapat tumbuh lebih cepat daripada pembagi $(n+1)!$.

Akibatnya, menaikkan derajat polinomial $n$ **tidak membuat hasil interpolasi semakin akurat**, melainkan memperbesar error osilasi di ujung interval.

## Contoh Fungsi Runge

$$f(x) = \frac{1}{1 + 25x^2} \quad \text{pada } x \in [-1, 1]$$

- Untuk $n$ kecil (misal $n=4$), kurva belum presisi tetapi stabil.
- Untuk $n$ besar (misal $n=10$ atau $20$), kurva akurat di $x=0$, tetapi meledak berosilasi tajam saat mendekati $x = -1$ dan $x = 1$.

## Solusi / Mitigasi

1. **[[Interpolation|Interpolasi Spline]] (Cubic Splines):** Membagi interval menjadi potongan-potongan kecil dan menerapkan polinomial derajat rendah (derajat 3) pada tiap potongan.
2. **Titik Chebyshev (*Chebyshev Nodes*):** Mengubah distribusi titik sampel agar lebih rapat di ujung interval daripada di tengah:
   $$x_k = \cos\left(\frac{2k+1}{2n+2} \pi\right)$$
