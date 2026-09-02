---
title: "Kaidah Pencacahan & Kombinatorika — Permutasi, Kombinasi, & Binomial Newton"
type: master-dashboard
subject: mathematics
level: sma
target_audience: "SMA Kelas 12"
created: 2026-08-09
sources:
  - "[[Logika Permutasi dan Kombinasi SMA]]"
  - "[[Teori Peluang dan Kejadian Majemuk SMA]]"
  - "[[LKPD Kaidah Pencacahan dan Kombinatorika SMA]]"
  - "[[LKPD Teori Peluang dan Kejadian Majemuk SMA]]"
  - "[[Suku Banyak Polinomial SMA]]"
tags:
  - teaching-material
  - mathematics
  - pencacahan
  - permutasi
  - kombinasi
  - binomial-newton
---

# Kaidah Pencacahan & Kombinatorika — Menghitung Segala Kemungkinan! 🎲🔢

Halo temen-temen Kelas 12! Selamat ya, udah sampai di tingkat paling akhir di SMA. Dikit lagi kalian bakal melangkah ke jenjang yang lebih tinggi—mulai dari masuk Kampus Impian (SNBP/SNBT), dunia kerja, sampai perjalanan hidup baru. 

Salah satu bab Matematika yang **paling sering keluar di Ujian Sekolah maupun UTBK-SNBT** adalah **Kaidah Pencacahan (Counting Principles) dan Kombinatorika**. 

Di kehidupan nyata, kemampuan menghitung kombinasi dan susunan ini sangat vital:
- *Berapa banyak kombinasi password/PIN 6 digit yang aman dari peretasan?*
- *Berapa banyak variasi susunan tim e-sports atau susunan pengurus organisasi yang dapat dibentuk?*
- *Bagaimana menghitung koefisien suku aljabar berpangkat tinggi tanpa harus mengalikan satu per satu?*

Di modul ini, kita bakal bedah tuntas semua konsep Kaidah Pencacahan secara **lengkap, komprehensif, santai, mudah dipahami**, dan *straight-to-the-point*! Yuk, siapkan catatan dan mari kita mulai! ☕🚀

---

## 1. Aturan Pengisian Tempat (Filling Slots) & Prinsip Dasar Pencacahan

Sebelum masuk ke rumus Permutasi & Kombinasi, fondasi paling dasar dari pencacahan adalah **Aturan Penjumlahan** dan **Aturan Perkalian**.

### a. Aturan Penjumlahan (Pilihan "ATAU" / Saling Lepas)
Jika ada $k$ pilihan kegiatan terpisah yang **tidak bisa dilakukan secara bersamaan** (saling lepas), maka total cara adalah:
$$\text{Total Cara} = n_1 + n_2 + \dots + n_k$$
- *Contoh:* Andi mau pergi ke sekolah. Ia punya 3 sepeda motor dan 2 mobil. Banyak pilihan kendaraan yang bisa dipakai Andi adalah $3 + 2 = 5\text{ cara}$.

### b. Aturan Perkalian (Pilihan "DAN" / Tahapan Berurutan)
Jika suatu rangkaian kegiatan terdiri dari beberapa tahap berurutan (Tahap 1 ada $n_1$ cara, Tahap 2 ada $n_2$ cara, dst.), total cara adalah:
$$\text{Total Cara} = n_1 \times n_2 \times \dots \times n_k$$
- *Contoh:* Rina punya 4 baju dan 3 celana. Banyak pasangan pakaian yang bisa dipakai adalah $4 \times 3 = 12\text{ pasang}$.

### c. Metode Pengisian Tempat (Filling Slots) — Pembentukan Bilangan Bersyarat
Metode ini sangat sering keluar di UTBK untuk menyusun angka/plat nomor bersyarat.

#### Contoh Real HOTS:
Disediakan angka-angka $\{1, 2, 3, 4, 5, 6, 7\}$. Akan dibentuk bilangan 3 digit yang **nilainya lebih besar dari 400** dan **tidak boleh ada angka yang berulang**. Berapa banyak bilangan yang terbentuk?

* **Analisis Kotak (Ratusan - Puluhan - Satuan):**
  1. **Kotak Ratusan:** Syarat $> 400$, maka angka ratusan yang boleh adalah $\{4, 5, 6, 7\} \rightarrow \mathbf{4\text{ pilihan}}$.
  2. **Kotak Puluhan:** Dari 7 angka yang tersedia, 1 angka sudah dipakai di ratusan $\rightarrow \text{sisa } 7 - 1 = \mathbf{6\text{ pilihan}}$.
  3. **Kotak Satuan:** 2 angka sudah dipakai di ratusan & puluhan $\rightarrow \text{sisa } 7 - 2 = \mathbf{5\text{ pilihan}}$.
* **Total Bilangan Formed:** $4 \times 6 \times 5 = 120\text{ bilangan}$.

---

## 2. Bedah 5 Jenis Permutasi (Urutan Diprioritaskan!)

> ⚠️ **Prinsip Utama Permutasi:** **URUTAN DIPERHATIKAN!** $(A, B) \neq (B, A)$.

### 1. Permutasi dari $n$ Elemen Berbeda
$$P = n! = n \times (n-1) \times \dots \times 1$$
- *Contoh:* Menyusun 5 bendera berbeda secara berjajar $= 5! = 120\text{ cara}$.

### 2. Permutasi $r$ Unsur dari $n$ Elemen ($r \le n$)
$$_n P_r = \frac{n!}{(n - r)!}$$
- *Contoh:* Memilih Ketua, Sekretaris, Bendahara dari 8 calon $= _8 P_3 = \frac{8!}{5!} = 8 \times 7 \times 6 = 336\text{ cara}$.

### 3. Permutasi dengan Unsur yang Sama (Identik)
$$P = \frac{n!}{k_1! \cdot k_2! \cdot \dots \cdot k_t!}$$
- *Contoh:* Menyusun kata dari **"BASSABASSI"** ($n=10, B=2, A=3, S=4, I=1$):
  $$P = \frac{10!}{2! \cdot 3! \cdot 4! \cdot 1!} = \frac{3.628.800}{2 \times 6 \times 24 \times 1} = 12.600\text{ susunan}$$.

### 4. Permutasi Siklis (Melingkar)
$$P_{\text{siklis}} = (n - 1)!$$
- *Contoh:* 5 orang duduk mengelilingi meja bundar $= (5-1)! = 4! = 24\text{ cara}$.

#### Variasi HOTS (Siklis Berdampingan):
Jika 7 orang (termasuk Ketua & Sekretaris) duduk melingkar dan **Ketua & Sekretaris harus selalu berdampingan**:
1. Ketua & Sekretaris diikat jadi 1 grup $\rightarrow$ total objek dianggap $(7 - 2) + 1 = 6$ objek.
2. Permutasi siklis 6 objek $= (6-1)! = 5! = 120$.
3. Posisi internal Ketua & Sekretaris $= 2! = 2$.
4. Total $= 120 \times 2 = 240\text{ cara}$.

### 5. Permutasi Berulang
$$P_{\text{berulang}} = n^k$$
- *Contoh:* PIN 3 digit dari angka $\{1,2,3,4,5,6\}$ (boleh berulang) $= 6^3 = 216\text{ susunan}$.

---

## 3. Kombinasi (Urutan Tidak Diprioritaskan)

> 💡 **Prinsip Utama Kombinasi:** **URUTAN TIDAK DIPERHATIKAN!** $(A, B) = (B, A)$.

Notasi kombinasi $r$ objek dari $n$ objek:
$$_n C_r = \binom{n}{r} = \frac{n!}{(n - r)! \cdot r!}$$

### Contoh Real:
Memilih tim basket (5 orang dari 9 calon pemain):
$$_9 C_5 = \frac{9!}{(9-5)! \cdot 5!} = \frac{9 \times 8 \times 7 \times 6 \times 5!}{4 \times 3 \times 2 \times 1 \times 5!} = 126\text{ cara}$$

---

## 4. Binomial Newton Lanjutan (HOTS)

Teorema Binomial Newton digunakan untuk mengekspansi aljabar $(a + b)^n$:
$$(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$

### Rumus Suku ke-$(r+1)$:
$$\text{Suku ke-}(r+1) = \binom{n}{r} a^{n-r} b^r$$

### 1. Mencari Koefisien Suku $x^k$
Tentukan koefisien suku yang memuat $x^9$ pada $(2x + y)^{15}$:
- $a = 2x, b = y, n = 15$.
- Pangkat $x$ pada suku ke-$(r+1)$ adalah $15-r$.
- Kita ingin $15 - r = 9 \implies r = 6$ (suku ke-7).
- $\text{Suku ke-}7 = \binom{15}{6} (2x)^9 y^6 = 5.005 \times 512 x^9 y^6 = 2.562.560 x^9 y^6$.
- Jadi koefisiennya adalah **$2.562.560$**.

### 2. Mencari Suku Bebas dari $x$ (Suku Konstan / $x^0$)
Tentukan suku konstan (bebas dari $x$) dalam penjabaran aljabar $\left(x^2 + \frac{2}{x}\right)^9$!
- **Analisis:**
  - $a = x^2, b = 2x^{-1}, n = 9$.
  - $\text{Suku ke-}(r+1) = \binom{9}{r} (x^2)^{9-r} (2x^{-1})^r = \binom{9}{r} x^{18-2r} \cdot 2^r \cdot x^{-r} = \binom{9}{r} 2^r \cdot x^{18-3r}$.
  - Bebas dari $x \implies$ Pangkat $x = 0 \implies 18 - 3r = 0 \implies r = 6$.
  - Maka nilainya $= \binom{9}{6} 2^6 = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} \times 64 = 84 \times 64 = 5.376$.

---

## 5. Cheat Sheet & Rangkuman Quick Reference 📋

| Jenis Pencacahan | Rumus Utama | Ciri Khas / Kata Kunci |
| :--- | :--- | :--- |
| **Filling Slots (Aturan Perkalian)** | $n_1 \times n_2 \times \dots \times n_k$ | Tahapan berurutan / pembentukan angka bersyarat |
| **Permutasi Unsur Berbeda** | $_n P_r = \frac{n!}{(n-r)!}$ | Urutan penting (Ketua, PIN, Juara) |
| **Permutasi Unsur Sama** | $P = \frac{n!}{k_1! k_2! \dots}$ | Kata dengan huruf kembar |
| **Permutasi Siklis** | $P_{\text{siklis}} = (n-1)!$ | Meja bundar / susunan melingkar |
| **Kombinasi** | $_n C_r = \frac{n!}{(n-r)! r!}$ | Urutan tidak penting (Tim, memilih delegasi) |
| **Binomial Newton (Suku Bebas $x$)** | $\text{Suku} = \binom{n}{r} a^{n-r} b^r$ | Cari $r$ hingga pangkat $x = 0$ |

---

> *“Kombinatorika bukan tentang menghafal rumus, melainkan tentang melatih logika menyusun kemungkinan secara sistematis!”* 💡🔥
