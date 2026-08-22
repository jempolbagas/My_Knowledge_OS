---
title: "Aritmatika Modulo"
course: "Self-Study Mathematics"
course_abbr: "MATH"
semester: 
week: 
date: "2026-08-20"
tags: ["lecture-note", "discrete-math"]
type: SelfStudyNote
---

# 🎓 Aritmatika Modulo — Pondasi Kriptografi dan Sinyal Diskrit

> [!info] **Course Overview:** [[Self_Study_Math_Overview]] | **Syllabus:** [[Discrete_Math_Syllabus]]
> **Topics Covered:** Definisi Modulo, Kongruensi, Invers Modular, Teorema Sisa Tiongkok (Chinese Remainder Theorem)

---

## 📌 1. Overview & Core Context
- **Latar Belakang & Motivasi:** Mengapa topik ini penting dalam konteks Matematika Diskrit. Aritmatika modulo membatasi domain himpunan bilangan bulat menjadi sebuah siklus periodik. Konsep ini digunakan di mana-mana mulai dari algoritma Fast Fourier Transform (FFT) pada Pengolahan Sinyal Digital, Image Wrapping pada Pengolahan Citra Digital, hingga enkripsi asimetris seperti RSA dalam Kriptografi.
- **High-Level Takeaway:** 3 poin utama yang wajib dikuasai:
  1. Cara bekerja dan menghitung sisa hasil bagi menggunakan operator modulo.
  2. Konsep kesetaraan dalam modulo (Kongruensi) dan cara menyelesaikan persamaan modular.
  3. Konsep Invers Modular dan Teorema Sisa Tiongkok sebagai basis algoritma komputer tingkat lanjut.

---

## 📖 2. Detailed Lecture Notes & Technical Deep-Dive

### 2.1 Definisi Aritmatika Modulo
Aritmatika modulo adalah sistem aritmatika untuk bilangan bulat, di mana bilangan tersebut "membungkus" atau kembali ke nol setelah mencapai nilai tertentu yang disebut **modulus**.
Misalkan $a$ dan $n$ adalah bilangan bulat dengan $n > 0$. Operasi $a \pmod n$ menghasilkan sisa pembagian dari $a$ dibagi dengan $n$.
$$ a = q \cdot n + r $$
di mana $q$ adalah hasil bagi (kuosien) dan $r$ adalah sisa (*remainder*), dengan syarat $0 \leq r < n$.
Oleh karena itu:
$$ a \pmod n = r $$

**Contoh:**
- $17 \pmod 5 = 2$ (karena $17 = 3 \cdot 5 + 2$)
- $-2 \pmod 5 = 3$ (karena $-2 = -1 \cdot 5 + 3$)

### 2.2 Kongruensi Modular
Dua bilangan $a$ dan $b$ dikatakan **kongruen modulo $n$** jika keduanya memberikan sisa yang sama saat dibagi dengan $n$. Ini ditulis sebagai:
$$ a \equiv b \pmod n $$
Hal ini ekuivalen dengan mengatakan bahwa $n$ habis membagi selisih $a - b$, yaitu $n \mid (a - b)$.

**Sifat-sifat Kongruensi:**
Jika $a \equiv b \pmod n$ dan $c \equiv d \pmod n$, maka:
1. **Penjumlahan:** $a + c \equiv b + d \pmod n$
2. **Pengurangan:** $a - c \equiv b - d \pmod n$
3. **Perkalian:** $a \cdot c \equiv b \cdot d \pmod n$
4. **Pemangkatan:** $a^k \equiv b^k \pmod n$ untuk bilangan bulat non-negatif $k$.

*Perhatian:* Pembagian dalam modulo tidak sesederhana aritmatika biasa; pembagian hanya dapat dilakukan jika pembagi memiliki **invers modular**.

### 2.3 Invers Modular dan Algoritma Euclidean Ekstensi
Dalam aritmatika biasa, pembagian dengan $a$ sama dengan perkalian dengan $a^{-1}$. Dalam modulo $n$, invers dari $a$ (ditulis $a^{-1} \pmod n$) adalah sebuah bilangan $x$ sedemikian hingga:
$$ a \cdot x \equiv 1 \pmod n $$

Invers modular hanya ada (atau $a$ memiliki invers modulo $n$) **jika dan hanya jika** $a$ dan $n$ saling prima (*coprime*), yaitu $FPB(a, n) = 1$.
Untuk mencari nilai invers tersebut secara efisien, kita menggunakan **Extended Euclidean Algorithm** yang mencari koefisien Bezout $x$ dan $y$ sehingga:
$$ a \cdot x + n \cdot y = FPB(a, n) = 1 $$

### 2.4 Chinese Remainder Theorem (Teorema Sisa Tiongkok)
CRT memberikan solusi unik terhadap sekumpulan persamaan kongruensi linier dengan modulus yang saling prima berpasangan.
Misalkan terdapat sistem persamaan:
$$ x \equiv a_1 \pmod{m_1} $$
$$ x \equiv a_2 \pmod{m_2} $$
$$ \vdots $$
$$ x \equiv a_k \pmod{m_k} $$
Jika semua $m_i$ saling prima, maka sistem ini memiliki solusi unik modulo $M = m_1 \cdot m_2 \cdots m_k$.

---

## ⚡ 3. Formulas, Key Theorems, & Algorithms

| Nama Konsep / Algoritma | Teorema / Formula Kunci | Kompleksitas / Catatan Kunci |
| :--- | :--- | :--- |
| **Definisi Modulo** | $a = q \cdot n + r \implies a \pmod n = r$ | $O(1)$ untuk instruksi CPU tunggal. |
| **Kongruensi** | $a \equiv b \pmod n \iff n \mid (a - b)$ | Relasi ekuivalensi dasar. |
| **Invers Modular** | $a \cdot x \equiv 1 \pmod n$ (ada jika $FPB(a,n)=1$) | $O(\log(\min(a, n)))$ menggunakan Extended Euclidean. |
| **Chinese Remainder Theorem** | Solusi unik modulo $M = \prod m_i$ untuk sistem kongruensi. | $O(k \log M)$ untuk $k$ persamaan. |

---

## 🧠 4. Active Recall & Practice Drills

(Silakan lihat berkas `Aritmatika_Modulo_Drills.md` untuk pengerjaan soal dan latihan komprehensif.)

---

## 🔗 Vault Linkage & Brain Atlas Promotion

> [!tip] **Promotable Concepts for Permanent Vault (`20 Brain Atlas/`)**
> Catatan ini mereferensikan konsep-konsep fundamental yang layak dipromosikan ke `20 Brain Atlas/20 Concepts/`:
> - `[[Kongruensi Modular]]`: Konsep kesetaraan dalam aritmatika melingkar yang menjadi basis pengolahan sinyal dan kriptografi.
> - `[[Invers Modular]]`: Syarat utama operasi "pembagian" di dunia diskrit.
> - `[[Chinese Remainder Theorem]]`: Teorema penting penentu uniksitas solusi modular.
