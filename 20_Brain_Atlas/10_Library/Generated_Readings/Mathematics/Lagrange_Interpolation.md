---
type: generated_reading
title: Lagrange Interpolation
topic: "Numerical Methods"
requested_on: 2026-08-19
prompt: "Bikinin aku bacaan materi tentang lagrange interpolation"
status: done
tags: []
promoted_to: []
---

## The reading

Interpolasi Lagrange adalah sebuah metode numerik yang digunakan untuk menemukan fungsi polinomial tunggal yang secara pasti melewati sekumpulan titik data yang telah diketahui. Metode ini bekerja dengan cara merakit polinomial secara aditif, di mana untuk setiap titik data, kita membuat sebuah "polinomial basis" khusus yang memuncak (bernilai 1) tepat di titik tersebut dan tereduksi (bernilai 0) pada semua titik data lainnya berkat rekayasa sifat Delta Kronecker. Polinomial ini kemudian dikalikan dengan nilai koordinat Y dari titik data asli dan dijumlahkan seluruhnya untuk menghasilkan kurva interpolasi akhir yang mulus dan presisi tanpa campur tangan antar titik.

### Formulasi Matematis

Misalkan kita diberikan serangkaian $n+1$ titik observasi empiris: $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$. Semua nilai absis ($x_i$) diasumsikan unik atau tidak ada yang tumpang tindih. Tujuan kita adalah mencari polinomial $P(x)$ berderajat paling tinggi $n$ sedemikian rupa sehingga $P(x_i) = y_i$ untuk setiap $0 \leq i \leq n$.

Bentuk umum dari polinomial interpolasi Lagrange diberikan oleh formula:
$$ P(x) = \sum_{i=0}^{n} y_i L_i(x) $$

Fungsi $L_i(x)$ dinamakan **Polinomial Basis Lagrange** untuk indeks ke-$i$. Rumus formal untuk mendefinisikan polinomial basis ini adalah hasil perkalian (product) berangkai:
$$ L_i(x) = \prod_{k=0, k \neq i}^{n} \frac{x - x_k}{x_i - x_k} $$

### Rekayasa Sifat Delta Kronecker ($\delta_{ij}$)

Karakteristik fundamental yang membuat metode interpolasi ini berhasil murni bersumber dari struktur polinomial basis $L_i(x)$. Struktur tersebut secara sengaja didesain untuk meniru perilaku saklar matematis **Delta Kronecker**.

Jika kita melakukan evaluasi polinomial basis $L_i(x)$ pada suatu titik sampel yang diketahui, $x_j$, maka fungsi tersebut akan bertindak logis:
- **Kondisi Bernilai 0**: Apabila kita mengevaluasinya pada titik data milik variabel lain ($j \neq i$), maka bagian pembilang akan terpaksa melibatkan faktor $(x_j - x_j)$ yang notabene adalah $0$. Karena sifat operasi perkaliannya, keseluruhan pembilang pun runtuh menjadi $0$.
- **Kondisi Bernilai 1**: Apabila kita mengevaluasinya pada titik lokasinya sendiri ($j = i$), maka ekspresi pada pembilang akan tumbuh identik dengan ekspresi pada penyebut. Sesuatu yang terbagi oleh cerminannya sendiri pasti menghasilkan nilai $1$.

Kombinasi kedua kondisi ini bisa diformalkan menjadi Sifat Delta Kronecker: $L_i(x_j) = \delta_{ij}$. Implikasi paling besarnya adalah saat kita membangun fungsi akhirnya:
$$ P(x_j) = \sum_{i=0}^n y_i L_i(x_j) = \sum_{i=0}^n y_i \delta_{ij} = y_j $$
Polinomial basis berhasil mematikan (memberikan bobot 0 pada) pengaruh titik lain, dan menghidupkan (memberikan bobot penuh 1 pada) titik acuannya sendiri.

### Contoh Perhitungan Kasus Sederhana

Pertimbangkan kita hanya memiliki dua titik data linier: $(x_0, y_0)$ dan $(x_1, y_1)$. Kita diminta mencari polinomial Lagrange berderajat $n=1$.

1. Menentukan basis pertama, $L_0(x)$:
   Hanya ada satu suku di mana $k \neq 0$, yaitu $k=1$. Maka:
   $$ L_0(x) = \frac{x - x_1}{x_0 - x_1} $$
2. Menentukan basis kedua, $L_1(x)$:
   Satu-satunya suku di mana $k \neq 1$ adalah $k=0$. Maka:
   $$ L_1(x) = \frac{x - x_0}{x_1 - x_0} $$

Kemudian kita menjahitnya ke dalam fungsi utuh $P(x)$:
$$ P(x) = y_0 \left( \frac{x - x_1}{x_0 - x_1} \right) + y_1 \left( \frac{x - x_0}{x_1 - x_0} \right) $$
Rumus akhirnya ekuivalen penuh secara aljabar dengan persamaan garis lurus biasa, merepresentasikan betapa solidnya arsitektur interpolasi Lagrange pada kasus-kasus linear maupun non-linear tingkat tinggi.

### Limitasi Kritis: Fenomena Runge (Runge's Phenomenon)

Meskipun secara konseptual sangat elegan dan mudah diimplementasikan ke dalam program komputer (karena bentuknya berupa loop iterasi perkalian sederhana), Interpolasi Lagrange tidak selamanya sempurna. 

Ketika kita memperbanyak jumlah titik sampel (meningkatkan derajat polinomial $n$) dengan interval jarak antar-titik yang seragam dan simetris secara terus-menerus, kurva polinomial interpolasi di titik-titik bagian tengah mungkin terlihat menjanjikan. Namun di area sekitar titik ujung (batas interval ekstrem), kurvanya berpotensi mengalami **osilasi liar** (ayunan grafis dramatis naik-turun yang parah). Hal tersebut dinamakan sebagai Runge's Phenomenon. Oleh sebab inilah, untuk titik observasi skala masif, rekayasawan lebih menyukai interpolasi menggunakan Cubic Spline dibandingkan Lagrange.

## Concepts to extract
- [ ] Runge's Phenomenon
- [ ] Polinomial Basis Lagrange
- [ ] Sifat Menyaring (Sifting Property)
