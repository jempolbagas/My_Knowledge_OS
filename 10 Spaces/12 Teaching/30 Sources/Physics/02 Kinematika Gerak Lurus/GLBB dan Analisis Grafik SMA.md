---
title: "GLBB dan Analisis Grafik — Percepatan Konstan & Kurva Kinematika"
type: materi
subject: Physics
level: sma
target_audience: "SMA Kelas X"
created: 2026-09-05
sources:
  - "[[Kinematika Gerak Lurus SMA]]"
  - "[[Besaran Gerak dan GLB SMA]]"
  - "[[Gerak Vertikal dan Kasus Dua Benda SMA]]"
  - "[[LKPD Kinematika Gerak Lurus SMA]]"
tags:
  - fisika
  - sma_kelas_10
  - kurikulum_merdeka
  - materi_ajar
  - kinematika
  - glbb
  - grafik-kinematika
---

# GLBB dan Analisis Grafik — Percepatan Konstan, Persamaan Emas, & Interpretasi Kurva 📈🏎️

> 📍 **Navigasi Modul Kinematika Gerak Lurus:**  
> [[Kinematika Gerak Lurus SMA|🏠 Master Dashboard]] | [[Besaran Gerak dan GLB SMA|⏱️ Modul 1: Besaran & GLB]] | **[📈 Modul 2: GLBB & Grafik]** | [[Gerak Vertikal dan Kasus Dua Benda SMA|🚀 Modul 3: Gerak Vertikal & 2 Benda]] | [[LKPD Kinematika Gerak Lurus SMA|📝 LKPD Inkuiri]] | [[Soal Kinematika Gerak Lurus SMA|🎯 Paket Soal Evaluasi]]

Pernahkah kamu memperhatikan jarum spidometer mobil saat pengemudi menginjak pedal gas dalam-dalam di jalan tol? Jarum tersebut tidak melompat seketika dari $0\text{ km/jam}$ ke $100\text{ km/jam}$, melainkan merangkak naik secara teratur detik demi detik. Sebaliknya, ketika melihat lampu merah dari kejauhan dan pedal rem diinjak, laju kendaraan melambat dengan laju penyusutan yang stabil hingga berhenti sempurna. Fenomena perubahan kelajuan yang teratur terhadap waktu ini adalah wujud nyata dari **Gerak Lurus Berubah Beraturan (GLBB)**. Modul ini membongkar konsep percepatan konstan, membuktikan secara geometris tiga persamaan emas GLBB, mendekonstruksi grafik kurva kinematika ($s-t, v-t, a-t$), hingga menganalisis jarak aman pengereman kendaraan dalam keselamatan lalu lintas.

---

## 1. Hakikat Percepatan ($a$): Perubahan Kecepatan per Satuan Waktu ⏱️⚡

Dalam dunia nyata, partikel jarang sekali bergerak dengan kelajuan yang konstan abadi seperti pada GLB. Benda hampir selalu mengalami percepatan atau perlambatan.

### A. Definisi Fisis Percepatan
**Percepatan ($\vec{a}$)** adalah besaran vektor yang mengukur seberapa cepat kecepatan suatu benda berubah dalam selang waktu tertentu. Satuan SI untuk percepatan adalah meter per sekon kuadrat ($\text{m/s}^2$).

$$\vec{a} = \frac{\Delta \vec{v}}{\Delta t} = \frac{\vec{v}_t - \vec{v}_0}{t_t - t_0}$$
*Legenda Variabel:*  
$\vec{a}$ = Percepatan rata-rata ($\text{m/s}^2$)  
$\vec{v}_0$ = Kecepatan mula-mula benda saat $t = 0$ ($\text{m/s}$)  
$\vec{v}_t$ = Kecepatan akhir benda pada saat $t$ ($\text{m/s}$)  
$\Delta t$ = Selang waktu perubahan kecepatan ($\text{s}$)

### B. Arti Fisis Satuan $\text{m/s}^2$
Jika sebuah mobil memiliki percepatan $a = +4\text{ m/s}^2$, artinya:  
> *"Setiap $1\text{ detik}$ berjalan, kecepatan mobil tersebut bertambah sebesar $4\text{ m/s}$."*  
- Pada $t = 0\text{ s} \longrightarrow v = 0\text{ m/s}$  
- Pada $t = 1\text{ s} \longrightarrow v = 4\text{ m/s}$  
- Pada $t = 2\text{ s} \longrightarrow v = 8\text{ m/s}$  
- Pada $t = 3\text{ s} \longrightarrow v = 12\text{ m/s}$

### C. Klasifikasi: Dipercepat vs Diperlambat (Deselerasi)
1. **GLBB Dipercepat ($a$ searah dengan $\vec{v}$):**  
   Kelajuan benda bertambah seiring berjalannya waktu. Jika gerak ke arah kanan disepakati bernilai positif ($v > 0$), maka percepatan juga bernilai positif ($a > 0$).
2. **GLBB Diperlambat / Retardasi ($a$ berlawanan arah dengan $\vec{v}$):**  
   Kelajuan benda berkurang seiring berjalannya waktu (misalnya saat proses pengereman). Jika gerak ke arah kanan ($v > 0$), maka percepatannya bernilai negatif ($a < 0$). Nilai percepatan negatif ini lazim disebut **perlambatan** (*deceleration*).

---

## 2. Penurunan Tiga Persamaan Emas GLBB 🪙📐

Gerak Lurus Berubah Beraturan didefinisikan sebagai gerak lurus dengan **nilai percepatan yang selalu tetap / konstan ($a = \text{konstan} \neq 0$)**. Dari definisi ini, diturunkan tiga persamaan fundamental:

```
                  ┌────────────────────────────────────────────────┐
                  │          TIGA PERSAMAAN EMAS GLBB              │
                  ├────────────────────────────────────────────────┤
                  │  (1)  vt = v0 + a·t                            │
                  │  (2)  s  = v0·t + ½·a·t²                       │
                  │  (3)  vt² = v0² + 2·a·s                        │
                  └────────────────────────────────────────────────┘
```

### Penurunan Persamaan (1): Hubungan Kecepatan dan Waktu ($v-t$)
Dari definisi percepatan:
$$a = \frac{v_t - v_0}{t} \quad \Longrightarrow \quad v_t - v_0 = a t$$
$$\mathbf{v_t = v_0 + a t}$$

### Penurunan Persamaan (2): Hubungan Posisi dan Waktu ($s-t$)
Perhatikan grafik kecepatan terhadap waktu ($v-t$) pada GLBB berikut. Daerah di bawah garis dari $t=0$ hingga $t$ membentuk bangun **trapesium**:

```
  v (m/s)
   ▲
vt ┼                 /
   │                /│  ▲
   │               / │  │ Δv = a·t (Segitiga)
v0 ┼──────────────/  │  ▼
   │░░░░░░░░░░░░░░│  │
   │░ (Persegi) ░░│  │  (Luas Total = Luas Persegi + Luas Segitiga)
  0└──────────────┴──┴──► t (s)
   0              t
```

$$\text{Luas Persegi Panjang} = v_0 \times t$$
$$\text{Luas Segitiga} = \frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times t \times (v_t - v_0) = \frac{1}{2} \times t \times (a t) = \frac{1}{2} a t^2$$
Karena total perpindahan $s$ adalah akumulasi luas kedua bangun tersebut:
$$\mathbf{s = v_0 t + \frac{1}{2} a t^2}$$

### Penurunan Persamaan (3): Persamaan Bebas Waktu ($v-s$)
Persamaan ketiga digunakan ketika variabel waktu ($t$) tidak diketahui dalam persoalan.  
Dari Persamaan (1), nyatakan waktu sebagai:
$$t = \frac{v_t - v_0}{a}$$
Substitusikan bentuk $t$ ini ke dalam persamaan kecepatan rata-rata $s = \left(\frac{v_0 + v_t}{2}\right) t$:
$$s = \left(\frac{v_t + v_0}{2}\right) \left(\frac{v_t - v_0}{a}\right) = \frac{v_t^2 - v_0^2}{2a}$$
$$2 a s = v_t^2 - v_0^2$$
$$\mathbf{v_t^2 = v_0^2 + 2 a s}$$

*Legenda Variabel Lengkap:*  
$v_0$ = Kecepatan awal partikel ($\text{m/s}$)  
$v_t$ = Kecepatan akhir partikel pada saat $t$ ($\text{m/s}$)  
$a$ = Percepatan konstan partikel ($\text{m/s}^2$); beri tanda ($-$) jika mengalami pengereman/perlambatan  
$s$ = Perpindahan atau jarak tempuh partikel ($\text{m}$)  
$t$ = Selang waktu gerak partikel ($\text{s}$)

---

## 3. Dekonstruksi Visual Kurva Kinematika ($s-t$, $v-t$, $a-t$) 📊

Korelasi fisis antara GLB, GLBB Dipercepat, dan GLBB Diperlambat diilustrasikan secara komprehensif pada diagram di bawah ini:

![[diagram_physics_kinematika_grafik_kurva.webp]]

### Rangkuman Karakteristik Tiga Pasang Grafik:

| Jenis Gerak | Grafik Posisi ($s-t$) | Grafik Kecepatan ($v-t$) | Grafik Percepatan ($a-t$) |
| :--- | :--- | :--- | :--- |
| **GLB** ($a = 0$) | **Garis lurus linier** miring (gradien = $v$) | **Garis horizontal** sejajar sumbu waktu ($v = \text{konstan}$) | **Garis berimpit di nol** ($a = 0$) |
| **GLBB Dipercepat** ($a > 0$) | **Parabola terbuka ke atas** (kecekungan positif, laju bertambah) | **Garis lurus miring naik** (gradien positif = $+a$) | **Garis horizontal di atas sumbu nol** ($a = \text{positif}$) |
| **GLBB Diperlambat** ($a < 0$) | **Parabola terbuka ke bawah** (kecekungan negatif, laju menurun) | **Garis lurus miring turun** (gradien negatif = $-a$) | **Garis horizontal di bawah sumbu nol** ($a = \text{negatif}$) |

### Dua Teorema Emas Grafik $v-t$:
1. **Teorema Kemiringan / Gradien:**  
   $$\text{Gradien kurva } v-t = \frac{\Delta v}{\Delta t} = \text{Percepatan } (a)$$
   - Garis menanjak $\Longrightarrow a > 0$ (dipercepat).
   - Garis mendatar $\Longrightarrow a = 0$ (GLB / kecepatan konstan).
   - Garis menurun $\Longrightarrow a < 0$ (diperlambat / pengereman).
2. **Teorema Luas Bidang:**  
   $$\text{Luas daerah di bawah kurva } v-t = \text{Perpindahan / Jarak Tempuh } (s)$$
   - Jika kurva berada di atas sumbu $t$ ($v > 0$), luas bernilai positif (gerak maju).
   - Jika kurva memotong dan berada di bawah sumbu $t$ ($v < 0$), luas bernilai negatif (gerak mundur).

---

## 4. Aplikasi Nyata Keselamatan: Analisis Jarak Berhenti Total 🛡️🚗

Salah satu aplikasi paling penting dari perpaduan GLB dan GLBB adalah perhitungan **Jarak Berhenti Aman (*Stopping Distance*)** pada kendaraan bermotor.

```
          Pengemudi Melihat Bahaya          Kaki Menginjak Pedal Rem              Mobil Berhenti Total
                     │                                 │                                    │
                     ▼                                 ▼                                    ▼
       Mobil melaju (v0) ──────── GLB ─────────► Mobil mulai mengerem ────── GLBB Diperlambat ──► vt = 0
                     └─────────┬───────────────┘ └──────────────────┬───────────────────────┘
                       Jarak Reaksi (s_reaksi)             Jarak Pengereman (s_rem)
                     └─────────────────────────────┬────────────────────────────────────────┘
                                     Jarak Berhenti Total (s_total)
```

Proses pemberhentian kendaraan terbagi menjadi dua fase berurutan:

### Fase 1: Waktu Reaksi Pengemudi (Fase GLB)
Ketika mata pengemudi melihat rintangan mendadak di jalan (misalnya anak melintas atau lampu rem mobil depan menyala), sinyal visual membutuhkan waktu untuk diproses oleh otak menuju saraf motorik kaki. Selama **waktu reaksi ($t_{\text{reaksi}} \approx 0{,}5\text{ sampai }1{,}0\text{ detik}$)** ini, kaki pengemudi belum sempat menyentuh pedal rem!  
Mobil masih meluncur dengan kelajuan awal konstan ($v_0$) menempuh **Jarak Reaksi**:
$$s_{\text{reaksi}} = v_0 \cdot t_{\text{reaksi}}$$

### Fase 2: Jarak Pengereman Mekanis (Fase GLBB Diperlambat)
Setelah pedal rem diinjak penuh, rem cakram memberikan gaya gesek yang menghasilkan perlambatan maksimum ($a = -a_{\text{rem}}$) hingga mobil berhenti total ($v_t = 0$).  
Menggunakan Persamaan Emas ke-3 GLBB ($v_t^2 = v_0^2 - 2 a_{\text{rem}} s_{\text{rem}}$):
$$0 = v_0^2 - 2 a_{\text{rem}} s_{\text{rem}} \quad \Longrightarrow \quad s_{\text{rem}} = \frac{v_0^2}{2 a_{\text{rem}}}$$

### Total Jarak Berhenti (*Total Stopping Distance*):
$$s_{\text{total}} = s_{\text{reaksi}} + s_{\text{rem}} = \left(v_0 \cdot t_{\text{reaksi}}\right) + \frac{v_0^2}{2 a_{\text{rem}}}$$

> [!WARNING]
> **Hukum Kuadrat Kelajuan:** Perhatikan bahwa $s_{\text{rem}}$ sebanding dengan **kuadrat kelajuan awal ($v_0^2$)**! Artinya, jika kelajuan mobil bertambah $2\times$ lipat (misal dari $40\text{ km/jam}$ menjadi $80\text{ km/jam}$), maka jarak pengereman yang dibutuhkan akan melonjak **$4\times$ lipat lebih jauh**!

---

## 5. Contoh Soal Terapan & Analisis Kurva 🎯

### Kasus 1: Pengereman Mobil Menghindari Tabrakan
Sebuah sedan melaju dengan kelajuan $72\text{ km/jam}$ di jalan lurus. Pengemudi tiba-tiba melihat sebatang pohon tumbang di tengah jalan pada jarak $45\text{ meter}$ di depannya. Waktu reaksi pengemudi adalah $0{,}6\text{ detik}$, dan sistem pengereman mampu menghasilkan deselerasi maksimum $a = 5\text{ m/s}^2$.  
Apakah mobil tersebut akan menabrak pohon tumbang tersebut?

**Solusi Sistematis:**
1. **Konversi Satuan:**  
   $$v_0 = 72\text{ km/jam} = 72 \times \frac{1000\text{ m}}{3600\text{ s}} = \mathbf{20\text{ m/s}}$$
2. **Hitung Jarak Reaksi (Fase GLB):**  
   $$s_{\text{reaksi}} = v_0 \times t_{\text{reaksi}} = 20\text{ m/s} \times 0{,}6\text{ s} = \mathbf{12\text{ meter}}$$
3. **Hitung Jarak Pengereman (Fase GLBB Diperlambat, $v_t = 0$):**  
   $$s_{\text{rem}} = \frac{v_0^2}{2 a} = \frac{20^2}{2 \times 5} = \frac{400}{10} = \mathbf{40\text{ meter}}$$
4. **Hitung Jarak Berhenti Total:**  
   $$s_{\text{total}} = s_{\text{reaksi}} + s_{\text{rem}} = 12\text{ m} + 40\text{ m} = \mathbf{52\text{ meter}}$$
5. **Kesimpulan:**  
   Karena jarak berhenti total ($52\text{ m}$) lebih besar daripada jarak pohon di depan ($45\text{ m}$), maka **mobil tersebut menabrak pohon** dengan sisa jarak $7\text{ m}$ sebelum sempat berhenti tuntas.

---

### Kasus 2: Komputasi Grafik $v-t$ Perjalanan Kereta Listrik
Perhatikan profil grafik $v-t$ perjalanan kereta komuter dari stasiun A ke stasiun B:

```
  v (m/s)
   ▲
20 ┼             ┌──────────────┐
   │            /│              │\
   │           / │              │ \
   │          /  │              │  \
  0└─────────┴───┴──────────────┴───┴──► t (s)
   0         10                 40  50
```

Tentukan:  
a. Percepatan pada selang $t = 0\text{ s}$ sampai $t = 10\text{ s}$, dan $t = 40\text{ s}$ sampai $t = 50\text{ s}$!  
b. Jarak total yang ditempuh kereta antara kedua stasiun tersebut!

**Solusi Sistematis:**
1. **Percepatan Tahap 1 ($0\text{--}10\text{ s}$, menanjak):**  
   $$a_1 = \frac{v_{10} - v_0}{10 - 0} = \frac{20 - 0}{10} = \mathbf{+2\text{ m/s}^2} \quad (\text{GLBB Dipercepat})$$
2. **Percepatan Tahap 2 ($10\text{--}40\text{ s}$, mendatar):**  
   $$a_2 = \frac{20 - 20}{40 - 10} = \mathbf{0\text{ m/s}^2} \quad (\text{GLB})$$
3. **Percepatan Tahap 3 ($40\text{--}50\text{ s}$, menurun):**  
   $$a_3 = \frac{0 - 20}{50 - 40} = \frac{-20}{10} = \mathbf{-2\text{ m/s}^2} \quad (\text{GLBB Diperlambat})$$
4. **Jarak Total (Metode Luas Bangun Trapesium):**  
   $$\text{Sisi Sejajar Atas} = 40 - 10 = 30\text{ s}$$  
   $$\text{Sisi Sejajar Bawah} = 50 - 0 = 50\text{ s}$$  
   $$\text{Tinggi Trapesium} = 20\text{ m/s}$$  
   $$s = \frac{\text{Sisi Atas} + \text{Sisi Bawah}}{2} \times \text{tinggi} = \frac{30 + 50}{2} \times 20 = 40 \times 20 = \mathbf{800\text{ meter}}$$

---

> 📍 **Navigasi Modul Kinematika Gerak Lurus:**  
> [[Kinematika Gerak Lurus SMA|🏠 Master Dashboard]] | [[Besaran Gerak dan GLB SMA|⏱️ Modul 1: Besaran & GLB]] | **[📈 Modul 2: GLBB & Grafik]** | [[Gerak Vertikal dan Kasus Dua Benda SMA|🚀 Modul 3: Gerak Vertikal & 2 Benda]] | [[LKPD Kinematika Gerak Lurus SMA|📝 LKPD Inkuiri]] | [[Soal Kinematika Gerak Lurus SMA|🎯 Paket Soal Evaluasi]]
