---
title: "Active Recall Drills & Advanced Problem Sets — Kebijakan Moneter dan Fiskal"
course: "Self-Study Ekonomi Makro"
course_abbr: "EKOMAKRO"
semester: 
week: 
date: "2026-08-22"
tags: ["practice-drills", "macroeconomics", "baumol-tobin", "cramer-rule", "mundell-fleming", "debt-sustainability"]
type: SelfStudyDrills
---

# 🧠 Advanced Active Recall Drills & Problem Sets — Kebijakan Moneter dan Fiskal

> [!info] **Master Dashboard:** [[00_Master_Dashboard]]
> **Module Links:** [[Kebijakan_Moneter_Notes|Modul 01: Moneter]] | [[Kebijakan_Fiskal_Notes|Modul 02: Fiskal]] | [[Model_IS_LM_Notes|Modul 03: IS-LM & Policy Mix]] | [[Kebijakan_Moneter_dan_Fiskal_Cheatsheet|Formula Cheatsheet]]

---

## 📝 Part I: Modul 01 — Kebijakan Moneter Advanced

### Q1: Kalkulasi Optimalisasi Kas Baumol-Tobin
Seorang investor institusi menerima pendapatan bulanan $Y = \text{Rp } 7.200.000.000$ (7,2 Miliar) yang didepositokan pada instrumen pasar uang dengan suku bunga $i = 8\%$ per tahun ($i = 0,6667\%$ per bulan). Setiap kali mencairkan dana deposit menjadi kas tunai, investor dikenakan biaya transaksi tetap $F = \text{Rp } 300.000$.
1. Hitung jumlah penarikan optimal ($N^*$) yang meminimalkan total biaya!
2. Hitung rata-rata saldo kas yang dipegang investor ($M^*$)!
3. Jika suku bunga naik menjadi $i' = 12\%$ per tahun ($1\%$ per bulan), berapakah saldo kas baru $M'^*$ dan berapakah persentase penurunannya?

### Q2: Formulasi Aturan Suku Bunga Taylor (*Taylor Rule*)
Diketahui suku bunga riil netral $r_n = 2\%$, target inflasi bank sentral $\pi^* = 3\%$, inflasi aktual $\pi_t = 5\%$, dan terjadi *negative output gap* di mana $y_t$ berada $2\%$ di bawah output potensial ($y_t - \bar{y}_t = -2\%$).
1. Hitung suku bunga acuan nominal ($i_t$) yang ideal ditetapkan oleh Bank Sentral berdasarkan Taylor Rule standar ($a_\pi = 0.5, a_y = 0.5$)!
2. Jika Bank Sentral menurunkan respon inflasi menjadi $a_\pi = 0.2$, tunjukkan bahwa Prinsip Taylor (*Taylor Principle*) dilanggar dan jelaskan dampaknya terhadap suku bunga riil!

---

## 📝 Part II: Modul 02 — Kebijakan Fiskal & Debt Sustainability

### Q3: Derivasi Pengganda Ekonomi Terbuka dengan Stabilisator Otomatis
Diketahui struktur perekonomian terbuka:
- $C = 500 + 0,75 Y_d$
- Pajak proporsional: $T = 0,2 Y$
- Investasi: $I = 400 - 30r$
- Belanja Pemerintah: $G = 600$
- Impor: $M = 100 + 0,1 Y$
- Ekspor: $X = 300$

1. Turunkan persamaan Kurva IS!
2. Tentukan besarnya nilai Pengganda Belanja Negara Ekonomi Terbuka ($K_{g,open}$)!
3. Bandingkan nilai pengganda tersebut jika ekonomi bersifat tertutup tanpa pajak ($t=0, m=0$) dan jelaskan fungsi pajak & impor sebagai *automatic stabilizers*!

### Q4: Analisis Keberlanjutan Utang Negara (*Debt Sustainability Analysis*)
Suatu negara memiliki rasio utang terhadap PDB $b_{t-1} = 60\%$. Beban suku bunga riil utang pemerintah $r = 5\%$ per tahun, sementara tingkat pertumbuhan PDB riil negara tersebut $g = 3\%$ per tahun.
1. Tentukan apakah rasio utang $b_t$ akan bertambah atau berkurang jika pemerintah menjalankan anggaran dengan **surplus primer 0%** ($ps_t = 0$)?
2. Hitung berapa rasio surplus primer terhadap PDB ($ps_t^*$) yang wajib dicapai pemerintah agar rasio utang stabil di angka 60% ($\Delta b_t = 0$)!

---

## 📝 Part III: Modul 03 — Model IS-LM Matriks & Mundell-Fleming

### Q5: Solusi Sistem Matriks IS-LM & Derivasi Eksak Crowding-Out
Diketahui sistem persamaan makroekonomi:
- Kurva IS: $0,4 Y + 40 r = 2000$ (dari $C = 200 + 0,8 Y_d, T = 0,25 Y, I = 300 - 40r, G = 500$)
- Kurva LM: $0,5 Y - 60 r = 600$ (dari $\frac{M^s}{P} = 600, L = 0,5 Y - 60 r$)

**Tugas:**
1. Susun sistem persamaan tersebut ke dalam bentuk matriks $A \cdot x = d$ dan hitung determinan matriks koefisien $\det(A)$!
2. Gunakan **Teorema Cramer** untuk menghitung tingkat pendapatan nasional ($Y^*$) dan suku bunga ($r^*$)!
3. Jika belanja negara naik $\Delta G = 100$, hitung nilai $Y^{**}$ baru, lalu hitung secara eksperimental dan teoretis besarnya hilangnya output akibat efek *Crowding-Out*!

### Q6: Analisis Kebijakan Model Mundell-Fleming
Suatu negara kecil menerapkan rejim **Nilai Tukar Mengambang (*Floating Exchange Rate*)** dengan mobilitas modal bebas sempurna ($r = r^*$).
1. Jika pemerintah melakukan ekspansi fiskal besar-besaran ($\Delta G > 0$), jelaskan alur mekanisme penyesuaian pasar valas dan mengapa output nasional $Y$ **tidak berubah sama sekali** ($\Delta Y = 0$)!
2. Bagaimana hasilnya jika negara tersebut mengganti rejim menjadi **Nilai Tukar Tetap (*Fixed Exchange Rate*)**?

---

## 🔑 Kunci Jawaban & Pembahasan Lengkap

### Pembahasan Q1 (Baumol-Tobin Cash Demand):
1. **Jumlah Penarikan Optimal ($N^*$):**
   $$ N^* = \sqrt{\frac{i Y}{2 F}} = \sqrt{\frac{0.006667 \times 7.200.000.000}{2 \times 300.000}} = \sqrt{\frac{48.000.000}{600.000}} = \sqrt{80} \approx 8,94 \text{ kali/bulan} $$
2. **Saldo Kas Rata-rata ($M^*$):**
   $$ M^* = \frac{Y}{2 N^*} = \frac{7.200.000.000}{2 \times 8.9443} = \text{Rp } 402.492.235 $$
3. **Saat Bunga Naik ($i' = 1\%$ per bulan):**
   $$ N'^* = \sqrt{\frac{0.01 \times 7.200.000.000}{600.000}} = \sqrt{120} \approx 10,95 \text{ kali} $$
   $$ M'^* = \frac{7.200.000.000}{21.9089} = \text{Rp } 328.633.535 $$
   Terjadi penurunan permintaan uang kas sebesar $18.35\%$.

### Pembahasan Q2 (Taylor Rule):
1. **Suku Bunga Nominal Taylor ($i_t$):**
   $$ i_t = r_n + \pi_t + 0.5(\pi_t - \pi^*) + 0.5(y_t - \bar{y}_t) $$
   $$ i_t = 2\% + 5\% + 0.5(5\% - 3\%) + 0.5(-2\%) = 7\% + 0.5(2\%) - 1\% = 7\% + 1\% - 1\% = 7\% $$
2. **Jika $a_\pi = 0.2$ (Pelanggaran Taylor Principle):**
   $$ i_t = 2\% + 5\% + 0.2(2\%) - 1\% = 6.4\% $$
   Suku bunga riil $r = i_t - \pi_t = 6.4\% - 5\% = 1.4\%$ (turun dari suku bunga riil netral 2%). Karena kenaikan inflasi $2\%$ hanya direspon dengan kenaikan nominal $0.4\%$, suku bunga riil malah **menurun**, yang memicu akselerasi permintaan agregat dan inflasi tak terkendali (*hyperinflationary spiral*).

### Pembahasan Q3 (Pengganda Ekonomi Terbuka):
1. **Kurva IS:**
   $$ Y = C + I + G + X - M = 500 + 0,75(0,8Y) + 400 - 30r + 600 + 300 - (100 + 0,1Y) $$
   $$ Y = 1700 + 0,6Y - 30r - 0,1Y \implies 0,5Y = 1700 - 30r \implies Y = 3400 - 60r $$
2. **Pengganda Belanja Terbuka:**
   $$ K_{g,open} = \frac{1}{1 - 0.75(1-0.2) + 0.1} = \frac{1}{1 - 0.6 + 0.1} = \frac{1}{0.5} = 2 $$
3. **Perbandingan:** Pada ekonomi tertutup sederhana, $K_g = \frac{1}{1-0.75} = 4$. Pajak $t$ dan impor $m$ menurunkan nilai pengganda dari 4 menjadi 2, berfungsi sebagai peredam kejutan (*stabilizer*).

### Pembahasan Q4 (Debt Sustainability):
1. **Jika $ps_t = 0$:**
   $$ \Delta b_t = (r - g) b_{t-1} - ps_t = (0.05 - 0.03) \times 0.60 - 0 = 0.02 \times 0.60 = +0.012 \text{ atau } +1.2\% $$
   Rasio utang meledak bertambah $1.2\%$ dari PDB setiap tahun.
2. **Rasio Surplus Primer Agar Stabil ($\Delta b_t = 0$):**
   $$ 0 = (0.05 - 0.03) \times 0.60 - ps_t^* \implies ps_t^* = 0.02 \times 0.60 = 0.012 \text{ atau } 1.2\% \text{ dari PDB} $$
   Pemerintah wajib mencetak surplus primer sebesar **1.2% dari PDB**.

### Pembahasan Q5 (Matriks IS-LM & Crowding-Out):
1. **Bentuk Matriks $A \cdot x = d$:**
   $$ \begin{bmatrix} 0,4 & 40 \\ 0,5 & -60 \end{bmatrix} \begin{bmatrix} Y \\ r \end{bmatrix} = \begin{bmatrix} 2000 \\ 600 \end{bmatrix} $$
   $$ \det(A) = (0,4)(-60) - (40)(0,5) = -24 - 20 = -44 $$

2. **Aturan Cramer:**
   $$ \det(A_Y) = \det \begin{bmatrix} 2000 & 40 \\ 600 & -60 \end{bmatrix} = -120.000 - 24.000 = -144.000 $$
   $$ Y^* = \frac{-144.000}{-44} = 3272,73 $$

   $$ \det(A_r) = \det \begin{bmatrix} 0,4 & 2000 \\ 0,5 & 600 \end{bmatrix} = 240 - 1000 = -760 $$
   $$ r^* = \frac{-760}{-44} = 17,27\% $$

3. **Hitung Crowding Out ($\Delta G = 100$):**
   - Tanpa perubahan $r$ (LM horizontal), Pengganda Keynesian $K_g = \frac{1}{0.4} = 2.5 \implies \Delta Y_{Keynes} = 2.5 \times 100 = 250$.
   - Pengganda IS-LM Nyata: $\alpha_G = \frac{h}{\Delta} = \frac{60}{44} = 1.3636 \implies \Delta Y_{ISLM} = 1.3636 \times 100 = 136,36$.
   - **Besarnya Crowding Out Output:** $250 - 136,36 = 113,64$ unit.

### Pembahasan Q6 (Mundell-Fleming):
1. **Floating Rate Regime:** Ekspansi fiskal $\Delta G > 0$ mendorong kurva IS ke kanan $\implies r > r^* \implies$ terjadi *capital inflow* besar-besaran $\implies$ nilai tukar mengalami apresiasi kuat $\implies$ barang ekspor mahal dan impor murah $\implies$ ekspor netto anjlok ($NX \downarrow$) $\implies$ kurva IS bergeser kembali ke kiri hingga persis berada di posisi awal. Akibatnya, $\Delta Y = 0$.
2. **Fixed Rate Regime:** Saat $r > r^*$, apresiasi dicegah oleh Bank Sentral dengan membeli valas dan mencetak Rupiah ($M^s \uparrow$) $\implies$ Kurva LM ikut bergeser ke kanan hingga $r = r^* \implies$ Output $Y$ mengalami lonjakan maksimal.
