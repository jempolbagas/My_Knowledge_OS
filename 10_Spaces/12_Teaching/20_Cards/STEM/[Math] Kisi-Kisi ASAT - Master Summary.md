---
title: "Kisi-Kisi ASAT Matematika — Master Summary"
course: ""
tags: ["Matematika", "ASAT", "PersamaanKuadrat", "SPLDV", "SPLTV", "Pertidaksamaan", "Statistika"]
aliases: ["Kisi-Kisi ASAT Matematika — Master Summary"]
created: "2026-06-03"
subject: Matematika
class: SMA
topic: "Kisi-Kisi ASAT"
up: "[[Matematika ASAT MOC]]"
---

# 📐 Kisi-Kisi ASAT Matematika — Master Summary

> [!info] Daftar Topik
> 1. Menentukan akar-akar persamaan kuadrat
> 2. Menentukan jumlah dan hasil kali akar
> 3. Menentukan persamaan kuadrat baru
> 4. Menentukan HP dari SPLDV dan SPLTV
> 5. Menentukan hasil SPLDV & SPLTV soal cerita
> 6. Menentukan DHP dari pertidaksamaan linier
> 7. Menentukan pertidaksamaan linier dari DHP
> 8. Menentukan rata-rata data tunggal dan rata-rata gabungan
> 9. Menentukan ukuran pemusatan data (data tunggal dan kelompok)
> 10. Menentukan ukuran penempatan data (data tunggal dan kelompok)
> 11. Menentukan ukuran penyebaran data (data tunggal dan kelompok)

> [!tip] Cara Menggunakan Catatan Ini
> Catatan ini merangkum **seluruh materi** kisi-kisi ASAT Matematika dalam satu dokumen. Setiap topik disusun dengan **rumus**, **langkah pengerjaan**, **contoh soal**, dan **tips ujian**. Gunakan sebagai panduan belajar terpadu sebelum ASAT.

---
---

# BAGIAN A — PERSAMAAN KUADRAT

---

## 1. Menentukan Akar-Akar Persamaan Kuadrat

### 1.1 Bentuk Umum

> [!quote] Definisi
> **Persamaan kuadrat** adalah persamaan polinomial berderajat dua, dengan bentuk umum:
> $$ax^2 + bx + c = 0, \quad a \neq 0$$

### 1.2 Tiga Metode Penyelesaian

#### A. Memfaktorkan

Langkah:
1. Cari dua bilangan yang jika **dikalikan** hasilnya = $a \times c$ dan jika **dijumlahkan** hasilnya = $b$
2. Uraikan persamaan ke bentuk $(px + q)(rx + s) = 0$
3. Gunakan sifat: jika $A \times B = 0$ maka $A = 0$ atau $B = 0$

> **Contoh:**
> $x^2 - 5x + 6 = 0$
>
> Cari dua bilangan: $(\cdot) = 6$ dan $(+) = -5$ → yaitu $-2$ dan $-3$
>
> $(x - 2)(x - 3) = 0$
>
> $x_1 = 2$ atau $x_2 = 3$

#### B. Melengkapkan Kuadrat Sempurna

Langkah:
1. Pastikan koefisien $a = 1$ (jika belum, bagi semua ruas)
2. Pindahkan konstanta $c$ ke ruas kanan
3. Tambahkan $\left(\frac{b}{2}\right)^2$ di kedua ruas
4. Faktorkan ruas kiri menjadi bentuk kuadrat sempurna
5. Tarik akar kuadrat kedua ruas

> **Contoh:**
> $x^2 + 6x + 5 = 0$
>
> $x^2 + 6x = -5$
>
> $x^2 + 6x + 9 = -5 + 9$
>
> $(x + 3)^2 = 4$
>
> $x + 3 = \pm 2$
>
> $x_1 = -1$ atau $x_2 = -5$

#### C. Rumus ABC (Kuadratik)

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

> **Contoh:**
> $2x^2 + 3x - 2 = 0$, dengan $a=2$, $b=3$, $c=-2$
>
> $D = b^2 - 4ac = 9 - 4(2)(-2) = 9 + 16 = 25$
>
> $x = \frac{-3 \pm \sqrt{25}}{4} = \frac{-3 \pm 5}{4}$
>
> $x_1 = \frac{-3+5}{4} = \frac{1}{2}$ atau $x_2 = \frac{-3-5}{4} = -2$

### 1.3 Diskriminan ($D$)

$$D = b^2 - 4ac$$

| Nilai $D$ | Jenis Akar | Keterangan |
|:---------:|:-----------|:-----------|
| $D > 0$ | Dua akar **real berbeda** | Parabola memotong sumbu-$x$ di 2 titik |
| $D = 0$ | Dua akar **real sama** (kembar) | Parabola menyinggung sumbu-$x$ |
| $D < 0$ | **Tidak ada** akar real | Parabola tidak memotong sumbu-$x$ |

> [!tip] Tips Ujian
> - Jika soal minta **memfaktorkan**, cari pasangan bilangan yang tepat dulu.
> - Jika bilangan sulit difaktorkan, langsung pakai **rumus ABC**.
> - Selalu cek: apakah $a \neq 0$.

---

## 2. Jumlah dan Hasil Kali Akar (Rumus Vieta)

### 2.1 Rumus Vieta

Jika $x_1$ dan $x_2$ adalah akar-akar dari $ax^2 + bx + c = 0$, maka:

$$x_1 + x_2 = -\frac{b}{a}$$

$$x_1 \cdot x_2 = \frac{c}{a}$$

### 2.2 Hubungan Turunan yang Sering Muncul

| Bentuk | Rumus |
|--------|-------|
| $x_1^2 + x_2^2$ | $(x_1 + x_2)^2 - 2x_1 x_2$ |
| $(x_1 - x_2)^2$ | $(x_1 + x_2)^2 - 4x_1 x_2$ |
| $\frac{1}{x_1} + \frac{1}{x_2}$ | $\frac{x_1 + x_2}{x_1 \cdot x_2}$ |
| $x_1^3 + x_2^3$ | $(x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2)$ |
| $\frac{x_1}{x_2} + \frac{x_2}{x_1}$ | $\frac{x_1^2 + x_2^2}{x_1 \cdot x_2}$ |

> **Contoh:**
> Diketahui persamaan $x^2 - 7x + 12 = 0$. Tentukan $x_1^2 + x_2^2$.
>
> $x_1 + x_2 = 7$, $\quad x_1 \cdot x_2 = 12$
>
> $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = 49 - 24 = 25$

> [!tip] Tips Ujian
> Kamu **tidak perlu** mencari akar satu per satu! Gunakan langsung rumus Vieta dan hubungan turunan di atas.

---

## 3. Menentukan Persamaan Kuadrat Baru

### 3.1 Metode: Dari Akar-Akar yang Diketahui

Jika akar-akar baru adalah $p$ dan $q$, maka persamaan kuadrat baru:

$$x^2 - (p + q)x + (p \cdot q) = 0$$

### 3.2 Langkah Pengerjaan

1. Identifikasi akar-akar baru (biasanya dinyatakan dalam $x_1$ dan $x_2$)
2. Hitung **jumlah akar baru** $(p + q)$ menggunakan rumus Vieta dari persamaan asal
3. Hitung **hasil kali akar baru** $(p \cdot q)$ menggunakan rumus Vieta
4. Substitusikan ke bentuk $x^2 - (p+q)x + pq = 0$

### 3.3 Tipe-Tipe Soal yang Sering Muncul

| Akar Baru | $p + q$ | $p \cdot q$ |
|-----------|---------|------------|
| $x_1 + 1$ dan $x_2 + 1$ | $(x_1+x_2) + 2$ | $x_1 x_2 + (x_1+x_2) + 1$ |
| $x_1^2$ dan $x_2^2$ | $(x_1+x_2)^2 - 2x_1 x_2$ | $(x_1 x_2)^2$ |
| $\frac{1}{x_1}$ dan $\frac{1}{x_2}$ | $\frac{x_1+x_2}{x_1 x_2}$ | $\frac{1}{x_1 x_2}$ |
| $2x_1$ dan $2x_2$ | $2(x_1+x_2)$ | $4 x_1 x_2$ |
| $x_1 + x_2$ dan $x_1 \cdot x_2$ | $(x_1+x_2) + x_1 x_2$ | $(x_1+x_2) \cdot x_1 x_2$ |

> **Contoh:**
> Persamaan $x^2 - 5x + 6 = 0$ memiliki akar $x_1$ dan $x_2$. Tentukan persamaan kuadrat baru yang akar-akarnya $\frac{1}{x_1}$ dan $\frac{1}{x_2}$.
>
> Dari Vieta: $x_1 + x_2 = 5$, $\quad x_1 x_2 = 6$
>
> Jumlah akar baru: $\frac{1}{x_1} + \frac{1}{x_2} = \frac{x_1+x_2}{x_1 x_2} = \frac{5}{6}$
>
> Hasil kali akar baru: $\frac{1}{x_1} \cdot \frac{1}{x_2} = \frac{1}{x_1 x_2} = \frac{1}{6}$
>
> PK baru: $x^2 - \frac{5}{6}x + \frac{1}{6} = 0$ → kalikan 6 → $6x^2 - 5x + 1 = 0$

> [!warning] Kesalahan Umum
> Jangan lupa **menghilangkan pecahan** di akhir dengan mengalikan seluruh persamaan dengan penyebut.

---
---

# BAGIAN B — SISTEM PERSAMAAN LINEAR

---

## 4. Himpunan Penyelesaian SPLDV dan SPLTV

### 4.1 SPLDV (Sistem Persamaan Linear Dua Variabel)

> [!quote] Definisi
> **SPLDV** adalah sistem yang terdiri dari dua persamaan linear dengan **dua variabel** ($x$ dan $y$).
> $$\begin{cases} a_1x + b_1y = c_1 \\ a_2x + b_2y = c_2 \end{cases}$$

#### Metode Penyelesaian SPLDV

**A. Substitusi**
1. Nyatakan salah satu variabel dari satu persamaan
2. Substitusikan ke persamaan lain
3. Selesaikan variabel yang tersisa
4. Substitusikan kembali untuk menemukan variabel lainnya

**B. Eliminasi**
1. Samakan koefisien salah satu variabel
2. Kurangkan/jumlahkan kedua persamaan untuk menghilangkan variabel tersebut
3. Selesaikan variabel yang tersisa
4. Substitusikan untuk menemukan variabel lainnya

**C. Campuran (Eliminasi-Substitusi)**
Gabungan metode eliminasi dan substitusi — paling umum dipakai.

> **Contoh:**
> $$\begin{cases} 2x + 3y = 12 \\ x - y = 1 \end{cases}$$
>
> **Eliminasi:** Dari pers. 2: $x = y + 1$
>
> **Substitusi** ke pers. 1: $2(y+1) + 3y = 12$
>
> $2y + 2 + 3y = 12 \Rightarrow 5y = 10 \Rightarrow y = 2$
>
> $x = 2 + 1 = 3$
>
> **HP = $\{(3, 2)\}$**

### 4.2 SPLTV (Sistem Persamaan Linear Tiga Variabel)

> [!quote] Definisi
> **SPLTV** adalah sistem yang terdiri dari tiga persamaan linear dengan **tiga variabel** ($x$, $y$, $z$).
> $$\begin{cases} a_1x + b_1y + c_1z = d_1 \\ a_2x + b_2y + c_2z = d_2 \\ a_3x + b_3y + c_3z = d_3 \end{cases}$$

#### Langkah Penyelesaian SPLTV

1. **Pilih dua pasang persamaan**, eliminasi satu variabel yang sama → dapat **dua persamaan baru** (SPLDV)
2. Selesaikan SPLDV tersebut
3. **Substitusikan** kembali untuk menemukan variabel ketiga

> **Contoh:**
> $$\begin{cases} x + y + z = 6 \quad \cdots (1) \\ 2x - y + z = 3 \quad \cdots (2) \\ x + 2y - z = 5 \quad \cdots (3) \end{cases}$$
>
> Pers. $(1) + (3)$: $2x + 3y = 11 \quad \cdots (4)$
>
> Pers. $(2) + (3)$: $3x + y = 8 \quad \cdots (5)$
>
> Dari $(5)$: $y = 8 - 3x$, substitusi ke $(4)$:
>
> $2x + 3(8 - 3x) = 11 \Rightarrow 2x + 24 - 9x = 11 \Rightarrow -7x = -13 \Rightarrow x = \frac{13}{7}$
>
> Lanjutkan: $y = 8 - 3 \cdot \frac{13}{7} = \frac{56 - 39}{7} = \frac{17}{7}$
>
> $z = 6 - x - y = 6 - \frac{13}{7} - \frac{17}{7} = \frac{42 - 13 - 17}{7} = \frac{12}{7}$

> [!tip] Tips Ujian
> - Pilih variabel yang **paling mudah** dieliminasi (koefisien sudah sama atau 1).
> - Beri **nomor** pada setiap persamaan agar tidak bingung.
> - Selalu **cek jawaban** dengan substitusi ke ketiga persamaan asal.

---

## 5. SPLDV & SPLTV — Soal Cerita

### 5.1 Langkah Mengubah Soal Cerita ke Bentuk Matematika

1. **Baca** soal dan identifikasi **variabel** (apa yang dicari?)
2. **Misalkan** variabel: $x$ = …, $y$ = …, $z$ = …
3. **Buat model** persamaan dari informasi yang diberikan
4. **Selesaikan** SPLDV/SPLTV
5. **Jawab** sesuai konteks soal (sertakan satuan!)

### 5.2 Contoh Soal Cerita SPLDV

> Harga 3 buku dan 2 pensil adalah Rp21.000. Harga 1 buku dan 4 pensil adalah Rp17.000. Tentukan harga 1 buku dan 1 pensil.
>
> **Misalkan:** $x$ = harga 1 buku, $y$ = harga 1 pensil
>
> $$\begin{cases} 3x + 2y = 21.000 \\ x + 4y = 17.000 \end{cases}$$
>
> Dari pers. 2: $x = 17.000 - 4y$
>
> Substitusi: $3(17.000 - 4y) + 2y = 21.000$
>
> $51.000 - 12y + 2y = 21.000 \Rightarrow -10y = -30.000 \Rightarrow y = 3.000$
>
> $x = 17.000 - 4(3.000) = 5.000$
>
> **Harga 1 buku = Rp5.000, 1 pensil = Rp3.000**

### 5.3 Contoh Soal Cerita SPLTV

> Ani, Budi, dan Citra membeli alat tulis. Ani membeli 2 buku, 1 pensil, dan 1 penghapus seharga Rp15.000. Budi membeli 1 buku, 3 pensil, dan 2 penghapus seharga Rp19.000. Citra membeli 3 buku, 2 pensil, dan 1 penghapus seharga Rp21.000. Tentukan harga masing-masing.
>
> **Misalkan:** $x$ = buku, $y$ = pensil, $z$ = penghapus
>
> $$\begin{cases} 2x + y + z = 15.000 \quad \cdots (1) \\ x + 3y + 2z = 19.000 \quad \cdots (2) \\ 3x + 2y + z = 21.000 \quad \cdots (3) \end{cases}$$
>
> Pers. $(1) - (3)$: $-x - y = -6.000 \Rightarrow x + y = 6.000 \quad \cdots (4)$
>
> Pers. $(1) \times 2 - (2)$: $4x + 2y + 2z - x - 3y - 2z = 30.000 - 19.000$
>
> $3x - y = 11.000 \quad \cdots (5)$
>
> Dari $(4) + (5)$: $4x = 17.000 \Rightarrow x = 4.250$
>
> $y = 6.000 - 4.250 = 1.750$
>
> $z = 15.000 - 2(4.250) - 1.750 = 4.750$

> [!warning] Kesalahan Umum pada Soal Cerita
> - Lupa **mendefinisikan variabel** dengan jelas
> - Salah menyusun persamaan (keliru menempatkan koefisien)
> - Lupa memberikan **satuan** pada jawaban akhir
> - Tidak **mengecek** jawaban ke persamaan asal

---
---

# BAGIAN C — PERTIDAKSAMAAN LINEAR

---

## 6. Menentukan DHP dari Pertidaksamaan Linear

### 6.1 Pengertian

> [!quote] Definisi
> **Daerah Himpunan Penyelesaian (DHP)** adalah daerah pada bidang koordinat yang memenuhi **semua** pertidaksamaan linear dalam suatu sistem.

### 6.2 Langkah Menentukan DHP

1. **Ubah** tanda pertidaksamaan menjadi tanda **sama dengan** → gambar garisnya
2. **Tentukan jenis garis:**
   - $\leq$ atau $\geq$ → garis **utuh** (solid)
   - $<$ atau $>$ → garis **putus-putus** (dashed)
3. **Uji titik** (biasanya $(0,0)$ jika tidak dilalui garis):
   - Jika memenuhi → arsir sisi yang mengandung titik uji
   - Jika tidak → arsir sisi sebaliknya
4. **DHP** = irisan (bagian yang diarsir oleh **semua** pertidaksamaan)

### 6.3 Contoh

> Tentukan DHP dari:
> $$\begin{cases} x + y \leq 6 \\ 2x + y \geq 4 \\ x \geq 0, \; y \geq 0 \end{cases}$$
>
> 1. Gambar garis $x + y = 6$ (potong sumbu di $(6,0)$ dan $(0,6)$) — garis utuh
> 2. Gambar garis $2x + y = 4$ (potong sumbu di $(2,0)$ dan $(0,4)$) — garis utuh
> 3. Batasan $x \geq 0$ dan $y \geq 0$ → kuadran I
> 4. Uji $(0,0)$:
>    - $0 + 0 \leq 6$ → ✅ (arsir sisi asal)
>    - $2(0) + 0 \geq 4$ → ❌ (arsir sisi **sebaliknya** dari asal)
> 5. DHP = daerah irisan di kuadran I

> [!tip] Tips Ujian
> - Selalu mulai dari **syarat non-negatif** ($x \geq 0$, $y \geq 0$) untuk membatasi kuadran I.
> - Gunakan **titik uji** $(0,0)$ kecuali garis melewati titik asal — dalam kasus itu gunakan titik lain seperti $(1,0)$.

---

## 7. Menentukan Pertidaksamaan Linear dari DHP (Kebalikan)

### 7.1 Langkah

1. **Identifikasi** garis-garis batas pada grafik DHP
2. **Tentukan persamaan garis** masing-masing ($y = mx + n$ atau $ax + by = c$)
3. **Tentukan tanda pertidaksamaan:**
   - Garis utuh → $\leq$ atau $\geq$
   - Garis putus-putus → $<$ atau $>$
   - Ambil titik di daerah arsiran, substitusi → tentukan arah tanda
4. **Tuliskan** sistem pertidaksamaan

### 7.2 Cara Menentukan Persamaan Garis dari Grafik

| Informasi | Rumus |
|-----------|-------|
| Melalui $(x_1, y_1)$ dan $(x_2, y_2)$ | $\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$ |
| Memotong sumbu-$x$ di $(a, 0)$ dan sumbu-$y$ di $(0, b)$ | $\frac{x}{a} + \frac{y}{b} = 1$ |
| Gradien $m$, melalui $(x_1, y_1)$ | $y - y_1 = m(x - x_1)$ |

> **Contoh:**
> Dari grafik, diketahui DHP dibatasi oleh:
> - Garis utuh melalui $(4,0)$ dan $(0,6)$ → arsiran ke bawah garis
> - Garis utuh melalui $(0,0)$ dan $(3,3)$ → arsiran ke kanan garis
>
> Garis 1: $\frac{x}{4} + \frac{y}{6} = 1 \Rightarrow 3x + 2y = 12$
>
> Uji titik $(0,0)$: $0 \leq 12$ ✅ → DHP di sisi asal → $3x + 2y \leq 12$
>
> Garis 2: $y = x$ → Uji $(2,0)$: $0 \leq 2$ → $y \leq x$ atau $x - y \geq 0$

---
---

# BAGIAN D — STATISTIKA

---

## 8. Rata-Rata Data Tunggal dan Rata-Rata Gabungan

### 8.1 Rata-Rata Data Tunggal (Mean)

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

> **Contoh:**
> Data: 5, 7, 8, 10, 10
>
> $\bar{x} = \frac{5 + 7 + 8 + 10 + 10}{5} = \frac{40}{5} = 8$

### 8.2 Rata-Rata Data Berbobot (dengan Frekuensi)

$$\bar{x} = \frac{\sum f_i \cdot x_i}{\sum f_i}$$

### 8.3 Rata-Rata Gabungan

Jika ada **dua kelompok** atau lebih data:

$$\bar{x}_{gab} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2}$$

Untuk $k$ kelompok:

$$\bar{x}_{gab} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2 + \cdots + n_k \bar{x}_k}{n_1 + n_2 + \cdots + n_k}$$

> **Contoh:**
> Kelas A (30 siswa) rata-rata 75. Kelas B (20 siswa) rata-rata 80.
>
> $\bar{x}_{gab} = \frac{30 \times 75 + 20 \times 80}{30 + 20} = \frac{2250 + 1600}{50} = \frac{3850}{50} = 77$

> [!warning] Kesalahan Umum
> Rata-rata gabungan **BUKAN** $\frac{75 + 80}{2} = 77{,}5$! Harus mempertimbangkan **jumlah data** di tiap kelompok.

---

## 9. Ukuran Pemusatan Data (Data Tunggal dan Kelompok)

### 9.1 Mean (Rata-Rata)

**Data Tunggal:** lihat Bagian 8.1

**Data Kelompok (Tabel Distribusi Frekuensi):**

$$\bar{x} = \frac{\sum f_i \cdot x_i}{\sum f_i}$$

di mana $x_i$ = **titik tengah kelas** = $\frac{\text{batas bawah} + \text{batas atas}}{2}$

> **Contoh:**
>
> | Interval | $f_i$ | $x_i$ | $f_i \cdot x_i$ |
> |:--------:|:-----:|:-----:|:---------------:|
> | 40–49 | 3 | 44,5 | 133,5 |
> | 50–59 | 7 | 54,5 | 381,5 |
> | 60–69 | 10 | 64,5 | 645 |
> | 70–79 | 5 | 74,5 | 372,5 |
> | **Σ** | **25** | | **1.532,5** |
>
> $\bar{x} = \frac{1.532{,}5}{25} = 61{,}3$

### 9.2 Median (Nilai Tengah)

**Data Tunggal:**
1. Urutkan data dari terkecil ke terbesar
2. Jika $n$ ganjil: median = data ke-$\frac{n+1}{2}$
3. Jika $n$ genap: median = $\frac{x_{n/2} + x_{(n/2)+1}}{2}$

**Data Kelompok:**

$$Me = L + \left(\frac{\frac{n}{2} - F}{f_{Me}}\right) \times p$$

| Simbol | Keterangan |
|--------|-----------|
| $L$ | Tepi bawah kelas median |
| $n$ | Jumlah seluruh data |
| $F$ | Frekuensi kumulatif **sebelum** kelas median |
| $f_{Me}$ | Frekuensi kelas median |
| $p$ | Panjang (lebar) kelas interval |

> [!tip] Cara Menentukan Kelas Median
> Kelas median adalah kelas di mana frekuensi kumulatifnya **pertama kali** ≥ $\frac{n}{2}$.

### 9.3 Modus (Nilai yang Paling Sering Muncul)

**Data Tunggal:** Nilai dengan frekuensi **terbesar**.

**Data Kelompok:**

$$Mo = L + \left(\frac{d_1}{d_1 + d_2}\right) \times p$$

| Simbol | Keterangan |
|--------|-----------|
| $L$ | Tepi bawah kelas modus |
| $d_1$ | Selisih frekuensi kelas modus dengan kelas **sebelumnya** |
| $d_2$ | Selisih frekuensi kelas modus dengan kelas **sesudahnya** |
| $p$ | Panjang kelas interval |

> [!tip] Kelas Modus
> Kelas modus = kelas dengan **frekuensi terbesar**.

---

## 10. Ukuran Penempatan Data (Data Tunggal dan Kelompok)

### 10.1 Kuartil ($Q_1$, $Q_2$, $Q_3$)

**Data Tunggal (sudah diurutkan):**

$$Q_i = \text{data ke-} \frac{i(n+1)}{4}, \quad i = 1, 2, 3$$

- $Q_1$ = kuartil bawah (25% data)
- $Q_2$ = median (50% data)
- $Q_3$ = kuartil atas (75% data)

Jika posisi jatuh di antara dua data, lakukan **interpolasi linear**.

**Data Kelompok:**

$$Q_i = L + \left(\frac{\frac{in}{4} - F}{f_{Q_i}}\right) \times p$$

> **Contoh Data Tunggal:**
> Data (n=11): 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
>
> $Q_1 = \text{data ke-} \frac{1 \times 12}{4} = \text{data ke-3} = 4$
>
> $Q_2 = \text{data ke-} \frac{2 \times 12}{4} = \text{data ke-6} = 7$
>
> $Q_3 = \text{data ke-} \frac{3 \times 12}{4} = \text{data ke-9} = 10$

### 10.2 Desil ($D_1, D_2, \ldots, D_9$)

**Data Tunggal:**

$$D_i = \text{data ke-} \frac{i(n+1)}{10}, \quad i = 1, 2, \ldots, 9$$

**Data Kelompok:**

$$D_i = L + \left(\frac{\frac{in}{10} - F}{f_{D_i}}\right) \times p$$

### 10.3 Persentil ($P_1, P_2, \ldots, P_{99}$)

**Data Tunggal:**

$$P_i = \text{data ke-} \frac{i(n+1)}{100}, \quad i = 1, 2, \ldots, 99$$

**Data Kelompok:**

$$P_i = L + \left(\frac{\frac{in}{100} - F}{f_{P_i}}\right) \times p$$

> [!info] Hubungan Antar Ukuran Penempatan
> - $Q_1 = P_{25} = D_{2{,}5}$
> - $Q_2 = P_{50} = D_5 = \text{Median}$
> - $Q_3 = P_{75} = D_{7{,}5}$

---

## 11. Ukuran Penyebaran Data (Data Tunggal dan Kelompok)

### 11.1 Jangkauan (Range)

$$R = x_{\max} - x_{\min}$$

### 11.2 Jangkauan Interkuartil (IQR) & Jangkauan Semi-Interkuartil

$$\text{IQR} = Q_3 - Q_1$$

$$Q_d = \frac{Q_3 - Q_1}{2} \quad \text{(hamparan semi-interkuartil)}$$

### 11.3 Simpangan Rata-Rata (Mean Deviation)

**Data Tunggal:**

$$SR = \frac{\sum_{i=1}^{n} |x_i - \bar{x}|}{n}$$

**Data Kelompok:**

$$SR = \frac{\sum f_i |x_i - \bar{x}|}{\sum f_i}$$

### 11.4 Ragam / Variansi (Variance)

**Data Tunggal (populasi):**

$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}$$

**Data Tunggal (sampel):**

$$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}$$

**Data Kelompok:**

$$\sigma^2 = \frac{\sum f_i (x_i - \bar{x})^2}{\sum f_i}$$

> [!tip] Rumus Cepat Variansi
> $$\sigma^2 = \frac{\sum x_i^2}{n} - \bar{x}^2 = \overline{x^2} - \bar{x}^2$$
> Atau untuk data berbobot:
> $$\sigma^2 = \frac{\sum f_i x_i^2}{\sum f_i} - \bar{x}^2$$

### 11.5 Simpangan Baku (Standard Deviation)

$$\sigma = \sqrt{\sigma^2} = \sqrt{\text{Variansi}}$$

### 11.6 Koefisien Variasi (CV)

$$CV = \frac{\sigma}{\bar{x}} \times 100\%$$

> Digunakan untuk **membandingkan** tingkat penyebaran dua kelompok data yang memiliki **satuan atau rata-rata berbeda**.

### 11.7 Contoh Lengkap — Ukuran Penyebaran Data Tunggal

> Data: 4, 6, 7, 8, 10
>
> **1. Jangkauan:** $R = 10 - 4 = 6$
>
> **2. Mean:** $\bar{x} = \frac{4+6+7+8+10}{5} = 7$
>
> **3. Simpangan Rata-Rata:**
>
> | $x_i$ | $\|x_i - 7\|$ |
> |:-----:|:-----------:|
> | 4 | 3 |
> | 6 | 1 |
> | 7 | 0 |
> | 8 | 1 |
> | 10 | 3 |
> | **Σ** | **8** |
>
> $SR = \frac{8}{5} = 1{,}6$
>
> **4. Variansi:**
>
> | $x_i$ | $(x_i - 7)^2$ |
> |:-----:|:-------------:|
> | 4 | 9 |
> | 6 | 1 |
> | 7 | 0 |
> | 8 | 1 |
> | 10 | 9 |
> | **Σ** | **20** |
>
> $\sigma^2 = \frac{20}{5} = 4$
>
> **5. Simpangan Baku:** $\sigma = \sqrt{4} = 2$

---
---

# 📝 RANGKUMAN RUMUS CEPAT

> [!tip] Cheat Sheet — Semua Rumus dalam Satu Tempat

### Persamaan Kuadrat

| Topik | Rumus |
|-------|-------|
| Rumus ABC | $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ |
| Diskriminan | $D = b^2 - 4ac$ |
| Jumlah akar | $x_1 + x_2 = -\frac{b}{a}$ |
| Hasil kali akar | $x_1 \cdot x_2 = \frac{c}{a}$ |
| PK baru dari akar $p, q$ | $x^2 - (p+q)x + pq = 0$ |

### Statistika — Data Kelompok

| Ukuran | Rumus |
|--------|-------|
| Mean | $\bar{x} = \frac{\sum f_i x_i}{\sum f_i}$ |
| Median | $Me = L + \frac{\frac{n}{2} - F}{f_{Me}} \times p$ |
| Modus | $Mo = L + \frac{d_1}{d_1 + d_2} \times p$ |
| Kuartil | $Q_i = L + \frac{\frac{in}{4} - F}{f_{Q}} \times p$ |
| Desil | $D_i = L + \frac{\frac{in}{10} - F}{f_{D}} \times p$ |
| Persentil | $P_i = L + \frac{\frac{in}{100} - F}{f_{P}} \times p$ |
| Variansi | $\sigma^2 = \frac{\sum f_i(x_i - \bar{x})^2}{\sum f_i}$ |
| Simpangan Baku | $\sigma = \sqrt{\sigma^2}$ |
| Rata-rata gabungan | $\bar{x}_{gab} = \frac{\sum n_i \bar{x}_i}{\sum n_i}$ |

---

## 📚 Istilah Penting (Glosarium)

| Istilah | Arti |
|---------|------|
| **Persamaan Kuadrat** | Persamaan polinomial derajat dua: $ax^2 + bx + c = 0$ |
| **Diskriminan** | Nilai $D = b^2 - 4ac$ yang menentukan jenis akar |
| **Rumus Vieta** | Hubungan jumlah dan hasil kali akar dengan koefisien |
| **SPLDV** | Sistem Persamaan Linear Dua Variabel |
| **SPLTV** | Sistem Persamaan Linear Tiga Variabel |
| **DHP** | Daerah Himpunan Penyelesaian (daerah arsiran di grafik) |
| **Mean** | Rata-rata hitung: jumlah data dibagi banyak data |
| **Median** | Nilai tengah data yang telah diurutkan |
| **Modus** | Nilai yang paling sering muncul |
| **Kuartil** | Membagi data menjadi **4 bagian** sama besar |
| **Desil** | Membagi data menjadi **10 bagian** sama besar |
| **Persentil** | Membagi data menjadi **100 bagian** sama besar |
| **Variansi** | Rata-rata kuadrat simpangan terhadap mean |
| **Simpangan Baku** | Akar kuadrat dari variansi |
| **Koefisien Variasi** | Perbandingan simpangan baku terhadap mean (dalam %) |
| **Titik Tengah Kelas** | Rata-rata batas bawah dan batas atas suatu interval |
| **Frekuensi Kumulatif** | Jumlah frekuensi dari kelas pertama sampai kelas tertentu |

---

## 🔗 Koneksi

- Kembali ke → [[Matematika ASAT MOC]]
- Terkait → [[Persamaan Kuadrat]]
- Terkait → [[Sistem Persamaan Linear]]
- Terkait → [[Pertidaksamaan Linear]]
- Terkait → [[Statistika Deskriptif]]
