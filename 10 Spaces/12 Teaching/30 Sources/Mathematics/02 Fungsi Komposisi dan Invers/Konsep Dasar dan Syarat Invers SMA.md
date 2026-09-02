---
title: "Konsep Dasar & Syarat Keberadaan Fungsi Invers"
type: "materi"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-12
sources:
  - "[[Fungsi Komposisi dan Invers SMA]]"
tags:
  - "#matematika"
  - "#fungsi_invers"
  - "#konsep_dasar"
  - "#bijektif"
  - "#kelas11"
---

[[Fungsi Komposisi dan Invers SMA|🏠 Master Dashboard]] | **Modul 1: Konsep & Syarat Invers** | [[Teknik Invers Fungsi Aljabar SMA|Modul 2: Teknik Aljabar ➡️]] | [[LKPD Fungsi Komposisi dan Invers SMA|📝 LKPD]]

---

# Modul 1: Konsep Dasar & Syarat Invers — Membongkar Mesin Undo Matematika! 🔮🔄

> **Pernahkah kamu salah mengetik paragraf panjang lalu refleks menekan `Ctrl + Z`?**  
> Atau pernahkah kamu menukar uang Rupiah (IDR) ke Yen Jepang (JPY) sebelum liburan, lalu ketika kembali ke Indonesia kamu menukar sisa Yen tersebut kembali menjadi Rupiah?  
>  
> Proses membalikkan suatu tindakan dari **hasil akhir kembali ke keadaan semula** adalah inti dari **Fungsi Invers**!

---

## 1. Analogi Visual: Mesin Fungsi vs Mesin Undo

Bayangkan sebuah fungsi matematika $f$ sebagai **Mesin Pemproses Data**:
1. Kamu memasukkan nilai bahan mentah $x$ (Domain) ke dalam mesin $f$.
2. Mesin $f$ mengolahnya dan mengeluarkan hasil olahan $y = f(x)$ (Range).

**Fungsi Invers** (dilambangkan dengan $f^{-1}$) adalah **Mesin Pembalik (Undo Machine)**:
- Mesin $f^{-1}$ mengambil hasil olahan $y$, mengolahnya kembali ke belakang, dan mengembalikan bahan mentah asli $x$!

![[diagram mathematics inverse function machine.webp]]

---

## 2. Definisi Formal Fungsi Invers

Secara matematis, jika fungsi $f$ memetakan himpunan $A$ ke himpunan $B$ yang dituliskan sebagai:
$$ f : A \rightarrow B \quad \text{dengan} \quad y = f(x) $$

Maka **invers dari fungsi $f$** (ditulis $f^{-1}$) adalah relasi yang memetakan himpunan $B$ kembali ke himpunan $A$:
$$ f^{-1} : B \rightarrow A \quad \text{dengan} \quad x = f^{-1}(y) $$

### Hubungan Utama Domain dan Range:
Setiap kali suatu fungsi memiliki invers, berlaku hubungan simetris yang sangat indah antara Domain (daerah asal) dan Range (daerah hasil):
$$ D_{f^{-1}} = R_f \quad \text{dan} \quad R_{f^{-1}} = D_f $$
* **Domain dari $f^{-1}$** adalah **Range dari $f$**.
* **Range dari $f^{-1}$** adalah **Domain dari $f$**.

---

## 3. Syarat Mutlak Keberadaan Invers: Kapan Invers Berupa Fungsi?

> [!WARNING]
> **Catatan Penting:** Semua fungsi pasti memiliki *relasi invers*, tetapi **TIDAK SEMUA** relasi invers merupakan *Fungsi Invers*!

Agar invers dari suatu fungsi $f$ juga membentuk sebuah **fungsi yang sah** (setiap anggota input dipetakan ke tepat satu output), maka fungsi awal $f$ **wajib bersifat Bijektif** (Korespondensi Satu-Satu).

Mari kita tinjau 3 jenis sifat pemetakan fungsi:

```text
1. Fungsi Injektif (Satu-Satu / One-to-One):
   - Setiap anggota B dihubungkan dengan maksimal satu anggota A.
   - Tidak boleh ada dua x berbeda yang memiliki nilai y sama (f(a) = f(b) => a = b).

2. Fungsi Surjektif (Pada / Onto):
   - Seluruh anggota B memiliki pasangan di A (Range = Kodomain).

3. Fungsi Bijektif (Injektif + Surjektif):
   - Setiap anggota A berpasangan tepat satu dengan anggota B, dan tidak ada anggota B yang menganggur.
   - HANYA FUNGSI BIJEKTIF YANG MEMILIKI FUNGSI INVERS (f^-1)!
```

### 🧪 Uji Garis Horizontal (Horizontal Line Test)

Bagaimana cara mengetahui apakah sebuah grafik fungsi memiliki invers berupa fungsi tanpa harus menghitung rumusnya? Gunakan **Uji Garis Horizontal**!

1. Gambarkan grafik fungsi $y = f(x)$ pada bidang Kartesius.
2. Tarik garis lurus horizontal sembarang ($y = c$) yang memotong grafik.
3. **Aturan Uji:**
   * Jika setiap garis horizontal memotong grafik di **tepat SATU titik**, maka fungsi tersebut bersifat **Injektif (Satu-Satu)** dan **MEMILIKI fungsi invers**.
   * Jika ada garis horizontal yang memotong grafik di **LEBIH DARI SATU titik**, maka fungsi tersebut **TIDAK memiliki fungsi invers** (kecuali domainnya dibatasi).

#### Contoh Kasus Grafik:
* **Fungsi Linier $f(x) = 2x + 3$:** Garis horizontal selalu memotong di 1 titik $\rightarrow$ Memiliki fungsi invers!
* **Fungsi Kuadrat $f(x) = x^2$ (untuk seluruh $x \in \mathbb{R}$):** Garis horizontal $y = 4$ memotong grafik di dua titik, yaitu $x = 2$ dan $x = -2$. Maka inversnya $x = \pm \sqrt{y}$ **bukan fungsi**!  
  *(Agar memilik invers, domain $f(x) = x^2$ harus dibatasi, misal untuk $x \geq 0$).*

---

## 4. Pencerminan Grafik Terhadap Garis $y = x$

Salah satu sifat geometris paling menakjubkan dari fungsi invers adalah kesimetrisannya.

Garis grafik fungsi invers $y = f^{-1}(x)$ merupakan **hasil pencerminan (refleksi)** dari grafik fungsi asli $y = f(x)$ terhadap garis cermin diagonal **$y = x$**.

Jika titik $(a, b)$ terletak pada grafik $y = f(x)$, maka titik $(b, a)$ pasti terletak pada grafik $y = f^{-1}(x)$!

---

## 🎯 Contoh Soal & Pembahasan Konseptual

### Contoh 1: Menguji Sifat Invers dari Diagram Panah
Diketahui dua pemetaan berikut:
* Pemetaan $f = \{(1, a), (2, b), (3, c)\}$
* Pemetaan $g = \{(1, a), (2, a), (3, b)\}$

Tentukan apakah invers dari $f$ dan $g$ merupakan fungsi!

**Pembahasan:**
1. Untuk pemetaan $f$:
   - Anggota domain $\{1, 2, 3\}$ dipetakan ke anggota kodomain $\{a, b, c\}$ secara unik satu-satu.
   - Inversnya adalah $f^{-1} = \{(a, 1), (b, 2), (c, 3)\}$. Setiap input $\{a, b, c\}$ memiliki tepat satu pasangan.
   - **Kesimpulan:** $f$ bersifat bijektif, sehingga $f^{-1}$ adalah **Fungsi Invers**.

2. Untuk pemetaan $g$:
   - Anggota $1$ dan $2$ sama-sama dipetakan ke $a$.
   - Inversnya adalah $g^{-1} = \{(a, 1), (a, 2), (b, 3)\}$.
   - Elemen $a$ pada invers bercabang memetakan ke $1$ dan $2$, yang melanggar definisi fungsi!
   - **Kesimpulan:** $g$ tidak bijektif, sehingga $g^{-1}$ **bukan merupakan fungsi invers** (hanya relasi biasa).

---

### Contoh 2: Menentukan Domain dan Range Invers
Diketahui fungsi linier $f(x) = 3x - 6$ dengan domain dibatasi pada $D_f = \{x \mid 1 \leq x \leq 5, x \in \mathbb{R}\}$.
Tentukan Domain ($D_{f^{-1}}$) dan Range ($R_{f^{-1}}$) dari fungsi inversnya!

**Pembahasan:**
1. Cari nilai minimum dan maksimum dari Range fungsi awal ($R_f$):
   - Untuk $x = 1 \Rightarrow f(1) = 3(1) - 6 = -3$
   - Untuk $x = 5 \Rightarrow f(5) = 3(5) - 6 = 9$
   - Maka Range awal adalah $R_f = \{y \mid -3 \leq y \leq 9, y \in \mathbb{R}\}$.

2. Gunakan sifat simetris domain-range invers:
   - $D_{f^{-1}} = R_f = \{x \mid -3 \leq x \leq 9, x \in \mathbb{R}\}$
   - $R_{f^{-1}} = D_f = \{y \mid 1 \leq y \leq 5, y \in \mathbb{R}\}$

---

[[Fungsi Komposisi dan Invers SMA|🏠 Master Dashboard]] | **Modul 1: Konsep & Syarat Invers** | [[Teknik Invers Fungsi Aljabar SMA|Modul 2: Teknik Aljabar ➡️]] | [[LKPD Fungsi Komposisi dan Invers SMA|📝 LKPD]]
