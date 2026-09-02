---
title: "LKPD: Suku Banyak (Polinomial)"
type: lkpd
subject: mathematics
level: sma
target_audience: "SMA Kelas 11"
created: 2026-07-28
sources:
  - "[[Mempelajari Konsep dan Nilai Suku Banyak (Polinomial)]]"
  - "[[Suku Banyak Polinomial SMA]]"
  - "[[Konsep_dan_Kesamaan_Polinomial_SMA]]"
  - "[[Metode_Horner_dan_Operasi_SMA]]"
  - "[[Teorema_Sisa_dan_Faktor_SMA]]"
  - "[[Pemfaktoran_dan_Akar_Rasional_SMA]]"
  - "[[Teorema_Vieta_Polinomial_SMA]]"
tags:
  - worksheet
  - practice
  - mathematics
  - suku-banyak
  - polinomial
  - metode-horner
---

# Lembar Kerja Peserta Didik (LKPD): Suku Banyak (Polinomial) 📝

---

## BAGIAN I: Lembar Kerja Peserta Didik (LKPD)

**Nama Kelompok:** ____________________  
**Kelas / Kelompok:** ____________________  
**Anggota Kelompok:** 
1. ______________________
2. ______________________
3. ______________________
4. ______________________

---

### Aktivitas 1: Detektif Polinomial (Eksplorasi Group)

**Petunjuk:** Periksalah bentuk-bentuk aljabar berikut bersama kelompokmu! Tentukan apakah bentuk tersebut merupakan **Polinomial** atau **Bukan Polinomial**. Berikan alasan logis kelompokmu!

| No. | Bentuk Aljabar | Polinomial / Bukan Polinomial | Alasan Kelompok | Derajat & Suku Tetap (Jika Polinomial) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | $3x^4 - 2x^3 + 5x - 7$ | | | Derajat: ____<br>Konstanta: ____ |
| 2 | $x^2 + \frac{4}{x^2} - 1$ | | | Derajat: ____<br>Konstanta: ____ |
| 3 | $2x^3 - 5\sqrt{x} + 6$ | | | Derajat: ____<br>Konstanta: ____ |
| 4 | $x(x - 3)(x + 2)$ | | | Derajat: ____<br>Konstanta: ____ |
| 5 | $\frac{x^3 + 2x^2 - 5}{3}$ | | | Derajat: ____<br>Konstanta: ____ |

---

### Aktivitas 2: Battle of Methods (Substitusi vs Horner vs Horner-Kino)

**Petunjuk:** Selesaikan dua permasalahan berikut menggunakan **dua metode berbeda** bersama kelompokmu. Isilah langkah-langkahnya pada tabel di bawah ini!

#### Soal A: Hitung Nilai Polinomial $P(x) = 2x^4 - 5x^3 + 3x - 4$ untuk $x = 3$.

| Metode | Langkah Penyelesaian Utama | Hasil Akhir $P(3)$ |
| :--- | :--- | :--- |
| **1. Metode Substitusi** | Substitusikan $x = 3$ langsung:<br>$P(3) = 2(3)^4 - 5(3)^3 + 3(3) - 4 = \dots$ | $P(3) = \dots$ |
| **2. Metode Horner Standar** | Susun koefisien suku ($x^4, x^3, x^2, x^1, x^0$):<br>*(Ingat: Koefisien $x^2 = 0$!)*<br>Jalankan skema Horner dengan $k = 3$. | $P(3) = \dots$ |

#### Soal B: Tentukan Hasil Bagi $H(x)$ dan Sisa $S(x)$ dari $P(x) = x^4 - 2x^3 + 4x^2 - 5x + 3$ dibagi oleh $x^2 - x + 2$.

| Metode | Langkah Penyelesaian Utama | Hasil Bagi $H(x)$ & Sisa $S(x)$ |
| :--- | :--- | :--- |
| **Metode Horner-Kino** | $a = 1, b = -1, c = 2$<br>$k_1 = -\frac{c}{a} = \dots$<br>$k_2 = -\frac{b}{a} = \dots$<br>Susun tabel 3 baris dengan pengatur tanda asteriks $*$. | $H(x) = \dots$<br>$S(x) = \dots$ |

---

### Aktivitas 3: Studi Kasus HOTS (Aplikasi Dunia Nyata)

**Kasus:**  
Sebuah perusahaan manufaktur membuat lembaran kardus berbentuk persegi panjang untuk membuat wadah kemasan produk.  
Volume wadah kemasan tersebut (dalam $\text{cm}^3$) sebagai fungsi dari panjang lipatan $x$ (dalam cm) dapat dimodelkan oleh polinomial berikut:

$$V(x) = 4x^3 - 60x^2 + 200x$$

**Tugas Kelompok:**
1. Tentukan derajat, suku utama, dan konstanta dari fungsi volume $V(x)$ di atas!
2. Jika panjang lipatan kardus dirancang sebesar $x = 4\text{ cm}$, hitunglah volume kemasan tersebut dengan menggunakan **Metode Horner**!
3. Jika wadah tersebut dipotong dan dibagi ke dalam sub-kemasan kecil dengan faktor penyusutan $(2x - 4)$, gunakan **Metode Horner Pembagi $(ax + b)$** untuk menentukan hasil bagi fungsi volume dan sisa ruang yang tidak terpakai!

---

## BAGIAN II: Latihan Soal Mandiri (Evaluasi)

### A. Pilihan Ganda (HOTS)

1. Diketahui polinomial $P(x) = (2x^2 - 3)(x^3 + 4x - 1)$. Derajat dan konstanta dari polinomial $P(x)$ berturut-turut adalah...
   A. Derajat $5$ dan konstanta $3$  
   B. Derajat $5$ dan konstanta $-3$  
   C. Derajat $6$ dan konstanta $3$  
   D. Derajat $6$ dan konstanta $-3$  

2. Jika nilai polinomial $f(x) = x^4 - 2x^3 + px^2 + 4x - 5$ untuk $x = 2$ adalah $7$, maka nilai $p$ adalah...
   A. $1$  
   B. $2$  
   C. $3$  
   D. $4$  

3. Hasil bagi $H(x)$ dan sisa $S$ dari pembagian polinomial $P(x) = 2x^3 - 5x^2 + 8x - 4$ oleh $(2x - 1)$ adalah...
   A. $H(x) = x^2 - 2x + 3$ dan $S = -1$  
   B. $H(x) = 2x^2 - 4x + 6$ dan $S = -1$  
   C. $H(x) = x^2 - 2x + 3$ dan $S = 1$  
   D. $H(x) = 2x^2 - 4x + 6$ dan $S = 1$  

4. Sisa pembagian polinomial $P(x) = x^4 - 3x^3 + 5x^2 - 6x + 8$ oleh $x^2 - 3x + 2$ dengan menggunakan metode Horner-Kino adalah...
   A. $S(x) = -x + 6$  
   B. $S(x) = x - 6$  
   C. $S(x) = -x - 6$  
   D. $S(x) = 2x + 4$  

5. Diketahui $(x - 2)$ dan $(x + 1)$ merupakan faktor-faktor dari polinomial $P(x) = x^3 + ax^2 - 5x + b$. Nilai $a + b$ adalah...
   A. $-4$  
   B. $-2$  
   C. $2$  
   D. $4$  

---

### B. Soal Uraian Penalaran

1. **Horner Standar & Evaluasi Nilai:**  
   Hitunglah nilai polinomial $P(x) = 3x^5 - 2x^3 + 7x^2 - 12$ untuk $x = -2$ menggunakan **Skema Horner**. Jelaskan mengapa kamu harus mencantumkan angka $0$ pada kolom tertentu dalam skema tersebut!

2. **Pembagian Pembagi Linear $(ax + b)$:**  
   Tentukan Hasil Bagi $H(x)$ dan Sisa Pembagian $S$ dari polinomial $P(x) = 4x^3 - 6x^2 + 5x - 1$ dibagi oleh $(2x - 3)$. Tunjukkan secara rinci penyesuaian koefisien skema yang kamu lakukan untuk mendapatkan Hasil Bagi yang sebenarnya!

3. **Horner-Kino & Analisis Teorema Faktor:**  
   Gunakan **Metode Horner-Kino** untuk menentukan sisa pembagian dari $P(x) = x^4 - x^3 - 7x^2 + 13x - 6$ oleh $x^2 - x - 6$. Berdasarkan sisa pembagian yang diperoleh, simpulkan apakah $x^2 - x - 6$ merupakan faktor dari $P(x)$ atau bukan! Berikan alasanmu!

---

## BAGIAN III: Kunci Jawaban, Pembahasan & Rubrik Penilaian

### Kunci Jawaban LKPD

#### Aktivitas 1:
1. **Polinomial** — Pangkat semua variabel bulat positif (4, 3, 1). Derajat: $4$, Konstanta: $-7$.
2. **Bukan Polinomial** — Ada suku $\frac{4}{x^2} = 4x^{-2}$ (pangkat negatif $-2$).
3. **Bukan Polinomial** — Ada suku $5\sqrt{x} = 5x^{1/2}$ (pangkat pecahan $1/2$).
4. **Polinomial** — Jika dikalikan $x(x^2 - x - 6) = x^3 - x^2 - 6x$. Derajat: $3$, Konstanta: $0$.
5. **Polinomial** — Merupakan $\frac{1}{3}x^3 + \frac{2}{3}x^2 - \frac{5}{3}$. Derajat: $3$, Konstanta: $-\frac{5}{3}$.

#### Aktivitas 2:
* **Soal A:** Kedua cara menghasilkan $P(3) = 2(81) - 5(27) + 3(3) - 4 = 162 - 135 + 9 - 4 = \mathbf{32}$.
* **Soal B (Horner-Kino):**  
  $k_1 = -2, k_2 = 1$.  
  Hasil Bagi $H(x) = \mathbf{x^2 - x + 1}$, Sisa $S(x) = \mathbf{-2x + 1}$.

#### Aktivitas 3:
1. Derajat $= 3$, Suku utama $= 4x^3$, Konstanta $= 0$.
2. Skema Horner untuk $x = 4$ pada $V(x) = 4x^3 - 60x^2 + 200x + 0$:  
   Nilai $V(4) = \mathbf{96\text{ cm}^3}$.
3. Pembagi $2x - 4 \implies k = 2$, $a = 2$.  
   Skema Horner memberikan koefisien $4, -52, 96$ dan Sisa $= 192$.  
   Hasil bagi sebenarnya $H(x) = \frac{4x^2 - 52x + 96}{2} = \mathbf{2x^2 - 26x + 48}$.  
   Sisa ruang $= \mathbf{192\text{ cm}^3}$.

---

### Kunci Jawaban & Pembahasan Latihan Soal Mandiri

#### Pilihan Ganda:
1. **Jawaban: B**  
   *Pembahasan:* Pangkat tertinggi $= 2 + 3 = 5$. Konstanta $= (-3) \times (-1) = 3$.  
   *Correction:* Perkalian $(-3) \times (-1) = +3$. Derajat 5, Konstanta $+3$. Pilihan A! (Jawaban: **A**).

2. **Jawaban: C**  
   *Pembahasan:* $f(2) = (2)^4 - 2(2)^3 + p(2)^2 + 4(2) - 5 = 7$  
   $16 - 16 + 4p + 8 - 5 = 7 \implies 4p + 3 = 7 \implies 4p = 4 \implies p = 1$. Pilihan **A**!

3. **Jawaban: A**  
   *Pembahasan:* Pembagi $2x - 1 \implies k = \frac{1}{2}, a = 2$.  
   Koefisien: $2, -5, 8, -4$.  
   Skema: $2 \to (2 \cdot \frac{1}{2} - 5 = -4) \to (-4 \cdot \frac{1}{2} + 8 = 6) \to (6 \cdot \frac{1}{2} - 4 = -1)$.  
   Koefisien skema: $2, -4, 6$. Sisa $S = -1$.  
   Hasil bagi $H(x) = \frac{2x^2 - 4x + 6}{2} = x^2 - 2x + 3$. Jawaban: **A**.

4. **Jawaban: A**  
   *Pembahasan:* Pembagi $x^2 - 3x + 2 \implies k_1 = -2, k_2 = 3$.  
   Tabel Horner-Kino menghasilkan Sisa $s_1 = -1, s_0 = 6 \implies S(x) = -x + 6$. Jawaban: **A**.

5. **Jawaban: B**  
   *Pembahasan:* $P(2) = 8 + 4a - 10 + b = 0 \implies 4a + b = 2$.  
   $P(-1) = -1 + a + 5 + b = 0 \implies a + b = -4$.  
   Eliminasi: $3a = 6 \implies a = 2$, maka $b = -6$.  
   Nilai $a + b = 2 + (-6) = -4$. Jawaban: **A**!

---

#### Uraian:
1. **Pembahasan Uraian 1:**  
   Polinomial: $3x^5 + 0x^4 - 2x^3 + 7x^2 + 0x - 12$.  
   Angka $0$ harus dicantumkan pada suku $x^4$ dan $x^1$ karena skema Horner mensyaratkan koefisien terurut dari pangkat tertinggi hingga nol secara lengkap. Jika tidak diberi 0, derajat polinomial akan bergeser dan hasilnya salah.  
   Skema Horner dengan $k = -2$: Hasil nilai $P(-2) = \mathbf{-36}$.

2. **Pembahasan Uraian 2:**  
   $P(x) = 4x^3 - 6x^2 + 5x - 1$ dibagi $(2x - 3) \implies k = \frac{3}{2}, a = 2$.  
   Koefisien: $4, -6, 5, -1$.  
   Skema Horner dengan $k = 3/2$:  
   * Turun $4$.  
   * $4 \times \frac{3}{2} = 6 \implies -6 + 6 = 0$.  
   * $0 \times \frac{3}{2} = 0 \implies 5 + 0 = 5$.  
   * $5 \times \frac{3}{2} = \frac{15}{2} \implies -1 + \frac{15}{2} = \frac{13}{2}$.  
   Koefisien skema: $4, 0, 5$. Sisa $S = \frac{13}{2}$.  
   Hasil bagi sebenarnya: $H(x) = \frac{4x^2 + 0x + 5}{2} = \mathbf{2x^2 + \frac{5}{2}}$.

3. **Pembahasan Uraian 3:**  
   Pembagi $x^2 - x - 6 \implies a = 1, b = -1, c = -6 \implies k_1 = 6, k_2 = 1$.  
   Koefisien: $1, -1, -7, 13, -6$.  
   Skema Horner-Kino:  
   Kolom sisa menghasilkan $s_1 = 0$ dan $s_0 = 0 \implies S(x) = 0$.  
   **Kesimpulan:** Karena Sisa Pembagian $S(x) = 0$, berdasarkan **Teorema Faktor**, maka $x^2 - x - 6$ **merupakan faktor** dari $P(x) = x^4 - x^3 - 7x^2 + 13x - 6$.

---

### Rubrik Penilaian

| Bentuk Soal | Jumlah Soal | Skor Maksimal per Soal | Total Skor |
| :--- | :--- | :--- | :--- |
| Pilihan Ganda | 5 | 10 | 50 |
| Uraian No. 1 | 1 | 15 | 15 |
| Uraian No. 2 | 1 | 15 | 15 |
| Uraian No. 3 | 1 | 20 | 20 |
| **Total Skor Maksimal** | | | **100** |

$$\text{Nilai Akhir} = \frac{\text{Total Skor yang Diperoleh}}{\text{Total Skor Maksimal (100)}} \times 100$$
