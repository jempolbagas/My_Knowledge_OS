---
title: "Matriks"
type: concept
subject: Mathematics
created: 2026-07-28
source:
  - "[[Mengenal Matriks Pengertian, Jenis, dan Transpose]]"
  - "[[Operasi Aljabar pada Matriks Penjumlahan, Pengurangan & Perkalian]]"
  - "[[Cara Mencari Determinan & Invers Matriks Beserta Contohnya]]"
  - "[[Types of Matrices Definition, Properties, Formulas and Examples]]"
  - "[[Matrix Operations Addition, Subtraction, Multiplication, Inverse]]"
source_hash: "8f2ad476d6c5550a3942702621047bb1"
promoted_to: []
tags:
  - concept
  - mathematics
  - matriks
---

# Matriks

## Ringkasan Konsep
**Matriks** adalah susunan sekumpulan bilangan yang diatur menurut urutan baris dan kolom serta dibatasi oleh tanda kurung biasa `( )` atau kurung siku `[ ]`. Matriks merupakan alat aljabar linier fundamental yang digunakan untuk menyajikan data tabular, menyelesaikan Sistem Persamaan Linier (SPLDV/SPLTV), enkripsi data, hingga komputasi grafis dan kecerdasan buatan.

## Anatomi & Komponen Utama
1. **Baris ($m$) & Kolom ($n$):** Baris berarah horizontal, kolom berarah vertikal.
2. **Ordo ($m \times n$):** Ukuran matriks. Terbagi menjadi matriks persegi ($m = n$), horisontal ($m < n$), dan vertikal ($m > n$).
3. **Elemen ($a_{ij}$):** Nilai bilangan di dalam matriks pada posisi baris ke-$i$ dan kolom ke-$j$.

## Kategori & Jenis Matriks Khusus
* **Bentuk & Ukuran:** Matriks Baris, Matriks Kolom, Matriks Singleton ($1 \times 1$), Matriks Persegi.
* **Elemen Diagonal:** Matriks Diagonal, Matriks Skalar (elemen diagonal bernilai sama $k$), Matriks Identitas ($I$), Matriks Nol ($O$).
* **Struktur Segitiga:** Matriks Segitiga Atas (Upper Triangular) dan Matriks Segitiga Bawah (Lower Triangular).
* **Aljabar & Sifat Khusus:**
  * **Simetris ($A^T = A$)** vs **Skew-Simetris ($A^T = -A$)**.
  * **Ortogonal:** $A \cdot A^T = I \iff A^T = A^{-1}$.
  * **Idempoten:** $A^2 = A$.
  * **Involutori:** $A^2 = I \iff A^{-1} = A$.
  * **Nilpoten:** $A^k = O$ untuk suatu $k \ge 1$.

## Sifat & Operasi Utama
* **Transpose ($A^T$):** Penukaran posisi elemen baris menjadi kolom ($a_{ij} \to a_{ji}$). Sifat: $(AB)^T = B^T A^T$.
* **Penjumlahan & Pengurangan ($A \pm B$):** Berlaku jika ordo identik. Sifat: Komutatif ($A+B = B+A$), Asosiatif, Identitas ($A+O = A$).
* **Perkalian Skalar ($k \cdot A$):** Mengalikan setiap elemen matriks $A$ dengan skalar $k$.
* **Perkalian Matriks ($A \times B$):** Berlaku jika kolom $A$ = baris $B$ ($A_{m \times p} \cdot B_{p \times n} = C_{m \times n}$). **Tidak komutatif** ($A \cdot B \neq B \cdot A$). Sifat perkalian: $(AB)C = A(BC)$, $A(B+C) = AB + AC$.
* **Determinan ($\det(A)$):** Skalar khusus matriks persegi. Sifat: $\det(AB) = \det(A)\det(B)$, $\det(A^T) = \det(A)$, $\det(A^{-1}) = 1/\det(A)$.
* **Invers ($A^{-1}$):** Kebalikan matriks sedemikian hingga $A \cdot A^{-1} = I$.
  * **Nonsingular:** $\det(A) \neq 0$ (Punya invers).
  * **Singular:** $\det(A) = 0$ (Tidak punya invers).
  * Sifat: $(AB)^{-1} = B^{-1} A^{-1}$.

## Catatan Rujukan & Keterkaitan
* Promoted from: [[Mengenal Matriks Pengertian, Jenis, dan Transpose]], [[Operasi Aljabar pada Matriks Penjumlahan, Pengurangan & Perkalian]], [[Cara Mencari Determinan & Invers Matriks Beserta Contohnya]], [[Types of Matrices Definition, Properties, Formulas and Examples]], [[Matrix Operations Addition, Subtraction, Multiplication, Inverse]]
* Berkas Ajar Terkait: [[Materi_Matriks]], [[LKPD_dan_Soal_Matriks]]
