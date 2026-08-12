---
title: "Materi Ajar Santai: Menaklukkan Persamaan Kuadrat Tanpa Pusing"
level: smp
target_audience: "SMP Kelas 9 / SMA Kelas 10"
created: 2026-07-28
sources:
  - "[[3 Cara Mudah Menyelesaikan Persamaan Kuadrat]]"
tags:
  - teaching-material
  - mathematics
  - persamaan-kuadrat
---

# Menaklukkan Persamaan Kuadrat: Dari Konsep Sampai Trik Cepat! 🚀

Halo teman-teman! Matematika sering kali kelihatan menakutkan karena penuh dengan simbol dan huruf yang misterius. Tapi tenang aja, di modul ini kita bakal bedah salah satu topik paling penting di matematika yaitu **Persamaan Kuadrat** dengan bahasa santai, kasual, dan langsung ke intinya!

---

## 1. Kenalan dengan Persamaan Kuadrat

### Apa sih Persamaan Kuadrat itu?
Sederhananya, **Persamaan Kuadrat** adalah persamaan matematika yang variabelnya memiliki **pangkat tertinggi yaitu 2**. 

Ingat kata kuncinya: **pangkat tertinggi dua**! 
* Kalau pangkat tertingginya 1 (misal $2x + 3 = 0$), itu namanya persamaan linier.
* Kalau pangkat tertingginya 3 (misal $x^3 - 2x = 0$), itu namanya persamaan kubik.
* Nah, kalau ada $x^2$ dan nggak ada pangkat yang lebih tinggi dari 2, selamat! Kamu sedang berhadapan dengan **Persamaan Kuadrat**.

---

## 2. Anatomi Bentuk Umum

Bentuk umum dari persamaan kuadrat bisa kita tuliskan seperti ini:

$$ax^2 + bx + c = 0$$

Syarat mutlak: $a, b, c$ adalah bilangan real dan **$a \neq 0$**.

Mari kita bedah satu per satu "anggota tubuh" dari persamaan ini:
* **$x$** = **Variabel** (si angka misterius yang nilainya belum kita ketahui dan ingin kita cari).
* **$a$** = **Koefisien dari $x^2$** (angka yang nempel di depan $x^2$). Kenapa $a$ tidak boleh 0? Karena kalau $a = 0$, suku $0 \cdot x^2$ bakal hilang, dan persamaannya berubah jadi $bx + c = 0$ (linier biasa, bukan kuadrat lagi!).
* **$b$** = **Koefisien dari $x$** (angka yang nempel di depan $x$).
* **$c$** = **Konstanta** (angka jomblo yang berdiri sendiri tanpa variabel $x$).

> **Contoh Cepat:**
> Pada persamaan $2x^2 - 5x + 3 = 0$:
> * Nilai $a = 2$
> * Nilai $b = -5$ *(ingat, tanda minusnya diikutkan ya!)*
> * Nilai $c = 3$

---

## 3. Misi Utama: Menyelesaikan Persamaan Kuadrat

Mungkin kamu bertanya: *"Kenapa sih persamaan kuadrat harus diselesaikan? Emang dia punya masalah apa?"* 😄

Masalah utamanya adalah kita **belum tahu berapa nilai $x$** yang kalau dimasukkan ke dalam persamaan tersebut bakal membuat ruas kiri nilainya sama dengan ruas kanan (yaitu sama dengan $0$).

Nilai $x$ yang memenuhi persamaan ini disebut sebagai **Akar-akar Persamaan Kuadrat** atau **Penyelesaian**. Biasanya persamaan kuadrat punya 2 nilai akar, kita sebut saja $x_1$ dan $x_2$.

Ada **3 Jurus Utama** untuk mencari nilai $x$ tersebut. Yuk kita bahas satu per satu!

---

## 4. 3 Jurus Pamungkas Menyelesaikan Persamaan Kuadrat

---

### 🗡️ Jurus 1: Pemfaktoran (Faktorisasi)

**Prinsip dasar:** Mengubah bentuk penjumlahan $ax^2 + bx + c = 0$ menjadi bentuk perkalian dua buah faktor $(px + q)(rx + s) = 0$. 

Kenapa? Karena kalau $A \times B = 0$, maka dipastikan $A = 0$ atau $B = 0$!

#### Bentuk-bentuk Umum Pemfaktoran:
1. **Selisih Dua Kuadrat:** $x^2 - y^2 = (x + y)(x - y)$
2. **Kuadrat Sempurna Positif:** $x^2 + 2xy + y^2 = (x + y)^2$
3. **Kuadrat Sempurna Negatif:** $x^2 - 2xy + y^2 = (x - y)^2$

#### Langkah Pemfaktoran untuk $ax^2 + bx + c = 0$:
Cari dua buah angka, sebut saja $p$ dan $q$, yang memenuhi dua syarat:
1. **$p \times q = a \times c$**
2. **$p + q = b$**

#### Contoh Soal Pemfaktoran:
Selesaikan persamaan kuadrat: $5x^2 + 13x + 6 = 0$

**Langkah Penyelesaian:**
1. Identifikasi $a = 5$, $b = 13$, $c = 6$.
2. Hitung $a \times c = 5 \times 6 = 30$.
3. Cari dua angka yang kalau dikali dapat $30$ dan kalau dijumlah dapat $13$. Angka tersebut adalah **$10$** dan **$3$** ($10 \times 3 = 30$ dan $10 + 3 = 13$).
4. Pecah suku tengah ($13x$) menjadi $10x + 3x$:
   $$5x^2 + 10x + 3x + 6 = 0$$
5. Kelompokkan dan keluarkan faktor persekutuan:
   $$5x(x + 2) + 3(x + 2) = 0$$
6. Karena kedua suku punya $(x + 2)$, keluarkan $(x + 2)$-nya:
   $$(5x + 3)(x + 2) = 0$$
7. Cari nilai $x$:
   * $5x + 3 = 0 \implies 5x = -3 \implies x_1 = -\frac{3}{5}$
   * $x + 2 = 0 \implies x_2 = -2$

**Jadi, penyelesaiannya adalah $x = -\frac{3}{5}$ atau $x = -2$.**

---

### 🛡️ Jurus 2: Melengkapi Kuadrat Sempurna

**Prinsip dasar:** Mengubah persamaan kuadrat menjadi bentuk $(x + p)^2 = q$, sehingga kita tinggal menarik akar kuadrat di kedua ruas ($x + p = \pm \sqrt{q}$).

#### Resep Rahasia Melengkapi Kuadrat:
1. Pastikan koefisien $x^2$ bernilai $1$ ($a = 1$). Jika belum $1$, bagilah seluruh ruas dengan $a$.
2. Pindahkan konstanta $c$ ke ruas kanan.
3. Tambahkan kedua ruas dengan kuadrat dari setengah koefisien $x$, yaitu $\left(\frac{b}{2}\right)^2$.

#### Contoh Soal Kuadrat Sempurna:
Selesaikan persamaan: $x^2 + 6x + 5 = 0$

**Langkah Penyelesaian:**
1. Koefisien $a$ sudah $1$. Pindahkan konstanta $+5$ ke ruas kanan:
   $$x^2 + 6x = -5$$
2. Hitung penambahnya: Setengah dari $b=6$ adalah $3$. Kuadratnya adalah $3^2 = 9$.
3. Tambahkan angka $9$ di ruas kiri dan ruas kanan:
   $$x^2 + 6x + 9 = -5 + 9$$
   $$x^2 + 6x + 9 = 4$$
4. Ruas kiri sekarang sudah menjadi kuadrat sempurna $(x + 3)^2$:
   $$(x + 3)^2 = 4$$
5. Tarik akar di kedua ruas:
   $$x + 3 = \pm \sqrt{4}$$
   $$x + 3 = \pm 2$$
6. Hitung kedua nilai $x$:
   * Untuk $+2$: $x + 3 = 2 \implies x = 2 - 3 \implies x_1 = -1$
   * Untuk $-2$: $x + 3 = -2 \implies x = -2 - 3 \implies x_2 = -5$

**Jadi, penyelesaiannya adalah $x = -1$ atau $x = -5$.**

---

### ⚔️ Jurus 3: Rumus Kuadratik (Rumus ABC)

**Prinsip dasar:** Ini adalah "senjata pamungkas" atau "sapu bersih". Mau persamaannya mudah atau sulit dipfaktorkan, rumus ABC **pasti bisa** menyelesaikannya!

#### Rumus ABC:

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

#### Mengenal Diskriminan ($D$):
Bagian di dalam akar, yaitu **$D = b^2 - 4ac$**, disebut **Diskriminan**. $D$ menentukan sifat akar-akar persamaan kuadrat:
* **$D > 0$**: Memiliki **2 akar real yang berbeda**.
* **$D = 0$**: Memiliki **2 akar real yang sama (kembar)**.
* **$D < 0$**: Tidak memiliki akar real (akarnya berupa **bilangan imajiner/kompleks**).

#### Contoh Soal Rumus ABC:
Selesaikan persamaan: $x^2 + 4x - 12 = 0$

**Langkah Penyelesaian:**
1. Tentukan nilai $a = 1$, $b = 4$, $c = -12$.
2. Masukkan ke dalam rumus ABC:
   $$x_{1,2} = \frac{-(4) \pm \sqrt{(4)^2 - 4(1)(-12)}}{2(1)}$$
   $$x_{1,2} = \frac{-4 \pm \sqrt{16 + 48}}{2}$$
   $$x_{1,2} = \frac{-4 \pm \sqrt{64}}{2}$$
   $$x_{1,2} = \frac{-4 \pm 8}{2}$$
3. Hitung $x_1$ dan $x_2$:
   * $x_1 = \frac{-4 + 8}{2} = \frac{4}{2} = 2$
   * $x_2 = \frac{-4 - 8}{2} = \frac{-12}{2} = -6$

**Jadi, penyelesaiannya adalah $x = 2$ atau $x = -6$.**

---

## 5. Cheatsheet: Pakai Jurus Yang Mana?

Biar lebih efisien pas ngerjain soal, ini panduan milih jurusnya:

| Kondisi Soal | Jurus Terbaik | Alasan |
| :--- | :--- | :--- |
| Angkanya bagus & gampang dicari faktornya | **Pemfaktoran** | Paling cepat & hemat waktu! |
| Koefisien $a = 1$ dan $b$ bernilai genap | **Melengkapi Kuadrat** | Hitungannya simpel tanpa pecahan. |
| Angkanya rumit/sulit difaktorkan | **Rumus ABC** | Dijamin selalu dapet jawabannya! |

---

## 6. Ringkasan Singkat

1. **Bentuk umum:** $ax^2 + bx + c = 0$ dengan $a \neq 0$.
2. Menyelesaikan persamaan kuadrat artinya mencari nilai $x$ (akar-akar).
3. 3 metode penyelesaian: **Pemfaktoran**, **Kuadrat Sempurna**, dan **Rumus ABC**.
4. Diskriminan $D = b^2 - 4ac$ menentukan jenis akar yang dihasilkan.

Tetap semangat berlatih! Semakin sering kamu coba, makin makin cepat kamu nemuin nilai $x$-nya! 🎯


---

## 📝 Lembar Kerja & Soal Evaluasi Terkait
- [[LKPD_Persamaan_Kuadrat_SMP]]
- [[index_teaching|🍎 Teaching Resources Hub]]
