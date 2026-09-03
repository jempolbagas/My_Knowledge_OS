# 🧠 Active Recall & Practice Drills: Aritmatika Modulo

Tujuan dari drills ini adalah menguji pemahaman intuitif dan perhitungan praktis mengenai kongruensi, invers modular, dan Teorema Sisa Tiongkok ([[Chinese Remainder Theorem|CRT]]).

---

## 📝 Practice Set 1 (Basic Drills)

### Q1: Perhitungan Modulo Dasar & Kongruensi
Tentukan apakah pernyataan kongruensi berikut **Benar** atau **Salah**. Buktikan jawaban Anda!
1. $38 \equiv 14 \pmod{12}$
2. $-7 \equiv 8 \pmod 5$
3. $100 \equiv 1 \pmod 9$

### Q2: Pencarian Invers Modular
Cari invers dari $3 \pmod{11}$. Tunjukkan proses perhitungan atau pengecekan Anda. 

### Q3: Solusi Persamaan Linier Kongruensi
Tentukan nilai $x$ (modulo 7) yang memenuhi persamaan berikut:
$$ 4x \equiv 5 \pmod 7 $$

### Q4: Studi Kasus Pengolahan Citra (Image Wrapping)
Misalkan sebuah indeks piksel pada sumbu X bergerak melebihi batas gambar akibat filter pergeseran. Jika lebar gambar adalah $N = 256$, dan posisi piksel baru adalah $x' = -45$. Di koordinat manakah posisi yang benar setelah dilakukan *circular wrapping* ($x' \pmod N$)?

---

## 🔑 Kunci Jawaban & Pembahasan (Set 1)

> [!check]- Klik untuk membuka Kunci Jawaban Set 1
> **Jawaban Q1:**
> 1. **Benar**. $38 - 14 = 24$. Karena $12 \mid 24$, maka $38 \equiv 14 \pmod{12}$.
> 2. **Benar**. $-7 - 8 = -15$. Karena $5 \mid -15$, maka $-7 \equiv 8 \pmod 5$.
> 3. **Benar**. $100 - 1 = 99$. Karena $9 \mid 99$, maka $100 \equiv 1 \pmod 9$. (Atau: $100 = 11 \cdot 9 + 1$).
>
> **Jawaban Q2:**
> Kita mencari nilai $x$ sehingga $3x \equiv 1 \pmod{11}$.
> Invers dari $3 \pmod{11}$ adalah **4** karena $3 \cdot 4 = 12 \equiv 1 \pmod{11}$.
>
> **Jawaban Q3:**
> $4x \equiv 5 \pmod 7$.
> Invers dari $4 \pmod 7$ adalah $2$ (karena $4 \cdot 2 = 8 \equiv 1 \pmod 7$).
> Kalikan kedua ruas dengan 2: $x \equiv 2 \cdot 5 = 10 \equiv 3 \pmod 7$.
>
> **Jawaban Q4:**
> $x' = -45 \pmod{256}$. Dalam matematika, $-45 = -1 \cdot 256 + 211$.
> Posisi piksel setelah *wrapping* berada pada indeks **211**.

---
---

## 📝 Practice Set 2 (Comprehensive Drills)

### Soal 1: Modulo Negatif & Sifat Dasar
Tentukan sisa hasil bagi terkecil non-negatif dari:
1. $-23 \pmod 7$
2. $17^{100} \pmod 5$

*Ruang Jawaban:*
- 

### Soal 2: Invers Modular & Kongruensi Linier ([[Invers Modular]])
Cari nilai $x$ positif terkecil yang memenuhi persamaan kongruensi linier berikut:
$$ 5x \equiv 3 \pmod{13} $$

*Ruang Jawaban:*
- 

### Soal 3: Eksponensiasi Modulo Besar
Tentukan dua digit terakhir (yaitu nilai $7^{402} \pmod{100}$) dari $7^{402}$.

*Ruang Jawaban:*
- 

### Soal 4: Teorema Sisa Tiongkok ([[Chinese Remainder Theorem]])
Cari bilangan bulat positif terkecil $x$ yang memenuhi sistem kongruensi berikut:
$$
\begin{aligned}
x &\equiv 2 \pmod 3 \\
x &\equiv 3 \pmod 5 \\
x &\equiv 2 \pmod 7
\end{aligned}
$$

*Ruang Jawaban:*
- 

### Soal 5: Aplikasi Praktis (Circular Wrapping / Signal Processing)
Dalam pemrosesan citra digital dengan lebar $N = 512$ piksel, pergeseran koordinat $x$ menggunakan aturan *circular wrapping* ($x_{\text{baru}} \pmod N$). Sebuah algoritma menggeser piksel dari posisi awal $x_0 = 120$ sejauh $k = -750$ langkah.  
Tentukan indeks piksel akhir $x_{\text{akhir}}$ pada rentang $0 \le x_{\text{akhir}} < 512$.

*Ruang Jawaban:*
- 

---

## 🔑 Kunci Jawaban & Pembahasan (Set 2)

> [!check]- Klik untuk membuka Kunci Jawaban Set 2
> **Jawaban Soal 1:**
> 1. $-23 = -4 \cdot 7 + 5 \implies -23 \equiv 5 \pmod 7$.
> 2. $17 \equiv 2 \pmod 5$. Karena $2^4 = 16 \equiv 1 \pmod 5$, maka $17^{100} \equiv (2^4)^{25} \equiv 1^{25} = 1 \pmod 5$.
> 
> **Jawaban Soal 2:**
> $5x \equiv 3 \pmod{13}$.
> Cari invers dari $5 \pmod{13}$: $5 \cdot 8 = 40 = 3 \cdot 13 + 1 \equiv 1 \pmod{13}$. Inversnya adalah $8$.
> Kalikan kedua ruas dengan $8$: $x \equiv 8 \cdot 3 = 24 \equiv 11 \pmod{13}$.
> 
> **Jawaban Soal 3:**
> Menggunakan fungsi Euler Totient $\phi(100) = 40$. Karena $\gcd(7, 100) = 1$, Teorema Euler menyatakan $7^{40} \equiv 1 \pmod{100}$.
> $7^{402} = (7^{40})^{10} \cdot 7^2 \equiv 1^{10} \cdot 49 = 49 \pmod{100}$.
> 
> **Jawaban Soal 4:**
> $M = 3 \cdot 5 \cdot 7 = 105$.
> - $m_1 = 35 \equiv 2 \pmod 3 \implies m_1^{-1} \equiv 2 \pmod 3$.
> - $m_2 = 21 \equiv 1 \pmod 5 \implies m_2^{-1} \equiv 1 \pmod 5$.
> - $m_3 = 15 \equiv 1 \pmod 7 \implies m_3^{-1} \equiv 1 \pmod 7$.
>
> $x \equiv (2 \cdot 35 \cdot 2 + 3 \cdot 21 \cdot 1 + 2 \cdot 15 \cdot 1) \pmod{105}$
> $x \equiv (140 + 63 + 30) = 233 \equiv 23 \pmod{105}$.
> 
> **Jawaban Soal 5:**
> $x_{\text{akhir}} = (120 - 750) \pmod{512} = -630 \pmod{512}$.
> $-630 = -2 \cdot 512 + 394 \implies x_{\text{akhir}} = 394$.
