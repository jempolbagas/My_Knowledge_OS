---
title: "Determinan Matriks dan Sifat-Sifatnya SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 11 (Fase F), Guru Matematika, dan Pembelajar Mandiri"
created: 2026-09-02
sources:
  - "[[Matriks SMA]]"
  - "[[Operasi_Aljabar_dan_Sifat_Matriks_SMA]]"
  - "[[Minor_Kofaktor_dan_Invers_Matriks_SMA]]"
  - "[[LKPD Matriks SMA]]"
tags:
  - teaching/mathematics
  - mathematics/linear-algebra
  - level/sma
  - topic/determinant
---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Operasi_Aljabar_dan_Sifat_Matriks_SMA|⬅️ Modul 2: Operasi & Sifat]] | **Modul 3: Determinan** | [[Minor_Kofaktor_dan_Invers_Matriks_SMA|Modul 4: Invers Matriks ➡️]] | [[LKPD Matriks SMA|📝 LKPD]]

---

# Determinan Matriks dan Sifat-Sifatnya — Skalar Ajaib Pengukur Skala Ruang 🔍📐

Ketika kita melihat sebuah matriks persegi berukuran $2 \times 2$ atau $3 \times 3$, ia tampak seperti kumpulan banyak angka yang terpisah. Namun, tahukah kamu bahwa ada satu nilai skalar tunggal yang dapat merangkum seluruh esensi geometri dari matriks tersebut? 

Nilai ajaib itu disebut **Determinan** (dinotasikan dengan $\det(A)$ atau $|A|$). Determinan memberi tahu kita apakah suatu transformasi matriks memperbesar atau memperkecil ruang, apakah ia membalik orientasi arah, dan yang paling krusial: **apakah matriks tersebut bisa dibalik (memiliki invers) atau tidak!**

Mari kita jelajahi konsep determinan dari sudut pandang geometris yang intuitif hingga metode perhitungannya yang presisi!

---

## 1. Arti Geometris Determinan: Faktor Penskala Luas dan Volume 🌍

Sebelum menghafal rumus aljabar, mari kita pahami apa yang sebenarnya sedang kita hitung:

```text
       Y ^
         |         (a+b, c+d)
         |         /-------/
 (b, d)  |        /       /
      *--|-------/       /  <--- Luas Jajaran Genjang = |ad - bc|
      |  |      /       /
      |  |     /       /
      |  |    /       /
      +--|---*-------+------> X
       (0,0) (a, c)
```

1. **Pada Ruang 2 Dimensi ($2\text{D}$):**
   Misalkan matriks $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Jika kolom pertama $\begin{pmatrix} a \\ c \end{pmatrix}$ dan kolom kedua $\begin{pmatrix} b \\ d \end{pmatrix}$ digambar sebagai dua vektor di bidang Cartesius, kedua vektor tersebut akan membentuk sebuah **jajaran genjang**.
   * Nilai mutlak dari determinan $|\det(A)| = |ad - bc|$ adalah **LUAS TEPAT dari jajaran genjang tersebut**!
   * Jika determinan bernilai positif ($> 0$), orientasi ruang tetap terjaga (berlawanan jarum jam). Jika bernilai negatif ($< 0$), orientasi ruang terbalik (seperti bayangan di cermin).

2. **Pada Ruang 3 Dimensi ($3\text{D}$):**
   Determinan matriks $3 \times 3$ merepresentasikan **VOLUME PARALELPIPEDUM** (balok miring 3 dimensi) yang dibentuk oleh ketiga vektor kolomnya di dalam ruang $xyz$.

3. **Apa Arti Jika Determinan Bernilai Nol ($\det(A) = 0$)?**
   * Jika $\det(A) = 0$, artinya jajaran genjang atau bangun ruang 3D tersebut **gepeng / gepeng total** menjadi satu garis lurus atau satu titik saja (kehilangan dimensi).
   * Karena ruang telah termampatkan dan informasinya hilang, kita **tidak bisa membalikkan prosesnya**. Itulah alasan geometris mengapa matriks dengan $\det(A) = 0$ disebut **Matriks Singular** dan **TIDAK MEMILIKI INVERS**!

---

## 2. Determinan Matriks Ordo $2 \times 2$

Untuk matriks persegi berordo $2 \times 2$, determinan dihitung dengan mengalikan elemen diagonal utama dikurangi perkalian elemen diagonal samping:

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies \det(A) = |A| = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = a \cdot d - b \cdot c$$

> [!NOTE]
> Perhatikan penggunaan tanda kurung lurus $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ untuk menyatakan operasi determinan, berbeda dengan tanda kurung lengkung $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ yang menyatakan matriks itu sendiri.

#### Contoh:
Hitung determinan matriks $P = \begin{pmatrix} 4 & -2 \\ 3 & 5 \end{pmatrix}$!
$$\det(P) = (4)(5) - (-2)(3) = 20 - (-6) = 20 + 6 = \mathbf{26}$$

---

## 3. Determinan Matriks Ordo $3 \times 3$ (Aturan Sarrus) ⚔️

Aturan Sarrus adalah metode cepat dan visual untuk menghitung determinan khusus matriks $3 \times 3$.

### Langkah Kerja Aturan Sarrus:
1. Tuliskan kembali matriks $3 \times 3$.
2. Salin **dua kolom pertama** dan tempatkan di sebelah kanan garis batas determinan.
3. Jumlahkan hasil kali diagonal yang mengarah dari kiri-atas ke kanan-bawah (tanda $\mathbf{+}$).
4. Kurangkan hasil kali diagonal yang mengarah dari kiri-bawah ke kanan-atas (tanda $\mathbf{-}$).

```text
       (+)    (+)    (+)
        \      \      \
       [ a      b      c ]  a    b
       [ d      e      f ]  d    e
       [ g      h      i ]  g    h
        /      /      /
       (-)    (-)    (-)
```

$$\det(A) = \underbrace{(aei + bfg + cdh)}_{\text{Diagonal Utama (+)}} - \underbrace{(ceg + afh + bdi)}_{\text{Diagonal Samping (-)}}$$

#### Contoh Perhitungan Sarrus:
Diberikan matriks $A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & 6 \end{pmatrix}$. Tentukan $\det(A)$!

Salin dua kolom pertama ke kanan:
$$\begin{vmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & 6 \end{vmatrix} \begin{matrix} 1 & 2 \\ 0 & 4 \\ 1 & 0 \end{matrix}$$

Hitung jalur diagonal:
* **Jalur Positif ($+$):**
  $$(1 \cdot 4 \cdot 6) + (2 \cdot 5 \cdot 1) + (3 \cdot 0 \cdot 0) = 24 + 10 + 0 = 34$$
* **Jalur Negatif ($-$):**
  $$(3 \cdot 4 \cdot 1) + (1 \cdot 5 \cdot 0) + (2 \cdot 0 \cdot 6) = 12 + 0 + 0 = 12$$

Maka nilai determinan:
$$\det(A) = 34 - 12 = \mathbf{22}$$

> [!WARNING]
> **Batasan Aturan Sarrus:**  
> Aturan Sarrus **HANYA BERLAKU untuk matriks ordo $3 \times 3$**. Jangan pernah mencoba menerapkan metode salin kolom Sarrus pada matriks $4 \times 4$ ke atas karena pola diagonalnya tidak lagi mencakup seluruh permutasi genap dan ganjil!

---

## 4. Determinan Ordo $n \times n$ (Metode Ekspansi Laplace / Kofaktor)

Metode Ekspansi Laplace adalah metode universal yang berlaku untuk matriks berukuran berapa pun ($2 \times 2, 3 \times 3, 4 \times 4, \dots, n \times n$).

### A. Konsep Dasar
Determinan dihitung dengan mengalikan setiap elemen pada **satu baris** (atau **satu kolom**) terpilih dengan kofaktornya masing-masing, lalu menjumlahkannya:

1. **Ekspansi Sepanjang Baris ke-$i$:**
   $$\det(A) = \sum_{j=1}^n a_{ij} C_{ij} = a_{i1} C_{i1} + a_{i2} C_{i2} + \dots + a_{in} C_{in}$$

2. **Ekspansi Sepanjang Kolom ke-$j$:**
   $$\det(A) = \sum_{i=1}^n a_{ij} C_{ij} = a_{1j} C_{1j} + a_{2j} C_{2j} + \dots + a_{nj} C_{nj}$$

Di mana kofaktor didefinisikan sebagai $C_{ij} = (-1)^{i+j} M_{ij}$, dan $M_{ij}$ adalah determinan submatriks setelah baris $i$ dan kolom $j$ dihapus.

---

### B. Trik Efisiensi Menghitung dengan Ekspansi Laplace
> [!TIP]
> **Pilihlah Baris atau Kolom yang Memiliki Angka 0 Terbanyak!**  
> Karena jika elemen $a_{ij} = 0$, maka suku $a_{ij} C_{ij} = 0 \cdot C_{ij} = 0$. Kamu tidak perlu repot-repot menghitung kofaktor pada posisi elemen nol tersebut!

#### Contoh:
Hitung determinan matriks $B = \begin{pmatrix} 3 & 0 & 0 \\ 2 & 4 & 5 \\ -1 & 1 & 6 \end{pmatrix}$!

Perhatikan **Baris ke-1** memiliki dua angka nol ($a_{12} = 0$ dan $a_{13} = 0$).  
Lakukan ekspansi sepanjang **Baris 1**:
$$\det(B) = a_{11} C_{11} + a_{12} C_{12} + a_{13} C_{13}$$
$$\det(B) = 3 \cdot (-1)^{1+1} \begin{vmatrix} 4 & 5 \\ 1 & 6 \end{vmatrix} + 0 + 0$$
$$\det(B) = 3 \cdot (+1) \cdot (4 \cdot 6 - 5 \cdot 1) = 3 \cdot (24 - 5) = 3 \cdot 19 = \mathbf{57}$$
*(Sangat cepat dan praktis!).*

---

## 5. Teorema dan Sifat-Sifat Emas Determinan 🌟

Memahami sifat-sifat determinan akan membuatmu bisa menyelesaikan soal-soal olimpiade dan ujian masuk universitas tanpa perlu melakukan perhitungan manual yang panjang!

Misalkan $A$ dan $B$ adalah matriks persegi berordo $n \times n$:

### 1. Determinan Transpose Matriks
$$\det(A^T) = \det(A)$$
*(Nilai determinan matriks tidak berubah jika baris dan kolomnya ditukar).*

### 2. Determinan Perkalian Matriks (Multiplicative Property)
$$\det(A \cdot B) = \det(A) \cdot \det(B)$$

### 3. Determinan Invers Matriks
$$\det(A^{-1}) = \frac{1}{\det(A)} = (\det(A))^{-1}$$
*(Bukti: $A \cdot A^{-1} = I \implies \det(A \cdot A^{-1}) = \det(I) \implies \det(A) \cdot \det(A^{-1}) = 1 \implies \det(A^{-1}) = \frac{1}{\det(A)}$).*

### 4. Determinan Perkalian Skalar dengan Matriks Berordo $n$
$$\det(k \cdot A_{n \times n}) = k^n \cdot \det(A)$$

> [!WARNING]
> **Jebakan Paling Sering Terjadi!**  
> Mengalikan matriks $A$ dengan skalar $k$ berarti mengalikan **seluruh $n$ buah baris** dengan $k$. Karena setiap baris mengeluarkan faktor $k$, maka total faktor yang keluar dari tanda determinan adalah $k^n$!  
> *Contoh:* Jika $\det(A_{3 \times 3}) = 5$, maka $\det(2A) = 2^3 \cdot \det(A) = 8 \cdot 5 = \mathbf{40}$ (Bukan $2 \times 5 = 10$!).

### 5. Determinan Pemangkatan Matriks
$$\det(A^m) = (\det(A))^m \quad \text{untuk sebarang bilangan bulat positif } m$$

### 6. Determinan Matriks Segitiga & Matriks Diagonal
Determinan dari matriks segitiga atas, matriks segitiga bawah, atau matriks diagonal adalah **hasil kali seluruh elemen pada diagonal utamanya**:
$$\det(A) = a_{11} \cdot a_{22} \cdot \dots \cdot a_{nn} = \prod_{i=1}^n a_{ii}$$

*Contoh:* $\det \begin{pmatrix} 2 & 7 & -5 \\ 0 & 3 & 8 \\ 0 & 0 & 4 \end{pmatrix} = 2 \cdot 3 \cdot 4 = \mathbf{24}$.

### 7. Kondisi Determinan Bernilai Nol ($\det(A) = 0$)
Nilai determinan suatu matriks persegi otomatis bernilai $0$ jika:
* Terdapat **satu baris atau satu kolom yang semua elemennya bernilai nol**.
* Terdapat **dua baris atau dua kolom yang identik (sama persis)**.
* Terdapat **dua baris atau dua kolom yang merupakan kelipatan linier dari baris/kolom lain** ($R_i = k \cdot R_j$).

### 8. Pengaruh Operasi Baris Elementer (OBE) terhadap Determinan
* **Menukar Dua Baris ($R_i \leftrightarrow R_j$):** Determinan bernilai lawannya ($\times -1$).
* **Mengalikan Satu Baris dengan Skalar $k$ ($k R_i \to R_i$):** Determinan bernilai $k$ kali lipat.
* **Menambahkan Kelipatan Baris ke Baris Lain ($R_i + k R_j \to R_i$):** **TIDAK MENGUBAH** nilai determinan sama sekali!

---

## 6. Contoh Soal Berjenjang & Pembahasan Komprehensif 🎯

### Level 1: Aplikasi Sifat Perkalian & Invers
**Soal 1:**  
Diketahui matriks persegi $A$ dan $B$ berordo $3 \times 3$ dengan $\det(A) = 4$ dan $\det(B) = -2$.  
Tentukan nilai dari:
a. $\det(A \cdot B)$  
b. $\det(A^T \cdot B^{-1})$  
c. $\det(3A)$  
d. $\det(A^3 \cdot B^2)$

**Pembahasan:**
a. $\det(AB) = \det(A) \cdot \det(B) = 4 \cdot (-2) = \mathbf{-8}$  
b. $\det(A^T \cdot B^{-1}) = \det(A^T) \cdot \det(B^{-1}) = \det(A) \cdot \frac{1}{\det(B)} = 4 \cdot \left(\frac{1}{-2}\right) = \mathbf{-2}$  
c. Matriks $A$ berordo $3 \times 3$, sehingga $n = 3$:  
   $$\det(3A) = 3^3 \cdot \det(A) = 27 \cdot 4 = \mathbf{108}$$  
d. $\det(A^3 \cdot B^2) = (\det(A))^3 \cdot (\det(B))^2 = (4)^3 \cdot (-2)^2 = 64 \cdot 4 = \mathbf{256}$

---

### Level 2: Menentukan Nilai Parameter pada Matriks Singular
**Soal 2:**  
Tentukan semua nilai $x$ yang membuat matriks $M = \begin{pmatrix} x-2 & -3 \\ 2 & x+3 \end{pmatrix}$ menjadi **matriks singular**!

**Pembahasan:**
1. Matriks $M$ singular jika dan hanya jika $\det(M) = 0$.
2. Hitung determinan $M$:
   $$\det(M) = (x - 2)(x + 3) - (-3)(2) = 0$$
3. Uraikan bentuk aljabar:
   $$(x^2 + x - 6) - (-6) = 0$$
   $$x^2 + x - 6 + 6 = 0$$
   $$x^2 + x = 0$$
4. Faktorkan persamaan kuadrat:
   $$x(x + 1) = 0 \implies x_1 = 0 \quad \text{atau} \quad x_2 = -1$$
   *Jawaban:* Nilai $x$ yang memenuhi adalah **$x = 0$ atau $x = -1$**.

---

### Level 3: Soal Analisis Penalaran Determinan $3 \times 3$ (HOTS)
**Soal 3:**  
Diberikan matriks $K = \begin{pmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{pmatrix}$ (dikenal sebagai *Matriks Vandermonde*).  
Buktikan bahwa $\det(K) = (b - a)(c - a)(c - b)$!

**Pembuktian Langkah demi Langkah Menggunakan Operasi Baris:**
1. Gunakan sifat bahwa menambah kelipatan baris tidak mengubah determinan:
   * Baris 2 dikurangi Baris 1 ($R_2 - R_1 \to R_2$):
   * Baris 3 dikurangi Baris 1 ($R_3 - R_1 \to R_3$):
   $$\det(K) = \begin{vmatrix} 1 & a & a^2 \\ 0 & b-a & b^2-a^2 \\ 0 & c-a & c^2-a^2 \end{vmatrix}$$
2. Ingat rumus selisih kuadrat $b^2 - a^2 = (b-a)(b+a)$ dan $c^2 - a^2 = (c-a)(c+a)$:
   $$\det(K) = \begin{vmatrix} 1 & a & a^2 \\ 0 & (b-a) & (b-a)(b+a) \\ 0 & (c-a) & (c-a)(c+a) \end{vmatrix}$$
3. Lakukan ekspansi Laplace sepanjang **Kolom ke-1**:
   $$\det(K) = 1 \cdot \begin{vmatrix} (b-a) & (b-a)(b+a) \\ (c-a) & (c-a)(c+a) \end{vmatrix}$$
4. Keluarkan faktor $(b-a)$ dari baris 1 dan $(c-a)$ dari baris 2:
   $$\det(K) = (b-a)(c-a) \begin{vmatrix} 1 & b+a \\ 1 & c+a \end{vmatrix}$$
5. Hitung determinan $2 \times 2$ yang tersisa:
   $$\begin{vmatrix} 1 & b+a \\ 1 & c+a \end{vmatrix} = 1(c+a) - 1(b+a) = c + a - b - a = (c - b)$$
6. Gabungkan seluruh faktor:
   $$\det(K) = (b - a)(c - a)(c - b) \quad \mathbf{\text{(Terbukti!) Walaupun terlihat rumit, faktorisasi ini sangat elegan!}}$$

---

## 7. Rangkuman Konsep Kunci Modul 3 📌

| Teorema / Karakteristik | Formula Matematis | Poin Pengingat |
| :--- | :--- | :--- |
| **Determinan $2 \times 2$** | $ad - bc$ | Luas jajaran genjang di bidang $2\text{D}$ |
| **Determinan $3 \times 3$** | Aturan Sarrus / Laplace | Sarrus **hanya** untuk ordo 3 |
| **Matriks Singular** | $\det(A) = 0$ | Tidak memiliki invers |
| **Perkalian Matriks** | $\det(AB) = \det(A)\det(B)$ | Berlaku distributif terhadap perkalian |
| **Perkalian Skalar** | $\det(kA_{n \times n}) = k^n \det(A)$ | Wajib dipangkatkan dengan ordo $n$ |
| **Invers Matriks** | $\det(A^{-1}) = \frac{1}{\det(A)}$ | Kebalikan nilai determinan |
| **Matriks Segitiga** | $\det(A) = \prod a_{ii}$ | Cukup kalikan elemen diagonal utama |

---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Operasi_Aljabar_dan_Sifat_Matriks_SMA|⬅️ Modul 2: Operasi & Sifat]] | **Modul 3: Determinan** | [[Minor_Kofaktor_dan_Invers_Matriks_SMA|Modul 4: Invers Matriks ➡️]] | [[LKPD Matriks SMA|📝 LKPD]]
