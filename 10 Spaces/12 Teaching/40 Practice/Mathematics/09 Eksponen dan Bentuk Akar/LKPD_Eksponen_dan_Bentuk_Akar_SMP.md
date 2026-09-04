---
title: "LKPD: Eksponen dan Bentuk Akar — Eksplorasi Konsep & Penalaran Kritis"
type: lkpd
subject: mathematics
level: smp
target_audience: "SMP Kelas VIII & IX (Fase D)"
created: 2026-09-04
sources:
  - "[[Eksponen_dan_Bentuk_Akar_SMP]]"
  - "[[Bilangan_Berpangkat_dan_Sifatnya_SMP]]"
  - "[[Operasi_Bentuk_Akar_dan_Merasionalkan_SMP]]"
  - "[[Persamaan_Eksponen_dan_Notasi_Ilmiah_SMP]]"
tags:
  - teaching/lkpd
  - matematika
  - eksponen
  - bentuk-akar
  - smp-kelas-8
  - smp-kelas-9
---

*Bilah Navigasi Modul:*  
[[Eksponen_dan_Bentuk_Akar_SMP|🏠 Master Dashboard]] | [[Bilangan_Berpangkat_dan_Sifatnya_SMP|Modul 1: Bilangan Berpangkat]] | [[Operasi_Bentuk_Akar_dan_Merasionalkan_SMP|Modul 2: Operasi Bentuk Akar]] | [[Persamaan_Eksponen_dan_Notasi_Ilmiah_SMP|Modul 3: Persamaan Eksponen & Sains]] | **📋 LKPD Siswa** | [[Soal_Eksponen_dan_Bentuk_Akar_SMP|📝 Soal Evaluasi]]

---

# Lembar Kerja Peserta Didik (LKPD): Eksponen & Bentuk Akar 📋📐

### 👥 Identitas Belajar Kelompok:
- **Nama Kelompok:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- **Kelas / Semester:** VIII / IX — Genap (Fase D)
- **Anggota Kelompok:**
  1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Ketua Tim)
  2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  3. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  4. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- **Alokasi Waktu:** $2 \times 40\text{ Menit}$ (Pertemuan Kolaboratif)

---

## 🎯 Tujuan Pembelajaran:
1. Menemukan sendiri konsep bilangan berpangkat, pangkat nol ($a^0=1$), dan pangkat negatif ($a^{-n} = \frac{1}{a^n}$) melalui simulasi lipatan fisik.
2. Menganalisis dan mengoreksi miskonsepsi umum aljabar eksponen dan bentuk akar.
3. Mengaplikasikan operasi bentuk akar dan teknik merasionalkan penyebut pada masalah geometri kontekstual.
4. Menyelesaikan persoalan sains kontekstual menggunakan notasi ilmiah dan persamaan eksponen.

---

## 🛠️ Petunjuk Kerja:
1. Siapkan selembar kertas HVS ukuran A4, penggaris, dan alat tulis.
2. Diskusikan setiap instruksi bersama anggota kelompok secara aktif.
3. Isilah kotak jawaban yang telah disediakan secara rapi dan sistematis.
4. Jika mengalami kebuntuan, periksa kembali [[Eksponen_dan_Bentuk_Akar_SMP|Master Dashboard]] atau modul terkait!

---

## 🧪 Aktivitas 1: Laboratorium Lipat Kertas & Menemukan Pola Pangkat

### Langkah Eksperimen:
1. Ambil selembar kertas HVS utuh. Pada kondisi belum dilipat sama sekali ($0$ kali lipatan), ada berapa bidang persegi panjang yang terlihat? Tentu **1 bidang**.
2. Lipat kertas tersebut tepat di tengah menjadi dua bagian sama besar. Buka lipatan, hitung ada berapa bidang yang terbentuk.
3. Lakukan kembali pelipatan kedua, ketiga, hingga keempat. Catat hasilnya pada tabel di bawah ini!

### Tabel Pengamatan:

| Jumlah Lipatan ($n$) | Ilustrasi Perkalian Berulang | Banyak Bidang Terbentuk ($N$) | Bentuk Eksponen ($2^n$) |
| :---: | :--- | :---: | :---: |
| **0** (Kertas Utuh) | Tidak ada lipatan | $1$ | $2^0 = 1$ |
| **1** | $2$ | $2$ | $2^1$ |
| **2** | $2 \times 2$ | $4$ | $2^2$ |
| **3** | $2 \times 2 \times 2$ | \_\_\_\_\_ | $2^{\dots}$ |
| **4** | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_ | $2^{\dots}$ |
| **$n$** | $\underbrace{2 \times 2 \times \dots \times 2}_{n\text{ faktor}}$ | \_\_\_\_\_ | $2^n$ |

---

### Diskusi Penalaran Kritis 1:
Perhatikan pola pembagian mundur berikut untuk membuktikan nilai pangkat nol dan negatif:
- Dari baris ke-4 ke baris ke-3: $2^4 \div 2 = 2^3$ ($16 \div 2 = 8$).
- Dari baris ke-3 ke baris ke-2: $2^3 \div 2 = 2^2$ ($8 \div 2 = 4$).
- Dari baris ke-2 ke baris ke-1: $2^2 \div 2 = 2^1$ ($4 \div 2 = 2$).
- Dari baris ke-1 ke baris ke-0: $2^1 \div 2 = 2^0$ ($2 \div 2 = \dots\dots$).

> **Pertanyaan Analisis:**  
> Berdasarkan keteraturan pola di atas, jelaskan dengan kalimat kelompokmu sendiri:  
> 1. Mengapa nilai $2^0$ harus sama dengan $1$?  
>    *Jawaban Kelompok:*  
>    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
> 2. Jika pola pembagian dengan $2$ dilanjutkan satu langkah lagi ke bawah nol:  
>    $2^0 \div 2 = 2^{0-1} = 2^{-1} \implies 1 \div 2 = \frac{1}{2^1} = \frac{1}{2}$.  
>    Bagaimanakah bentuk pecahan biasa dari $2^{-3}$?  
>    *Jawaban Kelompok:*  
>    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  

---

## 🕵️‍♂️ Aktivitas 2: Detektif Miskonsepsi Aljabar

Empat siswa SMP sedang mengerjakan tugas matematika di perpustakaan, namun masing-masing melakukan kesalahan fatal. Tugas tim detektifmu adalah **menemukan kesalahan mereka**, **menjelaskan mengapa cara mereka salah**, dan **menuliskan penyelesaian yang benar**!

### Kasus A: Lembar Kerja Rian
> **Pernyataan Rian:**  
> *"Hasil dari $(-4)^2$ dan $-4^2$ itu sama saja, yaitu sama-sama bernilai $16$ karena $4 \times 4 = 16$."*

*Analisis Detektif:*
- Apakah pernyataan Rian Benar atau Salah? **[ \_\_\_\_\_\_\_\_ ]**
- Di mana letak kesalahannya?  
  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Pembetulan yang benar:  
  $(-4)^2 = \dots\dots$ sedangkan $-4^2 = \dots\dots$

---

### Kasus B: Lembar Kerja Sinta
> **Pernyataan Sinta:**  
> *"$\sqrt{16 + 9} = \sqrt{16} + \sqrt{9} = 4 + 3 = 7$."*

*Analisis Detektif:*
- Apakah cara hitung Sinta Benar atau Salah? **[ \_\_\_\_\_\_\_\_ ]**
- Buktikan mengapa langkah Sinta salah menggunakan perhitungan yang sebenarnya:  
  $\sqrt{16 + 9} = \sqrt{\dots\dots} = \dots\dots$  
- Berapa selisih hasil antara hitungan Sinta yang keliru dengan hasil matematis yang benar?  
  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Kasus C: Lembar Kerja Budi
> **Pernyataan Budi:**  
> *"Pada persamaan $2 \times 3^x = 18$, kita kalikan dulu angka $2$ dengan $3$, sehingga menjadi $6^x = 18$."*

*Analisis Detektif:*
- Mengapa Budi melanggar aturan urutan operasi hitung matematika (*PEMDAS*)?  
  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Tuliskan langkah penyelesaian yang benar untuk menemukan nilai $x$:  
  $$2 \times 3^x = 18 \implies 3^x = \frac{\dots\dots}{\dots\dots} \implies 3^x = \dots\dots \implies x = \dots\dots$$

---

## 📐 Aktivitas 3: Ekspedisi Arsitek & Merasionalkan Bentuk Akar

Sebuah kelompok arsitek cilik sedang merancang fasad kanopi rumah berbentuk segitiga siku-siku dengan spesifikasi sebagai berikut:
- Panjang sisi alas ($a$): $(4 + \sqrt{3})\text{ meter}$
- Panjang sisi tegak ($b$): $(4 - \sqrt{3})\text{ meter}$

```
       |\
       | \
 b     |  \  c (Hipotenusa)
       |   \
       |____\
         a
```

### Pertanyaan Proyek:
1. **Hitung Luas Penampang Kanopi:**  
   Formula: $\text{Luas} = \frac{1}{2} \times \text{alas} \times \text{tinggi}$  
   Tunjukkan proses perkalian aljabar bentuk sekawannya secara lengkap!  
   *Penyelesaian:*  
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
   $$\text{Luas} = \dots\dots\dots\text{ m}^2$$

2. **Merasionalkan Rasio Beban Angin:**  
   Insinyur struktur menetapkan indeks kestabilan kanopi tersebut memenuhi rumus pecahan:  
   $$K = \frac{10}{\sqrt{7} - \sqrt{2}}$$  
   Bantulah arsitek merasionalkan penyebut pecahan tersebut hingga diperoleh bentuk aljabar tanpa akar pada penyebut!  
   *Penyelesaian Langkah demi Langkah:*  
   $$\frac{10}{\sqrt{7} - \sqrt{2}} \times \frac{\dots\dots\dots\dots}{\dots\dots\dots\dots} = \frac{\dots\dots\dots\dots}{\dots\dots\dots\dots} = \dots\dots\dots\dots$$

---

## 🚀 Aktivitas 4: Misi Sains Antariksa & Nanoteknologi

### Skenario Misi:
Stasiun Luar Angkasa Internasional (ISS) mencatat dua data penting dalam misi eksplorasi:
1. **Jarak Satelit Cuaca ke Pusat Pemancar Bumi:** $36.000.000\text{ meter}$.
2. **Ketebalan Lapisan Pelindung Radiasi Nanomaterial:** $0{,}000000045\text{ meter}$.

### Tugas Analisis Data:
1. Nyatakan kedua besaran fisika di atas ke dalam format **Notasi Ilmiah (Bentuk Baku)** yang valid ($a \times 10^n$, dengan $1 \le a < 10$):
   - Jarak Satelit: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ $\text{meter}$
   - Ketebalan Pelindung Radiasi: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ $\text{meter}$

2. Jika sebuah partikel debu antariksa berdiameter $1{,}5 \times 10^{-7}\text{ meter}$ melintas, berapa kali lipat ketebalan lapisan pelindung radiasi dibandingkan dengan diameter partikel debu tersebut?  
   *Hitung pembagian notasi ilmiah:*  
   $$\text{Rasio} = \frac{4{,}5 \times 10^{-8}}{1{,}5 \times 10^{-7}} = \left(\frac{4{,}5}{1{,}5}\right) \times 10^{(-8) - (-7)} = \dots\dots\dots\dots$$  
   *Kesimpulan:* \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## 📝 Lembar Refleksi Diri & Penilaian Diri

Beri tanda centang ($\checkmark$) pada kolom yang paling menggambarkan pemahaman tim kamu:

| Indikator Capaian Belajar | 🌟 Sangat Paham | 👍 Cukup Paham | 🔄 Perlu Bimbingan |
| :--- | :---: | :---: | :---: |
| 1. Menjelaskan mengapa $a^0=1$ dan $a^{-n}=\frac{1}{a^n}$ | | | |
| 2. Membedakan tanda negatif kurung $(-a)^n$ vs $-a^n$ | | | |
| 3. Menyederhanakan dan mengoperasikan bentuk akar sejenis | | | |
| 4. Merasionalkan penyebut bentuk tunggal dan sekawan | | | |
| 5. Mengubah data numerik ke bentuk notasi ilmiah yang valid | | | |

> **Pesan Refleksi Tim:**  
> Bagian mana yang paling menantang dan menyenangkan dari aktivitas LKPD hari ini?  
> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---
*Navigasi Pembelajaran:*  
[[Eksponen_dan_Bentuk_Akar_SMP|🏠 Master Dashboard]] | [[Bilangan_Berpangkat_dan_Sifatnya_SMP|Modul 1: Bilangan Berpangkat]] | [[Operasi_Bentuk_Akar_dan_Merasionalkan_SMP|Modul 2: Operasi Bentuk Akar]] | [[Persamaan_Eksponen_dan_Notasi_Ilmiah_SMP|Modul 3: Persamaan Eksponen & Sains]] | **📋 LKPD Siswa** | [[Soal_Eksponen_dan_Bentuk_Akar_SMP|📝 Soal Evaluasi]]
