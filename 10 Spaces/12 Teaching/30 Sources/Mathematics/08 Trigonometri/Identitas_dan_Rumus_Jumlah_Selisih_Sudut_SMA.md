---
title: "Identitas dan Rumus Jumlah-Selisih Sudut SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 11 (Fase F), Guru Matematika, dan Persiapan UTBK-SNBT"
created: 2026-09-01
sources:
  - "[[Trigonometri_SMA]]"
  - "[[Sudut_Berelasi_dan_Lingkaran_Satuan_SMA]]"
  - "[[Aturan_Sinus_Cosinus_dan_Luas_Segitiga_SMA]]"
  - "[[Grafik_Fungsi_dan_Persamaan_Trigonometri_SMA]]"
  - "[[LKPD_Trigonometri_SMA]]"
tags:
  - teaching/mathematics
  - mathematics/trigonometry
  - level/sma
  - topic/trig-identities
---

> **Bilah Navigasi:**
> [[Trigonometri_SMA|🏠 Master Dashboard]] | [[Sudut_Berelasi_dan_Lingkaran_Satuan_SMA|⬅️ Modul 2: Sudut Berelasi]] | **Modul 3: Identitas Analitik** | [[Aturan_Sinus_Cosinus_dan_Luas_Segitiga_SMA|Modul 4: Segitiga Sebarang ➡️]] | [[LKPD_Trigonometri_SMA|📝 LKPD]]

---

# Identitas dan Rumus Jumlah-Selisih Sudut — Aljabar Analitik & Transformasi Trigonometri 🧪🔢

Ketika memasuki jenjang Fase F (Kelas 11), trigonometri berevolusi dari sekadar geometri bangun datar menjadi **alat manipulasi aljabar analitik yang sangat kuat**. 

Banyak fenomena gelombang di alam—seperti interferensi suara (dua nada berpadu menghasilkan kenyaringan baru) atau modulasi sinyal radio FM/AM—memerlukan kemampuan untuk mengubah perkalian dua gelombang menjadi penjumlahan gelombang sederhana, atau mengurai sudut gabungan seperti $\sin(75^\circ)$ tanpa menggunakan kalkulator.

---

## 1. Tiga Identitas Pythagoras Fundamental

Identitas trigonometri adalah persamaan yang selalu bernilai benar untuk setiap nilai variabel sudut yang terdefinisi.

Berawal dari persamaan lingkaran satuan $x^2 + y^2 = 1$, dengan mensubstitusikan $x = \cos \alpha$ dan $y = \sin \alpha$:

### Identitas Utama 1:
$$\mathbf{\sin^2 \alpha + \cos^2 \alpha = 1}$$

Dari identitas utama ini, kita bisa menurunkan dua identitas turunan:

1. **Bagi kedua ruas dengan $\cos^2 \alpha$:**
   $$\frac{\sin^2 \alpha}{\cos^2 \alpha} + \frac{\cos^2 \alpha}{\cos^2 \alpha} = \frac{1}{\cos^2 \alpha} \implies \mathbf{1 + \tan^2 \alpha = \sec^2 \alpha}$$

2. **Bagi kedua ruas dengan $\sin^2 \alpha$:**
   $$\frac{\sin^2 \alpha}{\sin^2 \alpha} + \frac{\cos^2 \alpha}{\sin^2 \alpha} = \frac{1}{\sin^2 \alpha} \implies \mathbf{1 + \cot^2 \alpha = \csc^2 \alpha}$$

> [!TIP]
> **Bentuk Modifikasi Cepat yang Sering Dipakai:**
> * $\sin^2 \alpha = 1 - \cos^2 \alpha = (1 - \cos \alpha)(1 + \cos \alpha)$
> * $\cos^2 \alpha = 1 - \sin^2 \alpha = (1 - \sin \alpha)(1 + \sin \alpha)$
> * $\sec^2 \alpha - \tan^2 \alpha = 1 \iff (\sec \alpha - \tan \alpha)(\sec \alpha + \tan \alpha) = 1$

---

## 2. Rumus Jumlah dan Selisih Dua Sudut

> [!WARNING]
> **Awas Kesalahan Fatal Pemula!**
> $\sin(\alpha + \beta) \mathbf{\ne} \sin \alpha + \sin \beta$. Trigonometri adalah fungsi non-linear!

### A. Rumus Sinus Jumlah & Selisih
$$\mathbf{\sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta}$$
$$\mathbf{\sin(\alpha - \beta) = \sin \alpha \cos \beta - \cos \alpha \sin \beta}$$
*(Pola: Sin-Cos $\pm$ Cos-Sin, tanda operasi sama)*

### B. Rumus Kosinus Jumlah & Selisih
$$\mathbf{\cos(\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta}$$
$$\mathbf{\cos(\alpha - \beta) = \cos \alpha \cos \beta + \sin \alpha \sin \beta}$$
*(Pola: Cos-Cos $\mp$ Sin-Sin, tanda operasi berlawanan)*

### C. Rumus Tangen Jumlah & Selisih
$$\mathbf{\tan(\alpha + \beta) = \frac{\tan \alpha + \tan \beta}{1 - \tan \alpha \tan \beta}}$$
$$\mathbf{\tan(\alpha - \beta) = \frac{\tan \alpha - \tan \beta}{1 + \tan \alpha \tan \beta}}$$

---

## 3. Rumus Sudut Rangkap (*Double Angle*)

Jika kita menetapkan $\beta = \alpha$ pada rumus jumlah sudut, kita memperoleh formula sudut rangkap ($2\alpha$):

### 1. Sinus Sudut Rangkap
$$\sin(2\alpha) = \sin(\alpha + \alpha) = \sin \alpha \cos \alpha + \cos \alpha \sin \alpha \implies \mathbf{\sin(2\alpha) = 2 \sin \alpha \cos \alpha}$$

### 2. Kosinus Sudut Rangkap (Memiliki 3 Wajah!)
$$\cos(2\alpha) = \cos(\alpha + \alpha) = \cos \alpha \cos \alpha - \sin \alpha \sin \alpha \implies \mathbf{\cos(2\alpha) = \cos^2 \alpha - \sin^2 \alpha}$$

Dengan mensubstitusikan identitas $\cos^2 \alpha = 1 - \sin^2 \alpha$ atau $\sin^2 \alpha = 1 - \cos^2 \alpha$:
* Wujud 2: $\mathbf{\cos(2\alpha) = 2\cos^2 \alpha - 1}$
* Wujud 3: $\mathbf{\cos(2\alpha) = 1 - 2\sin^2 \alpha}$

### 3. Tangen Sudut Rangkap
$$\mathbf{\tan(2\alpha) = \frac{2\tan \alpha}{1 - \tan^2 \alpha}}$$

> [!IMPORTANT]
> **Rumus Penurun Derajat / Linearitas Pangkat (Power-Reduction Formula):**
> Bentuk ini sangat krusial saat mempelajari kalkulus integral di kelas 12:
> $$\mathbf{\sin^2 \alpha = \frac{1 - \cos(2\alpha)}{2}} \quad \text{dan} \quad \mathbf{\cos^2 \alpha = \frac{1 + \cos(2\alpha)}{2}}$$

---

## 4. Rumus Sudut Paruh / Setengah Sudut ($\frac{\alpha}{2}$)

Dengan mengganti $\alpha$ menjadi $\frac{\alpha}{2}$ pada rumus penurun derajat di atas:

$$\mathbf{\sin\left(\frac{\alpha}{2}\right) = \pm \sqrt{\frac{1 - \cos \alpha}{2}}}$$
$$\mathbf{\cos\left(\frac{\alpha}{2}\right) = \pm \sqrt{\frac{1 + \cos \alpha}{2}}}$$
$$\mathbf{\tan\left(\frac{\alpha}{2}\right) = \frac{\sin \alpha}{1 + \cos \alpha} = \frac{1 - \cos \alpha}{\sin \alpha}}$$
*(Tanda $\pm$ dipilih berdasarkan kuadran tempat sudut $\frac{\alpha}{2}$ berada).*

---

## 5. Rumus Konversi: Perkalian $\longleftrightarrow$ Penjumlahan

### A. Rumus Perkalian ke Penjumlahan (Product-to-Sum)

$$2\sin A \cos B = \sin(A+B) + \sin(A-B)$$
$$2\cos A \sin B = \sin(A+B) - \sin(A-B)$$
$$2\cos A \cos B = \cos(A+B) + \cos(A-B)$$
$$-2\sin A \sin B = \cos(A+B) - \cos(A-B)$$

### B. Rumus Penjumlahan ke Perkalian (Sum-to-Product / Rumus Simpson)

Misalkan $C = A+B$ dan $D = A-B$, sehingga $A = \frac{C+D}{2}$ dan $B = \frac{C-D}{2}$:

$$\sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right)$$
$$\sin C - \sin D = 2 \cos\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right)$$
$$\cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right)$$
$$\cos C - \cos D = -2 \sin\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right)$$

---

## 6. Contoh Soal Berpola & Pembahasan

### Contoh 1: Menghitung Nilai Eksak Sudut Non-Istimewa ($75^\circ$ dan $15^\circ$)
**Soal:** Tentukan nilai eksak dari $\sin 75^\circ$ dan $\cos 15^\circ$.

**Langkah Pembahasan:**
1. Urai $75^\circ = 45^\circ + 30^\circ$:
   $$\sin 75^\circ = \sin(45^\circ + 30^\circ) = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ$$
   $$\sin 75^\circ = \left(\frac{1}{2}\sqrt{2}\right)\left(\frac{1}{2}\sqrt{3}\right) + \left(\frac{1}{2}\sqrt{2}\right)\left(\frac{1}{2}\right) = \mathbf{\frac{\sqrt{6} + \sqrt{2}}{4}}$$
2. Urai $15^\circ = 45^\circ - 30^\circ$:
   $$\cos 15^\circ = \cos(45^\circ - 30^\circ) = \cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ$$
   $$\cos 15^\circ = \left(\frac{1}{2}\sqrt{2}\right)\left(\frac{1}{2}\sqrt{3}\right) + \left(\frac{1}{2}\sqrt{2}\right)\left(\frac{1}{2}\right) = \mathbf{\frac{\sqrt{6} + \sqrt{2}}{4}}$$
*(Terbukti bahwa $\sin 75^\circ = \cos 15^\circ$ karena keduanya saling berkomplemen $90^\circ - 15^\circ = 75^\circ$).*

---

### Contoh 2: Membuktikan Identitas Trigonometri Kompleks
**Soal:** Buktikan bahwa:
$$\frac{\sin(3x) + \sin x}{\cos(3x) + \cos x} = \tan(2x)$$

**Langkah Pembahasan:**
1. Mulai dari ruas kiri (LHS) menggunakan rumus penjumlahan ke perkalian (Sum-to-Product):
   * Pembilang: $\sin(3x) + \sin x = 2 \sin\left(\frac{3x+x}{2}\right) \cos\left(\frac{3x-x}{2}\right) = 2 \sin(2x) \cos(x)$
   * Penyebut: $\cos(3x) + \cos x = 2 \cos\left(\frac{3x+x}{2}\right) \cos\left(\frac{3x-x}{2}\right) = 2 \cos(2x) \cos(x)$
2. Masukkan kembali ke bentuk pecahan:
   $$\text{LHS} = \frac{2 \sin(2x) \cos(x)}{2 \cos(2x) \cos(x)}$$
3. Coret faktor persekutuan $2\cos(x)$:
   $$\text{LHS} = \frac{\sin(2x)}{\cos(2x)} = \tan(2x) = \text{RHS} \quad \mathbf{[TERBUKTI]}$$

---

## 7. Strategi Membuktikan Identitas Trigonometri

1. **Pilih Ruas yang Lebih Rumit:** Selalu mulai memanipulasi ruas yang terlihat lebih panjang atau banyak suku untuk disederhanakan menuju ruas yang lebih ringkas.
2. **Ubah ke Sinus dan Kosinus:** Jika buntu dengan $\tan, \cot, \sec, \csc$, ubah semuanya ke bentuk pecahan berbasis $\sin$ dan $\cos$.
3. **Samakan Penyebut:** Jika ada penjumlahan pecahan aljabar trigonometri, lakukan penyamaan penyebut terlebih dahulu.
4. **Faktorkan & Kenali Bentuk Selisih Kuadrat:** Manfaatkan $(a^2 - b^2) = (a-b)(a+b)$ bersama dengan identitas Pythagoras.

---

> **Bilah Navigasi:**
> [[Trigonometri_SMA|🏠 Master Dashboard]] | [[Sudut_Berelasi_dan_Lingkaran_Satuan_SMA|⬅️ Modul 2: Sudut Berelasi]] | **Modul 3: Identitas Analitik** | [[Aturan_Sinus_Cosinus_dan_Luas_Segitiga_SMA|Modul 4: Segitiga Sebarang ➡️]] | [[LKPD_Trigonometri_SMA|📝 LKPD]]
