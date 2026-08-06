---
type: concept
subject: Mathematics
source_hash: "8701f36defe0f8bd6df6a463e94ff6c1"
source: "[[Chinese_Remainder_Theorem_and_Reverse_CRT_Guide]]"
created: 2026-08-06
---

# Reverse CRT (Reverse Chinese Remainder Theorem)

**Reverse CRT (RCRT)** adalah proses dekomposisi atau pemecahan sebuah nilai skalar/rahasia $I$ menjadi himpunan sisa bagi (residue/primary shares) $r_i$ terhadap sejumlah basis modulo $\{P_1, P_2, \dots, P_n\}$ yang bersifat pairwise [[Coprime]]:

$$r_i = I \bmod P_i \quad \text{untuk } i = 1, 2, \dots, n$$

Dalam aljabar aljabar/teori bilangan, RCRT merepresentasikan pemetaan dari domain tunggal modulo $M$ ke domain produk Cartesian pecahan modulo:
$$I \pmod M \mapsto (r_1 \bmod P_1, r_2 \bmod P_2, \dots, r_n \bmod P_n)$$
di mana $M = \prod_{i=1}^{n} P_i$.

## Perbandingan dengan Reconstruction CRT
- **Reverse CRT (RCRT):** Proses pembagian/ekstraksi sisa bagi $I \to (r_1, r_2, \dots, r_n)$.
- **[[Chinese_Remainder_Theorem]] (Reconstruction):** Menggabungkan kembali pecahan $(r_1, r_2, \dots, r_n)$ menjadi nilai asli $I \pmod M$ dengan formula:
  $$I = \left( \sum_{i=1}^{n} r_i \cdot m_i \cdot m_i^{-1} \right) \bmod M$$
  dengan $m_i = \frac{M}{P_i}$ dan $m_i^{-1}$ sebagai [[Invers_Modular]] dari $m_i \pmod{P_i}$.

## Aplikasi Utama
1. **Secret Sharing Scheme (SSS):** Memecah piksel gambar rahasia atau data rahasia menjadi komponen sisa bagi tanpa kehilangan presisi (*lossless*).
2. **Residue Number System (RNS):** Digunakan dalam komputasi paralel hardware untuk mempercepat operasi aritmatika pada angka besar dengan mengoperasikan pecahan sisa bagi independen.
3. **Kriptografi Asimetris:** Mempercepat enkripsi/dekripsi RSA.

## Konsep Terkait
- [[Chinese_Remainder_Theorem]]
- [[Coprime]]
- [[Kongruensi_Modular]]
- [[Invers_Modular]]
