---
title: "Week 01: Sub-Note 2 — Elemen Dasar Sistem DSP"
course: "Pengolahan Sinyal Digital"
course_abbr: "SIGPRO"
semester: 5
week: 1
date: "2026-08-19"
tags: ["college", "sub-note", "sigpro", "dsp", "adc", "dac", "hardware"]
type: LectureNote
---

# 📖 Sub-Note 2: Arsitektur & Elemen Dasar Sistem Pemrosesan Sinyal Digital

> [!info] **Master Overview:** [[Week 01 Introduction to DSP Notes]] | **Sub-Note 1:** [[01 Konsep Sinyal dan Frekuensi]]

---

## 📌 1. Pipeline Rantai Blok Sistem DSP

Untuk memproses sinyal fisik analog menggunakan prosesor digital, diperlukan pemetaan dua arah antara domain kontinu dan diskrit.

```mermaid
flowchart TD
    subgraph Analog Domain Input
        A["Input Fisik (Suara, Suhu, Tekanan)"] --> B["Sensor / Transduser"]
        B --> C["Sinyal Analog x(t)"]
        C --> D["Anti-Aliasing Filter (Analog LPF)"]
    end
    
    subgraph Mixed-Signal Conversion (A/D)
        D --> E["Sampler (t = n T_s)"]
        E --> F["Quantizer (Kuantisasi Level B-bit)"]
        F --> G["Encoder (Biner 0/1)"]
    end

    subgraph Digital Domain Processing
        G --> H["DSP Core / Software x[n] (Filter, FFT, Control)"]
    end

    subgraph Mixed-Signal Conversion (D/A)
        H --> I["DAC (Digital-to-Analog Converter / ZOH)"]
    end

    subgraph Analog Domain Output
        I --> J["Reconstruction Filter (Analog LPF)"]
        J --> K["Sinyal Analog Output y(t)"]
    end
```

---

## 🔍 2. Deep-Dive Komponen Utama

### 2.1 Anti-Aliasing Filter (Analog LPF)
- **Fungsi:** Membatasi bandwidth sinyal analog masukan agar frekuensi maksimumnya tidak melebihi setengah frekuensi sampling ($f_{\max} < \frac{f_s}{2}$).
- **Mengapa Wajib?** Tanpa filter ini, komponen frekuensi tinggi di atas $f_s / 2$ akan terlipat ke dalam band frekuensi rendah (*aliasing*), menyebabkan distorsi permanen yang tidak dapat diperbaiki secara digital.

---

### 2.2 Konversi Analog-ke-Digital (ADC)
Proses ADC terdiri dari tiga tahap urut:

#### 1. Sampling (Pencuplikan)
Mengubah variabel waktu kontinu $t$ menjadi indeks waktu diskrit $n$:
$$
x_s[n] = x(n T_s)
$$
- **Teorema Sampling Nyquist-Shannon:** Agar sinyal analog $x(t)$ dengan frekuensi tertinggi $f_{\max}$ dapat direkonstruksi sempurna dari sampelnya, frekuensi sampling $f_s$ harus memenuhi:
  $$
  f_s \ge 2 f_{\max}
  $$
- Nilai $f_N = 2 f_{\max}$ disebut **Nyquist Rate**, dan $f_n = \frac{f_s}{2}$ disebut **Nyquist Frequency**.

#### 2. Quantization (Kuantisasi)
Mengubah nilai amplitudo kontinu $x[n]$ menjadi salah satu dari $L = 2^B$ level diskrit terdekat, di mana $B$ adalah jumlah bit ADC.
- **Ukuran Langkah Kuantisasi (Step Size $\Delta$):**
  $$
  \Delta = \frac{V_{\max} - V_{\min}}{L} = \frac{V_{pp}}{2^B}
  $$
- **Quantization Error $e[n]$:**
  $$
  e[n] = x_q[n] - x[n], \quad -\frac{\Delta}{2} \le e[n] \le \frac{\Delta}{2}
  $$
- **Daya Noise Kuantisasi ($\sigma_e^2$):** Diasumsikan terdistribusi seragam:
  $$
  \sigma_e^2 = \frac{\Delta^2}{12}
  $$
- **Signal-to-Quantization-Noise Ratio (SQNR):**
  $$
  \text{SQNR (dB)} \approx 6.02 B + 1.76 \text{ dB}
  $$
  *Rule of Thumb:* Setiap penambahan 1 bit ADC meningkatkan kualitas SQNR sebesar $\approx 6 \text{ dB}$.

#### 3. Encoding (Pengkodean)
Memetakan setiap nilai kuantisasi terkuantisasi ke dalam kata biner $B$-bit (misal: Two's Complement, Offset Binary).

---

### 2.3 DSP Core / Processing Hardware
Blok ini mengeksekusi algoritma matematis pada deret data biner $x[n]$ untuk menghasilkan deret keluaran $y[n]$.
- **Operasi Dasar:** Perkalian (*Multiplication*), Penjumlahan (*Addition*), dan Penundaan Sampel (*Delay $z^{-1}$*).
- **Arsitektur Hardware Utama:**
  - **DSP Processors (misal: TI TMS320, ADI Blackfin):** Dilengkapi unit *Multiply-Accumulate* (MAC) hardware yang mampu mengeksekusi $y[n] = y[n] + a \cdot x[n]$ dalam 1 clock cycle.
  - **FPGA (Field Programmable Gate Array):** Pemrosesan paralel tinggi untuk DSP berkecepatan tinggi (seperti radar dan Baseband 5G).
  - **General-Purpose CPU / Microcontroller (ARM Cortex-M4/M7 dengan SIMD/FPU):** Pemrosesan DSP tertanam hemat energi.

---

### 2.4 Konversi Digital-ke-Analog (DAC) & Reconstruction Filter
- **DAC (Zero-Order Hold / ZOH):** Memetakan kata biner $y[n]$ kembali menjadi tegangan analog tangga (staircase waveform) $y_{\text{zoh}}(t)$.
- **Reconstruction Filter (Analog LPF):** Filter analog low-pass dengan frekuensi cut-off $f_c = \frac{f_s}{2}$ yang berfungsi menghilangkan tangga spektrum frekuensi tinggi (artefak sinyal cermin / *image spectrum*) sehingga menghasilkan sinyal analog output yang mulus $y(t)$.

---

## ⚖️ 3. Perbandingan: DSP vs Pemrosesan Sinyal Analog

| Parameter Perbandingan | Pemrosesan Sinyal Analog (ASP) | Pemrosesan Sinyal Digital (DSP) |
| :--- | :--- | :--- |
| **Elemen Dasar** | Resistor, Kapasitor, Induktor, Op-Amp | Algoritma Software, Adder, Multiplier, Memori |
| **Fleksibilitas** | Kaku (harus ubah komponen fisik/solder) | Sangat Tinggi (cukup re-program software) |
| **Presisi & Toleransi** | Terpengaruh suhu, efek penuaan, & toleransi pasif (±5%) | Presisi mutlak (ditentukan oleh bit-depth $B$) |
| **Penyimpanan Data** | Sangat sulit (pita magnetik/rekaman fisik) | Sangat mudah (RAM, Flash, SSD, kompresi digital) |
| **Kecepatan & Bandwidth** | Tanpa batas sampling (cocok untuk frekuensi ekstrem GHz) | Dibatasi oleh frekuensi sampling $f_s$ dan ADC/DSP clock |
| **Kompleksitas Algoritma** | Terbatas pada fungsi linear sederhana | Mampu menjalankan FFT, Filter Adaptif, ML/AI |

---

## 🔗 Navigasi Modul
- [[Week 01 Introduction to DSP Notes|Master Overview Week 01]]
- [[01 Konsep Sinyal dan Frekuensi|Sub-Note 1: Konsep Sinyal & Frekuensi]]
- [[03 Bidang Aplikasi DSP|Sub-Note 3: Bidang Aplikasi DSP]]
