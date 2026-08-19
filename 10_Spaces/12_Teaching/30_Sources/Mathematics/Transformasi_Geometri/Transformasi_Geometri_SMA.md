---
title: "Transformasi Geometri — Pusat Kontrol & Navigasi Modul"
type: "master-dashboard"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-18
sources:
  - "[[Translasi_dan_Refleksi_SMA]]"
  - "[[Rotasi_dan_Dilatasi_SMA]]"
  - "[[Komposisi_Transformasi_dan_Matriks_SMA]]"
  - "[[LKPD_Transformasi_Geometri_SMA]]"
  - "[[Soal_Transformasi_Geometri_SMA]]"
tags:
  - "#matematika"
  - "#transformasi_geometri"
  - "#kelas11"
  - "#bahan_ajar"
  - "#master_dashboard"
---

# Transformasi Geometri — Peta Navigasi Pergeseran & Pemutaran Ruang! 📐✨

> **Salam Eksplorasi!** Pernahkah kamu memikirkan bagaimana animasi karakter di game MOBA bergerak mulus, bagaimana aplikasi peta digital melakukan *zoom-in*, atau bagaimana filter cermin di media sosial bekerja? Semua keajaiban visual digital tersebut bergerak berdasarkan aturan **Transformasi Geometri**! Modul ini dirancang khusus untuk membantumu menguasai pergeseran, pencerminan, pemutaran, hingga perbesaran koordinat ruang dengan mudah, intuitif, dan presisi menggunakan aljabar matriks.

---

## 🗺️ Peta Ringkasan Pembelajaran

Secara umum, Transformasi Geometri dibagi menjadi empat jenis transformasi dasar ditambah komposisi gabungan matriks:

1. **Translasi (Pergeseran):** Menggeser posisi titik/bangun sejauh vektor tertentu tanpa mengubah ukuran atau bentuk.
2. **Refleksi (Pencerminan):** Memindahkan titik/bangun dengan sifat cermin datar terhadap garis/titik acuan.
3. **Rotasi (Perputaran):** Memutar titik/bangun sejauh sudut $\theta$ terhadap pusat putaran tertentu.
4. **Dilatasi (Perkalian Skala):** Memperbesar atau memperkecil ukuran titik/bangun berdasarkan faktor skala $k$.
5. **Komposisi & Matriks:** Menggabungkan beberapa transformasi sekaligus secara berturutan serta menghitung transformasi kurva dan perubahan luas.

---

## 📑 Tabel Navigasi & Modul Pembelajaran

Gunakan tabel navigasi di bawah ini untuk mengakses setiap sub-modul materi, lembar kerja peserta didik (LKPD), serta paket latihan soal evaluasi:

| No | Modul / Berkas | Sub-Bahasan Utama | Target Hasil Belajar |
| :---: | :--- | :--- | :--- |
| **01** | [[Translasi_dan_Refleksi_SMA\|Modul 1: Translasi & Refleksi]] | Vektor Pergeseran $T = \begin{pmatrix} a \\ b \end{pmatrix}$, Pencerminan Sumbu $X, Y$, Garis $y=x$, $y=-x$, Garis $x=h$, $y=k$, dan Titik Asal. | Mahir menentukan koordinat bayangan translasi dan refleksi pada titik maupun persamaan garis. |
| **02** | [[Rotasi_dan_Dilatasi_SMA\|Modul 2: Rotasi & Dilatasi]] | Rotasi Pusat $O(0,0)$ & $P(a,b)$ Sejauh Sudut $\theta$, Dilatasi Pusat $O(0,0)$ & $P(a,b)$ dengan Skala $k$. | Menguasai pemutaran dan perkalian skala koordinat serta penerapannya pada bentuk parabola/lingkaran. |
| **03** | [[Komposisi_Transformasi_dan_Matriks_SMA\|Modul 3: Komposisi & Matriks Transformasi]] | Perkalian Matriks Komposisi $M = M_2 \times M_1$, Refleksi Dua Garis Sejajar/Tegak Lurus, Transformasi Kurva $y = f(x)$, & Luas Bayangan $|\det(M)| \times L$. | Memecahkan soal kombinasi transformasi kompleks, invers kurva, dan perhitungan luas bidang datar. |
| **📝** | [[LKPD_Transformasi_Geometri_SMA\|Lembar Kerja Peserta Didik (LKPD)]] | Eksplorasi Gerak Hero Game, Investigasi Matriks Bianglala & Zoom Foto, Detektif Desain Arsitektur. | Mengasah keterampilan kolaborasi kelompok, pemecahan masalah kontekstual HOTS, dan nalar intuitif. |
| **🎯** | [[Soal_Transformasi_Geometri_SMA\|Paket Soal Evaluasi & Pembahasan]] | 10 Soal Pilihan Ganda HOTS + 5 Soal Uraian Penalaran + Kunci Jawaban & Rubrik Penilaian Lengkap. | Menguji tingkat penguasaan individu dan kesiapan menghadapi Ujian Sekolah / Asesmen Sumatif. |

---

## ⚡ Cheatsheet Quick Reference (Rumus & Matriks Ringkas)

Gunakan *cheatsheet* ringkas ini sebagai panduan cepat saat menyelesaikan soal-soal latihan:

### 1. Translasi (Pergeseran)
$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} a \\ b \end{pmatrix}
$$

### 2. Matriks Refleksi (Pencerminan)
* **Sumbu $X$ ($y=0$):** $M_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$
* **Sumbu $Y$ ($x=0$):** $M_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$
* **Garis $y = x$:** $M_{y=x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$
* **Garis $y = -x$:** $M_{y=-x} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$
* **Titik $O(0,0)$:** $M_O = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$
* **Garis $x = h$:** $(x', y') = (2h - x, y)$
* **Garis $y = k$:** $(x', y') = (x, 2k - y)$

### 3. Matriks Rotasi (Perputaran Sudut $\theta$)
* **Pusat $O(0,0)$:**
  $$
  \begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
  $$
* **Pusat $P(a,b)$:**
  $$
  \begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x - a \\ y - b \end{pmatrix} + \begin{pmatrix} a \\ b \end{pmatrix}
  $$

### 4. Matriks Dilatasi (Faktor Skala $k$)
* **Pusat $O(0,0)$:**
  $$
  \begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} kx \\ ky \end{pmatrix}
  $$
* **Pusat $P(a,b)$:**
  $$
  \begin{pmatrix} x' \\ y' \end{pmatrix} = k \begin{pmatrix} x - a \\ y - b \end{pmatrix} + \begin{pmatrix} a \\ b \end{pmatrix}
  $$

### 5. Komposisi Matriks & Perubahan Luas
* **Urutan Operasi ($T_1$ lalu $T_2$):** $M = M_2 \times M_1$
* **Luas Bayangan Bidang Datar:**
  $$
  L_{\text{bayangan}} = |\det(M)| \times L_{\text{awal}}
  $$

---

> [!TIP]
> **Petunjuk Belajar:** Mulailah dari [[Translasi_dan_Refleksi_SMA|Modul 1]] untuk membangun fondasi logika pergeseran dan pencerminan sebelum berpindah ke pemutaran dan perkalian skala di Modul 2 serta komposisi matriks di Modul 3. Selesaikan aktivitas di [[LKPD_Transformasi_Geometri_SMA|LKPD]] bersama kelompokmu!
