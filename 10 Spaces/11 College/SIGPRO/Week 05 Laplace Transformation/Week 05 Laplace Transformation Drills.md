---
title: "Week 05: Active Recall & Practice Drills — Transformasi Laplace"
course: "Pengolahan Sinyal Digital"
course_abbr: "SIGPRO"
semester: 5
week: 5
date: "2026-08-19"
tags: ["college", "drills", "active-recall", "sigpro", "dsp", "laplace-transform", "semester-5"]
type: PracticeDrills
---

# 🧠 Week 05: Practice & Active Recall Drills — Transformasi Laplace

> [!info] **Master Note:** [[Week 05 Laplace Transformation Notes]] | **Cheatsheet:** [[Week 05 Laplace Transformation Cheatsheet]]
> Latihan soal berstandar Ujian Tengah Semester (UTS) universitas untuk menguji pemahaman konseptual, matematis, dan analisis sistem LTI dalam domain frekuensi kompleks $s$.

---

## 📋 Daftar Problem Set

---

### Problem 1: Penentuan ROC & Sifat Sinyal Domain Waktu
Diberikan fungsi alih $X(s)$ sebagai berikut:
$$
X(s) = \frac{s + 1}{(s + 2)(s - 4)}
$$
Tentukan seluruh kemungkinan wilayah konvergensi (ROC), gambarkan letak pole-zero-nya, serta jelaskan sifat sinyal $x(t)$ (kausal, anti-kausal, atau dua-sisi) dan stabilitasnya untuk setiap ROC yang mungkin!

<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**

1. **Analisis Pole dan Zero:**
   - **Zero:** $s = -1$
   - **Poles:** $p_1 = -2$ dan $p_2 = +4$

2. **Kemungkinan Wilayah Konvergensi (ROC):**
   Karena terdapat dua pole real di $s = -2$ dan $s = 4$, bidang-$s$ terbagi menjadi 3 wilayah ROC independen yang tidak memuat pole:

   - **Kasus A: $\text{Re}(s) > 4$ (Right-Sided / Kausal)**
     - **Sifat Sinyal:** $x(t)$ bersifat **kausal** (kanan).
     - **Stabilitas:** Karena ROC $\text{Re}(s) > 4$ tidak mencakup sumbu imajiner $\text{Re}(s) = 0$, maka sinyal/sistem ini **tidak stabil (unstable)**.
     - Form domain waktu: $x(t) = \left( A e^{-2t} + B e^{4t} \right) u(t)$.

   - **Kasus B: $-2 < \text{Re}(s) < 4$ (Two-Sided / Non-Kausal)**
     - **Sifat Sinyal:** $x(t)$ bersifat **dua-sisi** (non-kausal).
     - **Stabilitas:** ROC mencakup sumbu imajiner $\text{Re}(s) = 0$. Oleh karena itu, sinyal/sistem ini **stabil (BIBO Stable)**.
     - Form domain waktu: $x(t) = A e^{-2t} u(t) - B e^{4t} u(-t)$.

   - **Kasus C: $\text{Re}(s) < -2$ (Left-Sided / Anti-Kausal)**
     - **Sifat Sinyal:** $x(t)$ bersifat **anti-kausal** (kiri).
     - **Stabilitas:** ROC $\text{Re}(s) < -2$ tidak mencakup sumbu imajiner $\text{Re}(s) = 0$. Oleh karena itu, sinyal/sistem **tidak stabil (unstable)**.
     - Form domain waktu: $x(t) = \left( -A e^{-2t} - B e^{4t} \right) u(-t)$.
</details>

---

### Problem 2: Invers Transformasi Laplace dengan Pole Berulang (*Repeated Poles*)
Hitung invers Transformasi Laplace $f(t)$ dari ekspresi berikut (asumsikan sinyal kausal):
$$
F(s) = \frac{2s^2 + 5s + 4}{(s + 1)^2 (s + 2)}
$$

<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**

1. **Bentuk Ekspansi Pecahan Parsial (PFE):**
   Karena terdapat pole tunggal di $s = -2$ dan pole ganda di $s = -1$:
   $$
   F(s) = \frac{A}{s + 2} + \frac{B}{s + 1} + \frac{C}{(s + 1)^2}
   $$

2. **Hitung Koefisien $A$ (Cover-up Method pada $s = -2$):**
   $$
   A = \left. \frac{2s^2 + 5s + 4}{(s + 1)^2} \right|_{s = -2} = \frac{2(-2)^2 + 5(-2) + 4}{(-2 + 1)^2} = \frac{8 - 10 + 4}{1} = 2
   $$

3. **Hitung Koefisien $C$ (Cover-up Method pada $s = -1$):**
   $$
   C = \left. \frac{2s^2 + 5s + 4}{s + 2} \right|_{s = -1} = \frac{2(-1)^2 + 5(-1) + 4}{-1 + 2} = \frac{2 - 5 + 4}{1} = 1
   $$

4. **Hitung Koefisien $B$ (Turunan atau Substitusi Nilai $s$):**
   Menggunakan rumus turunan PFE untuk pole ganda:
   $$
   B = \left. \frac{d}{ds} \left[ \frac{2s^2 + 5s + 4}{s + 2} \right] \right|_{s = -1}
   $$
   $$
   \frac{d}{ds} \left[ \frac{2s^2 + 5s + 4}{s + 2} \right] = \frac{(4s + 5)(s + 2) - (2s^2 + 5s + 4)(1)}{(s + 2)^2}
   $$
   Evaluasi pada $s = -1$:
   $$
   B = \frac{(1)(1) - (1)(1)}{(1)^2} = 0
   $$

5. **Substitusi & Invers Laplace:**
   $$
   F(s) = \frac{2}{s + 2} + \frac{1}{(s + 1)^2}
   $$
   Dengan tabel transformasi dasar ($\mathcal{L}^{-1}\{\frac{1}{s+a}\} = e^{-at}u(t)$ dan $\mathcal{L}^{-1}\{\frac{1}{(s+a)^2}\} = t e^{-at} u(t)$):
   $$
   f(t) = \left( 2 e^{-2t} + t e^{-t} \right) u(t)
   $$
</details>

---

### Problem 3: Analisis Rangkaian RLC Kausal (Zero-State & Zero-Input Response)
Sebuah sistem LTI direpresentasikan oleh persamaan diferensial hubungan input-output:
$$
y''(t) + 4 y'(t) + 13 y(t) = 13 x(t)
$$
Jika diberikan kondisi awal $y(0^-) = 2$ dan $y'(0^-) = -4$, serta input $x(t) = u(t)$ (step function), tentukan:
a) Respon Masukan-Nol / Zero-Input Response ($y_{\text{ZIR}}(t)$)  
b) Respon Keadaan-Nol / Zero-State Response ($y_{\text{ZSR}}(t)$)  
c) Respon Total $y(t) = y_{\text{ZIR}}(t) + y_{\text{ZSR}}(t)$

<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**

1. **Transformasi Laplace Unilateral:**
   $$
   [s^2 Y(s) - s y(0^-) - y'(0^-)] + 4 [s Y(s) - y(0^-)] + 13 Y(s) = 13 X(s)
   $$
   Substitusi $y(0^-) = 2$ dan $y'(0^-) = -4$:
   $$
   [s^2 Y(s) - 2s - (-4)] + 4 [s Y(s) - 2] + 13 Y(s) = 13 X(s)
   $$
   $$
   Y(s) (s^2 + 4s + 13) - 2s + 4 - 8 = 13 X(s)
   $$
   $$
   Y(s) (s^2 + 4s + 13) = (2s + 4) + 13 X(s)
   $$
   $$
   Y(s) = \underbrace{\frac{2s + 4}{s^2 + 4s + 13}}_{Y_{\text{ZIR}}(s)} + \underbrace{\frac{13 X(s)}{s^2 + 4s + 13}}_{Y_{\text{ZSR}}(s)}
   $$

2. **a) Hitung Zero-Input Response $y_{\text{ZIR}}(t)$:**
   Lengkapi kuadrat penyebut: $s^2 + 4s + 13 = (s + 2)^2 + 3^2$.
   $$
   Y_{\text{ZIR}}(s) = \frac{2s + 4}{(s + 2)^2 + 3^2} = \frac{2(s + 2)}{(s + 2)^2 + 3^2}
   $$
   Invers Laplace menggunakan rumus $e^{-at} \cos(\omega t) u(t)$:
   $$
   y_{\text{ZIR}}(t) = 2 e^{-2t} \cos(3t) u(t)
   $$

3. **b) Hitung Zero-State Response $y_{\text{ZSR}}(t)$:**
   Substitusi $X(s) = \frac{1}{s}$:
   $$
   Y_{\text{ZSR}}(s) = \frac{13}{s (s^2 + 4s + 13)} = \frac{A}{s} + \frac{B s + C}{(s + 2)^2 + 3^2}
   $$
   - Hitung $A$: $A = \left. \frac{13}{s^2 + 4s + 13} \right|_{s=0} = \frac{13}{13} = 1$.
   - Kalikan kedua sisi dengan $s(s^2 + 4s + 13)$:
     $$
     13 = 1(s^2 + 4s + 13) + s(Bs + C) = (1 + B)s^2 + (4 + C)s + 13
     $$
     Samakan koefisien:
     - $s^2$: $1 + B = 0 \implies B = -1$
     - $s$: $4 + C = 0 \implies C = -4$

   Maka:
   $$
   Y_{\text{ZSR}}(s) = \frac{1}{s} - \frac{s + 4}{(s + 2)^2 + 3^2} = \frac{1}{s} - \frac{(s + 2) + \frac{2}{3}(3)}{(s + 2)^2 + 3^2}
   $$
   Invers Laplace:
   $$
   y_{\text{ZSR}}(t) = \left[ 1 - e^{-2t} \cos(3t) - \frac{2}{3} e^{-2t} \sin(3t) \right] u(t)
   $$

4. **c) Respon Total $y(t)$:**
   $$
   y(t) = y_{\text{ZIR}}(t) + y_{\text{ZSR}}(t)
   $$
   $$
   y(t) = \left[ 1 + e^{-2t} \cos(3t) - \frac{2}{3} e^{-2t} \sin(3t) \right] u(t)
   $$
</details>

---

### Problem 4: Teorema Nilai Awal (IVT) & Teorema Nilai Akhir (FVT)
Diberikan Transformasi Laplace suatu sinyal:
$$
X(s) = \frac{5s + 10}{s^3 + 4s^2 + 5s}
$$
Tanpa melakukan Invers Transformasi Laplace, tentukan:
a) Nilai awal sinyal $x(0^+)$  
b) Nilai akhir sinyal $\lim_{t \to \infty} x(t)$

<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**

1. **a) Teorema Nilai Awal (Initial Value Theorem / IVT):**
   $$
   x(0^+) = \lim_{s \to \infty} s X(s)
   $$
   $$
   s X(s) = \frac{s(5s + 10)}{s^3 + 4s^2 + 5s} = \frac{5s^2 + 10s}{s^3 + 4s^2 + 5s}
   $$
   Hitung limit ketika $s \to \infty$:
   $$
   \lim_{s \to \infty} \frac{5s^2 + 10s}{s^3 + 4s^2 + 5s} = 0
   $$
   Jadi, $x(0^+) = 0$.

2. **b) Teorema Nilai Akhir (Final Value Theorem / FVT):**
   Syarat FVT: Seluruh pole dari $s X(s)$ harus terletak strictly di Setengah Bidang Kiri (LHP, $\text{Re}(s) < 0$).
   Faktor penyebut $s X(s)$:
   $$
   s X(s) = \frac{5s + 10}{s^2 + 4s + 5}
   $$
   Akar-akar $s^2 + 4s + 5 = 0$ adalah $s_{1,2} = -2 \pm j 1$. Karena Re$(s_{1,2}) = -2 < 0$, syarat FVT terpenuhi!

   $$
   \lim_{t \to \infty} x(t) = \lim_{s \to 0} s X(s) = \lim_{s \to 0} \frac{5s + 10}{s^2 + 4s + 5} = \frac{10}{5} = 2
   $$
   Jadi, $\lim_{t \to \infty} x(t) = 2$.
</details>

---

## 🔗 Navigasi Pembelajaran
- [[Week 05 Laplace Transformation Notes|Master Lecture Note Week 05]]
- [[Week 05 Laplace Transformation Cheatsheet|Formula Cheatsheet Week 05]]
- [[Digital Signal Processing Overview]]
