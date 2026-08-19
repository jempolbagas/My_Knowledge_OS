---
title: "Rotasi dan Dilatasi — Modul 2 Transformasi Geometri"
type: "materi"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-18
sources:
  - "[[Transformasi_Geometri_SMA]]"
  - "[[Translasi_dan_Refleksi_SMA]]"
  - "[[LKPD_Transformasi_Geometri_SMA]]"
tags:
  - "#matematika"
  - "#rotasi"
  - "#dilatasi"
  - "#kelas11"
  - "#bahan_ajar"
---

[[Transformasi_Geometri_SMA|🏠 Master Dashboard]] | [[Translasi_dan_Refleksi_SMA|⬅️ Modul 1: Translasi & Refleksi]] | **Modul 2: Rotasi & Dilatasi** | [[Komposisi_Transformasi_dan_Matriks_SMA|Modul 3: Komposisi ➡️]] | [[LKPD_Transformasi_Geometri_SMA|📝 LKPD]]

---

# Modul 2: Rotasi (Perputaran) & Dilatasi (Perkalian Skala) 🎡🔍

## 1. Pendahuluan: Rotasi & Dilatasi di Dunia Nyata

Pernahkah kamu naik wahana Bianglala / Komedi Putar di pasar malam? Saat bianglala berputar, posisi tempat dudukmu mengalami perubahan sudut terhadap pusat porosnya. Fenomena ini dinamakan **Rotasi (Perputaran)**!

Di sisi lain, ketika kamu membuka foto di *smartphone* lalu mencubit layarnya untuk memperbesar (*zoom-in*) atau memperkecil (*zoom-out*), semua piksel koordinat foto berubah secara proporsional dari titik pusat sentuhan layarmu. Inilah penerapan **Dilatasi (Perkalian Skala)**!

Pada modul ini, kita akan mempelajari formulasi matematika dan matriks untuk rotasi dan dilatasi, baik dengan pusat titik asal $O(0,0)$ maupun titik pusat sembarang $P(a,b)$.

---

## 2. Rotasi (Perputaran)

### 2.1 Konsep & Aturan Sudut Rotasi
Rotasi memutar setiap titik sebesar sudut $\theta$ terhadap suatu titik pusat rotasi.

> **Aturan Tanda Sudut Rotasi ($\theta$):**
> * Sudut $\theta > 0$ (Positif) $\implies$ Berputar **Berlawanan arah jarum jam**.
> * Sudut $\theta < 0$ (Negatif) $\implies$ Berputar **Searah jarum jam**.

#### Nilai Sudut Istimewa yang Sering Digunakan:
* Rotasi $+90^\circ$ (sama dengan $-270^\circ$): $\cos 90^\circ = 0$, $\sin 90^\circ = 1 \implies M = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$
* Rotasi $+180^\circ$ (sama dengan $-180^\circ$): $\cos 180^\circ = -1$, $\sin 180^\circ = 0 \implies M = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$
* Rotasi $+270^\circ$ (sama dengan $-90^\circ$): $\cos 270^\circ = 0$, $\sin 270^\circ = -1 \implies M = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$

---

### 2.2 Formulasi Rotasi

#### A. Rotasi dengan Pusat $O(0,0)$
Jika titik $A(x,y)$ diputar sebesar sudut $\theta$ berlawanan arah jarum jam terhadap titik pusat $O(0,0)$:

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
$$

> **Hasil Perkalian Matriks:**
> $$x' = x \cos\theta - y \sin\theta$$
> $$y' = x \sin\theta + y \cos\theta$$

#### B. Rotasi dengan Pusat $P(a,b)$
Jika titik $A(x,y)$ diputar sebesar sudut $\theta$ terhadap titik pusat $P(a,b)$:

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x - a \\ y - b \end{pmatrix} + \begin{pmatrix} a \\ b \end{pmatrix}
$$

---

#### 💡 Contoh Soal 1 (Rotasi Titik & Garis):
Tentukan bayangan dari titik $A(4, -2)$ jika diputar sebesar $90^\circ$ berlawanan arah jarum jam terhadap titik pusat $P(1, 3)$!

**Pembahasan:**
Diketahui $\theta = 90^\circ$, $a = 1$, $b = 3$. 
Matriks rotasi $90^\circ$: $\begin{pmatrix} \cos 90^\circ & -\sin 90^\circ \\ \sin 90^\circ & \cos 90^\circ \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

Substitusi ke rumus pusat $P(a,b)$:
$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 4 - 1 \\ -2 - 3 \end{pmatrix} + \begin{pmatrix} 1 \\ 3 \end{pmatrix}$$

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 3 \\ -5 \end{pmatrix} + \begin{pmatrix} 1 \\ 3 \end{pmatrix}$$

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 5 \\ 3 \end{pmatrix} + \begin{pmatrix} 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 6 \\ 6 \end{pmatrix}$$

Jadi, bayangan akhir titik $A$ adalah **$A'(6, 6)$**.

---

## 3. Dilatasi (Perkalian Skala)

### 3.1 Konsep & Faktor Skala $k$
Dilatasi adalah transformasi yang mengubah ukuran (memperbesar atau memperkecil) suatu objek geometri tanpa mengubah bentuk dasarnya.

> **Sifat Faktor Skala $k$:**
> * Jika $|k| > 1$, objek **diperbesar**.
> * Jika $0 < |k| < 1$, objek **diperkecil**.
> * Jika $k > 0$, bayangan berada di **sisi yang sama** dengan objek terhadap pusat dilatasi.
> * Jika $k < 0$, bayangan berada di **sisi berlawanan** (terbalik) terhadap pusat dilatasi.

---

### 3.2 Formulasi Dilatasi

#### A. Dilatasi Pusat $O(0,0)$ dengan Faktor Skala $k$
Notasi: $[O, k]$

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} kx \\ ky \end{pmatrix}
$$

> **Persamaan Koordinat:**
> $$x' = kx \implies x = \frac{x'}{k}$$
> $$y' = ky \implies y = \frac{y'}{k}$$

#### B. Dilatasi Pusat $P(a,b)$ dengan Faktor Skala $k$
Notasi: $[P(a,b), k]$

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = k \begin{pmatrix} x - a \\ y - b \end{pmatrix} + \begin{pmatrix} a \\ b \end{pmatrix}
$$

> **Persamaan Koordinat:**
> $$x' = k(x - a) + a \implies x = \frac{x' - a}{k} + a$$
> $$y' = k(y - b) + b \implies y = \frac{y' - b}{k} + b$$

---

#### 💡 Contoh Soal 2 (Dilatasi Persamaan Lingkaran):
Tentukan bayangan lingkaran $x^2 + y^2 = 4$ jika didilatasi oleh $[O, 3]$ (pusat $O(0,0)$ dengan faktor skala $k = 3$)!

**Pembahasan:**
Dari dilatasi $[O, 3]$, didapat:
$$x' = 3x \implies x = \frac{x'}{3}$$
$$y' = 3y \implies y = \frac{y'}{3}$$

Substitusikan $x$ dan $y$ ke persamaan lingkaran awal:
$$\left(\frac{x'}{3}\right)^2 + \left(\frac{y'}{3}\right)^2 = 4$$

$$\frac{(x')^2}{9} + \frac{(y')^2}{9} = 4$$

Kalikan kedua ruas dengan $9$:
$$(x')^2 + (y')^2 = 36$$

Jadi, persamaan bayangan lingkarannya adalah **$x^2 + y^2 = 36$** (jari-jari lingkaran bertambah dari $r=2$ menjadi $r'=6$).

---

## 4. Rangkuman & Tips Cepat Modul 2

> [!NOTE]
> * **Rotasi $90^\circ$ positif pusat $(0,0)$:** Titik $(x, y) \to (-y, x)$.
> * **Rotasi $180^\circ$ pusat $(0,0)$:** Titik $(x, y) \to (-x, -y)$.
> * **Rotasi $270^\circ$ positif pusat $(0,0)$:** Titik $(x, y) \to (y, -x)$.
> * **Dilatasi memperbesar ukuran:** Luas bayangan setelah dilatasi dengan faktor skala $k$ menjadi $k^2$ kali luas semula!

---

[[Transformasi_Geometri_SMA|🏠 Master Dashboard]] | [[Translasi_dan_Refleksi_SMA|⬅️ Modul 1: Translasi & Refleksi]] | **Modul 2: Rotasi & Dilatasi** | [[Komposisi_Transformasi_dan_Matriks_SMA|Modul 3: Komposisi ➡️]] | [[LKPD_Transformasi_Geometri_SMA|📝 LKPD]]
