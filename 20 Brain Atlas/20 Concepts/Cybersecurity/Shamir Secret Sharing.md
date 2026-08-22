---
type: concept
subject: Cybersecurity
source_hash: "b256af68983e465a14456c26ec57d66e"
source: "[[Shamir Secret Sharing Comprehensive Study Guide]]"
created: 2026-08-05
updated: 2026-08-14
---

# Shamir's Secret Sharing

**Shamir's Secret Sharing (SSS)** adalah algoritma kriptografi $(k, n)$ threshold yang dikembangkan oleh Adi Shamir pada tahun 1979. Algoritma ini membagi rahasia $S$ ke dalam $n$ bagian (*shares*) dengan memanfaatkan sifat interpolasi polinomial derajat $k-1$:

$$f(x) = (a_0 + a_1 x + a_2 x^2 + \dots + a_{k-1} x^{k-1}) \pmod p$$

di mana konstanta $a_0 = S$ adalah data rahasia yang disembunyikan dan $p$ adalah bilangan prima ($p > S$ dan $p > n$).

## Prinsip Kerja
1. **Generasi Share:** Evaluasi fungsi $f(x)$ pada $n$ titik independen $x_1, x_2, \dots, x_n$. Setiap partisipan menerima pasangan titik $(x_i, f(x_i))$.
2. **Rekonstruksi Rahasia:** Menggunakan [[Lagrange Interpolation]] dari minimal $k$ titik untuk menemukan kembali koefisien $a_0 = S$ pada titik $x = 0$.

## Keamanan Sempurna & Aritmatika Medan Terhingga ($\mathbb{GF}(p)$)
Aritmatika polinomial standar pada bilangan bulat ($\mathbb{Z}$) atau riil ($\mathbb{R}$) memiliki dua kelemahan utama:
- **Kebocoran Informasi (*Information Leakage*):** Kepemilikan $k-1$ share pada domain bilangan bulat mengurangi ruang pencarian rahasia (misalnya, mengetahui titik share genap membocorkan sifat paritas rahasia).
- **Galat Pembulatan:** Pembagian pecahan biasa menimbulkan presisi numerik yang hilang.

Penggunaan aritmatika modulo prima $p$ ($\mathbb{GF}(p)$) menghasilkan **Perfect Secrecy** (Information-Theoretic Security):
- Titik-titik share tersebar secara acak di $\{0, 1, \dots, p-1\}$.
- Memegang $k-1$ share tidak memberikan informasi apapun tentang $S$; semua $p$ kemungkinan nilai $S$ tetap memiliki probabilitas yang sama persis.
- Operasi pembagian digantikan dengan perkalian [[Invers Modular]] via Algoritma Euklides Terperluas.

## Related Readings & Concepts
- [[Lagrange Interpolation]]
- [[Invers Modular]]
- [[Secret Sharing Scheme]]
- [[Shamir vs Pande Modified Secret Sharing]]

