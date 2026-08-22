---
title: "Teorema Vieta pada Polinomial"
type: materi
subject: Mathematics
level: sma
target_audience: "SMA Kelas 11"
created: 2026-08-20
sources:
  - "[[Suku Banyak Polinomial SMA]]"
tags:
  - teaching-material
  - mathematics
  - suku-banyak
  - polinomial
  - teorema-vieta
---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | [[Pemfaktoran_dan_Akar_Rasional_SMA|⬅️ Pemfaktoran Polinomial]] | Modul Ini | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]

# Teorema Vieta: Rahasia Hubungan Antar Akar 🔗

Masih ingat rumus jumlah dan hasil kali akar PK (Persamaan Kuadrat) $ax^2 + bx + c = 0$ di SMP/Kelas 10?
* $x_1 + x_2 = -\frac{b}{a}$
* $x_1 \cdot x_2 = \frac{c}{a}$

Ternyata, rumus ini memiliki pola ekstensi yang berlaku untuk polinomial pangkat berapapun! Pola ini ditemukan oleh matematikawan Prancis, **François Viète** (Vieta). 

Teorema Vieta adalah kunci utama untuk menjawab soal-soal HOTS polinomial tingkat tinggi (Olimpiade, UTBK/SNBT, dll) yang mana kita dituntut mencari sifat akar tanpa harus mencari nilai akar-akarnya satu per satu secara spesifik.

---

## 1. Teorema Vieta untuk Persamaan Kubik (Pangkat 3)

Bentuk umum: $ax^3 + bx^2 + cx + d = 0$. Misalkan memiliki akar-akar $x_1, x_2, x_3$.

Maka berlaku:
1. **Jumlah 1 akar:** $x_1 + x_2 + x_3 = -\frac{b}{a}$
2. **Jumlah hasil kali 2 akar:** $x_1x_2 + x_1x_3 + x_2x_3 = \frac{c}{a}$
3. **Hasil kali ke-3 akar:** $x_1 \cdot x_2 \cdot x_3 = -\frac{d}{a}$

*(Perhatikan pola tandanya selalu bergantian: Minus - Plus - Minus - Plus...)*

---

## 2. Teorema Vieta untuk Persamaan Kuartik (Pangkat 4)

Bentuk umum: $ax^4 + bx^3 + cx^2 + dx + e = 0$. Misalkan akar-akarnya $x_1, x_2, x_3, x_4$.

Pola yang sama berlanjut:
1. **Jumlah 1 akar:** $x_1 + x_2 + x_3 + x_4 = -\frac{b}{a}$
2. **Jumlah hasil kali 2 akar:** $x_1x_2 + x_1x_3 + \dots + x_3x_4 = \frac{c}{a}$
3. **Jumlah hasil kali 3 akar:** $x_1x_2x_3 + x_1x_2x_4 + x_1x_3x_4 + x_2x_3x_4 = -\frac{d}{a}$
4. **Hasil kali ke-4 akar:** $x_1 \cdot x_2 \cdot x_3 \cdot x_4 = \frac{e}{a}$

---

## 3. Aplikasi Soal HOTS Teorema Vieta

Variasi soal yang paling sering muncul adalah mengkombinasikan Teorema Vieta dengan barisan bilangan (Aritmatika/Geometri) atau manipulasi aljabar.

### 📝 Contoh Soal 1: Manipulasi Aljabar Dasar
Diketahui $x_1, x_2,$ dan $x_3$ adalah akar-akar dari persamaan $x^3 - 3x^2 - 10x + 24 = 0$.
Tentukan nilai dari $\frac{1}{x_1} + \frac{1}{x_2} + \frac{1}{x_3}$!

**Penyelesaian:**
Dari persamaan $x^3 - 3x^2 - 10x + 24 = 0$, kita identifikasi:
$a = 1$, $b = -3$, $c = -10$, $d = 24$.

Kita diminta mencari nilai $\frac{1}{x_1} + \frac{1}{x_2} + \frac{1}{x_3}$. Samakan penyebutnya:
$$\frac{1}{x_1} + \frac{1}{x_2} + \frac{1}{x_3} = \frac{x_2x_3 + x_1x_3 + x_1x_2}{x_1x_2x_3}$$

Perhatikan bahwa ini tepat sama dengan pembagian antara rumus Vieta ke-2 dengan rumus Vieta ke-3!
* Pembilang (Rumus ke-2): $\frac{c}{a} = \frac{-10}{1} = -10$
* Penyebut (Rumus ke-3): $-\frac{d}{a} = -\frac{24}{1} = -24$

Maka nilainya adalah:
$$\frac{-10}{-24} = \mathbf{\frac{5}{12}}$$

*(Bayangkan betapa repotnya jika kita harus memfaktorkan dan mencari $x_1, x_2, x_3$ satu per satu dulu!)*

---

### 📝 Contoh Soal 2: Kombinasi Barisan Aritmatika (Super HOTS)
Akar-akar persamaan kubik $x^3 - 9x^2 + 26x - 24 = 0$ membentuk barisan aritmatika. Tentukan nilai akar-akar tersebut!

**Penyelesaian:**
1. Karena 3 akar membentuk barisan aritmatika, kita bisa memisalkan akar-akar tersebut dengan:
   * $x_1 = p - b$
   * $x_2 = p$
   * $x_3 = p + b$
   *(Di mana $p$ adalah suku tengah, dan $b$ adalah beda barisan)*.
2. Gunakan rumus Vieta pertama (Jumlah Akar):
   $$x_1 + x_2 + x_3 = -\frac{b}{a}$$
   $$(p - b) + p + (p + b) = -\frac{-9}{1}$$
   $$3p = 9 \implies \mathbf{p = 3}$$
   *Wah, kita langsung mendapatkan salah satu akarnya, yaitu $x_2 = 3$!*
3. Karena kita sudah tahu satu akar ($x = 3$), kita bisa menggunakan **Skema Horner** pada persamaan awal dengan pembagi $k = 3$:
   ```text
    3 |  1   -9   26   -24
      |       3  -18    24
      -------------------- +
         1   -6    8 |   0   (Terbukti sisa 0)
   ```
4. Hasil baginya adalah $x^2 - 6x + 8 = 0$.
   Faktorkan: $(x - 2)(x - 4) = 0 \implies x = 2$ dan $x = 4$.
5. **Kesimpulan:** Akar-akar tersebut adalah **$2, 3,$ dan $4$**. Memang benar mereka membentuk barisan aritmatika dengan beda 1.

Sangat cerdas dan elegan bukan?

---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | [[Pemfaktoran_dan_Akar_Rasional_SMA|⬅️ Pemfaktoran Polinomial]] | Modul Ini | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]
