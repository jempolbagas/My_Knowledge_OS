---
type: concept
title: Coprime
subject: Mathematics
created: 2026-08-05
source: "[[Chinese Remainder Theorem]]"
---

# Coprime (Relatif Prima)

**Coprime** (atau **Relatif Prima / Saling Prima**) adalah hubungan antara dua atau lebih bilangan bulat yang memiliki Faktor Persekutuan Terbesar (FPB / *Greatest Common Divisor*) sama dengan 1.

$$\gcd(a, b) = 1$$

Artinya, tidak ada bilangan bulat selain 1 yang dapat membagi habis $a$ dan $b$ secara bersamaan.

## Ciri Utama & Miskonsepsi

- **Tidak Harus Bilangan Prima:** Pasangan bilangan yang *coprime* tidak mensyaratkan anggotanya berupa bilangan prima.
  - *Contoh:* Pasangan $(8, 9)$. Angka 8 (komposit) dan 9 (komposit) adalah *coprime* karena $\gcd(8, 9) = 1$.
- **Setiap Dua Bilangan Prima Berbeda Pasti Coprime:** Untuk bilangan prima $p$ dan $q$ ($p \neq q$), $\gcd(p, q) = 1$.

## Contoh Pasangan

| Pasangan | FPB / $\gcd$ | Status |
| :--- | :--- | :--- |
| $(14, 15)$ | $\gcd(14, 15) = 1$ | **Coprime** |
| $(5, 7)$ | $\gcd(5, 7) = 1$ | **Coprime** |
| $(6, 9)$ | $\gcd(6, 9) = 3$ | **Bukan Coprime** |
| $(12, 18)$ | $\gcd(12, 18) = 6$ | **Bukan Coprime** |

## Peran dalam Teori Bilangan & Kriptografi

- **[[Chinese Remainder Theorem]]:** CRT mewajibkan himpunan modulo $\{p_1, p_2, \dots, p_n\}$ bersifat *pairwise coprime* ($\gcd(p_i, p_j) = 1$ untuk $i \neq j$) agar keunikan solusi $x \pmod M$ terjamin.
- **[[Kongruensi Modular]] & Invers Modular:** Invers multiplikatif $a^{-1} \pmod m$ hanya ada jika dan hanya jika $\gcd(a, m) = 1$.

## Konsep Terkait
- [[Chinese Remainder Theorem]]
- [[Kongruensi Modular]]
