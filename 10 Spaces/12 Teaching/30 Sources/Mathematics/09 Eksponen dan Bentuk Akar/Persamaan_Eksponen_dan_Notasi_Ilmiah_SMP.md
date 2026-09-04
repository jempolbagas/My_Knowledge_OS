---
title: "Persamaan Eksponen dan Notasi Ilmiah — Dari Aljabar Presisi ke Skala Alam Semesta"
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
  - persamaan-eksponen
  - notasi-ilmiah
  - bentuk-baku
  - smp-kelas-8
  - smp-kelas-9
---

*Navigasi Cepat:*  
[[Eksponen_dan_Bentuk_Akar_SMP|🏠 Master Dashboard]] | [[Bilangan_Berpangkat_dan_Sifatnya_SMP|Modul 1: Bilangan Berpangkat]] | [[Operasi_Bentuk_Akar_dan_Merasionalkan_SMP|⬅️ Modul 2: Operasi Bentuk Akar]] | **Modul 3: Persamaan Eksponen & Sains** | [[LKPD_Eksponen_dan_Bentuk_Akar_SMP|📋 LKPD]] | [[Soal_Eksponen_dan_Bentuk_Akar_SMP|📝 Soal Evaluasi]]

---

# Persamaan Eksponen & Notasi Ilmiah — Dari Aljabar Presisi ke Skala Alam Semesta! 🌌🔬

Pernahkah kamu memikirkan bagaimana cara ilmuwan mencatat massa planet Bumi yang beratnya mencapai sekitar:
$$5.972.000.000.000.000.000.000.000\text{ kg}$$
Atau bagaimana ahli virologi mengukur diameter virus korona yang panjangnya hanya:
$$0{,}000000125\text{ meter}$$

Jika para ilmuwan harus menuliskan seluruh deretan angka nol tersebut di laporan penelitian mereka, kalkulator ilmiah akan kehabisan layar dan kesalahan pencatatan nol akan sering terjadi!

Di sinilah matematika menghadirkan dua instrumen cerdas:
1. **Persamaan Eksponen:** Teknik aljabar untuk memecahkan nilai rahasia yang tersembunyi di posisi pangkat.
2. **Notasi Ilmiah (Bentuk Baku):** Bahasa internasional sains untuk meringkas angka raksasa alam semesta (*makrokosmos*) hingga partikel terkecil kehidupan (*mikrokosmos*).

---

## 1. Persamaan Eksponen Sederhana untuk Siswa SMP 🔐

**Persamaan Eksponen** adalah persamaan matematika yang variabel pencarinya (biasanya huruf $x$) berada di bagian **pangkat**.

### Prinsip Utama Penyetaraan Basis:
Jika bilangan pokok (basis) di kedua ruas sudah sama persis, maka nilai pangkatnya **wajib sama**!

$$a^{f(x)} = a^p \iff f(x) = p \quad (a > 0, a \neq 1)$$

> **Legenda:**
> - $a$ = Bilangan pokok (basis), harus bilangan positif dan bukan $1$.
> - $f(x)$ = Fungsi aljabar yang memuat variabel $x$ pada pangkat.
> - $p$ = Nilai eksponen di ruas lainnya.

---

### Strategi 3 Langkah Menaklukkan Persamaan Eksponen:
1. **Ubah Semua Angka ke Basis Prima Terkecil:** Faktorkan angka-angka komposit menjadi basis prima (misal: $4 \to 2^2$, $8 \to 2^3$, $9 \to 3^2$, $27 \to 3^3$, $25 \to 5^2$, $125 \to 5^3$).
2. **Gunakan Sifat Eksponen:** Manfaatkan aturan $(a^m)^n = a^{mn}$, $a^{-n} = \frac{1}{a^n}$, dan $\sqrt[n]{a^m} = a^{\frac{m}{n}}$ agar masing-masing ruas hanya memiliki **satu bilangan basis tunggal**.
3. **Coret Basis & Samakan Pangkat:** Selesaikan persamaan linear satu variabel yang tersisa.

---

### Contoh Prosedur Pemecahan Kasus:

#### Kasus A: Basis Langsung Sama / Sederhana
Tentukan nilai $x$ dari:  
$$2^{3x - 1} = 32$$

**Penyelesaian:**  
- Ruas kanan: $32 = 2^5$.  
- Persamaan menjadi:  
  $$2^{3x - 1} = 2^5$$  
- Karena basisnya sama-sama $2$, samakan eksponennya:  
  $$3x - 1 = 5 \implies 3x = 6 \implies \mathbf{x = 2}$$

---

#### Kasus B: Kedua Ruas Perlu Difaktorkan ke Basis Prima
Tentukan nilai $x$ dari:  
$$9^{x + 2} = 27^{x - 1}$$

**Penyelesaian:**  
- Angka $9$ dan $27$ merupakan kelipatan pangkat dari basis prima $3$:  
  $9 = 3^2$ dan $27 = 3^3$.  
- Substitusikan ke dalam persamaan:  
  $$(3^2)^{x + 2} = (3^3)^{x - 1}$$  
- Kalikan eksponen luar dengan eksponen dalam:  
  $$3^{2(x + 2)} = 3^{3(x - 1)} \implies 3^{2x + 4} = 3^{3x - 3}$$  
- Samakan eksponen kedua ruas:  
  $$2x + 4 = 3x - 3$$  
  $$4 + 3 = 3x - 2x \implies \mathbf{x = 7}$$

---

#### Kasus C: Menggabungkan Bentuk Akar & Pecahan (Level Standar Ujian)
Tentukan nilai $x$ yang memenuhi persamaan:  
$$\sqrt{4^{x + 3}} = \left(\frac{1}{8}\right)^{x - 1}$$

**Penyelesaian:**  
- Samakan seluruh elemen ke basis prima $2$:  
  - Ruas Kiri: $4 = 2^2 \implies \sqrt{4^{x+3}} = \sqrt{(2^2)^{x+3}} = \sqrt{2^{2x+6}} = 2^{\frac{2x+6}{2}} = 2^{x+3}$.  
  - Ruas Kanan: $\frac{1}{8} = 8^{-1} = (2^3)^{-1} = 2^{-3}$.  
    Maka $\left(\frac{1}{8}\right)^{x - 1} = (2^{-3})^{x - 1} = 2^{-3(x - 1)} = 2^{-3x + 3}$.  
- Setarakan kedua ruas:  
  $$2^{x + 3} = 2^{-3x + 3}$$  
- Samakan eksponennya:  
  $$x + 3 = -3x + 3$$  
  $$x + 3x = 3 - 3 \implies 4x = 0 \implies \mathbf{x = 0}$$

---

## 2. Notasi Ilmiah (Bentuk Baku) 🪐🔬

**Notasi Ilmiah** adalah cara penulisan standar internasional untuk menyajikan bilangan yang nilainya sangat besar atau sangat kecil secara ringkas dan presisi.

### Format Baku:

$$a \times 10^n$$

> **Syarat Mutlak Penulisan:**
> 1. **Nilai $a$ (Mantissa / Angka Signifikan):**  
>    Wajib memenuhi rentang:  
>    $$1 \le a < 10$$  
>    *(Artinya, angka di depan tanda koma hanya boleh terdiri dari **satu digit bukan nol**, yaitu $1, 2, 3, 4, 5, 6, 7, 8,$ atau $9$)*.
> 2. **Nilai $n$ (Orde Pangkat / Eksponen Basis 10):**  
>    Wajib berupa **bilangan bulat** ($n \in \mathbb{Z}$).

---

### Prosedur Mengubah Bilangan ke Bentuk Baku:

#### 1. Bilangan Bernilai Sangat Besar ($\ge 10$): Pangkat $n$ Bernilai Positif ($+$)
- Tarik tanda koma desimal ke arah **kiri** hingga tersisa satu angka di depan koma.
- Jumlah pergeseran koma menjadi nilai pangkat positif ($+n$).

> **Contoh:**  
> - Jarak rata-rata Bumi ke Matahari:  
>   $$149.600.000\text{ km} = 1{,}49600000 \times 10^8 = \mathbf{1{,}496 \times 10^8\text{ km}}$$  
>   *(Koma digeser ke kiri sebanyak 8 langkah)*.
> - Kecepatan rambat cahaya di ruang hampa:  
>   $$300.000.000\text{ m/s} = \mathbf{3 \times 10^8\text{ m/s}}$$  
>   *(Koma digeser ke kiri sebanyak 8 langkah)*.

---

#### 2. Bilangan Desimal Sangat Kecil ($0 < x < 1$): Pangkat $n$ Bernilai Negatif ($-$)
- Tarik tanda koma desimal ke arah **kanan** hingga melewati angka bukan nol pertama.
- Jumlah pergeseran koma menjadi nilai pangkat negatif ($-n$).

> **Contoh:**  
> - Ukuran bakteri *E. coli*:  
>   $$0{,}000002\text{ meter} = \mathbf{2 \times 10^{-6}\text{ meter}}$$  
>   *(Koma digeser ke kanan sebanyak 6 langkah)*.
> - Massa setetes air mikroskopis:  
>   $$0{,}0000456\text{ gram} = \mathbf{4{,}56 \times 10^{-5}\text{ gram}}$$  
>   *(Koma digeser ke kanan sebanyak 5 langkah)*.

---

## 3. Operasi Aljabar pada Notasi Ilmiah 🧮

### A. Perkalian & Pembagian Notasi Ilmiah
Kelompokkan bilangan desimal dengan desimal, dan bilangan basis $10$ dengan basis $10$ menggunakan sifat eksponen:

$$(a \times 10^m) \times (b \times 10^n) = (a \times b) \times 10^{m+n}$$

> [!IMPORTANT]
> **Langkah Penyesuaian Mantissa:**  
> Jika hasil perkalian $(a \times b) \ge 10$, ubah kembali ke format baku $1 \le a < 10$ dengan menambah pangkat sepuluhnya!

**Contoh Soal Perkalian:**  
Hitung: $(4 \times 10^5) \times (5 \times 10^7)$  
$$= (4 \times 5) \times (10^5 \times 10^7) = 20 \times 10^{5+7} = 20 \times 10^{12}$$  
Karena $20 \ge 10$, jadikan bentuk baku:  
$$20 = 2 \times 10^1 \implies 2 \times 10^1 \times 10^{12} = \mathbf{2 \times 10^{13}}$$

**Contoh Soal Pembagian:**  
Hitung: $\frac{7{,}2 \times 10^9}{1{,}8 \times 10^4}$  
$$= \left(\frac{7{,}2}{1{,}8}\right) \times 10^{9 - 4} = \mathbf{4 \times 10^5}$$

---

### B. Penjumlahan & Pengurangan Notasi Ilmiah
Kamu **tidak boleh** langsung menjumlahkan angka desimalnya sebelum pangkat $10$-nya disamakan terlebih dahulu!

**Contoh Soal Penjumlahan:**  
Hitung: $(3{,}2 \times 10^4) + (5 \times 10^3)$  
- Samakan kedua suku ke pangkat terbesar, yaitu $10^4$:  
  $5 \times 10^3 = 0{,}5 \times 10^4$.  
- Faktorkan $10^4$ keluar:  
  $$= (3{,}2 + 0{,}5) \times 10^4 = \mathbf{3{,}7 \times 10^4}$$

---

## 🚨 Zona Waspada: 3 Jebakan Miskonsepsi Fatal!

> [!WARNING]
> ### Jebakan #1: Mengira $25 \times 10^6$ atau $0{,}45 \times 10^{-3}$ adalah Bentuk Baku
> Ingat syarat emas: angka di depan koma **harus berada di antara 1 dan 10**!
> - $25 \times 10^6$ ❌ $\implies$ Bentuk baku: $\mathbf{2{,}5 \times 10^7}$ ✅
> - $0{,}45 \times 10^{-3}$ ❌ $\implies$ Bentuk baku: $\mathbf{4{,}5 \times 10^{-4}}$ ✅

> [!WARNING]
> ### Jebakan #2: Mengalikan Koefisien dengan Basis Persamaan Eksponen
> Jangan pernah mengalikan angka luar dengan basis eksponen!
> $$2 \times 3^x \neq 6^x \quad \text{❌ (Salah Fatal!)}$$  
> Berdasarkan aturan urutan operasi hitung (*Order of Operations / PEMDAS*), operasi pemangkatan wajib dievaluasi lebih dulu sebelum operasi perkalian.

> [!WARNING]
> ### Jebakan #3: Tertukar Arah Tanda Pangkat pada Pergeseran Koma Desimal
> - Menggeser koma ke **kiri** $\to$ pangkat bertambah positif ($+$).  
> - Menggeser koma ke **kanan** $\to$ pangkat bertambah negatif ($-$).

---

## 💡 Contoh Soal Kontekstual Sains (HOTS)

### Studi Kasus: Populasi Bakteri dan Transmisi Data
Sebuah laboratorium virologi meneliti sampel bakteri yang membelah diri menjadi 2 setiap 15 menit. Awalnya terdapat 500 bakteri dalam wadah kultur.
a. Nyatakan jumlah bakteri setelah 2 jam dalam bentuk persamaan perpangkatan!  
b. Hitung jumlah akhir bakteri tersebut dan nyatakan dalam notasi ilmiah!

**Penyelesaian:**  
**a. Memodelkan Pertumbuhan Eksponen:**  
- Durasi waktu: $2\text{ jam} = 120\text{ menit}$.  
- Banyaknya periode pembelahan ($n$):  
  $$n = \frac{120\text{ menit}}{15\text{ menit}} = 8\text{ periode}$$  
- Jumlah akhir ($P_t$):  
  $$P_t = P_0 \times 2^n = 500 \times 2^8$$

**b. Menghitung & Mengubah ke Notasi Ilmiah:**  
- Nilai $2^8 = 256$.  
- Total bakteri:  
  $$P_t = 500 \times 256 = 128.000\text{ bakteri}$$  
- Ubah ke bentuk baku (geser koma 5 kali ke kiri):  
  $$128.000 = \mathbf{1{,}28 \times 10^5\text{ bakteri}}$$

---

## 🎯 Drill Kilat Uji Konsep (Active Recall)

> [!QUESTION]- Latihan 1: Persamaan Eksponen Pecahan
> Tentukan nilai $x$ jika $3^{2x - 3} = \frac{1}{27}$!
> > [!CHECK]- Jawaban & Pembahasan
> > Ubah $\frac{1}{27}$ ke basis $3$:  
> > $\frac{1}{27} = \frac{1}{3^3} = 3^{-3}$.  
> > Maka:  
> > $$3^{2x - 3} = 3^{-3} \implies 2x - 3 = -3 \implies 2x = 0 \implies \mathbf{x = 0}$$

> [!QUESTION]- Latihan 2: Bentuk Baku Desimal Sangat Kecil
> Tuliskan $0{,}00000705$ ke dalam notasi ilmiah!
> > [!CHECK]- Jawaban & Pembahasan
> > Geser koma desimal ke kanan sampai di belakang angka 7 (melewati 6 digit nol dan angka 7):  
> > $$0{,}00000705 = \mathbf{7{,}05 \times 10^{-6}}$$

---

*Navigasi Pembelajaran:*  
[[Eksponen_dan_Bentuk_Akar_SMP|🏠 Master Dashboard]] | [[Bilangan_Berpangkat_dan_Sifatnya_SMP|Modul 1: Bilangan Berpangkat]] | [[Operasi_Bentuk_Akar_dan_Merasionalkan_SMP|⬅️ Modul 2: Operasi Bentuk Akar]] | **Modul 3: Persamaan Eksponen & Sains** | [[LKPD_Eksponen_dan_Bentuk_Akar_SMP|📋 LKPD]] | [[Soal_Eksponen_dan_Bentuk_Akar_SMP|📝 Soal Evaluasi]]
