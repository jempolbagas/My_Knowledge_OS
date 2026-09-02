---
title: "Operasi Aljabar dan Sifat-Sifat Matriks SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 11 (Fase F), Guru Matematika, dan Pembelajar Mandiri"
created: 2026-09-02
sources:
  - "[[Matriks SMA]]"
  - "[[Konsep_Dasar_dan_Klasifikasi_Matriks_SMA]]"
  - "[[Determinan_Matriks_dan_Sifatnya_SMA]]"
  - "[[LKPD Matriks SMA]]"
tags:
  - teaching/mathematics
  - mathematics/linear-algebra
  - level/sma
  - topic/matrix-operations
---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Konsep_Dasar_dan_Klasifikasi_Matriks_SMA|⬅️ Modul 1: Konsep & Jenis]] | **Modul 2: Operasi & Sifat** | [[Determinan_Matriks_dan_Sifatnya_SMA|Modul 3: Determinan ➡️]] | [[LKPD Matriks SMA|📝 LKPD]]

---

# Operasi Aljabar pada Matriks — Dari Penjumlahan Elemen Hingga Rahasia Perkalian BaKo ➕✖️

Dalam aljabar bilangan real biasa, kita sudah sangat terbiasa dengan aturan aritmatika seperti $2 \times 3 = 3 \times 2 = 6$, atau jika $a \cdot b = 0$ maka pasti $a = 0$ atau $b = 0$. Namun, begitu kita memasuki semesta **Aljabar Matriks**, banyak intuisi lama kita yang ditantang! 

Matriks bukan sekadar kumpulan angka biasa—matriks adalah representasi dari transformasi matematis. Oleh karena itu, operasi aljabar pada matriks memiliki aturan main, syarat dimensi, serta sifat-sifat khusus yang sangat unik. Mari kita bedah tuntas satu per satu!

---

## 1. Penjumlahan dan Pengurangan Matriks

### A. Syarat Mutlak Operasi
> [!IMPORTANT]
> **Syarat Penjumlahan & Pengurangan:**  
> Dua atau lebih matriks **HANYA BISA** dijumlahkan atau dikurangkan jika dan hanya jika memiliki **ORDO YANG SAMA PERSIS** ($m_A = m_B$ dan $n_A = n_B$).

Jika ordonya berbeda (misal matriks $2 \times 3$ dijumlahkan dengan $3 \times 2$), maka operasi tersebut **tidak terdefinisi** secara matematis!

### B. Cara Pengerjaan
Operasi dilakukan dengan cara **menjumlahkan atau mengurangkan elemen-elemen yang seletak (*corresponding entries*)**:

Jika $A = (a_{ij})_{m \times n}$ dan $B = (b_{ij})_{m \times n}$, maka:
$$A \pm B = C \implies c_{ij} = a_{ij} \pm b_{ij}$$

#### Contoh Konkret:
$$A = \begin{pmatrix} 5 & -2 & 3 \\ 1 & 4 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} -3 & 7 & 1 \\ 6 & -2 & 5 \end{pmatrix}$$

$$A + B = \begin{pmatrix} 5 + (-3) & -2 + 7 & 3 + 1 \\ 1 + 6 & 4 + (-2) & 0 + 5 \end{pmatrix} = \begin{pmatrix} 2 & 5 & 4 \\ 7 & 2 & 5 \end{pmatrix}$$

$$A - B = \begin{pmatrix} 5 - (-3) & -2 - 7 & 3 - 1 \\ 1 - 6 & 4 - (-2) & 0 - 5 \end{pmatrix} = \begin{pmatrix} 8 & -9 & 2 \\ -5 & 6 & -5 \end{pmatrix}$$

---

### C. Sifat-Sifat Aljabar Penjumlahan Matriks
Misalkan $A, B,$ dan $C$ adalah matriks-matriks berordo sama $m \times n$, dan $O$ adalah matriks nol:

1. **Sifat Komutatif:**
   $$A + B = B + A$$
2. **Sifat Asosiatif:**
   $$(A + B) + C = A + (B + C)$$
3. **Eksistensi Elemen Identitas Penjumlahan (Matriks Nol $O$):**
   $$A + O = O + A = A$$
4. **Eksistensi Invers Penjumlahan (Lawan Aditif $-A$):**
   $$A + (-A) = (-A) + A = O$$
   *(Di mana $-A$ adalah matriks yang setiap elemennya merupakan lawan tanda dari elemen $A$, yaitu $-a_{ij}$).*

---

## 2. Perkalian Matriks dengan Skalar

### A. Definisi
Perkalian matriks $A$ dengan suatu bilangan skalar real $k$ didefinisikan sebagai operasi **mengalikan setiap elemen di dalam matriks tersebut dengan bilangan $k$**:

$$k \cdot A = k \cdot (a_{ij})_{m \times n} = (k \cdot a_{ij})_{m \times n}$$

#### Contoh:
Jika $A = \begin{pmatrix} 3 & -1 \\ 4 & 2 \end{pmatrix}$, maka:
$$3A = 3 \begin{pmatrix} 3 & -1 \\ 4 & 2 \end{pmatrix} = \begin{pmatrix} 3(3) & 3(-1) \\ 3(4) & 3(2) \end{pmatrix} = \begin{pmatrix} 9 & -3 \\ 12 & 6 \end{pmatrix}$$

---

### B. Sifat-Sifat Perkalian Skalar
Misalkan $k$ dan $m$ adalah skalar real, serta $A$ dan $B$ adalah matriks berordo sama:

1. **Distributif terhadap Penjumlahan Matriks:**
   $$k(A + B) = kA + kB$$
2. **Distributif terhadap Penjumlahan Skalar:**
   $$(k + m)A = kA + mA$$
3. **Asosiatif Perkalian Skalar:**
   $$k(mA) = (km)A$$
4. **Perkalian dengan Skalar Satuan:**
   $$1 \cdot A = A \quad \text{dan} \quad (-1) \cdot A = -A$$

---

## 3. Perkalian Matriks dengan Matriks (Matriks $\times$ Matriks) 🎯

Perkalian dua matriks adalah salah satu operasi paling esensial dalam aljabar linear. Aturan perkalian matriks **bukanlah** mengalikan elemen seletak, melainkan menggunakan metode **"Baris dikali Kolom" (*Dot Product*)**.

### A. Syarat Kompatibilitas Dimensi
> [!IMPORTANT]
> **Syarat Mutlak Perkalian Matriks:**  
> Dua matriks $A$ dan $B$ **hanya dapat dikalikan ($A \times B$)** jika **jumlah kolom matriks pertama ($A$) sama dengan jumlah baris matriks kedua ($B$)**.

$$\underbrace{A_{m \times \mathbf{p}} \times B_{\mathbf{p} \times n}}_{\text{Harus Sama!}} = C_{m \times n}$$

Hasil perkalian matriks $C$ akan memiliki ukuran **baris dari matriks pertama ($m$)** dan **kolom dari matriks kedua ($n$)**.

---

### B. Mengapa Didefinisikan "Baris dikali Kolom"?
Bayangkan sebuah toko menjual 2 paket snack:
* **Paket Super ($P_1$):** 3 Cokelat, 2 Biskuit
* **Paket Hemat ($P_2$):** 1 Cokelat, 4 Biskuit

Jika harga Cokelat $= Rp5.000$ dan Biskuit $= Rp3.000$:
* Total harga Paket Super $= (3 \times 5.000) + (2 \times 3.000) = 15.000 + 6.000 = Rp21.000$
* Total harga Paket Hemat $= (1 \times 5.000) + (4 \times 3.000) = 5.000 + 12.000 = Rp17.000$

Dalam representasi matriks:
$$\begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix}_{2 \times 2} \begin{pmatrix} 5.000 \\ 3.000 \end{pmatrix}_{2 \times 1} = \begin{pmatrix} 3(5.000) + 2(3.000) \\ 1(5.000) + 4(3.000) \end{pmatrix} = \begin{pmatrix} 21.000 \\ 17.000 \end{pmatrix}_{2 \times 1}$$

Itulah alasan ilmiah mengapa perkalian matriks menggabungkan **seluruh komponen satu baris dengan satu kolom**!

---

### C. Rumus Umum & Skema Visual Perkalian
Elemen $c_{ij}$ pada matriks hasil kali $C = A \cdot B$ diperoleh dari hasil kali skalar antara **Baris ke-$i$ dari matriks $A$** dan **Kolom ke-$j$ dari matriks $B$**:

$$c_{ij} = \sum_{k=1}^p a_{ik} b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{ip}b_{pj}$$

```text
       [ b_11   b_12 ]
       [ b_21   b_22 ]
--------------------------------------------
[ a_11  a_12 ] | [ (a_11*b_11 + a_12*b_21)   (a_11*b_12 + a_12*b_22) ]
[ a_21  a_22 ] | [ (a_21*b_11 + a_22*b_21)   (a_21*b_12 + a_22*b_22) ]
```

#### Contoh Perhitungan Ordo $2 \times 2$:
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

$$A \cdot B = \begin{pmatrix} 1(5) + 2(7) & 1(6) + 2(8) \\ 3(5) + 4(7) & 3(6) + 4(8) \end{pmatrix} = \begin{pmatrix} 5 + 14 & 6 + 16 \\ 15 + 28 & 18 + 32 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

---

## 4. Pemangkatan Matriks Persegi

Pemangkatan matriks hanya terdefinisi untuk **matriks persegi** ($n \times n$).
Jika $A$ adalah matriks persegi dan $k$ adalah bilangan bulat positif:

$$A^1 = A$$
$$A^2 = A \cdot A$$
$$A^3 = A^2 \cdot A = A \cdot A \cdot A$$
$$A^k = \underbrace{A \cdot A \cdot \dots \cdot A}_{k \text{ faktor}}$$

Dan didefinisikan $A^0 = I$ (Matriks Identitas berordo sama).

---

## 5. Anomali & Perbedaan Krusial: Aljabar Matriks vs Bilangan Real ⚠️

Banyak siswa terjebak karena menyamakan aljabar matriks dengan aljabar biasa. Berikut adalah **4 perbedaan fundamental** yang wajib kamu kuasai:

### 1. Perkalian Matriks TIDAK KOMUTATIF Secara Umum
$$A \cdot B \neq B \cdot A$$

Mari kita buktikan dengan mengalikan $B \cdot A$ dari contoh di atas:
$$B \cdot A = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 5(1)+6(3) & 5(2)+6(4) \\ 7(1)+8(3) & 7(2)+8(4) \end{pmatrix} = \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix}$$

Perhatikan bahwa $\begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix} \neq \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix}$. Terbukti bahwa $AB \neq BA$!

> [!NOTE]
> Dua matriks dikatakan *komutatif* jika kebetulan $AB = BA$, misalnya perkalian matriks dengan matriks identitas ($AI = IA = A$) atau perkalian sesama matriks diagonal berordo sama.

---

### 2. Adanya Pembagi Nol (*Zero Divisors*)
Pada aljabar real, jika $a \cdot b = 0$, maka $a = 0$ atau $b = 0$.  
Namun pada matriks:
$$A \cdot B = O \quad \mathbf{\text{TIDAK MENJAMIN}} \quad A = O \text{ atau } B = O$$

#### Bukti Konkret:
Ambil $A = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} \neq O$ dan $B = \begin{pmatrix} 3 & 5 \\ 0 & 0 \end{pmatrix} \neq O$.  
Hasil kalinya:
$$A \cdot B = \begin{pmatrix} 0(3) + 2(0) & 0(5) + 2(0) \\ 0(3) + 0(0) & 0(5) + 0(0) \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O$$
Dua matriks non-nol dapat menghasilkan matriks nol ketika dikalikan!

---

### 3. Kegagalan Hukum Kanselasi (*Cancellation Law*)
Pada aljabar real, jika $ab = ac$ dan $a \neq 0$, kita bisa langsung mencoret $a$ sehingga $b = c$.  
Pada matriks:
$$A \cdot B = A \cdot C \quad \mathbf{\text{TIDAK BERARTI}} \quad B = C$$

Pencoretan matriks $A$ hanya boleh dilakukan **jika matriks $A$ memiliki invers ($A^{-1}$)**. Jika $A$ tidak memiliki invers (singular), persamaan $AB = AC$ bisa terpenuhi meskipun $B \neq C$.

---

### 4. Penjabaran Bentuk Kuadrat Aljabar
Karena perkalian tidak komutatif ($AB \neq BA$), rumus pemfaktoran aljabar biasa berubah:

* $$(A + B)^2 = (A + B)(A + B) = A^2 + AB + BA + B^2 \quad \mathbf{\neq A^2 + 2AB + B^2}$$
* $$(A - B)^2 = A^2 - AB - BA + B^2 \quad \mathbf{\neq A^2 - 2AB + B^2}$$
* $$(A + B)(A - B) = A^2 - AB + BA - B^2 \quad \mathbf{\neq A^2 - B^2}$$

Rumus aljabar biasa hanya berlaku jika matriks $A$ dan $B$ komutatif ($AB = BA$).

---

## 6. Sifat-Sifat Sahih Perkalian Matriks

Jika ukuran matriks memungkinkan untuk dikalikan:
1. **Sifat Asosiatif:**
   $$(A \cdot B) \cdot C = A \cdot (B \cdot C)$$
2. **Sifat Distributif Kiri:**
   $$A(B + C) = AB + AC$$
3. **Sifat Distributif Kanan:**
   $$(A + B)C = AC + BC$$
4. **Identitas Perkalian:**
   $$A \cdot I = I \cdot A = A$$
5. **Perkalian dengan Matriks Nol:**
   $$A \cdot O = O \cdot A = O$$
6. **Hubungan dengan Skalar:**
   $$k(AB) = (kA)B = A(kB)$$

---

## 7. Contoh Soal Berjenjang & Pembahasan Komprehensif 🎯

### Level 1: Operasi Campuran & Persamaan Matriks
**Soal 1:**  
Diketahui $A = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 4 \\ 1 & 2 \end{pmatrix}$, dan $C = \begin{pmatrix} -3 & 2 \\ 5 & 1 \end{pmatrix}$.  
Tentukan hasil dari $2A - B + 3C^T$!

**Pembahasan:**
1. Transpose matriks $C$:
   $$C^T = \begin{pmatrix} -3 & 5 \\ 2 & 1 \end{pmatrix}$$
2. Hitung masing-masing perkalian skalar:
   $$2A = 2 \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ -2 & 6 \end{pmatrix}$$
   $$3C^T = 3 \begin{pmatrix} -3 & 5 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} -9 & 15 \\ 6 & 3 \end{pmatrix}$$
3. Lakukan operasi penjumlahan dan pengurangan:
   $$2A - B + 3C^T = \begin{pmatrix} 4 & 2 \\ -2 & 6 \end{pmatrix} - \begin{pmatrix} 0 & 4 \\ 1 & 2 \end{pmatrix} + \begin{pmatrix} -9 & 15 \\ 6 & 3 \end{pmatrix}$$
   $$= \begin{pmatrix} 4 - 0 + (-9) & 2 - 4 + 15 \\ -2 - 1 + 6 & 6 - 2 + 3 \end{pmatrix} = \begin{pmatrix} -5 & 13 \\ 3 & 7 \end{pmatrix}$$

---

### Level 2: Mencari Pola Pangkat Matriks ($A^n$)
**Soal 2:**  
Diberikan matriks $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$. Tentukan rumus umum untuk $A^n$ untuk sebarang bilangan bulat positif $n$, lalu hitung nilai $A^{100}$!

**Pembahasan:**
Mari kita hitung perpangkatan beberapa suku awal untuk melihat polanya:
* $A^1 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$
* $A^2 = A \cdot A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(1)+2(0) & 1(2)+2(1) \\ 0(1)+1(0) & 0(2)+1(1) \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2(2) \\ 0 & 1 \end{pmatrix}$
* $A^3 = A^2 \cdot A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(1)+4(0) & 1(2)+4(1) \\ 0(1)+1(0) & 0(2)+1(1) \end{pmatrix} = \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2(3) \\ 0 & 1 \end{pmatrix}$

Dari pola di atas, terlihat jelas bahwa elemen baris 1 kolom 2 selalu bertambah kelipatan $2n$:
$$A^n = \begin{pmatrix} 1 & 2n \\ 0 & 1 \end{pmatrix}$$

Maka untuk $n = 100$:
$$A^{100} = \begin{pmatrix} 1 & 2(100) \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 200 \\ 0 & 1 \end{pmatrix}$$

---

### Level 3: Tantangan Aljabar Persamaan Kuadrat Matriks (HOTS)
**Soal 3:**  
Diberikan matriks $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.  
Tunjukkan bahwa matriks $A$ memenuhi persamaan $A^2 - 5A - 2I = O$, kemudian gunakan persamaan tersebut untuk menentukan nilai $A^3$ tanpa mengalikan 3 buah matriks secara langsung!

**Pembahasan:**
1. Hitung $A^2$:
   $$A^2 = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 1(1)+2(3) & 1(2)+2(4) \\ 3(1)+4(3) & 3(2)+4(4) \end{pmatrix} = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$$
2. Hitung $5A + 2I$:
   $$5A = \begin{pmatrix} 5 & 10 \\ 15 & 20 \end{pmatrix}, \quad 2I = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} \implies 5A + 2I = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$$
3. Karena $A^2 = 5A + 2I$, maka:
   $$A^2 - 5A - 2I = O \quad \text{(Terbukti!)}$$
4. Menentukan $A^3$:
   Kalikan persamaan $A^2 = 5A + 2I$ dengan matriks $A$ dari sebelah kiri:
   $$A \cdot A^2 = A(5A + 2I) \implies A^3 = 5A^2 + 2A$$
   Substitusikan kembali $A^2 = 5A + 2I$:
   $$A^3 = 5(5A + 2I) + 2A = 25A + 10I + 2A = 27A + 10I$$
5. Masukkan nilai matriks $A$ dan $I$:
   $$A^3 = 27 \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + 10 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 27 & 54 \\ 81 & 108 \end{pmatrix} + \begin{pmatrix} 10 & 0 \\ 0 & 10 \end{pmatrix} = \begin{pmatrix} 37 & 54 \\ 81 & 118 \end{pmatrix}$$
   *(Teknik ini jauh lebih cepat dan elegan dibandingkan perkalian 3 matriks biasa!).*

---

## 8. Rangkuman Konsep Kunci Modul 2 📌

| Operasi / Sifat | Formula Kunci | Jebakan Umum |
| :--- | :--- | :--- |
| **Penjumlahan** | $(a_{ij} + b_{ij})$ | Wajib ordo sama persis |
| **Perkalian Skalar** | $k \cdot a_{ij}$ | Mengalikan seluruh elemen |
| **Perkalian Matriks** | $A_{m \times p} \cdot B_{p \times n} = C_{m \times n}$ | Baris $\times$ Kolom (BaKo) |
| **Sifat Komutatif** | $AB \neq BA$ | Jangan pernah menukar urutan matriks |
| **Pembagi Nol** | $AB = O \not\implies A=O \lor B=O$ | Matriks bukan nol bisa menghasilkan nol |
| **Hukum Kanselasi** | $AB = AC \not\implies B=C$ | Hanya berlaku jika $\det(A) \neq 0$ |
| **Kuadrat Binomial** | $(A+B)^2 = A^2+AB+BA+B^2$ | Bukan $A^2 + 2AB + B^2$ |

---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | [[Konsep_Dasar_dan_Klasifikasi_Matriks_SMA|⬅️ Modul 1: Konsep & Jenis]] | **Modul 2: Operasi & Sifat** | [[Determinan_Matriks_dan_Sifatnya_SMA|Modul 3: Determinan ➡️]] | [[LKPD Matriks SMA|📝 LKPD]]
