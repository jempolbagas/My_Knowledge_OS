---
title: "Week 01: Cheatsheet — Pengenalan DSP & Konversi Sinyal"
course: "Pengolahan Sinyal Digital"
course_abbr: "SIGPRO"
semester: 5
week: 1
date: "2026-08-19"
tags: ["college", "cheatsheet", "sigpro", "dsp", "introduction", "semester-5"]
type: Cheatsheet
---

# ⚡ Week 01: Cheatsheet — Pengenalan Pemrosesan Sinyal Digital

> [!info] **Master Note:** [[Week_01_Introduction_to_DSP_Notes]] | **Drills:** [[Week_01_Introduction_to_DSP_Drills]]

---

## 📌 1. Tabel Formula Konversi Frekuensi

| Parameter Frekuensi | Simbol | Satuan | Formula Hubungan | Rentang Unik |
| :--- | :--- | :--- | :--- | :--- |
| **Frekuensi Analog (Hz)** | $f$ | Hertz ($\text{s}^{-1}$) | $f = \frac{\Omega}{2\pi} = F \cdot f_s$ | $-\infty < f < \infty$ |
| **Frekuensi Sudut Analog** | $\Omega$ | rad/detik | $\Omega = 2\pi f = \frac{\omega}{T_s}$ | $-\infty < \Omega < \infty$ |
| **Frekuensi Normalisasi** | $F$ | siklus/sampel | $F = \frac{f}{f_s} = \frac{\omega}{2\pi}$ | $-\frac{1}{2} \le F < \frac{1}{2}$ |
| **Frekuensi Sudut Digital** | $\omega$ | rad/sampel | $\omega = \Omega T_s = 2\pi \frac{f}{f_s}$ | $-\pi \le \omega < \pi$ |

---

## ⚡ 2. Formulas Kunci ADC & Sampling

### 1. Teorema Sampling Nyquist-Shannon
- **Kriteria Bebas Aliasing:**
  $$
  f_s \ge 2 f_{\max}
  $$
- **Nyquist Rate:** $f_{\text{Nyquist}} = 2 f_{\max}$
- **Nyquist Frequency (Folding Frequency):** $f_n = \frac{f_s}{2}$

### 2. Formulas Kuantisasi ($B$-Bit ADC)
- **Jumlah Level Kuantisasi ($L$):** $L = 2^B$
- **Step Size Kuantisasi ($\Delta$):** $\Delta = \frac{V_{pp}}{2^B}$
- **Daya Noise Kuantisasi ($\sigma_e^2$):** $\sigma_e^2 = \frac{\Delta^2}{12}$
- **SQNR Teoritis:**
  $$
  \text{SQNR (dB)} \approx 6.02 B + 1.76 \text{ dB}
  $$

### 3. Syarat Periodisitas Sinusoid Diskrit
- Sinusoid $x[n] = e^{j\omega n}$ periodik jika dan hanya jika:
  $$
  \frac{\omega}{2\pi} = \frac{k}{N} \in \mathbb{Q} \quad (k, N \in \mathbb{Z}^+)
  $$
- Periode fundamental $N = \frac{k \cdot 2\pi}{\omega}$ (sampel).

---

## 🛡️ 3. Ringkasan Pipeline Blok DSP Hardware

```
[x(t)] -> (Anti-Aliasing Filter) -> (Sampler Ts) -> (Quantizer B-bit) -> (DSP Core) -> (DAC ZOH) -> (Reconstruction Filter) -> [y(t)]
```

- **Anti-Aliasing Filter:** Analog LPF dengan $f_c = \frac{f_s}{2}$ sebelum ADC.
- **Reconstruction Filter:** Analog LPF dengan $f_c = \frac{f_s}{2}$ setelah DAC.

---

## 🐍 4. Quick Python Snippet (Sampling & Plotting Sinyal Diskrit)

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameter Sampling
f_s = 8000          # 8 kHz Sampling Rate
T_s = 1.0 / f_s     # Sampling Period
t_end = 0.005       # 5 ms rekaman

# Sinyal Analog Kontinu (Simulasi Dense)
t_cont = np.linspace(0, t_end, 1000)
x_cont = 3 * np.cos(2 * np.pi * 1000 * t_cont)

# Sampling Diskrit
n = np.arange(0, int(t_end * f_s))
x_disc = 3 * np.cos(2 * np.pi * 1000 * n * T_s)

# Plotting Stem
plt.figure(figsize=(8, 4))
plt.plot(t_cont * 1000, x_cont, 'r--', label='Sinyal Kontinu x(t)')
plt.stem(n * T_s * 1000, x_disc, linefmt='b-', markerfmt='bo', basefmt='r-', label='Sampel Diskrit x[n]')
plt.xlabel('Waktu (ms)')
plt.ylabel('Amplitudo')
plt.title('Sampling Sinyal Sinusoidal 1 kHz pada f_s = 8 kHz')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('/mnt/data/life-hub/10_Knowledge_OS/30_Assets/plot_dsp_week01_sampling.png')
print("Plot sampling berhasil disimpan ke 30_Assets.")
```

---

## 🔗 Navigasi Pembelajaran
- [[Week_01_Introduction_to_DSP_Notes|Master Overview]]
- [[Week_01_Introduction_to_DSP_Drills|Practice Drills]]
- [[Digital Signal Processing Overview]]
