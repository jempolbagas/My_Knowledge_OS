---
title: "Advanced Summary & Formula Cheatsheet — Kebijakan Moneter dan Fiskal"
course: "Self-Study Ekonomi Makro"
course_abbr: "EKOMAKRO"
semester: 
week: 
date: "2026-08-22"
tags: ["cheatsheet", "macroeconomics", "monetary-policy", "fiscal-policy", "cramer-rule", "mundell-fleming"]
type: SelfStudyCheatsheet
---

# ⚡ Advanced Rapid Reference Cheatsheet — Kebijakan Moneter dan Fiskal

> [!info] **Master Dashboard:** [[00_Master_Dashboard]]
> **Module Links:** [[Kebijakan_Moneter_Notes|Modul 01: Moneter]] | [[Kebijakan_Fiskal_Notes|Modul 02: Fiskal]] | [[Model_IS_LM_Notes|Modul 03: IS-LM & Policy Mix]] | [[Kebijakan_Moneter_dan_Fiskal_Drills|Active Recall Drills]]

---

## 📐 1. Kompendium Formulasi Mikrofondasi & Makro

### A. Mikrofondasi Kas & Moneter (Modul 01)
1. **Baumol-Tobin Optimal Cash Balance ($M^*$):**
   $$ M^* = \sqrt{\frac{F Y}{2 i}} \quad \text{dan} \quad N^* = \sqrt{\frac{i Y}{2 F}} $$
2. **Pengganda Uang Kompleks ($m$):**
   $$ m = \frac{1 + c}{r + e + c} \implies M^s = \left(\frac{1 + c}{r + e + c}\right) B $$
3. **Aturan Suku Bunga Taylor (*Taylor Rule*):**
   $$ i_t = r_n + \pi_t + a_\pi (\pi_t - \pi^*) + a_y (y_t - \bar{y}_t) \quad (\text{Syarat Taylor: } a_\pi > 0) $$

### B. Mikrofondasi Fiskal & Sustainabilitas (Modul 02)
1. **Pengganda Fiskal Terbuka ($K_{g,open}$):**
   $$ K_{g,open} = \frac{1}{1 - c(1-t) + m} $$
2. **Dinamika Sustainabilitas Utang (*Debt Sustainability Analysis*):**
   $$ \Delta b_t \approx (r_t - g_t) b_{t-1} - ps_t $$
   *(di mana $b_t = D/Y$, $r = \text{bunga riil}$, $g = \text{pertumbuhan GDP riil}$, $ps = \text{surplus primer/PDB}$)*

### C. Aljabar Matriks IS-LM & Teorema Cramer (Modul 03)
$$ \begin{bmatrix} 1 - c(1-t) & b \\ k & -h \end{bmatrix} \begin{bmatrix} Y \\ r \end{bmatrix} = \begin{bmatrix} A_0 \\ M^s/P \end{bmatrix} \implies \Delta = h(1-c(1-t)) + bk $$

1. **Pengganda IS-LM Nyata:**
   $$ \alpha_G = \frac{\partial Y^*}{\partial G} = \frac{h}{h(1 - c(1-t)) + bk} $$
2. **Formula Eksplisit Crowding-Out:**
   $$ \text{Loss} = \frac{bk}{(1 - c(1-t))[h(1 - c(1-t)) + bk]} \cdot \Delta G $$

---

## 🏛️ 2. Matriks Kelembagaan & Regulasi Indonesia

| Sektor | Regulasi / UU Utama | Ketentuan & Batasan Hukum |
| :--- | :--- | :--- |
| **Moneter** | UU No. 4 Tahun 2023 (UU P2SK) | Mandat BI: Stabilitas Rupiah + Stabilitas Sistem Keuangan + Dukung Pertumbuhan Ekonomi Berkelanjutan. |
| **Fiskal** | UU No. 17 Tahun 2003 | Defisit APBN Maksimal **3% dari PDB**, Rasio Utang Maksimal **60% dari PDB**. |
| **Perpajakan** | UU No. 7 Tahun 2021 (UU HPP) | Kenaikan tarif PPN (11%-12%), integrasi NIK-NPWP, Pajak Karbon. |

---

## 🌐 3. Matriks Efektivitas Kebijakan Mundell-Fleming (IS-LM-BP)

*(Kondisi Mobilitas Modal Bebas Sempurna $r = r^*$)*

| Rejim Nilai Tukar | Kebijakan Fiskal Ekspansif ($\Delta G > 0$) | Kebijakan Moneter Ekspansif ($\Delta M^s > 0$) |
| :--- | :--- | :--- |
| **Floating Rate** | **TIDAK EFEKTIF ($\Delta Y = 0$)**<br>*(Apresiasi nilai tukar menghancurkan $NX$)* | **SANGAT EFEKTIF ($\Delta Y \uparrow\uparrow$)**<br>*(Depresiasi nilai tukar mendongkrak $NX$)* |
| **Fixed Rate** | **SANGAT EFEKTIF ($\Delta Y \uparrow\uparrow$)**<br>*(BI wajib mencetak Rupiah beli valas)* | **TIDAK EFEKTIF ($\Delta Y = 0$)**<br>*(Intervensi valas menghapus ekspansi $M^s$)* |
