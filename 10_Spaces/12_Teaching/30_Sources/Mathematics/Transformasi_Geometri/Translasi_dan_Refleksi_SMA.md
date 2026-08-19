---
title: "Translasi dan Refleksi — Modul 1 Transformasi Geometri"
type: "materi"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-18
sources:
  - "[[Transformasi_Geometri_SMA]]"
  - "[[LKPD_Transformasi_Geometri_SMA]]"
tags:
  - "#matematika"
  - "#translasi"
  - "#refleksi"
  - "#kelas11"
  - "#bahan_ajar"
---

[[Transformasi_Geometri_SMA|🏠 Master Dashboard]] | **Modul 1: Translasi & Refleksi** | [[Rotasi_dan_Dilatasi_SMA|Modul 2: Rotasi & Dilatasi ➡️]] | [[LKPD_Transformasi_Geometri_SMA|📝 LKPD]]

---

# Modul 1: Translasi (Pergeseran) & Refleksi (Pencerminan) 🚀🪞

## 1. Pendahuluan: Mengapa Translasi & Refleksi Penting?

Bayangkan kamu sedang memainkan game *Mobile Legends* atau *Valorant*. Ketika karaktermu bergerak dari koordinat $(2, 3)$ ke $(6, 8)$ di dalam *map*, game sedang melakukan perhitungan **Translasi (Pergeseran)**! 

Sementara itu, ketika kamu berkaca di cermin rias atau melihat bayangan gedung di atas permukaan air danau yang tenang, kamu sedang menyaksikan fenomena fisika-matematika dari **Refleksi (Pencerminan)**. 

Kedua konsep ini merupakan fondasi dasar dari geometri transformasi yang mempertahankan bentuk dan ukuran objek asli (*isometri*). Mari kita bedah satu per satu secara intuitif dan matematis!

---

## 2. Translasi (Pergeseran)

### 2.1 Konsep & Pengertian
Translasi adalah pemindahan semua titik pada bidang datar sejauh jarak dan arah tertentu yang diwakili oleh suatu **vektor pergeseran**. 

Misalkan suatu titik $A(x, y)$ ditranslasikan oleh matriks komponen translasi $T = \begin{pmatrix} a \\ b \end{pmatrix}$, maka:
* $a$ menentukan komponen pergeseran horizontal (ke kanan jika $a > 0$, ke kiri jika $a < 0$).
* $b$ menentukan komponen pergeseran vertikal (ke atas jika $b > 0$, ke bawah jika $b < 0$).

### 2.2 Formulasi Matematika Translasi
Jika titik asal $A(x,y)$ digeser oleh $T = \begin{pmatrix} a \\ b \end{pmatrix}$ menghasilkan titik bayangan $A'(x', y')$, maka rumus dasarnya adalah:

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} x + a \\ y + b \end{pmatrix}
$$

> **Persamaan Koordinat:**
> $$x' = x + a \quad \Longrightarrow \quad x = x' - a$$
> $$y' = y + b \quad \Longrightarrow \quad y = y' - b$$

---

### 2.3 Translasi pada Persamaan Garis dan Kurva

Untuk mentranslasikan suatu persamaan garis atau kurva $y = f(x)$:
1. Tuliskan $x$ dan $y$ dalam bentuk bayangan $x'$ dan $y'$:
   $$x = x' - a, \quad y = y' - b$$
2. Substitusikan $x$ dan $y$ tersebut ke dalam persamaan awal.
3. Rapikan persamaan baru, lalu hilangkan tanda aksen (') untuk mendapatkan persamaan bayangan akhir.

#### 💡 Contoh Soal 1 (Translasi Titik & Garis):
Tentukan bayangan dari:
a. Titik $P(-3, 7)$ oleh translasi $T = \begin{pmatrix} 5 \\ -4 \end{pmatrix}$.
b. Garis $2x - 3y + 6 = 0$ oleh translasi $T = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$.

**Pembahasan:**
a. Koordinat bayangan $P'$:
   $$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} -3 \\ 7 \end{pmatrix} + \begin{pmatrix} 5 \\ -4 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$$
   Jadi, bayangan titik $P$ adalah $P'(2, 3)$.

b. Untuk garis $2x - 3y + 6 = 0$:
   $$x' = x + 1 \implies x = x' - 1$$
   $$y' = y + 3 \implies y = y' - 3$$
   Substitusi ke persamaan asal:
   $$2(x' - 1) - 3(y' - 3) + 6 = 0$$
   $$2x' - 2 - 3y' + 9 + 6 = 0$$
   $$2x' - 3y' + 13 = 0$$
   Jadi, bayangan garisnya adalah **$2x - 3y + 13 = 0$**.

---

## 3. Refleksi (Pencerminan)

### 3.1 Konsep & Sifat Refleksi
Refleksi memindahkan setiap titik pada bidang menggunakan sifat cermin datar:
1. Jarak titik awal ke cermin sama dengan jarak titik bayangan ke cermin.
2. Garis yang menghubungkan titik asal dan bayangannya selalu **tegak lurus** dengan garis cermin.
3. Ukuran dan bentuk objek bayangan sama persis dengan objek asal (*kongruen*).

---

### 3.2 Matriks Transformasi Refleksi

Berikut adalah 7 jenis pencerminan standar beserta matriks transformasinya:

```
┌──────────────────────────────────────┬───────────────────────────────┬──────────────────────────────────────────┐
│ Jenis Pencerminan (Cermin)           │ Matriks Transformasi (M)      │ Hubungan Koordinat Bayangan              │
├──────────────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ Terhadap Sumbu X (y = 0)             │ ┌──  1   0 ──┐                │ x' = x                                   │
│                                      │ └──  0  -1 ──┘                │ y' = -y                                  │
├──────────────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ Terhadap Sumbu Y (x = 0)             │ ┌── -1   0 ──┐                │ x' = -x                                  │
│                                      │ └──  0   1 ──┘                │ y' = y                                   │
├──────────────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ Terhadap Garis y = x                 │ ┌──  0   1 ──┐                │ x' = y                                   │
│                                      │ └──  1   0 ──┘                │ y' = x                                   │
├──────────────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ Terhadap Garis y = -x                │ ┌──  0  -1 ──┐                │ x' = -y                                  │
│                                      │ └── -1   0 ──┘                │ y' = -x                                  │
├──────────────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ Terhadap Titik Asal O(0,0)           │ ┌── -1   0 ──┐                │ x' = -x                                  │
│                                      │ └──  0  -1 ──┘                │ y' = -y                                  │
├──────────────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ Terhadap Garis x = h                 │ Non-Matriks Tunggal           │ x' = 2h - x                              │
│                                      │                               │ y' = y                                   │
├──────────────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ Terhadap Garis y = k                 │ Non-Matriks Tunggal           │ x' = x                                   │
│                                      │                               │ y' = 2k - y                              │
└──────────────────────────────────────┴───────────────────────────────┴──────────────────────────────────────────┘
```

> **Formulasi Umum Matriks Refleksi:**
> $$\begin{pmatrix} x' \\ y' \end{pmatrix} = M \begin{pmatrix} x \\ y \end{pmatrix}$$

---

#### 💡 Contoh Soal 2 (Refleksi Kurva Parabola):
Tentukan persamaan bayangan dari parabola $y = x^2 - 4x + 3$ yang dicerminkan terhadap:
a. Garis $y = x$
b. Garis $x = 2$

**Pembahasan:**
a. Dicerminkan terhadap garis $y = x$:
   Matriks $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, sehingga:
   $$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} y \\ x \end{pmatrix}$$
   Artinya $x' = y \implies y = x'$ dan $y' = x \implies x = y'$.
   Substitusi $x = y'$ dan $y = x'$ ke persamaan parabola $y = x^2 - 4x + 3$:
   $$x' = (y')^2 - 4y' + 3$$
   Jadi, persamaan bayangannya adalah **$x = y^2 - 4y + 3$**.

b. Dicerminkan terhadap garis $x = 2$ ($h = 2$):
   $$x' = 2h - x = 2(2) - x = 4 - x \implies x = 4 - x'$$
   $$y' = y \implies y = y'$$
   Substitusi ke persamaan asal:
   $$y' = (4 - x')^2 - 4(4 - x') + 3$$
   $$y' = (16 - 8x' + (x')^2) - 16 + 4x' + 3$$
   $$y' = (x')^2 - 4x' + 3$$
   Jadi, persamaan bayangan akhirnya tetap **$y = x^2 - 4x + 3$** (karena sumbu simetri parabola awal terletak tepat di $x = 2$).

---

## 4. Rangkuman & Tips Cepat Modul 1

> [!NOTE]
> * **Translasi** bersifat penjumlahan vektor: $\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} a \\ b \end{pmatrix}$.
> * **Tukar Tanda pada Garis Khusus:** Refleksi terhadap garis $y = x$ menukar nilai $x$ dan $y$. Refleksi terhadap $y = -x$ menukar posisi sekaligus mengubah tanda keduanya menjadi negatif.
> * **Garis $x=h$ dan $y=k$:** Ingat rumus pengkali 2, yaitu $2h - x$ dan $2k - y$.

---

[[Transformasi_Geometri_SMA|🏠 Master Dashboard]] | **Modul 1: Translasi & Refleksi** | [[Rotasi_dan_Dilatasi_SMA|Modul 2: Rotasi & Dilatasi ➡️]] | [[LKPD_Transformasi_Geometri_SMA|📝 LKPD]]
