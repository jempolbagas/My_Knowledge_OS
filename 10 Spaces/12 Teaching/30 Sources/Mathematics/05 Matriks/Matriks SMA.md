---
title: "Materi Ajar Santai: Menaklukkan Matriks Tanpa Pusing"
level: sma
type: teaching-material
subject: Mathematics
target_audience: "SMA Kelas 11"
created: 2026-07-28
updated: 2026-08-09
sources:
  - "[[Mengenal Matriks Pengertian, Jenis, dan Transpose]]"
  - "[[Operasi Aljabar pada Matriks Penjumlahan, Pengurangan & Perkalian]]"
  - "[[Cara Mencari Determinan & Invers Matriks Beserta Contohnya]]"
  - "[[Types of Matrices Definition, Properties, Formulas and Examples]]"
  - "[[Matrix Operations Addition, Subtraction, Multiplication, Inverse]]"
tags:
  - teaching-material
  - mathematics
  - matriks
---

# Menaklukkan Matriks: Dari Konsep Dasar Sampai Invers tanpa Pusing! 🚀

Halo teman-teman! Kalau denger kata **Matriks**, apa yang langsung terlintas di pikiranmu? Film fiksi ilmiah *The Matrix* yang ikonik itu? Atau tabel berisi tumpukan angka yang bikin dahi berkerut? 😄

Tenang aja! Di modul ini kita bakal bedah semua konsep matriks—mulai dari cara baca susunannya, jenis-jenis matriks khusus, sifat-sifat operasi aljabar, determinan, invers (ordo $2 \times 2$ & $3 \times 3$), hingga penyelesaian Sistem Persamaan Linear (SPL)—dengan bahasa yang santai, kasual, dan gampang dicerna!

---

## 1. Kenalan dengan Matriks & Analogi Dunia Nyata

### Kenapa Harus Ada Matriks?
Bayangin kamu sama temen-temenmu lagi mau pesen nasi goreng di warung langganan. Pesenannya macem-macem: ada yang pedes telor dadar, pedes telor ceplok, sedang tanpa telor, dan seterusnya. Kalau dicatat pakai kalimat panjang, abang penjualnya pasti pusing dan rawan tertukar!

Tapi coba kalau catatannya kita rapikan jadi bentuk tabel sederhana:

| Tingkat Pedas | Telor Dadar | Telor Ceplok | Tanpa Telor |
| :--- | :---: | :---: | :---: |
| **Tidak Pedas** | 1 | 0 | 2 |
| **Sedang** | 3 | 2 | 1 |
| **Pedas** | 0 | 4 | 0 |

Nah, kalau judul baris dan kolomnya disingkirkan, lalu angka-angkanya dibungkus pakai tanda kurung, jadilah **Matriks**:

$$\begin{pmatrix} 1 & 0 & 2 \\ 3 & 2 & 1 \\ 0 & 4 & 0 \end{pmatrix}$$

Jadi sederhana dan rapi banget, kan?

### Definisi Matriks
Secara matematis, **Matriks** adalah **sekumpulan bilangan yang disusun berdasarkan urutan baris dan kolom, serta ditempatkan di dalam tanda kurung** (bisa kurung biasa `( )` atau kurung siku `[ ]`). Nama matriks selalu ditulis dengan **huruf kapital** (misal $A, B, C$).

---

## 2. Anatomi Matriks: Baris, Kolom, Ordo, dan Elemen

Mari kita pahami struktur pembentuk matriks:

```text
       Kolom 1   Kolom 2   Kolom 3
Baris 1 [   1        0        2   ]
Baris 2 [   3        2        1   ]
Baris 3 [   0        4        0   ]
```

* **Baris (Horizontal):** Susunan angka yang sejajar ke samping (kiri ke kanan). Baris ke-1 dari paling atas.
* **Kolom (Vertikal):** Susunan angka yang tegak lurus (atas ke bawah). Kolom ke-1 dari paling kiri.
* **Ordo (Ukuran Matriks):** Menyatakan banyaknya baris ($m$) dikali banyaknya kolom ($n$), ditulis $A_{m \times n}$.
  * **Matriks Horisontal:** Jika jumlah baris lebih sedikit dari kolom ($m < n$).
  * **Matriks Vertikal:** Jika jumlah baris lebih banyak dari kolom ($m > n$).
  * **Matriks Persegi:** Jika jumlah baris sama dengan kolom ($m = n$).
* **Elemen Matriks ($a_{ij}$):** Angka di dalam matriks pada **baris ke-$i$** dan **kolom ke-$j$**.
  * Contoh: $a_{21}$ artinya elemen pada baris ke-2 kolom ke-1, yaitu bernilai $3$.

---

## 3. Galeri Jenis-Jenis Matriks Khusus 🏛️

Selain matriks biasa, ada keluarga matriks khusus yang punya sifat-sifat unik:

### A. Berdasarkan Bentuk & Ordo
1. **Matriks Baris:** Cuma punya **satu baris** ($1 \times n$), misal $A = \begin{pmatrix} 4 & -1 & 7 \end{pmatrix}$.
2. **Matriks Kolom:** Cuma punya **satu kolom** ($m \times 1$), misal $B = \begin{pmatrix} 2 \\ 5 \\ -3 \end{pmatrix}$.
3. **Matriks Singleton:** Cuma punya **satu elemen** ($1 \times 1$), misal $S = [5]_{1 \times 1}$.
4. **Matriks Persegi:** Jumlah baris = jumlah kolom ($m = n$). Memiliki **Diagonal Utama** (kiri-atas ke kanan-bawah) dan **Diagonal Samping** (arah sebaliknya).

### B. Berdasarkan Elemen Diagonal & Elemen Khusus
5. **Matriks Nol ($O$):** Semua elemennya bernilai $0$.
6. **Matriks Diagonal:** Matriks persegi yang elemen di luar diagonal utamanya bernilai **nol**.
7. **Matriks Skalar:** Matriks diagonal yang semua elemen diagonal utamanya bernilai **sama** (misal angka $4$ semua).
8. **Matriks Identitas ($I$):** Matriks skalar yang elemen diagonal utamanya bernilai **1** dan lainnya **0**. (Angka 1-nya dunia matriks!).
9. **Matriks Segitiga (Triangular Matrix):**
   * **Segitiga Atas (Upper Triangular):** Elemen di **bawah** diagonal utama semuanya bernilai $0$.
   * **Segitiga Bawah (Lower Triangular):** Elemen di **atas** diagonal utama semuanya bernilai $0$.

### C. Berdasarkan Sifat Transpose & Perkalian
10. **Matriks Simetris:** Matriks yang jika ditranspose hasilnya **sama dengan dirinya sendiri** ($A^T = A$).
11. **Matriks Skew-Simetris:** Matriks yang jika ditranspose hasilnya **sama dengan negatif dirinya** ($A^T = -A$). Elemen diagonal utamanya selalu $0$.
12. **Matriks Ortogonal:** Matriks persegi yang transposenya sama dengan inversnya ($A^T = A^{-1} \implies A \cdot A^T = I$).
13. **Matriks Idempoten:** Matriks yang kalau dikalikan dengan dirinya sendiri hasilnya tetap sama ($A^2 = A$).
14. **Matriks Involutori:** Matriks yang jika dikuadratkan menghasilkan matriks identitas ($A^2 = I \implies A^{-1} = A$).

---

## 4. Transpose Matriks ($A^T$)

### Konsep Dasar
**Transpose matriks** adalah proses **menukarkan posisi baris menjadi kolom** dan **kolom menjadi baris**. Transpose dari matriks $A$ dinotasikan dengan $A^T$ atau $A^t$.

Jika $A$ berordo $m \times n$, maka $A^T$ berordo $n \times m$.

### Contoh Transpose
Misal matriks $A = \begin{pmatrix} 2 & 4 & 1 \\ 5 & 0 & 3 \end{pmatrix}$ (ordo $2 \times 3$).

Maka $A^T$ berordo $3 \times 2$:
$$A^T = \begin{pmatrix} 2 & 5 \\ 4 & 0 \\ 1 & 3 \end{pmatrix}$$

#### Sifat-sifat Transpose:
* $(A^T)^T = A$
* $(A + B)^T = A^T + B^T$
* $(k \cdot A)^T = k \cdot A^T$
* $(A \cdot B)^T = B^T \cdot A^T$ *(Ingat, posisinya dibalik!)*

---

## 5. Operasi Aljabar pada Matriks & Sifat-Sifatnya

### A. Penjumlahan & Pengurangan Matriks

#### Syarat Mutlak:
Dua atau lebih matriks **hanya bisa dijumlahkan atau dikurangkan jika memiliki ORDO YANG SAMA**.

#### Sifat-sifat Penjumlahan Matriks:
1. **Komutatif:** $A + B = B + A$
2. **Asosiatif:** $(A + B) + C = A + (B + C)$
3. **Identitas Penjumlahan:** $A + O = O + A = A$ (di mana $O$ adalah matriks nol)
4. **Invers Penjumlahan (Lawan Matriks):** $A + (-A) = O$

#### Contoh Pengurangan:
$A - B$ pada dasarnya adalah penjumlahan $A + (-B)$:
$$\begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix} - \begin{pmatrix} 0 & 5 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 3-0 & 1-5 \\ 4-(-1) & 2-3 \end{pmatrix} = \begin{pmatrix} 3 & -4 \\ 5 & -1 \end{pmatrix}$$

---

### B. Perkalian Matriks dengan Skalar (Bilangan Real)

#### Cara Pengerjaan & Sifat:
Kalikan **setiap elemen** di dalam matriks dengan skalar $k$.

* $k(A + B) = kA + kB$
* $(k + m)A = kA + mA$
* $k(mA) = (km)A$

---

### C. Perkalian Matriks dengan Matriks

#### Syarat Mutlak Perkalian Matriks:
Jumlah **kolom matriks pertama** harus sama dengan jumlah **baris matriks kedua**!

$$\underbrace{A_{m \times \mathbf{p}} \times B_{\mathbf{p} \times n}}_{\text{Sama!}} = C_{m \times n}$$

#### Metode "Baris dikali Kolom" (BaKo):
$$A \times B = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} (1 \cdot 5 + 2 \cdot 7) & (1 \cdot 6 + 2 \cdot 8) \\ (3 \cdot 5 + 4 \cdot 7) & (3 \cdot 6 + 4 \cdot 8) \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

#### Sifat-Sifat Perkalian Matriks:
* ⚠️ **TIDAK KOMUTATIF:** Umumnya $A \times B \neq B \times A$.
* **Asosiatif:** $(A \cdot B) \cdot C = A \cdot (B \cdot C)$
* **Distributif:** $A(B + C) = AB + AC$ dan $(A + B)C = AC + BC$
* **Identitas Perkalian:** $A \cdot I = I \cdot A = A$
* 💡 **Catatan Unik:** Jika $A \cdot B = O$, **tidak berarti** $A = O$ atau $B = O$! Dua matriks bukan nol bisa menghasilkan matriks nol saat dikalikan.

---

## 6. Determinan Matriks ($\det(A)$ atau $|A|$)

**Determinan** adalah sebuah nilai skalar tunggal yang diperoleh dari elemen-elemen matriks persegi.

### A. Determinan Ordo $2 \times 2$
Jika $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies \det(A) = ad - bc$

### B. Determinan Ordo $3 \times 3$ (Aturan Sarrus)
Salin 2 kolom pertama ke sebelah kanan matriks:
$$\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} \begin{matrix} a & b \\ d & e \\ g & h \end{matrix}$$

$$\det(A) = (aei + bfg + cdh) - (ceg + afh + bdi)$$

### C. Determinan Ordo $3 \times 3$ (Ekspansi Kofaktor / Metode Laplace)
Ekspansi kofaktor dapat dilakukan sepanjang **baris mana saja** atau **kolom mana saja** (disarankan memilih baris/kolom yang punya angka $0$ paling banyak).

Misal ekspansi sepanjang **Baris ke-1**:
$$\det(A) = a_{11} \cdot C_{11} + a_{12} \cdot C_{12} + a_{13} \cdot C_{13}$$

$$\det(A) = a_{11} \det\begin{pmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{pmatrix} - a_{12} \det\begin{pmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{pmatrix} + a_{13} \det\begin{pmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix}$$

#### Sifat-Sifat Determinan:
* $\det(A^T) = \det(A)$
* $\det(A \cdot B) = \det(A) \cdot \det(B)$
* $\det(A^{-1}) = \frac{1}{\det(A)}$
* $\det(k \cdot A_{n \times n}) = k^n \cdot \det(A)$

---

## 6.5 Bedah Tuntas Konsep Minor & Kofaktor 🔍

Banyak dari kita yang sering bingung membedakan antara **Minor**, **Kofaktor**, **Matriks Kofaktor**, dan **Adjoin**. Yuk, kita bedah satu per satu secara visual sampai tuntas!

### 1. Apa itu Minor ($M_{ij}$)?
**Minor ($M_{ij}$)** adalah nilai determinan matriks berordo lebih kecil (misal $2 \times 2$) yang diperoleh dengan cara **"menutup" (mencoret) baris ke-$i$ dan kolom ke-$j$** dari matriks utama.

#### 💡 Ilustrasi Visual Mencari Minor:
Misalkan kita punya matriks $A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$.

* **Mencari $M_{11}$ (Tutup Baris 1 & Kolom 1):**
  $$\begin{pmatrix} \mathbf{\xcancel{a_{11}}} & \mathbf{\xcancel{a_{12}}} & \mathbf{\xcancel{a_{13}}} \\ \mathbf{\xcancel{a_{21}}} & a_{22} & a_{23} \\ \mathbf{\xcancel{a_{31}}} & a_{32} & a_{33} \end{pmatrix} \implies M_{11} = \det\begin{pmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{pmatrix} = a_{22}a_{33} - a_{23}a_{32}$$

* **Mencari $M_{12}$ (Tutup Baris 1 & Kolom 2):**
  $$\begin{pmatrix} \mathbf{\xcancel{a_{11}}} & \mathbf{\xcancel{a_{12}}} & \mathbf{\xcancel{a_{13}}} \\ a_{21} & \mathbf{\xcancel{a_{22}}} & a_{23} \\ a_{31} & \mathbf{\xcancel{a_{32}}} & a_{33} \end{pmatrix} \implies M_{12} = \det\begin{pmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{pmatrix} = a_{21}a_{33} - a_{23}a_{31}$$

* **Mencari $M_{23}$ (Tutup Baris 2 & Kolom 3):**
  $$\begin{pmatrix} a_{11} & a_{12} & \mathbf{\xcancel{a_{13}}} \\ \mathbf{\xcancel{a_{21}}} & \mathbf{\xcancel{a_{22}}} & \mathbf{\xcancel{a_{23}}} \\ a_{31} & a_{32} & \mathbf{\xcancel{a_{33}}} \end{pmatrix} \implies M_{23} = \det\begin{pmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} \end{pmatrix} = a_{11}a_{32} - a_{12}a_{31}$$

---

### 2. Apa itu Kofaktor ($C_{ij}$)?
**Kofaktor ($C_{ij}$)** pada dasarnya adalah **Minor yang diberi tanda posisional $(+)$ atau $(-)$**.

#### Rumus Utama Kofaktor:
$$C_{ij} = (-1)^{i+j} \cdot M_{ij}$$

#### Dari Mana Asal Tanda $(-1)^{i+j}$?
Perhatikan nilai $(-1)^{i+j}$ bergantung pada penjumlahan nomor baris ($i$) dan kolom ($j$):
* **Jika $(i + j)$ GENAP:** $(-1)^{\text{genap}} = \mathbf{+1} \implies C_{ij} = +M_{ij}$ (Tanda minor tetap!).
  * *Contoh:* Posisi $C_{11} \implies 1+1=2$ (genap) $\implies C_{11} = +M_{11}$.
  * *Contoh:* Posisi $C_{22} \implies 2+2=4$ (genap) $\implies C_{22} = +M_{22}$.
* **Jika $(i + j)$ GANJIL:** $(-1)^{\text{ganjil}} = \mathbf{-1} \implies C_{ij} = -M_{ij}$ (Tanda minor diubah jadi lawannya!).
  * *Contoh:* Posisi $C_{12} \implies 1+2=3$ (ganjil) $\implies C_{12} = -M_{12}$.
  * *Contoh:* Posisi $C_{23} \implies 2+3=5$ (ganjil) $\implies C_{23} = -M_{23}$.

#### Tanda Kofaktor Membentuk Pola Papan Catur (*Checkerboard Pattern*):
Agar tidak perlu menghitung $(-1)^{i+j}$ satu per satu, kamu cukup mengingat pola tanda selang-seling ini:

Untuk matriks $3 \times 3$:
$$\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}$$

---

### 3. Membedakan Matriks Kofaktor & Matriks Adjoin

Agar tidak tertukar saat pengerjaan soal:

1. **Matriks Minor:** Matriks yang elemen-elemennya berupa nilai minor $M_{ij}$:
   $$\text{Min}(A) = \begin{pmatrix} M_{11} & M_{12} & M_{13} \\ M_{21} & M_{22} & M_{23} \\ M_{31} & M_{32} & M_{33} \end{pmatrix}$$

2. **Matriks Kofaktor ($\text{Cof}(A)$):** Matriks Minor yang setiap elemennya sudah diberi tanda papan catur:
   $$\text{Cof}(A) = \begin{pmatrix} +M_{11} & -M_{12} & +M_{13} \\ -M_{21} & +M_{22} & -M_{23} \\ +M_{31} & -M_{32} & +M_{33} \end{pmatrix} = \begin{pmatrix} C_{11} & C_{12} & C_{13} \\ C_{21} & C_{22} & C_{23} \\ C_{31} & C_{32} & C_{33} \end{pmatrix}$$

3. **Matriks Adjoin ($\text{Adj}(A)$):** **TRANSPOSE dari Matriks Kofaktor**! (Tukar baris jadi kolom):
   $$\text{Adj}(A) = (\text{Cof}(A))^T = \begin{pmatrix} C_{11} & C_{21} & C_{31} \\ C_{12} & C_{22} & C_{32} \\ C_{13} & C_{23} & C_{33} \end{pmatrix}$$

---

### 4. Ringkasan Hubungan Alur Kerja Minor $\to$ Adjoin

```text
[Matriks A] 
    │
    ▼ (Tutup baris i & kolom j, hitung determinan 2x2)
[Minor M_ij] 
    │
    ▼ (Kalikan dengan tanda papan catur (-1)^(i+j))
[Kofaktor C_ij / Matriks Cof(A)] 
    │
    ▼ (Transpose baris <-> kolom)
[Matriks Adjoin Adj(A)] 
    │
    ▼ (Kalikan dengan 1 / det(A))
[Invers A^-1]
```

---

## 7. Invers Matriks ($A^{-1}$)

### Konsep Utama
Invers matriks $A$ adalah matriks $A^{-1}$ yang jika dikalikan dengan $A$ menghasilkan matriks identitas ($I$):
$$A \times A^{-1} = A^{-1} \times A = I$$

* Jika $\det(A) \neq 0 \implies$ **Nonsingular** (Memiliki Invers).
* Jika $\det(A) = 0 \implies$ **Singular** (TIDAK Memiliki Invers).

---

### A. Rumus Invers Ordo $2 \times 2$
$$A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

---

### B. Invers Ordo $3 \times 3$ (Metode Adjoin: Minor & Kofaktor) 🎯

Untuk mencari invers matriks ordo $3 \times 3$, kita gunakan rumus umum:
$$A^{-1} = \frac{1}{\det(A)} \cdot \text{Adj}(A)$$

Berikut adalah **4 Langkah Sistematis** untuk menaklukkan invers $3 \times 3$:

#### Langkah 1: Hitung Determinan $\det(A)$
Hitung $\det(A)$ menggunakan Aturan Sarrus atau Ekspansi Kofaktor. Pastikan $\det(A) \neq 0$.

#### Langkah 2: Hitung 9 Kofaktor ($C_{ij} = (-1)^{i+j} M_{ij}$)
Gunakan rumus kofaktor atau pola papan catur $\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}$ yang sudah kita pelajari di atas.

#### Langkah 3: Susun Matriks Kofaktor $\text{Cof}(A)$ dan Matriks Adjoin $\text{Adj}(A)$
* **Matriks Kofaktor:** $\text{Cof}(A) = \begin{pmatrix} C_{11} & C_{12} & C_{13} \\ C_{21} & C_{22} & C_{23} \\ C_{31} & C_{32} & C_{33} \end{pmatrix}$
* **Matriks Adjoin:** Transpose dari matriks kofaktor!
  $$\text{Adj}(A) = (\text{Cof}(A))^T = \begin{pmatrix} C_{11} & C_{21} & C_{31} \\ C_{12} & C_{22} & C_{32} \\ C_{13} & C_{23} & C_{33} \end{pmatrix}$$

#### Langkah 4: Kalikan dengan $\frac{1}{\det(A)}$
$$A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} C_{11} & C_{21} & C_{31} \\ C_{12} & C_{22} & C_{32} \\ C_{13} & C_{23} & C_{33} \end{pmatrix}$$

---

#### 💡 Contoh Konkret Perhitungan Invers $3 \times 3$ Step-by-Step

Diketahui matriks $A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 3 & 1 \\ 2 & 0 & 1 \end{pmatrix}$. Tentukan $A^{-1}$!

**1. Hitung $\det(A)$ (Ekspansi Baris ke-1):**
$$\det(A) = 1(3\cdot 1 - 1\cdot 0) - 2(0\cdot 1 - 1\cdot 2) + 1(0\cdot 0 - 3\cdot 2)$$
$$\det(A) = 1(3) - 2(-2) + 1(-6) = 3 + 4 - 6 = 1$$
*(Karena $\det(A) = 1 \neq 0$, matriks $A$ memiliki invers).*

**2. Hitung 9 Kofaktor ($C_{ij}$):**
* $C_{11} = +(3\cdot 1 - 1\cdot 0) = 3$
* $C_{12} = -(0\cdot 1 - 1\cdot 2) = -(-2) = 2$
* $C_{13} = +(0\cdot 0 - 3\cdot 2) = -6$
* $C_{21} = -(2\cdot 1 - 1\cdot 0) = -2$
* $C_{22} = +(1\cdot 1 - 1\cdot 2) = -1$
* $C_{23} = -(1\cdot 0 - 2\cdot 2) = -(-4) = 4$
* $C_{31} = +(2\cdot 1 - 1\cdot 3) = -1$
* $C_{32} = -(1\cdot 1 - 1\cdot 0) = -1$
* $C_{33} = +(1\cdot 3 - 2\cdot 0) = 3$

**3. Susun Matriks Kofaktor & Transpose menjadi Adjoin:**
$$\text{Cof}(A) = \begin{pmatrix} 3 & 2 & -6 \\ -2 & -1 & 4 \\ -1 & -1 & 3 \end{pmatrix} \implies \text{Adj}(A) = (\text{Cof}(A))^T = \begin{pmatrix} 3 & -2 & -1 \\ 2 & -1 & -1 \\ -6 & 4 & 3 \end{pmatrix}$$

**4. Hitung Invers $A^{-1}$:**
$$A^{-1} = \frac{1}{1} \begin{pmatrix} 3 & -2 & -1 \\ 2 & -1 & -1 \\ -6 & 4 & 3 \end{pmatrix} = \begin{pmatrix} 3 & -2 & -1 \\ 2 & -1 & -1 \\ -6 & 4 & 3 \end{pmatrix}$$

---

### C. Catatan Metode Operasi Baris Elementer (OBE / Gauss-Jordan)
Selain metode Adjoin, invers $3 \times 3$ dapat dicari dengan menggandengkan matriks $A$ dengan matriks identitas $I$:
$$[A \mid I] \xrightarrow{\text{Operasi Baris}} [I \mid A^{-1}]$$
Melalui transformasi baris (tukar baris, kalikan skalar, jumlahkan kelipatan baris), sisi kiri diubah menjadi $I$, sehingga sisi kanan otomatis menjadi $A^{-1}$.

#### Sifat-Sifat Invers Matriks:
* $(A^{-1})^{-1} = A$
* $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$ *(Posisinya dibalik!)*
* $(A^T)^{-1} = (A^{-1})^T$

---

## 8. Persamaan Matriks ($AX = B$ dan $XA = B$) 🗝️

Karena perkalian matriks **TIDAK KOMUTATIF** ($AB \neq BA$), letak perkalian invers sangat krusial!

### 1. Bentuk $A \cdot X = B$
Untuk mengisolasi $X$, kalikan **kedua ruas dari KIRI** dengan $A^{-1}$:
$$A^{-1} \cdot (A \cdot X) = A^{-1} \cdot B \implies I \cdot X = A^{-1} \cdot B \implies \mathbf{X = A^{-1} \cdot B}$$

### 2. Bentuk $X \cdot A = B$
Untuk mengisolasi $X$, kalikan **kedua ruas dari KANAN** dengan $A^{-1}$:
$$(X \cdot A) \cdot A^{-1} = B \cdot A^{-1} \implies X \cdot I = B \cdot A^{-1} \implies \mathbf{X = B \cdot A^{-1}}$$

> [!WARNING]
> Jangan sampai terbalik! $AX = B \implies X = A^{-1}B$, sedangkan $XA = B \implies X = BA^{-1}$.

---

## 9. Penerapan Matriks dalam Sistem Persamaan Linear (SPL) 📐

Sistem Persamaan Linear dapat diubah ke dalam bentuk persamaan matriks $A \cdot X = B$.

Contoh Sistem Persamaan Linear 2 Variabel (SPLDV):
$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases} \implies \begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$

Ada dua metode utama untuk menyelesaikannya:

### A. Metode Invers Matriks
Gunakan rumus $X = A^{-1} \cdot B$:
$$\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{a_1 b_2 - b_1 a_2} \begin{pmatrix} b_2 & -b_1 \\ -a_2 & a_1 \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$

---

### B. Metode Aturan Cramer (Cramer's Rule)
Aturan Cramer menggunakan determinan matriks utama dan determinan matriks pengganti:

1. **Determinan Utama ($D$ atau $\det(A)$):**
   $$D = \det\begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix}$$
2. **Determinan $D_x$:** Ganti kolom variabel $x$ (kolom 1) dengan matriks konstanta $B$:
   $$D_x = \det\begin{pmatrix} c_1 & b_1 \\ c_2 & b_2 \end{pmatrix}$$
3. **Determinan $D_y$:** Ganti kolom variabel $y$ (kolom 2) dengan matriks konstanta $B$:
   $$D_y = \det\begin{pmatrix} a_1 & c_1 \\ a_2 & c_2 \end{pmatrix}$$

**Nilai Variabel:**
$$x = \frac{D_x}{D} \quad \text{dan} \quad y = \frac{D_y}{D} \quad (\text{dengan syarat } D \neq 0)$$

*(Metode Cramer ini juga berlaku identik untuk SPLTV 3 variabel: $x = \frac{D_x}{D}$, $y = \frac{D_y}{D}$, $z = \frac{D_z}{D}$).*

---

## 10. Cheatsheet Ringkas & Panduan Cepat 📌

| Jenis / Operasi | Formula / Syarat Kunci | Sifat / Catatan Penting |
| :--- | :--- | :--- |
| **Simetris** | $A^T = A$ | Elemen cermin terhadap diag. utama sama |
| **Skew-Simetris** | $A^T = -A$ | Diagonal utama bernilai $0$ |
| **Ortogonal** | $A \cdot A^T = I$ | Invers sama dengan transpose ($A^{-1} = A^T$) |
| **Perkalian** | $A_{m \times p} \cdot B_{p \times n} = C_{m \times n}$ | **TIDAK komutatif** ($AB \neq BA$) |
| **Determinan $3 \times 3$** | Sarrus / Ekspansi Kofaktor | $\det(AB) = \det(A)\det(B)$ |
| **Invers $2 \times 2$** | $\frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ | Syarat: $\det(A) \neq 0$ (Nonsingular) |
| **Invers $3 \times 3$** | $A^{-1} = \frac{1}{\det(A)} \text{Adj}(A)$ | $\text{Adj}(A) = (\text{Cof}(A))^T$ |
| **Persamaan $AX = B$** | $X = A^{-1} \cdot B$ | Kiri dikali $A^{-1}$ |
| **Persamaan $XA = B$** | $X = B \cdot A^{-1}$ | Kanan dikali $A^{-1}$ |
| **Aturan Cramer** | $x = \frac{D_x}{D}, y = \frac{D_y}{D}, z = \frac{D_z}{D}$ | Praktis untuk SPLDV & SPLTV |

Semangat berlatih, makin sering coba corat-coret latihan soal, makin lincah ngerjain soal matriks! 🎯

---

## 📝 Lembar Kerja & Soal Evaluasi Terkait
- [[LKPD Matriks SMA]]
- [[index teaching|🍎 Teaching Resources Hub]]
