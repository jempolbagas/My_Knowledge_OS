---
title: "Pengantar XGBoost: Pembelajaran Sekuensial dan Penanganan Overfitting"
course: "Artificial Intelligence"
tags:
  - college/study-guide
  - machine-learning
  - xgboost
  - decision-tree
  - boosting
aliases:
  - Pengantar XGBoost
  - Materi Belajar XGBoost
created: 2026-07-01
---

# Pengantar XGBoost: Pembelajaran Sekuensial dan Penanganan Overfitting

Halo gaes! Setelah sebelumnya kita berhasil membongkar cara kerja model linear lewat [[../Air_Quality_Prediction_MLR_Complete_Guide|Panduan Lengkap MLR]] dan mengaplikasikannya di [[../Prediksi Kualitas Udara Harian Berbasis Faktor Cuaca di Jakarta Menggunakan Multiple Linear Regression|Laporan Tugas Besar MLR]], sekarang kita bakal melangkah ke level berikutnya. 

Kita tahu kalau hubungan antara cuaca dan polusi udara (AQI) di Jakarta kadang gak sesederhana garis lurus aja. Ada kalanya hubungannya berkelok-kelok alias non-linear. Nah, salah satu algoritma *machine learning* paling perkasa untuk melibas pola non-linear yang kompleks ini adalah **XGBoost (Extreme Gradient Boosting)**.

Di panduan ini, kita bakal bongkar pelan-pelan dari nol mulai dari konsep dasar Decision Tree, cara kerja Boosting secara sekuensial untuk meminimalkan error sisa (*residual error*), sampai kenapa model sekuat XGBoost ini malah rentan kena jebakan *overfitting* pas dikasih data yang ukurannya mini. Yuk, kita mulai!

---

## Bab 1: Fondasi Utama - Decision Tree (Pohon Keputusan)

Sebelum masuk ke boosting yang rumit, kita kudu paham dulu batu bata penyusunnya, yaitu **Decision Tree**. 

> [!INFO]
> **Analogi Game Tebak-Tebakan:**
> Bayangkan kamu lagi main tebak-tebakan untuk menentukan apakah hari ini kualitas udara di Jakarta sehat atau enggak. Kamu bakal nanya beberapa pertanyaan berantai:
> 1. "Apakah hari ini hujan?" $\rightarrow$ Jika Ya, langsung tebak "Sehat".
> 2. Jika Tidak Hujan: "Apakah kecepatan angin > 2 m/s?" $\rightarrow$ Jika Ya, tebak "Sedang". Jika Tidak, tebak "Sangat Tidak Sehat".
> 
> Setiap pertanyaan di atas membagi data kita menjadi kelompok-kelompok yang lebih spesifik. Itulah intuisi dasar dari Decision Tree!

Secara visual, Decision Tree membagi *feature space* (ruang data kita) menggunakan batas-batas tegak lurus (axis-aligned splits) seperti diagram berikut:

```mermaid
graph TD
    Root["Hujan? (Root Node)"] ──►|"Ya"| Leaf1["AQI Sehat (Leaf Node)"]
    Root ──►|"Tidak"| Node1["Angin > 2 m/s? (Internal Node)"]
    Node1 ──►|"Ya"| Leaf2["AQI Sedang (Leaf Node)"]
    Node1 ──►|"Tidak"| Leaf3["AQI Buruk (Leaf Node)"]
```

### Bagaimana Decision Tree Membagi Data?
Untuk kasus regresi (seperti memprediksi angka AQI secara kontinu), pohon keputusan bakal membagi data sedemikian rupa agar nilai di setiap daun (leaf) memiliki variansi atau error yang sekecil mungkin.

Kriteria pemisahan yang paling umum digunakan adalah **Variance Reduction** atau penurunan Mean Squared Error (MSE). Model bakal ceki-ceki semua fitur dan semua kemungkinan titik potong ($s$) untuk mencari pemisahan yang menghasilkan penurunan MSE paling maksimal:

$$\text{Gain} = \text{MSE}_{\text{parent}} - \left( \frac{n_L}{n} \text{MSE}_L + \frac{n_R}{n} \text{MSE}_R \right)$$

*Dengan:*
* $\text{MSE}_{\text{parent}}$: Rata-rata kuadrat error sebelum data dibagi.
* $\text{MSE}_L$ dan $\text{MSE}_R$: Rata-rata kuadrat error pada anak cabang kiri (Left) dan kanan (Right) setelah dibagi.
* $n, n_L, n_R$: Jumlah sampel total, sampel di kiri, dan sampel di kanan.

Pohon ini bakal tumbuh terus ke bawah sampai kriteria berhenti (seperti batas kedalaman maksimum `max_depth` atau jumlah sampel minimum di daun) terpenuhi.

---

## Bab 2: Membongkar Konsep Boosting (Sequential Learning)

Kalau satu Decision Tree biasa sering kali kurang akurat (lemah/bias tinggi), kita bisa menggabungkan banyak pohon menjadi sebuah tim yang kuat. Teknik ini disebut *Ensemble Learning*. Salah satu cara menggabungkannya adalah dengan **Boosting**.

> [!INFO]
> **Analogi Belajar untuk Ujian:**
> Bayangkan kamu lagi belajar ngerjain soal-soal latihan ujian AI. 
> * Di sesi pertama, kamu ngerjain seluruh soal secara acak. Pas ceki-ceki jawaban, ternyata ada beberapa soal yang salah.
> * Di sesi kedua, kamu gak bakal belajar materi yang udah kamu kuasai. Kamu bakal fokus belajar materi dari **soal-soal yang salah** tadi biar nilaimu meningkat.
> * Di sesi ketiga, kamu fokus lagi ke sisa-sisa kesalahan dari sesi kedua. 
> 
> Proses belajar bertahap yang berfokus memperbaiki kesalahan sebelumnya ini adalah inti dari **Boosting**!

Di dalam Boosting, pohon-pohon keputusan dibangun secara **sekuensial (berurutan)**, bukan paralel. Setiap pohon baru dilatih khusus untuk memprediksi **residual error (error sisa)** yang dihasilkan oleh gabungan pohon-pohon sebelumnya.

### Formulasi Matematika Pembelajaran Sekuensial

Misalkan kita punya model ensemble dengan $t-1$ buah pohon. Prediksi untuk data ke-$i$ pada langkah $t-1$ adalah $\hat{y}_i^{(t-1)}$. 

Ketika kita ingin menambahkan pohon ke-$t$ (yaitu $f_t(x)$), prediksi barunya dirumuskan sebagai:

$$\hat{y}_i^{(t)} = \hat{y}_i^{(t-1)} + \eta f_t(x_i)$$

*Di mana:*
* $\hat{y}_i^{(t)}$: Prediksi gabungan setelah ditambahkan pohon baru ke-$t$.
* $\hat{y}_i^{(t-1)}$: Prediksi akumulatif dari langkah sebelumnya.
* $f_t(x_i)$: Pohon baru yang sedang dilatih pada langkah $t$.
* $\eta$ (eta): *Learning rate* atau *shrinkage* (biasanya bernilai $0.01$ s.d. $0.3$). Parameter ini kudu disetel kecil agar kontribusi setiap pohon tidak terlalu agresif, sehingga model belajar dengan stabil.

Tujuan utama kita di setiap langkah $t$ adalah meminimalkan fungsi kerugian (*loss function*) total:

$$\mathcal{L}^{(t)} = \sum_{i=1}^{n} l\left(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \Omega(f_t)$$

Di sini, $l$ adalah fungsi loss (misalnya MSE), dan $\Omega(f_t)$ adalah penalti regularisasi agar pohon baru tidak tumbuh terlalu kompleks (kita bahas ini di bab berikutnya!).

### Walkthrough: Contoh Kasus Sederhana Regresi Sisa

> [!EXAMPLE]
> **Simulasi Angka Tebakan AQI:**
> Bayangkan kita punya dataset super mini berisi 3 data hari dengan target AQI asli ($y$) sebagai berikut:
> * Hari 1: $y_1 = 40$ (Sehat)
> * Hari 2: $y_2 = 65$ (Sedang)
> * Hari 3: $y_3 = 90$ (Mulai Buruk)
> 
> **Langkah 0: Inisialisasi Prediksi Awal**
> Kita mulai dengan prediksi baseline konstan, misalnya rata-rata nilai AQI:
> $$\hat{y}_1^{(0)} = 65, \quad \hat{y}_2^{(0)} = 65, \quad \hat{y}_3^{(0)} = 65$$
> 
> Mari kita hitung residual awal (error sisa) yaitu $r_i^{(0)} = y_i - \hat{y}_i^{(0)}$:
> * Hari 1: $r_1^{(0)} = 40 - 65 = -25$
> * Hari 2: $r_2^{(0)} = 65 - 65 = 0$
> * Hari 3: $r_3^{(0)} = 90 - 65 = +25$
> 
> **Langkah 1: Latih Pohon Pertama ($f_1$)**
> Kita latih Decision Tree pertama ($f_1$) **bukan** untuk memprediksi $y = [40, 65, 90]$, melainkan untuk memprediksi target residual $r^{(0)} = [-25, 0, 25]$.
> 
> Katakanlah pohon $f_1$ membagi data dan menghasilkan prediksi residual berikut:
> * Hari 1: $f_1(x_1) = -12.5$
> * Hari 2: $f_1(x_2) = -12.5$
> * Hari 3: $f_1(x_3) = 25.0$
> 
> Kita perbarui prediksi model menggunakan *learning rate* $\eta = 0.3$:
> $$\hat{y}_i^{(1)} = \hat{y}_i^{(0)} + 0.3 \times f_1(x_i)$$
> * Hari 1: $\hat{y}_1^{(1)} = 65 + 0.3(-12.5) = 61.25$
> * Hari 2: $\hat{y}_2^{(1)} = 65 + 0.3(-12.5) = 61.25$
> * Hari 3: $\hat{y}_3^{(1)} = 65 + 0.3(25.0) = 72.50$
> 
> **Langkah 2: Hitung Residual Baru ($r_i^{(1)}$)**
> Mari kita cek sisa error setelah pohon pertama bekerja:
> * Hari 1: $r_1^{(1)} = 40 - 61.25 = -21.25$
> * Hari 2: $r_2^{(1)} = 65 - 61.25 = 3.75$
> * Hari 3: $r_3^{(1)} = 90 - 72.50 = 17.50$
> 
> Ceki-ceki deh! Error sisanya sudah menyusut dibanding langkah awal (Hari 1 dari $-25$ jadi $-21.25$, Hari 3 dari $25$ jadi $17.50$). Selanjutnya, pohon kedua ($f_2$) akan dilatih untuk memprediksi residual baru $[-21.25, 3.75, 17.50]$ ini. Proses ini berulang terus sampai ratusan pohon!

---

## Bab 3: Mengapa XGBoost Disebut "Extreme"?

Gradient Boosting biasa sudah ada sejak lama, tapi **XGBoost (Extreme Gradient Boosting)** memodifikasinya menjadi jauh lebih cepat dan kuat. Huruf *"Extreme"* disematkan karena algoritma ini dirancang dengan optimasi sistem tingkat dewa dan penambahan fungsi matematika yang cerdas.

### 1. Fungsi Regularisasi Formal
Salah satu alasan utama XGBoost sangat unggul adalah karena ia memasukkan unsur penalti kompleksitas pohon secara langsung ke dalam fungsi tujuannya. Penalti ini dirumuskan sebagai:

$$\Omega(f_t) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^{T} w_j^2 + \alpha \sum_{j=1}^{T} |w_j|$$

*Di mana:*
* $T$: Jumlah daun (*leaves*) pada pohon. Penalti $\gamma T$ mencegah pohon tumbuh terlalu rimbun/dalam.
* $w_j$: Nilai prediksi (bobot) pada daun ke-$j$.
* $\lambda$ (L2 regularization): Parameter penalti kuadrat bobot (seperti pada Ridge Regression). Mencegah nilai prediksi daun terlalu ekstrem.
* $\alpha$ (L1 regularization): Parameter penalti nilai mutlak bobot (seperti pada Lasso Regression).

### 2. Ekspansi Taylor untuk Optimasi Cepat
XGBoost menggunakan pendekatan deret Taylor hingga orde kedua untuk mendekati fungsi loss secara cepat tanpa peduli fungsi loss apa yang kita pakai (asal bisa diturunkan). 

Fungsi loss pada langkah $t$ didekati dengan:

$$\mathcal{L}^{(t)} \approx \sum_{i=1}^{n} \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \Omega(f_t)$$

Di mana $g_i$ (gradient) dan $h_i$ (hessian) adalah turunan pertama dan kedua dari fungsi loss terhadap prediksi sebelumnya:

$$g_i = \frac{\partial l(y_i, \hat{y}_i^{(t-1)})}{\partial \hat{y}_i^{(t-1)}} \quad \text{dan} \quad h_i = \frac{\partial^2 l(y_i, \hat{y}_i^{(t-1)})}{\partial (\hat{y}_i^{(t-1)})^2}$$

Dengan rumus ini, XGBoost bisa menentukan skor kualitas struktur suatu daun node ($S$) secara analitis tanpa harus melakukan iterasi uji coba yang lambat:

$$S = \frac{\left( \sum_{i \in I} g_i \right)^2}{\sum_{i \in I} h_i + \lambda}$$

Dan nilai peningkatan kualitas pemisahan (*Gain*) ketika sebuah node dibagi menjadi cabang kiri ($I_L$) dan kanan ($I_R$) dirumuskan dengan sangat elegan:

$$\text{Gain} = \frac{1}{2} \left[ \frac{\left( \sum_{i \in I_L} g_i \right)^2}{\sum_{i \in I_L} h_i + \lambda} + \frac{\left( \sum_{i \in I_R} g_i \right)^2}{\sum_{i \in I_R} h_i + \lambda} - \frac{\left( \sum_{i \in I} g_i \right)^2}{\sum_{i \in I} h_i + \lambda} \right] - \gamma$$

Jika nilai $\text{Gain}$ ini negatif (atau lebih kecil dari $\gamma$), XGBoost bakal memutuskan untuk **tidak melakukan pemisahan** pada node tersebut. Ini adalah pertahanan otomatis pertama terhadap overfitting!

---

## Bab 4: Bahaya Overfitting pada Dataset Kecil

Meskipun XGBoost dibekali dengan regularisasi yang canggih, algoritma ini tetap menyimpan satu kelemahan fatal: **sangat rentan mengalami overfitting pada dataset berukuran kecil**.

> [!WARNING]
> **Jebakan Overfitting:**
> *Overfitting* terjadi ketika model terlalu fokus menghafal detail-detail kecil dan *noise* (gangguan/anomali) pada data latihan (*training set*), sehingga ia gagal memahami pola umum yang sesungguhnya. Akibatnya, performa model saat diuji dengan data baru (*testing set*) bakal anjlok drastis.

### Kenapa XGBoost Gampang Overfitting di Data Kecil?

1. **Kapasitas Model yang Terlalu Tinggi (High Capacity):**
   XGBoost memiliki parameter pemisahan yang sangat fleksibel. Dengan menggabungkan ratusan pohon keputusan yang masing-masing bisa memotong ruang data berkali-kali, model ini bisa dengan mudah membuat batas keputusan yang super rumit demi meminimalkan error data latih hingga nol.
   
2. **Ketiadaan Data yang Cukup untuk Generalisasi:**
   Jika kita memiliki dataset berukuran kecil (seperti data cuaca Jakarta kita yang hanya sekitar $731$ baris di [[../Air_Quality_Prediction_MLR_Complete_Guide|Panduan Lengkap MLR]]), variasi pola cuaca ekstrem tidak terwakili dengan cukup. XGBoost akan menganggap pencilan kecil (*outliers*) sebagai aturan umum yang mutlak.
   
3. **Kekuatan Algoritma Sederhana:**
   Pada dataset kecil yang polanya cenderung linear, model sederhana seperti regresi linear berganda (MLR) justru jauh lebih tangguh karena keterbatasan kapasitasnya bertindak sebagai pencegah alami overfitting. MLR hanya menarik satu garis lurus rata-rata, sehingga ia tidak akan terganggu oleh riak-riak kecil *noise* data.

### Cara Menjinakkan Overfitting pada XGBoost

Jika kamu terpaksa harus menggunakan XGBoost pada dataset berukuran kecil, pastikan kamu melakukan langkah-langkah penyelamatan berikut:

* **Batasi Kedalaman Pohon (`max_depth`):** 
  Sret nilai `max_depth` ke angka kecil (misalnya $2$ atau $3$). Ini membatasi jumlah cabang pohon agar tidak membuat aturan yang terlalu spesifik.
* **Gunakan Subsampling (`subsample` & `colsample_bytree`):**
  Setel parameter ini di rentang $0.5$ s.d. $0.8$. Artinya, setiap pohon hanya dilatih menggunakan sebagian baris data dan sebagian kolom fitur acak. Ini memaksa pohon untuk tidak terlalu bergantung pada fitur atau baris data tertentu.
* **Tingkatkan Regularisasi L2 (`lambda`) dan L1 (`alpha`):**
  Perbesar nilai $\lambda$ dan $\alpha$ untuk menekan nilai prediksi di daun agar lebih konservatif dekat dengan nol.
* **Kecilkan Learning Rate (`learning_rate` / `eta`):**
  Setel `learning_rate` sangat kecil (misal $0.01$ s.d. $0.05$) dibarengi dengan mekanisme **Early Stopping** (berhenti latihan jika error pada data validasi tidak turun dalam beberapa iterasi).

---

## Ringkasan Materi

* **Decision Tree** bekerja dengan membagi ruang data berdasarkan fitur terpilih yang meminimalkan variansi (error) di setiap daun cabang.
* **Boosting** melatih pohon-pohon keputusan secara sekuensial, di mana tiap pohon baru ditugaskan untuk menebak *residual error* dari kombinasi pohon sebelumnya.
* **XGBoost** membawa konsep boosting ke level ekstrem dengan optimasi deret Taylor orde dua dan menyematkan parameter regularisasi L1/L2 ($\alpha, \lambda$) secara langsung ke dalam fungsi tujuan.
* **Data Kecil** adalah musuh utama XGBoost. Tanpa penyetelan hyperparameter yang ketat, model ini bakal mengalami *overfitting* parah karena menghafal *noise* data latihan. Dalam skenario data terbatas, model linear sederhana sering kali menjadi pemenangnya.

Semoga catatan belajar ini ngebantu kita makin paham tentang dinamika algoritma non-linear, gaes! Sampai jumpa di topik seru AI lainnya!
