---
type: concept
title: "Suku Banyak (Polinomial)"
subject: "Mathematics"
date_created: 2026-07-28
tags:
  - concept
  - mathematics
  - algebra
  - polynomial
source: "[[Materi Suku Banyak Polinomial]]"
source_hash: "8fc3435a6aa003239e7dbf0fa74c32dd"
---

## The idea (one clear statement)
Suku banyak (polinomial) adalah bentuk aljabar penjumlahan/pengurangan suku-suku berderajat variabel berupa bilangan bulat non-negatif ($n \in \mathbb{N}_0$) yang nilainya dapat dievaluasi dan dibagi secara efisien menggunakan skema sintetik Metode Horner dan Metode Horner-Kino.

## Why it matters / how it connects
Polinomial merupakan fondasi dasar aljabar tinggi, pemodelan kurva, kalkulus (turunan dan integral aljabar), serta penyelesaian persamaan derajat tinggi. Memahami evaluasi nilai dan pembagian polinomial memungkinkan penentuan akar-akar rasional via Teorema Faktor serta penyederhanaan fungsi rasional.

## Key Properties & Horner Methods
- **Bentuk Umum:** $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ dengan koefisien $a_n \neq 0$ dan derajat $n$.
- **Syarat Wajib:** Pangkat variabel harus bilangan cacah (0, 1, 2, ...), variabel tidak di penyebut atau di dalam tanda akar.
- **Metode Horner Standar:** Mengubah perkalian berpangkat tinggi menjadi operasi perkalian-penjumlahan skema beruntun untuk pembagi $(x - k)$ dan $(ax + b)$.
- **Metode Horner-Kino:** Modifikasi skema Horner 3-baris dengan pembanding $k_1 = -c/a$ dan $k_2 = -b/a$ untuk membagi polinomial dengan pembagi kuadrat $ax^2 + bx + c$ tanpa perlu memfaktorkan.
- **Teorema Sisa & Faktor:** $S = P(k)$, dan $(x - k)$ adalah faktor jika dan hanya jika $S = P(k) = 0$.

## Related concepts
- [[Materi Suku Banyak Polinomial]]
- [[LKPD dan Soal Suku Banyak Polinomial]]
- [[Persamaan Kuadrat]]
