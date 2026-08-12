---
type: concept
subject: Cybersecurity
source_hash: "1380dde6540ae949ff00e2dfb902853d"
source: "[[Shamir_Secret_Sharing_and_Modified_Pande_Scheme]]"
created: 2026-08-05
---

# Shamir's Secret Sharing

**Shamir's Secret Sharing** adalah algoritma kriptografi $(t, n)$ threshold yang dikembangkan oleh Adi Shamir pada tahun 1979. Algoritma ini membagi rahasia $S$ dengan memanfaatkan sifat polinomial derajat $t-1$:

$$f(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_{t-1} x^{t-1} \pmod p$$

di mana konstanta $a_0 = S$ adalah data rahasia yang disembunyikan.

## Prinsip Kerja
1. **Generasi Share:** Evaluasi fungsi $f(x)$ pada $n$ titik independen $x_1, x_2, \dots, x_n$. Setiap partisipan menerima pasangan titik $(x_i, f(x_i))$.
2. **Rekonstruksi Rahasia:** Menggunakan [[Lagrange_Interpolation]] dari minimal $t$ titik untuk menemukan kembali koefisien $a_0 = S$.

## Keunggulan
- **Information-Theoretic Security:** Kurang dari $t$ share tidak memberikan informasi sedikit pun tentang rahasia $S$.
- **Fleksibilitas:** Nilai $t$ dan $n$ dapat disesuaikan tanpa mengubah struktur dasar algoritma.
