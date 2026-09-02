---
title: "Minor, Kofaktor, dan Invers Matriks SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 11 (Fase F), Guru Matematika, dan Pembelajar Mandiri"
created: 2026-09-02
sources:
  - "[[Matriks SMA]]"
  - "[[Determinan_Matriks_dan_Sifatnya_SMA]]"
  - "[[Persamaan_Matriks_dan_Sistem_Persamaan_Linear_SMA]]"
  - "[[LKPD Matriks SMA]]"
tags:
  - teaching/mathematics
  - mathematics/linear-algebra
  - level/sma
  - topic/matrix-inverse
---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Determinan_Matriks_dan_Sifatnya_SMA|⬅️ Modul 3: Determinan]] | **Modul 4: Invers Matriks** | [[Persamaan_Matriks_dan_Sistem_Persamaan_Linear_SMA|Modul 5: Persamaan & SPL ➡️]] | [[LKPD Matriks SMA|📝 LKPD]]

---

# Minor, Kofaktor, dan Invers Matriks — Membalik Transformasi Aljabar Linear 🔄🎯

Dalam aritmatika dasar, jika kita memiliki persamaan $3x = 12$, kita bisa dengan mudah membagi kedua ruas dengan $3$ (atau mengalikannya dengan $\frac{1}{3}$) untuk mendapatkan $x = 4$. 

Namun di dalam dunia matriks, **OPERASI PEMBAGIAN TIDAK PERNAH DIDEFINISIKAN**! Kita tidak bisa menuliskan bentuk $\frac{B}{A}$. Sebagai gantinya, konsep pembagian digantikan secara elegan oleh operasi **Perkalian dengan Invers Matriks ($A^{-1}$)**. 

Bagaimana cara mencari invers matriks? Dari mana datangnya konsep Minor, Kofaktor, dan Adjoin? Mari kita bedah secara mendalam langkah demi langkah!

---

## 1. Konsep Invers Matriks dan Syarat Eksistensinya

### A. Definisi Formal
Invers dari matriks persegi $A$ adalah suatu matriks unik yang dinotasikan dengan **$A^{-1}$** sedemikian rupa sehingga jika dikalikan dengan matriks asalnya (baik dari kiri maupun dari kanan) akan menghasilkan **Matriks Identitas ($I$)**:

$$A \cdot A^{-1} = A^{-1} \cdot A = I$$

---

### B. Syarat Mutlak Eksistensi Invers
Tidak semua matriks memiliki invers. Suatu matriks $A$ memiliki invers jika dan hanya jika memenuhi dua syarat:
1. **Matriks Persegi:** Jumlah baris harus sama dengan jumlah kolom ($n \times n$).
2. **Matriks Nonsingular ($\det(A) \neq 0$):** Nilai determinan matriks tidak boleh sama dengan nol.

> [!CAUTION]
> * Jika $\det(A) \neq 0 \implies$ Matriks **Nonsingular** (Memiliki Invers $A^{-1}$).
> * Jika $\det(A) = 0 \implies$ Matriks **Singular** (TIDAK Memiliki Invers).

---

## 2. Bedah Tuntas: Konstruksi Minor, Kofaktor, dan Adjoin 🔍

Untuk menemukan invers matriks secara umum (khususnya ordo $3 \times 3$ ke atas), kita harus memahami rantai transformasi: **Matriks Asli $\to$ Minor $\to$ Kofaktor $\to$ Adjoin $\to$ Invers**.

### A. Apa itu Minor ($M_{ij}$)?
**Minor $M_{ij}$** adalah nilai determinan submatriks yang diperoleh dengan cara **menghapus (mencoret) baris ke-$i$ dan kolom ke-$j$** dari matriks utama.

#### Visualisasi Perhitungan Minor Matriks $3 \times 3$:
Misalkan $A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$.

* **Mencari $M_{11}$ (Coret Baris 1 & Kolom 1):**
  $$\begin{pmatrix} \xcancel{a_{11}} & \xcancel{a_{12}} & \xcancel{a_{13}} \\ \xcancel{a_{21}} & a_{22} & a_{23} \\ \xcancel{a_{31}} & a_{32} & a_{33} \end{pmatrix} \implies M_{11} = \begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} = a_{22}a_{33} - a_{23}a_{32}$$

* **Mencari $M_{12}$ (Coret Baris 1 & Kolom 2):**
  $$\begin{pmatrix} \xcancel{a_{11}} & \xcancel{a_{12}} & \xcancel{a_{13}} \\ a_{21} & \xcancel{a_{22}} & a_{23} \\ a_{31} & \xcancel{a_{32}} & a_{33} \end{pmatrix} \implies M_{12} = \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} = a_{21}a_{33} - a_{23}a_{31}$$

* **Mencari $M_{23}$ (Coret Baris 2 & Kolom 3):**
  $$\begin{pmatrix} a_{11} & a_{12} & \xcancel{a_{13}} \\ \xcancel{a_{21}} & \xcancel{a_{22}} & \xcancel{a_{23}} \\ a_{31} & a_{32} & \xcancel{a_{33}} \end{pmatrix} \implies M_{23} = \begin{vmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} \end{vmatrix} = a_{11}a_{32} - a_{12}a_{31}$$

---

### B. Apa itu Kofaktor ($C_{ij}$)?
**Kofaktor ($C_{ij}$)** adalah nilai Minor $M_{ij}$ yang telah dikalikan dengan **faktor tanda posisi $(-1)^{i+j}$**:

$$C_{ij} = (-1)^{i+j} \cdot M_{ij}$$

#### Asal Usul Tanda Posisi:
* Jika $(i + j)$ bernilai **GENAP** $\implies (-1)^{\text{genap}} = \mathbf{+1} \implies C_{ij} = +M_{ij}$
* Jika $(i + j)$ bernilai **GANJIL** $\implies (-1)^{\text{ganjil}} = \mathbf{-1} \implies C_{ij} = -M_{ij}$

#### Pola Tanda Papan Catur (*Checkerboard Pattern*):
Untuk mempermudah tanpa perlu menghitung $(-1)^{i+j}$ berulang-ulang, hafalkan pola selang-seling tanda kofaktor ini:

$$\text{Ordo } 2 \times 2: \begin{pmatrix} + & - \\ - & + \end{pmatrix}, \qquad \text{Ordo } 3 \times 3: \begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}$$

---

### C. Matriks Kofaktor vs Matriks Adjoin ($\operatorname{Adj}(A)$)
Perbedaan ini adalah sumber kesalahan paling umum siswa di lembar ujian. Perhatikan definisinya dengan teliti:

1. **Matriks Kofaktor ($\operatorname{Cof}(A)$):**
   Matriks yang berisikan seluruh nilai kofaktor $C_{ij}$:
   $$\operatorname{Cof}(A) = \begin{pmatrix} C_{11} & C_{12} & C_{13} \\ C_{21} & C_{22} & C_{23} \\ C_{31} & C_{32} & C_{33} \end{pmatrix}$$

2. **Matriks Adjoin ($\operatorname{Adj}(A)$):**
   > [!IMPORTANT]
   > **Adjoin adalah TRANSPOSE dari Matriks Kofaktor!**
   > $$\operatorname{Adj}(A) = (\operatorname{Cof}(A))^T = \begin{pmatrix} C_{11} & C_{21} & C_{31} \\ C_{12} & C_{22} & C_{32} \\ C_{13} & C_{23} & C_{33} \end{pmatrix}$$
   > Jangan lupa menukar posisi baris menjadi kolom setelah menghitung kofaktor!

---

## 3. Invers Matriks Ordo $2 \times 2$

### A. Rumus Cepat dan Deduksinya
Diberikan matriks $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ dengan $\det(A) = ad - bc \neq 0$:

1. Hitung minor dan kofaktor:
   * $M_{11} = d \implies C_{11} = +d$
   * $M_{12} = c \implies C_{12} = -c$
   * $M_{21} = b \implies C_{21} = -b$
   * $M_{22} = a \implies C_{22} = +a$
2. Matriks kofaktor: $\operatorname{Cof}(A) = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix}$
3. Matriks adjoin (transpose kofaktor): $\operatorname{Adj}(A) = (\operatorname{Cof}(A))^T = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$

Sehingga rumus invers ordo $2 \times 2$ menjadi:

$$A^{-1} = \frac{1}{\det(A)} \operatorname{Adj}(A) = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

> [!TIP]
> **Jembatan Keledai Invers $2 \times 2$:**
> 1. **Tukar posisi** elemen pada diagonal utama ($a$ dan $d$ bertukar tempat).
> 2. **Ubah tanda** elemen pada diagonal samping ($b$ menjadi $-b$, dan $c$ menjadi $-c$).
> 3. Kalikan seluruh matriks dengan $\frac{1}{\det(A)}$.

#### Contoh:
Tentukan invers dari matriks $P = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$!
1. $\det(P) = (3)(2) - (5)(1) = 6 - 5 = 1$.
2. $P^{-1} = \frac{1}{1} \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix}$.

---

## 4. Invers Matriks Ordo $3 \times 3$ (Metode Adjoin Lengkap) 🎯

Formula umum invers matriks adalah:
$$A^{-1} = \frac{1}{\det(A)} \cdot \operatorname{Adj}(A)$$

Berikut adalah **Panduan Sistematis 4 Langkah** untuk menyelesaikan invers $3 \times 3$:

```text
[ Matriks A ]
      │
      ├─► Langkah 1: Hitung Det(A) (Pastikan Det(A) ≠ 0)
      │
      ├─► Langkah 2: Hitung 9 Kofaktor C_ij = (-1)^(i+j) * M_ij
      │
      ├─► Langkah 3: Susun Matriks Kofaktor & Transpose menjadi Adj(A)
      │
      └─► Langkah 4: Kalikan Adj(A) dengan 1 / Det(A) ──► [ Matriks A^-1 ]
```

---

### Contoh Komprehensif Langkah demi Langkah Invers $3 \times 3$

Diketahui matriks $A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 3 & 1 \\ 2 & 0 & 1 \end{pmatrix}$. Tentukan $A^{-1}$ dan buktikan bahwa $A \cdot A^{-1} = I$!

#### Langkah 1: Hitung Determinan $\det(A)$
Lakukan ekspansi baris ke-1:
$$\det(A) = 1 \begin{vmatrix} 3 & 1 \\ 0 & 1 \end{vmatrix} - 2 \begin{vmatrix} 0 & 1 \\ 2 & 1 \end{vmatrix} + 1 \begin{vmatrix} 0 & 3 \\ 2 & 0 \end{vmatrix}$$
$$\det(A) = 1(3 - 0) - 2(0 - 2) + 1(0 - 6) = 3 - 2(-2) + (-6) = 3 + 4 - 6 = \mathbf{1}$$
*(Karena $\det(A) = 1 \neq 0$, matriks memiliki invers).*

---

#### Langkah 2: Hitung 9 Kofaktor $C_{ij}$
* $C_{11} = + \begin{vmatrix} 3 & 1 \\ 0 & 1 \end{vmatrix} = +(3\cdot 1 - 1\cdot 0) = \mathbf{3}$
* $C_{12} = - \begin{vmatrix} 0 & 1 \\ 2 & 1 \end{vmatrix} = -(0\cdot 1 - 1\cdot 2) = -(-2) = \mathbf{2}$
* $C_{13} = + \begin{vmatrix} 0 & 3 \\ 2 & 0 \end{vmatrix} = +(0\cdot 0 - 3\cdot 2) = \mathbf{-6}$
* $C_{21} = - \begin{vmatrix} 2 & 1 \\ 0 & 1 \end{vmatrix} = -(2\cdot 1 - 1\cdot 0) = \mathbf{-2}$
* $C_{22} = + \begin{vmatrix} 1 & 1 \\ 2 & 1 \end{vmatrix} = +(1\cdot 1 - 1\cdot 2) = 1 - 2 = \mathbf{-1}$
* $C_{23} = - \begin{vmatrix} 1 & 2 \\ 2 & 0 \end{vmatrix} = -(1\cdot 0 - 2\cdot 2) = -(-4) = \mathbf{4}$
* $C_{31} = + \begin{vmatrix} 2 & 1 \\ 3 & 1 \end{vmatrix} = +(2\cdot 1 - 1\cdot 3) = 2 - 3 = \mathbf{-1}$
* $C_{32} = - \begin{vmatrix} 1 & 1 \\ 0 & 1 \end{vmatrix} = -(1\cdot 1 - 1\cdot 0) = \mathbf{-1}$
* $C_{33} = + \begin{vmatrix} 1 & 2 \\ 0 & 3 \end{vmatrix} = +(1\cdot 3 - 2\cdot 0) = \mathbf{3}$

---

#### Langkah 3: Susun Matriks Kofaktor & Transpose menjadi Adjoin
$$\operatorname{Cof}(A) = \begin{pmatrix} 3 & 2 & -6 \\ -2 & -1 & 4 \\ -1 & -1 & 3 \end{pmatrix}$$

Transpose matriks kofaktor untuk mendapatkan $\operatorname{Adj}(A)$:
$$\operatorname{Adj}(A) = (\operatorname{Cof}(A))^T = \begin{pmatrix} 3 & -2 & -1 \\ 2 & -1 & -1 \\ -6 & 4 & 3 \end{pmatrix}$$

---

#### Langkah 4: Kalikan dengan $\frac{1}{\det(A)}$
$$A^{-1} = \frac{1}{1} \begin{pmatrix} 3 & -2 & -1 \\ 2 & -1 & -1 \\ -6 & 4 & 3 \end{pmatrix} = \begin{pmatrix} 3 & -2 & -1 \\ 2 & -1 & -1 \\ -6 & 4 & 3 \end{pmatrix}$$

---

#### Verifikasi Kebenaran Hasil ($A \cdot A^{-1} = I$):
$$A \cdot A^{-1} = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 3 & 1 \\ 2 & 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & -2 & -1 \\ 2 & -1 & -1 \\ -6 & 4 & 3 \end{pmatrix}$$
$$= \begin{pmatrix} 1(3)+2(2)+1(-6) & 1(-2)+2(-1)+1(4) & 1(-1)+2(-1)+1(3) \\ 0(3)+3(2)+1(-6) & 0(-2)+3(-1)+1(4) & 0(-1)+3(-1)+1(3) \\ 2(3)+0(2)+1(-6) & 2(-2)+0(-1)+1(4) & 2(-1)+0(-1)+1(3) \end{pmatrix}$$
$$= \begin{pmatrix} 3+4-6 & -2-2+4 & -1-2+3 \\ 0+6-6 & 0-3+4 & 0-3+3 \\ 6+0-6 & -4+0+4 & -2+0+3 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I \quad \mathbf{\text{(Tepat 100\%!) ✨}}$$

---

## 5. Pengenalan Metode Eliminasi Gauss-Jordan (OBE) 💡

Selain metode Adjoin, ada metode yang sangat disukai dalam pemrograman komputer untuk matriks berukuran besar ($4 \times 4, 100 \times 100$), yaitu **Metode Operasi Baris Elementer (OBE) Gauss-Jordan**.

### Prinsip Kerja:
1. Bentuk matriks teraugmentasi $[A \mid I]$, di mana matriks $A$ digandengkan dengan matriks identitas $I$ berordo sama di sebelah kanannya:
   $$[A \mid I] = \left[ \begin{array}{ccc|ccc} a_{11} & a_{12} & a_{13} & 1 & 0 & 0 \\ a_{21} & a_{22} & a_{23} & 0 & 1 & 0 \\ a_{31} & a_{32} & a_{33} & 0 & 0 & 1 \end{array} \right]$$
2. Lakukan operasi baris elementer (menukar baris, mengalikan baris dengan skalar, menjumlahkan kelipatan baris) sampai sisi kiri berubah menjadi matriks identitas $I$:
   $$[A \mid I] \xrightarrow{\text{Operasi Baris Elementer}} [I \mid A^{-1}]$$
3. Begitu sisi kiri berhasil menjadi $I$, matriks yang berada di sisi kanan **otomatis menjadi $A^{-1}$**!

---

## 6. Teorema dan Sifat-Sifat Emas Invers Matriks 🌟

Misalkan $A$ dan $B$ adalah matriks-matriks nonsingular berordo sama, serta $k$ adalah skalar real bukan nol:

1. **Involusi Invers:**
   $$(A^{-1})^{-1} = A$$
2. **Sifat Pembalikan Perkalian Invers (*Shoe-Socks Property*):**
   $$(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$$
   > [!NOTE]
   > Analogi memakai sepatu dan kaus kaki: Saat memakai pakaian, kita mengenakan **kaus kaki ($A$) lalu sepatu ($B$)**. Saat melepas pakaian kembali (invers), kita harus melepas **sepatu dulu ($B^{-1}$) baru kemudian melepas kaus kaki ($A^{-1}$)**! Itulah sebabnya $(AB)^{-1} = B^{-1} A^{-1}$.
3. **Invers Transpose:**
   $$(A^T)^{-1} = (A^{-1})^T$$
4. **Invers Perkalian Skalar:**
   $$(k \cdot A)^{-1} = \frac{1}{k} \cdot A^{-1}$$
5. **Invers Pemangkatan:**
   $$(A^m)^{-1} = (A^{-1})^m = A^{-m}$$

---

## 7. Contoh Soal Berjenjang & Pembahasan Komprehensif 🎯

### Level 1: Aplikasi Sifat Invers Perkalian
**Soal 1:**  
Diketahui matriks $A = \begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix}$. Tentukan matriks $(AB)^{-1}$!

**Pembahasan:**
*Metode 1 (Menggunakan Sifat $(AB)^{-1} = B^{-1} A^{-1}$):*
1. Invers $A$:
   $$\det(A) = 2(2) - 3(1) = 4 - 3 = 1 \implies A^{-1} = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$$
2. Invers $B$:
   $$\det(B) = 1(2) - (-1)(0) = 2 \implies B^{-1} = \frac{1}{2} \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & \frac{1}{2} \\ 0 & \frac{1}{2} \end{pmatrix}$$
3. Hitung $(AB)^{-1} = B^{-1} \cdot A^{-1}$:
   $$(AB)^{-1} = \begin{pmatrix} 1 & \frac{1}{2} \\ 0 & \frac{1}{2} \end{pmatrix} \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1(2)+\frac{1}{2}(-1) & 1(-3)+\frac{1}{2}(2) \\ 0(2)+\frac{1}{2}(-1) & 0(-3)+\frac{1}{2}(2) \end{pmatrix} = \begin{pmatrix} \frac{3}{2} & -2 \\ -\frac{1}{2} & 1 \end{pmatrix}$$

---

### Level 2: Mencari Invers Matriks Simetris Berordo $3 \times 3$
**Soal 2:**  
Tentukan invers dari matriks diagonal $D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 4 \end{pmatrix}$!

**Pembahasan:**
Untuk setiap matriks diagonal $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$ di mana semua $d_i \neq 0$, inversnya adalah matriks diagonal baru yang elemennya merupakan kebalikan dari masing-masing diagonalnya:
$$D^{-1} = \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & \frac{1}{-1} & 0 \\ 0 & 0 & \frac{1}{4} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & \frac{1}{4} \end{pmatrix}$$
*(Sifat ini sangat bermanfaat dan mempercepat kalkulasi!).*

---

### Level 3: Tantangan Analisis Eksistensi Invers Matriks Aljabar (HOTS)
**Soal 3:**  
Diberikan matriks $A$ yang memenuhi persamaan polinomial matriks:
$$A^3 - 4A^2 + 3A - 5I = O$$
Buktikan bahwa matriks $A$ **pasti memiliki invers ($A^{-1}$)**, lalu nyatakan $A^{-1}$ sebagai kombinasi linier dari $A^2, A,$ dan $I$!

**Pembuktian Langkah demi Langkah:**
1. Susun ulang persamaan sehingga suku yang memuat identitas berada di ruas kanan:
   $$A^3 - 4A^2 + 3A = 5I$$
2. Faktorkan matriks $A$ keluar dari sebelah kiri:
   $$A \cdot (A^2 - 4A + 3I) = 5I$$
3. Bagi kedua ruas dengan skalar $5$:
   $$A \cdot \left[ \frac{1}{5}(A^2 - 4A + 3I) \right] = I$$
4. Berdasarkan definisi invers matriks ($A \cdot B = I \implies B = A^{-1}$), maka ekspresi di dalam tanda kurung siku **pasti merupakan invers dari matriks $A$**!
   $$A^{-1} = \frac{1}{5} A^2 - \frac{4}{5} A + \frac{3}{5} I$$
5. Karena invers $A^{-1}$ ada dan terdefinisi secara nyata, maka terbukti bahwa matriks $A$ adalah **matriks nonsingular**.

---

## 8. Rangkuman Konsep Kunci Modul 4 📌

| Konsep | Formula Kunci | Catatan Krusial |
| :--- | :--- | :--- |
| **Definisi Invers** | $A \cdot A^{-1} = A^{-1} \cdot A = I$ | Pembagian matriks tidak ada |
| **Minor $M_{ij}$** | $\det(\text{Submatriks})$ | Hapus baris $i$ dan kolom $j$ |
| **Kofaktor $C_{ij}$** | $(-1)^{i+j} M_{ij}$ | Perhatikan tanda papan catur $\pm$ |
| **Adjoin $\operatorname{Adj}(A)$** | $(\operatorname{Cof}(A))^T$ | **Wajib transpose** matriks kofaktor |
| **Invers $2 \times 2$** | $\frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ | Tukar diagonal utama, ganti tanda samping |
| **Invers $3 \times 3$** | $\frac{1}{\det(A)} \operatorname{Adj}(A)$ | Algoritma 4 langkah |
| **Invers Perkalian** | $(AB)^{-1} = B^{-1} A^{-1}$ | Posisi wajib dibalik |

---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Determinan_Matriks_dan_Sifatnya_SMA|⬅️ Modul 3: Determinan]] | **Modul 4: Invers Matriks** | [[Persamaan_Matriks_dan_Sistem_Persamaan_Linear_SMA|Modul 5: Persamaan & SPL ➡️]] | [[LKPD Matriks SMA|📝 LKPD]]
