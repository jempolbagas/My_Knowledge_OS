---
title: "Simulasi Ujian Mandiri: Relasi Rekursif"
course: Discrete Mathematics I
tags: ["discrete-mathematics", "recurrence-relations", "mock-exam"]
aliases: ["Recurrence Relations Mock Exam", "Simulasi Ujian Relasi Rekursif"]
created: "2026-06-21"
---

# Simulasi Ujian Mandiri: Relasi Rekursif

**Waktu:** 90 Menit

## Soal Ujian

1. Selesaikan relasi rekursif berikut dengan menggunakan metode iterasi (unrolling):
   $$a_n = a_{n-1} + 3n - 2 \quad \text{untuk } n \geq 1$$
   dengan kondisi awal $a_0 = 4$.

2. Tentukan solusi dari relasi rekursif linier homogen berikut:
   $$a_n = 5a_{n-1} - 4a_{n-2} \quad \text{untuk } n \geq 2$$
   dengan kondisi awal $a_0 = 3$ dan $a_1 = 9$.

3. Tentukan solusi dari relasi rekursif linier homogen berikut:
   $$a_n = 6a_{n-1} - 9a_{n-2} \quad \text{untuk } n \geq 2$$
   dengan kondisi awal $a_0 = 2$ dan $a_1 = 12$.

4. Selesaikan relasi rekursif non-homogen berikut dengan menggunakan metode fungsi pembangkit biasa (ordinary generating function):
   $$a_n = 2a_{n-1} + 3^n \quad \text{untuk } n \geq 1$$
   dengan kondisi awal $a_0 = 1$.

5. Tentukan relasi rekursif beserta kondisi awal untuk menghitung jumlah barisan biner (binary strings) dengan panjang $n$ yang tidak mengandung dua angka '0' berturut-turut. Kemudian, tentukan formula eksplisit untuk suku ke-$n$ dari relasi tersebut.

---

## Kunci Jawaban & Pembahasan

### Solusi Soal 1

Diberikan relasi rekursif:
$$a_n = a_{n-1} + 3n - 2 \quad \text{untuk } n \geq 1$$
dengan kondisi awal $a_0 = 4$.

Lakukan ekspansi (unrolling) terhadap persamaan tersebut secara bertahap:
$$\begin{aligned}
a_n &= a_{n-1} + (3n - 2) \\
a_n &= [a_{n-2} + 3(n-1) - 2] + (3n - 2) \\
    &= a_{n-2} + 3(n + (n-1)) - 2(2) \\
a_n &= [a_{n-3} + 3(n-2) - 2] + 3(n + (n-1)) - 2(2) \\
    &= a_{n-3} + 3(n + (n-1) + (n-2)) - 2(3)
\end{aligned}$$

Berdasarkan pola yang terbentuk, setelah dilakukan ekspansi sebanyak $k$ langkah, diperoleh bentuk umum:
$$a_n = a_{n-k} + 3 \sum_{i=0}^{k-1} (n - i) - 2k$$

Proses ekspansi dihentikan ketika mencapai kondisi awal, yaitu saat indeks mencapai $0$. Hal ini terjadi ketika $n - k = 0 \implies k = n$. 
Substitusikan nilai $k = n$ ke dalam persamaan umum:
$$a_n = a_0 + 3 \sum_{i=0}^{n-1} (n - i) - 2n$$

Perhatikan bahwa deret $\sum_{i=0}^{n-1} (n - i)$ adalah penjumlahan deret bilangan bulat positif dari $1$ hingga $n$:
$$\sum_{i=0}^{n-1} (n - i) = n + (n-1) + (n-2) + \dots + 1 = \sum_{j=1}^n j = \frac{n(n+1)}{2}$$

Substitusikan nilai $a_0 = 4$ dan rumus jumlah deret tersebut ke dalam persamaan $a_n$:
$$\begin{aligned}
a_n &= 4 + 3 \left( \frac{n(n+1)}{2} \right) - 2n \\
    &= 4 + \frac{3n^2 + 3n}{2} - \frac{4n}{2} \\
    &= \frac{8 + 3n^2 - n}{2} \\
    &= \frac{3n^2 - n + 8}{2}
\end{aligned}$$

Jadi, solusi closed-form dari relasi rekursif tersebut adalah:
$$a_n = \frac{3n^2 - n + 8}{2} \quad \text{untuk } n \geq 0$$

---

### Solusi Soal 2

Diberikan relasi rekursif linier homogen:
$$a_n = 5a_{n-1} - 4a_{n-2} \quad \text{untuk } n \geq 2$$
dengan kondisi awal $a_0 = 3$ dan $a_1 = 9$.

Asumsikan solusi berbentuk $a_n = r^n$ dengan $r \neq 0$. Substitusikan asumsi tersebut ke dalam persamaan relasi rekursif:
$$r^n = 5r^{n-1} - 4r^{n-2}$$

Bagi kedua ruas dengan $r^{n-2}$ untuk memperoleh persamaan karakteristik:
$$r^2 - 5r + 4 = 0$$

Faktorkan persamaan kuadrat tersebut:
$$(r - 4)(r - 1) = 0$$

Diperoleh akar-akar karakteristik yang real dan berbeda:
$$r_1 = 4 \quad \text{dan} \quad r_2 = 1$$

Oleh karena itu, bentuk solusi umum dari relasi rekursif tersebut adalah:
$$a_n = \alpha_1 (4)^n + \alpha_2 (1)^n = \alpha_1 4^n + \alpha_2$$

Terapkan kondisi awal untuk menentukan nilai konstanta $\alpha_1$ dan $\alpha_2$:
1. Untuk $n = 0$:
   $$a_0 = \alpha_1 4^0 + \alpha_2 = 3 \implies \alpha_1 + \alpha_2 = 3 \quad \text{--- (Persamaan i)}$$
2. Untuk $n = 1$:
   $$a_1 = \alpha_1 4^1 + \alpha_2 = 9 \implies 4\alpha_1 + \alpha_2 = 9 \quad \text{--- (Persamaan ii)}$$

Kurangkan Persamaan (ii) dengan Persamaan (i):
$$(4\alpha_1 + \alpha_2) - (\alpha_1 + \alpha_2) = 9 - 3$$
$$3\alpha_1 = 6 \implies \alpha_1 = 2$$

Substitusikan nilai $\alpha_1 = 2$ ke dalam Persamaan (i):
$$2 + \alpha_2 = 3 \implies \alpha_2 = 1$$

Jadi, solusi eksplisit dari relasi rekursif tersebut adalah:
$$a_n = 2 \cdot 4^n + 1 \quad \text{untuk } n \geq 0$$

---

### Solusi Soal 3

Diberikan relasi rekursif linier homogen:
$$a_n = 6a_{n-1} - 9a_{n-2} \quad \text{untuk } n \geq 2$$
dengan kondisi awal $a_0 = 2$ dan $a_1 = 12$.

Asumsikan solusi berbentuk $a_n = r^n$ dengan $r \neq 0$. Dengan membagi persamaan dengan $r^{n-2}$, diperoleh persamaan karakteristik:
$$r^2 - 6r + 9 = 0$$

Faktorkan persamaan kuadrat tersebut:
$$(r - 3)^2 = 0$$

Diperoleh akar karakteristik kembar (repeated root):
$$r_1 = r_2 = 3$$

Karena akar karakteristik bernilai kembar, bentuk solusi umum dari relasi rekursif tersebut adalah:
$$a_n = \alpha_1 3^n + \alpha_2 n 3^n = (\alpha_1 + \alpha_2 n)3^n$$

Terapkan kondisi awal untuk menentukan nilai konstanta $\alpha_1$ dan $\alpha_2$:
1. Untuk $n = 0$:
   $$a_0 = (\alpha_1 + \alpha_2 \cdot 0)3^0 = 2 \implies \alpha_1 = 2$$
2. Untuk $n = 1$:
   $$a_1 = (\alpha_1 + \alpha_2 \cdot 1)3^1 = 12$$
   $$(\alpha_1 + \alpha_2) \cdot 3 = 12 \implies \alpha_1 + \alpha_2 = 4$$

Substitusikan nilai $\alpha_1 = 2$ ke dalam persamaan di atas:
$$2 + \alpha_2 = 4 \implies \alpha_2 = 2$$

Jadi, solusi eksplisit dari relasi rekursif tersebut adalah:
$$a_n = (2 + 2n)3^n = 2(n + 1)3^n \quad \text{untuk } n \geq 0$$

---

### Solusi Soal 4

Diberikan relasi rekursif non-homogen:
$$a_n = 2a_{n-1} + 3^n \quad \text{untuk } n \geq 1$$
dengan kondisi awal $a_0 = 1$.

Definisikan fungsi pembangkit biasa (ordinary generating function) $G(x)$ untuk barisan $\{a_n\}$ sebagai berikut:
$$G(x) = \sum_{n=0}^\infty a_n x^n$$

Kalikan persamaan relasi rekursif dengan $x^n$ kemudian lakukan penjumlahan untuk seluruh $n \geq 1$:
$$\sum_{n=1}^\infty a_n x^n = \sum_{n=1}^\infty (2a_{n-1} + 3^n)x^n$$
$$\sum_{n=1}^\infty a_n x^n = 2 \sum_{n=1}^\infty a_{n-1} x^n + \sum_{n=1}^\infty 3^n x^n \quad \text{--- (Persamaan i)}$$

Representasikan setiap bagian penjumlahan dalam bentuk fungsi $G(x)$:
1. Ruas kiri Persamaan (i):
   $$\sum_{n=1}^\infty a_n x^n = G(x) - a_0 = G(x) - 1$$
2. Suku pertama pada ruas kanan Persamaan (i):
   $$2 \sum_{n=1}^\infty a_{n-1} x^n = 2x \sum_{n=1}^\infty a_{n-1} x^{n-1} = 2x G(x)$$
3. Suku kedua pada ruas kanan Persamaan (i) merupakan deret geometri:
   $$\sum_{n=1}^\infty 3^n x^n = \sum_{n=1}^\infty (3x)^n = \frac{3x}{1 - 3x}$$

Substitusikan ketiga representasi tersebut kembali ke dalam Persamaan (i):
$$G(x) - 1 = 2x G(x) + \frac{3x}{1 - 3x}$$

Selesaikan persamaan aljabar tersebut untuk memperoleh bentuk eksplisit dari $G(x)$:
$$G(x)(1 - 2x) = 1 + \frac{3x}{1 - 3x}$$
$$G(x)(1 - 2x) = \frac{(1 - 3x) + 3x}{1 - 3x}$$
$$G(x)(1 - 2x) = \frac{1}{1 - 3x}$$
$$G(x) = \frac{1}{(1 - 2x)(1 - 3x)}$$

Lakukan dekomposisi pecahan parsial terhadap $G(x)$:
$$\frac{1}{(1 - 2x)(1 - 3x)} = \frac{A}{1 - 2x} + \frac{B}{1 - 3x}$$
$$1 = A(1 - 3x) + B(1 - 2x)$$

Untuk menentukan nilai $A$, substitusikan $x = \frac{1}{2}$:
$$1 = A\left(1 - \frac{3}{2}\right) = A\left(-\frac{1}{2}\right) \implies A = -2$$

Untuk menentukan nilai $B$, substitusikan $x = \frac{1}{3}$:
$$1 = B\left(1 - \frac{2}{3}\right) = B\left(\frac{1}{3}\right) \implies B = 3$$

Dengan demikian, bentuk pecahan parsial dari $G(x)$ adalah:
$$G(x) = \frac{-2}{1 - 2x} + \frac{3}{1 - 3x}$$

Ubah kembali fungsi pembangkit tersebut menjadi bentuk deret pangkat formal:
$$G(x) = -2 \sum_{n=0}^\infty (2x)^n + 3 \sum_{n=0}^\infty (3x)^n = \sum_{n=0}^\infty \left( 3 \cdot 3^n - 2 \cdot 2^n \right) x^n$$
$$G(x) = \sum_{n=0}^\infty \left( 3^{n+1} - 2^{n+1} \right) x^n$$

Solusi dari relasi rekursif $a_n$ didefinisikan sebagai koefisien dari $x^n$ pada fungsi pembangkit $G(x)$:
$$a_n = 3^{n+1} - 2^{n+1} \quad \text{untuk } n \geq 0$$

---

### Solusi Soal 5

Misalkan $a_n$ menyatakan jumlah barisan biner dengan panjang $n$ yang tidak mengandung dua angka '0' berturut-turut.

**Konstruksi Relasi Rekursif:**
Suatu barisan biner valid dengan panjang $n$ dapat diklasifikasikan menjadi dua kategori berdasarkan digit terakhirnya:
1. **Barisan berakhiran dengan digit '1':**
   Karena digit terakhir bernilai '1', tidak ada batasan untuk digit sebelumnya. Dengan demikian, $n-1$ digit pertama dapat membentuk barisan biner valid dengan panjang $n-1$ apa saja. Jumlah barisan pada kategori ini adalah $a_{n-1}$.
2. **Barisan berakhiran dengan digit '0':**
   Karena barisan tidak boleh mengandung dua angka '0' berturut-turut, digit sebelum '0' haruslah bernilai '1'. Sehingga barisan berakhir dengan pola '10'. Maka, $n-2$ digit pertama dapat membentuk barisan biner valid dengan panjang $n-2$ apa saja. Jumlah barisan pada kategori ini adalah $a_{n-2}$.

Dengan menjumlahkan kedua kasus mutually exclusive tersebut, diperoleh relasi rekursif:
$$a_n = a_{n-1} + a_{n-2} \quad \text{untuk } n \geq 3$$

**Kondisi Awal:**
- Untuk $n = 1$, barisan valid adalah: `0`, `1`. Maka $a_1 = 2$.
- Untuk $n = 2$, barisan valid adalah: `01`, `10`, `11`. Maka $a_2 = 3$.
*(Catatan: Untuk penyederhanaan aljabar, kita dapat menetapkan kondisi awal pada $n=0$ dengan $a_0 = 1$ (barisan kosong dianggap valid), sehingga relasi rekursif berlaku untuk $n \geq 2$ dengan kondisi awal $a_0 = 1$ dan $a_1 = 2$).*

**Penyelesaian Relasi Rekursif:**
Gunakan kondisi awal $a_0 = 1$ dan $a_1 = 2$.
Persamaan karakteristik dari relasi $a_n - a_{n-1} - a_{n-2} = 0$ adalah:
$$r^2 - r - 1 = 0$$

Menggunakan rumus kuadratis, diperoleh akar-akar karakteristik:
$$r_1 = \frac{1 + \sqrt{5}}{2} \quad \text{dan} \quad r_2 = \frac{1 - \sqrt{5}}{2}$$

Bentuk solusi umum:
$$a_n = \alpha_1 \left( \frac{1 + \sqrt{5}}{2} \right)^n + \alpha_2 \left( \frac{1 - \sqrt{5}}{2} \right)^n$$

Terapkan kondisi awal untuk menentukan $\alpha_1$ dan $\alpha_2$:
1. Untuk $n = 0$:
   $$\alpha_1 + \alpha_2 = 1 \implies \alpha_2 = 1 - \alpha_1 \quad \text{--- (Persamaan i)}$$
2. Untuk $n = 1$:
   $$\alpha_1 \left( \frac{1 + \sqrt{5}}{2} \right) + \alpha_2 \left( \frac{1 - \sqrt{5}}{2} \right) = 2 \quad \text{--- (Persamaan ii)}$$

Substitusikan Persamaan (i) ke dalam Persamaan (ii):
$$\alpha_1 \left( \frac{1 + \sqrt{5}}{2} \right) + (1 - \alpha_1) \left( \frac{1 - \sqrt{5}}{2} \right) = 2$$
$$\alpha_1 \left( \frac{1 + \sqrt{5}}{2} - \frac{1 - \sqrt{5}}{2} \right) + \frac{1 - \sqrt{5}}{2} = 2$$
$$\alpha_1 \sqrt{5} = 2 - \frac{1 - \sqrt{5}}{2}$$
$$\alpha_1 \sqrt{5} = \frac{3 + \sqrt{5}}{2}$$
$$\alpha_1 = \frac{3 + \sqrt{5}}{2\sqrt{5}} = \frac{5 + 3\sqrt{5}}{10}$$

Tentukan nilai $\alpha_2$:
$$\alpha_2 = 1 - \alpha_1 = 1 - \frac{5 + 3\sqrt{5}}{10} = \frac{5 - 3\sqrt{5}}{10}$$

Substitusikan nilai $\alpha_1$ dan $\alpha_2$ kembali ke bentuk solusi umum:
$$a_n = \left(\frac{5 + 3\sqrt{5}}{10}\right) \left( \frac{1 + \sqrt{5}}{2} \right)^n + \left(\frac{5 - 3\sqrt{5}}{10}\right) \left( \frac{1 - \sqrt{5}}{2} \right)^n$$

*(Bentuk di atas setara dengan representasi deret Fibonacci $a_n = F_{n+2}$ menggunakan rumus Binet)*:
$$a_n = \frac{1}{\sqrt{5}} \left[ \left(\frac{1+\sqrt{5}}{2}\right)^{n+2} - \left(\frac{1-\sqrt{5}}{2}\right)^{n+2} \right]$$
