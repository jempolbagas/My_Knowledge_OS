---
type: concept
subject: Mathematics
source_hash: "66e12d9252a0cc3e9ac35ebb4ee78657"
source: "[[Single_Secret_Sharing_CRT_Shamir_XOR]]"
created: 2026-08-05
---

# Chinese Remainder Theorem (CRT)

**Chinese Remainder Theorem (CRT)** adalah teorema teori bilangan yang menyatakan bahwa jika kita memiliki himpunan modulo coprime $\{P_1, P_2, \dots, P_n\}$ dan sisa bagi $\{r_1, r_2, \dots, r_n\}$, maka terdapat satu solusi tunggal $x$ modulo $M = P_1 \times P_2 \times \dots \times P_n$ yang memenuhi seluruh sistem kongruensi linear:

$$x \equiv r_i \pmod{P_i} \quad \text{untuk } i = 1, 2, \dots, n$$

## Formula Rekonstruksi
Solusi unik $x$ dihitung dengan:
$$x = \left( \sum_{i=1}^{n} r_i \cdot m_i \cdot m_i^{-1} \right) \bmod M$$
di mana $m_i = \frac{M}{P_i}$ dan $m_i^{-1}$ adalah invers kuadratik/multiplikatif dari $m_i \pmod{P_i}$.

## Aplikasi Kriptografi
- **Reverse CRT (RCRT):** Digunakan untuk memecah data acak/piksel rahasia menjadi komponen sisa bagi (*shares*).
- **Dekripsi Cepat:** Digunakan dalam RSA dan *Secret Sharing Schemes* untuk mempercepat kalkulasi modulo tanpa kehilangan akurasi data (*lossless*).
