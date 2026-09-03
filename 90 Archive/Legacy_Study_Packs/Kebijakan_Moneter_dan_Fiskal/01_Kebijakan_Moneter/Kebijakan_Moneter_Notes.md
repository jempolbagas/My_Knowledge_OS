---
title: "Modul 01 — Kebijakan Moneter (Advanced Deep-Dive)"
course: "Self-Study Ekonomi Makro"
course_abbr: "EKOMAKRO"
semester: 
week: 
date: "2026-08-22"
tags: ["lecture-note", "macroeconomics", "monetary-policy", "baumol-tobin", "taylor-rule", "uu-p2sk"]
type: SelfStudyNote
---

# 🎓 Modul 01: Kebijakan Moneter — Teori Pasar Uang, MTKM, & Kerangka Kelembagaan BI

> [!info] **Master Dashboard:** [[00_Master_Dashboard]] | **Drills:** [[Kebijakan_Moneter_dan_Fiskal_Drills]] | **Cheatsheet:** [[Kebijakan_Moneter_dan_Fiskal_Cheatsheet]]
> **Topics Covered:** Teori Permintaan Uang Baumol-Tobin, Penciptaan Uang & Neraca Perbankan, Aturan Suku Bunga Taylor (*Taylor Rule*), Kurva Phillips & Ekspektasi Inflasi, Instrumen Operasi Moneter Modern BI (SRBI/SVBI), Kebijakan Makroprudensial, dan UU No. 4/2023 (UU P2SK).

---

## 📌 1. Overview & Core Context
- **Latar Belakang & Motivasi:** Kebijakan moneter bukan sekadar aksi menaikkan/menurunkan suku bunga secara acak, melainkan intervensi terstruktur atas pasar likuiditas berdasarkan fondasi mikronomik (*microfoundations*). Memahami kebijakan moneter tingkat lanjut membutuhkan analisis neraca bank sentral, teori optimasi kas riil, ekspektasi inflasi forward-looking, dan dinamika kelembagaan hukum terkini.
- **High-Level Takeaway:**
  1. **Mikrofondasi Permintaan Uang:** Model Baumol-Tobin menjelaskan trade-off biaya transaksi vs *opportunity cost* memegang uang tunai.
  2. **Aturan Kebijakan (Policy Rules):** Taylor Rule memberikan pedoman sistematik reaksi suku bunga acuan terhadap deviasi inflasi dan *output gap*.
  3. **Kelembagaan UU P2SK (2023):** Mandat Bank Indonesia kini diperluas untuk mencakup stabilitas nilai Rupiah, stabilitas sistem keuangan, serta mendukung pertumbuhan ekonomi yang berkelanjutan.

---

## 📖 2. Mathematical Microfoundations & Theoretical Deep-Dive

### 2.1 Mikrofondasi Permintaan Uang: Model Baumol-Tobin
Model Baumol-Tobin menjelaskan permintaan uang untuk transaksi ($L_1$) sebagai keputusan optimasi persediaan (*inventory management*).

Misalkan seseorang menerima pendapatan $Y$ per periode yang diinvestasikan pada aset berimbal hasil suku bunga $i$. Untuk bertransaksi, orang tersebut harus mencairkan aset menjadi uang tunai sebanyak $N$ kali per periode. Setiap pencairan dikenakan biaya tetap transaksi $F$.

#### A. Total Biaya Memegang Uang ($TC$)
- Biaya penarikan transaksi: $N \cdot F$
- Rata-rata saldo kas yang dipegang: $\frac{Y}{2N}$
- Biaya kesempatan (*opportunity cost* / bunga hilang): $i \cdot \frac{Y}{2N}$

$$ TC(N) = N \cdot F + i \cdot \frac{Y}{2N} $$

#### B. Optimasi Frekuensi Penarikan ($N^*$)
Turunan pertama $TC(N)$ terhadap $N$ disamakan dengan nol ($\frac{dTC}{dN} = 0$):
$$ \frac{dTC}{dN} = F - \frac{i Y}{2 N^2} = 0 \implies N^2 = \frac{i Y}{2 F} \implies N^* = \sqrt{\frac{i Y}{2 F}} $$

#### C. Permintaan Kas Rata-Rata ($M^*$)
$$ M^* = \frac{Y}{2 N^2} = \frac{Y}{2 \sqrt{\frac{i Y}{2 F}}} = \sqrt{\frac{F Y}{2 i}} $$

**Implikasi Makro:** Permintaan uang riil berbanding lurus dengan akar pendapatan $\sqrt{Y}$ (skala ekonomi dalam memegang uang) dan berbanding terbalik dengan akar suku bunga $\frac{1}{\sqrt{i}}$.

---

### 2.2 Neraca Perbankan & Penciptaan Uang (*Money Creation*)

Uang beredar tidak hanya diciptakan oleh cetakan Bank Sentral, melainkan melalui ekspansi neraca bank umum (*fractional-reserve banking*).

#### A. Komposisi Uang Beredar ($M_1$) & Basis Moneter ($B$)
- Uang Beredar: $M = CU + D$ (Uang Kartal $CU$ + Simpanan Giral $D$).
- Basis Moneter (*High-Powered Money*): $B = CU + R$ (Uang Kartal $CU$ + Cadangan Bank $R$).
- Cadangan Bank: $R = RE + RR$ (Cadangan Wajib $RR = r \cdot D$ + Cadangan Kelebihan $RE = e \cdot D$).

#### B. Derivasi Pengganda Uang Kompleks ($m$)
Bagi dengan $D$:
$$ c = \frac{CU}{D} \quad (\text{Currency Ratio}), \quad r = \frac{RR}{D} \quad (\text{Required Reserve Ratio}), \quad e = \frac{RE}{D} \quad (\text{Excess Reserve Ratio}) $$

$$ M = (c + 1)D \quad \text{dan} \quad B = (c + r + e)D $$

$$ m = \frac{M}{B} = \frac{1 + c}{r + e + c} $$

$$ M^s = \left( \frac{1 + c}{r + e + c} \right) B $$

**Analisis Sensitivitas:** Jika perbankan khawatir akan krisis dan menaikkan *excess reserve* ($e \uparrow$), pengganda uang $m$ akan anjlok meskipun basis moneter $B$ disuntik oleh Bank Sentral (*credit crunch*).

---

### 2.3 Aturan Suku Bunga Taylor (*Taylor Rule*)

Untuk mencegah keputusan diskresioner yang memicu ketidakstabilan, John Taylor merumuskan pedoman suku bunga acuan nominal ($i_t$):

$$ i_t = r_n + \pi_t + a_\pi (\pi_t - \pi^*) + a_y (y_t - \bar{y}_t) $$

di mana:
- $r_n$: Suku bunga riil netral (*neutral real interest rate*).
- $\pi_t$: Inflasi saat ini, $\pi^*$: Target inflasi bank sentral.
- $(y_t - \bar{y}_t)$: *Output gap* (PDB riil vs PDB potensial).
- $a_\pi, a_y$: Bobot responsivitas (standar Taylor: $a_\pi = 0,5$, $a_y = 0,5$).

#### Prinsip Taylor (*Taylor Principle*)
Responsivitas terhadap inflasi harus memuaskan $1 + a_\pi > 1$ (yaitu $\frac{\partial i}{\partial \pi} > 1$). Jika inflasi naik 1%, suku bunga nominal harus dinaikkan **lebih dari 1%** agar suku bunga riil ($r = i - \pi$) naik untuk meredam permintaan agregat.

---

### 2.4 Kurva Phillips & Dynamics Ekspektasi Inflasi

$$ \pi_t = \pi_t^e - \gamma (u_t - u_n) + v_t $$

- **Ekspektasi Adaptif (*Adaptive Expectations*):** $\pi_t^e = \pi_{t-1}$. Inflasi periode lalu menjadi patokan. Menghasilkan trade-off jangka pendek antara inflasi dan pengangguran.
- **Ekspektasi Rasional (*Rational Expectations - Lucas Critique*):** Agen memanfaatkan seluruh informasi kebijakan secara *forward-looking*. Jika Bank Sentral mengumumkan ekspansi moneter yang kredibel, inflasi akan langsung naik tanpa menurunkan pengangguran $u$.

---

## 🏛️ 3. Kerangka Kelembagaan & Instrumen Modern Bank Indonesia

### 3.1 Mandat Baru UU No. 4 Tahun 2023 (UU P2SK)
Pasca reformasi sektor keuangan melalui UU P2SK:
- **Tujuan Tunggal Lama:** Memelihara kestabilan nilai Rupiah (stabilitas harga & nilai tukar).
- **Mandat Diperluas:** Memelihara kestabilan nilai Rupiah, memelihara stabilitas sistem keuangan, serta **turut mendukung pertumbuhan ekonomi yang berkelanjutan**.

### 3.2 Sekuritas Moneter Modern BI
1. **SRBI (Sertifikat Rupiah Bank Indonesia):** Instrumen pro-pasar untuk menyerap likuiditas Rupiah sekaligus menarik aliran modal asing (*capital inflow*) melalui perdagangan pasar sekunder.
2. **SVBI & SUVBI (Sertifikat Valas Bank Indonesia):** Instrumen sekuritisasi valuta asing untuk memperkuat cadangan devisa dan stabilitas nilai tukar Rupiah.
3. **Term Deposit Valas DHE:** Fasilitas penempatan Devisa Hasil Ekspor di Bank Indonesia dengan imbal hasil kompetitif.

### 3.3 Kerangka Kebijakan Makroprudensial
- **CCb (Countercyclical Capital Buffer):** Tambahan modal bank saat periode ekspansi kredit berlebihan.
- **LTV / FTV (Loan-to-Value):** Pembatasan rasio pinjaman terhadap nilai properti/kendaraan.
- **KLM (Kebijakan Insentif Likuiditas Makroprudensial):** Kelonggaran GWM bagi bank yang menyalurkan kredit ke sektor prioritas (hilirisasi, UMKM, ekonomi hijau).

---

## ⚡ 4. Matriks Ringkasan & Formulasi Utama

| Konsep / Teori | Formulasi Matematika | Implikasi Utama / Kebijakan |
| :--- | :--- | :--- |
| **Baumol-Tobin Cash Demand** | $M^* = \sqrt{\frac{F Y}{2 i}}$ | Permintaan kas bereaksi terhadap suku bunga secara non-linier. |
| **Pengganda Uang Kompleks** | $m = \frac{1+c}{r+e+c}$ | Cadangan berlebih ($e$) dan perilaku masyarakat ($c$) menentukan efektivitas basis moneter. |
| **Taylor Rule** | $i_t = r_n + \pi_t + a_\pi(\pi - \pi^*) + a_y(y - \bar{y})$ | Mencegah inflasi dengan menaikkan suku bunga riil saat inflasi terakselerasi. |
| **Kurva Phillips** | $\pi_t = \pi_t^e - \gamma(u_t - u_n) + v_t$ | Menghubungkan ekspektasi inflasi, *unemployment gap*, dan kejutan penawaran ($v$). |
