---
type: note
title: "Spatial Filtering - Smoothing and Noise Reduction"
course: "Pengolahan Citra Digital"
semester: 5
week: 5
created: 2026-09-03
prerequisites: ["[[Image Processing Overview]]"]
tags: [college, image-processing, spatial-filtering, noise-reduction]
---

# Spatial Filtering - Smoothing and Noise Reduction

Filtering spasial (*spatial filtering*) adalah teknik manipulasi citra digital yang beroperasi langsung pada intensitas piksel dalam koordinat spasial tanpa melalui transformasi domain frekuensi. Di dalam ranah reduksi noise dan penghalusan citra (*smoothing*), dua pendekatan fundamental yang saling melengkapi adalah **Gaussian filtering** (filter linear berbasis konvolusi bobot spasial) dan **Median filtering** (filter non-linear berbasis statistik urutan). Memahami trade-off matematis keduanya sangat krusial untuk menyeimbangkan eliminasi noise dengan pelestarian ketajaman tepi objek (*edge preservation*).

## Mekanisme Pemrosesan Bertetangga (Neighborhood Processing)

Operasi spasial menggunakan jendela geser (*sliding window/sub-image*) berukuran ganjil $k \times k$ (misalnya $3 \times 3$, $5 \times 5$) dengan titik acuan di piksel pusat $(x, y)$. Nilai baru pada koordinat $(x, y)$ dihasilkan dari fungsi $T$ terhadap nilai-nilai piksel tetangga di dalam himpunan $\mathcal{S}_{xy}$:

$$g(x, y) = T(f(s, t)), \quad (s, t) \in \mathcal{S}_{xy}$$

Perbedaan mendasar antara filter linear dan non-linear terletak pada formulasi operator $T$:
* **Filter Linear:** $T$ berupa kombinasi linear (penjumlahan perkalian bobot/konvolusi). Jika input merupakan superposisi sinyal, outputnya adalah superposisi respon.
* **Filter Non-Linear:** $T$ melibatkan operasi logis atau statistik urutan (misalnya pengurutan, pengambilan nilai tengah, min, max) yang tidak memenuhi prinsip superposisi.

## Gaussian Filtering: Penghalusan Linear Berbobot Jarak

Ketika citra terkontaminasi oleh noise aditif kontinu (seperti *Gaussian noise* akibat fluktuasi termal sensor kamera), perataan nilai menggunakan rata-rata sederhana (*box filter*) sering kali menghasilkan artefak garis kotak yang tidak alami. Filter Gaussian mengatasi kelemahan ini dengan memberikan bobot tertinggi pada piksel pusat, kemudian meluruh secara halus dan isotropik seiring bertambahnya jarak euclidean dari pusat.

### Formulasi Matematis

Kernel Gaussian 2D diturunkan dari fungsi kepadatan probabilitas distribusi normal multivariat dengan rata-rata nol:

$$G(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}$$

Keterangan parameter:
* $(x, y)$: Jarak koordinat relatif dari titik pusat kernel $(0, 0)$.
* $\sigma$ (*standard deviation*): Mengontrol dispersi spasial kurva lonceng. Nilai $\sigma$ menentukan derajat pemburaman (*blurring*). Semakin besar $\sigma$, semakin luas area tetangga yang berkontribusi secara signifikan.

Untuk menjaga agar intensitas rata-rata citra tidak mengalami pergeseran energi iluminasi, matriks kernel diskret $K$ harus dinormalisasi:

$$K_{\text{norm}}(x, y) = \frac{K(x, y)}{\sum_{u} \sum_{v} K(u, v)}$$

### Optimasi Komputasi melalui Separabilitas (Separable Kernels)

Fungsi eksponensial Gaussian 2D dapat difaktorkan menjadi perkalian dua fungsi Gaussian 1D independen:

$$G(x, y) = \left( \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{x^2}{2\sigma^2}} \right) \left( \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{y^2}{2\sigma^2}} \right) = G(x) \cdot G(y)$$

Sifat ini memungkinkan konvolusi 2D penuh berukuran $k \times k$ dipecah menjadi dua lintasan konvolusi 1D:
1. Konvolusi setiap baris citra dengan kernel horizontal $1 \times k$.
2. Konvolusi setiap kolom dari hasil langkah pertama dengan kernel vertikal $k \times 1$.

Efisiensi komputasi meningkat drastis: kompleksitas per piksel terpangkas dari $\mathcal{O}(k^2)$ perkalian menjadi $\mathcal{O}(2k)$.

### Contoh Pembentukan Kernel $3 \times 3$ ($\sigma = 1.0$)

Matriks jarak koordinat relatif dari pusat $(0, 0)$:

$$
\begin{bmatrix}
(-1, -1) & (0, -1) & (1, -1) \\
(-1,  0) & (0,  0) & (1,  0) \\
(-1,  1) & (0,  1) & (1,  1)
\end{bmatrix}
\implies
x^2 + y^2 = 
\begin{bmatrix}
2 & 1 & 2 \\
1 & 0 & 1 \\
2 & 1 & 2
\end{bmatrix}
$$

Substitusi ke formula unnormalized $e^{-\frac{x^2 + y^2}{2(1)^2}}$:

$$
K \approx
\begin{bmatrix}
e^{-1.0} & e^{-0.5} & e^{-1.0} \\
e^{-0.5} & e^{0}    & e^{-0.5} \\
e^{-1.0} & e^{-0.5} & e^{-1.0}
\end{bmatrix}
\approx
\begin{bmatrix}
0.3679 & 0.6065 & 0.3679 \\
0.6065 & 1.0000 & 0.6065 \\
0.3679 & 0.6065 & 0.3679
\end{bmatrix}
$$

Total bobot matriks $\sum K \approx 4.8976$. Setelah dinormalisasi ($K / \sum K$):

$$
K_{\text{norm}} \approx
\begin{bmatrix}
0.0751 & 0.1238 & 0.0751 \\
0.1238 & 0.2042 & 0.1238 \\
0.0751 & 0.1238 & 0.0751
\end{bmatrix}
$$

Piksel pusat mendapatkan bobot dominan ($20.4\%$), sementara sudut-sudut diagonal terjauh hanya menyerap ($7.5\%$).

## Median Filtering: Restorasi Non-Linear Berbasis Statistik Peringkat

Ketika noise citra berupa impuls ekstrem diskret—seperti *salt-and-pepper noise* di mana nilai piksel rusak menjadi $0$ (hitam pekat) atau $255$ (putih maksimal)—filter linear seperti Gaussian mengalami kegagalan struktural. Nilai ekstrem tersebut tetap masuk ke dalam perhitungan rata-rata, menghasilkan bercak noda kabur di sekitar titik noise.

Median filter bekerja dengan paradigma *order-statistic*: mengganti nilai piksel pusat dengan nilai tengah himpunan intensitas lokal yang telah diurutkan.

### Prosedur Operasi

1. Definisikan jendela tetangga $\mathcal{S}_{xy}$ berdimensi $k \times k$ (dengan $k$ ganjil).
2. Ekstrak seluruh intensitas piksel di dalam jendela menjadi vektor 1D berukuran $N = k^2$.
3. Urutkan elemen vektor secara menaik: $I_{(1)} \le I_{(2)} \le \dots \le I_{(N)}$.
4. Ambil elemen pada posisi median:
   
   $$\hat{f}(x, y) = \text{median}\{f(s, t)\} = I_{\left(\frac{N+1}{2}\right)}$$

### Kekuatan Eliminasi Outlier dan Preservasi Tepi

Median filter memiliki dua keunggulan esensial:
1. **Kebal Terhadap Outlier:** Selama jumlah piksel noise di dalam jendela lokal kurang dari separuh kapasitas jendela ($\lfloor N/2 \rfloor$), nilai noise ekstrem ($0$ atau $255$) akan selalu terdorong ke ujung kiri ($I_{(1)}$) atau ujung kanan ($I_{(N)}$) dari array terurut, sehingga tidak akan pernah terpilih sebagai nilai tengah.
2. **Edge Preservation:** Pada transisi tepi tajam (*step edge*), misalnya separuh jendela bernilai $20$ dan separuh lainnya bernilai $200$, median akan selalu memilih salah satu nilai asli ($20$ atau $200$). Median filter tidak menghasilkan intensitas rata-rata buatan (seperti $110$), sehingga ketajaman batas visual tetap terjaga tanpa terdegradasi menjadi gradien blur.

### Contoh Numerik Eliminasi Noise

Tinjau blok citra $3 \times 3$ di mana piksel pusat terinfeksi noise salt ($255$):

$$
f(x, y) =
\begin{bmatrix}
50 & 52 & 49 \\
51 & \mathbf{255} & 53 \\
48 & 50 & 52
\end{bmatrix}
$$

* Vektor terurut: $[48, 49, 50, 50, \mathbf{51}, 52, 52, 53, 255]$
* Nilai median ($N=9$, indeks ke-5): **$51$**
* Respon output: Piksel pusat $255$ langsung dinormalisasi kembali menjadi $51$. Outlier hilang total tanpa mengaburkan tetangganya.

## Analisis Komparatif: Gaussian vs Median

| Parameter Evaluasi | Gaussian Filter | Median Filter |
| :--- | :--- | :--- |
| **Kategori Matematis** | Linear (Spatial Convolution) | Non-linear (Order-Statistics) |
| **Profil Noise Target** | Gaussian, Uniform, Thermal noise kontinu | Salt-and-pepper, Bipolar impulse noise |
| **Respon Outlier Ekstrem** | Rentan; menyebarkan energi outlier ke tetangga | Kebal mutlak (selama $< 50\%$ jendela) |
| **Dampak Tepi (*Edges*)** | Isotropic blurring; mendegradasi ketajaman tepi | Mempertahankan batas tepi tajam bertingkat |
| **Piksel Sintetis** | Menghasilkan nilai interpolasi desimal baru | Menggunakan nilai riil yang ada pada jendela |
| **Kompleksitas Komputasi** | $\mathcal{O}(2k)$ per piksel via dekomposisi separable | $\mathcal{O}(k^2 \log k)$ per piksel (sorting baku) |
| **Efek Samping Negatif** | Kehilangan detail frekuensi tinggi dan tekstur | Menghapus fitur garis tipis & sudut tajam (*corners*) |

> [!abstract]- Quick Reference
> 
> ### Formula Inti
> * **Gaussian 2D Kernel:**
>   $$G(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}$$
> * **Median Filter:**
>   $$\hat{f}(x, y) = \text{median}\left\{ f(s, t) \mid (s, t) \in \mathcal{S}_{xy} \right\}$$
> 
> ### Aturan Pemilihan Praktis
> 1. **Salt-and-Pepper Noise:** Selalu gunakan **Median Filter**. Filter Gaussian tidak akan mampu membersihkan titik putih/hitam tanpa merusak total citra.
> 2. **Continuous/Sensor Noise:** Gunakan **Gaussian Filter**. Filter linear memberikan error kuadrat terkecil (MSE) terendah untuk noise Gaussian.
> 3. **Ukuran Kernel Gaussian:** Pilih ukuran kernel $k \ge 6\sigma$ (dibulatkan ke ganjil terdekat) agar memuat $\ge 99.7\%$ energi volume fungsi lonceng.
> 4. **Batas Teoretis Median:** Median filter gagal jika noise density $p > 0.5$ dalam suatu jendela. Untuk kasus noise sangat padat, beralih ke *Adaptive Median Filter*.

> [!question]- Practice
> 
> **Soal 1:** Sebuah citra biner 1D memiliki transisi tepi berupa array: $[0, 0, 0, 100, 100, 100]$. Bandingkan output pada titik transisi (indeks ke-3 bernilai $0$ dan indeks ke-4 bernilai $100$) jika diterapkan:
> (a) Box filter 1D ukuran $3$ dengan kernel $[\frac{1}{3}, \frac{1}{3}, \frac{1}{3}]$.
> (b) Median filter 1D ukuran $3$.
> 
> > [!check]- Answer
> > * **Box Filter:**
> >   - Indeks 3 (tetangga: $[0, 0, 100]$): $(0 + 0 + 100)/3 = \mathbf{33.33}$
> >   - Indeks 4 (tetangga: $[0, 100, 100]$): $(0 + 100 + 100)/3 = \mathbf{66.67}$
> >   Hasil: Tepi tajam $0 \to 100$ memudar menjadi transisi landai $[0, 0, 33.33, 66.67, 100, 100]$ (*edge blurring*).
> > * **Median Filter:**
> >   - Indeks 3 (tetangga: $[0, 0, 100]$): Median dari array terurut $[0, 0, 100]$ adalah $\mathbf{0}$.
> >   - Indeks 4 (tetangga: $[0, 100, 100]$): Median dari array terurut $[0, 100, 100]$ adalah $\mathbf{100}$.
> >   Hasil: Array tetap utuh $[0, 0, 0, 100, 100, 100]$. Tepi tajam dipertahankan sempurna (*perfect edge preservation*).
> 
> **Soal 2:** Kenapa fungsi konvolusi Gaussian 2D dapat dihitung jauh lebih cepat menggunakan dua konvolusi 1D, sedangkan Median filter tidak dapat dipisahkan (*non-separable*) menjadi dua lintasan 1D?
> 
> > [!check]- Answer
> > Gaussian filter bersifat *separable* karena kernel 2D-nya merupakan *outer product* dari dua vektor 1D ($G(x, y) = G(x) \cdot G(y)$) dan operasi konvolusi adalah linear (memenuhi sifat asosiatif dan distributif). 
> > Sebaliknya, median filter adalah operasi non-linear berbasis perankingan. $\text{median}_{2D}(A)$ tidak sama dengan $\text{median}_{1D}(\text{median}_{1D}(A))$. Menghitung median baris lalu kolom akan menghasilkan distorsi statistik urutan dan bukan merepresentasikan median dari himpunan 2D sejati.

> [!info]- Going Deeper
> 
> * **Bilateral Filtering:** Mengatasi kompromi Gaussian filter dengan menggabungkan dua kernel Gaussian sekaligus: bobot kedekatan spasial (*domain filter*) dan bobot kemiripan intensitas radiometrik (*range filter*). Hasilnya adalah penghalusan noise Gaussian dengan kemampuan pelestarian tepi setara median filter.
> * **Adaptive Median Filter (AMF):** Algoritma yang secara dinamis memperbesar ukuran jendela $k \times k$ ketika nilai median lokal itu sendiri terindikasi sebagai piksel noise impulsif. Efektif menangani noise salt-and-pepper hingga kepadatan $p > 70\%$.
> * **Huang's Algorithm & Constant Time Median:** Implementasi standar median filter membutuhkan waktu $\mathcal{O}(k^2 \log k)$ per piksel. Algoritma histogram pergeseran oleh Huang mereduksinya menjadi $\mathcal{O}(k)$, dan metode Perreault/Hebert memungkinkan komputasi konstan $\mathcal{O}(1)$ independen terhadap ukuran kernel.
