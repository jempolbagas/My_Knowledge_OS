---
title: "LKPD: Kinematika Gerak Lurus (GLB & GLBB)"
type: lkpd
subject: Physics
level: sma
target_audience: "SMA Kelas X"
created: 2026-09-05
sources:
  - "[[Kinematika Gerak Lurus SMA]]"
  - "[[Besaran Gerak dan GLB SMA]]"
  - "[[GLBB dan Analisis Grafik SMA]]"
  - "[[Gerak Vertikal dan Kasus Dua Benda SMA]]"
tags:
  - lkpd
  - lembar_kerja
  - fisika
  - sma_kelas_10
  - inkuiri
  - kinematika
  - glb
  - glbb
  - hots
---

# Lembar Kerja Peserta Didik (LKPD): Kinematika Gerak Lurus 📝🏎️

> [!info] Informasi Dokumen & Navigasi Cepat
> **Modul Induk:** [[Kinematika Gerak Lurus SMA|🏠 Master Dashboard]] | **Materi Pendukung:** [[Besaran Gerak dan GLB SMA|⏱️ Modul 1: Besaran & GLB]], [[GLBB dan Analisis Grafik SMA|📈 Modul 2: GLBB & Grafik]], & [[Gerak Vertikal dan Kasus Dua Benda SMA|🚀 Modul 3: Gerak Vertikal & 2 Benda]] | **Instrumen Evaluasi:** [[Soal Kinematika Gerak Lurus SMA|🎯 Soal Evaluasi HOTS]]  
> **Jenjang / Kelas:** SMA Kelas X (Fase E)  
> **Model Pembelajaran:** *Inquiry-Based Learning & Collaborative Physics Lab*  
> **Alokasi Waktu:** 2 Pertemuan Pembelajaran ($4 \times 45\text{ Menit}$)

---

## 👥 Identitas Peserta Didik / Kelompok
- **Nama Anggota Kelompok:**
  1. ..................................................................... (Ketua)
  2. .....................................................................
  3. .....................................................................
  4. .....................................................................
- **Kelas / No. Presensi :** X - ....... / ............................
- **Tanggal Eksperimen :** ............................................

---

## 🎯 Tujuan Pembelajaran Inkuiri:
1. Membedakan secara analitis pasangan besaran fisis posisi, jarak, perpindahan, kelajuan, dan kecepatan melalui simulasi data spasial GPS/Google Maps.
2. Menginterpretasikan jejak ketukan pita pewaktu getar (*ticker timer*) dan pola tetesan oli untuk mengidentifikasi jenis gerak lurus (GLB, GLBB dipercepat, dan GLBB diperlambat).
3. Menganalisis kurva grafik posisi ($s-t$) dan kecepatan ($v-t$) secara kuantitatif dengan membuktikan nilai percepatan (gradien) serta jarak tempuh (luas area di bawah kurva).
4. Menerapkan konsep waktu reaksi pengemudi (GLB) dan deselerasi pengereman (GLBB) dalam merekonstruksi kasus keselamatan berkendara dan jarak henti aman (*stopping distance*).

---

## 🗺️ AKTIVITAS 1: Ekspedisi Spasial GPS & Google Maps (Distingsi Besaran Gerak)

Bayangkan kelompokmu sedang merancang perjalanan liburan darat dari **Kota A** menuju **Kota B**, kemudian melanjutkan perjalanan singkat ke tempat wisata di **Kota C**, dan akhirnya kembali pulang tidur di hotel yang terletak di **Kota A**.

```
                           Kota B (Km 120)
                             ▲
                            / │
         Lintasan Berkelok /  │ Jalan Tol Lurus
                          /   │ (80 km ke arah Selatan)
                         /    ▼
       Titik Start/Finish     Kota C (Km 40)
       Kota A (Km 0)
```

### Tabel Analisis Fungsional Besaran Spasial:
Lengkapilah tabel komparasi besaran kinematika di bawah ini berdasarkan pemahaman kelompokmu:

| No | Besaran Fisis | Definisi Operasional | Kategori (Skalar / Vektor) | Nilai Positif / Negatif / Nol? | Satuan SI |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 1 | **Posisi ($x$)** | Letak suatu benda pada suatu garis acuan relatif terhadap titik origin ($0$). | .................... | Bisa positif, negatif, atau nol | $\text{meter (m)}$ |
| 2 | **Jarak Tempuh ($s$)** | .................................................................................................................... | .................... | Selalu .................... | ................ |
| 3 | **Perpindahan ($\Delta x$)** | .................................................................................................................... | .................... | Bisa positif, negatif, atau nol | ................ |
| 4 | **Kelajuan Rata-Rata ($v$)** | Rasio antara total jarak tempuh terhadap total selang waktu perjalanan. | .................... | Selalu .................... | $\text{m/s}$ |
| 5 | **Kecepatan Rata-Rata ($\vec{v}$)** | .................................................................................................................... | .................... | Bisa bernilai .................... | $\text{m/s}$ |

### ❓ Pertanyaan Analisis Kritis (Aktivitas 1):
1. Sebuah mobil keluarga menempuh perjalanan dari Jakarta ke Bandung menempuh jarak $150\text{ km}$ lewat jalan tol, lalu kembali lagi ke Jakarta pada malam hari melalui rute yang sama. Perjalanan pulang-pergi membutuhkan waktu total $6\text{ jam}$.  
   - Berapakah **jarak tempuh total** yang tercatat pada odometer mobil?  
     *Jawaban Kelompok:* ...................................................................................................................................
   - Berapakah **perpindahan total** mobil tersebut sejak berangkat hingga kembali ke garasi rumah?  
     *Jawaban Kelompok:* ...................................................................................................................................
   - Hitunglah **kelajuan rata-rata** dan **kecepatan rata-rata** mobil selama $6\text{ jam}$ tersebut!  
     *Jawaban Kelompok:* ...................................................................................................................................

2. Mengapa jarum penunjuk pada spidometer dasbor mobil hanya bisa menunjukkan angka kelajuan sesaat dan tidak pernah menunjukkan arah gerak kendaraan? Instrumen tambahan apa di smartphone yang mampu menunjukkan arah kecepatan?  
   *Jawaban Kelompok:*  
   ...................................................................................................................................................................................  
   ...................................................................................................................................................................................

---

## ⏱️ AKTIVITAS 2: Bedah Sains Pola Jejak Gerak (Laboratorium Ticker Timer & Tetesan Oli)

Di laboratorium fisika, gerak lurus suatu troli dapat direkam menggunakan pita kertas yang ditarik melintasi jarum pengetik bergetar frekuensi konstan ($50\text{ Hz}$ atau $50\text{ ketukan/sekon}$, sehingga selang waktu antardua titik adalah $\Delta t = 0{,}02\text{ s}$). Di jalan raya, fenomena serupa terjadi saat bak oli mesin mobil mengalami kebocoran dan meneteskan oli dengan interval waktu tetesan yang teratur.

```
PITA TICKER TIMER: (Troli bergerak menarik pita ke arah KANAN)
    ◄── Titik Awal Tertinggal             [Arah Gerak Troli ──►]
    ●       ●       ●       ●       ●       ●   ●  ●  ● ● (Pita Kertas)

TETESAN OLI MOBIL DI ASPAL: (Mobil melaju ke arah KANAN)
    [Titik Awal Tetesan]                          [Arah Gerak Mobil ──►]
    ●   ●  ●  ● ●       ●       ●       ●       ●       ● (Jalan Aspal)
```

> [!WARNING]
> **Awas Jebakan Arah Baca!**  
> - Pada **Ticker Timer**: Titik yang paling pertama dibuat adalah titik yang terletak paling jauh di belakang tarikan troli.  
> - Pada **Tetesan Oli**: Tetesan pertama berada di titik awal di mana mobil mulai melaju, sedangkan tetesan terbaru berada tepat di bawah posisi mobil saat ini.

### Prosedur Analisis Pola Ketukan:
Amatilah pola titik pada tabel berikut, tentukan jenis geraknya, dan jelaskan alasan fisis perubahan jarak antartitiknya!

| Pola Jejak Rekaman | Jenis Alat / Fenomena | Arah Gerak Benda | Jarak Antardua Titik Berurutan | Kesimpulan Jenis Gerak (GLB / GLBB Dipercepat / GLBB Diperlambat) |
| :--- | :--- | :---: | :---: | :---: |
| `●   ●   ●   ●   ●   ●` | Ticker Timer | Ke Kanan | Konstan / Tetap sama | .................................................... |
| `●  ●   ●    ●     ●      ●` | Ticker Timer | Ke Kanan | Semakin .................... | .................................................... |
| `●      ●     ●    ●   ●  ●` | Ticker Timer | Ke Kanan | Semakin .................... | .................................................... |
| `●   ●   ●   ●   ●   ●` | Tetesan Oli Mobil | Ke Kanan | Konstan / Tetap sama | .................................................... |
| `●      ●     ●    ●   ●  ●` | Tetesan Oli Mobil | Ke Kanan | Semakin .................... | .................................................... |

### ❓ Analisis Kinematika Matematis Ticker Timer:
Sebuah pita ticker timer berfrekuensi $50\text{ Hz}$ merekam gerak sebuah troli menuruni bidang miring. Jarak antara titik ke-$1$ dan titik ke-$6$ (mencakup $5$ ketukan selang waktu) diukur menggunakan penggaris dan bernilai $10\text{ cm}$.  
1. Berapakah total selang waktu ($\Delta t$) untuk $5$ ketukan tersebut?  
   *Jawaban Kelompok:* ...................................................................................................................................
2. Hitunglah kelajuan rata-rata troli pada segmen tersebut dalam satuan $\text{m/s}$!  
   *Jawaban Kelompok:* ...................................................................................................................................

---

## 📈 AKTIVITAS 3: Lab Matematika-Fisika Grafik Kinematika (Studio Kurva v-t)

Perhatikan grafik kecepatan terhadap waktu ($v-t$) dari sebuah kendaraan listrik otonom yang melaju lurus di lintasan pengujian berikut:

```
  v (m/s)
   ▲
30 ┼                         ┌────────────────┐ (C)
   │                        /│                │\
20 ┼                       / │                │ \
   │                      /  │                │  \
10 ┼          ┌──────────┘   │                │   \
   │         /│ (B)          │                │    \ (D)
  0└────────┴─┴──────────────┴────────────────┴─────┴──► t (s)
   0        5 10            20               40    50
```

### Panduan Teorema Analitis Grafik:
- **Percepatan ($a$):** Dihitung dari kemiringan gradien garis: $a = \frac{\Delta v}{\Delta t} = \frac{v_{\text{akhir}} - v_{\text{awal}}}{t_{\text{akhir}} - t_{\text{awal}}}$.
- **Jarak Tempuh ($s$):** Dihitung dari total luas bidang geometri (persegi panjang, segitiga, atau trapesium) di bawah kurva $v-t$.

### 🧮 Tabel Komputasi Segmen Gerak Kendaraan:
Isilah tabel analisis gerak per segmen waktu di bawah ini bersama kelompokmu:

| Segmen Waktu ($t$) | Bentuk Kurva Garis | Nilai Kecepatan Awal ($v_0$) & Akhir ($v_t$) | Perhitungan Percepatan ($a = \frac{\Delta v}{\Delta t}$) | Sifat Gerak (GLB / GLBB Dipercepat / GLBB Diperlambat) | Rumus & Perhitungan Luas Area (Jarak Tempuh, $s$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$0\text{ s} - 5\text{ s}$** | Menanjak lurus | $v_0 = 0\text{ m/s}$, $v_5 = 10\text{ m/s}$ | $a = \frac{10 - 0}{5 - 0} = \mathbf{+2\text{ m/s}^2}$ | GLBB Dipercepat | $\text{Luas Segitiga} = \frac{1}{2} \times 5 \times 10 = \mathbf{25\text{ m}}$ |
| **$5\text{ s} - 10\text{ s}$** | Mendatar horizontal | $v_5 = 10\text{ m/s}$, $v_{10} = 10\text{ m/s}$ | $a = \text{........... m/s}^2$ | .................... | $\text{Luas Persegi} = \text{........... m}$ |
| **$10\text{ s} - 20\text{ s}$** | Menanjak lurus | $v_{10} = 10\text{ m/s}$, $v_{20} = 30\text{ m/s}$ | $a = \text{........... m/s}^2$ | .................... | $\text{Luas Trapesium} = \text{........... m}$ |
| **$20\text{ s} - 40\text{ s}$** | Mendatar horizontal | $v_{20} = 30\text{ m/s}$, $v_{40} = 30\text{ m/s}$ | $a = \text{........... m/s}^2$ | .................... | $\text{Luas Persegi} = \text{........... m}$ |
| **$40\text{ s} - 50\text{ s}$** | Menurun lurus | $v_{40} = 30\text{ m/s}$, $v_{50} = 0\text{ m/s}$ | $a = \text{........... m/s}^2$ | .................... | $\text{Luas Segitiga} = \text{........... m}$ |

### ❓ Pertanyaan Analisis Data (Aktivitas 3):
1. Berapakah **jarak total ($s_{\text{total}}$)** yang ditempuh oleh kendaraan listrik tersebut selama $50\text{ detik}$ perjalanan pengujian?  
   *Jawaban Kelompok:* ...................................................................................................................................
2. Hitunglah nilai **kelajuan rata-rata ($v_{\text{rata-rata}}$)** kendaraan listrik tersebut untuk seluruh perjalanan $50\text{ detik}$!  
   *Jawaban Kelompok:* ...................................................................................................................................
3. Pada selang waktu manakah kendaraan mengalami gaya dorong maju terbesar, dan pada selang waktu manakah sistem rem bekerja paling keras? Jelaskan kaitannya dengan nilai percepatan ($a$)!  
   *Jawaban Kelompok:*  
   ...................................................................................................................................................................................  
   ...................................................................................................................................................................................

---

## 🚗 AKTIVITAS 4: Rekonstruksi Kecelakaan Lalu Lintas & Jarak Henti Aman (*Stopping Distance*)

Keselamatan transportasi darat sangat bergantung pada fisika pengereman. Ketika pengemudi melihat bahaya mendadak, kendaraan tidak dapat langsung berhenti seketika karena adanya keterbatasan biologis (waktu reaksi saraf manusia) dan keterbatasan fisis (gaya gesek ban-aspal).

```
   Pengemudi Melihat Rintangan               Rem Mulai Diinjak                      Kendaraan Berhenti
                 │                                  │                                        │
                 ▼                                  ▼                                        ▼
    Kecepatan Awal v0 ───────── (Fase GLB) ───► Kecepatan Masih v0 ── (Fase GLBB Diperlambat) ──► vt = 0
                 └──────────────┬───────────────┘   └────────────────────┬───────────────────┘
                    Jarak Reaksi (s_reaksi)                 Jarak Pengereman (s_rem)
                 └───────────────────────────────┬───────────────────────────────────────────┘
                                   Jarak Berhenti Total (s_total)
```

### Kasus Investigasi Simulasi Dua Pengemudi:
Dua buah mobil identik (Mobil X dan Mobil Y) melaju beriringan di jalur cepat jalan tol dengan kelajuan yang sama, yaitu $v_0 = 108\text{ km/jam}$ ($30\text{ m/s}$). Sistem rem kedua mobil mampu menghasilkan deselerasi maksimum $a_{\text{rem}} = 6\text{ m/s}^2$. Tiba-tiba terjadi tabrakan beruntun di depan mereka pada jarak $100\text{ meter}$.
- **Pengemudi Mobil X:** Pengemudi profesional, sangat fokus, waktu reaksi $t_{\text{reaksi}} = 0{,}6\text{ sekon}$.
- **Pengemudi Mobil Y:** Pengemudi terdistraksi karena sedang melirik notifikasi ponsel, waktu reaksi $t_{\text{reaksi}} = 1{,}5\text{ sekon}$.

#### Formula Wajib:
$$s_{\text{reaksi}} = v_0 \times t_{\text{reaksi}} \quad (\text{GLB})$$
$$s_{\text{rem}} = \frac{v_0^2}{2 a_{\text{rem}}} \quad (\text{GLBB Diperlambat})$$
$$s_{\text{total}} = s_{\text{reaksi}} + s_{\text{rem}}$$

### Tabel Komparasi Hasil Analisis Kelompok:

| Parameter Fisika Pengereman | Mobil X (Pengemudi Fokus) | Mobil Y (Pengemudi Terdistraksi HP) |
| :--- | :---: | :---: |
| **Kelajuan Awal ($v_0$)** | $30\text{ m/s}$ | $30\text{ m/s}$ |
| **Waktu Reaksi ($t_{\text{reaksi}}$)** | $0{,}6\text{ s}$ | $1{,}5\text{ s}$ |
| **Jarak Reaksi ($s_{\text{reaksi}}$)** | .................... meter | .................... meter |
| **Jarak Pengereman ($s_{\text{rem}}$)** | .................... meter | .................... meter |
| **Jarak Berhenti Total ($s_{\text{total}}$)** | **.................... meter** | **.................... meter** |
| **Apakah Menabrak Rintangan yang Berjarak $100\text{ m}$?** | (*Selamat / Menabrak*) | (*Selamat / Menabrak*) |

### ❓ Pertanyaan Evaluasi Kasus (Aktivitas 4):
1. Mengapa pengemudi yang terdistraksi ponsel (Mobil Y) mengalami nasib yang sangat fatal dibanding pengemudi Mobil X, meskipun performa rem kedua mobil persis sama? Jelaskan pengaruh waktu reaksi terhadap jarak tempuh sebelum rem sempat diinjak!  
   *Jawaban Kelompok:*  
   ...................................................................................................................................................................................  
   ...................................................................................................................................................................................

2. Jika pada kondisi jalan basah/hujan licin koefisien gesek ban berkurang sehingga deselerasi rem turun menjadi hanya $a_{\text{rem}} = 3\text{ m/s}^2$ (setengah dari kondisi normal), apa yang terjadi pada jarak pengereman ($s_{\text{rem}}$) Mobil X? Berikan rekomendasi batas kelajuan aman berkendara saat hujan lebat!  
   *Jawaban Kelompok:*  
   ...................................................................................................................................................................................  
   ...................................................................................................................................................................................

---

## 📋 Lembar Kesimpulan Inkuiri & Refleksi Diri

Tuliskan sintesis menyeluruh yang berhasil kelompokmu rumuskan mengenai keterpaduan konsep kinematika gerak lurus, interpretasi grafik, dan aplikasinya dalam keselamatan teknologi transportasi:

```
KESIMPULAN UMUM KELOMPOK:
.........................................................................................................................................................
.........................................................................................................................................................
.........................................................................................................................................................
.........................................................................................................................................................
```

### Rubrik Penilaian Diri (Self-Assessment):
Berilah tanda centang ($\checkmark$) pada kotak pencapaian belajarmu hari ini:

- [ ] Saya mampu membedakan dengan jelas antara jarak vs perpindahan serta kelajuan vs kecepatan pada kasus nyata.
- [ ] Saya dapat membaca dan menganalisis pola titik rekaman pita *ticker timer* serta tetesan oli mobil.
- [ ] Saya mampu menghitung percepatan dari gradien kurva $v-t$ dan menghitung jarak tempuh dari luas daerah di bawah kurva $v-t$.
- [ ] Saya memahami keterkaitan matematis antara waktu reaksi pengemudi (GLB) dan jarak pengereman deselerasi (GLBB) dalam keselamatan berkendara.
