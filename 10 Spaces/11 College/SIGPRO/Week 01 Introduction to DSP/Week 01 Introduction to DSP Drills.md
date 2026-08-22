---
title: "Week 01: Active Recall & Practice Drills — Pengenalan DSP"
course: "Pengolahan Sinyal Digital"
course_abbr: "SIGPRO"
semester: 5
week: 1
date: "2026-08-19"
tags: ["college", "drills", "active-recall", "sigpro", "dsp", "introduction", "semester-5"]
type: PracticeDrills
---

# 🧠 Week 01: Practice & Active Recall Drills — Pengenalan DSP

> [!info] **Master Note:** [[Week 01 Introduction to DSP Notes]] | **Cheatsheet:** [[Week 01 Introduction to DSP Cheatsheet]]
> Latihan soal konseptual dan kalkulasi numerik berstandar ujian universitas untuk menguji pemahaman dasar pengolahan sinyal digital.

---

## 📋 Problem Set

---

### Problem 1: Konversi Frekuensi Analog ke Digital & Nyquist Sampling
Sebuah sinyal analog kontinu didefinisikan sebagai:
$$
x(t) = 3 \cos(2000 \pi t) + 5 \sin(6000 \pi t)
$$
Sinyal ini disampling dengan frekuensi sampling $f_s = 8000 \text{ Hz}$ (atau sampel/detik).

a) Tentukan frekuensi tertinggi $f_{\max}$ dari sinyal analog $x(t)$ dan hitung Nyquist Rate-nya!  
b) Tentukan persamaan sinyal waktu-diskrit $x[n]$ dalam bentuk frekuensi sudut digital $\omega$ (rad/sample)!  
c) Apakah terjadi *aliasing* pada proses sampling ini? Jelaskan!

<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**

1. **a) Menentukan $f_{\max}$ dan Nyquist Rate:**
   - Komponen 1: $2\pi f_1 = 2000\pi \implies f_1 = 1000 \text{ Hz}$.
   - Komponen 2: $2\pi f_2 = 6000\pi \implies f_2 = 3000 \text{ Hz}$.
   - Frekuensi tertinggi $f_{\max} = 3000 \text{ Hz}$.
   - **Nyquist Rate:** $f_{\text{Nyquist}} = 2 \cdot f_{\max} = 2 \cdot 3000 = 6000 \text{ Hz}$.

2. **b) Persamaan Sinyal Diskrit $x[n]$:**
   Substitusi $t = \frac{n}{f_s} = \frac{n}{8000}$:
   $$
   x[n] = 3 \cos\left(2000 \pi \frac{n}{8000}\right) + 5 \sin\left(6000 \pi \frac{n}{8000}\right)
   $$
   $$
   x[n] = 3 \cos\left(\frac{\pi}{4} n\right) + 5 \sin\left(\frac{3\pi}{4} n\right)
   $$
   Di mana frekuensi digitalnya adalah $\omega_1 = \frac{\pi}{4} \text{ rad/sample}$ dan $\omega_2 = \frac{3\pi}{4} \text{ rad/sample}$.

3. **c) Analisis Aliasing:**
   Karena frekuensi sampling $f_s = 8000 \text{ Hz} > f_{\text{Nyquist}} = 6000 \text{ Hz}$ (dan frekuensi maksimum $f_{\max} = 3000 \text{ Hz} < \frac{f_s}{2} = 4000 \text{ Hz}$), maka kriteria Nyquist **terpenuhi**. Oleh karena itu, **tidak terjadi aliasing**.
</details>

---

### Problem 2: Pengujian Periodisitas Sinusoid Diskrit
Tentukan apakah sinyal diskrit berikut bersifat periodik atau aperiodik. Jika periodik, hitung periode fundamentalnya $N$ (dalam sampel):
a) $x_1[n] = \cos(0.12 \pi n)$  
b) $x_2[n] = \sin(0.5 n)$

<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**

1. **a) Untuk $x_1[n] = \cos(0.12 \pi n)$:**
   Frekuensi digital $\omega_1 = 0.12 \pi = \frac{12}{100} \pi = \frac{3}{25} \pi$.
   Evaluasi rasio $\frac{\omega_1}{2\pi}$:
   $$
   \frac{\omega_1}{2\pi} = \frac{\frac{3}{25}\pi}{2\pi} = \frac{3}{50}
   $$
   Karena hasilnya berupa bilangan rasional ($\frac{3}{50}$ di mana $k=3, N=50$), sinyal $x_1[n]$ bersifat **PERIODIK** dengan periode fundamental $N = 50 \text{ sampel}$.

2. **b) Untuk $x_2[n] = \sin(0.5 n)$:**
   Frekuensi digital $\omega_2 = 0.5 \text{ rad/sample}$.
   Evaluasi rasio $\frac{\omega_2}{2\pi}$:
   $$
   \frac{\omega_2}{2\pi} = \frac{0.5}{2\pi} = \frac{1}{4\pi}
   $$
   Karena $\pi$ adalah bilangan irasional, maka rasio $\frac{1}{4\pi}$ adalah bilangan irasional.
   Oleh karena itu, sinyal $x_2[n]$ bersifat **APERIODIK** (tidak pernah berulang secara sempurna pada indeks bilangan bulat $n$).
</details>

---

### Problem 3: Kalkulasi Bit ADC & Signal-to-Quantization Noise Ratio (SQNR)
Sebuah sistem perekaman audio menggunakan ADC 16-bit dengan rentang tegangan pik-ke-pik $V_{pp} = 10 \text{ V}$.
a) Hitung jumlah level kuantisasi $L$ dan ukuran langkah kuantisasi $\Delta$!  
b) Hitung nilai SQNR teoritis dalam desibel (dB)!  
c) Jika sistem ditingkatkan menjadi ADC 24-bit, berapa kenaikan SQNR yang diperoleh?

<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**

1. **a) Jumlah Level $L$ & Step Size $\Delta$:**
   $$
   L = 2^{16} = 65,536 \text{ level}
   $$
   $$
   \Delta = \frac{V_{pp}}{L} = \frac{10}{65536} \approx 1.5259 \times 10^{-4} \text{ V} \approx 0.1526 \text{ mV}
   $$

2. **b) Nilai SQNR Teoritis (16-bit):**
   Gunakan rumus pendekatan SQNR:
   $$
   \text{SQNR} \approx 6.02 B + 1.76 \text{ dB}
   $$
   Substitusi $B = 16$:
   $$
   \text{SQNR} \approx 6.02(16) + 1.76 = 96.32 + 1.76 = 98.08 \text{ dB}
   $$

3. **c) Kenaikan SQNR untuk ADC 24-bit:**
   Perbedaan jumlah bit $\Delta B = 24 - 16 = 8 \text{ bit}$.
   Kenaikan SQNR:
   $$
   \Delta \text{SQNR} \approx 6.02 \times \Delta B = 6.02 \times 8 = 48.16 \text{ dB}
   $$
   SQNR total untuk 24-bit adalah $98.08 + 48.16 = 146.24 \text{ dB}$.
</details>

---

### Problem 4: Aliasing Sinyal & Frekuensi Terlipat
Sebuah sinyal sinus analog $x(t) = \cos(2\pi \cdot 7000 t)$ disampling dengan frekuensi sampling $f_s = 10,000 \text{ Hz}$ tanpa menggunakan Anti-Aliasing Filter.
Tentukan frekuensi tampak (*apparent frequency*) dari sinyal terdiskon tersebut pada domain waktu-diskrit!

<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**

1. Frekuensi sinyal asli $f = 7000 \text{ Hz}$. Batas Nyquist $f_n = \frac{f_s}{2} = 5000 \text{ Hz}$.
2. Karena $f = 7000 \text{ Hz} > 5000 \text{ Hz}$, terjadi **aliasing**.
3. Sinyal hasil sampling:
   $$
   x[n] = \cos\left(2\pi \frac{7000}{10000} n\right) = \cos(1.4 \pi n)
   $$
4. Gunakan sifat identitas kosinus $\cos(\theta) = \cos(2\pi - \theta)$:
   $$
   x[n] = \cos(2\pi n - 1.4\pi n) = \cos(0.6 \pi n)
   $$
5. Frekuensi digital tampak $\omega_a = 0.6 \pi \text{ rad/sample}$.
6. Frekuensi analog tampak $f_a$:
   $$
   \omega_a = 2\pi \frac{f_a}{f_s} \implies 0.6\pi = 2\pi \frac{f_a}{10000} \implies f_a = 3000 \text{ Hz}
   $$
   **Kesimpulan:** Sinyal $7000 \text{ Hz}$ akan "menyamar" menjadi sinyal $3000 \text{ Hz}$ akibat aliasing.
</details>

---

## 🔗 Navigasi Pembelajaran
- [[Week 01 Introduction to DSP Notes|Master Overview]]
- [[Week 01 Introduction to DSP Cheatsheet|Formula Cheatsheet]]
- [[Digital Signal Processing Overview]]
