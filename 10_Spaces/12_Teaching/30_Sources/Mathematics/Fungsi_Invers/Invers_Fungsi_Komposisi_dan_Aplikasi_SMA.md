---
title: "Invers Fungsi Komposisi & Aplikasi Kontekstual HOTS"
type: "materi"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-12
sources:
  - "[[Fungsi_Invers_SMA]]"
  - "[[Teknik_Invers_Fungsi_Aljabar_SMA]]"
tags:
  - "#matematika"
  - "#fungsi_invers"
  - "#fungsi_komposisi"
  - "#hots"
  - "#aplikasi_nyata"
  - "#kelas11"
---

[[Fungsi_Invers_SMA|🏠 Master Dashboard]] | [[Teknik_Invers_Fungsi_Aljabar_SMA|⬅️ Modul 2: Teknik Aljabar]] | **Modul 3: Invers Komposisi & Aplikasi** | [[LKPD_Fungsi_Invers_SMA|📝 LKPD]] | [[Soal_Fungsi_Invers_SMA|🎯 Soal Evaluasi]]

---

# Modul 3: Invers Fungsi Komposisi & Aplikasi Kontekstual HOTS 🛍️💱

> Selamat datang di modul penutup! Di sini kita akan menggabungkan dua konsep matematika yang sangat ampuh: **Fungsi Komposisi** dan **Fungsi Invers**, serta melihat bagaimana rumusan ini dipakai dalam bisnis, keuangan, dan sistem keamanan kode!

---

## 1. Analogi Kaos Kaki & Sepatu: Rahasia Urutan Terbalik!

Bayangkan kamu hendak bersiap-siap berangkat sekolah di pagi hari:
1. **Langkah 1 (\(g\)):** Kamu memakai kaos kaki terlebih dahulu.
2. **Langkah 2 (\(f\)):** Kamu memakai sepatu di atas kaos kaki.

Proses gabungan berangkat sekolah adalah komposisi fungsi \((f \circ g)(x)\).

Sekarang, bayangkan saat kamu pulang sekolah dan ingin membatalkan (meng-invers) tindakan tersebut:
* Apakah kamu melepas kaos kaki dulu baru melepas sepatu? **Tentu tidak mungkin!**
* Kamu harus **melepas sepatu dulu (\(f^{-1}\))**, baru kemudian **melepas kaos kaki (\(g^{-1}\))**!

```text
Proses Maju (Komposisi):         x  ---> [ g ] ---> [ f ] ---> (f o g)(x)
Proses Mundur (Invers):  (f o g)(x) ---> [ f^-1 ] ---> [ g^-1 ] ---> x

Aturan Utama:
(f o g)^-1(x) = (g^-1 o f^-1)(x)
```

> ⚠️ **Peringatan Penting:** Urutan pemetaan pada invers komposisi **WAJIB DIBALIK**!  
> \((f \circ g)^{-1} \neq f^{-1} \circ g^{-1}\), melainkan \((f \circ g)^{-1} = g^{-1} \circ f^{-1}\).

---

## 2. Sifat-Sifat Utama Invers Fungsi Komposisi

Berikut adalah teorema dan sifat dasar yang sering muncul dalam pembuktian dan latihan soal:

1. **Sifat Invers Ganda:**
   \[ (f^{-1})^{-1}(x) = f(x) \]
2. **Sifat Fungsi Identitas:**
   \[ (f \circ f^{-1})(x) = (f^{-1} \circ f)(x) = I(x) = x \]
3. **Invers Tiga Komposisi Fungsi:**
   \[ (f \circ g \circ h)^{-1}(x) = (h^{-1} \circ g^{-1} \circ f^{-1})(x) \]
4. **Mencari Salah Satu Fungsi Komposisi:**
   - Jika \( (f \circ g)(x) = h(x) \), maka:
     \[ f(x) = (h \circ g^{-1})(x) \]
     \[ g(x) = (f^{-1} \circ h)(x) \]

---

## 3. Dua Metode Penyelesaian Soal Invers Komposisi

Ada 2 cara yang dapat kamu gunakan saat menyelesaikan soal tipe \((f \circ g)^{-1}(x)\):

### 🛠️ Metode A: Komposisikan Dulu, Lalu Inverskan
1. Cari rumus komposisi gabungan \(h(x) = (f \circ g)(x)\).
2. Tentukan invers dari hasil tersebut: \(h^{-1}(x) = (f \circ g)^{-1}(x)\).

### 🛠️ Metode B: Inverskan Masing-masing, Lalu Komposisikan Terbalik
1. Cari invers masing-masing fungsi: \(f^{-1}(x)\) dan \(g^{-1}(x)\).
2. Masukkan ke dalam rumus: \((g^{-1} \circ f^{-1})(x)\).

---

### Contoh Soal 1 (Komposisi Invers):
Diketahui fungsi \(f(x) = 2x + 1\) dan \(g(x) = \frac{x - 3}{x + 2}, x \neq -2\). Tentukan nilai dari \((f \circ g)^{-1}(1)\)!

**Pembahasan (Menggunakan Metode B - Cepat untuk Nilai Spesifik):**
Ingat bahwa \((f \circ g)^{-1}(1) = (g^{-1} \circ f^{-1})(1) = g^{-1}(f^{-1}(1))\).

* **Langkah 1:** Cari nilai \(f^{-1}(1)\):  
  Misalkan \(f(a) = 1 \Rightarrow 2a + 1 = 1 \Rightarrow 2a = 0 \Rightarrow a = 0\).  
  Jadi, \(f^{-1}(1) = 0\).

* **Langkah 2:** Hitung \(g^{-1}(0)\):  
  Misalkan \(g(b) = 0 \Rightarrow \frac{b - 3}{b + 2} = 0 \Rightarrow b - 3 = 0 \Rightarrow b = 3\).  
  Jadi, \(g^{-1}(0) = 3\).

* **Kesimpulan:** Nilai dari \((f \circ g)^{-1}(1) = 3\).

---

## 4. Aplikasi Kontekstual Dunia Nyata (Soal HOTS)

### 🏬 Kasus 1: Perhitungan Diskon Bertingkat & Pembatalannya
Sebuah pusat perbelanjaan memberikan penawaran **Diskon Ganda Promo Kemerdekaan**:
- **Promo 1 (Fungsi \(g\)):** Diskon sebesar \(20\%\) dari harga awal \(x\).
  \[ g(x) = 0{,}8x \]
- **Promo 2 (Fungsi \(f\)):** Potongan harga tambahan dari kupon member sebesar Rp \(50.000\).
  \[ f(x) = x - 50.000 \]

#### Permasalahan:
1. Tentukan fungsi total harga yang harus dibayar konsumen \( (f \circ g)(x) \)!
2. Jika seorang pembeli membayar sebesar **Rp \(350.000\)** di kasir, berapa harga asli barang tersebut sebelum diskon? *(Gunakan Fungsi Invers)*.

#### Pembahasan:
1. **Fungsi Total Harga \( (f \circ g)(x) \):**  
   \[ (f \circ g)(x) = f(g(x)) = f(0{,}8x) = 0{,}8x - 50.000 \]

2. **Mencari Harga Asli Barang via Invers \( (f \circ g)^{-1}(y) \):**  
   Misalkan \(y = 0{,}8x - 50.000\)  
   \(y + 50.000 = 0{,}8x\)  
   \(x = \frac{y + 50.000}{0{,}8} = 1{,}25(y + 50.000)\)  

   Maka rumus inversnya:  
   \[ (f \circ g)^{-1}(y) = 1{,}25y + 62.500 \]

   Untuk pembeli yang membayar \(y = 350.000\):  
   \[ x = 1{,}25(350.000) + 62.500 = 437.500 + 62.500 = 500.000 \]

   > **Hasil:** Harga asli barang sebelum seluruh diskon adalah **Rp \(500.000\)**.

---

### 💱 Kasus 2: Konversi Valuta Asing Ganda
Sebuah agen perjalanan internasional melayani penukaran uang dengan rute:
* Rupiah (IDR) ke US Dollar (USD): \( f(x) = \frac{x}{15.000} \)
* US Dollar (USD) ke Euro (EUR): \( g(y) = 0{,}9y \)

Tentukan fungsi invers \((g \circ f)^{-1}(z)\) yang menghitung berapa Rupiah yang dibutuhkan jika seorang turis memerlukan \(z\) Euro!

#### Pembahasan:
1. **Fungsi Komposisi IDR ke EUR:**  
   \[ (g \circ f)(x) = g(f(x)) = g\left(\frac{x}{15.000}\right) = 0{,}9 \times \frac{x}{15.000} = \frac{0{,}9x}{15.000} = \frac{3x}{50.000} \]

2. **Invers Fungsi (EUR ke IDR):**  
   Misalkan \(z = \frac{3x}{50.000}\)  
   \(3x = 50.000z\)  
   \(x = \frac{50.000z}{3}\)

   > **Hasil:** Untuk mendapatkan \(z\) Euro, jumlah Rupiah yang dibutuhkan adalah \((g \circ f)^{-1}(z) = \frac{50.000}{3} z\).

---

[[Fungsi_Invers_SMA|🏠 Master Dashboard]] | [[Teknik_Invers_Fungsi_Aljabar_SMA|⬅️ Modul 2: Teknik Aljabar]] | **Modul 3: Invers Komposisi & Aplikasi** | [[LKPD_Fungsi_Invers_SMA|📝 LKPD]] | [[Soal_Fungsi_Invers_SMA|🎯 Soal Evaluasi]]
