---
title: "LKPD: Transformasi Geometri — Eksplorasi Pergeseran, Pemutaran, & Matriks Ruang"
type: "lkpd"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-18
sources:
  - "[[Transformasi_Geometri_SMA]]"
  - "[[Translasi_dan_Refleksi_SMA]]"
  - "[[Rotasi_dan_Dilatasi_SMA]]"
  - "[[Komposisi_Transformasi_dan_Matriks_SMA]]"
tags:
  - "#matematika"
  - "#lkpd"
  - "#transformasi_geometri"
  - "#kelas11"
  - "#aktivitas_kelompok"
---

[[Transformasi_Geometri_SMA|🏠 Master Dashboard]] | [[Translasi_dan_Refleksi_SMA|Modul 1]] | [[Rotasi_dan_Dilatasi_SMA|Modul 2]] | [[Komposisi_Transformasi_dan_Matriks_SMA|Modul 3]] | [[Soal_Transformasi_Geometri_SMA|🎯 Soal Evaluasi]]

---

# Lembar Kerja Peserta Didik (LKPD): Transformasi Geometri 📝✨

**Nama Kelompok:** ___________________________  
**Anggota Kelompok:**  
1. __________________________________ (Ketua)  
2. __________________________________  
3. __________________________________  
4. __________________________________  
**Kelas / Semester:** XI / Genap  
**Alokasi Waktu:** $2 \times 45$ Menit  

---

## 🎯 Petunjuk & Tujuan Pembelajaran

### Petunjuk Pengisian:
1. Bacalah setiap petunjuk aktivitas dan studi kasus dengan cermat bersama anggota kelompokmu.
2. Manfaatkan [[Transformasi_Geometri_SMA|Cheatsheet Master Dashboard]] serta Modul 1, 2, dan 3 sebagai bahan acuan referensi.
3. Kerjakan setiap tantangan secara berdiskusi dan tuliskan langkah aljabar matriksmu secara rapi.

---

## 🧩 Aktivitas 1: Eksplorasi Pergerakan Hero Game (Translasi & Refleksi)

### Konteks Kasus:
Dalam sebuah game arena pertarungan online, seorang hero bernama **Zilong** berada di koordinat awal $A(-4, 3)$. 
1. Zilong menggunakan skill pergeseran instan (translasi) $T_1 = \begin{pmatrix} 6 \\ 2 \end{pmatrix}$.
2. Setelah itu, musuh melontarkan mantra cermin bayangan yang mencerminkan posisi Zilong terhadap garis $y = x$.

```
    [Koordinat Awal Zilong: A(-4, 3)]
                    │
                    ▼  (Translasi T1 = [6, 2]^T)
    [Koordinat Posisi Ke-2: A'(..., ...)]
                    │
                    ▼  (Refleksi terhadap garis y = x)
    [Koordinat Akhir Bayangan: A''(..., ...)]
```

### Pertanyaan & Tugas Diskusi:
1. **Langkah 1 (Translasi):** Tentukan koordinat titik $A'$ setelah dikena translasi $T_1$!
   $$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} -4 \\ 3 \end{pmatrix} + \begin{pmatrix} 6 \\ 2 \end{pmatrix} = \begin{pmatrix} \dots \\ \dots \end{pmatrix}$$

2. **Langkah 2 (Refleksi):** Tentukan koordinat posisi akhir $A''$ setelah dicerminkan terhadap garis $y = x$!
   $$\begin{pmatrix} x'' \\ y'' \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \dots \\ \dots \end{pmatrix}$$

3. **Diskusi Penalaran:** Apakah jika urutan dibalik (Refleksi garis $y=x$ terlebih dahulu baru Translasi $T_1$) akan menghasilkan posisi akhir yang sama? Buktikan dengan matriks!

---

## 🔍 Aktivitas 2: Matriks Rotasi Bianglala & Zoom Digital (Rotasi & Dilatasi)

### Matriks Komparasi Transformasi:
Lengkapilah matriks komparasi transformasi dasar di bawah ini untuk membantu investigasimu:

| Jenis Transformasi | Pusat / Acuan | Parameter | Matriks Transformasi $M$ | Hubungan $(x', y')$ |
| :--- | :--- | :---: | :---: | :--- |
| **Rotasi $+90^\circ$** | Pusat $O(0,0)$ | $\theta = 90^\circ$ | $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | $x' = -y, \quad y' = x$ |
| **Rotasi $+180^\circ$** | Pusat $O(0,0)$ | $\theta = 180^\circ$ | $\begin{pmatrix} \dots & \dots \\ \dots & \dots \end{pmatrix}$ | $x' = \dots, \quad y' = \dots$ |
| **Dilatasi Skala $k$** | Pusat $O(0,0)$ | Faktor $k$ | $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ | $x' = kx, \quad y' = ky$ |
| **Dilatasi Skala $k$** | Pusat $P(a,b)$ | Faktor $k$, $(a,b)$ | Non-tunggal | $x' = k(x-a)+a, \quad y' = \dots$ |

---

### Studi Kasus Zoom Logo Vektor:
Sebuah logo berbentuk segitiga dengan titik sudut $P(1, 2)$, $Q(4, 2)$, dan $R(1, 6)$ diperbesar oleh desainer grafis menggunakan fitur zoom dengan pusat skala di $P(1, 2)$ dan faktor skala $k = 3$.

1. Hitung koordinat bayangan akhir $P', Q', R'$!
   $$\begin{pmatrix} x' \\ y' \end{pmatrix} = 3 \begin{pmatrix} x - 1 \\ y - 2 \end{pmatrix} + \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
   * Titik $P'(..., ...)$
   * Titik $Q'(..., ...)$
   * Titik $R'(..., ...)$

2. **Analisis Luas:**
   * Hitung luas segitiga awal $PQR$: $L = \frac{1}{2} \times \text{alas} \times \text{tinggi} = \dots$
   * Hitung luas segitiga bayangan $P'Q'R'$: $L' = \dots$
   * Bandingkan perbandingan $\frac{L'}{L}$ dengan nilai $k^2$! Apa kesimpulan kelompokmu?

---

## 🏛️ Aktivitas 3: Detektif Arsitektur & Komposisi Matriks (HOTS)

### Kasus Desain Denah Bangunan:
Seorang arsitek sedang merancang tata letak denah taman yang memiliki persamaan batas kurva parabola $y = x^2 - 2x + 1$. Arsitek tersebut memutuskan untuk merotasi denah sebesar $180^\circ$ berpusat di $O(0,0)$, lalu merefleksikannya terhadap sumbu $Y$.

1. **Tentukan Matriks Komposisi Tunggal ($M$):**
   $$M = M_{\text{refleksi sumbu Y}} \times M_{\text{rotasi } 180^\circ}$$
   $$M = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} \dots & \dots \\ \dots & \dots \end{pmatrix}$$

2. **Identifikasi Jenis Transformasi Tunggal:**
   Matriks hasil $M$ di atas ekivalen dengan jenis transformasi tunggal apa?

3. **Persamaan Kurva Akhir:**
   Tentukan persamaan batas kurva denah taman yang baru!

---

## 🔑 Kunci Jawaban Lengkap & Rubrik Penilaian LKPD

### Kunci Jawaban Singkat Aktivitas:

* **Aktivitas 1:**
  1. $A' = (-4+6, 3+2) = (2, 5)$.
  2. $A'' = (5, 2)$ (tukar koordinat karena refleksi $y=x$).
  3. *Penarikan urutan sebaliknya:* Refleksi $y=x$ pada $A(-4,3) \to (3, -4)$. Lalu translasi $T_1(6,2) \to (3+6, -4+2) = (9, -2)$. **Hasil Berbeda!** Komposisi translasi dan refleksi umumnya tidak komutatif.

* **Aktivitas 2:**
  1. $P'(1, 2)$, $Q'(10, 2)$, $R'(1, 14)$.
  2. Luas awal $L = \frac{1}{2} \times 3 \times 4 = 6$. Luas bayangan $L' = \frac{1}{2} \times 9 \times 12 = 54$. Perbandingan $\frac{54}{6} = 9 = 3^2 = k^2$. Terbukti!

* **Aktivitas 3:**
  1. $M = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.
  2. Matriks $M$ ekivalen dengan **Refleksi terhadap Sumbu X**.
  3. $x' = x \implies x = x'$, $y' = -y \implies y = -y'$. Substitusi ke $y = x^2 - 2x + 1 \implies -y' = (x')^2 - 2x' + 1 \implies$ **$y = -x^2 + 2x - 1$**.

### Rubrik Penilaian LKPD:
* **Skor Maksimal Total:** 100
  * **Aktivitas 1 (Translasi & Refleksi):** 30 Poin
  * **Aktivitas 2 (Rotasi, Dilatasi, & Luas):** 35 Poin
  * **Aktivitas 3 (Komposisi Matriks HOTS):** 35 Poin

---

[[Transformasi_Geometri_SMA|🏠 Master Dashboard]] | [[Translasi_dan_Refleksi_SMA|Modul 1]] | [[Rotasi_dan_Dilatasi_SMA|Modul 2]] | [[Komposisi_Transformasi_dan_Matriks_SMA|Modul 3]] | [[Soal_Transformasi_Geometri_SMA|🎯 Soal Evaluasi]]
