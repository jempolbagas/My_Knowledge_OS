---
type: concept
subject: Cybersecurity
source_hash: 1380dde6540ae949ff00e2dfb902853d
source: "[[Shamir vs Pande Modified Secret Sharing]]"
created: 2026-08-10
---

# Modified Shamir Scheme (Pande et al., 2023)

**Modified Shamir Scheme** adalah varian dari Shamir's Secret Sharing Scheme yang diperkenalkan oleh Dinesh Pande et al. (2023) untuk enkripsi citra digital sensitif.

## Perbedaan Utama dengan Classical Shamir SSS
1. **Koefisien Polinomial**: Tidak menggunakan koefisien acak ($a_1 \dots a_{k-1}$). Sebaliknya, seluruh $n$ koefisien polinomial $F(P) = PS_1 + PS_2 \cdot P + \dots + PS_n \cdot P^{n-1} \pmod{251}$ adalah **Primary Shares** $\{PS_1, PS_2, \dots, PS_n\}$ hasil dari Reverse CRT.
2. **Access Structure**: Mengubah skema threshold $(k, n)$ menjadi skema $(n, n)$ deterministik, di mana seluruh $n$ share dibutuhkan untuk merekonstruksi polinomial derajat $n-1$.
3. **Integrasi Pipeline**: Hasil evaluasi titik $IS_i = F(P_i) \pmod{251}$ di-XOR dengan ranspose gambar teracak $R^T$ untuk menghasilkan *encrypted randomized shares*.

## Evaluasi & Limitasi KTI
- **Kelebihan**: Sangat efisien, komputasi ringan (modulus 251 dekat dengan byte 255), dan tingkat acak citra (NPCR ~99.99%, UACI ~33.33%) sangat tinggi.
- **Kelemahan**: **Zero fault tolerance**. Kehilangan 1 share membatalkan rekonstruksi polinomial secara total. Ini menjadi peluang pivot riset Gemastik KTI untuk mengembangkan skema $(k, n)$ multi-secret.
