---
title: "Konsep Dasar, Notasi, dan Klasifikasi Matriks SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 11 (Fase F), Guru Matematika, dan Pembelajar Mandiri"
created: 2026-09-02
sources:
  - "[[Matriks SMA]]"
  - "[[Operasi_Aljabar_dan_Sifat_Matriks_SMA]]"
  - "[[LKPD Matriks SMA]]"
tags:
  - teaching/mathematics
  - mathematics/linear-algebra
  - level/sma
  - topic/matrix-fundamentals
---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | **Modul 1: Konsep & Jenis** | [[Operasi_Aljabar_dan_Sifat_Matriks_SMA|Modul 2: Operasi & Sifat ➡️]] | [[LKPD Matriks SMA|📝 LKPD]]

---

# Konsep Dasar, Notasi, dan Klasifikasi Matriks — Membaca Pola di Balik Larik Angka 🧮📊

Pernahkah kamu berpikir bagaimana komputer memproses gambar digital di layar ponselmu? Atau bagaimana filter kamera di media sosial bisa mendeteksi wajah dan mengubah warna foto secara instan? 

Di balik layar, sebuah gambar digital berukuran $1080 \times 1920$ piksel sebenarnya adalah sebuah **tabel raksasa berisi jutaan angka** yang merepresentasikan intensitas warna merah (*Red*), hijau (*Green*), dan biru (*Blue*). Setiap kali komputer memproses foto, memutar objek 3D di game, atau menjalankan algoritma kecerdasan buatan (*Machine Learning*), ia sedang melakukan manipulasi terhadap struktur data matematis yang disebut **Matriks**.

Matriks adalah bahasa dasar dari aljabar linear. Mari kita pelajari fondasinya dari nol dengan runut, jelas, dan menyeluruh!

---

## 1. Dari Data Tabular ke Bentuk Matriks

### A. Mengapa Kita Butuh Matriks?
Bayangkan kamu sedang mengelola inventaris stok barang di tiga cabang toko sepatu olahraga. Data stok sepatu lari, sepatu basket, dan sepatu kasual di masing-masing cabang dicatat sebagai berikut:

| Cabang Toko | Sepatu Lari (Pasang) | Sepatu Basket (Pasang) | Sepatu Kasual (Pasang) |
| :--- | :---: | :---: | :---: |
| **Cabang 1 (Pusat)** | $25$ | $14$ | $30$ |
| **Cabang 2 (Barat)** | $18$ | $20$ | $15$ |
| **Cabang 3 (Timur)** | $12$ | $8$ | $22$ |

Jika kita membuang label deskriptif teksnya dan hanya mengambil susunan angkanya dengan mempertahankan posisi baris dan kolom, lalu membungkusnya dengan tanda kurung besar, kita mendapatkan bentuk ringkas:

$$A = \begin{pmatrix} 25 & 14 & 30 \\ 18 & 20 & 15 \\ 12 & 8 & 22 \end{pmatrix} \quad \text{atau} \quad A = \begin{bmatrix} 25 & 14 & 30 \\ 18 & 20 & 15 \\ 12 & 8 & 22 \end{bmatrix}$$

Dengan format matriks ini, matematikawan dan sistem komputer dapat melakukan ratusan ribu kalkulasi (penambahan stok, perkalian dengan harga per unit, proyeksi keuntungan) secara serentak (*vectorized calculation*) tanpa harus menghitung satu per satu barang secara terpisah.

---

### B. Definisi Formal Matriks
> [!NOTE]
> **Definisi Matriks:**  
> **Matriks** adalah susunan bilangan, simbol, atau ekspresi matematika yang diatur dalam baris (horizontal) dan kolom (vertikal) sehingga membentuk susunan persegi panjang, dan diletakkan di dalam sepasang tanda kurung biasa $( \dots )$ atau kurung siku $[ \dots ]$.

Bilangan-bilangan yang terdapat di dalam matriks disebut **elemen** atau **entri** matriks.

---

## 2. Anatomi Matriks: Notasi, Ordo, dan Elemen

Untuk membedakan dan mengidentifikasi setiap komponen di dalam matriks secara presisi, kita menggunakan aturan notasi standar internasional:

### A. Notasi Nama dan Elemen
* **Nama Matriks:** Selalu menggunakan **huruf kapital** tebal/tegak, seperti $A, B, C, M, X$.
* **Elemen Matriks:** Ditulis dengan **huruf kecil** yang bersesuaian dengan nama matriksnya, dilengkapi dengan **indeks ganda tersubskrip** $a_{ij}$:
  - Indeks pertama ($i$) menyatakan **nomor baris** tempat elemen berada ($i = 1, 2, \dots, m$).
  - Indeks kedua ($j$) menyatakan **nomor kolom** tempat elemen berada ($j = 1, 2, \dots, n$).

Bentuk umum matriks $A$ yang memiliki $m$ baris dan $n$ kolom adalah:

$$A = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}$$

Secara singkat dinotasikan dengan $A = (a_{ij})_{m \times n}$ atau $A = [a_{ij}]_{m \times n}$.

---

### B. Ordo (Ukuran) Matriks
**Ordo** menyatakan ukuran atau dimensi dari suatu matriks yang ditentukan oleh banyaknya baris ($m$) dan banyaknya kolom ($n$), ditulis dalam format:

$$\text{Ordo } A = m \times n \quad (\text{dibaca: } m \text{ kali } n)$$

> [!WARNING]
> **Awas Tertukar Urutan!**  
> Ordo selalu **Baris lebih dulu baru Kolom** ($m \times n$). Jembatan keledai untuk mengingatnya: **Ba-Ko** (Baris kemudian Kolom) atau **B-K** (Buku Gambar). Matriks berordo $2 \times 3$ **tidak sama** strukturnya dengan matriks berordo $3 \times 2$!

#### Contoh Identifikasi Elemen:
Diberikan matriks $M = \begin{pmatrix} 7 & -3 & 4 & 1 \\ 0 & 9 & -2 & 8 \\ 5 & 6 & 11 & -4 \end{pmatrix}$.
1. Berapa ordo matriks $M$?  
   Matriks $M$ memiliki 3 baris dan 4 kolom, sehingga ordonya adalah $3 \times 4$ (ditulis $M_{3 \times 4}$).
2. Tentukan nilai dari elemen $m_{13}$, $m_{24}$, dan $m_{32}$!
   - $m_{13}$ = elemen baris ke-1 kolom ke-3 $= \mathbf{4}$.
   - $m_{24}$ = elemen baris ke-2 kolom ke-4 $= \mathbf{8}$.
   - $m_{32}$ = elemen baris ke-3 kolom ke-2 $= \mathbf{6}$.
3. Tentukan letak posisi dari elemen bernilai $-2$!  
   Nilai $-2$ berada pada baris ke-2 dan kolom ke-3, sehingga posisinya adalah $m_{23}$.

---

### C. Diagonal Utama, Diagonal Sekunder, dan Trace pada Matriks Persegi
Khusus untuk matriks persegi (di mana jumlah baris sama dengan kolom, $m = n$):

```text
               Diagonal Utama (a_11, a_22, a_33)
                   ↘   
            [  a_11   a_12   a_13  ] 
            [  a_21   a_22   a_23  ] 
            [  a_31   a_32   a_33  ] 
                   ↗
         Diagonal Sekunder / Samping (a_31, a_22, a_13)
```

1. **Diagonal Utama (*Main Diagonal*):** Himpunan elemen $a_{ij}$ di mana $i = j$ (yaitu $a_{11}, a_{22}, \dots, a_{nn}$) yang membentang miring dari pojok kiri-atas ke pojok kanan-bawah.
2. **Diagonal Sekunder (*Anti-Diagonal*):** Himpunan elemen yang membentang miring dari pojok kiri-bawah ke pojok kanan-atas ($i + j = n + 1$).
3. **Trace Matriks ($\operatorname{Tr}(A)$):** Jumlah total dari seluruh elemen pada diagonal utama matriks persegi:
   $$\operatorname{Tr}(A) = \sum_{i=1}^n a_{ii} = a_{11} + a_{22} + \dots + a_{nn}$$

*Contoh:* Jika $A = \begin{pmatrix} 4 & 1 & 7 \\ -2 & 5 & 0 \\ 3 & 8 & -6 \end{pmatrix}$, maka $\operatorname{Tr}(A) = 4 + 5 + (-6) = 3$.

---

## 3. Galeri & Klasifikasi Lengkap Jenis-Jenis Matriks 🏛️

Berdasarkan bentuk ordo, susunan nilainya, serta sifat aljabarnya, matriks dikelompokkan ke dalam beberapa keluarga:

### A. Klasifikasi Berdasarkan Bentuk & Dimensi

1. **Matriks Baris:** Matriks yang hanya terdiri dari **satu baris saja** (berordo $1 \times n$).  
   *Contoh:* $P = \begin{pmatrix} 3 & -1 & 5 & 7 \end{pmatrix}_{1 \times 4}$.
2. **Matriks Kolom:** Matriks yang hanya terdiri dari **satu kolom saja** (berordo $m \times 1$), sering juga disebut *vektor kolom*.  
   *Contoh:* $Q = \begin{pmatrix} 2 \\ -4 \\ 9 \end{pmatrix}_{3 \times 1}$.
3. **Matriks Persegi Panjang:** Matriks di mana jumlah baris tidak sama dengan jumlah kolom ($m \neq n$).
4. **Matriks Persegi (*Square Matrix*):** Matriks di mana jumlah baris sama persis dengan jumlah kolom ($m = n$). Sering disebut matriks berordo $n$.  
   *Contoh:* $R = \begin{pmatrix} 1 & 4 \\ 2 & 5 \end{pmatrix}_{2 \times 2}$.
5. **Matriks Singleton:** Matriks berukuran $1 \times 1$ yang hanya memuat satu elemen tunggal.  
   *Contoh:* $S = [8]_{1 \times 1}$.

---

### B. Klasifikasi Berdasarkan Pola Nilai Elemen

6. **Matriks Nol ($O$ atau $O_{m \times n}$):** Matriks yang **seluruh elemennya bernilai nol** ($a_{ij} = 0$ untuk setiap $i, j$). Berfungsi sebagai elemen netral pada operasi penjumlahan matriks.  
   *Contoh:* $O_{2 \times 3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.

7. **Matriks Diagonal ($D$):** Matriks persegi yang seluruh elemen di luar diagonal utamanya bernilai **nol** ($a_{ij} = 0$ untuk semua $i \neq j$).  
   *Contoh:* $D = \begin{pmatrix} 5 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 7 \end{pmatrix}$.

8. **Matriks Skalar:** Matriks diagonal yang semua elemen pada diagonal utamanya memiliki nilai **konstanta yang sama** ($a_{11} = a_{22} = \dots = a_{nn} = k$ dan $a_{ij} = 0$ untuk $i \neq j$).  
   *Contoh:* $K = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix}$.

9. **Matriks Identitas ($I$ atau $I_n$):** Matriks skalar yang semua elemen diagonal utamanya bernilai **satu** ($k = 1$).  
   Elemennya dapat didefinisikan dengan fungsi Delta Kronecker ($\delta_{ij}$):
   $$\delta_{ij} = \begin{cases} 1, & \text{jika } i = j \\ 0, & \text{jika } i \neq j \end{cases}$$
   *Contoh:* $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.  
   *(Catatan: Matriks identitas bertindak seperti angka 1 dalam perkalian bilangan real, yaitu $A \cdot I = I \cdot A = A$).*

10. **Matriks Segitiga Atas (*Upper Triangular Matrix*):** Matriks persegi yang semua elemen di **bawah diagonal utama** bernilai nol ($a_{ij} = 0$ untuk setiap $i > j$).  
    *Contoh:* $U = \begin{pmatrix} 3 & 8 & 2 \\ 0 & -1 & 5 \\ 0 & 0 & 4 \end{pmatrix}$.

11. **Matriks Segitiga Bawah (*Lower Triangular Matrix*):** Matriks persegi yang semua elemen di **atas diagonal utama** bernilai nol ($a_{ij} = 0$ untuk setiap $i < j$).  
    *Contoh:* $L = \begin{pmatrix} 2 & 0 & 0 \\ 6 & 7 & 0 \\ -3 & 1 & 9 \end{pmatrix}$.

---

### C. Klasifikasi Berdasarkan Sifat Transpose & Perkalian Khusus

12. **Matriks Simetris:** Matriks persegi yang bernilai **identik dengan hasil transposenya** ($A^T = A$).  
    Syarat elemen: $a_{ij} = a_{ji}$ untuk setiap pasangan indeks $i, j$.
    *Contoh:* $A = \begin{pmatrix} 1 & 2 & 4 \\ 2 & 3 & -5 \\ 4 & -5 & 6 \end{pmatrix}$. (Perhatikan bahwa elemen di seberang diagonal utama saling bercermin sama persis!).

13. **Matriks Skew-Simetris (*Antisymmetric Matrix*):** Matriks persegi yang hasil transposenya bernilai **negatif dari dirinya sendiri** ($A^T = -A$).  
    Syarat elemen: $a_{ij} = -a_{ji}$ untuk setiap $i, j$.
    
> [!IMPORTANT]
    > **Bukti Analitis Mengapa Diagonal Utama Matriks Skew-Simetris Selalu 0:**  
    > Pada diagonal utama, nilai indeks baris dan kolom adalah sama ($i = j$).  
    > Berdasarkan syarat $a_{ij} = -a_{ji}$, maka untuk diagonal utama berlaku:  
    > $$a_{ii} = -a_{ii} \implies a_{ii} + a_{ii} = 0 \implies 2a_{ii} = 0 \implies a_{ii} = 0$$  
    > Oleh karena itu, semua elemen pada diagonal utama matriks skew-simetris **wajib bernilai 0**!
    
    *Contoh:* $B = \begin{pmatrix} 0 & 3 & -5 \\ -3 & 0 & 2 \\ 5 & -2 & 0 \end{pmatrix}$.

14. **Matriks Ortogonal:** Matriks persegi yang transposenya sama dengan inversnya ($A^T = A^{-1} \iff A \cdot A^T = A^T \cdot A = I$).
15. **Matriks Idempoten:** Matriks persegi yang jika dikalikan dengan dirinya sendiri menghasilkan matriks aslinya ($A^2 = A$).
16. **Matriks Involutori:** Matriks persegi yang jika dikuadratkan menghasilkan matriks identitas ($A^2 = I \iff A^{-1} = A$).
17. **Matriks Nilpoten:** Matriks persegi yang jika dipangkatkan suatu bilangan bulat positif $k$ menghasilkan matriks nol ($A^k = O$). Nilai $k$ terkecil disebut *indeks nilpotensi*.

---

## 4. Transpose Matriks ($A^T$)

### A. Definisi dan Mekanisme Transpose
**Transpose matriks** adalah operasi mengubah susunan matriks dengan cara **menukar baris menjadi kolom** dan **kolom menjadi baris**. Transpose dari matriks $A$ dinotasikan dengan $A^T, A^t,$ atau $A'$.

Secara formal, jika $A = (a_{ij})_{m \times n}$, maka transpose dari $A$ adalah:

$$A^T = (b_{ji})_{n \times m} \quad \text{di mana } b_{ji} = a_{ij}$$

* **Perubahan Dimensi:** Jika matriks $A$ berordo $m \times n$, maka matriks $A^T$ akan berordo $n \times m$.

#### Visualisasi Transpose:
```text
Matriks A (2x3):             Matriks A^T (3x2):
[  2   4   1  ]  --- Baris 1 --->  [  2   5  ]  <-- Kolom 1
[  5   0   3  ]  --- Baris 2 --->  [  4   0  ]  <-- Kolom 2
                                    [  1   3  ]  <-- Kolom 3
```

---

### B. Teorema dan Sifat-Sifat Transpose Matriks

Misalkan $A$ dan $B$ adalah matriks-matriks yang memiliki ukuran yang bersesuaian, dan $k$ adalah suatu skalar konstan real:

1. **Involusi Transpose:**
   $$(A^T)^T = A$$
   *(Jika ditranspose dua kali, matriks kembali ke bentuk semula).*

2. **Linearitas Penjumlahan:**
   $$(A + B)^T = A^T + B^T \quad \text{dan} \quad (A - B)^T = A^T - B^T$$

3. **Perkalian dengan Skalar:**
   $$(k \cdot A)^T = k \cdot A^T$$

4. **Sifat Pembalikan Perkalian (*Reversal Property*):**
   $$(A \cdot B)^T = B^T \cdot A^T$$

> [!WARNING]
> **Awas Sifat $(AB)^T$!**  
> Urutan perkalian **harus dibalik**: $(AB)^T = B^T A^T$, **bukan** $A^T B^T$!  
> *Alasan dimensi:* Jika $A_{2 \times 3}$ dan $B_{3 \times 4}$, maka $(AB)$ berordo $2 \times 4$, sehingga $(AB)^T$ berordo $4 \times 2$.  
> Jika kita menghitung $A^T B^T$, ordonya adalah $(3 \times 2) \times (4 \times 3)$ yang bahkan **tidak bisa dikalikan** karena jumlah kolom matriks pertama ($2$) tidak sama dengan jumlah baris matriks kedua ($4$). Sebaliknya, $B^T_{4 \times 3} \times A^T_{3 \times 2}$ terdefinisi sempurna dan menghasilkan ordo $4 \times 2$.

---

## 5. Kesamaan Dua Matriks (*Equality of Matrices*)

Dua buah matriks $A$ dan $B$ dikatakan **sama persis** ($A = B$) jika dan hanya jika memenuhi **dua syarat mutlak**:
1. **Ordo matriks sama:** Matriks $A$ dan matriks $B$ memiliki dimensi ukuran yang identik ($m_A = m_B$ dan $n_A = n_B$).
2. **Setiap elemen seletak bernilai sama:** $a_{ij} = b_{ij}$ untuk semua nilai $i$ dan $j$.

Prinsip kesamaan matriks ini sangat sering digunakan dalam soal-soal aljabar untuk menyusun sistem persamaan dan menemukan nilai variabel yang belum diketahui.

---

## 6. Contoh Soal Berjenjang & Pembahasan Komprehensif 🎯

### Level 1: Fondasi Konsep & Transpose
**Soal 1:**  
Diketahui matriks $P = \begin{pmatrix} 2x & 4 \\ 3 & x+2y \end{pmatrix}$ dan $Q = \begin{pmatrix} 8 & 3 \\ 4 & -1 \end{pmatrix}$. Jika berlaku $P = Q^T$, tentukan nilai dari $x \cdot y$!

**Pembahasan Langkah demi Langkah:**
1. Pertama, tentukan hasil transpose matriks $Q$ ($Q^T$):
   $$Q = \begin{pmatrix} 8 & 3 \\ 4 & -1 \end{pmatrix} \implies Q^T = \begin{pmatrix} 8 & 4 \\ 3 & -1 \end{pmatrix}$$
2. Terapkan prinsip kesamaan matriks $P = Q^T$:
   $$\begin{pmatrix} 2x & 4 \\ 3 & x+2y \end{pmatrix} = \begin{pmatrix} 8 & 4 \\ 3 & -1 \end{pmatrix}$$
3. Samakan elemen-elemen yang seletak:
   * Elemen baris 1 kolom 1:
     $$2x = 8 \implies x = \frac{8}{2} = 4$$
   * Elemen baris 2 kolom 2:
     $$x + 2y = -1$$
     Substitusikan nilai $x = 4$:
     $$4 + 2y = -1 \implies 2y = -1 - 4 \implies 2y = -5 \implies y = -\frac{5}{2}$$
4. Hitung nilai $x \cdot y$:
   $$x \cdot y = 4 \cdot \left(-\frac{5}{2}\right) = -10$$
   *Jawaban:* Nilai dari $x \cdot y$ adalah **$-10$**.

---

### Level 2: Karakteristik Matriks Simetris & Trace
**Soal 2:**  
Diberikan matriks $A = \begin{pmatrix} 2 & a+b & 4 \\ 5 & 3 & c-1 \\ 2b & 7 & -1 \end{pmatrix}$. Jika matriks $A$ diketahui merupakan **matriks simetris**, tentukan:
a. Nilai $a, b,$ dan $c$.  
b. Nilai $\operatorname{Tr}(A)$.

**Pembahasan:**
1. Karena matriks $A$ simetris, maka berlaku $A = A^T$, yang berarti setiap elemen seberang diagonal utama harus sama ($a_{ij} = a_{ji}$):
   * Elemen posisi $(1,3)$ dan $(3,1)$:
     $$a_{13} = a_{31} \implies 4 = 2b \implies b = 2$$
   * Elemen posisi $(1,2)$ dan $(2,1)$:
     $$a_{12} = a_{21} \implies a + b = 5$$
     Substitusikan $b = 2$:
     $$a + 2 = 5 \implies a = 3$$
   * Elemen posisi $(2,3)$ dan $(3,2)$:
     $$a_{23} = a_{32} \implies c - 1 = 7 \implies c = 8$$
   Jadi, diperoleh $a = 3, b = 2,$ dan $c = 8$.

2. Menghitung Trace $\operatorname{Tr}(A)$:
   $$\operatorname{Tr}(A) = a_{11} + a_{22} + a_{33} = 2 + 3 + (-1) = \mathbf{4}$$

---

### Level 3: Tantangan Penalaran HOTS
**Soal 3:**  
Buktikan bahwa untuk sebarang matriks persegi $M$, matriks $S = M + M^T$ **selalu merupakan matriks simetris**, sedangkan matriks $K = M - M^T$ **selalu merupakan matriks skew-simetris**!

**Pembuktian Analitis:**
1. **Membuktikan $S = M + M^T$ adalah simetris:**  
   Suatu matriks $S$ disebut simetris jika $S^T = S$.  
   Ambil transpose dari kedua ruas:
   $$S^T = (M + M^T)^T$$
   Gunakan sifat linearitas transpose $(A+B)^T = A^T + B^T$:
   $$S^T = M^T + (M^T)^T$$
   Gunakan sifat involusi $(M^T)^T = M$:
   $$S^T = M^T + M$$
   Karena penjumlahan matriks bersifat komutatif ($M^T + M = M + M^T$):
   $$S^T = M + M^T = S$$
   *Terbukti bahwa $S = M + M^T$ selalu simetris.*

2. **Membuktikan $K = M - M^T$ adalah skew-simetris:**  
   Suatu matriks $K$ disebut skew-simetris jika $K^T = -K$.  
   Ambil transpose dari kedua ruas:
   $$K^T = (M - M^T)^T = M^T - (M^T)^T = M^T - M$$
   Faktorkan tanda negatif keluar:
   $$K^T = -(M - M^T) = -K$$
   *Terbukti bahwa $K = M - M^T$ selalu skew-simetris.*

*(Konsekuensi penting: Setiap matriks persegi $M$ dapat selalu diuraikan menjadi penjumlahan matriks simetris dan skew-simetris, yaitu $M = \frac{1}{2}(M + M^T) + \frac{1}{2}(M - M^T)$).*

---

## 7. Rangkuman Konsep Kunci Modul 1 📌

| Istilah / Sifat | Formula / Definisi | Catatan Krusial |
| :--- | :--- | :--- |
| **Ordo Matriks** | $m \times n$ ($m$ baris, $n$ kolom) | Selalu sebut Baris lebih dulu baru Kolom |
| **Elemen Matriks** | $a_{ij}$ | $i = \text{baris}, j = \text{kolom}$ |
| **Trace** | $\operatorname{Tr}(A) = \sum a_{ii}$ | Hanya terdefinisi pada matriks persegi |
| **Identitas ($I$)** | $I \cdot A = A \cdot I = A$ | Diagonal utama bernilai 1, lainnya 0 |
| **Simetris** | $A^T = A$ ($a_{ij} = a_{ji}$) | Cermin diagonal utama identik |
| **Skew-Simetris** | $A^T = -A$ ($a_{ij} = -a_{ji}$) | Diagonal utama **wajib bernilai 0** |
| **Transpose** | Baris $\leftrightarrow$ Kolom | Sifat kunci: $(AB)^T = B^T A^T$ |

---

> **Bilah Navigasi:**  
> [[Matriks SMA|🏠 Master Dashboard]] | **Modul 1: Konsep & Jenis** | [[Operasi_Aljabar_dan_Sifat_Matriks_SMA|Modul 2: Operasi & Sifat ➡️]] | [[LKPD Matriks SMA|📝 LKPD]]
