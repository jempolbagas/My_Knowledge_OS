---
type: concept
subject: Mathematics
source_hash: "a5494b3c28edc219b1379c83ee67b3d3"
created: 2026-08-05
---
# Invers Modular

**Invers Modular** (*Modular Multiplicative Inverse*) dari sebuah bilangan bulat $A$ terhadap modulo $m$ adalah bilangan bulat $y$ sedemikian rupa sehingga hasil kali $A \cdot y$ jika dibagi $m$ menghasilkan sisa $1$:

$$A \cdot y \equiv 1 \pmod m$$

Dalam notasi matematika, $y$ sering ditulis sebagai $A^{-1} \pmod m$.

## Alasan Penamaan "Invers Modular"

1. **Invers (Kebalikan):** Pada aritmatika biasa, invers perkalian dari $A$ adalah $\frac{1}{A}$ karena $A \cdot \frac{1}{A} = 1$. Dalam [[Kongruensi Modular]], pecahan tidak diizinkan, sehingga posisi $\frac{1}{A}$ digantikan oleh bilangan bulat $y$.
2. **Modular:** Sifat kebalikan ini tidak mutlak, melainkan terikat pada nilai modulo $m$ tertentu. Nilai $y$ berbeda-beda tergantung nilai $m$.

## Syarat Keberadaan
Invers modular dari $A \pmod m$ **hanya ada** jika $A$ dan $m$ bersifat [[Coprime]] (artinya $\gcd(A, m) = 1$).

## Contoh
Cari invers dari $3 \pmod 7$:
- Kita mencari $y$ sehingga $(3 \cdot y) \pmod 7 = 1$.
- Untuk $y = 5 \rightarrow 3 \cdot 5 = 15 \equiv 1 \pmod 7$.
- Jadi, invers modular dari $3 \pmod 7$ adalah $5$.

## Kegunaan
- Digunakan dalam [[Chinese Remainder Theorem]] untuk menghitung komponen bobot rekonstruksi.
- Kunci utama dalam algoritma kriptografi seperti RSA dan *Elliptic Curve Cryptography* (ECC).
