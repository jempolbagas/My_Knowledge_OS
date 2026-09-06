---
title: "Kinematika Gerak Lurus — Master Guide & Navigasi Modul"
type: master-dashboard
subject: Physics
level: sma
target_audience: "SMA Kelas X"
created: 2026-09-05
sources:
  - "[[Besaran Gerak dan GLB SMA]]"
  - "[[GLBB dan Analisis Grafik SMA]]"
  - "[[Gerak Vertikal dan Kasus Dua Benda SMA]]"
  - "[[Dinamika Gerak SMA]]"
tags:
  - fisika
  - sma_kelas_10
  - kurikulum_merdeka
  - materi_ajar
  - kinematika
  - glb
  - glbb
  - master-dashboard
---

# Kinematika Gerak Lurus — Navigasi Ruang & Waktu Benda Bergerak! 🚗⏱️

Kinematika gerak lurus adalah cabang mekanika klasik yang mempelajari karakteristik gerak suatu partikel pada lintasan lurus—meliputi posisi, perpindahan, kelajuan, kecepatan, dan percepatan—secara murni matematis dan geometris tanpa meninjau gaya penyebab timbulnya gerakan tersebut. Pemahaman kinematika satu dimensi ($1\text{D}$) merupakan landasan mutlak bagi seluruh fisika lanjutan, mulai dari rekayasa sistem kendali jelajah otomatis (*cruise control*), kalkulasi deselerasi rem darurat kereta cepat, navigasi satelit dan roket luar angkasa, hingga dasar pemahaman mekanika gaya pada [[Dinamika Gerak SMA]]. Modul pembelajaran ini disusun khusus untuk peserta didik SMA Kelas X (Fase E) guna membedah tuntas fondasi besaran gerak, Gerak Lurus Beraturan (GLB), Gerak Lurus Berubah Beraturan (GLBB), fenomena percepatan gravitasi bumi pada gerak vertikal, serta analisis matematis-grafis skenario pertemuan dua benda bergerak.

---

## 📊 Overview Bab & Peta Konsep

Secara analitis, gerak lurus suatu benda diklasifikasikan berdasarkan keberadaan dan kestabilan nilai percepatannya ($a$). Jika suatu benda bergerak tanpa percepatan ($a = 0$), benda menempuh jarak yang sebanding dengan selang waktu dalam **Gerak Lurus Beraturan (GLB)**. Sebaliknya, bila suatu benda mengalami percepatan yang bernilai konstan ($a = \text{konstan} \neq 0$), kecepatannya akan berubah secara linier terhadap waktu dalam **Gerak Lurus Berubah Beraturan (GLBB)**.

![[infographic_physics_kinematika_gerak_lurus_master.webp]]

### Fokus Penguasaan Konsep:
1. **Fondasi Spasial & Vektor:** Membedakan secara tegas pasangan besaran fisis skalar versus vektor: Jarak ($s$) vs Perpindahan ($\Delta x$), serta Kelajuan ($v$) vs Kecepatan ($\vec{v}$), termasuk interpretasi pembacaan instrumen nyata seperti spidometer dan odometer.
2. **Karakteristik GLB & Kurva Fisis:** Memahami kondisi kecepatan konstan ($\vec{v} = \text{konstan}$) pada lintasan horizontal tanpa gesekan/hambatan, formulasi linear $s = v \cdot t$, serta dekonstruksi grafik $s-t$ dan $v-t$.
3. **Persamaan Emas GLBB & Analisis Kurva:** Menurunkan dan menerapkan tiga persamaan fundamental GLBB, membedakan kondisi dipercepat ($a > 0$) dan diperlambat/deselerasi ($a < 0$), serta menguasai arti fisis gradien kurva $v-t$ sebagai percepatan dan luas daerah di bawah kurva $v-t$ sebagai perpindahan.
4. **Dinamika Gerak Vertikal:** Menganalisis aplikasi GLBB di bawah pengaruh medan gravitasi bumi ($a = \pm g$) tanpa gesekan udara, yang mencakup Gerak Jatuh Bebas (GJB), Gerak Vertikal ke Bawah (GVB), dan Gerak Vertikal ke Atas (GVA) beserta sifat simetri waktu naik-turun dan kelajuan pendaratannya.
5. **Masalah Terpadu Dua Benda (HOTS):** Memecahkan skenario pertemuan dua benda bergerak, baik yang saling menyongsong/berpapasan ($s_A + s_B = d$) maupun saling mengejar/susul-menyusul ($s_B = s_A + \Delta s$), melalui formulasi aljabar substitusi waktu dan interpretasi perpotongan grafik.

---

## 🧭 Navigasi Modul Pembelajaran

Paket materi pembelajaran Kinematika Gerak Lurus ini terbagi menjadi tiga sub-modul berjenjang yang saling terintegrasi:

### ⏱️ [[Besaran Gerak dan GLB SMA | Modul 1: Fondasi Besaran Kinematika & Gerak Lurus Beraturan]]
> *Fokus Pembahasan:*
> - Kerangka acuan dan posisi partikel pada garis bilangan satu dimensi.
> - Perbedaan fundamental Jarak (besaran skalar, total lintasan) vs Perpindahan (besaran vektor, perubahan kedudukan).
> - Analisis Kelajuan rata-rata & sesaat versus Kecepatan rata-rata & sesaat.
> - Karakteristik hakiki GLB: Kecepatan konstan dan percepatan nol ($a = 0$).
> - Interpretasi kurva grafik $s-t$ (garis lurus miring dengan gradien = kecepatan) dan grafik $v-t$ (garis horizontal datar).
> - Contoh aplikasi nyata: Laju jelajah Kereta Cepat Whoosh dan pesawat komersial pada ketinggian konstan.

### 📈 [[GLBB dan Analisis Grafik SMA | Modul 2: Percepatan Konstan, Persamaan Emas GLBB, & Analisis Kurva]]
> *Fokus Pembahasan:*
> - Definisi percepatan rata-rata dan percepatan sesaat ($a = \frac{\Delta v}{\Delta t}$).
> - Penurunan tiga persamaan emas GLBB secara sistematis:
>   1. $v_t = v_0 + a t$
>   2. $s = v_0 t + \frac{1}{2} a t^2$
>   3. $v_t^2 = v_0^2 + 2 a s$
> - Dekonstruksi kurva $s-t$, $v-t$, dan $a-t$ untuk kondisi dipercepat ($a > 0$) dan diperlambat ($a < 0$).
> - Teorema Grafis Emas: **Gradien kurva $v-t$ = Percepatan ($a$)** dan **Luas area di bawah kurva $v-t$ = Jarak/Perpindahan ($s$)**.
> - Aplikasi keselamatan transportasi: Jarak reaksi pengemudi, jarak pengereman (*braking distance*), dan analisis jarak berhenti aman (*stopping distance*).

### 🚀 [[Gerak Vertikal dan Kasus Dua Benda SMA | Modul 3: Gerak Vertikal Gravitasi & Dinamika Pertemuan Dua Benda]]
> *Fokus Pembahasan:*
> - Gerak vertikal di bawah percepatan gravitasi bumi ($g \approx 9{,}8\text{ m/s}^2$ atau $10\text{ m/s}^2$):
>   - Gerak Jatuh Bebas (GJB, $v_0 = 0$, $h = \frac{1}{2}gt^2$, $v_t = \sqrt{2gh}$).
>   - Gerak Vertikal ke Bawah (GVB, $v_0 \neq 0$, $v_t^2 = v_0^2 + 2gh$).
>   - Gerak Vertikal ke Atas (GVA, $v_{\text{puncak}} = 0$, $h_{\text{maks}} = \frac{v_0^2}{2g}$, $t_{\text{naik}} = \frac{v_0}{g}$, $t_{\text{total}} = \frac{2v_0}{g}$).
> - Analisis simetri fisis GVA: Waktu naik sama dengan waktu turun ($t_{\text{naik}} = t_{\text{turun}}$), serta kelajuan saat kembali menyentuh tanah sama persis dengan kelajuan awal pelemparan ($|v_{\text{akhir}}| = v_0$).
> - Dinamika pertemuan dua partikel bergerak: Skenario berpapasan saling mendekat ($s_A + s_B = d$) dan skenario saling mengejar / susul-menyusul ($s_B = s_A + \Delta s$).

---

## 🛠️ Instrumen Praktik & Evaluasi

Guna memperkuat keterampilan berpikir analitis-kritis (HOTS), pengolahan data saintifik, serta pengujian pemahaman secara menyeluruh:

1. **Lembar Kerja Peserta Didik (Inkuiri & Eksperimen Kolaboratif):**  
   👉 **[[LKPD Kinematika Gerak Lurus SMA]]**  
   *Memuat 4 aktivitas laboratorium mandiri/kelompok: (1) Ekspedisi GPS & Google Maps (Distingsi Spasial), (2) Bedah Sains Pola Ticker Timer & Tetesan Oli, (3) Studio Kurva Kinematika (Komputasi Gradien & Luas Area), serta (4) Rekonstruksi Kecelakaan Lalu Lintas & Jarak Berhenti Total.*

2. **Paket Soal Evaluasi & Bank Soal HOTS:**  
   👉 **[[Soal Kinematika Gerak Lurus SMA]]**  
   *Terdiri dari 15 Soal Pilihan Ganda HOTS (Level 1 Fondasi C2–C3, Level 2 Analisis Mekanisme C4, Level 3 Evaluasi Kasus & Grafik C4–C5) + 5 Soal Uraian Penalaran Mendalam, dilengkapi Kunci Jawaban Lengkap, Pembahasan Saintifik Step-by-Step, dan Rubrik Penilaian Analitik berbobot 100 Poin.*

---

## ⚡ Cheatsheet Konsep Kunci (Quick Reference)

> [!abstract]- Ringkasan Cepat & Formula Kinematika Gerak Lurus
> - **Gerak Lurus Beraturan (GLB) ($a = 0$):**
>   $$s = v \cdot t$$
>   *Legenda Variabel:*  
>   $s$ = Jarak tempuh atau perpindahan ($\text{m}$)  
>   $v$ = Kelajuan atau kecepatan konstan ($\text{m/s}$)  
>   $t$ = Selang waktu perjalanan ($\text{s}$)  
>
> - **Tiga Persamaan Fundamental GLBB ($a = \text{konstan} \neq 0$):**
>   $$v_t = v_0 + a t$$
>   $$s = v_0 t + \frac{1}{2} a t^2$$
>   $$v_t^2 = v_0^2 + 2 a s$$
>   *Legenda Variabel:*  
>   $v_0$ = Kecepatan awal benda ($\text{m/s}$)  
>   $v_t$ = Kecepatan akhir benda pada saat $t$ ($\text{m/s}$)  
>   $a$ = Percepatan benda ($\text{m/s}^2$); bernilai positif ($+$) jika dipercepat, bernilai negatif ($-$) jika diperlambat  
>   $s$ = Jarak tempuh atau perpindahan benda ($\text{m}$)  
>   $t$ = Waktu tempuh gerak ($\text{s}$)  
>
> - **Kaidah Analisis Grafis ($v-t$):**
>   $$a = \text{Gradien kurva } v-t = \frac{\Delta v}{\Delta t} = \frac{v_t - v_0}{t_t - t_0}$$
>   $$s = \text{Luas daerah di bawah grafik } v-t$$
>
> - **Gerak Jatuh Bebas (GJB) ($v_0 = 0, a = +g$):**
>   $$v_t = g t = \sqrt{2 g h}$$
>   $$h = \frac{1}{2} g t^2$$
>   *Legenda Variabel:*  
>   $h$ = Ketinggian lintasan jatuh vertikal ($\text{m}$)  
>   $g$ = Percepatan gravitasi bumi ($\approx 9{,}8\text{ m/s}^2$ atau $10\text{ m/s}^2$)  
>
> - **Gerak Vertikal ke Atas (GVA) ($a = -g$):**
>   $$h_{\text{maks}} = \frac{v_0^2}{2g}$$
>   $$t_{\text{naik}} = \frac{v_0}{g} \quad \Longrightarrow \quad t_{\text{total}} = \frac{2v_0}{g}$$
>   *Legenda Variabel:*  
>   $h_{\text{maks}}$ = Ketinggian maksimum yang dicapai benda ($\text{m}$)  
>   $t_{\text{naik}}$ = Waktu untuk mencapai ketinggian maksimum ($\text{s}$)  
>   $t_{\text{total}}$ = Waktu total sejak dilempar hingga kembali ke titik awal pelemparan ($\text{s}$)  
>
> - **Kondisi Pertemuan Dua Benda:**
>   - Saling Berpapasan (Berlawanan Arah): $s_A(t) + s_B(t) = d$ ($d$ = jarak mula-mula antar-kedua benda)
>   - Saling Menyusul (Searah): $s_B(t) = s_A(t) + \Delta s$ ($\Delta s$ = jarak keunggulan awal benda A)
