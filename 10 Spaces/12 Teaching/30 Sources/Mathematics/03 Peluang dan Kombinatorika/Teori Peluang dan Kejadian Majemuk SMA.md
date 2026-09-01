---
title: "Teori Peluang & Kejadian Majemuk — Peluang Bersyarat & Saling Lepas"
level: sma
target_audience: "SMA Kelas 12"
created: 2026-08-09
sources:
  - "[[Kaidah Pencacahan dan Kombinatorika SMA]]"
  - "[[Logika Permutasi dan Kombinasi SMA]]"
  - "[[Pahami Konsep, Rumus & Cara Menghitung Peluang Suatu Kejadian]]"
tags:
  - teaching-material
  - mathematics
  - peluang
  - kejadian-majemuk
  - peluang-bersyarat
  - frekuensi-harapan
---

# Teori Peluang & Kejadian Majemuk — Rahasia Angka Peluang & Kepastian! 🎯🎲

Halo temen-temen Kelas 12! Di modul sebelumnya, kita sudah belajar cara menghitung banyaknya kemungkinan menggunakan Kaidah Pencacahan (Permutasi & Kombinasi). Sekarang, saatnya kita masuk ke inti dari **Teori Peluang dan Kejadian Majemuk**.

Topik ini merupakan salah satu materi matematika yang **paling sering keluar di Ujian Sekolah maupun UTBK-SNBT**.

Di kehidupan nyata, teori peluang kepake banget lho!
- *Berapa peluang kita lolos di Jurusan A berdasarkan rasio peminat vs daya tampung?*
- *Berapa peluang dapet karakter/item SSR pas nge-pull gacha di game kesayangan?*
- *Berapa probabilitas pengambilan kelereng/kartu tanpa pengembalian dalam analisis risiko industri & asuransi?*

Di modul ini, kita bakal bedah tuntas semua konsep Teori Peluang secara **lengkap, komprehensif, santai, mudah dipahami**, dan *straight-to-the-point*! Yuk, siapkan catatan dan mari kita mulai! ☕🚀

---

## 1. Fondasi Teori Peluang, Istilah Kunci & Visualisasi Ruang Sampel

Sebelum masuk ke rumus-rumus hitungan, kita harus kenalan dulu sama istilah-istilah wajib di teori peluang serta cara memvisualisasikan ruang sampelnya!

### a. Istilah-Istilah Dasar
1. **Percobaan (Trial):** Suatu tindakan atau eksperimen yang diulang-ulang dan menghasilkan nilai yang tidak pasti, tapi kita tahu seluruh kemungkinan hasil yang bakal keluar.
   - *Contoh:* Melempar 2 buah dadu bermata 6, mengambil 1 bola dari kantong acak, atau mengambil kartu remi.
2. **Ruang Sampel ($S$) & Jumlah Anggota ($n(S)$):** Himpunan dari **semua hasil yang mungkin terjadi** dari suatu percobaan.
3. **Titik Sampel & Kejadian ($A$):** Titik sampel adalah anggota tunggal dari $S$. Kejadian ($A$) adalah himpunan bagian dari ruang sampel sesuai kondisi yang dikehendaki ($n(A)$).

---

### b. Visualisasi Ruang Sampel

#### 1. Tabel Ruang Sampel (Pelemparan 2 Dadu Bermata 6)
Ketika melempar 2 dadu sekaligus, terdapat total $n(S) = 6 \times 6 = 36$ titik sampel:

| Dadu 1 \ Dadu 2 | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | (1,1) | (1,2) | (1,3) | (1,4) | (1,5) | (1,6) |
| **2** | (2,1) | (2,2) | (2,3) | (2,4) | (2,5) | (2,6) |
| **3** | (3,1) | (3,2) | (3,3) | (3,4) | (3,5) | (3,6) |
| **4** | (4,1) | (4,2) | (4,3) | (4,4) | (4,5) | (4,6) |
| **5** | (5,1) | (5,2) | (5,3) | (5,4) | (5,5) | (5,6) |
| **6** | (6,1) | (6,2) | (6,3) | (6,4) | (6,5) | (6,6) |

#### 2. Diagram Pohon (Pelemparan 3 Koin Logam)
Pada pelemparan 3 koin (A = Angka, G = Gambar), ruang sampel terbentuk bertingkat:
- **Koin 1:** A atau G
- **Koin 2:** (A $\rightarrow$ AA, AG), (G $\rightarrow$ GA, GG)
- **Koin 3:** AAA, AAG, AGA, AGG, GAA, GAG, GGA, GGG
- **Total Ruang Sampel:** $n(S) = 2^3 = 8$.

---

## 2. Rumus Peluang Dasar, Peluang Komplemen & Frekuensi Harapan

### a. Rumus Peluang Kejadian $P(A)$
$$P(A) = \frac{n(A)}{n(S)}$$

### b. Sifat-Sifat Penting Peluang
1. **Rentang Nilai Peluang:** $0 \le P(A) \le 1$.
   - $P(A) = 0 \implies$ **Mustahil (Impossible)**.
   - $P(A) = 1 \implies$ **Pasti (Certain)**.
2. **Peluang Komplemen $P(A^c)$:** Komplemen $A$ (disimbolkan $A^c$ atau $A'$) adalah kejadian **bukan $A$**.
   $$P(A^c) = 1 - P(A)$$

#### Contoh Real Peluang Komplemen:
Kantong berisi 8 bola merah, 4 bola putih, dan 2 bola hijau ($n(S) = 14$). Diambil 1 bola secara acak. Peluang terambil bola **bukan merah**:
- Peluang Merah $P(M) = \frac{8}{14} = \frac{4}{7}$.
- Peluang Bukan Merah $P(M^c) = 1 - \frac{4}{7} = \frac{3}{7}$.

---

### c. Frekuensi Harapan ($F_h$)
Frekuensi harapan adalah perkiraan berapa kali suatu kejadian $A$ diharapkan terjadi dalam $N$ kali pengulangan percobaan.

$$F_h(A) = N \times P(A)$$

#### Contoh Real:
Terdapat 7 buah kartu bertuliskan $A, B, C, D, E, F, G$ ($n(S)=7$). Ambil 1 kartu secara acak (kartu vokal $n(A)=2$, yaitu $A$ dan $E$, sehingga $P(A) = 2/7$). Jika percobaan diulangi sebanyak 70 kali ($N=70$):
$$F_h(A) = 70 \times \frac{2}{7} = 20\text{ kali}.$$

---

## 3. Bedah Tuntas Peluang Kejadian Majemuk

Kejadian majemuk adalah penggabungan dua atau lebih kejadian sederhana.

### a. Peluang Kejadian Saling Lepas (Mutually Exclusive)
Dua kejadian $A$ dan $B$ dikatakan **saling lepas** jika $A$ dan $B$ **tidak mungkin terjadi bersamaan** ($A \cap B = \emptyset$).
Kata kunci di soal: **"ATAU"** tanpa irisan.

$$P(A \cup B) = P(A) + P(B)$$

#### Contoh Real:
Pada pelemparan 1 dadu bermata 6, berapa peluang muncul mata dadu genap ($A$) **atau** mata dadu 5 ($B$)?
- $A = \{2, 4, 6\} \implies P(A) = \frac{3}{6}$.
- $B = \{5\} \implies P(B) = \frac{1}{6}$.
- Karena $A \cap B = \emptyset$, maka $P(A \cup B) = \frac{3}{6} + \frac{1}{6} = \frac{4}{6} = \frac{2}{3}$.

---

### b. Peluang Kejadian Tidak Saling Lepas (Memiliki Irisan)
Dua kejadian $A$ dan $B$ dikatakan **tidak saling lepas** jika $A$ dan $B$ **bisa terjadi secara bersamaan** ($A \cap B \neq \emptyset$).

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

```
    Diagram Venn Kejadian Tidak Saling Lepas:
    +-----------------------------------+
    | Ruang Sampel (S)                  |
    |    /-----\     /-----\            |
    |   /       \   /       \           |
    |  |    A    |X|    B    |          |
    |   \       /   \       /           |
    |    \-----/     \-----/            |
    |             A ∩ B                 |
    +-----------------------------------+
```

#### Contoh Real (Kartu Remi):
Dari satu set kartu remi standar (52 kartu), diambil 1 kartu secara acak. Berapa peluang terambil kartu **As** ($A$) **atau** kartu berdaun **Hati** ($B$)?
- $n(S) = 52$.
- Banyak kartu As: $n(A) = 4 \implies P(A) = \frac{4}{52}$.
- Banyak kartu Hati: $n(B) = 13 \implies P(B) = \frac{13}{52}$.
- Irisan (Kartu As sekaligus Hati): $n(A \cap B) = 1 \implies P(A \cap B) = \frac{1}{52}$.
- Maka $P(A \cup B) = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}$.

---

### c. Peluang Kejadian Saling Bebas (Independent Events)
Dua kejadian $A$ dan $B$ dikatakan **saling bebas** jika terjadinya kejadian $A$ **tidak mempengaruhi** peluang terjadinya kejadian $B$.
Kata kunci di soal: **"DAN"** pada dua percobaan terpisah.

$$P(A \cap B) = P(A) \times P(B)$$

#### Contoh Real:
Sebuah koin logam dan sebuah dadu dilempar bersamaan. Berapa peluang muncul **Angka** ($A$) pada koin **dan** mata dadu **6** ($B$) pada dadu?
- Peluang Angka pada koin: $P(A) = \frac{1}{2}$.
- Peluang mata dadu 6: $P(B) = \frac{1}{6}$.
- Peluang keduanya: $P(A \cap B) = \frac{1}{2} \times \frac{1}{6} = \frac{1}{12}$.

---

### d. Peluang Kejadian Bersyarat & Pengambilan Berturut-turut Tanpa Pengembalian
Dua kejadian dikatakan **bersyarat (dependen)** jika terjadinya kejadian $A$ **mempengaruhi** peluang terjadinya kejadian $B$.

$$P(B|A) = \frac{P(A \cap B)}{P(A)} \iff P(A \cap B) = P(A) \times P(B|A)$$

> **Keterangan:** $P(B|A)$ dibaca "Peluang kejadian $B$ terjadi **dengan syarat** kejadian $A$ telah terjadi sebelumnya".

#### Contoh Real (Pengambilan Berturut-turut Tanpa Pengembalian):
Sebuah kotak berisi **6 kelereng merah** dan **4 kelereng biru** (total 10 kelereng). Diambil 2 kelereng satu per satu **tanpa pengembalian**. Berapa peluang terambil kelereng pertama **Merah** DAN kelereng kedua **Biru**?
- **Pengambilan Pertama ($M_1$):**
  Peluang terambil Merah $= P(M_1) = \frac{6}{10}$.
- **Pengambilan Kedua ($B_2$ bersyarat $M_1$ sudah terambil):**
  Karena kelereng merah pertama tidak dikembalikan, sisa kelereng di kotak $= 9$ buah (5 merah, 4 biru).
  Peluang terambil Biru $= P(B_2 | M_1) = \frac{4}{9}$.
- **Peluang Total ($M_1 \cap B_2$):**
  $$P(M_1 \cap B_2) = P(M_1) \times P(B_2 | M_1) = \frac{6}{10} \times \frac{4}{9} = \frac{24}{90} = \frac{4}{15} \approx 0,2667$$

---

## 4. Cheat Sheet & Rangkuman Quick Reference 📋

| Jenis Kejadian | Rumus Utama | Ciri Khas / Kata Kunci |
| :--- | :--- | :--- |
| **Peluang Dasar** | $P(A) = \frac{n(A)}{n(S)}$ | Kejadian tunggal dalam ruang sampel |
| **Peluang Komplemen** | $P(A^c) = 1 - P(A)$ | Kejadian **"bukan A"** |
| **Frekuensi Harapan** | $F_h(A) = N \times P(A)$ | Pengulangan percobaan sebanyak $N$ kali |
| **Peluang Saling Lepas** | $P(A \cup B) = P(A) + P(B)$ | Kata hubung **"ATAU"**, tidak ada irisan ($A \cap B = \emptyset$) |
| **Peluang Tidak Saling Lepas** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Kata hubung **"ATAU"**, ada irisan (misal: As Hati) |
| **Peluang Saling Bebas** | $P(A \cap B) = P(A) \times P(B)$ | Kata hubung **"DAN"**, 2 percobaan independen |
| **Peluang Bersyarat** | $P(A \cap B) = P(A) \times P(B\|A)$ | Kata hubung **"DAN"**, pengambilan tanpa pengembalian |

---

> *“Dalam matematika maupun kehidupan, peluang membantu kita mengambil keputusan terukur di tengah ketidakpastian!”* 💪🔥
