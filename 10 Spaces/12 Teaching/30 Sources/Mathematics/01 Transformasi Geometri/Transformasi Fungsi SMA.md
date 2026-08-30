---
title: "Transformasi Fungsi — Modul 4 Transformasi Geometri"
type: "materi"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-19
sources:
  - "[[Transformasi Geometri SMA]]"
  - "[[LKPD Transformasi Geometri SMA]]"
tags:
  - "#matematika"
  - "#transformasi_fungsi"
  - "#kelas11"
  - "#bahan_ajar"
---

[[Transformasi Geometri SMA|🏠 Master Dashboard]] | [[Komposisi Transformasi dan Matriks SMA|⬅️ Modul 3: Komposisi & Matriks]] | **Modul 4: Transformasi Fungsi** | [[Regangan Guntingan Transformasi SMA|Modul 5: Regangan & Guntingan ➡️]] | [[LKPD Transformasi Geometri SMA|📝 LKPD]]

---

# Modul 4: Transformasi Fungsi $y = f(x)$ 📈⚡

## 1. Pendahuluan: Memahami Pergerakan Grafik Fungsi

Dalam Matematika Wajib Kelas 11 Kurikulum Merdeka (Fase F), konsep transformasi geometri diperluas tidak hanya pada titik atau bidang datar, melainkan pada **grafik fungsi** $y = f(x)$. 

Ketika persamaan fungsi diubah strukturnya—misalnya dari $f(x)$ menjadi $f(x - 2) + 3$ atau $-2 f(x)$—grafik fungsi tersebut mengalami pergeseran, pencerminan, atau peregangan/penyusutan di dalam koordinat Kartesius. Konsep ini sangat vital dalam analisis data real-time, pemodelan ekonomi, sinyal gelombang audio, dan grafik komputer.

> **Prinsip Utama Perubahan Fungsi:**
> * **Transformasi Input (Horizontal / Dalam Kurung):** Mengubah variabel $x$ secara langsung. Efeknya sering kali **berlawanan intuitif** (misal: $x - a$ menggeser ke *kanan*).
> * **Transformasi Output (Vertikal / Luar Kurung):** Mengubah nilai total fungsi $y$. Efeknya **searah intuitif** (misal: $+ b$ menggeser ke *atas*).

---

## 2. Translasi (Pergeseran) Fungsi

### 2.1 Konsep & Formulasi Translasi Fungsi

Translasi mengubah posisi grafik fungsi sejauh $a$ satuan secara horizontal dan $b$ satuan secara vertikal tanpa mengubah bentuk grafik dasarnya.

| Jenis Pergeseran | Persamaan Fungsi Baru | Arah Pergeseran Grafik |
| :--- | :---: | :--- |
| **Pergeseran Horizontal (Ke Kanan)** | $y = f(x - a)$ | Bergeser sejauh $a$ satuan ke kanan |
| **Pergeseran Horizontal (Ke Kiri)** | $y = f(x + a)$ | Bergeser sejauh $a$ satuan ke kiri |
| **Pergeseran Vertikal (Ke Atas)** | $y = f(x) + b$ | Bergeser sejauh $b$ satuan ke atas |
| **Pergeseran Vertikal (Ke Bawah)** | $y = f(x) - b$ | Bergeser sejauh $b$ satuan ke bawah |

> **Bentuk Gabungan Translasi Fungsi:**
> Jika grafik $y = f(x)$ ditranslasikan oleh vektor $T = \begin{pmatrix} a \\ b \end{pmatrix}$, maka persamaan bayangan barunya adalah:
> $$y = f(x - a) + b$$

---

### 💡 Contoh Soal 1 (Translasi Parabola & Fungsi Eksponensial):

1. Grafik fungsi kuadrat $f(x) = x^2 - 4x + 3$ digeser ke kanan sejauh $3$ satuan dan ke atas sejauh $2$ satuan. Tentukan persamaan bayangan grafiknya!
2. Grafik fungsi eksponensial $g(x) = 2^x$ digeser ke kiri sejauh $1$ satuan dan ke bawah sejauh $4$ satuan. Tentukan persamaan grafik barunya!

**Pembahasan:**

1. Translasi oleh $T = \begin{pmatrix} 3 \\ 2 \end{pmatrix} \implies y = f(x - 3) + 2$:
   $$y = \left((x - 3)^2 - 4(x - 3) + 3\right) + 2$$
   $$y = (x^2 - 6x + 9) - (4x - 12) + 3 + 2$$
   $$y = x^2 - 10x + 26$$
   Jadi, persamaan bayangannya adalah **$y = x^2 - 10x + 26$**.

2. Translasi oleh $T = \begin{pmatrix} -1 \\ -4 \end{pmatrix} \implies y = g(x - (-1)) - 4 = g(x + 1) - 4$:
   $$y = 2^{x + 1} - 4$$
   Jadi, persamaan grafik barunya adalah **$y = 2^{x + 1} - 4$** (garis asimtot datar bergeser dari $y=0$ menjadi $y=-4$).

---

## 3. Refleksi (Pencerminan) Fungsi

### 3.1 Konsep & Formulasi Refleksi Fungsi

Refleksi mencerminkan grafik fungsi terhadap sumbu koordinat.

* **Refleksi Terhadap Sumbu-X (Pencerminan Vertikal):**
  Mengubah seluruh nilai output menjadi negatif.
  $$y = -f(x)$$
  *(Grafik terbalik ke atas/bawah).*

* **Refleksi Terhadap Sumbu-Y (Pencerminan Horizontal):**
  Mengubah tanda variabel input $x$.
  $$y = f(-x)$$
  *(Grafik terbalik ke kiri/kanan).*

---

### 💡 Contoh Soal 2 (Refleksi Fungsi Polinomial):
Diketahui fungsi $f(x) = x^3 - 3x$. Tentukan persamaan bayangan jika:
a. Dicerminkan terhadap sumbu-X
b. Dicerminkan terhadap sumbu-Y

**Pembahasan:**
a. Dicerminkan terhadap sumbu-X ($y = -f(x)$):
   $$y = -(x^3 - 3x) = -x^3 + 3x$$
   Jadi, persamaannya adalah **$y = -x^3 + 3x$**.

b. Dicerminkan terhadap sumbu-Y ($y = f(-x)$):
   $$y = (-x)^3 - 3(-x) = -x^3 + 3x$$
   Jadi, persamaannya adalah **$y = -x^3 + 3x$**.

---

## 4. Dilatasi (Peregangan & Penyusutan) Fungsi

### 4.1 Konsep & Formulasi Dilatasi Fungsi

Dilatasi pada grafik fungsi mengubah skala bentuk grafik, baik diregangkan (*stretched*) maupun disusutkan/dimampatkan (*compressed*).

#### A. Dilatasi Vertikal ($y = a \cdot f(x)$)
Fungsi dikalikan dengan faktor skala $a$ di luar fungsi:
* Jika $|a| > 1$, grafik mengalami **peregangan vertikal** (makin curam / makin tinggi).
* Jika $0 < |a| < 1$, grafik mengalami **penyusutan vertikal** (makin landai / makin pipih).

#### B. Dilatasi Horizontal ($y = f(b \cdot x)$)
Variabel $x$ dikalikan dengan faktor $b$ di dalam fungsi:
* Jika $|b| > 1$, grafik mengalami **penyusutan horizontal** (dimampatkan secara mendatar sejauh faktor $\frac{1}{b}$).
* Jika $0 < |b| < 1$, grafik mengalami **peregangan horizontal** (melebar secara mendatar sejauh faktor $\frac{1}{b}$).

---

### 💡 Contoh Soal 3 (Dilatasi Fungsi Kuadrat):
Grafik $f(x) = x^2 + 2x$ mengalami penyusutan vertikal dengan faktor skala $\frac{1}{2}$, kemudian dilanjutkan penyusutan horizontal dengan faktor $b = 3$. Tentukan persamaan bayangan akhirnya!

**Pembahasan:**
1. Penyusutan vertikal skala $\frac{1}{2} \implies y_1 = \frac{1}{2} f(x) = \frac{1}{2}(x^2 + 2x) = \frac{1}{2}x^2 + x$.
2. Penyusutan horizontal faktor $b = 3 \implies y_2 = y_1(3x)$:
   $$y = \frac{1}{2}(3x)^2 + (3x) = \frac{1}{2}(9x^2) + 3x = \frac{9}{2}x^2 + 3x$$
Jadi, persamaan bayangannya adalah **$y = \frac{9}{2}x^2 + 3x$**.

---

## 5. Rangkuman & Tips Cepat Modul 4

> [!NOTE]
> * **Translasi:** $x \to x - a$ (kanan), $x \to x + a$ (kiri), $y \to y + b$ (atas), $y \to y - b$ (bawah).
> * **Refleksi:** Terhadap Sumbu-X $\to -f(x)$, Terhadap Sumbu-Y $\to f(-x)$.
> * **Dilatasi Vertikal vs Horizontal:** Faktor $a$ di luar kurung memengaruhi tinggi grafik ($a \cdot f(x)$), sedangkan faktor $b$ di dalam kurung memengaruhi lebarnya ($f(b \cdot x)$).

---

[[Transformasi Geometri SMA|🏠 Master Dashboard]] | [[Komposisi Transformasi dan Matriks SMA|⬅️ Modul 3: Komposisi & Matriks]] | **Modul 4: Transformasi Fungsi** | [[Regangan Guntingan Transformasi SMA|Modul 5: Regangan & Guntingan ➡️]] | [[LKPD Transformasi Geometri SMA|📝 LKPD]]
