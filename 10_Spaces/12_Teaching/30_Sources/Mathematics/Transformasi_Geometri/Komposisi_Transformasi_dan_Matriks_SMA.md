---
title: "Komposisi Transformasi dan Matriks — Modul 3 Transformasi Geometri"
type: "materi"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-18
sources:
  - "[[Transformasi_Geometri_SMA]]"
  - "[[Translasi_dan_Refleksi_SMA]]"
  - "[[Rotasi_dan_Dilatasi_SMA]]"
  - "[[LKPD_Transformasi_Geometri_SMA]]"
tags:
  - "#matematika"
  - "#komposisi_transformasi"
  - "#matriks_transformasi"
  - "#luas_bayangan"
  - "#kelas11"
  - "#bahan_ajar"
---

[[Transformasi_Geometri_SMA|🏠 Master Dashboard]] | [[Rotasi_dan_Dilatasi_SMA|⬅️ Modul 2: Rotasi & Dilatasi]] | **Modul 3: Komposisi & Matriks** | [[LKPD_Transformasi_Geometri_SMA|📝 LKPD]] | [[Soal_Transformasi_Geometri_SMA|🎯 Soal Evaluasi]]

---

# Modul 3: Komposisi Transformasi & Matriks Umum 🔗🧮

## 1. Pendahuluan: Menggabungkan Berbagai Transformasi

Bagaimana jika suatu objek tidak hanya digeser, tetapi juga diputar lalu dicerminkan secara berturutan? Dalam animasi grafik komputer 3D dan pengolahan gambar digital, serangkaian pergerakan ini digabungkan menjadi satu operasi tunggal menggunakan **Komposisi Transformasi Matriks**.

Modul ini akan membahas aturan perkalian matriks untuk komposisi berturutan, sifat-sifat khusus refleksi garis ganda, teknik invers matriks untuk transformasi kurva kompleks, serta cara cepat menentukan **luas bayangan bidang datar** pasca-transformasi.

---

## 2. Komposisi Transformasi

### 2.1 Konsep & Perkalian Matriks Komposisi
Jika suatu titik $A(x,y)$ ditransformasikan oleh $T_1$ dengan matriks $M_1$, kemudian dilanjutkan oleh transformasi $T_2$ dengan matriks $M_2$, maka bentuk komposisi notasinya dilambangkan sebagai:

$$
(T_2 \circ T_1)(A)
$$

> [!WARNING]
> **Aturan Urutan Perkalian Matriks:**
> Meskipun ditulis $(T_2 \circ T_1)$, pengerjaan matriks gabungannya dilakukan dari **kanan ke kiri**!
> $$M_{\text{gabungan}} = M_2 \times M_1$$
> Maka koordinat bayangan akhir $A''(x'', y'')$ dirumuskan sebagai:
> $$\begin{pmatrix} x'' \\ y'' \end{pmatrix} = (M_2 \times M_1) \begin{pmatrix} x \\ y \end{pmatrix}$$

---

### 2.2 Sifat Komposisi Khusus

#### A. Komposisi Dua Refleksi terhadap Garis-Garis Sejajar
1. **Dua garis sejajar Sumbu $Y$ ($x = h_1$ lalu $x = h_2$):**
   Hasilnya sama dengan **Translasi** searah Sumbu $X$ sebesar:
   $$T = \begin{pmatrix} 2(h_2 - h_1) \\ 0 \end{pmatrix}$$
2. **Dua garis sejajar Sumbu $X$ ($y = k_1$ lalu $y = k_2$):**
   Hasilnya sama dengan **Translasi** searah Sumbu $Y$ sebesar:
   $$T = \begin{pmatrix} 0 \\ 2(k_2 - k_1) \end{pmatrix}$$

#### B. Komposisi Dua Refleksi terhadap Garis Saling Tegak Lurus
Jika dua garis cermin $x = h$ dan $y = k$ saling tegak lurus berpotongan di titik $(h, k)$, maka komposisi refleksi berturut-turut ekivalen dengan **Rotasi $180^\circ$** yang berpusat di titik potong $(h, k)$!

---

#### 💡 Contoh Soal 1 (Komposisi Matriks):
Tentukan bayangan titik $P(2, -4)$ oleh pencerminan terhadap sumbu $Y$ dilanjutkan dengan rotasi $90^\circ$ berlawanan arah jarum jam terhadap pusat $O(0,0)$!

**Pembahasan:**
1. Transformasi pertama $T_1$ (Refleksi Sumbu $Y$):
   $$M_1 = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$$
2. Transformasi kedua $T_2$ (Rotasi $+90^\circ$):
   $$M_2 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
3. Hitung Matriks Gabungan $M = M_2 \times M_1$:
   $$M = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$$
4. Hitung bayangan koordinat $P'$:
   $$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} \begin{pmatrix} 2 \\ -4 \end{pmatrix} = \begin{pmatrix} 4 \\ -2 \end{pmatrix}$$
Jadi, bayangan akhirnya adalah **$P'(4, -2)$**.

---

## 3. Transformasi Menggunakan Matriks Umum & Invers

Suatu transformasi geometri dapat diwakili oleh matriks persegi berordo $2 \times 2$ sembarang $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$

Jika kita ingin mencari koordinat awal $(x,y)$ dari koordinat bayangan $(x', y')$, kita dapat menggunakan **Invers Matriks**:

$$
\begin{pmatrix} x \\ y \end{pmatrix} = M^{-1} \begin{pmatrix} x' \\ y' \end{pmatrix} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \begin{pmatrix} x' \\ y' \end{pmatrix}
$$

---

## 4. Luas Bayangan Bangun Datar Pasca-Transformasi

Ketika sebuah bangun datar (seperti segitiga, persegi panjang, atau lingkaran) ditransformasikan oleh matriks $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, luas bidang bangun datar tersebut akan berubah secara rasional sebanding dengan nilai **determinan matriks transformasinya**.

$$
\text{Luas Bayangan } (L') = |\det(M)| \times \text{Luas Awal } (L)
$$

dengan:
$$\det(M) = ad - bc$$

> **Catatan Penting:**
> * Untuk **Translasi, Refleksi, dan Rotasi**, nilai $|\det(M)| = 1$, sehingga **luas tidak berubah** ($L' = L$).
> * Untuk **Dilatasi** dengan faktor skala $k$, matriksnya $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$, sehingga $\det(M) = k^2$. Luas bayangannya menjadi **$L' = k^2 \times L$**.

---

#### 💡 Contoh Soal 2 (Luas Bayangan Segitiga):
Diketahui segitiga $ABC$ dengan koordinat $A(1, 1)$, $B(5, 1)$, dan $C(1, 4)$. Segitiga tersebut ditransformasikan oleh matriks $M = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$. Tentukan luas bayangan segitiga $A'B'C'$!

**Pembahasan:**
1. Hitung Luas Awal Segitiga $ABC$ ($L$):
   Segitiga $ABC$ merupakan segitiga siku-siku dengan alas $ab = 5 - 1 = 4$ dan tinggi $t = 4 - 1 = 3$.
   $$L = \frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times 4 \times 3 = 6 \text{ satuan luas}$$

2. Hitung Determinan Matriks $M$:
   $$\det(M) = (3)(4) - (1)(2) = 12 - 2 = 10$$

3. Hitung Luas Bayangan Segitiga $A'B'C'$ ($L'$):
   $$L' = |\det(M)| \times L = 10 \times 6 = 60 \text{ satuan luas}$$

Jadi, luas bayangan segitiga $A'B'C'$ adalah **$60$ satuan luas**.

---

## 5. Rangkuman & Checklist Penguasaan Modul 3

> [!NOTE]
> * **Ingat Urutan:** Komposisi $(T_2 \circ T_1)$ artinya jalankan $T_1$ dulu, baru $T_2$. Matriksnya dikalikan $M_2 \times M_1$.
> * **Dua Garis Sejajar:** Refleksi berurutan terhadap garis $x=h_1$ lalu $x=h_2$ sama dengan translasi sejauh $2(h_2 - h_1)$.
> * **Determinan Matriks = Faktor Pengkali Luas:** Gunakan rumus $L' = |\det(M)| \times L$ untuk menyelesaikan soal luas bayangan secara cepat tanpa perlu mencari koordinat titik satu per satu.

---

[[Transformasi_Geometri_SMA|🏠 Master Dashboard]] | [[Rotasi_dan_Dilatasi_SMA|⬅️ Modul 2: Rotasi & Dilatasi]] | **Modul 3: Komposisi & Matriks** | [[LKPD_Transformasi_Geometri_SMA|📝 LKPD]] | [[Soal_Transformasi_Geometri_SMA|🎯 Soal Evaluasi]]
