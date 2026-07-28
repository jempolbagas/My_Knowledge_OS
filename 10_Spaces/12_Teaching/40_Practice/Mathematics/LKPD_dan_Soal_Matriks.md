---
title: "LKPD & Latihan Soal Evaluasi: Matriks"
target_audience: "SMA Kelas 11"
created: 2026-07-28
sources:
  - "[[Materi_Matriks]]"
tags:
  - lkpd
  - practice
  - mathematics
  - matriks
---

# Lembar Kerja Peserta Didik (LKPD) & Latihan Soal: Matriks 📊

**Nama Kelompok / Peserta Didik:** .....................................................  
**Kelas:** XI (Sebelas)  
**Mata Pelajaran:** Matematika  
**Topik Utama:** Konsep Matriks, Operasi Aljabar, Determinan, & Invers Matriks  

---

## 🎯 Tujuan Pembelajaran
1. Peserta didik dapat mengidentifikasi ordo, elemen, dan transpose matriks dari konteks kehidupan nyata.
2. Peserta didik dapat menyelesaikan masalah konstekstual yang berkaitan dengan penjumlahan, pengurangan, dan perkalian matriks.
3. Peserta didik dapat menghitung determinan dan invers matriks $2 \times 2$ serta menggunakannya dalam pemecahan masalah sederhana (termasuk enkripsi/dekripsi pesan rahasia).

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

### 👥 Aktivitas 3: Detektif Kriptografi Matriks (Dekripsi Pesan Rahasia dengan Invers)

**Konteks Kasus:**  
Seorang agen rahasia mengirimkan pesan berkode berbentuk matriks matriks enkripsi.
Pesan asli dibentuk menjadi vektor kolom $X = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$.
Pesan tersebut dienkripsi menggunakan matriks kunci $K = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}$, sehingga menghasilkan matriks kode rahasia $Y = K \cdot X = \begin{pmatrix} 16 \\ 7 \end{pmatrix}$.

**Instruksi Kerjakan Bersama Kelompok:**

1. Tentukan determinan dari matriks kunci $K$! Apakah matriks kunci $K$ memiliki invers?
2. Hitung invers dari matriks kunci $K^{-1}$!
3. Temukan isi pesan asli $X$ dengan menggunakan rumus $X = K^{-1} \cdot Y$!

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

---

### 📝 B. Soal Uraian Penalaran

**1.** Dua buah matriks $A$ dan $B$ berordo $2 \times 2$ memenuhi persamaan $A \cdot \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 1 & 0 \end{pmatrix}$. Tentukanlah matriks $A$!

**2.** Diketahui toko perlengkapan sekolah menjual dua paket alat tulis:
* Paket A: 3 Buku Tulis + 2 Pensil = Rp 18.000
* Paket B: 2 Buku Tulis + 4 Pensil = Rp 20.000  
Sajikan permasalahan di atas ke dalam persamaan matriks $A \cdot X = B$, lalu selesaikan dengan invers matriks untuk menentukan harga 1 buku tulis dan 1 pensil!

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
3. $P \times H = \begin{pmatrix} (5 \cdot 14.000 + 2 \cdot 18.000 + 3 \cdot 16.000) \\ (3 \cdot 14.000 + 1 \cdot 18.000 + 2 \cdot 16.000) \end{pmatrix} = \begin{pmatrix} 70.000 + 36.000 + 48.000 \\ 42.000 + 18.000 + 32.000 \end{pmatrix} = \begin{pmatrix} 154.000 \\ 92.000 \end{pmatrix}$
   * Total biaya 1 Paket Super = **Rp 154.000**
   * Total biaya 1 Paket Hemat = **Rp 92.000**

### Aktivitas 3:
1. $\det(K) = (3 \cdot 1) - (2 \cdot 1) = 3 - 2 = 1 \neq 0$. Memiliki invers (Nonsingular).
2. $K^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}$
3. $X = K^{-1} \cdot Y = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix} \begin{pmatrix} 16 \\ 7 \end{pmatrix} = \begin{pmatrix} (16 - 14) \\ (-16 + 21) \end{pmatrix} = \begin{pmatrix} 2 \\ 5 \end{pmatrix}$.  
   Pesan asli $X$: $x_1 = 2$, $x_2 = 5$.

---

## 🔑 Kunci Jawaban & Pembahasan Bagian II (Latihan Soal Mandiri)

### A. Pilihan Ganda
1. **Jawaban: C ($7$)**  
   *Pembahasan:*  
   $A = B^T \implies \begin{pmatrix} 2a & 4 \\ 3 & b+1 \end{pmatrix} = \begin{pmatrix} 6 & 3 \\ 4 & 5 \end{pmatrix}$.  
   * $2a = 6 \implies a = 3$  
   * $b+1 = 5 \implies b = 4$  
   * $a + b = 3 + 4 = 7$.

2. **Jawaban: A ($\begin{pmatrix} 5 & -2 \\ -2 & 6 \end{pmatrix}$)**  
   *Pembahasan:*  
   $2K = 2 \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 0 & 6 \end{pmatrix}$.  
   $2K - L = \begin{pmatrix} 4 - (-1) & 2 - 4 \\ 0 - 2 & 6 - 0 \end{pmatrix} = \begin{pmatrix} 5 & -2 \\ -2 & 6 \end{pmatrix}$.

3. **Jawaban: B ($6$)**  
   *Pembahasan:*  
   $P \times Q = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} a & 0 \\ 1 & b \end{pmatrix} = \begin{pmatrix} a+2 & 2b \\ 3a+4 & 4b \end{pmatrix}$.  
   Samakan dengan $\begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix}$:  
   * $a + 2 = 4 \implies a = 2$  
   * $2b = 6 \implies b = 3$  
   * $a \times b = 2 \times 3 = 6$.

4. **Jawaban: C ($59$)**  
   *Pembahasan (Sarrus):*  
   $\det(M) = (3 \cdot 4 \cdot 5 + (-2) \cdot 0 \cdot 2 + 1 \cdot 1 \cdot 1) - (1 \cdot 4 \cdot 2 + 3 \cdot 0 \cdot 1 + (-2) \cdot 1 \cdot 5)$  
   $\det(M) = (60 + 0 + 1) - (8 + 0 - 10) = 61 - (-2) = 61 + 2 = 63$. (Revisi: **Jawaban D ($63$)**).

5. **Jawaban: A ($x = 3$ atau $x = -2$)**  
   *Pembahasan:*  
   Matriks singular $\implies \det(A) = 0$.  
   $x(x+1) - (2 \cdot 3) = 0 \implies x^2 + x - 6 = 0 \implies (x+3)(x-2) = 0$.  
   $x = -3$ atau $x = 2$. (Jawaban: **B**).

---

### B. Uraian Penalaran

1. Misal $A \cdot M = N$, maka $A = N \cdot M^{-1}$.  
   $M = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \implies \det(M) = 6 - 5 = 1 \implies M^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.  
   $A = \begin{pmatrix} 4 & 2 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} (12 - 10) & (-4 + 4) \\ (3 - 0) & (-1 + 0) \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 3 & -1 \end{pmatrix}$.

2. Model Matriks: $\begin{pmatrix} 3 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 18.000 \\ 20.000 \end{pmatrix}$.  
   $\det = 12 - 4 = 8$. Invers: $\frac{1}{8} \begin{pmatrix} 4 & -2 \\ -2 & 3 \end{pmatrix}$.  
   $\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{8} \begin{pmatrix} 4 & -2 \\ -2 & 3 \end{pmatrix} \begin{pmatrix} 18.000 \\ 20.000 \end{pmatrix} = \frac{1}{8} \begin{pmatrix} 72.000 - 40.000 \\ -36.000 + 60.000 \end{pmatrix} = \frac{1}{8} \begin{pmatrix} 32.000 \\ 24.000 \end{pmatrix} = \begin{pmatrix} 4.000 \\ 3.000 \end{pmatrix}$.  
   **Jadi, harga 1 buku tulis = Rp 4.000 dan 1 pensil = Rp 3.000.**

---

## 📊 Rubrik Penilaian & Pedoman Penskoran

| Bagian | Kriteria Penilaian | Skor Maksimal |
| :--- | :--- | :---: |
| **LKPD Aktivitas Kelompok** | Pemodelan matriks, operasi, dan dekripsi tepat | 30 |
| **Pilihan Ganda** | 5 Soal x 8 Poin per soal | 40 |
| **Soal Uraian 1** | Langkah pemodelan & penggunaan invers tepat | 15 |
| **Soal Uraian 2** | Pemodelan SPLDV ke matriks & penyelesaian tepat | 15 |
| **TOTAL SKOR** | | **100** |
