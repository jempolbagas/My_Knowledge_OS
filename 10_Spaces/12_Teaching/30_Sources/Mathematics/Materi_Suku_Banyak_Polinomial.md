---
title: "Materi Ajar Santai: Menaklukkan Suku Banyak (Polinomial) & Metode Horner"
target_audience: "SMA Kelas 11"
created: 2026-07-28
sources:
  - "[[Mempelajari Konsep dan Nilai Suku Banyak (Polinomial)]]"
  - "[[Materi_Kaidah_Pencacahan_dan_Kombinatorika]]"
tags:
  - teaching-material
  - mathematics
  - suku-banyak
  - polinomial
  - metode-horner
---

# Menaklukkan Suku Banyak (Polinomial): Konsep Dasar hingga Metode Horner 🚀

Halo teman-teman! Saat mendengar kata **Polinomial** atau **Suku Banyak**, mungkin pikiranmu langsung terbayang rumus-rumus panjang dengan pangkat tinggi. Tapi tenang saja! Di modul ini, kita akan bedah materi ini dari dasar, memahami konsepnya dengan cara yang santai dan intuitif, serta menguasai **Metode Horner** yang super efisien untuk menyelesaikan soal-soal suku banyak!

---

## 1. Kenalan dengan Suku Banyak (Polinomial)

### Apa sih Suku Banyak itu?
Secara bahasa, **Polinomial** berasal dari kata *Poly* (banyak) dan *Nomial* (suku/nama). 

> **Definisi:**  
> **Suku banyak (Polinomial)** adalah suatu bentuk aljabar yang terdiri dari penjumlahan atau pengurangan suku-suku dengan variabel berpangkat **bilangan bulat positif (tak-negatif)**.

Contoh sederhana dalam kehidupan sehari-hari: ketika kamu merancang volume kotak kardus kemasan, menghitung keuntungan variabel bisnis, atau memodelkan lintasan kurva, kamu sedang menggunakan konsep polinomial!

---

## 2. Anatomi & Bentuk Umum Polinomial

Bentuk umum dari suatu polinomial derajat $n$ dengan satu variabel $x$ dituliskan sebagai berikut:

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + a_{n-2} x^{n-2} + \dots + a_1 x + a_0$$

Mari kita bedah komponen-komponennya:
* **Variabel ($x$):** Simbol atau lambang yang nilainya bisa berubah-ubah.
* **Derajat ($n$):** Pangkat **tertinggi** dari variabel $x$. Syaratnya $n \in \{0, 1, 2, 3, \dots\}$ (bilangan cacah/bulat tak-negatif).
* **Suku Utama ($a_n x^n$):** Suku yang memuat variabel berpangkat tertinggi.
* **Koefisien Utama ($a_n$):** Angka di depan variabel berpangkat tertinggi ($a_n \neq 0$).
* **Koefisien-koefisien ($a_{n-1}, a_{n-2}, \dots, a_1$):** Angka-angka yang menempel di depan variabel $x$.
* **Suku Tetap / Konstanta ($a_0$):** Suku berpangkat nol ($x^0 = 1$), yaitu angka jomblo tanpa variabel $x$.

> **Contoh Cepat:**  
> Diketahui polinomial: $P(x) = 5x^4 - 3x^3 + 2x - 7$
> * **Derajat polinomial:** $4$ (karena pangkat tertinggi $x$ adalah 4).
> * **Koefisien $x^4$ (Koefisien Utama):** $5$
> * **Koefisien $x^3$:** $-3$
> * **Koefisien $x^2$:** $0$ *(suku $x^2$ tidak ditulis, artinya koefisiennya 0!)*
> * **Koefisien $x$:** $2$
> * **Suku Tetap (Konstanta):** $-7$

---

## 3. Aturan & Syarat Bentuk Polinomial

Tidak semua bentuk aljabar disebut polinomial! Ada syarat tegas yang harus dipenuhi:

| Syarat Polinomial | Contoh Polinomial (Boleh ✅) | Contoh Bukan Polinomial (Tidak Boleh ❌) | Alasan |
| :--- | :--- | :--- | :--- |
| **1. Pangkat berupa bilangan bulat $\ge 0$** | $x^3 + 2x^2 - 5$ | $x^{\frac{1}{2}} + 3x$ atau $\sqrt{x} + 2$ | Pangkat berupa pecahan ($\frac{1}{2}$). |
| **2. Variabel tidak berada di penyebut** | $\frac{1}{4}x^2 + 5x$ | $\frac{3}{x} + x^2$ | $\frac{3}{x} = 3x^{-1}$ (pangkat negatif). |
| **3. Jumlah suku harus terbatas** | $x^5 - 2x^3 + 1$ | $1 + x + x^2 + x^3 + \dots$ | Jumlah suku tak terbatas (deret). |
| **4. Variabel tidak dalam fungsi trigonometri/logaritma** | $x^2 \sin(30^\circ) + 4$ | $\sin(x) + x^2$ | Variabel $x$ berada di dalam fungsi trigonometri. |

---

## 4. Menghitung Nilai Polinomial

Misalkan kita punya fungsi polinomial $f(x)$. Nilai polinomial untuk $x = k$ dinotasikan sebagai $f(k)$, yaitu hasil yang diperoleh ketika variabel $x$ diganti dengan nilai $k$.

Ada **2 Metode Utama** untuk menghitung nilai $f(k)$:
1. **Metode Substitusi** (Cara konvensional).
2. **Metode Horner** (Cara cepat & efisien, diciptakan oleh William George Horner).

---

### 4.1 Metode Substitusi
Cara ini dilakukan dengan mengganti langsung setiap variabel $x$ pada polinomial dengan angka $k$.

**Contoh:**  
Hitung nilai $f(x) = 2x^3 - 4x^2 + 3x - 5$ untuk $x = 3$.

**Penyelesaian:**
$$f(3) = 2(3)^3 - 4(3)^2 + 3(3) - 5$$
$$f(3) = 2(27) - 4(9) + 9 - 5$$
$$f(3) = 54 - 36 + 9 - 5 = 22$$

*Kekurangan cara substitusi:* Jika derajat polinomial sangat tinggi (misal $x^6$ atau $x^8$) dan angkanya besar/pecahan, perhitungan manual menjadi sangat panjang dan rawan salah hitung.

---

## 5. Prosedur Lengkap Metode-Metode Horner

Metode Horner adalah teknik algoritma berbasis skema sintetik yang meminimalkan operasi perkalian. Selain untuk menghitung nilai polinomial, Metode Horner juga digunakan untuk **pembagian polinomial**, **menentukan sisa pembagian**, dan **pemfaktoran**.

Berikut adalah prosedur langkah demi langkah dari berbagai variasi Metode Horner!

---

### 5.1 Metode Horner Standar (Evaluasi Nilai $f(k)$)

#### 📋 Prosedur Langkah demi Langkah:
1. **Urutkan Koefisien:** Tuliskan seluruh koefisien polinomial secara mendatar dari pangkat tertinggi hingga pangkat $0$ (konstanta).
   * ⚠️ **Catatan Penting:** Jika ada pangkat yang "loncat" (hilang), tulis koefisiennya dengan angka **$0$**.
2. **Letakkan Pembagi ($k$):** Tulis nilai $x = k$ di sebelah kiri garis vertikal.
3. **Turunkan Koefisien Pertama:** Turunkan koefisien suku pertama ke baris paling bawah (baris hasil) tanpa diubah.
4. **Kalikan & Operasikan secara Diagonal-Vertikal:**
   * Kalikan angka di baris hasil dengan $k$.
   * Tulis hasilnya di baris kedua pada kolom berikutnya.
   * **Jumlahkan** angka baris pertama dan baris kedua pada kolom tersebut.
5. **Ulangi:** Lakukan langkah ini terus menerus sampai kolom paling kanan. Angka paling akhir di pojok kanan bawah adalah **Nilai Polinomial $f(k)$** (atau Sisa Pembagian).

#### 📐 Skema Visual Horner Standar:
Untuk $P(x) = ax^3 + bx^2 + cx + d$ pada $x = k$:

```text
  k  |   a       b           c               d
     |          a*k     (a*k + b)*k     ((a*k + b)*k + c)*k
-----+------------------------------------------------------- (+)
         a    a*k + b   (a*k + b)*k + c |  f(k)  <-- NILAI / SISA
```

#### ✏️ Contoh Soal 1 (Horner Standar):
Hitung nilai $g(x) = 3x^3 + x^2 + 2x - 5$ untuk $x = 4$.

**Penyelesaian:**
* Koefisien dari $x^3, x^2, x^1, x^0$ berturut-turut adalah: **$3, 1, 2, -5$**. Nilai $k = 4$.

```text
  4  |   3     1     2     -5
     |        12    52    216
-----+--------------------------- (+)
         3    13    54  |  211
```

* **Langkah 1:** Turunkan angka $3$.
* **Langkah 2:** $3 \times 4 = 12 \implies 1 + 12 = 13$.
* **Langkah 3:** $13 \times 4 = 52 \implies 2 + 52 = 54$.
* **Langkah 4:** $54 \times 4 = 216 \implies -5 + 216 = 211$.

**Jadi, nilai $g(4) = 211$.** *(Sama persis dengan hasil cara substitusi, tapi jauh lebih cepat!)*

---

### 5.2 Metode Horner untuk Pembagian Polinomial dengan Pembagi $(x - k)$

Ketika $P(x)$ dibagi oleh $(x - k)$, kita bisa menuliskan persamaan pembagian:

$$P(x) = (x - k) \cdot H(x) + S$$

* $H(x)$ = Hasil Bagi (berderajat $n - 1$)
* $S$ = Sisa Pembagian (konstanta $= P(k)$)

#### 📋 Prosedur:
* Gunakan Skema Horner yang sama seperti di atas dengan nilai $k$.
* Baris hasil paling bawah (kecuali angka terakhir) adalah **koefisien-koefisien dari Hasil Bagi $H(x)$**.
* Angka paling kanan di baris bawah adalah **Sisa Pembagian ($S$)**.

#### ✏️ Contoh Soal 2:
Tentukan Hasil Bagi $H(x)$ dan Sisa $S$ jika $P(x) = 2x^4 - 3x^3 + 5x - 8$ dibagi oleh $(x - 2)$.

**Penyelesaian:**
1. Pembagi: $x - 2 = 0 \implies k = 2$.
2. Perhatikan suku $x^2$ tidak ada, jadi koefisiennya $= 0$.
3. Koefisien: **$2, -3, 0, 5, -8$**.

```text
  2  |   2    -3     0     5    -8
     |         4     2     4    18
-----+-------------------------------- (+)
         2     1     2     9  |  10
```

* **Sisa Pembagian ($S$):** $10$
* **Koefisien Hasil Bagi $H(x)$:** Derajat $P(x)$ adalah 4, maka derajat $H(x)$ adalah $4 - 1 = 3$.
  Koefisiennya: $2, 1, 2, 9$
  $$\mathbf{H(x) = 2x^3 + x^2 + 2x + 9}$$

---

### 5.3 Metode Horner untuk Pembagi Bentuk Linear $(ax + b)$

Bagaimana jika pembaginya memiliki koefisien di depan $x$, misalnya $(ax + b)$ atau $(ax - b)$?

#### 📋 Prosedur & Penyesuaian Wajib:
1. Tentukan pembanding: $ax + b = 0 \implies k = -\frac{b}{a}$.
2. Jalankan Skema Horner seperti biasa dengan pembanding $k = -\frac{b}{a}$.
3. Diperoleh koefisien skema $h_{n-1}, h_{n-2}, \dots, h_0$ dan sisa $S$.
4. **ATURAN WAJIB:** Hasil Bagi yang sebenarnya adalah koefisien skema **dibagi dengan $a$**!
   $$H(x) = \frac{H_{\text{skema}}(x)}{a}$$
5. **Sisa Pembagian ($S$):** Tetap angka paling kanan (tidak perlu dibagi $a$).

#### ✏️ Contoh Soal 3:
Tentukan Hasil Bagi dan Sisa dari $P(x) = 3x^3 + 7x^2 - 11x + 4$ dibagi oleh $(3x - 2)$.

**Penyelesaian:**
1. Pembagi $3x - 2 = 0 \implies x = \frac{2}{3}$ (maka $k = \frac{2}{3}$, dengan $a = 3$).
2. Koefisien: **$3, 7, -11, 4$**.

```text
 2/3 |   3     7   -11     4
     |         2     6    -10
-----+--------------------------- (+)
         3     9    -5  | -6
```

* **Sisa Pembagian ($S$):** $-6$
* **Koefisien Skema:** $3, 9, -5$ (derajat 2)
* **Hasil Bagi Sebenarnya $H(x)$:** Bagikan koefisien skema dengan $a = 3$:
  $$H(x) = \frac{3x^2 + 9x - 5}{3} = \mathbf{x^2 + 3x - \frac{5}{3}}$$

---

### 5.4 Metode Horner-Kino (Pembagi Derajat Dua $ax^2 + bx + c$)

**Horner-Kino** adalah modifikasi jenius dari metode Horner yang digunakan untuk pembagi berbentuk kuadrat $ax^2 + bx + c$ **tanpa perlu memfaktorkan** pembagi terlebih dahulu!

#### 📋 Prosedur Langkah demi Langkah:
1. Hitung dua nilai pengali dari pembagi $ax^2 + bx + c$:
   * $k_1 = -\frac{c}{a}$ (Pengali baris 1, untuk suku konstanta)
   * $k_2 = -\frac{b}{a}$ (Pengali baris 2, untuk suku linier)
2. Buat tabel Horner dengan **3 baris operasi**:
   * Baris 1: Koefisien polinomial $P(x)$.
   * Baris 2: Hasil perkalian dengan $k_1$.
   * Baris 3: Hasil perkalian dengan $k_2$.
3. **Pola Pergeseran (Tanda Bintang $*$):**
   * Berikan tanda asteriks/bintang $*$ (kosong) pada:
     * Kolom 1 baris 2 & baris 3.
     * Kolom 2 baris 2.
     * Kolom terakhir baris 3.
4. **Penjumlahan:** Jumlahkan kolom demi kolom dari kiri ke kanan.
5. **Hasil Bagi & Sisa:**
   * $n$ kolom pertama di kiri (setelah dipisah) memberikan koefisien Hasil Bagi $H(x)$, yang kemudian **dibagi dengan $a$**.
   * **2 kolom terakhir di sebelah kanan** adalah sisa pembagian $S(x) = s_1 x + s_0$.

#### 📐 Skema Visual Horner-Kino ($a=1$):

```text
  k1 = -c |   *     *    d1*k1  d2*k1  ...
  k2 = -b |   *   d1*k2  d2*k2  d3*k2  ...
  --------+----------------------------------- (+)
  Koef:      a4     d1     d2     d3  |  s1   s0
          [ --- Hasil Bagi H(x) --- ] [ Sisa S(x) ]
```

#### ✏️ Contoh Soal 4 (Horner-Kino):
Tentukan Hasil Bagi dan Sisa Pembagian dari $P(x) = x^4 - 3x^3 + 5x^2 - 7x + 6$ dibagi oleh $x^2 - 2x + 3$.

**Penyelesaian:**
* Pembagi: $x^2 - 2x + 3 \implies a = 1, b = -2, c = 3$.
* Nilai pengali:
  * $k_1 = -\frac{c}{a} = -\frac{3}{1} = -3$
  * $k_2 = -\frac{b}{a} = -\frac{-2}{1} = 2$
* Koefisien $P(x)$: **$1, -3, 5, -7, 6$** (5 suku).

Tabel Horner-Kino:

```text
 k1 = -3 |   *     *    -3      3     -6
 k2 =  2 |   *     2    -2     -4      *
---------+---------------------------------- (+)
             1    -1      0  | -8      0
```

**Penjelasan Langkah:**
1. Kolom 1: Turunkan $1$.
2. Perkalian: $1 \times k_2 (2) = 2$ di baris $k_2$ kolom 2. $1 \times k_1 (-3) = -3$ di baris $k_1$ kolom 3.
3. Kolom 2: Jumlahkan $-3 + 2 = -1$.
4. Perkalian: $-1 \times k_2 (2) = -2$ di baris $k_2$ kolom 3. $-1 \times k_1 (-3) = 3$ di baris $k_1$ kolom 4.
5. Kolom 3: Jumlahkan $5 + (-3) + (-2) = 0$.
6. Perkalian: $0 \times k_2 (2) = 0$ (di luar/tidak dipakai). $0 \times k_1 (-3) = 0$ di kolom 5.
7. Kolom 4 (Sisa $s_1$): $-7 + 3 + (-4) = -8$.
8. Kolom 5 (Sisa $s_0$): $6 + (-6) + 0 = 0$.

* **Hasil Bagi $H(x)$:** Derajat $4 - 2 = 2$. Koefisien: $1, -1, 0$.
  $$\mathbf{H(x) = x^2 - x}$$
* **Sisa Pembagian $S(x)$:** Koefisien: $-8, 0$.
  $$\mathbf{S(x) = -8x + 0 = -8x}$$

---

## 6. Teorema Sisa dan Teorema Faktor

Metode Horner berhubungan erat dengan dua teorema fundamental polinomial:

### 6.1 Teorema Sisa
1. Jika polinomial $P(x)$ dibagi oleh $(x - k)$, maka sisanya adalah **$S = P(k)$**.
2. Jika $P(x)$ dibagi oleh $(ax + b)$, maka sisanya adalah **$S = P\left(-\frac{b}{a}\right)$**.
3. Jika $P(x)$ dibagi oleh $(x - a)(x - b)$, maka sisa pembagian berpangkat 1: **$S(x) = px + q$**.

### 6.2 Teorema Faktor
> Polinomial $(x - k)$ merupakan **faktor** dari $P(x)$ jika dan hanya jika **Sisa Pembagian $S = P(k) = 0$**.

#### Trik Cepat Mencari Akar-Akar Polinomial:
1. Cari calon pembuat nol $k$ dari faktor-faktor konstanta $a_0$ dibagi faktor-faktor koefisien utama $a_n$.
2. Uji nilai $k$ menggunakan Skema Horner. Jika sisa paling kanan bernilai **$0$**, maka $x = k$ adalah **akar** dan $(x - k)$ adalah **faktor**!

---

## 7. Cheatsheet & Panduan Memilih Metode Horner

| Kasus Pembagian / Evaluasi | Nilai Pembanding ($k$) | Catatan Penyesuaian Hasil Bagi $H(x)$ | Sisa Pembagian ($S$) |
| :--- | :--- | :--- | :--- |
| **Evaluasi Nilai $f(k)$** | $x = k$ | Tidak ada | $f(k) =$ Angka pojok kanan |
| **Pembagi $(x - k)$** | $k$ | $H(x) =$ Koefisien skema | $S =$ Angka pojok kanan |
| **Pembagi $(ax + b)$** | $k = -\frac{b}{a}$ | **$H(x) = \frac{\text{Koefisien skema}}{a}$** | $S =$ Angka pojok kanan |
| **Pembagi Kuadrat $ax^2+bx+c$** | $k_1 = -\frac{c}{a}, k_2 = -\frac{b}{a}$ | **$H(x) = \frac{\text{Koefisien skema}}{a}$** | **$S(x) = s_1 x + s_0$** (2 kolom terakhir) |

---

## 8. Ringkasan Singkat

1. **Polinomial** adalah suku banyak dengan pangkat variabel berupa bilangan bulat non-negatif.
2. Nilai polinomial dapat dicari dengan **Substitusi** atau **Metode Horner**.
3. **Metode Horner Standar** memangkas operasi perkalian dan menghasilkan Hasil Bagi serta Sisa Pembagian sekaligus.
4. Jangan lupa membagi koefisien skema dengan $a$ jika pembagi berbentuk $(ax + b)$ atau $ax^2 + bx + c$.
5. **Horner-Kino** sangat ampuh menyelesaikan pembagian kuadrat tanpa perlu memfaktorkan!

Selamat berlatih! Semakin sering mencoba skema Horner, makin mahir kamu menyelesaikan soal polinomial jenis apa pun! 🎯


---

## 📝 Lembar Kerja & Soal Evaluasi Terkait
- [[LKPD_dan_Soal_Suku_Banyak_Polinomial]]
- [[index_teaching|🍎 Teaching Resources Hub]]
