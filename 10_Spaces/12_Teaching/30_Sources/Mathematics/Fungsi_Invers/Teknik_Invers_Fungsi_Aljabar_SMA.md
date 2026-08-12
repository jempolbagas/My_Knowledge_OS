---
title: "Teknik Menentukan Fungsi Invers Aljabar"
type: "materi"
subject: "Mathematics"
level: "sma"
target_audience: "SMA Kelas 11 (Fase F)"
created: 2026-08-12
sources:
  - "[[Fungsi_Invers_SMA]]"
  - "[[Konsep_Dasar_dan_Syarat_Invers_SMA]]"
tags:
  - "#matematika"
  - "#fungsi_invers"
  - "#aljabar"
  - "#rumus_cepat"
  - "#kelas11"
---

[[Fungsi_Invers_SMA|🏠 Master Dashboard]] | [[Konsep_Dasar_dan_Syarat_Invers_SMA|⬅️ Modul 1: Konsep]] | **Modul 2: Teknik Aljabar** | [[Invers_Fungsi_Komposisi_dan_Aplikasi_SMA|Modul 3: Invers Komposisi ➡️]] | [[LKPD_Fungsi_Invers_SMA|📝 LKPD]]

---

# Modul 2: Teknik Aljabar Fungsi Invers — Prosedur 4 Langkah & Rumus Cepat! 🛠️📐

> Setelah memahami konsep dasar mesin undo pada Modul 1, sekarang saatnya kita menguasai **teknik aljabar** untuk membongkar dan membalikkan berbagai bentuk persamaan matematika!

---

## 🔑 Prosedur Umum 4 Langkah Menentukan \(f^{-1}(x)\)

Apapun jenis fungsinya (linier, pecahan, kuadrat, atau eksponen), langkah-langkah aljabar dasar untuk mencari invers selalu mengikuti **Prosedur 4 Langkah Standar**:

```text
[Langkah 1] Ganti f(x) dengan variabel y:
            y = f(x)

[Langkah 2] Lakukan manipulasi aljabar untuk mengisolasi variabel x di ruas kiri:
            x = (ekspresi matematika dalam y)

[Langkah 3] Ganti variabel x menjadi f^-1(y):
            f^-1(y) = (ekspresi matematika dalam y)

[Langkah 4] Ganti seluruh variabel y kembali menjadi x:
            f^-1(x) = (ekspresi matematika dalam x)
```

---

## 1. Invers Fungsi Linier

Fungsi linier memiliki bentuk umum \(f(x) = ax + b\) dengan \(a \neq 0\).

### Penurunan Rumus:
1. Misalkan \(y = ax + b\)
2. Pindahkan \(b\) ke ruas kiri:  
   \(y - b = ax\)
3. Bagi kedua ruas dengan \(a\):  
   \(x = \frac{y - b}{a}\)
4. Maka diperoleh rumus invers:
   $$ f^{-1}(x) = \frac{x - b}{a} $$

#### Contoh Soal 1 (Linier):
Tentukan invers dari fungsi \(f(x) = \frac{3x - 5}{2}\)!

**Pembahasan:**
Misalkan \(y = \frac{3x - 5}{2}\)  
\(2y = 3x - 5\)  
\(3x = 2y + 5\)  
\(x = \frac{2y + 5}{3}\)  

Maka, \(f^{-1}(x) = \frac{2x + 5}{3}\).

---

## 2. Invers Fungsi Pecahan Rasional

Fungsi pecahan rasional memiliki bentuk umum:
$$ f(x) = \frac{ax + b}{cx + d}, \quad x \neq -\frac{d}{c} $$

### Penurunan Rumus Aljabar (Lengkap):
1. Misalkan \(y = \frac{ax + b}{cx + d}\)
2. Kalikan silang pembagi ke ruas kiri:  
   \(y(cx + d) = ax + b\)  
   \(cxy + dy = ax + b\)
3. Kelompokkan suku yang memuat variabel \(x\) ke ruas kiri, dan suku lainnya ke ruas kanan:  
   \(cxy - ax = b - dy\)
4. Faktorkan variabel \(x\) keluar di ruas kiri:  
   \(x(cy - a) = -dy + b\)
5. Isolasi \(x\):  
   \(x = \frac{-dy + b}{cy - a}\)
6. Ubah variabel \(y\) menjadi \(x\):
   $$ f^{-1}(x) = \frac{-dx + b}{cx - a}, \quad x \neq \frac{a}{c} $$

> 💡 **Trik Rumus Cepat (Super Quick Trick):**  
> Untuk bentuk \(f(x) = \frac{ax + b}{cx + d}\), cukup **tukar posisi elemen diagonal utama \(a\) dan \(d\)**, lalu **ubah tandanya (kalikan \(-1\))**!  
> * Element \(a\) di kiri atas turun ke kanan bawah menjadi \(-a\).  
> * Element \(d\) di kanan bawah naik ke kiri atas menjadi \(-d\).  
> * Elemen \(b\) dan \(c\) tetap di posisinya!

#### Contoh Soal 2 (Pecahan Rasional):
Tentukan invers dari fungsi \(g(x) = \frac{4x + 3}{2x - 5}, x \neq \frac{5}{2}\)!

**Pembahasan (Menggunakan Trik Cepat):**
Dari fungsi \(g(x) = \frac{4x + 3}{2x - 5}\):
- \(a = 4\), \(b = 3\), \(c = 2\), \(d = -5\)

Tukar \(a = 4\) dan \(d = -5\) serta balik tandanya:
- \(-d = -(-5) = 5\)
- \(-a = -(4) = -4\)

Maka diperoleh:
$$ g^{-1}(x) = \frac{5x + 3}{2x - 4}, \quad x \neq 2 $$

---

## 3. Invers Fungsi Kuadrat (Dengan Pembatasan Domain)

Bentuk umum fungsi kuadrat adalah \(f(x) = ax^2 + bx + c\). Karena grafik fungsi kuadrat berupa parabola simetris, fungsi ini baru memiliki fungsi invers jika domainnya dibatasi (agar memenuhi syarat bijektif).

### Metode Melengkapkan Kuadrat Sempurna:
Ubah bentuk kuadrat umum menjadi bentuk puncak:
$$ f(x) = a(x - h)^2 + k $$

#### Penurunan Rumus Invers:
1. Misalkan \(y = a(x - h)^2 + k\)
2. \(y - k = a(x - h)^2\)
3. \(\frac{y - k}{a} = (x - h)^2\)
4. Ambil akar kuadrat kedua ruas:  
   \(x - h = \pm \sqrt{\frac{y - k}{a}}\)
5. \(x = h \pm \sqrt{\frac{y - k}{a}}\)

Maka rumus inversnya adalah:
$$ f^{-1}(x) = h + \sqrt{\frac{x - k}{a}} \quad \text{(diambil tanda positif jika domain awal } x \geq h \text{)} $$

#### Contoh Soal 3 (Fungsi Kuadrat):
Tentukan invers dari fungsi \(f(x) = x^2 - 6x + 5\) untuk domain \(x \geq 3\)!

**Pembahasan:**
1. Lengkapkan kuadrat sempurna dari \(f(x)\):  
   \(f(x) = (x^2 - 6x + 9) - 9 + 5\)  
   \(f(x) = (x - 3)^2 - 4\)

2. Lakukan prosedur aljabar:  
   \(y = (x - 3)^2 - 4\)  
   \(y + 4 = (x - 3)^2\)  
   \(x - 3 = \sqrt{y + 4}\) *(pilih tanda \(+\) karena domain \(x \geq 3\))*  
   \(x = 3 + \sqrt{y + 4}\)

3. Maka diperoleh:
   $$ f^{-1}(x) = 3 + \sqrt{x + 4}, \quad x \geq -4 $$

---

## 4. Invers Fungsi Eksponen & Logaritma

Fungsi eksponen dan fungsi logaritma merupakan dua fungsi yang saling berinvers secara alami!

### Hubungan Utama:
$$ f(x) = a^x \quad \Longleftrightarrow \quad f^{-1}(x) = {}^a\log x, \quad x > 0 $$
$$ g(x) = {}^a\log(x + b) \quad \Longleftrightarrow \quad g^{-1}(x) = a^x - b $$

#### Contoh Soal 4 (Eksponen & Logaritma):
Tentukan invers dari fungsi logaritma \(h(x) = {}^3\log(2x - 1)\)!

**Pembahasan:**
1. Misalkan \(y = {}^3\log(2x - 1)\)
2. Gunakan definisi logaritma (\( {}^b\log a = c \iff b^c = a \)):  
   \(3^y = 2x - 1\)
3. Isolasi \(x\):  
   \(2x = 3^y + 1\)  
   \(x = \frac{3^y + 1}{2}\)

4. Maka diperoleh:
   $$ h^{-1}(x) = \frac{3^x + 1}{2} $$

---

## 📌 Ringkasan Matriks Rumus Cepat Aljabar

| Jenis Fungsi | Bentuk Asli \(f(x)\) | Bentuk Invers \(f^{-1}(x)\) | Catatan / Syarat |
| :--- | :--- | :--- | :--- |
| **Linier** | \(ax + b\) | \(\frac{x - b}{a}\) | \(a \neq 0\) |
| **Pecahan Rasional** | \(\frac{ax + b}{cx + d}\) | \(\frac{-dx + b}{cx - a}\) | \(x \neq \frac{a}{c}\), tukar & balik tanda \(a\) & \(d\) |
| **Bentuk Akar** | \(\sqrt[n]{ax + b}\) | \(\frac{x^n - b}{a}\) | \(x \geq 0\) untuk \(n\) genap |
| **Eksponen** | \(a^{px + q}\) | \(\frac{{}^a\log x - q}{p}\) | \(x > 0, a > 0, a \neq 1\) |

---

[[Fungsi_Invers_SMA|🏠 Master Dashboard]] | [[Konsep_Dasar_dan_Syarat_Invers_SMA|⬅️ Modul 1: Konsep]] | **Modul 2: Teknik Aljabar** | [[Invers_Fungsi_Komposisi_dan_Aplikasi_SMA|Modul 3: Invers Komposisi ➡️]] | [[LKPD_Fungsi_Invers_SMA|📝 LKPD]]
