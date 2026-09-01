---
title: "Grafik Fungsi dan Persamaan Trigonometri SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 11 (Fase F), Guru Matematika, dan Persiapan UTBK-SNBT"
created: 2026-09-01
sources:
  - "[[Trigonometri_SMA]]"
  - "[[Sudut_Berelasi_dan_Lingkaran_Satuan_SMA]]"
  - "[[Identitas_dan_Rumus_Jumlah_Selisih_Sudut_SMA]]"
  - "[[LKPD_Trigonometri_SMA]]"
tags:
  - teaching/mathematics
  - mathematics/trigonometry
  - level/sma
  - topic/trig-graphs-equations
---

> **Bilah Navigasi:**
> [[Trigonometri_SMA|🏠 Master Dashboard]] | [[Aturan_Sinus_Cosinus_dan_Luas_Segitiga_SMA|⬅️ Modul 4: Segitiga Sebarang]] | **Modul 5: Grafik & Persamaan** | [[LKPD_Trigonometri_SMA|📝 LKPD ➡️]]

---

# Grafik Fungsi dan Persamaan Trigonometri — Gelombang Harmonik & Solusi Aljabar 🌊📈

Jika kamu memperhatikan pergerakan penumpang pada bianglala raksasa (*ferris wheel*), pasang surut air laut di pantai, arus bolak-balik listrik PLN ($50\text{ Hz}$), hingga getaran senar gitar, semuanya bergerak naik dan turun secara teratur dan berulang. 

Dalam matematika dan fisika, gerak periodik yang halus ini dimodelkan secara sempurna oleh **Fungsi Gelombang Trigonometri**.

---

## 1. Anatomi Tiga Fungsi Induk (*Parent Functions*)

![[diagram_mathematics_trigonometry_graphs_waveform.webp]]

### Karakteristik Tiga Fungsi Induk:

| Parameter | $y = \sin x$ | $y = \cos x$ | $y = \tan x$ |
| :--- | :---: | :---: | :---: |
| **Domain ($x$)** | $x \in \mathbb{R}$ | $x \in \mathbb{R}$ | $x \ne 90^\circ + k \cdot 180^\circ$ |
| **Range ($y$)** | $[-1, 1]$ | $[-1, 1]$ | $(-\infty, \infty)$ |
| **Amplitudo ($A$)** | $1$ | $1$ | Tidak terdefinisi (asimtotik) |
| **Periode ($T$)** | $360^\circ \ (2\pi)$ | $360^\circ \ (2\pi)$ | $180^\circ \ (\pi)$ |
| **Titik Mulai di $x=0$** | $(0,0)$ (Titik Belok) | $(0,1)$ (Puncak Maksimum) | $(0,0)$ |
| **Asimtot Tegak** | Tidak Ada | Tidak Ada | $x = 90^\circ, 270^\circ, \dots$ |

---

## 2. Transformasi Gelombang Umum

Bentuk umum fungsi sinusoidal tergeser:

$$\mathbf{y = A \sin(k(x \pm b)) \pm c} \quad \text{atau} \quad \mathbf{y = A \cos(k(x \pm b)) \pm c}$$

Setiap konstanta mengontrol satu sifat fisik gelombang:

1. **Amplitudo ($|A|$):** Jarak vertikal dari garis tengah (*midline*) ke puncak tertinggi atau lembah terendah.
   $$\text{Amplitudo} = \frac{y_{\max} - y_{\min}}{2} = |A|$$
   *(Jika $A < 0$, grafik dipantulkan/dibalik terhadap garis tengah).*

2. **Frekuensi Sudut / Pengali Periode ($k$):** Jumlah gelombang lengkap dalam rentang $360^\circ$ ($2\pi$).
   $$\mathbf{\text{Periode } (T) = \frac{360^\circ}{k} = \frac{2\pi}{k}}$$
   *(Khusus fungsi Tangen: $\text{Periode} = \frac{180^\circ}{k} = \frac{\pi}{k}$).*

3. **Pergeseran Fasa Horizontal ($b$):** 
   * Jika $(x - b)$, grafik **bergeser ke kanan** sejauh $b$.
   * Jika $(x + b)$, grafik **bergeser ke kiri** sejauh $b$.

4. **Pergeseran Vertikal / Garis Tengah ($c$):**
   * Menaikkan atau menurunkan seluruh gelombang sejauh $c$.
   * $\mathbf{y_{\max} = |A| + c}$
   * $\mathbf{y_{\min} = -|A| + c}$
   * Garis tengah osilasi: $y = c = \frac{y_{\max} + y_{\min}}{2}$.

---

## 3. Persamaan Trigonometri Dasar

Persamaan trigonometri adalah persamaan yang memuat fungsi trigonometri dengan variabel sudut yang belum diketahui. Karena fungsi trigonometri bersifat periodik, solusinya **berulang setiap interval periode tertentu** ($k \in \mathbb{Z}$ = bilangan bulat $\dots, -2, -1, 0, 1, 2, \dots$).

### A. Tipe Sinus: $\sin x = \sin \alpha$
Kuadran yang bernilai positif adalah Kuadran I dan Kuadran II:
$$\mathbf{x_1 = \alpha + k \cdot 360^\circ}$$
$$\mathbf{x_2 = (180^\circ - \alpha) + k \cdot 360^\circ}$$

---

### B. Tipe Kosinus: $\cos x = \cos \alpha$
Kuadran yang bernilai positif adalah Kuadran I dan Kuadran IV:
$$\mathbf{x_1 = \alpha + k \cdot 360^\circ}$$
$$\mathbf{x_2 = -\alpha + k \cdot 360^\circ} \quad (\text{atau } x_2 = (360^\circ - \alpha) + k \cdot 360^\circ)$$

---

### C. Tipe Tangen: $\tan x = \tan \alpha$
Karena periode tangen hanya $180^\circ$ ($\pi$), solusinya cukup satu baris:
$$\mathbf{x = \alpha + k \cdot 180^\circ}$$

---

## 4. Persamaan Trigonometri Berbentuk Kuadrat

Jika persamaan trigonometri memuat bentuk kuadrat seperti $a\sin^2 x + b\sin x + c = 0$ atau $a\cos^2 x + b\cos x + c = 0$:

### Prosedur Standar Penyelesaian:
1. **Samakan Jenis Fungsinya:** Jika terdapat campuran $\sin^2 x$ dan $\cos x$, gunakan identitas Pythagoras $\sin^2 x = 1 - \cos^2 x$ agar semua suku memiliki fungsi yang seragam.
2. **Lakukan Substitusi Variabel:** Misalkan $u = \cos x$.
3. **Faktorkan Persamaan Kuadrat:** Selesaikan nilai $u_1$ dan $u_2$.
4. **Validasi Syarat Range Nilai:** Ingat bahwa $-1 \le \sin x \le 1$ dan $-1 \le \cos x \le 1$. Nilai $u$ di luar rentang ini **harus ditolak / tidak memenuhi (TM)**.
5. **Cari Himpunan Penyelesaian Sudut ($x$):** Selesaikan nilai $x$ yang memenuhi interval yang diminta.

---

## 5. Contoh Soal Berpola & Pembahasan

### Contoh 1: Menentukan Solusi Persamaan Dasar dalam Interval
**Soal:** Tentukan Himpunan Penyelesaian (HP) dari persamaan $2\cos(2x - 30^\circ) = \sqrt{3}$ untuk interval $0^\circ \le x \le 360^\circ$.

**Langkah Pembahasan:**
1. Sederhanakan persamaan ke bentuk dasar $\cos \theta = \cos \alpha$:
   $$\cos(2x - 30^\circ) = \frac{\sqrt{3}}{2} = \cos 30^\circ$$
2. Terapkan solusi kosinus:
   * **Kemungkinan 1:**
     $$2x - 30^\circ = 30^\circ + k \cdot 360^\circ$$
     $$2x = 60^\circ + k \cdot 360^\circ \implies x = 30^\circ + k \cdot 180^\circ$$
     * Untuk $k = 0 \implies x = \mathbf{30^\circ}$
     * Untuk $k = 1 \implies x = 30^\circ + 180^\circ = \mathbf{210^\circ}$
     * Untuk $k = 2 \implies x = 30^\circ + 360^\circ = 390^\circ$ (Di luar batas)
   * **Kemungkinan 2:**
     $$2x - 30^\circ = -30^\circ + k \cdot 360^\circ$$
     $$2x = 0^\circ + k \cdot 360^\circ \implies x = 0^\circ + k \cdot 180^\circ$$
     * Untuk $k = 0 \implies x = \mathbf{0^\circ}$
     * Untuk $k = 1 \implies x = \mathbf{180^\circ}$
     * Untuk $k = 2 \implies x = \mathbf{360^\circ}$
3. Gabungkan seluruh solusi dalam interval $0^\circ \le x \le 360^\circ$:
   $$\mathbf{HP = \{0^\circ, 30^\circ, 180^\circ, 210^\circ, 360^\circ\}}$$

---

### Contoh 2: Persamaan Kuadrat Trigonometri
**Soal:** Tentukan semua nilai $x$ yang memenuhi $2\sin^2 x - 3\sin x + 1 = 0$ pada rentang $0 \le x \le 2\pi$.

**Langkah Pembahasan:**
1. Misalkan $u = \sin x$, maka persamaan menjadi:
   $$2u^2 - 3u + 1 = 0$$
   $$(2u - 1)(u - 1) = 0 \implies u_1 = \frac{1}{2} \quad \text{atau} \quad u_2 = 1$$
2. Cari nilai $x$ untuk setiap akar:
   * **Kasus 1 ($u_1 = \frac{1}{2} \implies \sin x = \frac{1}{2}$):**
     * Kuadran I: $x = \frac{\pi}{6}$
     * Kuadran II: $x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$
   * **Kasus 2 ($u_2 = 1 \implies \sin x = 1$):**
     * $x = \frac{\pi}{2}$
3. Himpunan Penyelesaian:
   $$\mathbf{HP = \left\{\frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}\right\}}$$

---

## 6. Rangkuman Konsep Kunci

* Gelombang $y = A\sin(kx)$ memiliki amplitudo $|A|$ dan periode $T = \frac{360^\circ}{k}$.
* Persamaan sinus dan kosinus selalu menghasilkan **dua cabang keluarga solusi** ditambah pengali $k \cdot 360^\circ$.
* Persamaan tangen hanya memiliki **satu cabang solusi** dengan pengali $k \cdot 180^\circ$.
* Pada persamaan kuadrat trigonometri, nilai $\sin x$ dan $\cos x$ wajib berada pada rentang $[-1, 1]$.

---

> **Bilah Navigasi:**
> [[Trigonometri_SMA|🏠 Master Dashboard]] | [[Aturan_Sinus_Cosinus_dan_Luas_Segitiga_SMA|⬅️ Modul 4: Segitiga Sebarang]] | **Modul 5: Grafik & Persamaan** | [[LKPD_Trigonometri_SMA|📝 LKPD ➡️]]
