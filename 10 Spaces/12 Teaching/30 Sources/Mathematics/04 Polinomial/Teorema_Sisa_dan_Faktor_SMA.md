---
title: "Teorema Sisa dan Teorema Faktor"
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
  - teorema-sisa
  - teorema-faktor
---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | [[Metode_Horner_dan_Operasi_SMA|⬅️ Metode Horner]] | Modul Ini | [[Pemfaktoran_dan_Akar_Rasional_SMA|Pemfaktoran Polinomial ➡️]] | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]

# Teorema Sisa dan Teorema Faktor 🎯

Setelah menguasai pembagian polinomial menggunakan Skema Horner, sekarang kita akan berkenalan dengan dua teorema yang menjadi "jantung" dari soal-soal HOTS polinomial: **Teorema Sisa** dan **Teorema Faktor**.

---

## 1. Teorema Sisa

Tanpa harus melakukan pembagian panjang atau skema Horner secara utuh, kita bisa **menebak** langsung berapa sisa pembagian dari suatu polinomial hanya dengan mensubstitusikan nilai tertentu!

> **Teorema Sisa I (Pembagi Linear $x - k$):**  
> Jika polinomial $P(x)$ dibagi oleh $(x - k)$, maka sisa pembagiannya adalah **$S = P(k)$**.

> **Teorema Sisa II (Pembagi Linear $ax + b$):**  
> Jika polinomial $P(x)$ dibagi oleh $(ax + b)$, maka sisa pembagiannya adalah **$S = P\left(-\frac{b}{a}\right)$**.

### 📝 Contoh Soal Teorema Sisa:
Jika $P(x) = x^3 - 2x^2 + 4x - 5$ dibagi $(x - 2)$, maka sisanya adalah:
$$S = P(2) = (2)^3 - 2(2)^2 + 4(2) - 5 = 8 - 8 + 8 - 5 = 3$$

---

## 2. Teorema Sisa Lanjutan (Pembagi Derajat Dua / Kuadrat)

Soal ujian seringkali menampilkan pembagi yang bentuknya kuadrat, misalnya $(x^2 - 4)$ atau $(x^2 - x - 6)$. Apa yang terjadi pada sisanya?

> **Prinsip Penting:** Derajat dari sisa pembagian maksimal **selalu 1 tingkat lebih rendah** dari derajat pembagi.
> * Jika pembagi berderajat 1 (linear), sisa adalah **angka/konstanta** ($S$).
> * Jika pembagi berderajat 2 (kuadrat), sisa berbentuk **persamaan linear** ($S(x) = px + q$).

### 📝 Trik Cepat Pembagi Kuadrat (Jika Bisa Difaktorkan)

**Soal:**  
Suatu suku banyak $P(x)$ jika dibagi $(x - 2)$ bersisa 5, dan jika dibagi $(x + 1)$ bersisa -4. Tentukan sisa pembagian $P(x)$ oleh $(x^2 - x - 2)$!

**Penyelesaian:**
1. Faktorkan pembagi derajat dua: $x^2 - x - 2 = (x - 2)(x + 1)$. (Sama persis dengan pembagi yang diketahui di soal!)
2. Karena pembaginya derajat 2, misal sisa pembagiannya adalah **$S(x) = ax + b$**.
3. Gunakan Teorema Sisa dari data yang diketahui:
   * Dibagi $(x - 2) \implies k = 2$, sisanya 5. Maka $P(2) = 2a + b = 5$.
   * Dibagi $(x + 1) \implies k = -1$, sisanya -4. Maka $P(-1) = -a + b = -4$.
4. Lakukan Eliminasi Persamaan:
   $$2a + b = 5$$
   $$-a + b = -4$$
   (Kurangkan) $\implies 3a = 9 \implies \mathbf{a = 3}$
5. Substitusi nilai $a$:
   $2(3) + b = 5 \implies 6 + b = 5 \implies \mathbf{b = -1}$
6. Jadi, sisa pembagiannya adalah $S(x) = ax + b = \mathbf{3x - 1}$.

---

## 3. Teorema Faktor

Teorema faktor sangat berguna untuk mencari akar-akar dari suatu polinomial.

> **Teorema Faktor:**  
> Polinomial $(x - k)$ merupakan **faktor** dari polinomial $P(x)$ **jika dan hanya jika** Sisa Pembagiannya sama dengan nol ($S = P(k) = 0$).

Analogi: Sama seperti 3 adalah faktor dari 12 karena 12 dibagi 3 sisanya 0. Tetapi 5 bukan faktor dari 12 karena bersisa 2.

### 📝 Contoh Soal Teorema Faktor:
Tentukan nilai $m$ agar $(x - 1)$ menjadi faktor dari $P(x) = 2x^3 - mx^2 + 5x - 3$.

**Penyelesaian:**
Agar menjadi faktor, maka syarat mutlaknya: **$P(1) = 0$**.
$$2(1)^3 - m(1)^2 + 5(1) - 3 = 0$$
$$2 - m + 5 - 3 = 0$$
$$4 - m = 0 \implies \mathbf{m = 4}$$

Sangat mudah bukan? Di modul berikutnya, kita akan menggunakan Teorema Faktor ini sebagai senjata utama untuk memecahkan dan mencari seluruh akar polinomial derajat tinggi secara sistematis!

---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | [[Metode_Horner_dan_Operasi_SMA|⬅️ Metode Horner]] | Modul Ini | [[Pemfaktoran_dan_Akar_Rasional_SMA|Pemfaktoran Polinomial ➡️]] | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]
