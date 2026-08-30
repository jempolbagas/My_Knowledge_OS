---
title: "Regangan, Guntingan, & Refleksi Garis Miring — Modul 5 Transformasi Geometri"
type: "materi"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F - Tingkat Lanjut & HOTS UTBK)"
created: 2026-08-19
sources:
  - "[[Transformasi Geometri SMA]]"
  - "[[Komposisi Transformasi dan Matriks SMA]]"
  - "[[Transformasi Fungsi SMA]]"
tags:
  - "#matematika"
  - "#regangan"
  - "#guntingan"
  - "#refleksi_garis_miring"
  - "#kelas11"
  - "#bahan_ajar"
---

[[Transformasi Geometri SMA|🏠 Master Dashboard]] | [[Transformasi Fungsi SMA|⬅️ Modul 4: Transformasi Fungsi]] | **Modul 5: Regangan & Guntingan** | [[LKPD Transformasi Geometri SMA|📝 LKPD]] | [[Soal Transformasi Geometri SMA|🎯 Soal Evaluasi]]

---

# Modul 5: Regangan (Stretching), Guntingan (Shearing), & Refleksi Garis Miring 📐✂️

## 1. Pendahuluan: Transformasi Matriks Non-Isometri & Pengayaan HOTS

Dalam Matematika Tingkat Lanjut Kelas 11 serta soal-soal seleksi masuk PTN (UTBK-SNBT / SIMAK UI), kita tidak hanya menjumpai transformasi isometri (yang mempertahankan ukuran/bentuk objek seperti translasi, refleksi standar, dan rotasi). Terdapat jenis transformasi matriks umum yang mengubah bentuk objek secara nonsimetris: **Regangan (*Stretching*)** dan **Guntingan (*Shearing*)**.

Selain itu, modul ini juga membedah formulasi matriks untuk **pencerminan terhadap garis miring $y = mx$** ($y = x \tan\theta$), yang merupakan pengembangan dari refleksi garis $y = x$ dan $y = -x$.

---

## 2. Regangan (Stretching)

### 2.1 Konsep & Matriks Regangan

Regangan adalah transformasi matriks yang "menarik" atau "menekan" objek hanya searah salah satu sumbu koordinat dengan faktor skala $k$, sementara koordinat sumbu lainnya tidak berubah.

| Arah Regangan | Matriks Transformasi ($M$) | Hubungan Bayangan Koordinat |
| :--- | :---: | :--- |
| **Searah Sumbu $X$ (Skala $k$)** | $\begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix}$ | $x' = k \cdot x, \quad y' = y$ |
| **Searah Sumbu $Y$ (Skala $k$)** | $\begin{pmatrix} 1 & 0 \\ 0 & k \end{pmatrix}$ | $x' = x, \quad y' = k \cdot y$ |

> **Perbedaannya dengan Dilatasi:**
> Dilatasi mengubah koordinat $x$ dan $y$ secara bersamaan ($\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$), sedangkan Regangan hanya mengubah satu arah aksis saja.

---

### 💡 Contoh Soal 1 (Regangan Persegi Panjang):
Diketahui titik-titik sudut persegi $ABCD$ adalah $A(0,0)$, $B(3,0)$, $C(3,3)$, dan $D(0,3)$. Persegi tersebut dikenakan regangan searah sumbu $X$ dengan faktor skala $k = 2$. Tentukan koordinat bayangannya dan luas bangun datar hasil regangan!

**Pembahasan:**
Matriks Regangan searah Sumbu X: $M = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$.
* Titik $A'(0,0)$
* Titik $B'\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ 0 \end{pmatrix} = \begin{pmatrix} 6 \\ 0 \end{pmatrix}$
* Titik $C'\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ 3 \end{pmatrix} = \begin{pmatrix} 6 \\ 3 \end{pmatrix}$
* Titik $D'\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 0 \\ 3 \end{pmatrix} = \begin{pmatrix} 0 \\ 3 \end{pmatrix}$

Bangun bayangan $A'B'C'D'$ berubah menjadi persegi panjang dengan alas $6$ dan tinggi $3$.
Luas Bayangan $L' = 6 \times 3 = 18$ satuan luas (luas awal $L = 9$, $\det(M) = 2 \implies L' = 2 \times 9 = 18$).

---

## 3. Guntingan (Shearing)

### 3.1 Konsep & Matriks Guntingan

Guntingan adalah transformasi yang menggeser titik-titik sejajar dengan suatu sumbu koordinat proporsional terhadap jarak titik tersebut ke sumbu aksisnya, seolah-olah bidang datar "dipotong dan dimiringkan".

| Arah Guntingan | Matriks Transformasi ($M$) | Hubungan Bayangan Koordinat |
| :--- | :---: | :--- |
| **Searah Sumbu $X$ (Faktor Skala $k$)** | $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ | $x' = x + k \cdot y, \quad y' = y$ |
| **Searah Sumbu $Y$ (Faktor Skala $k$)** | $\begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix}$ | $x' = x, \quad y' = y + k \cdot x$ |

> **Sifat Unik Guntingan (Determinant = 1):**
> Perhatikan bahwa $\det(M) = (1)(1) - (0)(k) = 1$. Artinya, **guntingan tidak mengubah luas bidang datar** ($L' = L$), melainkan hanya mengubah kemiringan/sudutnya!

---

### 💡 Contoh Soal 2 (Guntingan pada Garis):
Garis $y = 2x + 1$ dikenakan guntingan searah sumbu $X$ dengan faktor skala $k = 3$. Tentukan persamaan garis bayangannya!

**Pembahasan:**
Matriks Guntingan searah Sumbu X ($k = 3$): $M = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$.
Perubahan koordinat:
$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + 3y \\ y \end{pmatrix}$$

Artinya:
* $y' = y \implies y = y'$
* $x' = x + 3y \implies x = x' - 3y = x' - 3y'$

Substitusikan $x$ dan $y$ ke persamaan garis awal $y = 2x + 1$:
$$y' = 2(x' - 3y') + 1$$
$$y' = 2x' - 6y' + 1$$
$$7y' = 2x' + 1 \implies y = \frac{2}{7}x + \frac{1}{7}$$

Jadi, persamaan garis bayangannya adalah **$y = \frac{2}{7}x + \frac{1}{7}$**.

---

## 4. Refleksi Terhadap Garis Miring $y = mx$

### 4.1 Formulasi Matriks Refleksi Garis $y = x \tan\theta$

Refleksi terhadap garis miring melalui titik pusat $O(0,0)$ dengan gradien $m = \tan\theta$ dirumuskan menggunakan matriks sudut ganda:

$$
M_{y = mx} = \begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix}
$$

dengan hubungan gradien $m$:
$$\cos 2\theta = \frac{1 - m^2}{1 + m^2}, \quad \sin 2\theta = \frac{2m}{1 + m^2}$$

Sehingga matriks dalam bentuk gradien $m$ adalah:

$$
M_{y = mx} = \frac{1}{1 + m^2} \begin{pmatrix} 1 - m^2 & 2m \\ 2m & m^2 - 1 \end{pmatrix}
$$

---

### 💡 Contoh Soal 3 (Refleksi Garis $y = 2x$):
Tentukan bayangan titik $P(3, 4)$ jika dicerminkan terhadap garis $y = 2x$!

**Pembahasan:**
Diketahui gradien $m = 2$.
Substitusi $m=2$ ke rumus matriks refleksi:
$$M = \frac{1}{1 + 2^2} \begin{pmatrix} 1 - 2^2 & 2(2) \\ 2(2) & 2^2 - 1 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} -3 & 4 \\ 4 & 3 \end{pmatrix}$$

Hitung bayangan titik $P(3, 4)$:
$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \frac{1}{5} \begin{pmatrix} -3 & 4 \\ 4 & 3 \end{pmatrix} \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} -9 + 16 \\ 12 + 12 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 7 \\ 24 \end{pmatrix} = \begin{pmatrix} 1.4 \\ 4.8 \end{pmatrix}$$

Jadi, bayangan titik $P$ adalah **$P'\left(\frac{7}{5}, \frac{24}{5}\right)$** atau **$P'(1.4, 4.8)$**.

---

## 5. Rangkuman & Cheatsheet Matriks Pengayaan

> [!NOTE]
> * **Regangan Sumbu X:** $\begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix} \implies$ Luas berubah sebanding $k$.
> * **Regangan Sumbu Y:** $\begin{pmatrix} 1 & 0 \\ 0 & k \end{pmatrix} \implies$ Luas berubah sebanding $k$.
> * **Guntingan Sumbu X:** $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix} \implies$ Luas **tetap** ($\det = 1$).
> * **Guntingan Sumbu Y:** $\begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix} \implies$ Luas **tetap** ($\det = 1$).
> * **Refleksi Garis $y=mx$:** $M = \frac{1}{1+m^2}\begin{pmatrix} 1-m^2 & 2m \\ 2m & m^2-1 \end{pmatrix}$.

---

[[Transformasi Geometri SMA|🏠 Master Dashboard]] | [[Transformasi Fungsi SMA|⬅️ Modul 4: Transformasi Fungsi]] | **Modul 5: Regangan & Guntingan** | [[LKPD Transformasi Geometri SMA|📝 LKPD]] | [[Soal Transformasi Geometri SMA|🎯 Soal Evaluasi]]
