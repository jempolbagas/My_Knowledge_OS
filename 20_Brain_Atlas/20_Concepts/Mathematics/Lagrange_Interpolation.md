---
type: concept
subject: Mathematics
source_hash: 8df6084569ef92443bd518c41900696e
source: "[[Shamir_vs_Pande_Modified_Secret_Sharing]]"
created: 2026-08-12
---

# Interpolasi Lagrange

**Interpolasi Lagrange** adalah metode analisis numerik untuk menemukan polinomial tunggal berderajat minimal yang melalui sekumpulan titik data $(x_0, y_0), (x_1, y_1), \dots, (x_k, y_k)$.

## Prinsip Saklar (Lagrange Basis)
Metode ini membentuk polinomial $P(x)$ tanpa perlu menyelesaikan sistem persamaan linear, melainkan dengan menjumlahkan **fungsi basis Lagrange** $\ell_i(x)$ yang berfungsi sebagai "saklar":

$$P(x) = \sum_{i=0}^{k} y_i \cdot \ell_i(x)$$

Fungsi basis $\ell_i(x)$ dirancang sedemikian rupa sehingga:
$$\ell_i(x_j) = \begin{cases} 1 & \text{jika } j = i \\ 0 & \text{jika } j \neq i \end{cases}$$

Formula fungsi basis $\ell_i(x)$ adalah:
$$\ell_i(x) = \prod_{\substack{0 \le j \le k \\ j \neq i}} \frac{x - x_j}{x_i - x_j} = \frac{(x - x_0)\dots(x - x_{i-1})(x - x_{i+1})\dots(x - x_k)}{(x_i - x_0)\dots(x_i - x_{i-1})(x_i - x_{i+1})\dots(x_i - x_k)}$$

## Keunggulan & Keterbatasan
- **Keunggulan:** Konstruksi langsung tanpa eliminasi matriks (seperti eliminasi Gauss). Sangat efisien untuk mencari nilai pada $x$ tertentu saja.
- **Keterbatasan:** Jika ada penambahan titik data baru, seluruh basis $\ell_i(x)$ harus dihitung ulang dari awal.

## Aplikasi dalam Kriptografi
Digunakan dalam [[Shamir_Secret_Sharing]] untuk memulihkan suku konstan rahasia $S = P(0)$ dari $t$ buah [[Suku_Banyak_Polinomial|share polinomial]].
