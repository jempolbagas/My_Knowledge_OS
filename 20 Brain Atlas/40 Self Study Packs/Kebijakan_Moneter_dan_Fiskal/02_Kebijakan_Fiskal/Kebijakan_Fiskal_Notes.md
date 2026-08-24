---
title: "Modul 02 — Kebijakan Fiskal (Advanced Deep-Dive)"
course: "Self-Study Ekonomi Makro"
course_abbr: "EKOMAKRO"
semester: 
week: 
date: "2026-08-22"
tags: ["lecture-note", "macroeconomics", "fiscal-policy", "ricardian-equivalence", "debt-sustainability"]
type: SelfStudyNote
---

# 🎓 Modul 02: Kebijakan Fiskal — Mikrofondasi Konsumsi, Pengganda Terbuka, & Berkelanjutan Utang

> [!info] **Master Dashboard:** [[00_Master_Dashboard]] | **Drills:** [[Kebijakan_Moneter_dan_Fiskal_Drills]] | **Cheatsheet:** [[Kebijakan_Moneter_dan_Fiskal_Cheatsheet]]
> **Topics Covered:** Mikrofondasi Konsumsi (PIH, LCH, Ekuivalensi Ricardian), Teori Investasi Tobin's q, Derivasi Pengganda Fiskal Ekonomi Terbuka, *Debt Sustainability Analysis (DSA)*, dan Kerangka Aturan APBN Indonesia (UU 17/2003 & UU HPP).

---

## 📌 1. Overview & Core Context
- **Latar Belakang & Motivasi:** Kebijakan fiskal tidak dapat dianalisis hanya dengan mengasumsikan masyarakat langsung menghabiskan setiap potongan pajak secara naif. Perilaku konsumsi dipengaruhi oleh ekspektasi pendapatan sepanjang hidup (*intertemporal choice*), ekspektasi beban pajak masa depan (*Ricardian Equivalence*), serta struktur keterbukaan perdagangan (*import leakage*).
- **High-Level Takeaway:**
  1. **Mikrofondasi Konsumsi:** *Permanent Income Hypothesis* dan *Life-Cycle Hypothesis* menunjukkan bahwa konsumsi responsif terhadap pendapatan permanen, bukan pendapatan sementara.
  2. **Ekuivalensi Ricardian:** Pemotongan pajak yang dibiayai utang hari ini tidak merangsang konsumsi jika masyarakat mengantisipasi kenaikan pajak di masa depan.
  3. **Analisis Sustainabilitas Utang:** Rasio utang/PDB tergantung pada selisih suku bunga riil dan pertumbuhan ekonomi ($r - g$).

---

## 📖 2. Mathematical Microfoundations & Theoretical Deep-Dive

### 2.1 Mikrofondasi Konsumsi: Intertemporal Choice & Hypotheses

#### A. Konsumsi Intertemporal Fisher & Ricardian Equivalence
Seorang konsumen hidup dalam 2 periode dengan pendapatan $Y_1, Y_2$, konsumsi $C_1, C_2$, dan suku bunga $r$.
Kendala Anggaran Intertemporal:
$$ C_1 + \frac{C_2}{1 + r} = Y_1 - T_1 + \frac{Y_2 - T_2}{1 + r} $$

**Teorema Ekuivalensi Ricardian (Barro-Ricardo):**
Jika pemerintah menurunkan pajak periode 1 sebesar $\Delta T_1$ dan membiayainya dengan menerbitkan utang $B$ yang harus dilunasi pada periode 2 melalui kenaikan pajak $\Delta T_2 = (1+r)\Delta T_1$:
$$ \Delta (Y_1 - T_1) + \frac{\Delta (Y_2 - T_2)}{1 + r} = \Delta T_1 - \frac{(1+r)\Delta T_1}{1 + r} = 0 $$
**Kesimpulan:** Nilai sekarang dari total pendapatan siap dibelanjakan (*present value of disposable income*) **tidak berubah sama sekali**. Konsumen rasional tidak akan menaikkan $C_1$, melainkan menabung seluruh pemotongan pajak tersebut ($\Delta S = \Delta T_1$) untuk membayar kenaikan pajak di periode 2. Dalam kondisi ini, pengganda pajak $K_t = 0$.

#### B. Permanent Income Hypothesis (Friedman) & Life-Cycle (Modigliani)
- Pendapatan terbagi menjadi pendapatan permanen ($Y_p$) dan transitori ($Y_t$): $Y = Y_p + Y_t$.
- Konsumsi hanya merespon $Y_p$: $C = \alpha Y_p$.
- Pemotongan pajak sementara (stimulus satu kali) dianggap sebagai $Y_t$, sehingga memiliki *Marginal Propensity to Consume* ($MPC$) yang mendekati nol.

---

### 2.2 Teori Investasi Swasta: Tobin's q & User Cost of Capital

Investasi swasta ($I$) dianalisis dari keputusan optimasi stok kapital perusahaan ($K$).

#### A. User Cost of Capital
Kondisi optimal akumulasi modal tercapai ketika marjinal produk kapital ($MPK$) sama dengan biaya riil kepemilikan modal (*User Cost*):
$$ MPK = \frac{r + \delta}{1 - \tau} $$
di mana $r$ adalah suku bunga riil, $\delta$ adalah tingkat depresiasi modal, dan $\tau$ adalah tarif pajak korporasi.

#### B. Tobin's q Ratio
$$ q = \frac{\text{Nilai Pasar Saham & Utang Perusahaan}}{\text{Biaya Pengganti Kapital (Replacement Cost of Capital)}} $$
- Jika $q > 1$: Nilai pasar perusahaan lebih tinggi dibanding biaya membeli mesin/peralatan baru $\implies$ Perusahaan terstimulasi melakukan investasi fisik baru ($I > 0$).
- Jika $q < 1$: Lebih murah membeli perusahaan lain melalui akuisisi daripada berinvestasi modal baru $\implies I = 0$.

---

### 2.3 Derivasi Lengkap Pengganda Fiskal Ekonomi Terbuka

Misalkan fungsi perekonomian terbuka:
1. Konsumsi: $C = C_0 + c(Y - T_0 - tY) = C_0 - c T_0 + c(1-t)Y$
2. Investasi: $I = I_0 - br$
3. Belanja Negara: $G = G_0$
4. Ekspor Netto: $NX = X_0 - M = X_0 - (M_0 + mY)$ (di mana $m$ adalah *Marginal Propensity to Import*).

Keseimbangan Keseimbangan Pasar Barang:
$$ Y = C + I + G + NX $$
$$ Y = C_0 - c T_0 + c(1-t)Y + I_0 - br + G_0 + X_0 - M_0 - mY $$
$$ Y [1 - c(1-t) + m] = C_0 - c T_0 + I_0 - br + G_0 + X_0 - M_0 $$
$$ Y = \frac{C_0 - c T_0 + I_0 - br + G_0 + X_0 - M_0}{1 - c(1-t) + m} $$

#### Pengganda Belanja Negara Terbuka ($K_{g,open}$)
$$ K_{g,open} = \frac{\partial Y}{\partial G} = \frac{1}{1 - c(1-t) + m} $$

**Implikasi Makro:** Keterbukaan ekonomi (impor $m > 0$) dan pajak proporsional ($t > 0$) bertindak sebagai **Stabilisator Otomatis (*Automatic Stabilizers*)** yang mengecilkan nilai pengganda fiskal dibanding ekonomi tertutup sederhana ($\frac{1}{1-c}$).

---

### 2.4 Debt Sustainability Analysis (DSA)

Dinamika akumulasi utang pemerintah dari waktu ke waktu diposisikan sebagai berikut:

$$ D_t = (1 + i_t) D_{t-1} - PS_t $$

di mana $D_t$ adalah total nominal utang, $i_t$ suku bunga nominal, dan $PS_t$ adalah surplus primer (*Primary Surplus* $= T_t - G_t$ tanpa pembayaran bunga utang).

Dalam bentuk rasio terhadap PDB nominal ($b_t = \frac{D_t}{P_t Y_t}$):

$$ \Delta b_t = b_t - b_{t-1} \approx (r_t - g_t) b_{t-1} - ps_t $$

di mana:
- $r_t$: Suku bunga riil beban utang.
- $g_t$: Tingkat pertumbuhan PDB riil.
- $ps_t$: Rasio surplus primer terhadap PDB.

#### Kondisi Solvensi Utang (*Solvency Condition*)
- Jika **$r > g$** (suku bunga riil melebihi pertumbuhan ekonomi), pemerintah **wajib** menjalankan surplus primer ($ps_t > 0$) agar rasio utang tidak meledak secara eksponensial (*explosive debt path*).
- Jika **$g > r$** (pertumbuhan ekonomi melebihi suku bunga), perekonomian dapat "tumbuh mengatasi utang" (*grow out of debt*) meskipun mengalami defisit primer kecil.

---

## 🏛️ 3. Kerangka Aturan APBN & Regulasi Indonesia

### 3.1 Aturan Fiskal Utama (UU No. 17 Tahun 2003 tentang Keuangan Negara)
1. **Batas Defisit APBN:** Maksimal **3% dari PDB** pada setiap tahun anggaran (kecuali kondisi darurat yang ditetapkan undang-undang).
2. **Batas Rasio Utang:** Maksimal **60% dari PDB**.

### 3.2 Reformasi Perpajakan (UU No. 7 Tahun 2021 tentang HPP)
- Penyesuaian tarif PPN bertahap (11% dan 12%).
- Integrasi NIK menjadi NPWP untuk memperluas *tax base*.
- Penerapan Pajak Karbon (*Carbon Tax*) sebagai instrumen fiskal lingkungan.

---

## ⚡ 4. Matriks Ringkasan & Formulasi Utama

| Konsep / Teori | Formulasi Matematika | Implikasi Utama / Kebijakan |
| :--- | :--- | :--- |
| **Ricardian Equivalence** | $\Delta C = 0 \implies K_t = 0$ | Pemotongan pajak yang dibiayai utang netral terhadap konsumsi. |
| **Tobin's q** | $q = \frac{\text{Nilai Pasar}}{\text{Replacement Cost}}$ | $q > 1$ memicu insentif investasi fisik baru perusahan. |
| **Pengganda Ekonomi Terbuka** | $K_{g,open} = \frac{1}{1 - c(1-t) + m}$ | Impor ($m$) dan pajak ($t$) meredam efek guncangan belanja. |
| **Dinamika Utang (DSA)** | $\Delta b_t = (r - g) b_{t-1} - ps_t$ | Jika $r > g$, stabilitas utang membutuhkan surplus APBN primer. |
