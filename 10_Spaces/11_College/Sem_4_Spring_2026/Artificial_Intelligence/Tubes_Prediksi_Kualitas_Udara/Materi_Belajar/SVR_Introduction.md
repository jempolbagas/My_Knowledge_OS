---
title: "Membongkar Support Vector Regression (SVR): Intuisi, Matematika, dan Kernel Trick"
course: "Artificial Intelligence"
tags:
  - college/study-guide
  - machine-learning
  - support-vector-regression
  - svr
aliases:
  - Pengenalan SVR
  - SVR Introduction
created: 2026-07-01
---

# Membongkar Support Vector Regression (SVR): Intuisi, Matematika, dan Kernel Trick

Halo gaes! Setelah sebelumnya kita sukses nguliti [[10_Spaces/11_College/Sem_4_Spring_2026/Artificial_Intelligence/Tubes_Prediksi_Kualitas_Udara/Air_Quality_Prediction_MLR_Complete_Guide|Multiple Linear Regression (MLR)]] buat prediksi kualitas udara Jakarta, sekarang kita bakal bongkar algoritma machine learning lain yang gak kalah sakti: **Support Vector Regression (SVR)**. 

Kalau di [[10_Spaces/11_College/Sem_4_Spring_2026/Artificial_Intelligence/Tubes_Prediksi_Kualitas_Udara/Prediksi Kualitas Udara Harian Berbasis Faktor Cuaca di Jakarta Menggunakan Multiple Linear Regression|Laporan Utama MLR]] kita sempat bahas kalau MLR menang karena hubungan datanya cenderung linear, kita kudu tetap paham alternatif algoritma yang tangguh kalau seandainya data yang kita hadapi meliuk-liuk gak karuan (non-linear) dan punya banyak data pencilan (*outliers*). Di sinilah SVR unjuk gigi!

Yuk, kita bedah konsepnya satu per satu dari intuisi dasar sampai matematika di baliknya!

---

## Bab 1: Intuisi Dasar SVR (Kenapa SVR Beda Kelas?)

Untuk paham SVR, kita kudu bandingkan dulu filosofi kerjanya dengan regresi tradisional kayak MLR.

Pada MLR biasa, misi utama kita adalah meminimalkan kuadrat selisih (*squared error*) antara nilai asli dengan prediksi. Dampaknya, sekecil apa pun jarak suatu titik ke garis regresi, dia bakal tetap dihitung dan memengaruhi kemiringan garis. Kalau ada satu atau dua data pencilan (*outliers*) yang nilainya ekstrem, garis regresi MLR bakal langsung ketarik (*bias*).

SVR punya cara pandang yang beda banget. SVR menerapkan apa yang disebut dengan **$\epsilon$-insensitive loss function** (fungsi kerugian tak-sensitif epsilon).

> [!INFO]
> **Analogi Jalan Tol dan Pagar Pengaman:**
> Bayangkan kita mau bikin jalan tol lurus (garis prediksi). Di kanan-kiri jalan tol itu, kita pasang pagar pengaman berjarak $\epsilon$ (pipa toleransi atau **$\epsilon$-tube**).
> Selama mobil-mobil (titik data) melaju dengan aman di dalam area jalan tol ini (jarak error $\le \epsilon$), kita bakal santai aja dan menganggap error-nya **nol**. Kita baru bakal ngasih penalti (denda) kalau ada mobil yang menabrak pagar pengaman dan keluar dari area jalan tol tersebut.
> 
> Dengan filosofi ini, SVR gak gampang goyah sama fluktuasi kecil data di dalam pipa toleransi, sehingga modelnya jauh lebih stabil dan kebal terhadap pencilan!

---

## Bab 2: Komponen Utama SVR

Untuk ngerjain SVR, ada beberapa pilar utama yang wajib kita kuasai:

### 1. Hyperplane (Bidang Pembatas)
Sama seperti model linear lainnya, di dalam SVR kita ingin mencari sebuah fungsi pembatas yang disebut **hyperplane**. Rumus dasarnya mirip dengan persamaan garis linear:

$$f(x) = \langle w, x \rangle + b$$

Di mana:
* $w$: Vektor bobot (*weight vector*) yang menentukan kemiringan *hyperplane*.
* $x$: Fitur input (misal parameter cuaca seperti suhu, kecepatan angin, dll.).
* $b$: Konstanta bias.
* $\langle w, x \rangle$: Hasil perkalian titik (*dot product*) antara bobot dan fitur.

### 2. $\epsilon$-Tube (Epsilon-Insensitive Band)
Ini adalah pipa toleransi pembungkus *hyperplane*. Tebal total pipa ini adalah $2\epsilon$. Aturan main dari pipa ini adalah:

$$\mathcal{L}_\epsilon(y, f(x)) = \begin{cases} 0 & \text{jika } |y - f(x)| \le \epsilon \\ |y - f(x)| - \epsilon & \text{lainnya} \end{cases}$$

Di mana $y$ adalah nilai aktual dan $f(x)$ adalah nilai prediksi. Kalau selisihnya masih di bawah $\epsilon$, SVR tutup mata!

### 3. Slack Variables ($\xi_i$ dan $\xi_i^*$)
Tentu saja di dunia nyata, gak mungkin semua data bisa muat pas di dalam pipa toleransi $\epsilon$. Pasti ada aja titik-titik data membandel yang loncat ke luar pipa. Biar model SVR kita gak puyeng dan tetap bisa menemukan solusi, kita mengenalkan variabel pelonggar yang disebut **slack variables**:
* $\xi_i$ (xi): Jarak kesalahan untuk data yang meleset di *atas* pipa.
* $\xi_i^*$ (xi-star): Jarak kesalahan untuk data yang meleset di *bawah* pipa.

---

## Bab 3: Parameter Kontrol SVR (C dan Kernel)

Ada dua tombol pengontrol utama yang kudu kita setel pas konfigurasi SVR biar hasilnya kece:

### 1. Parameter Penalti $C$
Parameter $C$ ini bertindak sebagai juri pengadil yang menyeimbangkan antara kesederhanaan model (kerataan pipa) dengan toleransi terhadap kesalahan data yang keluar dari pipa.

> [!IMPORTANT]
> **Dilema Penyetelan Nilai C:**
> * **Nilai $C$ Kecil:** Kita sangat toleran terhadap kesalahan. SVR bakal fokus membuat pipa se-datar dan se-sederhana mungkin dengan meminimalkan $\|w\|^2$. Risiko: model bisa mengalami *underfitting* karena terlalu mengabaikan data.
> * **Nilai $C$ Besar:** Kita galak banget! Setiap ada titik data yang meleset keluar pipa, penaltinya bakal luar biasa besar. SVR bakal meliuk-liuk ekstrem demi memuat semua data ke dalam pipa. Risiko: model sangat rentan terkena *overfitting* karena menghafal *noise* data latih.

### 2. Kernel Trick & RBF (Radial Basis Function) Kernel
Nah, ini dia senjata pamungkas SVR! Bagaimana kalau hubungan data cuaca dan kualitas udara kita ternyata melengkung non-linear? SVR mengatasi ini dengan memetakan data input asli ke ruang dimensi yang lebih tinggi (*high-dimensional space*) di mana data tersebut menjadi linear dan bisa dipotong oleh *hyperplane*. Proses pemetaan ini dipermudah lewat **Kernel Trick**.

Salah satu fungsi kernel yang paling populer dan sering dipakai adalah **RBF Kernel (Radial Basis Function)**:

$$K(x_i, x_j) = \exp\left( -\gamma \|x_i - x_j\|^2 \right)$$

Di mana:
* $\|x_i - x_j\|^2$: Jarak Euclidean kuadrat antara dua titik data.
* $\gamma$ (gamma): Parameter yang menentukan seberapa jauh jangkauan pengaruh dari satu titik data latih tunggal.

> [!TIP]
> **Memahami Parameter Gamma ($\gamma$):**
> * **$\gamma$ Tinggi:** Jangkauan pengaruh tiap titik sangat dekat (lokal). Kurva prediksi SVR bakal bergelombang tajam mengikuti masing-masing titik terdekat. Rentan *overfitting*.
> * **$\gamma$ Rendah:** Jangkauan pengaruh menyebar jauh. Kurva prediksi SVR akan sangat mulus (*smooth*) dan menyerupai tren umum data. Rentan *underfitting* jika disetel terlalu rendah.

---

## Bab 4: Formulasi Matematis Optimasi SVR

Secara matematis, tujuan utama SVR adalah meminimalkan fungsi tujuan berikut (dikenal sebagai *primal optimization problem*):

$$\min_{w, b, \xi, \xi^*} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^n (\xi_i + \xi_i^*)$$

Dengan kendala (*constraints*):

$$y_i - \langle w, x_i \rangle - b \le \epsilon + \xi_i$$
$$\langle w, x_i \rangle + b - y_i \le \epsilon + \xi_i^*$$
$$\xi_i, \xi_i^* \ge 0 \quad \text{untuk } i = 1, \dots, n$$

Untuk mempermudah perhitungan (terutama saat menggunakan trik kernel), masalah optimasi di atas diubah ke dalam bentuk dual menggunakan pengali Lagrange (*Lagrange Multipliers*) $\alpha_i$ dan $\alpha_i^*$. Formulasi dualnya menjadi:

$$\max_{\alpha, \alpha^*} -\frac{1}{2} \sum_{i,j=1}^n (\alpha_i - \alpha_i^*)(\alpha_j - \alpha_j^*) K(x_i, x_j) - \epsilon \sum_{i=1}^n (\alpha_i + \alpha_i^*) + \sum_{i=1}^n y_i(\alpha_i - \alpha_i^*)$$

Dengan kendala:

$$\sum_{i=1}^n (\alpha_i - \alpha_i^*) = 0$$
$$0 \le \alpha_i, \alpha_i^* \le C \quad \text{untuk } i = 1, \dots, n$$

Setelah masalah optimasi dual ini diselesaikan, kita bakal mendapatkan nilai $\alpha_i$ dan $\alpha_i^*$. Fungsi prediksi akhir SVR dirumuskan sebagai:

$$f(x) = \sum_{i=1}^n (\alpha_i - \alpha_i^*) K(x_i, x) + b$$

> [!INFO]
> **Siapa itu Support Vectors?**
> Menariknya, sebagian besar titik data di dalam pipa $\epsilon$ akan menghasilkan nilai $\alpha_i - \alpha_i^* = 0$. 
> Hanya titik-titik data yang berada di batas pipa atau di luar pipa yang memiliki nilai $\alpha_i - \alpha_i^* \neq 0$. Titik-titik inilah yang disebut **Support Vectors** (vektor pendukung). 
> Mereka adalah penyangga utama seluruh struktur model SVR. Jika kita menghapus data lain yang bukan support vectors dari dataset kita, model prediksi SVR yang dihasilkan tidak akan berubah sedikit pun!

---

## Bab 5: Contoh Kasus Kerja SVR pada Prediksi AQI Jakarta

Biar makin kebayang cara kerjanya di lapangan, mari kita ceki-ceki contoh kasus sederhana berikut.

> [!EXAMPLE]
> **Studi Kasus: Hubungan Suhu vs AQI**
> Bayangkan kita ingin memprediksi nilai AQI ($Y$) berdasarkan Suhu Udara ($X$) menggunakan data historis harian Jakarta. Hubungannya bersifat non-linear:
> * Pada suhu rendah ($23^\circ\text{C}$ - $25^\circ\text{C}$), AQI stabil rendah sekitar $40$ (udara bersih).
> * Pada suhu sedang ($26^\circ\text{C}$ - $29^\circ\text{C}$), AQI naik perlahan ke angka $70$.
> * Pada suhu ekstrem panas ($30^\circ\text{C}$ - $34^\circ\text{C}$), terjadi lonjakan reaksi fotokimia polutan sekunder yang membuat AQI meroket non-linear hingga di atas $150$ (sangat tidak sehat).
> 
> **Langkah Kerja SVR dengan RBF Kernel:**
> 1. **Standarisasi Fitur:** Pertama-tama, data suhu distandarisasi menggunakan Z-Score scaling agar rata-rata bernilai 0 dan standar deviasi bernilai 1.
> 2. **Pemetaan Kernel:** RBF Kernel secara implisit memetakan data suhu terstandarisasi ini ke dimensi yang lebih tinggi sehingga pola belokan ekstrem di suhu panas bisa diakomodasi oleh garis lurus di ruang baru tersebut.
> 3. **Penyusunan Pipa Epsilon:** Kita setel $\epsilon = 10$. Artinya, jika prediksi model meleset maksimal 10 poin AQI dari data asli, SVR mengabaikan kesalahan tersebut.
> 4. **Penanganan Outlier:** Bayangkan ada satu hari anomali di mana suhu sangat panas ($33^\circ\text{C}$) tetapi nilai AQI tiba-tiba jatuh ke $30$ akibat ada kebijakan pembatasan kendaraan darurat. Data ini menjadi *outlier* yang berada jauh di bawah pipa toleransi.
>    * Jika kita setel parameter penalti $C$ moderat, SVR tidak akan merusak kelengkungan garis prediksi demi mengejar satu titik anomali ini. Model akan tetap setia mengikuti tren data normal lainnya (para *support vectors*).

---

## Bab 6: Ringkasan Alur Kerja SVR

Berikut adalah visualisasi alur bagaimana algoritma SVR bekerja memproses data input hingga menghasilkan nilai prediksi AQI:

```mermaid
graph TD
    DataInput["Data Cuaca Mentah (X)"] ──►|"Preprocessing"| Scaling["Z-Score Scaling"]
    Scaling ──►|"Kernel Trick"| RBFKernel["RBF Kernel Transformation"]
    RBFKernel ──►|"Memetakan ke"| HighDim["Ruang Dimensi Tinggi"]
    HighDim ──►|"Formulasi Optimasi"| OptProblem["Minimasi Error dengan Penalti C & Toleransi Epsilon"]
    OptProblem ──►|"Identifikasi"| SV["Menemukan Support Vectors"]
    SV ──►|"Konstruksi"| Hyperplane["Membentuk Hyperplane Optimal"]
    Hyperplane ──►|"Prediksi Akhir"| FinalPrediction["Prediksi AQI (Y-hat)"]
```

Dengan menguasai SVR ini, kita sekarang punya alternatif model machine learning yang kokoh jika di masa depan tugas besar kita menuntut akurasi pada pola data lingkungan yang non-linear dan penuh derau (*noisy*)! Sampai jumpa di materi belajar berikutnya, gaes!
