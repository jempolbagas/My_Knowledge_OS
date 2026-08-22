# ⚡ Aritmatika Modulo Cheatsheet

Referensi ringkas mengenai operasi, identitas, dan algoritma utama pada Aritmatika Modulo.

---

## 1. Operasi Dasar dan Kongruensi
Sifat-sifat dasar jika $a \equiv b \pmod n$ dan $c \equiv d \pmod n$:

- **Penjumlahan:** $a + c \equiv b + d \pmod n$
- **Pengurangan:** $a - c \equiv b - d \pmod n$
- **Perkalian:** $a \cdot c \equiv b \cdot d \pmod n$
- **Eksponensial:** $a^k \equiv b^k \pmod n$ (Pangkat harus bilangan non-negatif eksak, tidak dimodulokan dengan $n$ kecuali menggunakan Teorema Euler/Fermat).

## 2. Invers Modular
Invers dari $a \pmod n$ adalah sebuah nilai $x$ sedemikian hingga:
$$ a \cdot x \equiv 1 \pmod n $$
- **Syarat Ada Invers:** $FPB(a, n) = 1$ ($a$ dan $n$ saling prima).
- **Pencarian Algoritmik:** Menggunakan *Extended Euclidean Algorithm*.

## 3. Teorema Kecil Fermat (Fermat's Little Theorem)
Jika $p$ adalah bilangan prima dan $a$ adalah bilangan bulat yang tidak habis dibagi $p$, maka:
$$ a^{p-1} \equiv 1 \pmod p $$
**Kegunaan Praktis:** Mencari invers modular jika modulus adalah bilangan prima $p$.
Invers dari $a \pmod p$ adalah $a^{p-2} \pmod p$.

## 4. Fungsi Totient Euler ($\phi(n)$) & Teorema Euler
Perluasan dari Teorema Fermat untuk sembarang modulus $n$.
$$ a^{\phi(n)} \equiv 1 \pmod n $$
(Dengan syarat $FPB(a, n) = 1$).
- $\phi(n)$ menghitung jumlah bilangan bulat positif kurang dari $n$ yang saling prima dengan $n$.
- Jika $p$ prima, $\phi(p) = p - 1$.
- Jika modulus $n$ adalah hasil kali dua prima $p$ dan $q$ (misalnya di RSA kriptografi), maka $\phi(n) = (p-1)(q-1)$.

## 5. Chinese Remainder Theorem (CRT)
Digunakan untuk menyelesaikan sistem persamaan:
$x \equiv a_1 \pmod{m_1}$
$x \equiv a_2 \pmod{m_2}$
$\dots$

**Formula Solusi:**
$$ x = \sum_{i=1}^k a_i \cdot M_i \cdot y_i \pmod M $$
Dimana:
- $M = m_1 \cdot m_2 \dots m_k$
- $M_i = \frac{M}{m_i}$
- $y_i = (M_i)^{-1} \pmod{m_i}$

## 6. Aplikasi Umum di Ilmu Komputer
- **Pengolahan Citra (PCD):** *Circular shifts*, Padding/Wrapping tepi.
- **Pengolahan Sinyal (PSD):** Transformasi domain periodik seperti *Fast Fourier Transform* (FFT).
- **Kriptografi:** RSA (faktorisasi prima dan modular eksponensiasi), Diffie-Hellman Key Exchange.
- **Hashing:** Hash function ringan (misalnya $H(x) = x \pmod p$) untuk mendistribusikan data ke tabel *hash*.
