---
title: "Pemfaktoran Polinomial dan Mencari Akar Rasional"
type: materi
subject: Mathematics
level: sma
target_audience: "SMA Kelas 11"
created: 2026-08-20
sources:
  - "[[Suku Banyak Polinomial SMA]]"
tags:
  - teaching-material
  - mathematics
  - suku-banyak
  - polinomial
  - pemfaktoran
  - akar-rasional
---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | [[Teorema_Sisa_dan_Faktor_SMA|⬅️ Teorema Sisa]] | Modul Ini | [[Teorema_Vieta_Polinomial_SMA|Teorema Vieta ➡️]] | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]

# Pemfaktoran Polinomial & Mencari Akar Rasional 🕵️‍♂️

Di SMP, kamu sudah mahir memfaktorkan persamaan kuadrat ($x^2$). Namun, bagaimana jika kamu diminta memfaktorkan persamaan derajat tinggi, seperti pangkat 3 (kubik) atau pangkat 4 (kuartik)?

Misalnya, tentukan semua akar dari $x^3 - 4x^2 + x + 6 = 0$!

Tenang, kita punya prosedur rahasianya: **Teorema Akar Rasional** dikombinasikan dengan **Metode Horner** dan **Teorema Faktor**.

---

## 1. Teorema Akar Rasional (Jurus Tebak Jitu)

Kita tidak bisa memfaktorkan pangkat tiga secara langsung. Kita harus "menebak" minimal satu akar pertama ($x = k$) yang tepat, sehingga sisa pembagiannya $0$ (Teorema Faktor).

Masalahnya, dari sekian banyak angka di dunia (1, 2, -100, 3.5), angka mana yang harus dicoba?

> **Trik Teorema Akar Rasional:**  
> Calon-calon akar bilangan rasional ($x = \frac{p}{q}$) hanyalah berasal dari kombinasi:
> $$x = \pm \frac{\text{Faktor dari Konstanta (suku terakhir)}}{\text{Faktor dari Koefisien Utama (suku pertama)}}$$

**Contoh:** Untuk persamaan $2x^3 + \dots - 6 = 0$
* Konstanta terakhir = $-6$. Faktornya: $\pm 1, \pm 2, \pm 3, \pm 6$.
* Koefisien utama = $2$. Faktornya: $\pm 1, \pm 2$.
* Maka kemungkinan akarnya berkisar di pembagian angka-angka tersebut, seperti $1, -1, 2, \frac{1}{2}, \frac{3}{2},$ dst.

*Pro Tip:* **Selalu** mulai uji coba dari angka terkecil dan termudah, yaitu **$x = 1$** dan **$x = -1$**.

---

## 2. Langkah Sistematis Pemfaktoran Pangkat Tinggi

Mari kita bedah penyelesaian dari soal $x^3 - 4x^2 + x + 6 = 0$.

### Langkah 1: Daftar Calon Akar (Pembuat Nol)
* Konstanta akhir $= 6$. Koefisien utama $= 1$.
* Calon akar: Faktor dari 6 dibagi 1, yaitu $\pm 1, \pm 2, \pm 3, \pm 6$.

### Langkah 2: Uji Akar Pertama dengan Skema Horner
Uji dari yang termudah: $x = 1$.
* Koefisien: $1, -4, 1, 6$

```text
 1 |  1   -4    1    6
   |       1   -3   -2
   ------------------- (+)
      1   -3   -2  | 4   <-- SISA BUKAN 0!
```
Karena Sisa $= 4$, maka $x = 1$ **bukan akar**.

Lanjut uji $x = -1$:
```text
 -1 |  1   -4    1    6
    |      -1    5   -6
    ------------------- (+)
       1   -5    6  | 0   <-- SISA = 0! BINGO! 🎉
```
Karena Sisa $= 0$, maka **$x = -1$ adalah akar pertama**, dan **$(x + 1)$ adalah faktor pertama**.

### Langkah 3: Ambil Hasil Bagi untuk Faktor Selanjutnya
Lihat baris hasil di skema Horner yang berhasil tadi: angkanya adalah `1, -5, 6`.
Karena polinomial asli pangkat 3, maka hasil baginya turun 1 tingkat menjadi pangkat 2 (kuadrat).
$$H(x) = x^2 - 5x + 6$$

Nah, polinomial sudah turun jadi persamaan kuadrat. Dari sini, kamu bebas mau pakai Horner lagi, atau langsung difaktorkan cara biasa ala SMP!
$$x^2 - 5x + 6 = 0$$
$$(x - 2)(x - 3) = 0$$
Diperoleh akar lainnya: $x = 2$ dan $x = 3$.

### Langkah 4: Tuliskan Kesimpulan
* **Faktor-Faktor dari Polinomial:** $(x + 1)(x - 2)(x - 3)$
* **Akar-Akar Persamaan (Himpunan Penyelesaian):** $x = \{-1, 2, 3\}$

---

## 📝 Ringkasan Prosedur
Jika kamu berhadapan dengan pangkat 4, lakukan prosedur Horner yang sama berulang dua kali, sampai hasil baginya mengerucut menjadi persamaan kuadrat ($x^2$) yang bisa diselesaikan dengan mudah!

---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | [[Teorema_Sisa_dan_Faktor_SMA|⬅️ Teorema Sisa]] | Modul Ini | [[Teorema_Vieta_Polinomial_SMA|Teorema Vieta ➡️]] | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]
