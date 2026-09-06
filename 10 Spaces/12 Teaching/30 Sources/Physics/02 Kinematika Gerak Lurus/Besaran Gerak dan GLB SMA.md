---
title: "Besaran Gerak dan GLB — Fondasi Kinematika Satu Dimensi"
type: materi
subject: Physics
level: sma
target_audience: "SMA Kelas X"
created: 2026-09-05
sources:
  - "[[Kinematika Gerak Lurus SMA]]"
  - "[[GLBB dan Analisis Grafik SMA]]"
  - "[[LKPD Kinematika Gerak Lurus SMA]]"
tags:
  - fisika
  - sma_kelas_10
  - kurikulum_merdeka
  - materi_ajar
  - kinematika
  - glb
  - besaran-gerak
---

# Besaran Gerak dan GLB — Membedah Posisi, Kecepatan, & Keteraturan Lintasan Lurus 🧭📏

> 📍 **Navigasi Modul Kinematika Gerak Lurus:**  
> [[Kinematika Gerak Lurus SMA|🏠 Master Dashboard]] | **[⏱️ Modul 1: Besaran & GLB]** | [[GLBB dan Analisis Grafik SMA|📈 Modul 2: GLBB & Grafik]] | [[Gerak Vertikal dan Kasus Dua Benda SMA|🚀 Modul 3: Gerak Vertikal & 2 Benda]] | [[LKPD Kinematika Gerak Lurus SMA|📝 LKPD Inkuiri]] | [[Soal Kinematika Gerak Lurus SMA|🎯 Paket Soal Evaluasi]]

Pernahkah kamu duduk santai di dalam gerbong kereta api yang baru saja mulai meluncur mulus, lalu saat menatap ke luar jendela, kamu sempat bingung sesaat: *"Apakah keretaku yang bergerak maju, atau kereta di sebelahku yang sedang bergerak mundur?"* Kebingungan ini bukanlah ilusi optik semata, melainkan esensi paling mendasar dari fisika mekanika: **semua gerak di alam semesta bersifat relatif terhadap kerangka acuan yang dipilih**. Modul ini membedah fondasi parameter spasial gerak satu dimensi ($1\text{D}$)—memisahkan mitos dan fakta seputar jarak versus perpindahan, kelajuan versus kecepatan—hingga menganalisis karakteristik partikel yang melaju tanpa percepatan dalam **Gerak Lurus Beraturan (GLB)**.

---

## 1. Kerangka Acuan & Relativitas Gerak 📍

Dalam fisika, sebuah benda dikatakan **bergerak** jika kedudukan atau posisinya mengalami perubahan terhadap suatu titik acuan tertentu seiring berjalannya waktu. Jika posisinya tidak berubah terhadap titik acuan tersebut, benda dinyatakan **diam**.

```
    Pengamat A (Diam di Peron)          Pengamat B (Duduk di Dalam Kereta)
               웃                                     [ 웃 B ]
        ════════════════════════════════════════════════════════════════► v_kereta
```

### Konsekuensi Relativitas:
- Bagi **Pengamat A** yang berdiri di peron stasiun, kereta api beserta seluruh penumpang di dalamnya sedang **bergerak** meninggalkan stasiun dengan kecepatan $\vec{v}$.
- Bagi **Pengamat B** yang duduk berdampingan di kursi penumpang kereta, rekannya di sebelah dinyatakan **diam** karena jarak dan posisi relatif antarkursi tidak mengalami perubahan sama sekali.
- **Kesimpulan Fisis:** Menentukan apakah suatu benda bergerak atau diam selalu mensyaratkan pendefinisian **titik acuan (reference point)** yang eksplisit.

---

## 2. Jarak vs Perpindahan: Skalar vs Vektor 📏🧭

Salah satu kesalahan paling jamak dalam mempelajari kinematika adalah menyamakan antara jarak tempuh (*distance*) dengan perpindahan (*displacement*). Keduanya memiliki dimensi panjang yang sama (satuan SI: meter, $\text{m}$), namun memiliki sifat matematis yang bertolak belakang.

```
Lintasan Sebenarnya (Panjang Total = Jarak, s)
    A ───►───┐
             │
             └───►─── B
    ▲                 ▲
    └───────►─────────┘
    Perpindahan (Δx = Vektor Garis Lurus A ke B)
```

### A. Jarak ($s$) — Besaran Skalar
- **Definisi:** Panjang total seluruh lintasan fisik yang dilalui oleh suatu benda selama bergerak dari titik awal ke titik akhir, tanpa memperhitungkan arah tempuhnya.
- **Karakteristik:** Bersifat skalar, nilainya selalu positif ($s \ge 0$), dan selalu bertambah secara kumulatif selama benda bergerak (tidak pernah berkurang).

### B. Perpindahan ($\Delta x$) — Besaran Vektor
- **Definisi:** Perubahan posisi netto suatu benda dari posisi awal ($x_0$) menuju posisi akhir ($x_t$), diukur sepanjang garis lurus terpendek yang menghubungkan kedua titik tersebut disertai arahnya.
- **Formulasi Matematis:**
  $$\Delta x = x_t - x_0$$
  *Legenda Variabel:*  
  $\Delta x$ = Perpindahan partikel ($\text{m}$)  
  $x_0$ = Posisi awal pada garis koordinat ($\text{m}$)  
  $x_t$ = Posisi akhir pada garis koordinat ($\text{m}$)
- **Karakteristik:** Bersifat vektor, dapat bernilai positif ($+$), negatif ($-$), atau nol ($0$). Tanda $(+)$ dan $(-)$ pada gerak $1\text{D}$ merepresentasikan arah gerak (misalnya: kanan/kiri atau timur/barat).

> [!TIP]
> **Kondisi Khusus Perpindahan Nol:** Jika kamu berlari mengelilingi lapangan sepak bola sejauh $400\text{ m}$ dan kembali tepat ke titik start semula, maka jarak tempuhmu adalah $s = 400\text{ m}$, namun perpindahan nettormu adalah $\Delta x = 0\text{ m}$!

---

## 3. Kelajuan vs Kecepatan: Odometer vs Spidometer 🚗💨

Perbedaan antara skalar dan vektor berlanjut pada penurunan laju perubahan posisi terhadap waktu.

### A. Kelajuan Rata-Rata ($v_{\text{rata-rata}}$) — Skalar
Kelajuan rata-rata mengukur seberapa cepat total jarak fisik ditempuh dalam selang waktu total perjalanan:
$$v_{\text{rata-rata}} = \frac{s_{\text{total}}}{t_{\text{total}}}$$
*Legenda Variabel:*  
$v_{\text{rata-rata}}$ = Kelajuan rata-rata ($\text{m/s}$)  
$s_{\text{total}}$ = Total jarak tempuh kumulatif lintasan ($\text{m}$)  
$t_{\text{total}}$ = Total selang waktu perjalanan termasuk waktu istirahat ($\text{s}$)

### B. Kecepatan Rata-Rata ($\vec{v}_{\text{rata-rata}}$) — Vektor
Kecepatan rata-rata mengukur laju perubahan posisi netto (vektor perpindahan) per satuan selang waktu:
$$\vec{v}_{\text{rata-rata}} = \frac{\Delta x}{\Delta t} = \frac{x_t - x_0}{t_t - t_0}$$
*Legenda Variabel:*  
$\vec{v}_{\text{rata-rata}}$ = Kecepatan rata-rata ($\text{m/s}$)  
$\Delta x$ = Vektor perpindahan netto ($\text{m}$)  
$\Delta t$ = Selang waktu terjadinya perpindahan ($\text{s}$)

### 💡 Fakta Rekayasa: Odometer vs Spidometer
- **Odometer** pada dasbor mobil mencatat akumulasi putaran roda untuk menghitung **jarak total ($s$)**. Nilai odometer tidak akan pernah berkurang meskipun mobil dimundurkan.
- **Spidometer** analog menampilkan besaran **kelajuan sesaat ($v$)**, yaitu nilai kelajuan pada detik tersebut tanpa menunjukkan ke arah mata angin mana mobil melaju.

---

## 4. Gerak Lurus Beraturan (GLB) 🚅

Gerak Lurus Beraturan (GLB) adalah bentuk gerak paling murni dan sederhana dalam mekanika.

### Karakteristik Hakiki GLB:
1. **Lintasan Berupa Garis Lurus:** Partikel bergerak satu dimensi pada sumbu tunggal ($x$).
2. **Kecepatan Konstan ($\vec{v} = \text{konstan}$):** Baik kelajuan (besarnya) maupun arah geraknya tidak pernah mengalami perubahan sepanjang waktu.
3. **Percepatan Nol ($a = 0$):** Karena kecepatannya konstan ($\Delta v = 0$), maka partikel tidak mengalami percepatan maupun perlambatan.
4. **Jarak Sebanding dengan Waktu:** Partikel menempuh panjang lintasan yang persis sama pada setiap selang waktu yang sama.

### Persamaan Matematis GLB:
$$s = v \cdot t$$
Atau jika memperhitungkan posisi awal ($x_0$):
$$x_t = x_0 + v \cdot t$$
*Legenda Variabel:*  
$s$ = Jarak tempuh benda ($\text{m}$)  
$x_t$ = Posisi akhir benda pada saat $t$ ($\text{m}$)  
$x_0$ = Posisi awal benda saat $t = 0$ ($\text{m}$)  
$v$ = Kecepatan konstan benda ($\text{m/s}$)  
$t$ = Waktu tempuh perjalanan ($\text{s}$)

---

## 5. Analisis Grafis Kinematika GLB 📈📊

Pemahaman grafik merupakan kunci utama penguasaan soal-soal fisika modern dan UTBK-SNBT.

### A. Grafik Posisi terhadap Waktu ($s-t$ atau $x-t$)
Grafik $s-t$ pada GLB berupa **garis lurus miring (linier)** yang dimulai dari titik posisi awal.

```
  s (m)
   ▲              /  (Benda A: v lebih besar, garis lebih curam)
   │             /
   │            /   / (Benda B: v lebih kecil, garis lebih landai)
   │           /   /
   │          /   /
   │         /   /
 s0├────────/───/
   │       /   /
  0└──────┴───┴───────► t (s)
```

- **Makna Fisis Gradien (Kemiringan Garis):**
  $$\text{Kemiringan (Gradien) } m = \frac{\Delta s}{\Delta t} = v$$
- Semakin curam kemiringan garis pada grafik $s-t$, semakin besar kecepatan gerak benda tersebut.
- Jika garis grafik $s-t$ mendatar horizontal sejajar sumbu waktu ($\text{gradien} = 0$), artinya posisi benda tidak berubah (benda sedang **diam**).
- Jika kemiringan garis mengarah ke bawah (gradien negatif), artinya benda bergerak ke arah berlawanan (mundur menuju titik acuan).

### B. Grafik Kecepatan terhadap Waktu ($v-t$)
Karena kecepatan pada GLB bernilai tetap sepanjang waktu, maka kurva $v-t$ berupa **garis lurus mendatar (horizontal)** sejajar dengan sumbu waktu $t$.

```
  v (m/s)
   ▲
   │
 v ├──────────────┬─────────────── (Kecepatan Konstan)
   │░░░░░░░░░░░░░░│
   │░░░ LUAS = s ░│
   │░░░░░░░░░░░░░░│
  0└──────────────┴───────────────► t (s)
                  t
```

- **Teorema Luas Bidang:** Luas daerah berbentuk persegi panjang di bawah kurva $v-t$ dari $t = 0$ sampai $t$ sama dengan nilai **jarak/perpindahan ($s$)**:
  $$\text{Luas Persegi Panjang} = \text{panjang} \times \text{lebar} = v \cdot t = s$$

---

## 6. Contoh Soal Terapan & Bedah Kasus 🎯

### Kasus 1: Perjalanan Atlet Mengelilingi Lintasan
Seorang pelari berlari ke arah Timur menempuh jarak $120\text{ m}$ dalam waktu $20\text{ detik}$. Kemudian ia berbalik arah melangkah ke Barat sejauh $40\text{ m}$ dalam waktu $10\text{ detik}$.  
Hitunglah:  
a. Jarak total dan perpindahan pelari!  
b. Kelajuan rata-rata dan kecepatan rata-rata pelari!

**Solusi Sistematis:**
1. **Identifikasi Data:**  
   - Tahap 1: $s_1 = 120\text{ m}$ (ke arah $+x$), $t_1 = 20\text{ s}$  
   - Tahap 2: $s_2 = 40\text{ m}$ (ke arah $-x$), $t_2 = 10\text{ s}$  
   - Waktu total: $t_{\text{total}} = 20 + 10 = 30\text{ s}$
2. **Perhitungan Jarak dan Perpindahan:**  
   - Jarak total: $s = s_1 + s_2 = 120 + 40 = \mathbf{160\text{ m}}$  
   - Perpindahan: $\Delta x = (+120) + (-40) = \mathbf{+80\text{ m}}$ (ke arah Timur)
3. **Perhitungan Kelajuan dan Kecepatan Rata-rata:**  
   - Kelajuan rata-rata: $v_{\text{rata-rata}} = \frac{s_{\text{total}}}{t_{\text{total}}} = \frac{160\text{ m}}{30\text{ s}} = \mathbf{5{,}33\text{ m/s}}$  
   - Kecepatan rata-rata: $\vec{v}_{\text{rata-rata}} = \frac{\Delta x}{t_{\text{total}}} = \frac{+80\text{ m}}{30\text{ s}} = \mathbf{+2{,}67\text{ m/s}}$ (ke arah Timur)

---

### Kasus 2: Penerapan GLB Kereta Cepat Whoosh
Kereta Cepat Whoosh melaju lurus stabil dengan kelajuan operasional $360\text{ km/jam}$ melintasi jalur bebas hambatan antara Karawang dan Padalarang.  
a. Konversikan kelajuan kereta tersebut ke dalam satuan internasional ($\text{m/s}$)!  
b. Berapa jarak yang ditempuh kereta tersebut jika ia melaju stabil selama $15\text{ menit}$?

**Solusi Sistematis:**
1. **Konversi Satuan:**  
   $$v = 360\text{ km/jam} = 360 \times \frac{1000\text{ m}}{3600\text{ s}} = \mathbf{100\text{ m/s}}$$
2. **Konversi Waktu:**  
   $$t = 15\text{ menit} = 15 \times 60\text{ s} = \mathbf{900\text{ s}}$$
3. **Kalkulasi Jarak Tempuh (GLB):**  
   $$s = v \cdot t = 100\text{ m/s} \times 900\text{ s} = 90.000\text{ m} = \mathbf{90\text{ km}}$$

---

> 📍 **Navigasi Modul Kinematika Gerak Lurus:**  
> [[Kinematika Gerak Lurus SMA|🏠 Master Dashboard]] | **[⏱️ Modul 1: Besaran & GLB]** | [[GLBB dan Analisis Grafik SMA|📈 Modul 2: GLBB & Grafik]] | [[Gerak Vertikal dan Kasus Dua Benda SMA|🚀 Modul 3: Gerak Vertikal & 2 Benda]] | [[LKPD Kinematika Gerak Lurus SMA|📝 LKPD Inkuiri]] | [[Soal Kinematika Gerak Lurus SMA|🎯 Paket Soal Evaluasi]]
