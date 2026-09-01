---
title: "Sudut Berelasi dan Lingkaran Satuan SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 10 (Fase E), Guru Matematika, dan Pembelajar Mandiri"
created: 2026-09-01
sources:
  - "[[Trigonometri_SMA]]"
  - "[[Perbandingan_Trigonometri_dan_Sudut_Istimewa_SMA]]"
  - "[[Identitas_dan_Rumus_Jumlah_Selisih_Sudut_SMA]]"
  - "[[LKPD_Trigonometri_SMA]]"
tags:
  - teaching/mathematics
  - mathematics/trigonometry
  - level/sma
  - topic/unit-circle-quadrants
---

> **Bilah Navigasi:**
> [[Trigonometri_SMA|🏠 Master Dashboard]] | [[Perbandingan_Trigonometri_dan_Sudut_Istimewa_SMA|⬅️ Modul 1: Rasio Dasar]] | **Modul 2: Sudut Berelasi** | [[Identitas_dan_Rumus_Jumlah_Selisih_Sudut_SMA|Modul 3: Identitas Analitik ➡️]] | [[LKPD_Trigonometri_SMA|📝 LKPD]]

---

# Sudut Berelasi dan Lingkaran Satuan — Menjelajah 4 Kuadran Tanpa Batas Derajat 🔄🧭

Pada Modul 1, kita mempelajari trigonometri menggunakan segitiga siku-siku. Namun, muncul satu dilema mendasar: **jumlah sudut dalam segitiga selalu $180^\circ$**, sehingga sudut lancip dalam segitiga siku-siku tidak akan pernah bisa melebihi $90^\circ$. 

Lantas, bagaimana jika kita perlu menghitung arah navigasi kapal pada sudut azimuth $150^\circ$, fase gelombang radar pada sudut $240^\circ$, atau putaran roda turbin sebesar $-45^\circ$ dan $750^\circ$?

Jawabannya adalah memindahkan trigonometri ke dalam **Sistem Koordinat Kartesius** melalui konsep **Lingkaran Satuan (*Unit Circle*)**.

---

## 1. Lingkaran Satuan (*The Unit Circle*)

Lingkaran satuan adalah lingkaran yang berpusat di titik asal $O(0,0)$ dan memiliki jari-jari $r = 1\text{ satuan}$. Persamaan lingkarannya adalah:
$$x^2 + y^2 = 1$$

Misalkan ada sebuah titik $P(x,y)$ pada keliling lingkaran yang dibentuk oleh jari-jari yang berputar berlawanan arah jarum jam sejauh sudut $\theta$ dari sumbu X positif:

![[diagram_mathematics_trigonometry_unit_circle.webp]]

Pada segitiga siku-siku bayangan di dalam lingkaran satuan:
* $\sin \theta = \frac{\text{Depan}}{\text{Miring}} = \frac{y}{1} \implies \mathbf{y = \sin \theta}$
* $\cos \theta = \frac{\text{Samping}}{\text{Miring}} = \frac{x}{1} \implies \mathbf{x = \cos \theta}$
* $\tan \theta = \frac{\text{Depan}}{\text{Samping}} \implies \mathbf{\tan \theta = \frac{y}{x} = \frac{\sin \theta}{\cos \theta}}$

> [!NOTE]
> **Definisi Universal Trigonometri:**
> Setiap koordinat titik di keliling lingkaran satuan **selalu merupakan pasangan $(\cos \theta, \sin \theta)$**.
> * Nilai $\cos \theta$ mewakili **posisi horizontal ($x$)**.
> * Nilai $\sin \theta$ mewakili **posisi vertikal ($y$)**.
> * Nilai $\tan \theta$ mewakili **gradien/kemiringan garis jari-jari**.

---

## 2. Pembagian 4 Kuadran & Aturan Tanda ASTC

Karena koordinat $(x, y)$ bernilai positif atau negatif tergantung pada kuadran tempat titik tersebut berada, tanda nilai trigonometri mengikuti kaidah berikut:

| Kuadran | Rentang Sudut ($\theta$) | Tanda Koordinat | Fungsi Positif (+) | Jembatan Keledai |
| :---: | :---: | :---: | :---: | :---: |
| **I** | $0^\circ < \theta < 90^\circ$ | $x > 0, y > 0$ | **Semua (All)** | **A**ll |
| **II** | $90^\circ < \theta < 180^\circ$ | $x < 0, y > 0$ | **Sinus** (dan $\csc$) | **S**tudents / **S**urat |
| **III** | $180^\circ < \theta < 270^\circ$ | $x < 0, y < 0$ | **Tangen** (dan $\cot$) | **T**ake / **T**anda |
| **IV** | $270^\circ < \theta < 360^\circ$ | $x > 0, y < 0$ | **Kosinus** (dan $\sec$) | **C**alculus / **C**inta |

### Jembatan Keledai Tanda Kuadran:
1. **"ASTC"** $\to$ **A**ll, **S**in, **T**an, **C**os.
2. **"Semua Surat Tanda Cinta"** (Semua $\to$ Sinus $\to$ Tangen $\to$ Cosinus).
3. **"All Students Take Calculus"**.

---

## 3. Sistem Formula Sudut Berelasi

Untuk mencari nilai trigonometri sudut tumpul atau refleks, kita selalu mengaitkannya dengan sudut lancip $\alpha$ ($0^\circ \le \alpha \le 90^\circ$) di Kuadran I.

Ada **Dua Strategi Relasi**:

### Strategi 1: Patokan Sumbu Horizontal / Sumbu X ($180^\circ$ & $360^\circ$) $\to$ *FUNGSI TETAP*
*(Metode Paling Direkomendasikan karena minim risiko kekeliruan)*

* **Kuadran II ($180^\circ - \alpha$):**
  $$\sin(180^\circ - \alpha) = +\sin \alpha$$
  $$\cos(180^\circ - \alpha) = -\cos \alpha$$
  $$\tan(180^\circ - \alpha) = -\tan \alpha$$

* **Kuadran III ($180^\circ + \alpha$):**
  $$\sin(180^\circ + \alpha) = -\sin \alpha$$
  $$\cos(180^\circ + \alpha) = -\cos \alpha$$
  $$\tan(180^\circ + \alpha) = +\tan \alpha$$

* **Kuadran IV ($360^\circ - \alpha$):**
  $$\sin(360^\circ - \alpha) = -\sin \alpha$$
  $$\cos(360^\circ - \alpha) = +\cos \alpha$$
  $$\tan(360^\circ - \alpha) = -\tan \alpha$$

---

### Strategi 2: Patokan Sumbu Vertikal / Sumbu Y ($90^\circ$ & $270^\circ$) $\to$ *FUNGSI BERUBAH KE KOFUNGSI*

Jika menggunakan patokan sumbu Y, nama fungsi berganti menjadi kofungsinya:
$$\sin \leftrightarrow \cos, \quad \tan \leftrightarrow \cot, \quad \sec \leftrightarrow \csc$$
Tanda $+/-$ **tetap ditentukan oleh kuadran fungsi asalnya!**

* **Kuadran I ($90^\circ - \alpha$):**
  $$\sin(90^\circ - \alpha) = \cos \alpha, \quad \cos(90^\circ - \alpha) = \sin \alpha, \quad \tan(90^\circ - \alpha) = \cot \alpha$$

* **Kuadran II ($90^\circ + \alpha$):**
  $$\sin(90^\circ + \alpha) = +\cos \alpha \quad (\text{karena sinus di Kuadran II positif})$$
  $$\cos(90^\circ + \alpha) = -\sin \alpha \quad (\text{karena cosinus di Kuadran II negatif})$$
  $$\tan(90^\circ + \alpha) = -\cot \alpha$$

---

## 4. Sudut Negatif ($-\alpha$) & Sifat Paritas Fungsi

Sudut negatif $-\alpha$ merepresentasikan perputaran **searah jarum jam** dari sumbu X positif, yang langsung masuk ke **Kuadran IV**.

Karena di Kuadran IV nilai koordinat $x$ (kosinus) tetap positif sedangkan nilai $y$ (sinus) menjadi negatif:
1. **Fungsi Genap (*Even Function*):**
   $$\mathbf{\cos(-\alpha) = \cos \alpha} \quad \text{dan} \quad \sec(-\alpha) = \sec \alpha$$
2. **Fungsi Ganjil (*Odd Function*):**
   $$\mathbf{\sin(-\alpha) = -\sin \alpha} \quad \text{dan} \quad \csc(-\alpha) = -\csc \alpha$$
   $$\mathbf{\tan(-\alpha) = -\tan \alpha} \quad \text{dan} \quad \cot(-\alpha) = -\cot \alpha$$

---

## 5. Sudut Lebih dari $360^\circ$ (Sudut Periodik / Berputar Penuh)

Karena satu putaran penuh lingkaran bernilai $360^\circ$ ($2\pi\text{ radian}$), posisi titik akan berulang setiap kali melakukan putaran lengkap sebanyak $k$ kali ($k \in \mathbb{Z}$):

$$\sin(k \cdot 360^\circ + \alpha) = \sin \alpha$$
$$\cos(k \cdot 360^\circ + \alpha) = \cos \alpha$$
$$\tan(k \cdot 180^\circ + \alpha) = \tan \alpha \quad (\text{periode tangen adalah } 180^\circ)$$

---

## 6. Contoh Soal Berpola & Pembahasan

### Contoh 1: Menentukan Nilai Eksak Sudut di Berbagai Kuadran
**Soal:** Hitung nilai eksak dari:
1. $\sin 150^\circ$
2. $\cos 225^\circ$
3. $\tan 300^\circ$
4. $\cos(-60^\circ)$
5. $\sin 750^\circ$

**Langkah Pembahasan:**
1. **$\sin 150^\circ$:** 
   * Kuadran II (Sinus bernilai $+$).
   * Relasi sumbu X: $\sin(180^\circ - 30^\circ) = +\sin 30^\circ = \mathbf{\frac{1}{2}}$.
2. **$\cos 225^\circ$:**
   * Kuadran III (Cosinus bernilai $-$).
   * Relasi sumbu X: $\cos(180^\circ + 45^\circ) = -\cos 45^\circ = \mathbf{-\frac{1}{2}\sqrt{2}}$.
3. **$\tan 300^\circ$:**
   * Kuadran IV (Tangen bernilai $-$).
   * Relasi sumbu X: $\tan(360^\circ - 60^\circ) = -\tan 60^\circ = \mathbf{-\sqrt{3}}$.
4. **$\cos(-60^\circ)$:**
   * Sifat fungsi genap: $\cos(-60^\circ) = \cos 60^\circ = \mathbf{\frac{1}{2}}$.
5. **$\sin 750^\circ$:**
   * Sudut periodik: $750^\circ = 2 \cdot 360^\circ + 30^\circ$.
   * $\sin(2 \cdot 360^\circ + 30^\circ) = \sin 30^\circ = \mathbf{\frac{1}{2}}$.

---

### Contoh 2: Menyederhanakan Ekspresi Trigonometri Simbolik
**Soal:** Sederhanakan bentuk berikut:
$$\frac{\sin(180^\circ - x) \cdot \cos(90^\circ + x)}{\tan(360^\circ - x) \cdot \sin(270^\circ - x)}$$

**Langkah Pembahasan:**
1. Urai setiap suku berdasarkan relasi kuadrannya:
   * $\sin(180^\circ - x) = \sin x$ (Kuadran II, $+$)
   * $\cos(90^\circ + x) = -\sin x$ (Kuadran II, $-$, sumbu Y ubah ke sinus)
   * $\tan(360^\circ - x) = -\tan x$ (Kuadran IV, $-$)
   * $\sin(270^\circ - x) = -\cos x$ (Kuadran III, $-$, sumbu Y ubah ke cosinus)
2. Masukkan ke dalam pecahan:
   $$\text{Pembilang} = (\sin x) \cdot (-\sin x) = -\sin^2 x$$
   $$\text{Penyebut} = (-\tan x) \cdot (-\cos x) = \left(-\frac{\sin x}{\cos x}\right) \cdot (-\cos x) = \sin x$$
3. Hitung hasil bagi:
   $$\frac{-\sin^2 x}{\sin x} = \mathbf{-\sin x}$$

---

## 7. Rangkuman Kaidah Sudut Berelasi

1. Lingkaran satuan menghubungkan sudut putar dengan titik kartesius $(\cos \theta, \sin \theta)$.
2. Hafalkan kata kunci kuadran: **Semua (I) $\to$ Sin (II) $\to$ Tan (III) $\to$ Cos (IV)**.
3. Gunakan selalu patokan horizontal $180^\circ \pm \alpha$ dan $360^\circ \pm \alpha$ agar nama fungsi tidak berubah.
4. Cosinus adalah fungsi genap ($\cos(-\alpha) = \cos \alpha$), sedangkan Sinus dan Tangen adalah fungsi ganjil ($\sin(-\alpha) = -\sin \alpha$).

---

> **Bilah Navigasi:**
> [[Trigonometri_SMA|🏠 Master Dashboard]] | [[Perbandingan_Trigonometri_dan_Sudut_Istimewa_SMA|⬅️ Modul 1: Rasio Dasar]] | **Modul 2: Sudut Berelasi** | [[Identitas_dan_Rumus_Jumlah_Selisih_Sudut_SMA|Modul 3: Identitas Analitik ➡️]] | [[LKPD_Trigonometri_SMA|📝 LKPD]]
