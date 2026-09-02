---
title: "LKPD: Matriks SMA"
type: lkpd
subject: mathematics
level: sma
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-07-28
updated: 2026-09-02
sources:
  - "[[Matriks SMA]]"
  - "[[Konsep_Dasar_dan_Klasifikasi_Matriks_SMA]]"
  - "[[Operasi_Aljabar_dan_Sifat_Matriks_SMA]]"
  - "[[Determinan_Matriks_dan_Sifatnya_SMA]]"
  - "[[Minor_Kofaktor_dan_Invers_Matriks_SMA]]"
  - "[[Persamaan_Matriks_dan_Sistem_Persamaan_Linear_SMA]]"
tags:
  - lkpd
  - practice
  - teaching/mathematics
  - level/sma
  - topic/matrix-practice
---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Konsep_Dasar_dan_Klasifikasi_Matriks_SMA|Modul 1]] | [[Operasi_Aljabar_dan_Sifat_Matriks_SMA|Modul 2]] | [[Determinan_Matriks_dan_Sifatnya_SMA|Modul 3]] | [[Minor_Kofaktor_dan_Invers_Matriks_SMA|Modul 4]] | [[Persamaan_Matriks_dan_Sistem_Persamaan_Linear_SMA|Modul 5]] | **📝 LKPD & Latihan**

---

# Lembar Kerja Peserta Didik (LKPD): Matriks 📝

**Nama Kelompok / Peserta Didik:** .....................................................  
**Kelas:** XI (Sebelas) — Fase F  
**Mata Pelajaran:** Matematika  
**Topik Utama:** Konsep Matriks, Operasi Aljabar, Determinan, Invers Matriks ($2 \times 2$ & $3 \times 3$), & Sistem Persamaan Linear  

---

## 🎯 Tujuan Pembelajaran
1. Peserta didik dapat mengidentifikasi ordo, elemen, dan transpose matriks dari konteks kehidupan nyata.
2. Peserta didik dapat menyelesaikan masalah kontekstual yang berkaitan dengan penjumlahan, pengurangan, dan perkalian matriks.
3. Peserta didik dapat menghitung determinan dan invers matriks ordo $2 \times 2$ serta $3 \times 3$ menggunakan metode Adjoin (Minor & Kofaktor).
4. Peserta didik dapat menyelesaikan masalah kontekstual dan sistem persamaan linear (SPLDV & SPLTV) menggunakan invers matriks dan Aturan Cramer.

---

# BAGIAN I: Lembar Kerja Peserta Didik (LKPD Aktivitas Kelompok)

### 👥 Aktivitas 1: Pemodelan Data Warung Kopi Kekinian (Ordo, Elemen, & Transpose)

**Konteks Kasus:**  
Dua cabang Warung Kopi "Kopi Senja" mencatat jumlah penjualan 3 jenis minuman utama (Es Kopi Susu, Matcha Latte, Americano) selama 2 shift (Shift Pagi & Shift Malam) dalam satu hari:

* **Cabang A:**
  * Shift Pagi: 40 Es Kopi Susu, 25 Matcha Latte, 15 Americano
  * Shift Malam: 60 Es Kopi Susu, 35 Matcha Latte, 30 Americano
* **Cabang B:**
  * Shift Pagi: 50 Es Kopi Susu, 20 Matcha Latte, 10 Americano
  * Shift Malam: 70 Es Kopi Susu, 40 Matcha Latte, 25 Americano

**Instruksi Kerjakan Bersama Kelompok:**

1. **Sajikan** data penjualan **Cabang A** ke dalam bentuk matriks $A$ dan **Cabang B** ke dalam bentuk matriks $B$! (Baris menyatakan Shift, Kolom menyatakan Jenis Minuman).
2. Tentukan **ordo** dari matriks $A$ dan matriks $B$!
3. Sebutkan nilai dari elemen $a_{21}$ dan $b_{13}$, lalu jelaskan artinya dalam konteks penjualan kopi!
4. Tentukan **transpose** dari matriks $A$ (yaitu $A^T$)! Apa arti perubahan baris dan kolom setelah ditranspose?

---

### 👥 Aktivitas 2: Analisis Keuangan & Penjualan Paket Sembako (Operasi Matriks)

**Konteks Kasus:**  
Sebuah toko kelontong membuat 2 jenis paket sembako untuk bakti sosial:
* **Paket Super:** 5 kg Beras, 2 liter Minyak Goreng, 3 kg Gula.
* **Paket Hemat:** 3 kg Beras, 1 liter Minyak Goreng, 2 kg Gula.

Harga bahan pokok per unit adalah: Beras = Rp 14.000/kg, Minyak Goreng = Rp 18.000/liter, Gula = Rp 16.000/kg.

**Instruksi Kerjakan Bersama Kelompok:**

1. Susun matriks kebutuhan bahan paket sembako $P_{2 \times 3}$ (Baris: Jenis Paket, Kolom: Jenis Bahan).
2. Susun matriks harga bahan pokok $H_{3 \times 1}$ (Baris: Jenis Bahan, Kolom: Harga per unit).
3. Dengan menggunakan **Perkalian Matriks** $P \times H$, hitunglah total biaya pembuatan untuk 1 unit Paket Super dan 1 unit Paket Hemat!

---

### 👥 Aktivitas 3: Detektif Kriptografi Matriks $2 \times 2$ (Dekripsi Pesan Rahasia)

**Konteks Kasus:**  
Seorang agen rahasia mengirimkan pesan berkode berbentuk matriks enkripsi.
Pesan asli dibentuk menjadi vektor kolom $X = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$.
Pesan tersebut dienkripsi menggunakan matriks kunci $K = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}$, sehingga menghasilkan matriks kode rahasia $Y = K \cdot X = \begin{pmatrix} 16 \\ 7 \end{pmatrix}$.

**Instruksi Kerjakan Bersama Kelompok:**

1. Tentukan determinan dari matriks kunci $K$! Apakah matriks kunci $K$ memiliki invers?
2. Hitung invers dari matriks kunci $K^{-1}$!
3. Temukan isi pesan asli $X$ dengan menggunakan rumus $X = K^{-1} \cdot Y$!

---

### 👥 Aktivitas 4: Operasi Siber Kriptografi Matriks Ordo $3 \times 3$ (Metode Adjoin) 🔐

**Konteks Kasus:**  
Tim Keamanan Siber menemukan dokumen rahasia terenkripsi 3 angka berturut-turut $X = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}$.
Dokumen tersebut dienkripsi menggunakan matriks kunci ordo $3 \times 3$:
$$K = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 2 & 0 & 1 \end{pmatrix}$$

Hasil enkripsi menghasilkan matriks kode terenkripsi $Y = \begin{pmatrix} 7 \\ 4 \\ 11 \end{pmatrix}$.

**Instruksi Kerjakan Bersama Kelompok:**

1. Hitung determinan matriks $K$ ($\det(K)$)!
2. Tentukan **9 Nilai Kofaktor** ($C_{11}$ sampai $C_{33}$), lalu susun Matriks Kofaktor $\operatorname{Cof}(K)$!
3. Transpose matriks kofaktor tersebut untuk memperoleh Matriks Adjoin ($\operatorname{Adj}(K)$), lalu hitung Matriks Invers $K^{-1}$!
4. Dekripsi dan temukan nilai pesan asli $X$ dengan rumus $X = K^{-1} \cdot Y$!

---

# BAGIAN II: Latihan Soal Mandiri (Evaluasi Individu)

### 📝 A. Soal Pilihan Ganda (HOTS)

**1.** Diketahui matriks $A = \begin{pmatrix} 2a & 4 \\ 3 & b+1 \end{pmatrix}$ dan $B^T = \begin{pmatrix} 6 & 3 \\ 4 & 5 \end{pmatrix}$. Jika $A = B^T$, maka nilai dari $a + b$ adalah...  
A. $3$  
B. $5$  
C. $7$  
D. $8$  
E. $10$  

**2.** Diketahui matriks $K = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$ dan $L = \begin{pmatrix} -1 & 4 \\ 2 & 0 \end{pmatrix}$. Hasil dari $2K - L$ adalah...  
A. $\begin{pmatrix} 5 & -2 \\ -2 & 6 \end{pmatrix}$  
B. $\begin{pmatrix} 5 & -2 \\ 2 & 6 \end{pmatrix}$  
C. $\begin{pmatrix} 3 & -2 \\ -2 & 6 \end{pmatrix}$  
D. $\begin{pmatrix} 5 & 2 \\ -2 & 6 \end{pmatrix}$  
E. $\begin{pmatrix} 1 & -2 \\ -2 & 6 \end{pmatrix}$  

**3.** Jika matriks $P = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ dan $Q = \begin{pmatrix} a & 0 \\ 1 & b \end{pmatrix}$, serta $P \times Q = \begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix}$, maka nilai $a \times b$ adalah...  
A. $4$  
B. $6$  
C. $8$  
D. $12$  
E. $16$  

**4.** Nilai determinan dari matriks $M = \begin{pmatrix} 3 & -2 & 1 \\ 1 & 4 & 0 \\ 2 & 1 & 5 \end{pmatrix}$ adalah...  
A. $51$  
B. $55$  
C. $59$  
D. $63$  
E. $67$  

**5.** Sebuah matriks $A = \begin{pmatrix} x & 2 \\ 3 & x+1 \end{pmatrix}$ merupakan matriks singular. Nilai $x$ yang memenuhi adalah...  
A. $x = 3$ atau $x = -2$  
B. $x = -3$ atau $x = 2$  
C. $x = 6$ atau $x = -1$  
D. $x = -6$ atau $x = 1$  
E. $x = 2$ atau $x = 3$  

**6.** Matriks Adjoin ($\operatorname{Adj}(A)$) dari matriks $A = \begin{pmatrix} 1 & 0 & 2 \\ 2 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix}$ adalah...  
A. $\begin{pmatrix} 1 & 2 & -2 \\ -4 & 2 & 3 \\ 2 & -1 & 1 \end{pmatrix}$  
B. $\begin{pmatrix} 1 & -4 & 2 \\ 2 & 2 & -1 \\ -2 & 3 & 1 \end{pmatrix}$  
C. $\begin{pmatrix} 1 & 2 & 2 \\ -4 & 2 & -1 \\ -2 & 3 & 1 \end{pmatrix}$  
D. $\begin{pmatrix} -1 & 2 & -2 \\ 4 & -2 & 3 \\ -2 & 1 & -1 \end{pmatrix}$  
E. $\begin{pmatrix} 2 & 1 & -2 \\ -4 & 1 & 3 \\ 2 & -1 & 2 \end{pmatrix}$  

---

### 📝 B. Soal Uraian Penalaran

**1.** Dua buah matriks $A$ dan $B$ berordo $2 \times 2$ memenuhi persamaan $A \cdot \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 1 & 0 \end{pmatrix}$. Tentukanlah matriks $A$!

**2.** Diketahui toko perlengkapan sekolah menjual dua paket alat tulis:
* Paket A: 3 Buku Tulis + 2 Pensil = Rp 18.000
* Paket B: 2 Buku Tulis + 4 Pensil = Rp 20.000  
Sajikan permasalahan di atas ke dalam persamaan matriks $A \cdot X = B$, lalu selesaikan dengan invers matriks untuk menentukan harga 1 buku tulis dan 1 pensil!

**3.** Sebuah UMKM memproduksi 3 jenis kue kering (Nastar, Kastengel, Putri Salju). Penggunaan bahan baku tepung ($x$ kg), gula ($y$ kg), dan mentega ($z$ kg) dinyatakan dalam sistem persamaan linear berikut:
$$\begin{cases} x + z = 4 \\ y + z = 3 \\ 2x + y + z = 7 \end{cases}$$

a. Ubah sistem persamaan linear di atas ke dalam persamaan matriks $A \cdot X = B$!  
b. Hitung invers matriks koefisien $A^{-1}$ dengan metode Adjoin (Minor & Kofaktor)!  
c. Tentukan kebutuhan masing-masing bahan baku ($x, y, z$) dengan rumus $X = A^{-1} \cdot B$!

---

# BAGIAN III: Kunci Jawaban, Pembahasan, & Rubrik Penilaian

---

## 🔑 Kunci Jawaban Bagian I (LKPD Aktivitas Kelompok)

### Aktivitas 1:
1. $A = \begin{pmatrix} 40 & 25 & 15 \\ 60 & 35 & 30 \end{pmatrix}$, $B = \begin{pmatrix} 50 & 20 & 10 \\ 70 & 40 & 25 \end{pmatrix}$
2. Ordo matriks $A$ dan $B$ adalah $2 \times 3$ (2 baris, 3 kolom).
3. $a_{21} = 60$ (Penjualan Es Kopi Susu pada Shift Malam di Cabang A). $b_{13} = 10$ (Penjualan Americano pada Shift Pagi di Cabang B).
4. $A^T = \begin{pmatrix} 40 & 60 \\ 25 & 35 \\ 15 & 30 \end{pmatrix}$. Artinya: Baris sekarang menyatakan jenis minuman, dan Kolom menyatakan Shift.

### Aktivitas 2:
1. $P = \begin{pmatrix} 5 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix}$
2. $H = \begin{pmatrix} 14.000 \\ 18.000 \\ 16.000 \end{pmatrix}$
3. $P \times H = \begin{pmatrix} (5 \cdot 14.000 + 2 \cdot 18.000 + 3 \cdot 16.000) \\ (3 \cdot 14.000 + 1 \cdot 18.000 + 2 \cdot 16.000) \end{pmatrix} = \begin{pmatrix} 154.000 \\ 92.000 \end{pmatrix}$
   * Total biaya 1 Paket Super = **Rp 154.000**
   * Total biaya 1 Paket Hemat = **Rp 92.000**

### Aktivitas 3:
1. $\det(K) = (3 \cdot 1) - (2 \cdot 1) = 3 - 2 = 1 \neq 0$. Memiliki invers (Nonsingular).
2. $K^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}$
3. $X = K^{-1} \cdot Y = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix} \begin{pmatrix} 16 \\ 7 \end{pmatrix} = \begin{pmatrix} 2 \\ 5 \end{pmatrix} \implies x_1 = 2, x_2 = 5$.

### Aktivitas 4:
1. $\det(K) = 1(1-0) - 0 + 1(0-2) = 1 - 2 = -1$.
2. Kofaktor:
   * $C_{11} = 1, C_{12} = 0, C_{13} = -2$
   * $C_{21} = 0, C_{22} = -1, C_{23} = 0$
   * $C_{31} = -1, C_{32} = 0, C_{33} = 1$
   
   Matriks Kofaktor $\operatorname{Cof}(K) = \begin{pmatrix} 1 & 0 & -2 \\ 0 & -1 & 0 \\ -1 & 0 & 1 \end{pmatrix}$.
3. Matriks Adjoin $\operatorname{Adj}(K) = (\operatorname{Cof}(K))^T = \begin{pmatrix} 1 & 0 & -1 \\ 0 & -1 & 0 \\ -2 & 0 & 1 \end{pmatrix}$.  
   Invers $K^{-1} = \frac{1}{-1} \begin{pmatrix} 1 & 0 & -1 \\ 0 & -1 & 0 \\ -2 & 0 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 0 & 1 \\ 0 & 1 & 0 \\ 2 & 0 & -1 \end{pmatrix}$.
4. $X = K^{-1} \cdot Y = \begin{pmatrix} -1 & 0 & 1 \\ 0 & 1 & 0 \\ 2 & 0 & -1 \end{pmatrix} \begin{pmatrix} 7 \\ 4 \\ 11 \end{pmatrix} = \begin{pmatrix} -7 + 0 + 11 \\ 0 + 4 + 0 \\ 14 + 0 - 11 \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \\ 3 \end{pmatrix}$.  
   **Pesan Asli $X$:** $x_1 = 4, x_2 = 4, x_3 = 3$.

---

## 🔑 Kunci Jawaban & Pembahasan Bagian II (Latihan Soal Mandiri)

### A. Pilihan Ganda
1. **Jawaban: C ($7$)**  
   $A = B^T \implies 2a = 6 \implies a = 3$; $b+1 = 5 \implies b = 4$.  
   $a + b = 3 + 4 = 7$.

2. **Jawaban: A ($\begin{pmatrix} 5 & -2 \\ -2 & 6 \end{pmatrix}$)**  
   $2K - L = \begin{pmatrix} 4 & 2 \\ 0 & 6 \end{pmatrix} - \begin{pmatrix} -1 & 4 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 5 & -2 \\ -2 & 6 \end{pmatrix}$.

3. **Jawaban: B ($6$)**  
   $P \times Q = \begin{pmatrix} a+2 & 2b \\ 3a+4 & 4b \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix} \implies a = 2, b = 3 \implies a \times b = 6$.

4. **Jawaban: D ($63$)**  
   $\det(M) = (3 \cdot 4 \cdot 5 + (-2) \cdot 0 \cdot 2 + 1 \cdot 1 \cdot 1) - (1 \cdot 4 \cdot 2 + 3 \cdot 0 \cdot 1 + (-2) \cdot 1 \cdot 5) = 61 - (-2) = 63$.

5. **Jawaban: B ($x = -3$ atau $x = 2$)**  
   $\det(A) = 0 \implies x(x+1) - 6 = 0 \implies x^2 + x - 6 = 0 \implies (x+3)(x-2) = 0 \implies x = -3 \text{ atau } x = 2$.

6. **Jawaban: A ($\begin{pmatrix} 1 & 2 & -2 \\ -4 & 2 & 3 \\ 2 & -1 & 1 \end{pmatrix}$)**  
   Kofaktor:  
   $C_{11} = 1, C_{12} = -4, C_{13} = 2$  
   $C_{21} = 2, C_{22} = 2, C_{23} = -1$  
   $C_{31} = -2, C_{32} = 3, C_{33} = 1$  
   $\operatorname{Cof}(A) = \begin{pmatrix} 1 & -4 & 2 \\ 2 & 2 & -1 \\ -2 & 3 & 1 \end{pmatrix} \implies \operatorname{Adj}(A) = (\operatorname{Cof}(A))^T = \begin{pmatrix} 1 & 2 & -2 \\ -4 & 2 & 3 \\ 2 & -1 & 1 \end{pmatrix}$.

---

### B. Uraian Penalaran

1. Misal $A \cdot M = N \implies A = N \cdot M^{-1}$.  
   $M = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \implies M^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.  
   $A = \begin{pmatrix} 4 & 2 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 3 & -1 \end{pmatrix}$.

2. Model Matriks: $\begin{pmatrix} 3 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 18.000 \\ 20.000 \end{pmatrix}$.  
   $\det = 12 - 4 = 8 \implies \begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{8} \begin{pmatrix} 4 & -2 \\ -2 & 3 \end{pmatrix} \begin{pmatrix} 18.000 \\ 20.000 \end{pmatrix} = \begin{pmatrix} 4.000 \\ 3.000 \end{pmatrix}$.  
   **Jadi, 1 buku tulis = Rp 4.000 dan 1 pensil = Rp 3.000.**

3. **Penyelesaian SPLTV:**  
   a. Persamaan Matriks: $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 2 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \\ 7 \end{pmatrix}$  
   b. Determinan $\det(A) = -2$.  
      Matriks Adjoin $\operatorname{Adj}(A) = \begin{pmatrix} 0 & 1 & -1 \\ 2 & -1 & -1 \\ -2 & -1 & 1 \end{pmatrix}$.  
      Invers $A^{-1} = \begin{pmatrix} 0 & -1/2 & 1/2 \\ -1 & 1/2 & 1/2 \\ 1 & 1/2 & -1/2 \end{pmatrix}$.  
   c. $X = A^{-1} \cdot B = \begin{pmatrix} 0 & -1/2 & 1/2 \\ -1 & 1/2 & 1/2 \\ 1 & 1/2 & -1/2 \end{pmatrix} \begin{pmatrix} 4 \\ 3 \\ 7 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix}$.  
      **Bahan baku:** Tepung ($x$) = 2 kg, Gula ($y$) = 1 kg, Mentega ($z$) = 2 kg.

---

## 📊 Rubrik Penilaian & Pedoman Penskoran

| Bagian | Kriteria Penilaian | Skor Maksimal |
| :--- | :--- | :---: |
| **LKPD Aktivitas Kelompok** | Pemodelan matriks, operasi, dan dekripsi 2x2 & 3x3 tepat | 34 |
| **Pilihan Ganda** | 6 Soal x 5 Poin per soal | 30 |
| **Soal Uraian 1** | Persamaan $AX=B$, penggunaan invers tepat | 10 |
| **Soal Uraian 2** | Pemodelan SPLDV ke matriks & penyelesaian tepat | 12 |
| **Soal Uraian 3** | Pemodelan SPLTV, hitung Adjoin & Invers 3x3 tepat | 14 |
| **TOTAL SKOR** | | **100** |

---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Konsep_Dasar_dan_Klasifikasi_Matriks_SMA|Modul 1]] | [[Operasi_Aljabar_dan_Sifat_Matriks_SMA|Modul 2]] | [[Determinan_Matriks_dan_Sifatnya_SMA|Modul 3]] | [[Minor_Kofaktor_dan_Invers_Matriks_SMA|Modul 4]] | [[Persamaan_Matriks_dan_Sistem_Persamaan_Linear_SMA|Modul 5]] | **📝 LKPD & Latihan**
