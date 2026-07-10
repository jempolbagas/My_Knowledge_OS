---
title: "[Chem] Konsep Mol - Rangkuman"
course: ""
tags: ["chemistry", "stoichiometry", "mole-concept", "cheat-sheet"]
aliases: ["[Chem] Konsep Mol - Rangkuman"]
created: "2026-05-25"
date: "2026-05-24"
---

# 📋 Konsep Mol — Rangkuman

> Lihat [[[Chem] Konsep Mol - First Principle|📖 Penjelasan Lengkap]] untuk derivasi dan analogi detail.

---

## 🔢 Konstanta Penting

| Konstanta | Nilai |
|-----------|-------|
| Bilangan Avogadro ($L_a$) | $6{,}022 \times 10^{23}$ partikel/mol |
| Volume molar (STP: 0°C, 1 atm) | 22,4 L/mol |
| Volume molar (RTP: 25°C, 1 atm) | 24 L/mol |

---

## 📐 Tabel Rumus Utama

| Mencari | Rumus | Keterangan |
|---------|-------|------------|
| Mol dari massa | $n = \dfrac{m}{M_r}$ | Berlaku semua zat |
| Mol dari partikel | $n = \dfrac{N}{L_a}$ | Berlaku semua zat |
| Mol dari volume gas | $n = \dfrac{V}{22{,}4}$ (STP) atau $\dfrac{V}{24}$ (RTP) | **Gas saja!** |
| Massa | $m = n \times M_r$ | — |
| Jumlah partikel | $N = n \times L_a$ | Perhatikan atom vs molekul |
| Volume gas | $V = n \times 22{,}4$ (STP) atau $n \times 24$ (RTP) | **Gas saja!** |
| Fraksi mol | $X_a = \dfrac{n_a}{n_{\text{total}}}$ | $\sum X_i = 1$ |
| $M_r$ senyawa | $M_r = \sum (A_r \times \text{jumlah atom})$ | — |

---

## 🔄 Diagram Konversi

```
                ÷ Mr                            × Lₐ
    MASSA (g) ──────→ MOL (n) ──────→ PARTIKEL (N)
              ←──────       ←──────
                × Mr                            ÷ Lₐ
                              │
                              │ × 22,4 (STP) / × 24 (RTP)
                              ▼
                        VOLUME (L)
                        [gas saja!]
```

**Ingat:** Semua konversi **melewati mol** di tengah!

---

## 📝 Algoritma Rumus Empiris

1. **% komposisi** → anggap 100 g → **gram** tiap unsur
2. **Gram** ÷ $A_r$ → **mol** tiap unsur
3. **Semua mol** ÷ mol terkecil → **rasio**
4. Bulatkan ke bilangan bulat → **rumus empiris**
5. Jika diberi $M_r$: $\text{pengali} = \dfrac{M_r(\text{molekul})}{M_r(\text{empiris})}$
6. **Rumus molekul** = pengali × rumus empiris

---

## 💧 Algoritma Senyawa Hidrat

1. Massa air = massa hidrat − massa anhidrat
2. Hitung $n_{\text{anhidrat}} = \dfrac{m_{\text{anhidrat}}}{M_r(\text{anhidrat})}$
3. Hitung $n_{\text{air}} = \dfrac{m_{\text{air}}}{18}$
4. $x = \dfrac{n_{\text{air}}}{n_{\text{anhidrat}}}$
5. Tulis rumus: Senyawa·$x$H₂O

---

## ⚠️ Tips & Perangkap Umum

> [!warning] Jangan Tertukar!
> - **STP ≠ RTP**: Volume molar 22,4 L (STP) vs 24 L (RTP). Selalu cek kondisi soal!
> - **Atom ≠ Molekul**: 1 mol H₂O = $L_a$ *molekul* = $3 \times L_a$ *atom* (2H + 1O).
> - **$A_r$ ≠ $M_r$**: $A_r$ untuk atom tunggal, $M_r$ untuk senyawa/molekul.
> - **Volume hanya gas**: Jangan gunakan $V = n \times 22{,}4$ untuk zat cair/padat!

> [!tip] Trik Cepat
> - Jika angka dalam soal habis dibagi 22,4 → kemungkinan soal STP.
> - Fraksi mol selalu antara 0 dan 1, dan total semua fraksi = 1 (gunakan sebagai cek jawaban).
> - Dalam rumus empiris, jika rasio menghasilkan 1,5 → kalikan semua dengan 2; jika 1,33 → kalikan dengan 3.
> - Pemanasan hidrat **harus sempurna**. Jika tidak, massa air terhitung **kurang** → $x$ terlalu **kecil**.

---

**🔗 Navigasi:** [[[Chem] Konsep Mol - First Principle|📖 Penjelasan Lengkap]] · [[[Chem] Worksheet - Konsep Mol|📝 Latihan Soal]] · [[[Chem] Kunci Jawaban - Konsep Mol|🔑 Kunci Jawaban]]
