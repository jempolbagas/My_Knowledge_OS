---
title: "Week 05: Cheatsheet & Formula Reference — Transformasi Laplace"
course: "Pengolahan Sinyal Digital"
course_abbr: "SIGPRO"
semester: 5
week: 5
date: "2026-08-19"
tags: ["college", "cheatsheet", "sigpro", "dsp", "laplace-transform", "semester-5"]
type: Cheatsheet
---

# ⚡ Week 05: Cheatsheet — Transformasi Laplace & Analisis Domain Kompleks s

> [!info] **Master Note:** [[Week_05_Laplace_Transformation_Notes]] | **Drills:** [[Week_05_Laplace_Transformation_Drills]]
> Kartu referensi cepat untuk persiapan ujian UTS/UAS mata kuliah [[Digital Signal Processing Overview|Pengolahan Sinyal Digital (SIGPRO)]].

---

## 📌 1. Tabel Pasangan Transformasi Laplace Kunci

| Sinyal Waktu $f(t)$ | Transformasi Laplace $F(s)$ | ROC (Region of Convergence) |
| :--- | :--- | :--- |
| $\delta(t)$ | $1$ | Seluruh bidang-$s$ |
| $u(t)$ | $\frac{1}{s}$ | $\text{Re}(s) > 0$ |
| $t u(t)$ | $\frac{1}{s^2}$ | $\text{Re}(s) > 0$ |
| $t^n u(t)$ | $\frac{n!}{s^{n+1}}$ | $\text{Re}(s) > 0$ |
| $e^{-at} u(t)$ | $\frac{1}{s + a}$ | $\text{Re}(s) > -a$ |
| $-e^{-at} u(-t)$ | $\frac{1}{s + a}$ | $\text{Re}(s) < -a$ |
| $t e^{-at} u(t)$ | $\frac{1}{(s + a)^2}$ | $\text{Re}(s) > -a$ |
| $\sin(\omega_0 t) u(t)$ | $\frac{\omega_0}{s^2 + \omega_0^2}$ | $\text{Re}(s) > 0$ |
| $\cos(\omega_0 t) u(t)$ | $\frac{s}{s^2 + \omega_0^2}$ | $\text{Re}(s) > 0$ |
| $e^{-at} \sin(\omega_0 t) u(t)$ | $\frac{\omega_0}{(s + a)^2 + \omega_0^2}$ | $\text{Re}(s) > -a$ |
| $e^{-at} \cos(\omega_0 t) u(t)$ | $\frac{s + a}{(s + a)^2 + \omega_0^2}$ | $\text{Re}(s) > -a$ |

---

## ⚡ 2. Ringkasan Sifat-Sifat Utama

| Operasi / Sifat | Domain Waktu $f(t)$ | Domain-$s$ $F(s)$ | Keterangan / ROC |
| :--- | :--- | :--- | :--- |
| **Linearitas** | $a f_1(t) + b f_2(t)$ | $a F_1(s) + b F_2(s)$ | ROC $\supseteq R_1 \cap R_2$ |
| **Pergeseran Waktu** | $f(t - t_0) u(t - t_0)$ | $e^{-s t_0} F(s)$ | ROC $= R$ |
| **Pergeseran Frekuensi** | $e^{s_0 t} f(t)$ | $F(s - s_0)$ | ROC digeser $\text{Re}(s_0)$ |
| **Turunan ke-1 (Unilateral)** | $f'(t)$ | $s F(s) - f(0^-)$ | Wajib sertakan kondisi awal |
| **Turunan ke-2 (Unilateral)** | $f''(t)$ | $s^2 F(s) - s f(0^-) - f'(0^-)$ | Pemodelan Orde-2 |
| **Integrasi Waktu** | $\int_{0^-}^{t} f(\tau) d\tau$ | $\frac{1}{s} F(s)$ | ROC $\cap \{\text{Re}(s) > 0\}$ |
| **Perkalian $t$** | $t f(t)$ | $-\frac{d}{ds} F(s)$ | Diferensiasi domain-$s$ |
| **Konvolusi Waktu** | $f_1(t) * f_2(t)$ | $F_1(s) \cdot F_2(s)$ | Sifat utama Sistem LTI |

---

## 🎯 3. Teorema Batas (Initial & Final Value Theorems)

- **Initial Value Theorem (IVT):**
  $$
  f(0^+) = \lim_{s \to \infty} s F(s)
  $$
- **Final Value Theorem (FVT):**
  $$
  \lim_{t \to \infty} f(t) = \lim_{s \to 0} s F(s)
  $$
  *Syarat FVT:* Seluruh pole dari $s F(s)$ harus berada di **Left-Half Plane (LHP)**, yaitu $\text{Re}(p_i) < 0$.

---

## 🛡️ 4. Matriks Kausalitas & Stabilitas Sistem LTI

| Sifat Sistem | Kriteria pada Bidang-$s$ |
| :--- | :--- |
| **Kausal (Causal)** | ROC berupa setengah bidang kanan: $\text{Re}(s) > \max(\text{Re}(p_i))$ |
| **Anti-Kausal** | ROC berupa setengah bidang kiri: $\text{Re}(s) < \min(\text{Re}(p_i))$ |
| **Stabil BIBO** | ROC mencakup sumbu imajiner $j\omega$ ($\text{Re}(s) = 0$) |
| **Kausal & Stabil** | Seluruh pole berada di Left-Half Plane ($\text{Re}(p_i) < 0$) |

---

## 🐍 5. Quick Python Snippet (SciPy / SymPy)

```python
import sympy as sp

# Definisi Variabel
t, s = sp.symbols('t s', real=True, positive=True)

# 1. Transformasi Laplace dari f(t) = t * exp(-2*t)
f = t * sp.exp(-2*t)
F = sp.laplace_transform(f, t, s, noconds=True)
print("F(s) =", F)  # Hasil: 1/(s + 2)**2

# 2. Invers Transformasi Laplace dari F(s) = (s + 1)/(s**2 + 5*s + 6)
F_s = (s + 1) / (s**2 + 5*s + 6)
f_t = sp.inverse_laplace_transform(F_s, s, t)
print("f(t) =", f_t) # Hasil: (2*exp(-3*t) - exp(-2*t))*Heaviside(t)
```

---

## 🔗 Navigasi Pembelajaran
- [[Week_05_Laplace_Transformation_Notes|Master Lecture Note]]
- [[Week_05_Laplace_Transformation_Drills|Practice Drills]]
- [[Digital Signal Processing Overview]]
