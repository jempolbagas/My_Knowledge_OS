---
title: "Operasi Bentuk Akar dan Merasionalkan Penyebut — Dari Geometri ke Aljabar Presisi"
type: materi
subject: mathematics
level: smp
target_audience: "SMP Kelas VIII & IX (Fase D)"
created: 2026-09-04
sources:
  - "[[Eksponen_dan_Bentuk_Akar_SMP]]"
tags:
  - teaching/materi
  - matematika
  - bentuk-akar
  - merasionalkan-penyebut
  - smp-kelas-8
  - smp-kelas-9
---

*Navigasi Cepat:*  
[[Eksponen_dan_Bentuk_Akar_SMP|🏠 Master Dashboard]] | [[Bilangan_Berpangkat_dan_Sifatnya_SMP|⬅️ Modul 1: Bilangan Berpangkat]] | **Modul 2: Operasi Bentuk Akar** | [[Persamaan_Eksponen_dan_Notasi_Ilmiah_SMP|Modul 3: Persamaan Eksponen & Sains ➡️]] | [[LKPD_Eksponen_dan_Bentuk_Akar_SMP|📋 LKPD]] | [[Soal_Eksponen_dan_Bentuk_Akar_SMP|📝 Soal Evaluasi]]

---

# Operasi Bentuk Akar & Merasionalkan Penyebut — Dari Geometri ke Aljabar Presisi! 📐🌿

Pernahkah kamu memperhatikan spesifikasi layar smartphone atau laptop? Ketika produsen menulis *"Layar 6,5 inci"*, angka tersebut sebenarnya adalah **panjang diagonal** layar!

Kalau kamu punya bingkai persegi dengan panjang sisi masing-masing $1\text{ meter}$, berapa panjang garis diagonal yang membelah persegi itu? Menurut Teorema Pythagoras:

$$c = \sqrt{1^2 + 1^2} = \sqrt{1 + 1} = \sqrt{2}\text{ meter}$$

Berapa nilai pasti dari $\sqrt{2}$? Kalau kamu tekan kalkulator, layarmu akan menampilkan $1{,}41421356237\dots$ dan desimalnya tidak pernah berhenti ataupun berulang secara teratur! Angka misterius inilah yang dalam sejarah matematika kuno membuat para pengikut Pythagoras takjub sekaligus bingung, karena nilainya tidak bisa ditulis sebagai pecahan bilangan bulat biasa.

Inilah gerbang pembuka kita menuju dunia **Bentuk Akar** dan teknik **Merasionalkan Penyebut**!

---

## 1. Membedakan Akar Rasional vs Bentuk Akar (Irasional) 🔍

Tidak semua bilangan yang memakai simbol akar $(\sqrt{\dots})$ disebut sebagai **Bentuk Akar**. Mari kita bedakan dengan tegas:

1. **Akar Rasional (Bukan Bentuk Akar):**  
   Akar yang jika dihitung menghasilkan bilangan bulat atau pecahan rasional $\frac{a}{b}$.
   - $\sqrt{4} = 2$ (karena $2 \times 2 = 4$)
   - $\sqrt{25} = 5$
   - $\sqrt{144} = 12$
   - $\sqrt{0{,}49} = 0{,}7 = \frac{7}{10}$

2. **Bentuk Akar (Bilangan Irasional):**  
   Akar dari suatu bilangan rasional positif yang hasilnya berupa **bilangan irasional** (desimal tak berhingga dan tidak berulang).
   - $\sqrt{2}, \sqrt{3}, \sqrt{5}, \sqrt{7}, \sqrt{10}, \sqrt{50}$ adalah **bentuk akar sejati**.

---

## 2. Jurus Menyederhanakan Bentuk Akar ✂️

Bentuk akar yang angkanya besar sering kali bisa kita rampingkan agar mudah dioperasikan. Kuncinya ada pada sifat perkalian akar:

$$\sqrt{a \cdot b} = \sqrt{a} \times \sqrt{b} \quad (a, b \ge 0)$$

> **Trik Emas:**  
> Pecah bilangan di dalam akar menjadi perkalian dua bilangan, di mana **salah satu bilangannya wajib merupakan angka kuadrat sempurna terbesar** ($4, 9, 16, 25, 36, 49, 64, 81, 100, \dots$)!

### Contoh Kasus:
1. **Sederhanakan $\sqrt{12}$:**  
   Pecah $12$ menjadi $4 \times 3$ ($4$ adalah kuadrat dari $2$):  
   $$\sqrt{12} = \sqrt{4 \times 3} = \sqrt{4} \times \sqrt{3} = \mathbf{2\sqrt{3}}$$
2. **Sederhanakan $\sqrt{75}$:**  
   Pecah $75$ menjadi $25 \times 3$:  
   $$\sqrt{75} = \sqrt{25 \times 3} = \sqrt{25} \times \sqrt{3} = \mathbf{5\sqrt{3}}$$
3. **Sederhanakan $\sqrt{72}$:**  
   $72$ bisa dipecah jadi $9 \times 8$ atau $36 \times 2$. Selalu pilih kuadrat sempurna **terbesar** ($36$):  
   $$\sqrt{72} = \sqrt{36 \times 2} = \sqrt{36} \times \sqrt{2} = \mathbf{6\sqrt{2}}$$

---

## 3. Operasi Aljabar pada Bentuk Akar ➕✖️

### A. Penjumlahan & Pengurangan (Wajib Suku Sejenis)
Kamu hanya boleh menjumlahkan atau mengurangkan bentuk akar jika **angka di dalam akarnya (radikan) persis sama**. Ini sama persis seperti aljabar variabel: $3x + 2x = 5x$.

$$p\sqrt{a} + q\sqrt{a} = (p + q)\sqrt{a}$$
$$p\sqrt{a} - q\sqrt{a} = (p - q)\sqrt{a}$$

> **Legenda:**
> - $p, q$ = Koefisien di luar akar.
> - $a$ = Radikan (bilangan di dalam akar).

**Contoh:**
1. $4\sqrt{3} + 5\sqrt{3} = (4 + 5)\sqrt{3} = \mathbf{9\sqrt{3}}$.
2. $\sqrt{50} + \sqrt{18} - \sqrt{32}$:  
   *Langkah:* Sederhanakan masing-masing akar terlebih dahulu!  
   - $\sqrt{50} = \sqrt{25 \times 2} = 5\sqrt{2}$  
   - $\sqrt{18} = \sqrt{9 \times 2} = 3\sqrt{2}$  
   - $\sqrt{32} = \sqrt{16 \times 2} = 4\sqrt{2}$  
   
   Gabungkan:  
   $$= 5\sqrt{2} + 3\sqrt{2} - 4\sqrt{2} = (5 + 3 - 4)\sqrt{2} = \mathbf{4\sqrt{2}}$$

---

### B. Perkalian Bentuk Akar
Pada perkalian, angka di dalam akar tidak harus sama. Rumusnya: **"Luar kalikan luar, dalam kalikan dalam!"**

$$(p\sqrt{a}) \times (q\sqrt{b}) = (p \cdot q)\sqrt{a \cdot b}$$

> **Sifat Khusus Akar Kembar:**  
> $$\sqrt{a} \times \sqrt{a} = (\sqrt{a})^2 = a \quad (a \ge 0)$$

**Contoh:**
1. $2\sqrt{3} \times 4\sqrt{5} = (2 \times 4)\sqrt{3 \times 5} = \mathbf{8\sqrt{15}}$.
2. $3\sqrt{6} \times 2\sqrt{3} = (3 \times 2)\sqrt{6 \times 3} = 6\sqrt{18}$.  
   Sederhanakan $\sqrt{18} = \sqrt{9 \times 2} = 3\sqrt{2}$:  
   $$= 6 \times 3\sqrt{2} = \mathbf{18\sqrt{2}}$$
3. Distributif Aljabar:  
   $$\sqrt{3}(2 + \sqrt{6}) = (\sqrt{3} \times 2) + (\sqrt{3} \times \sqrt{6}) = 2\sqrt{3} + \sqrt{18} = \mathbf{2\sqrt{3} + 3\sqrt{2}}$$

---

### C. Pembagian Bentuk Akar
Penyederhanaan pecahan di bawah tanda akar dapat langsung dibagi:

$$\frac{\sqrt{a}}{\sqrt{b}} = \sqrt{\frac{a}{b}} \quad (a \ge 0, b > 0)$$

**Contoh:**
$$\frac{\sqrt{48}}{\sqrt{3}} = \sqrt{\frac{48}{3}} = \sqrt{16} = \mathbf{4}$$

---

## 4. Seni Merasionalkan Penyebut Pecahan 💎

Mengapa penyebut pecahan tidak boleh berupa bentuk akar?  
Bayangkan kamu harus menghitung $\frac{6}{\sqrt{2}}$ secara manual: membagi angka $6$ dengan desimal $1{,}414213\dots$ adalah mimpi buruk! Tapi kalau penyebutnya dirasionalkan menjadi bilangan bulat, perhitungannya jadi sangat mudah dan rapi.

### Tipe 1: Penyebut Tunggal ($\frac{a}{\sqrt{b}}$)
Kalikan pembilang dan penyebut dengan bentuk akar yang sama:

$$\frac{a}{\sqrt{b}} = \frac{a}{\sqrt{b}} \times \frac{\sqrt{b}}{\sqrt{b}} = \frac{a\sqrt{b}}{b}$$

> **Contoh:**  
> Rasionalkan $\frac{8}{\sqrt{2}}$:  
> $$\frac{8}{\sqrt{2}} = \frac{8}{\sqrt{2}} \times \frac{\sqrt{2}}{\sqrt{2}} = \frac{8\sqrt{2}}{2} = \mathbf{4\sqrt{2}}$$

---

### Tipe 2: Penyebut Dua Suku Sekawan ($\frac{c}{a \pm \sqrt{b}}$)
Jika penyebut berbentuk penjumlahan atau pengurangan dua suku, gunakan **Bentuk Sekawan (*Conjugate*)**!  
- Sekawan dari $(a + \sqrt{b})$ adalah $(a - \sqrt{b})$.  
- Sekawan dari $(a - \sqrt{b})$ adalah $(a + \sqrt{b})$.

Prinsip ini memanfaatkan identitas aljabar selisih kuadrat:
$$(x + y)(x - y) = x^2 - y^2 \implies (a + \sqrt{b})(a - \sqrt{b}) = a^2 - (\sqrt{b})^2 = a^2 - b$$

$$\frac{c}{a + \sqrt{b}} = \frac{c}{a + \sqrt{b}} \times \frac{a - \sqrt{b}}{a - \sqrt{b}} = \frac{c(a - \sqrt{b})}{a^2 - b}$$

> **Contoh:**  
> Rasionalkan $\frac{4}{3 - \sqrt{5}}$:  
> *Langkah 1:* Pengali sekawan dari $3 - \sqrt{5}$ adalah $3 + \sqrt{5}$.  
> $$\frac{4}{3 - \sqrt{5}} \times \frac{3 + \sqrt{5}}{3 + \sqrt{5}} = \frac{4(3 + \sqrt{5})}{3^2 - (\sqrt{5})^2}$$  
> *Langkah 2:* Hitung penyebutnya: $3^2 = 9$ dan $(\sqrt{5})^2 = 5$, sehingga $9 - 5 = 4$.  
> $$= \frac{4(3 + \sqrt{5})}{4} = \mathbf{3 + \sqrt{5}}$$

---

### Tipe 3: Penyebut Akar Ganda ($\frac{c}{\sqrt{a} \pm \sqrt{b}}$)
Gunakan sekawan serupa untuk mengeliminasi kedua akar pada penyebut:

$$\frac{c}{\sqrt{a} + \sqrt{b}} \times \frac{\sqrt{a} - \sqrt{b}}{\sqrt{a} - \sqrt{b}} = \frac{c(\sqrt{a} - \sqrt{b})}{a - b}$$

> **Contoh:**  
> Rasionalkan $\frac{10}{\sqrt{7} - \sqrt{2}}$:  
> $$\frac{10}{\sqrt{7} - \sqrt{2}} \times \frac{\sqrt{7} + \sqrt{2}}{\sqrt{7} + \sqrt{2}} = \frac{10(\sqrt{7} + \sqrt{2})}{(\sqrt{7})^2 - (\sqrt{2})^2} = \frac{10(\sqrt{7} + \sqrt{2})}{7 - 2} = \frac{10(\sqrt{7} + \sqrt{2})}{5} = \mathbf{2(\sqrt{7} + \sqrt{2})}$$

---

## 🚨 Zona Waspada: 3 Jebakan Miskonsepsi Bentuk Akar!

> [!WARNING]
> ### Jebakan #1: Menjumlahkan Angka di Bawah Lambang Akar!
> Sifat penjumlahan akar **TIDAK SAMA** dengan sifat perkalian:
> - $\sqrt{a \times b} = \sqrt{a} \times \sqrt{b}$ ✅ (Benar)
> - $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$! ❌ (Salah besar!)
>
> **Bukti Pembantah (*Counter-example*):**  
> Ambillah $a = 9$ dan $b = 16$:  
> - Ruas Kiri: $\sqrt{9 + 16} = \sqrt{25} = \mathbf{5}$  
> - Ruas Kanan: $\sqrt{9} + \sqrt{16} = 3 + 4 = \mathbf{7}$  
> Karena $5 \neq 7$, maka $\sqrt{a+b}$ **tidak pernah boleh** dipisah jadi $\sqrt{a} + \sqrt{b}$!

> [!WARNING]
> ### Jebakan #2: Memaksakan Penjumlahan Suku Akar Tak Sejenis
> - $2\sqrt{3} + 3\sqrt{2} \neq 5\sqrt{5}$! ❌  
> Karena $\sqrt{3}$ dan $\sqrt{2}$ adalah radikan yang berbeda, bentuk tersebut sudah dalam wujud paling sederhana dan **tidak bisa digabungkan lagi**.

> [!WARNING]
> ### Jebakan #3: Lupa Mendistribusikan Tanda Negatif pada Sekawan
> Ketika mengalikan bentuk sekawan seperti $(3 - \sqrt{2})$, jangan mengubah tanda angka depan menjadi $-3 - \sqrt{2}$! Yang berubah tanda **hanya tanda operasi penghubung di tengahnya**.

---

## 💡 Contoh Soal Prosedural Lengkap

### Contoh Soal: Menghitung Luas & Diagonal Persegi Panjang
Sebuah bingkai foto berbentuk persegi panjang memiliki panjang $(3\sqrt{5} + 2)\text{ cm}$ dan lebar $(3\sqrt{5} - 2)\text{ cm}$.
a. Tentukan luas bingkai foto tersebut!  
b. Jika luasnya dibagi dengan $\sqrt{41}$, rasionalkan hasil akhirnya!

**Penyelesaian:**  
**a. Menghitung Luas:**  
$$\text{Luas} = \text{panjang} \times \text{lebar} = (3\sqrt{5} + 2)(3\sqrt{5} - 2)$$  
Bentuk ini adalah selisih kuadrat $(x+y)(x-y) = x^2 - y^2$:  
$$\text{Luas} = (3\sqrt{5})^2 - (2)^2$$  
$$(3\sqrt{5})^2 = 3^2 \times (\sqrt{5})^2 = 9 \times 5 = 45$$  
$$2^2 = 4$$  
$$\text{Luas} = 45 - 4 = \mathbf{41\text{ cm}^2}$$

**b. Merasionalkan Hasil:**  
$$\frac{\text{Luas}}{\sqrt{41}} = \frac{41}{\sqrt{41}} \times \frac{\sqrt{41}}{\sqrt{41}} = \frac{41\sqrt{41}}{41} = \mathbf{\sqrt{41}\text{ cm}}$$

---

## 🎯 Drill Kilat Uji Konsep (Active Recall)

> [!QUESTION]- Latihan 1: Penyederhanaan Akar Campuran
> Sederhanakan: $2\sqrt{12} - 3\sqrt{27} + \sqrt{75}$!
> > [!CHECK]- Jawaban & Pembahasan
> > Ubah ke bentuk $\sqrt{3}$:  
> > - $2\sqrt{12} = 2(2\sqrt{3}) = 4\sqrt{3}$  
> > - $3\sqrt{27} = 3(3\sqrt{3}) = 9\sqrt{3}$  
> > - $\sqrt{75} = 5\sqrt{3}$  
> > Maka:  
> > $$4\sqrt{3} - 9\sqrt{3} + 5\sqrt{3} = (4 - 9 + 5)\sqrt{3} = 0\sqrt{3} = \mathbf{0}$$

> [!QUESTION]- Latihan 2: Merasionalkan Pecahan Bertingkat
> Sederhanakan bentuk rasional dari $\frac{\sqrt{3}}{\sqrt{5} - \sqrt{2}}$!
> > [!CHECK]- Jawaban & Pembahasan
> > Kalikan dengan sekawan $(\sqrt{5} + \sqrt{2})$:  
> > $$\frac{\sqrt{3}(\sqrt{5} + \sqrt{2})}{(\sqrt{5} - \sqrt{2})(\sqrt{5} + \sqrt{2})} = \frac{\sqrt{15} + \sqrt{6}}{5 - 2} = \mathbf{\frac{\sqrt{15} + \sqrt{6}}{3}}$$

---

*Navigasi Pembelajaran:*  
[[Eksponen_dan_Bentuk_Akar_SMP|🏠 Master Dashboard]] | [[Bilangan_Berpangkat_dan_Sifatnya_SMP|⬅️ Modul 1: Bilangan Berpangkat]] | **Modul 2: Operasi Bentuk Akar** | [[Persamaan_Eksponen_dan_Notasi_Ilmiah_SMP|Modul 3: Persamaan Eksponen & Sains ➡️]] | [[LKPD_Eksponen_dan_Bentuk_Akar_SMP|📋 LKPD]] | [[Soal_Eksponen_dan_Bentuk_Akar_SMP|📝 Soal Evaluasi]]
