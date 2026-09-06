---
title: "Gerak Vertikal dan Kasus Dua Benda — Aplikasi Gravitasi & Dinamika Pertemuan"
type: materi
subject: Physics
level: sma
target_audience: "SMA Kelas X"
created: 2026-09-05
sources:
  - "[[Kinematika Gerak Lurus SMA]]"
  - "[[Besaran Gerak dan GLB SMA]]"
  - "[[GLBB dan Analisis Grafik SMA]]"
  - "[[LKPD Kinematika Gerak Lurus SMA]]"
tags:
  - fisika
  - sma_kelas_10
  - kurikulum_merdeka
  - materi_ajar
  - kinematika
  - gerak-vertikal
  - kasus-dua-benda
---

# Gerak Vertikal dan Kasus Dua Benda — Tarikan Gravitasi & Simfoni Pertemuan Partikel 🚀🍎

> 📍 **Navigasi Modul Kinematika Gerak Lurus:**  
> [[Kinematika Gerak Lurus SMA|🏠 Master Dashboard]] | [[Besaran Gerak dan GLB SMA|⏱️ Modul 1: Besaran & GLB]] | [[GLBB dan Analisis Grafik SMA|📈 Modul 2: GLBB & Grafik]] | **[🚀 Modul 3: Gerak Vertikal & 2 Benda]** | [[LKPD Kinematika Gerak Lurus SMA|📝 LKPD Inkuiri]] | [[Soal Kinematika Gerak Lurus SMA|🎯 Paket Soal Evaluasi]]

Jika sebuah koin logam seberat $10\text{ gram}$ dan sebutir batu seberat $1\text{ kilogram}$ dijatuhkan secara bersamaan dari ketinggian yang sama di ruang hampa udara, manakah yang akan menyentuh lantai terlebih dahulu? Aristoteles pada era kuno meyakini benda berat akan jatuh lebih cepat, namun Galileo Galilei membuktikan sebaliknya: **semua benda tanpa memandang massa jatuh dengan percepatan gravitasi yang persis sama**. Gerak vertikal merupakan manifestasi paling alami dari GLBB pada sumbu tegak ($y$). Modul ini mengupas tuntas tiga variasi gerak vertikal di bawah kendali gravitasi bumi, hukum simetri pelemparan ke atas, hingga strategi aljabar cerdas memecahkan persoalan dua benda yang saling berpapasan atau kejar-kejaran.

---

## 1. Hakikat Percepatan Gravitasi Bumi ($g$) 🌍

Di dekat permukaan bumi, semua benda yang bergerak bebas di udara mengalami tarikan gaya berat ke arah pusat bumi. Jika gaya gesekan udara diabaikan (*free fall condition*):
- Semua benda mengalami percepatan yang bernilai tetap, yaitu **percepatan gravitasi ($g$)**.
- Nilai standar percepatan gravitasi bumi di permukaan laut adalah $g \approx 9{,}8\text{ m/s}^2$, atau untuk mempermudah perhitungan numerik sering dibulatkan menjadi $g = 10\text{ m/s}^2$.
- Karena arah gravitasi selalu mengarah tegak lurus ke bawah (menuju pusat bumi), maka tanda percepatan disesuaikan dengan arah gerak benda:
  - **Gerak ke bawah:** Dipercepat oleh gravitasi ($a = +g$).
  - **Gerak ke atas:** Diperlambat oleh gravitasi ($a = -g$).

---

## 2. Tiga Varian Gerak Vertikal (GLBB Sumbu Y) 📐

Gerak vertikal diklasifikasikan menjadi tiga jenis berdasarkan ada-tidaknya kecepatan awal serta arah lemparannya:

```
        GERAK JATUH BEBAS (GJB)       GERAK VERTIKAL KE BAWAH (GVB)     GERAK VERTIKAL KE ATAS (GVA)
              (v0 = 0)                         (v0 ≠ 0)                          (v0 > 0)
                 ●                                ●                                 ▲
                 │                                │ v0                              │ v0
                 │ a = +g                         │ a = +g                          │ a = -g
                 ▼                                ▼                                 ● (Titik Lempar)
                 
           vt = √(2gh)                      vt = √(v0² + 2gh)                  h_maks = v0² / (2g)
```

---

### A. Gerak Jatuh Bebas (GJB)
- **Definisi:** Gerak suatu benda yang dijatuhkan dari suatu ketinggian tertentu **tanpa kecepatan awal ($v_0 = 0$)** dan hanya dipengaruhi oleh gaya gravitasi.
- **Kondisi Awal:** $v_0 = 0$ dan $a = +g$.
- **Formulasi Matematis:**
  $$v_t = g t$$
  $$h = \frac{1}{2} g t^2 \quad \Longrightarrow \quad t = \sqrt{\frac{2h}{g}}$$
  $$v_t = \sqrt{2 g h}$$
  *Legenda Variabel:*  
  $v_t$ = Kecepatan benda pada saat $t$ atau saat menyentuh tanah ($\text{m/s}$)  
  $g$ = Percepatan gravitasi bumi ($\text{m/s}^2$)  
  $t$ = Waktu tempuh jatuh bebas ($\text{s}$)  
  $h$ = Ketinggian lintasan jatuh vertikal ($\text{m}$)

> [!TIP]
> **Karakteristik Independen Massa:** Perhatikan bahwa rumus waktu jatuh $t = \sqrt{\frac{2h}{g}}$ dan kecepatan akhir $v_t = \sqrt{2gh}$ sama sekali **tidak memuat variabel massa ($m$)**! Artinya, mobil seberat $2\text{ ton}$ dan kelereng seberat $5\text{ gram}$ yang dijatuhkan bersamaan dari atap gedung akan mendarat di tanah pada detik yang sama dengan kelajuan yang sama (bila gesekan udara diabaikan).

---

### B. Gerak Vertikal ke Bawah (GVB)
- **Definisi:** Gerak suatu benda yang **dilemparkan atau ditembakkan lurus ke bawah** dengan memiliki kecepatan awal tertentu ($v_0 \neq 0$).
- **Kondisi Awal:** $v_0 \neq 0$ dan $a = +g$.
- **Formulasi Matematis:**
  $$v_t = v_0 + g t$$
  $$h = v_0 t + \frac{1}{2} g t^2$$
  $$v_t^2 = v_0^2 + 2 g h$$

---

### C. Gerak Vertikal ke Atas (GVA)
- **Definisi:** Gerak suatu benda yang **dilemparkan lurus ke atas** dengan kecepatan awal $v_0$. Karena arah gerak berlawanan dengan arah gravitasi, benda mengalami perlambatan konstan ($a = -g$) hingga berhenti sesaat di titik tertinggi.
- **Kondisi Puncak:** Di ketinggian maksimum ($h_{\text{maks}}$), kecepatan sesaat benda menjadi **nol ($v_t = 0$)**, sebelum berbalik arah jatuh ke bawah.
- **Formulasi Titik Puncak:**
  $$0 = v_0 - g t_{\text{naik}} \quad \Longrightarrow \quad \mathbf{t_{\text{naik}} = \frac{v_0}{g}}$$
  $$0 = v_0^2 - 2 g h_{\text{maks}} \quad \Longrightarrow \quad \mathbf{h_{\text{maks}} = \frac{v_0^2}{2g}}$$

### Hukum Simetri Fisis GVA:
1. **Simetri Waktu:** Waktu yang dibutuhkan benda untuk bergerak naik dari tanah ke titik puncak ($t_{\text{naik}}$) persis sama dengan waktu yang dibutuhkan untuk jatuh kembali dari puncak ke tanah ($t_{\text{turun}}$):
   $$t_{\text{total}} = t_{\text{naik}} + t_{\text{turun}} = \frac{2v_0}{g}$$
2. **Simetri Kelajuan:** Besar kelajuan saat benda kembali tiba di titik pelemparan sama persis dengan kelajuan awal saat pertama kali dilemparkan:
   $$|v_{\text{kembali}}| = v_0$$
   *(Hanya arah kecepatannya yang berbalik menjadi mengarah ke bawah).*

---

## 3. Dinamika Pertemuan Dua Benda Bergerak (Kasus HOTS) 🤝🏎️

Dalam evaluasi fisika SMA dan seleksi perguruan tinggi, persoalan gerak dua partikel merupakan materi favorit untuk menguji kemampuan pemodelan aljabar.

```
       KASUS A: BERPAPASAN (SALING MENDEKAT)               KASUS B: SUSUL-MENYUSUL (SEARAH)
          vA ──►                  ◄── vB                      vA ──►              vB ──►
      ● A ────────────────────────────── ● B              ● A ─────────────── ● B ─────────────────►
      └──────────────── d ───────────────┘                └─── Δs (Selisih) ──┘
               sA(t) + sB(t) = d                                    sA(t) = sB(t) + Δs
```

### Skenario 1: Dua Benda Berpapasan (Berlawanan Arah)
Dua benda A dan B terpisah sejauh $d$, bergerak saling menyongsong dari dua arah berlawanan hingga berpapasan pada waktu $t$:
$$\mathbf{s_A(t) + s_B(t) = d}$$
- **Jika keduanya GLB:**  
  $$v_A t + v_B t = d \quad \Longrightarrow \quad t_{\text{temu}} = \frac{d}{v_A + v_B}$$
- **Jika A GLB dan B GLBB (dari diam, $a_B$):**  
  $$v_A t + \frac{1}{2} a_B t^2 = d$$

### Skenario 2: Dua Benda Saling Mengejar / Susul-Menyusul (Searah)
Benda A berada di belakang benda B dengan jarak pemisah awal $\Delta s$. Benda A mengejar benda B dan tepat berdampingan saat waktu $t$:
$$\mathbf{s_A(t) = s_B(t) + \Delta s}$$
- Jika benda B berangkat lebih awal selama $\Delta t$ sekon dibanding benda A, maka selang waktu gerak benda B menjadi $t_B = t_A + \Delta t$.

---

## 4. Contoh Soal Terapan & Strategi Pemecahan 🎯

### Kasus 1: Pelemparan Vertikal dari Puncak Gedung
Sebuah bola dilemparkan vertikal ke atas dari atap sebuah gedung setinggi $H = 40\text{ meter}$ dengan kecepatan awal $v_0 = 10\text{ m/s}$. Percepatan gravitasi bumi $g = 10\text{ m/s}^2$.  
Tentukan:  
a. Ketinggian maksimum yang dicapai bola diukur dari atas tanah!  
b. Waktu total yang dibutuhkan bola hingga menghantam permukaan tanah!

**Solusi Sistematis:**
1. **Tinggi Maksimum di Atas Atap Gedung:**  
   $$h_{\text{maks}} = \frac{v_0^2}{2g} = \frac{10^2}{2 \times 10} = \frac{100}{20} = \mathbf{5\text{ meter}}$$
   - Tinggi maksimum dari permukaan tanah:  
     $$H_{\text{total}} = H + h_{\text{maks}} = 40 + 5 = \mathbf{45\text{ meter}}$$
2. **Waktu Total Hingga Mencapai Tanah:**  
   Gunakan persamaan posisi vertikal dengan titik acuan atap gedung ($y_0 = 0$, arah atas positif, arah bawah negatif sehingga tanah berada di $y = -40\text{ m}$):
   $$y_t = v_0 t - \frac{1}{2} g t^2$$
   $$-40 = 10 t - \frac{1}{2}(10) t^2$$
   $$-40 = 10 t - 5 t^2$$
   Pindahkan seluruh suku ke ruas kiri dan bagi dengan $5$:
   $$5 t^2 - 10 t - 40 = 0 \quad \Longrightarrow \quad t^2 - 2 t - 8 = 0$$
   Faktorkan persamaan kuadrat:
   $$(t - 4)(t + 2) = 0$$
   Karena waktu tidak mungkin bernilai negatif, maka:
   $$\mathbf{t = 4\text{ detik}}$$

---

### Kasus 2: Polisi Mengejar Pelanggar Batas Kecepatan
Sebuah sedan pelanggar melintas di depan pos polisi dengan kelajuan tetap $v_M = 30\text{ m/s}$ (GLB). Tepat $2\text{ detik}$ kemudian, sebuah mobil patroli polisi mulai mengejar dari keadaan diam dengan percepatan tetap $a_P = 5\text{ m/s}^2$ (GLBB).  
Berapa lama waktu yang dibutuhkan polisi sejak mulai bergerak untuk menyusul mobil sedan tersebut?

**Solusi Sistematis:**
1. **Definisi Variabel Waktu:**  
   - Misalkan waktu tempuh mobil patroli polisi adalah $t$ sekon.  
   - Karena sedan telah melaju $2\text{ detik}$ lebih awal, maka waktu tempuh sedan adalah $t_M = (t + 2)$ sekon.
2. **Kondisi Susul-Menyusul:**  
   $$s_P(t) = s_M(t)$$
   $$\frac{1}{2} a_P t^2 = v_M (t + 2)$$
   $$\frac{1}{2} (5) t^2 = 30(t + 2)$$
   $$2{,}5 t^2 = 30 t + 60$$
   Kalikan dengan $2$ untuk menyederhanakan:
   $$5 t^2 - 60 t - 120 = 0 \quad \Longrightarrow \quad t^2 - 12 t - 24 = 0$$
   Gunakan rumus kuadratik (rumus ABC):
   $$t = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{12 \pm \sqrt{(-12)^2 - 4(1)(-24)}}{2} = \frac{12 \pm \sqrt{144 + 96}}{2} = \frac{12 \pm \sqrt{240}}{2}$$
   $$t \approx \frac{12 + 15{,}49}{2} = \frac{27{,}49}{2} \approx \mathbf{13{,}75\text{ detik}}$$
   - Polisi berhasil menyusul sedan setelah bergerak selama $\approx 13{,}75\text{ detik}$.

---

### Kasus 3: Dua Bola Bertabrakan Vertikal
Bola A dijatuhkan bebas ($v_{0A} = 0$) dari puncak menara setinggi $80\text{ m}$. Pada saat yang bersamaan, bola B ditembakkan vertikal ke atas dari dasar tanah dengan kelajuan awal $v_{0B} = 40\text{ m/s}$.  
Kapan dan pada ketinggian berapa kedua bola saling bertabrakan di udara?

**Solusi Sistematis:**
1. **Analisis Gerak Masing-Masing Bola:**  
   - Bola A (GJB ke bawah): $s_A = \frac{1}{2} g t^2 = 5 t^2$  
   - Bola B (GVA ke atas): $s_B = v_{0B} t - \frac{1}{2} g t^2 = 40 t - 5 t^2$
2. **Kondisi Berpapasan:**  
   $$s_A + s_B = H$$
   $$(5 t^2) + (40 t - 5 t^2) = 80$$
   Perhatikan bahwa suku kuadrat saling menghilangkan ($5t^2 - 5t^2 = 0$):
   $$40 t = 80 \quad \Longrightarrow \quad \mathbf{t = 2\text{ detik}}$$
3. **Ketinggian Tabrakan Diukur dari Tanah ($s_B$):**  
   $$h_{\text{tabrakan}} = s_B = 40(2) - 5(2)^2 = 80 - 20 = \mathbf{60\text{ meter di atas tanah}}$$

---

> 📍 **Navigasi Modul Kinematika Gerak Lurus:**  
> [[Kinematika Gerak Lurus SMA|🏠 Master Dashboard]] | [[Besaran Gerak dan GLB SMA|⏱️ Modul 1: Besaran & GLB]] | [[GLBB dan Analisis Grafik SMA|📈 Modul 2: GLBB & Grafik]] | **[🚀 Modul 3: Gerak Vertikal & 2 Benda]** | [[LKPD Kinematika Gerak Lurus SMA|📝 LKPD Inkuiri]] | [[Soal Kinematika Gerak Lurus SMA|🎯 Paket Soal Evaluasi]]
