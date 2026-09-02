---
title: "Persamaan Matriks dan Sistem Persamaan Linear (SPL) SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 11 (Fase F), Guru Matematika, dan Pembelajar Mandiri"
created: 2026-09-02
sources:
  - "[[Matriks SMA]]"
  - "[[Determinan_Matriks_dan_Sifatnya_SMA]]"
  - "[[Minor_Kofaktor_dan_Invers_Matriks_SMA]]"
  - "[[LKPD Matriks SMA]]"
tags:
  - teaching/mathematics
  - mathematics/linear-algebra
  - level/sma
  - topic/matrix-equations-and-cramer
---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Minor_Kofaktor_dan_Invers_Matriks_SMA|⬅️ Modul 4: Invers Matriks]] | **Modul 5: Persamaan & SPL** | [[LKPD Matriks SMA|📝 LKPD & Latihan Soal]]

---

# Persamaan Matriks dan Sistem Persamaan Linear (SPL) — Solusi Cerdas Masalah Multivariabel 📐💡

Pernahkah kamu membayangkan bagaimana teknisi kelistrikan menganalisis arus di 10 titik cabang sirkuit yang rumit, atau bagaimana pakar ekonomi memprediksi harga keseimbangan ratusan komoditas di pasar global? 

Di SMP, kita belajar menyelesaikan Sistem Persamaan Linear Dua Variabel (SPLDV) menggunakan metode eliminasi dan substitusi. Namun, jika jumlah variabel bertambah menjadi 3, 5, atau bahkan 1.000 variabel, metode eliminasi manual akan sangat memakan waktu dan rawan keliru. Di sinilah **Aljabar Matriks** menunjukkan kekuatan sesungguhnya!

Dengan mengubah sistem persamaan menjadi persamaan matriks berbentuk **$AX = B$**, seluruh sistem dapat diselesaikan secara sistematis melalui **Metode Invers Matriks** atau **Aturan Cramer (*Cramer's Rule*)**. Mari kita kuasai tekniknya secara mendalam!

---

## 1. Aljabar Persamaan Matriks

Karena perkalian matriks **TIDAK BERSIFAT KOMUTATIF** ($AB \neq BA$), posisi perkalian invers matriks menjadi faktor paling menentukan.

Misalkan $A, B,$ dan $X$ adalah matriks-matriks yang ordonya bersesuaian, dan $A$ memiliki invers ($A^{-1}$):

### A. Persamaan Tipe 1: $A \cdot X = B$ (Matriks yang Dicari Berada di Kanan)
Untuk mengisolasi matriks $X$, kita harus mengalikan **kedua ruas dari sebelah KIRI** dengan $A^{-1}$:

$$\begin{aligned}
A \cdot X &= B \\
A^{-1} \cdot (A \cdot X) &= A^{-1} \cdot B \\
(A^{-1} \cdot A) \cdot X &= A^{-1} \cdot B \\
I \cdot X &= A^{-1} \cdot B \\
\mathbf{X} &= \mathbf{A^{-1} \cdot B}
\end{aligned}$$

---

### B. Persamaan Tipe 2: $X \cdot A = B$ (Matriks yang Dicari Berada di Kiri)
Untuk mengisolasi matriks $X$, kita harus mengalikan **kedua ruas dari sebelah KANAN** dengan $A^{-1}$:

$$\begin{aligned}
X \cdot A &= B \\
(X \cdot A) \cdot A^{-1} &= B \cdot A^{-1} \\
X \cdot (A \cdot A^{-1}) &= B \cdot A^{-1} \\
X \cdot I &= B \cdot A^{-1} \\
\mathbf{X} &= \mathbf{B \cdot A^{-1}}
\end{aligned}$$

> [!WARNING]
> **Jebakan Fatal Aljabar Matriks!**  
> * Jika $A \cdot X = B \implies X = A^{-1} \cdot B$ (Invers di depan).
> * Jika $X \cdot A = B \implies X = B \cdot A^{-1}$ (Invers di belakang).  
> **Jangan pernah tertukar!** Menulis $X = B \cdot A^{-1}$ untuk persamaan $AX = B$ adalah kesalahan fatal karena $A^{-1}B \neq BA^{-1}$.

---

### C. Persamaan Tipe 3: Bentuk Komposit $A \cdot X \cdot B = C$
Jika matriks $X$ diapit oleh matriks $A$ di sebelah kiri dan matriks $B$ di sebelah kanan:
1. Kalikan kedua ruas dari kiri dengan $A^{-1}$:
   $$X \cdot B = A^{-1} \cdot C$$
2. Kalikan kedua ruas dari kanan dengan $B^{-1}$:
   $$\mathbf{X = A^{-1} \cdot C \cdot B^{-1}}$$

---

## 2. Mengubah Sistem Persamaan Linear (SPL) ke Bentuk Matriks

Setiap sistem persamaan linear dapat dipecah menjadi tiga komponen matriks utama:
1. **Matriks Koefisien ($A$):** Matriks yang berisi seluruh angka koefisien di depan variabel.
2. **Matriks Variabel ($X$):** Vektor kolom yang memuat variabel yang ingin dicari ($x, y, z$).
3. **Matriks Konstanta ($B$):** Vektor kolom yang memuat nilai konstanta di ruas kanan persamaan.

### A. Pada SPLDV (2 Variabel):
$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases} \iff \underbrace{\begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix}}_{A} \underbrace{\begin{pmatrix} x \\ y \end{pmatrix}}_{X} = \underbrace{\begin{pmatrix} c_1 \\ c_2 \end{pmatrix}}_{B}$$

### B. Pada SPLTV (3 Variabel):
$$\begin{cases} a_1 x + b_1 y + c_1 z = d_1 \\ a_2 x + b_2 y + c_2 z = d_2 \\ a_3 x + b_3 y + c_3 z = d_3 \end{cases} \iff \underbrace{\begin{pmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{pmatrix}}_{A} \underbrace{\begin{pmatrix} x \\ y \\ z \end{pmatrix}}_{X} = \underbrace{\begin{pmatrix} d_1 \\ d_2 \\ d_3 \end{pmatrix}}_{B}$$

---

## 3. Metode 1: Penyelesaian SPL Menggunakan Invers Matriks

Karena bentuk persamaan matriksnya adalah $A \cdot X = B$, maka himpunan penyelesaiannya langsung didapatkan dari formula:

$$X = A^{-1} \cdot B$$

### Untuk SPLDV:
$$\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{a_1 b_2 - b_1 a_2} \begin{pmatrix} b_2 & -b_1 \\ -a_2 & a_1 \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$

#### Contoh Kasus SPLDV:
Selesaikan sistem persamaan berikut dengan metode invers:
$$\begin{cases} 2x + 3y = 8 \\ 3x - y = 1 \end{cases}$$

1. Tuliskan dalam bentuk matriks $AX = B$:
   $$\begin{pmatrix} 2 & 3 \\ 3 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 8 \\ 1 \end{pmatrix}$$
2. Hitung $\det(A)$:
   $$\det(A) = 2(-1) - 3(3) = -2 - 9 = -11$$
3. Cari $A^{-1}$:
   $$A^{-1} = \frac{1}{-11} \begin{pmatrix} -1 & -3 \\ -3 & 2 \end{pmatrix} = \frac{1}{11} \begin{pmatrix} 1 & 3 \\ 3 & -2 \end{pmatrix}$$
4. Hitung $X = A^{-1} B$:
   $$\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{11} \begin{pmatrix} 1 & 3 \\ 3 & -2 \end{pmatrix} \begin{pmatrix} 8 \\ 1 \end{pmatrix} = \frac{1}{11} \begin{pmatrix} 1(8) + 3(1) \\ 3(8) + (-2)(1) \end{pmatrix} = \frac{1}{11} \begin{pmatrix} 11 \\ 22 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
   *Hasil:* Diperoleh $x = 1$ dan $y = 2$.

---

## 4. Metode 2: Penyelesaian SPL Menggunakan Aturan Cramer (*Cramer's Rule*) 🎯

**Aturan Cramer** adalah metode penyelesaian berbasis perbandingan determinan matriks. Metode ini sangat disukai karena **kita bisa mencari nilai salah satu variabel saja secara langsung** tanpa harus mencari variabel lainnya terlebih dahulu!

### A. Definisi Matriks Determinan Cramer:
1. **Determinan Utama ($D$):** Determinan dari matriks koefisien $A$.
2. **Determinan $D_x$:** Determinan dari matriks $A$ di mana **kolom ke-1 (kolom koefisien $x$) diganti dengan kolom konstanta $B$**.
3. **Determinan $D_y$:** Determinan dari matriks $A$ di mana **kolom ke-2 (kolom koefisien $y$) diganti dengan kolom konstanta $B$**.
4. **Determinan $D_z$:** Determinan dari matriks $A$ di mana **kolom ke-3 (kolom koefisien $z$) diganti dengan kolom konstanta $B$**.

---

### B. Rumus Solusi Variabel Aturan Cramer:
Jika $D \neq 0$, maka nilai variabel penyelesaian adalah:

$$x = \frac{D_x}{D}, \qquad y = \frac{D_y}{D}, \qquad z = \frac{D_z}{D}$$

#### Skema Visual Matriks Determinan (SPLTV):
$$D = \begin{vmatrix} \mathbf{a_1} & \mathbf{b_1} & \mathbf{c_1} \\ \mathbf{a_2} & \mathbf{b_2} & \mathbf{c_2} \\ \mathbf{a_3} & \mathbf{b_3} & \mathbf{c_3} \end{vmatrix}, \quad 
D_x = \begin{vmatrix} \mathbf{d_1} & b_1 & c_1 \\ \mathbf{d_2} & b_2 & c_2 \\ \mathbf{d_3} & b_3 & c_3 \end{vmatrix}, \quad 
D_y = \begin{vmatrix} a_1 & \mathbf{d_1} & c_1 \\ a_2 & \mathbf{d_2} & c_2 \\ a_3 & \mathbf{d_3} & c_3 \end{vmatrix}, \quad 
D_z = \begin{vmatrix} a_1 & b_1 & \mathbf{d_1} \\ a_2 & b_2 & \mathbf{d_2} \\ a_3 & b_3 & \mathbf{d_3} \end{vmatrix}$$

---

## 5. Analisis Klasifikasi Solusi SPL Berdasarkan Determinan 🔍

Determinan matriks koefisien $D$ dan determinan parsial $D_x, D_y, D_z$ menentukan sifat geometris dari solusi sistem persamaan linear:

```text
                                  [ Nilai Determinan Utama D ]
                                                │
                       ┌────────────────────────┴────────────────────────┐
                       ▼                                                 ▼
                 [ D ≠ 0 ]                                           [ D = 0 ]
                     │                                                   │
             Solusi Tunggal / Unik                       ┌───────────────┴───────────────┐
           (Garis/Bidang Berpotongan)                    ▼                               ▼
                                               [ Semua D_x=D_y=D_z=0 ]        [ Ada D_k ≠ 0 ]
                                                         │                               │
                                              Tak Hingga Solusi                  Tidak Ada Solusi
                                            (Berimpit / Dependen)            (Sejajar / Inkonsisten)
```

1. **Kasus 1: Solusi Tunggal / Unik (*Unique Solution / Consistent Independent*):**
   * **Syarat:** $D \neq 0$.
   * **Geometri:** Garis-garis (pada $2\text{D}$) atau bidang-bidang (pada $3\text{D}$) berpotongan tepat di **satu titik koordinat tunggal**.

2. **Kasus 2: Tak Terhingga Banyak Solusi (*Infinite Solutions / Consistent Dependent*):**
   * **Syarat:** $D = 0$ dan seluruh determinan pengganti bernilai nol ($D_x = D_y = D_z = 0$).
   * **Geometri:** Garis atau bidang-bidang persamaan saling **berimpit** membentuk satu garis/bidang bersama.

3. **Kasus 3: Tidak Ada Solusi / Mustahil (*No Solution / Inconsistent*):**
   * **Syarat:** $D = 0$, tetapi **minimal ada salah satu** determinan pengganti yang bernilai bukan nol ($D_x \neq 0$ atau $D_y \neq 0$ atau $D_z \neq 0$).
   * **Geometri:** Garis atau bidang-bidang persamaan saling **sejajar** dan tidak pernah bertemu di titik mana pun.

---

## 6. Penerapan Kontekstual di Dunia Nyata 🌐

### A. Kriptografi: Enkripsi Pesan Rahasia (Hill Cipher $2 \times 2$)
Dalam dunia keamanan data, matriks digunakan untuk menyandikan teks (*plaintext*) menjadi kode rahasia (*ciphertext*).
* Setiap huruf diubah menjadi angka ($A=1, B=2, \dots, Z=26$).
* Pasangan huruf $X = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$ dienkripsi dengan matriks kunci rahasia $K$:
  $$\text{Ciphertext } C = K \cdot X$$
* Untuk membaca kembali pesan aslinya, penerima yang sah cukup mengalikan ciphertext dengan matriks invers kunci ($K^{-1}$):
  $$\text{Plaintext } X = K^{-1} \cdot C$$

---

### B. Fisika & Teknik Elektro: Analisis Arus Rangkaian Listrik
Berdasarkan Hukum Arus Kirchhoff ($\sum I_{\text{masuk}} = \sum I_{\text{keluar}}$) dan Hukum Tegangan Kirchhoff ($\sum V + \sum IR = 0$), persamaan sirkuit multi-loop dapat dimodelkan menjadi:

$$\begin{pmatrix} R_{11} & R_{12} & R_{13} \\ R_{21} & R_{22} & R_{23} \\ R_{31} & R_{32} & R_{33} \end{pmatrix} \begin{pmatrix} I_1 \\ I_2 \\ I_3 \end{pmatrix} = \begin{pmatrix} V_1 \\ V_2 \\ V_3 \end{pmatrix}$$

Nilai kuat arus pada masing-masing loop ($I_1, I_2, I_3$) dapat langsung dihitung menggunakan Aturan Cramer: $I_1 = \frac{D_{I_1}}{D}$.

---

## 7. Contoh Soal Berjenjang & Pembahasan Komprehensif 🎯

### Level 1: Persamaan Matriks Bentuk $XA = B$
**Soal 1:**  
Tentukan matriks $X$ yang berordo $2 \times 2$ jika diketahui:
$$X \begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix} = \begin{pmatrix} 10 & 10 \\ 5 & 10 \end{pmatrix}$$

**Pembahasan:**
1. Persamaan ini bertipe $X \cdot A = B$, sehingga solusinya adalah $X = B \cdot A^{-1}$ (Invers dikalikan dari kanan!).
2. Mencari $A^{-1}$ untuk $A = \begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix}$:
   $$\det(A) = (3)(4) - (2)(1) = 12 - 2 = 10$$
   $$A^{-1} = \frac{1}{10} \begin{pmatrix} 4 & -2 \\ -1 & 3 \end{pmatrix}$$
3. Menghitung $X = B \cdot A^{-1}$:
   $$X = \begin{pmatrix} 10 & 10 \\ 5 & 10 \end{pmatrix} \left[ \frac{1}{10} \begin{pmatrix} 4 & -2 \\ -1 & 3 \end{pmatrix} \right]$$
   Keluarkan faktor skalar $\frac{1}{10}$ ke depan agar perkalian angka lebih mudah:
   $$X = \frac{1}{10} \left[ \begin{pmatrix} 10 & 10 \\ 5 & 10 \end{pmatrix} \begin{pmatrix} 4 & -2 \\ -1 & 3 \end{pmatrix} \right]$$
   $$X = \frac{1}{10} \begin{pmatrix} 10(4)+10(-1) & 10(-2)+10(3) \\ 5(4)+10(-1) & 5(-2)+10(3) \end{pmatrix}$$
   $$X = \frac{1}{10} \begin{pmatrix} 40-10 & -20+30 \\ 20-10 & -10+30 \end{pmatrix} = \frac{1}{10} \begin{pmatrix} 30 & 10 \\ 10 & 20 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$$

---

### Level 2: SPLTV Menggunakan Aturan Cramer
**Soal 2:**  
Diberikan sistem persamaan tiga variabel:
$$\begin{cases} x + y + z = 6 \\ 2y + 5z = -4 \\ 2x + 5y - z = 27 \end{cases}$$
Gunakan Aturan Cramer untuk mencari nilai $y$ saja!

**Pembahasan:**
1. Susun matriks koefisien $A$ dan matriks konstanta $B$:
   $$A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 5 \\ 2 & 5 & -1 \end{pmatrix}, \quad B = \begin{pmatrix} 6 \\ -4 \\ 27 \end{pmatrix}$$
2. Hitung determinan utama $D$ (Ekspansi Kolom 1):
   $$D = 1 \begin{vmatrix} 2 & 5 \\ 5 & -1 \end{vmatrix} - 0 + 2 \begin{vmatrix} 1 & 1 \\ 2 & 5 \end{vmatrix}$$
   $$D = 1(-2 - 25) + 2(5 - 2) = -27 + 2(3) = -27 + 6 = \mathbf{-21}$$
3. Hitung determinan $D_y$ (Ganti kolom ke-2 dengan kolom konstanta $B$):
   $$D_y = \begin{vmatrix} 1 & \mathbf{6} & 1 \\ 0 & \mathbf{-4} & 5 \\ 2 & \mathbf{27} & -1 \end{vmatrix}$$
   Ekspansi sepanjang Kolom 1:
   $$D_y = 1 \begin{vmatrix} -4 & 5 \\ 27 & -1 \end{vmatrix} - 0 + 2 \begin{vmatrix} 6 & 1 \\ -4 & 5 \end{vmatrix}$$
   $$D_y = 1(4 - 135) + 2(30 - (-4)) = -131 + 2(34) = -131 + 68 = \mathbf{-63}$$
4. Hitung nilai variabel $y$:
   $$y = \frac{D_y}{D} = \frac{-63}{-21} = \mathbf{3}$$
   *(Kita berhasil menemukan $y = 3$ dengan sangat efisien tanpa perlu menghitung $x$ dan $z$!).*

---

### Level 3: Analisis Eksistensi Solusi dengan Parameter (HOTS)
**Soal 3:**  
Diketahui sistem persamaan linear dengan parameter real $k$:
$$\begin{cases} kx + y = 1 \\ x + ky = k \end{cases}$$
Tentukan semua nilai $k$ agar sistem tersebut:
a. Memiliki tepat **satu solusi unik**.  
b. Memiliki **tak terhingga banyak solusi**.  
c. **Tidak memiliki solusi sama sekali**.

**Pembahasan Langkah demi Langkah:**
1. Matriks koefisien dan konstanta:
   $$A = \begin{pmatrix} k & 1 \\ 1 & k \end{pmatrix}, \quad B = \begin{pmatrix} 1 \\ k \end{pmatrix}$$
2. Hitung determinan-determinan Cramer:
   * $D = \begin{vmatrix} k & 1 \\ 1 & k \end{vmatrix} = k^2 - 1 = (k - 1)(k + 1)$
   * $D_x = \begin{vmatrix} 1 & 1 \\ k & k \end{vmatrix} = k - k = 0$
   * $D_y = \begin{vmatrix} k & 1 \\ 1 & k \end{vmatrix} = k^2 - 1 = (k - 1)(k + 1)$

3. Analisis Nilai Parameter $k$:
   * **a. Solusi Unik ($D \neq 0$):**  
     $$k^2 - 1 \neq 0 \implies \mathbf{k \neq 1 \text{ dan } k \neq -1}$$
     *(Solusinya adalah $x = \frac{0}{k^2-1} = 0$ dan $y = \frac{k^2-1}{k^2-1} = 1$).*
   * **b. Tak Terhingga Solusi ($D = 0$ dan $D_x = D_y = 0$):**  
     Untuk $k = 1$:  
     $D = 1^2 - 1 = 0$, $D_x = 0$, dan $D_y = 1^2 - 1 = 0$.  
     Sistem menjadi $\begin{cases} x + y = 1 \\ x + y = 1 \end{cases}$ (kedua garis berimpit sempurna).  
     Jadi, terjadi saat $\mathbf{k = 1}$.
   * **c. Tidak Ada Solusi ($D = 0$ dan ada $D_k \neq 0$):**  
     Untuk $k = -1$:  
     $D = (-1)^2 - 1 = 0$, $D_x = 0$, dan $D_y = (-1)^2 - 1 = 0$.  
     Mari kita cek persamaan aslinya saat $k = -1$:  
     $$\begin{cases} -x + y = 1 \implies y - x = 1 \\ x - y = -1 \implies y - x = 1 \end{cases}$$  
     Kedua persamaan ini sebenarnya ekuivalen (dikalikan $-1$), sehingga untuk $k = -1$ sistem juga memiliki **tak terhingga banyak solusi**.  
     Maka, **tidak ada nilai $k$ yang membuat sistem tidak memiliki solusi**.

---

## 8. Rangkuman Konsep Kunci Modul 5 📌

| Tipe Masalah | Metode / Formula Kunci | Peringatan / Kunci Sukses |
| :--- | :--- | :--- |
| **Persamaan $AX = B$** | $X = A^{-1} \cdot B$ | Invers dikalikan dari **KIRI** |
| **Persamaan $XA = B$** | $X = B \cdot A^{-1}$ | Invers dikalikan dari **KANAN** |
| **Bentuk $AXB = C$** | $X = A^{-1} C B^{-1}$ | Invers mengapit di kiri dan kanan |
| **Aturan Cramer** | $x = \frac{D_x}{D}, y = \frac{D_y}{D}, z = \frac{D_z}{D}$ | Sangat cepat untuk mencari 1 variabel spesifik |
| **Solusi Unik** | $D \neq 0$ | Titik potong tunggal |
| **Banyak Solusi** | $D = 0$ dan semua $D_k = 0$ | Persamaan berimpit |
| **Tidak Ada Solusi** | $D = 0$ dan ada $D_k \neq 0$ | Persamaan sejajar / bertentangan |

---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Minor_Kofaktor_dan_Invers_Matriks_SMA|⬅️ Modul 4: Invers Matriks]] | **Modul 5: Persamaan & SPL** | [[LKPD Matriks SMA|📝 LKPD & Latihan Soal]]
