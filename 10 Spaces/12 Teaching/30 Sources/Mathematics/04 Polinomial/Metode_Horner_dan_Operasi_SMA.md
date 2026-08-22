---
title: "Metode Horner dan Operasi Polinomial"
type: materi
subject: Mathematics
level: sma
target_audience: "SMA Kelas 11"
created: 2026-08-20
sources:
  - "[[Suku Banyak Polinomial SMA]]"
tags:
  - teaching-material
  - mathematics
  - suku-banyak
  - polinomial
  - metode-horner
---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | [[Konsep_dan_Kesamaan_Polinomial_SMA|⬅️ Konsep Polinomial]] | Modul Ini | [[Teorema_Sisa_dan_Faktor_SMA|Teorema Sisa ➡️]] | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]

# Metode Horner dan Operasi Polinomial 🧮

Salah satu hal paling menantang dari polinomial adalah saat kita harus mengevaluasi nilainya atau membaginya dengan polinomial lain. Untungnya, William George Horner menemukan trik luar biasa yang disebut **Skema Horner**!

---

## 1. Menghitung Nilai Polinomial

Misalkan kita punya fungsi polinomial $f(x)$. Nilai polinomial untuk $x = k$ dinotasikan sebagai $f(k)$. Ada 2 metode:

### 1.1 Metode Substitusi
Mengganti langsung setiap variabel $x$ pada polinomial dengan angka $k$.

**Contoh:**  
Hitung nilai $f(x) = 2x^3 - 4x^2 + 3x - 5$ untuk $x = 3$.
$$f(3) = 2(3)^3 - 4(3)^2 + 3(3) - 5$$
$$f(3) = 2(27) - 4(9) + 9 - 5$$
$$f(3) = 54 - 36 + 9 - 5 = 22$$

*Kekurangan:* Jika derajat polinomial sangat tinggi, perhitungan manual menjadi sangat panjang.

---

## 2. Metode Horner Standar (Evaluasi & Pembagi Linear)

Metode Horner meminimalkan operasi perkalian melalui skema visual bertingkat. Selain untuk menghitung nilai, metode ini sekaligus mencari **Hasil Bagi** dan **Sisa Pembagian**.

### 📋 Prosedur:
1. **Urutkan Koefisien:** Tuliskan seluruh koefisien secara mendatar (dari pangkat tertinggi ke 0). Jika ada pangkat yang hilang, beri angka **$0$**.
2. **Letakkan Pembuat Nol:** Tulis $k$ di sebelah kiri garis vertikal.
3. Turunkan angka pertama.
4. Kalikan angka bawah dengan $k$, tulis di kolom berikutnya baris kedua, lalu **Jumlahkan**. Ulangi hingga akhir.
5. **Angka paling kanan** = Nilai Fungsi $f(k)$ / Sisa Pembagian ($S$).
6. **Angka lainnya di baris bawah** = Koefisien Hasil Bagi ($H(x)$).

### ✏️ Contoh 1: Pembagian $(x - k)$
Tentukan Hasil Bagi dan Sisa jika $P(x) = 2x^4 - 3x^3 + 5x - 8$ dibagi oleh $(x - 2)$.

**Penyelesaian:**
Pembagi: $x - 2 = 0 \implies k = 2$. (Perhatikan suku $x^2$ tidak ada, koefisien = 0).

```text
  2  |   2    -3     0     5    -8
     |         4     2     4    18
-----+-------------------------------- (+)
         2     1     2     9  |  10
```

* **Sisa Pembagian ($S$):** $10$
* **Koefisien $H(x)$:** Derajat $P(x)$ adalah 4, maka derajat $H(x)$ adalah 3.
  $$\mathbf{H(x) = 2x^3 + x^2 + 2x + 9}$$

---

## 3. Metode Horner Pembagi $(ax + b)$

Bagaimana jika pembaginya punya angka di depan $x$, misal $(3x - 2)$?

### 📋 Penyesuaian Wajib:
1. Pembuat nol: $ax + b = 0 \implies k = -\frac{b}{a}$.
2. Jalankan skema Horner seperti biasa.
3. **ATURAN EMAS:** Hasil Bagi yang sebenarnya adalah koefisien skema **dibagi dengan $a$**! 
   $$H(x) = \frac{H_{\text{skema}}(x)}{a}$$
4. Sisa pembagian ($S$) **TIDAK PERLU** dibagi $a$.

### ✏️ Contoh 2:
Tentukan Hasil Bagi dan Sisa $P(x) = 3x^3 + 7x^2 - 11x + 4$ dibagi $(3x - 2)$.

1. Pembagi $3x - 2 = 0 \implies x = \frac{2}{3}$ (maka $k = \frac{2}{3}$, $a = 3$).
2. Koefisien: $3, 7, -11, 4$.

```text
 2/3 |   3     7   -11     4
     |         2     6    -10
-----+--------------------------- (+)
         3     9    -5  | -6
```

* **Sisa Pembagian ($S$):** $-6$
* **Hasil Bagi Sebenarnya $H(x)$:** Bagikan koefisien skema dengan $a = 3$:
  $$H(x) = \frac{3x^2 + 9x - 5}{3} = \mathbf{x^2 + 3x - \frac{5}{3}}$$

---

## 4. Metode Horner-Kino (Pembagi Kuadrat $ax^2 + bx + c$)

**Horner-Kino** digunakan untuk pembagi kuadrat **tanpa perlu memfaktorkan** pembaginya terlebih dahulu!

### 📋 Prosedur Cepat:
1. Hitung dua pengali:
   * $k_1 = -\frac{c}{a}$ (Pengali atas, baris 1)
   * $k_2 = -\frac{b}{a}$ (Pengali bawah, baris 2)
2. Buat tabel Horner 3 baris. Beri tanda bintang $(*)$ pada: Kolom 1 (dua-duanya), Kolom 2 (atas saja), Kolom terakhir (bawah saja).
3. Jalankan pola kali dan jumlah seperti biasa dari kiri ke kanan.
4. **2 kolom terakhir** adalah sisa pembagian $S(x) = s_1 x + s_0$. Kolom sisanya adalah koefisien hasil bagi (ingat bagi $a$ jika $a \neq 1$).

### ✏️ Contoh 3 (Horner-Kino):
Tentukan Hasil Bagi dan Sisa dari $P(x) = x^4 - 3x^3 + 5x^2 - 7x + 6$ dibagi oleh $x^2 - 2x + 3$.

* Pembagi: $x^2 - 2x + 3 \implies a = 1, b = -2, c = 3$.
* Pengali: $k_1 = -3$ dan $k_2 = 2$.
* Koefisien $P(x)$: $1, -3, 5, -7, 6$.

```text
 k1 = -3 |   *     *    -3      3     -6
 k2 =  2 |   *     2    -2     -4      *
---------+---------------------------------- (+)
             1    -1      0  | -8      0
             ^     ^      ^     ^      ^
          Koefisien H(x)     Sisa S(x)
```

* **Hasil Bagi $H(x)$:** Koefisien: $1, -1, 0 \implies \mathbf{H(x) = x^2 - x}$
* **Sisa Pembagian $S(x)$:** $s_1 = -8, s_0 = 0 \implies \mathbf{S(x) = -8x}$

---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | [[Konsep_dan_Kesamaan_Polinomial_SMA|⬅️ Konsep Polinomial]] | Modul Ini | [[Teorema_Sisa_dan_Faktor_SMA|Teorema Sisa ➡️]] | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]
