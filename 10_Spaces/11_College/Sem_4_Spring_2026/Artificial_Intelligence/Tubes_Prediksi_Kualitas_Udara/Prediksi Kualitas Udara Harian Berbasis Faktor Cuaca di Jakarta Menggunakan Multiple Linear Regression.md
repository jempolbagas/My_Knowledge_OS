---
title: "Prediksi Kualitas Udara Harian Berbasis Faktor Cuaca di Jakarta Menggunakan Multiple Linear Regression"
course: "Artificial Intelligence"
tags:
  - college/assignment
  - artificial-intelligence
  - machine-learning
  - multiple-linear-regression
aliases:
  - Tubes AI - Prediksi Kualitas Udara Jakarta
created: 2026-07-01
---

# Prediksi Kualitas Udara Harian Berbasis Faktor Cuaca di Jakarta Menggunakan Multiple Linear Regression

---

**Disusun oleh:**

| Nama                        | NIM      |
| :-------------------------- | :------- |
| Bagas Aditama Suryo Nugroho | L0124042 |
| Raditya Adi Pradana         | L0124070 |
| Syaikhasril Maulana Firdaus | L0124077 |

**PROGRAM STUDI INFORMATIKA** 
**FAKULTAS TEKNOLOGI INFORMASI DAN SAINS DATA** 
**UNIVERSITAS SEBELAS MARET** **2026**

---

## ABSTRAK

Prediksi kualitas udara merupakan aspek krusial dalam manajemen lingkungan perkotaan. Penelitian ini bertujuan untuk membangun model *Machine Learning* yang mampu memprediksi *Air Quality Index* (AQI) harian berdasarkan parameter cuaca, sekaligus mengevaluasi dampak kebaruan data (*data recency*) terhadap akurasi prediksi. Pengujian komparatif dilakukan menggunakan dua rentang waktu data dari satelit Open-Meteo, yaitu data historis (2021-2025) dan data terbaru (2024-2025). Tiga algoritma diuji secara bersamaan yaitu *Multiple Linear Regression* (MLR), *Support Vector Regression* (SVR), dan *Extreme Gradient Boosting* (XGBoost).

Hasil penelitian menunjukkan bahwa penggunaan dataset terbaru (2024-2025) menghasilkan performa yang lebih baik dengan menghindari anomali *concept drift* akibat masa pandemi. Pada tahap evaluasi, MLR terbukti menjadi model paling optimal dengan tingkat kesalahan absolut rata-rata (MAE) terendah sebesar 10.45 dan akurasi pola ($R\text{-Squared}$) tertinggi sebesar 0.72, mengungguli model kompleks lainnya. Sebagai implementasi akhir, model MLR dioperasionalkan secara publik melalui arsitektur *microservices*, yang mengintegrasikan backend REST API berbasis FastAPI di server Render dengan antarmuka frontend Next.js di infrastruktur Vercel. Pemisahan beban komputasi ini berhasil menghasilkan ekosistem aplikasi prakiraan kualitas udara yang responsif, berkinerja tinggi, dan terukur.

**Kata-kata kunci:** *Air Quality Index, Machine Learning, Multiple Linear Regression*

---

## 1. PENDAHULUAN

Pencemaran udara merupakan masalah lingkungan global yang serius dan berdampak buruk bagi kesehatan masyarakat serta lingkungan (Anggraini et al., 2025). Menurut laporan *World Health Organization* (WHO) pada tahun 2019, polusi udara menyumbang sekitar 4,2 juta kematian dini di seluruh dunia setiap tahunnya (Faldo et al., 2025). Jakarta, sebagai ibu kota Indonesia, secara konsisten menempati peringkat sebagai salah satu kota dengan tingkat polusi udara tertinggi di dunia, bahkan tercatat memiliki *Air Quality Index* (AQI) tertinggi kelima secara global pada Agustus 2023 (Faldo et al., 2025). Tingginya tingkat polusi ini didorong oleh aktivitas transportasi komuter, emisi industri, dan pertumbuhan penduduk perkotaan yang masif (Angraini et al., 2025; Faldo et al., 2025; Persis & Amar, 2022; Singh & Suthar, 2024). Kondisi yang membahayakan kesehatan ini menjadikan ketersediaan instrumen informasi prediksi kualitas udara sangat esensial untuk mendukung sistem peringaran dini, pengelolaan, dan pengambilan keputusan mitigasi yang efektif (Faldo et al., 2025; Persis & Amar, 2022; Singh & Suthar, 2024).

Kualitas udara di suatu wilayah tidak hanya bergantung pada keberadaan sumber emisi polutan, tetapi juga dipengaruhi secara signifikan oleh faktor meteorologi atau cuaca secara simultan (Anggraini et al., 2025; Bose & Chowdhury, 2023). Berbagai parameter cuaca seperti suhu udara, kelembaban relatif, kecepatan angin, tekanan udara, dan curah hujan memiliki korelasi yang erat terhadap proses pembentukan, dispersi, dan akumulasi partikel polutan di atmosfer (Anggraini et al., 2025; Bose & Chowdhury, 2023; Saiohai et al., 2023). Sebagai contoh, tingginya kecepatan dan pergerakan arah angin sangat menentukan sejauh mana polusi tersebar dari sumbernya, sementara intensitas curah hujan dapat memicu pencucian atau pelarutan polutan di udara (Anggraini et al., 2025; Bose & Chowdhury, 2023). Oleh karena itu, mengintegrasikan multi-parameter meteorologi sebagai variabel independen sangat krusial untuk dibangunnya model prakiraan kualitas udara harian yang representatif (Anggraini et al., 2025; Singh & Suthar, 2024).

Dalam beberapa tahun terakhir, penerapan algoritma *Machine Learning* untuk memprediksi kualitas udara telah menunjukkan kinerja komputasi yang sangat menjanjikan dan dipercaya secara luas. Berbagai studi terdahulu telah berhasil mencoba memprediksi kualitas udara dan elemen polutan menggunakan metode seperti *Artificial Neural Network* (ANN), *Support Vector Machine* (SVM), *Random Forest* (RF), dan *Decision Tree* dengan capaian tingkat akurasi yang baik (Faldo et al., 2025; Persis & Amar, 2022; Singh & Suthar, 2024). Namun, model-model kompleks (*black-box*) semacam itu umumnya menuntut proses pelatihan komputasi yang memakan waktu lama (Persis & Amar, 2022), serta struktur arsitekturnya menyulitkan pengguna awam untuk menginterpretasikan dan memahami bobot pengaruh dari setiap parameter cuaca secara lugas (Al-Saeedi et al., 2026). Di sisi lain, pemodelan berbasis regresi seperti *Linear Regression* menawarkan penyederhanaan beban komputasi, kejelasan implementasi arsitektur, serta kemudahan bagi peneliti untuk mengekstraksi dan membaca korelasi linier antar parameter (Al-Saeedi et al., 2026; Singh & Suthar, 2024).

Meskipun telah banyak model prediksi cerdas dikembangkan, sebagian besar riset terdahulu masih memiliki keterbatasan pada aspek kebaruan dan kelengkapan dataset. Sebagai contoh, pembatasan cakupan training hanya pada rentang tahun 2020 hingga 2021 memaksa model-model sebelumnya untuk sepenuhnya menghilangkan parameter polutan yang sangat krusial seperti PM2.5 demi menjaga keseragaman data, yang pada akhirnya mengurangi komprehensivitas informasi yang diekstrak dari analisis (Faldo et al., 2025). Pada periode tersebut, kebijakan pembatasan aktivitas sosial (*lockdown*) akibat pandemi COVID-19 diberlakukan secara masif dan secara langsung memutus sumber utama emisi gas buang. Penghentian aktivitas operasional industri serta penurunan drastis dalam penggunaan kendaraan bermotor ini memicu fenomena penurunan konsentrasi PM10 serta PM2.5 secara rata-rata masing-masing sebesar 27% dan 50%, melahirkan perbaikan kualitas udara sementara yang secara fundamental tidak wajar (Li & Li, 2023; Persis & Amar, 2022).

Pemanfaatan data anomali historis dari masa pandemi ini untuk memprediksi kondisi Jakarta pasca-pandemi terbukti memicu fenomena *concept drift* atau pergeseran distribusi (*distribution drift*) (Vashney et al., 2022; Xie & Tummala, 2025). Hal ini merugikan karena metode *machine learning* tradisional sangat bergantung pada asumsi bahwa data *training* dan data *testing* harus memiliki distribusi yang serupa, sementara kebijakan *lockdown* menghasilkan perbedaan distribusi yang sangat signifikan dan kondisi non stasioner yang tidak lagi relevan dengan dinamika lalu lintas normal (Varshney et al., 2022; Xie & Tummala, 2025). Akibatnya, fluktuasi data masa pandemi tersebut masuk ke dalam perhitungan matematis algoritma sebagai *noise* anomali yang mengganggu logika adaptasi model (Li & Li, 2023; Zhao, Wu, et al., 2023). Tanpa adanya penyesuaian matematis khusus untuk menghilangkan efek *lockdown* jangka pendek dan mengungkap tren utamanya, anomali ini akan sangat mendegradasi performa dan akurasi prediksi model secara keseluruhan (Li & Li, 2023; Zhao, Wu, et al., 2023).

Untuk mengatasi tantangan dan celah penelitian tersebut, penelitian ini bertujuan membangun model prediksi AQI harian di Jakarta dengan mengadopsi pendekatan *Multiple Linear Regression* (MLR) berbasis tujuh parameter cuaca secara simultan. Fokus eksplorasi pada riset ini ditekankan pada evaluasi prinsip kebaruan data (*data recency*) melalui perbandingan performa antara pengolahan data rentang waktu historis panjang (2021-2025) melawan data terbaru (2024-2025) demi membuktikan pengaruh anomali pandemi. Model MLR juga akan diuji secara kompetitif (*benchmarking*) dengan algoritma kompleks yang populer, yaitu *Support Vector Regression* (SVR) dan *Extreme Gradient Boosting* (XGBoost). MLR diproyeksikan sebagai solusi paling optimal berdasarkan premis bahwa parameter cuaca memiliki hubungan yang sangat linier terhadap polusi. Model yang lebih sederhana ini ditujukan untuk mencegah masalah *overfitting* yang sering dijumpai pada algoritma kompleks seperti XGBoost, sehingga mampu melahirkan ekosistem perangkat lunak prediksi polusi udara yang *scalable*, responsif, dan ringan secara operasional.

---

## 2. METODE PENELITIAN

### 2.1 Pendekatan Penelitian
Penelitian ini menggunakan pendekatan kuantitatif dengan menerapkan metode *Multiple Linear Regression* untuk memprediksi kualitas udara harian di Jakarta berdasarkan faktor-faktor cuaca. Metode ini dipilih karena mampu menganalisis hubungan antara satu variabel dependen dengan beberapa variabel independen secara simultan serta menghasilkan model yang mudah diinterpretasikan.

### 2.2 Tahapan Penelitian
Tahapan penelitian yang dilakukan terdiri dari beberapa langkah, yaitu pengumpulan data, *preprocessing* data, eksplorasi data, pembangunan model, serta evaluasi model.

#### 2.2.1 Pengumpulan Data
Data yang digunakan merupakan data historis kualitas udara dan data cuaca harian di Jakarta yang diperoleh dari website https://www.aqi.in dan https://open-meteo.com. Variabel dependen pada penelitian ini adalah *Air Quality Index* (AQI) harian, sedangkan variabel independen berupa tujuh parameter cuaca. Data yang digunakan meliputi:
* Suhu udara rata-rata (°C)
* Kelembaban relatif rata-rata (%)
* Kecepatan angin rata-rata pada ketinggian 10 m (m/s)
* Tekanan udara permukaan rata-rata (hPa)
* Total curah hujan (mm)
* Tutupan awan rata-rata (%)
* Total radiasi gelombang pendek ($\text{MJ/m}^2$)

#### 2.2.2 Preprocessing Data
Tahap *preprocessing* dilakukan untuk meningkatkan kualitas data sebelum digunakan dalam proses pelatihan model. Langkah-langkah *preprocessing* meliputi:
* Menghapus data duplikat.
* Menangani *missing value* menggunakan metode imputasi atau penghapusan data.
* Memeriksa dan menangani *outlier*.
* Menyesuaikan format data agar siap digunakan dalam analisis.
* Memisahkan variabel independen dan variabel dependen.

**Variabel Independen (X):**
* Suhu udara rata-rata (°C)
* Kelembaban relatif rata-rata (%)
* Kecepatan angin rata-rata pada ketinggian 10 m (m/s)
* Tekanan udara permukaan rata-rata (hPa)
* Total curah hujan (mm)
* Tutupan awan rata-rata (%)
* Total radiasi gelombang pendek ($\text{MJ/m}^2$)

**Variabel Dependen (Y):**
* AQI (*Air Quality Index*)

#### 2.2.3 Analisis Data Eksploratif
Analisis data eksploratif dilakukan untuk memahami karakteristik data serta hubungan antar variabel. Aktivitas yang dilakukan antara lain:
* Analisis statistik deskriptif.
* Visualisasi distribusi data.
* Analisis korelasi antar variabel.
* Identifikasi pola hubungan antara faktor cuaca dan AQI.

#### 2.2.4 Pembangunan Model
Pada tahap ini dilakukan pembangunan model prediksi menggunakan *Multiple Linear Regression*. Model regresi linear berganda dinyatakan sebagai:

$$\text{AQI} = \beta_0 + \beta_1\text{RH} + \beta_2\text{P} + \beta_3\text{T} + \beta_4\text{WS} + \beta_5\text{SP} + \beta_6\text{CC} + \beta_7\text{SR} + \epsilon$$

**Keterangan:**
* $\text{AQI}$: Nilai *Air Quality Index* (variabel dependen)
* $\text{RH}$: *Relative Humidity* (kelembaban relatif rata-rata)
* $\text{P}$: *Precipitation* (total curah hujan)
* $\text{T}$: *Temperature* (suhu rata-rata)
* $\text{WS}$: *Wind Speed* (kecepatan angin rata-rata)
* $\text{SP}$: *Surface Pressure* (tekanan udara permukaan rata-rata)
* $\text{CC}$: *Cloud Cover* (tutupan awan rata-rata)
* $\text{SR}$: *Shortwave Radiation* (total radiasi gelombang pendek)
* $\beta_0$: Konstanta
* $\beta_1 \dots \beta_7$: Koefisien regresi
* $\epsilon$: *Error* atau residual

Model dilatih menggunakan data historis cuaca dan kualitas udara harian Jakarta. Data kemudian dibagi menjadi data latih (80%) and data uji (20%) untuk mengukur kemampuan generalisasi model terhadap data yang belum pernah dilihat sebelumnya.

#### 2.2.5 Evaluasi Model
Setelah model dibangun, dilakukan evaluasi untuk mengukur kinerja prediksi. Metrik evaluasi yang digunakan meliputi:

| No | Metrik Evaluasi | Rumus |
| :--- | :--- | :--- |
| 1. | *Mean Absolute Error* (MAE) | $\text{MAE} = \frac{1}{n}\sum_{i=1}^{n} \lvert y_i - \hat{y}_i \rvert$ |
| 2. | *Root Mean Squared Error* (RMSE) | $\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$ |
| 3. | *Mean Absolute Percentage Error* (MAPE) | $\text{MAPE} = \frac{100\%}{n}\sum_{i=1}^{n}\lvert \frac{y_i - \hat{y}_i}{y_i} \vert$ |
| 4. | Koefisien Determinasi ($R^2$) | $R^2 = 1 - \frac{\Sigma(y_i - \hat{y}_i)^2}{\Sigma(y_i - \bar{y})^2}$ |

---

## 3. HASIL DAN PEMBAHASAN

### 3.1 Eksplorasi dan Pra-Pemrosesan Data
Tahap pra-pemrosesan data merupakan fondasi krusial dalam alur kerja *Machine Learning* untuk memastikan bahwa dataset yang akan dilatih ke dalam algoritma telah terstruktur, bersih, dan memiliki format matematis yang sesuai. Proses ini mencakup ekstraksi data mentah, transformasi deret waktu, analisis distribusi visual, hingga penyesuaian skala fitur (*feature scaling*).

#### 3.1.1 Penarikan Data (Data Extraction)
Dataset yang digunakan dalam penelitian ini bersumber dari satelit meteorologi Open-Meteo API dan *scraping* data dari website aqi.in. Penarikan data mencakup variabel cuaca harian dan Indeks Standar Pencemar Udara (ISPU) di wilayah Jakarta dengan rentang waktu pengambilan dimulai dari 1 Januari 2024 hingga 31 Desember 2025. Dari proses ekstraksi ini, diperoleh dataset mentah dengan total 732 baris data harian. Cuplikan dari dataset mentah tersebut disajikan pada Tabel 3.1.

**Tabel 3.1 Cuplikan Dataset Mentah**

| Tanggal | AQI | Kelembapan (%) | Curah Hujan (mm) | Suhu (°C) | Kec. Angin (m/s) | Tekanan (hPa) | Awan (%) | Radiasi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2024-01-01 | 92 | 85,77 | 12,3 | 26,98 | 5,42 | 1008,18 | 99,83 | 17,54 |
| 2024-01-02 | 78 | 83,81 | 8 | 27,30 | 6,03 | 1007,25 | 99,41 | 18,07 |
| 2024-01-03 | 86 | 89,81 | 26,19 | 25,95 | 6,99 | 1007,84 | 98,25 | 8,5 |

#### 3.1.2 Transformasi Deret Waktu (Time-Series Shifting)
Mengingat tujuan dari model yang dibangun adalah untuk melakukan prakiraan (prediksi H+1), fitur cuaca pada hari ini tidak dapat digunakan untuk memprediksi AQI pada hari yang sama. Oleh karena itu, dilakukan transformasi pergeseran nilai (*shifting*) pada kolom target AQI. Variabel target digeser naik sebanyak satu indeks sehingga parameter cuaca hari ini akan sejajar dengan nilai polusi keesokan harinya. Proses *shifting* ini mengakibatkan baris data terakhir pada dataset kehilangan pasangan targetnya, sehingga baris tersebut dihapus. Ilustrasi pergeseran variabel target ini ditunjukkan pada Tabel 3.2, di mana terlihat fitur cuaca sejajar dengan target nilai AQI pada hari berikutnya.

**Tabel 3.2 Ilustrasi Pergeseran Variabel**

| Tanggal | Suhu (t) | Curah Hujan (t) | AQI Awal | Target AQI (t+1) | Keterangan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2024-01-01 | 26,98 | 12,30 | 92 | 78 | Mengambil AQI 2 Jan |
| 2024-01-02 | 27,30 | 8,00 | 78 | 86 | Mengambil AQI 3 Jan |
| 2024-01-03 | 25,95 | 26,19 | 86 | 58 | Mengambil AQI 4 Jan |
| 2025-12-31 | 25,44 | 31,3 | 56 | NaN | Baris dihapus |

#### 3.1.3 Analisis Distribusi dan Pembersihan Anomali
Sebelum data dipisahkan, dilakukan analisis visual untuk meninjau distribusi atau sebaran angka dari masing-masing parameter menggunakan grafik histogram. Langkah ini bertujuan untuk mengidentifikasi keberadaan *outlier* (pencilan data ekstrim) serta melihat kecenderungan kurva normal atau kemiringan (*skewness*) yang merupakan representasi karakteristik alam. Berdasarkan pengujian batasan anomali ekstrem ($\text{AQI} > 300$), tidak ditemukan *outlier* yang melampaui batas tersebut pada rentang tahun 2024-2025. Setelah dikurangi satu baris akibat proses *shifting*, total data bersih yang tervalidasi dan siap digunakan untuk tahap selanjutnya adalah 731 baris data. Hasil visualisasi distribusi dari seluruh fitur dapat dilihat pada Gambar 3.1.

![Gambar 3.1 Visualisasi Distribusi Variabel Cuaca](Gambar%203.1.png)

*(Gambar 3.1 Visualisasi Distribusi Variabel Cuaca)*

Berdasarkan Gambar 3.1, dapat diamati bahwa beberapa parameter membentuk kurva normal yang simetris, sedangkan parameter lain seperti curah hujan atau tutupan awan memiliki distribusi yang miring, yang merupakan wujud wajar dari karakteristik iklim di wilayah penelitian.

#### 3.1.4 Analisis Korelasi dan Uji Multikolinearitas
Sebelum fitur-fitur cuaca diumpankan ke dalam model *Multiple Linear Regression* (MLR), perlu dilakukan pengujian asumsi klasik, salah satunya adalah uji multikolinearitas. Multikolinearitas terjadi ketika terdapat korelasi linier yang terlalu kuat (umumnya di atas 0,80 atau di bawah -0,80) antar sesama variabel independen. Hal ini dapat menyebabkan koefisien regresi menjadi tidak stabil dan bias. Untuk mengevaluasi hal tersebut, dilakukan perhitungan matriks korelasi Pearson yang divisualisasikan melalui *heatmap* pada Gambar 3.2.

![Gambar 3.2 Heatmap Korelasi Antar Variabel Cuaca](Gambar%203.2.png)

*(Gambar 3.2 Heatmap Korelasi Antar Variabel Cuaca)*

Berdasarkan matriks korelasi pada Gambar 3.2, dapat diamati bahwa nilai korelasi antar variabel independen cuaca secara keseluruhan berada pada batas aman. Korelasi tertinggi antar fitur independen terjadi antara suhu udara rata-rata (*temperature_2m_mean*) dan kelembaban relatif (*relative_humidity_2m_mean*) dengan nilai koefisien sebesar -0,75. Meskipun menunjukkan korelasi negatif yang cukup kuat di mana peningkatan suhu diikuti oleh penurunan kelembaban, nilai absolutnya masih berada di bawah ambang batas kritis 0,80.

Oleh karena itu, dapat disimpulkan bahwa tidak terdapat masalah multikolinearitas yang ekstrem pada dataset ini. Asumsi dasar algoritma regresi linier telah terpenuhi, sehingga seluruh ketujuh parameter cuaca dapat dipertahankan sebagai fitur prediksi tanpa perlu melakukan reduksi dimensi. Selain itu, variabel kecepatan angin (*wind_speed*) dan tutupan awan (*cloud_cover*) menunjukkan korelasi negatif tertinggi terhadap target AQI_Besok (masing-masing -0,38 dan -0,31), yang mengindikasikan bahwa tiupan angin dan cuaca mendung berperan cukup signifikan dalam menurunkan angka polusi keesokan harinya.

#### 3.1.5 Penyesuaian Skala Fitur (Feature Scaling)
Algoritma Regresi Linier melakukan perhitungan bobot matematika berdasarkan metrik jarak dan magnitudo angka. Untuk mencegah parameter bersatuan besar (seperti tekanan udara) mendominasi parameter bersatuan kecil (seperti curah hujan), diterapkan teknik *Standardization* (Z-Score Scaling). Teknik ini mengubah seluruh rentang data mentah sehingga memiliki nilai rata-rata 0 dan standar deviasi 1, yang direpresentasikan dengan persamaan matematis berikut:

$$Z = \frac{x - \mu}{\sigma}$$

*(Keterangan: $x$ adalah nilai observasi, $\mu$ adalah nilai rata-rata, dan $\sigma$ adalah standar deviasi).*

![Gambar 3.3 Visualisasi Standarisasi Variabel Cuaca](Gambar%203.3.png)

*(Gambar 3.3 Visualisasi Standarisasi Variabel Cuaca)*

Penerapan `StandardScaler` menghasilkan matriks fitur baru yang telah dinormalisasi ke dalam skala komputasi yang seragam. Dataset inilah yang secara final diberikan ke dalam fase pelatihan model *Machine Learning*.

### 3.2 Analisis Perbandingan Time Frame Dataset
Kualitas dan relevansi data memegang peranan vital dalam pemodelan deret waktu (*time-series*). Umumnya, penambahan kuantitas data latih diasumsikan berbanding lurus dengan peningkatan akurasi model *Machine Learning*. Untuk membuktikan hipotesis tersebut pada kasus kualitas udara, dilakukan eksperimen komparatif yang mengevaluasi performa model menggunakan dua rentang waktu (*time frame*) dataset yang berbeda, yakni rentang waktu panjang (2021-2025) dan rentang waktu pendek yang lebih mutakhir (2024-2025).

#### 3.2.1 Skenario Pemisahan Data (Data Splitting)
Eksperimen ini menggunakan proporsi pembagian data standar untuk memisahkan data latih (*training set*) dan data uji (*testing set*). Berdasarkan ekstraksi data, diperoleh dua skenario pengujian sebagai berikut:
* **a. Skenario Historis Panjang (2021-2025):** Menggunakan total dataset yang dialokasikan menjadi 1.418 baris sebagai data latih dan 355 baris sebagai data uji.
* **b. Skenario Pendek (2024-2025):** Menggunakan subset data yang lebih baru, di mana 584 baris dialokasikan sebagai data latih dan 146 baris sebagai data uji.

#### 3.2.2 Hasil Evaluasi Kinerja Komparatif
Kedua dataset tersebut kemudian diumpankan pada algoritma regresi yang sama untuk diukur tingkat kesalahannya menggunakan metrik *Mean Absolute Error* (MAE), *Root Mean Squared Error* (RMSE), *Mean Absolute Percentage Error* (MAPE), dan *R-squared* ($R^2$). Perbandingan hasil pengujian kedua *time frame* tersebut dapat dilihat pada Tabel 3.3.

**Tabel 3.3 Perbandingan Hasil Pengujian Time Frame**

| Time Frame | MAE | RMSE | MAPE | $R^2$ |
| :--- | :--- | :--- | :--- | :--- |
| 2021-2025 | 12.94 | 16.66 | 16.27% | 0.62 |
| 2024-2025 | 10.45 | 14.50 | 14.01% | 0.72 |

Berdasarkan Tabel 3.3, pengujian menunjukkan hasil yang berlawanan dengan hipotesis kuantitas data. Model yang dilatih dengan dataset mutakhir (2024-2025) meskipun jumlahnya lebih sedikit, berhasil mencatatkan performa yang jauh lebih bagus dengan skor $R^2$ sebesar 0.72, tingkat kesalahan absolut (MAE) sebesar 10.45 AQI, dan persentase kesalahan (MAPE) sebesar 14.01%. Sebaliknya, ketika model disuplai dengan data historis yang jauh lebih masif (2021-2025), akurasi $R^2$ justru mengalami degradasi menjadi 0.62, disertai dengan peningkatan *error* rata-rata di mana nilai MAE naik menjadi 12.94 AQI dan persentase kesalahan (MAPE) memburuk menjadi 16.27%.

#### 3.2.3 Fenomena Concept Drift dan Data Recency
Penurunan performa model akibat penambahan data historis membuktikan terjadinya fenomena *concept drift* atau pergeseran pola konsep seiring berjalannya waktu. Pola korelasi antara parameter cuaca dan tingkat emisi polutan pada tahun 2021 hingga pertengahan 2022 sangat dipengaruhi oleh anomali pembatasan aktivitas sosial dan industri berskala besar akibat pandemi COVID-19. Pada periode tersebut, kondisi cuaca tertentu (seperti kemarau panjang) tidak selalu diikuti oleh lonjakan polusi akibat minimnya volume kendaraan.

Data anomali masa lalu ini masuk ke dalam perhitungan matematis algoritma sebagai *noise* (gangguan) yang merusak logika prediksi model untuk tata kota masa kini yang aktivitasnya telah kembali normal. Oleh karena itu, eksperimen ini menyimpulkan bahwa dalam pemodelan lingkungan yang sangat dinamis, prinsip kebaruan data (*data recency*) memiliki bobot urgensi yang jauh lebih tinggi dalam menghasilkan prediksi yang akurat dibandingkan dengan memprioritaskan kuantitas data historis.

### 3.3 Benchmarking dan Pemilihan Algoritma
Untuk memastikan bahwa model komputasi yang dikembangkan merupakan solusi paling optimal bagi karakteristik dataset kualitas udara, dilakukan tahapan *benchmarking* atau uji komparasi kinerja algoritma. Algoritma dasar *Multiple Linear Regression* (MLR) dievaluasi secara kompetitif melawan dua algoritma regresi tingkat lanjut yang memiliki arsitektur lebih kompleks, yakni *Support Vector Regression* (SVR) dan *Extreme Gradient Boosting* (XGBoost).

#### 3.3.1 Skenario Pengujian Algoritma
Ketiga model diinisialisasi dan dilatih menggunakan porsi data *training* (2024-2025) yang identik. Untuk memberikan perbandingan yang adil, algoritma kompetitor dikonfigurasi menggunakan parameter dasar yang umum digunakan dalam pemodelan. Model SVR diimplementasikan menggunakan kernel RBF (*Radial Basis Function*) dengan nilai penalti $C=100$, sementara model XGBoost dibangun menggunakan arsitektur *ensemble* berupa 100 pohon keputusan (`n_estimators=100`) dengan laju pembelajaran 0.1.

#### 3.3.2 Hasil Komparasi Performa Model
Setelah proses pelatihan selesai, ketiga model diuji menggunakan data *testing* untuk memprediksi nilai polusi masa depan. Kemampuan prediksi dari masing-masing model dikuantifikasi menggunakan metrik tingkat kesalahan absolut (MAE), Akar Rata-rata Kuadrat Kesalahan (RMSE), Rata-rata Persentase Kesalahan Absolut (MAPE), dan rasio kecocokan pola (*R-Squared*). Hasil evaluasi komparatif dari terminal komputasi dapat dilihat pada Tabel 3.4 dan divisualisasikan pada Gambar 3.4.

**Tabel 3.4 Perbandingan Hasil Evaluasi Model**

| Model Algoritma | MAE | RMSE | MAPE (%) | $R^2$ |
| :--- | :--- | :--- | :--- | :--- |
| **MLR** | **10,45** | **14,50** | **14,01** | **0.72** |
| SVR | 10,97 | 15,27 | 15,11 | 0,69 |
| XGBoost | 10,97 | 15,94 | 14,72 | 0,66 |

![Gambar 3.4 Perbandingan Hasil Evaluasi Model](Gambar%203.4.png)

*(Gambar 3.4 Perbandingan Hasil Evaluasi Model)*

Berdasarkan hasil kalkulasi sistem, algoritma *Multiple Linear Regression* (MLR) terbukti secara konsisten mencatatkan metrik performa komputasi terbaik di seluruh parameter evaluasi. Model regresi dasar ini menghasilkan tingkat kesalahan terendah dengan nilai MAE sebesar 10,45, RMSE sebesar 14,50, dan MAPE di angka 14,01%. Selain itu, MLR juga memimpin pada kemampuan pengenalan pola dengan skor *R-Squared* tertinggi yang mencapai 0,72.

Sebagai pembanding, model komputasi yang lebih kompleks yakni SVR dan XGBoost menunjukkan performa yang berada di bawah MLR. Kedua algoritma tersebut mencatatkan nilai MAE yang identik sebesar 10,97. Jika ditinjau lebih dalam, SVR menunjukkan stabilitas yang sedikit lebih baik dalam menangani *error* kuadratik ($\text{RMSE } 15,27$) dan akurasi pola ($R^2 \text{ } 0,69$) dibandingkan XGBoost ($\text{RMSE } 15,94$ dan $R^2 \text{ } 0,66$). Di sisi lain, XGBoost memiliki persentase kesalahan relatif (MAPE) sebesar 14,72%, yang menjadikannya sedikit lebih akurat secara persentase dibandingkan SVR (15,11%). Secara keseluruhan, evaluasi ini menegaskan bahwa pendekatan linier sederhana (MLR) adalah model yang paling optimal untuk mengurai pola dataset kualitas udara ini.

#### 3.3.3 Justifikasi Pemilihan Model Final
Kemenangan MLR atas algoritma yang jauh lebih kompleks (SVR dan XGBoost) memberikan wawasan krusial mengenai struktur dataset. Hasil ini membuktikan bahwa hubungan kausalitas antara parameter meteorologi (suhu, kelembaban, angin) dengan pergerakan polusi udara di wilayah penelitian memiliki tendensi yang sangat linier.

Ketika dihadapkan pada pola data linier, algoritma kompleks seperti XGBoost yang berbasis *decision tree* rentan mengalami fenomena *overfitting* atau kesulitan menggeneralisasi pola (*overthinking*), yang berakibat pada penurunan akurasi saat diuji pada data baru. Kesederhanaan persamaan matematis pada MLR tidak hanya memberikan tingkat presisi prediksi yang lebih tinggi, tetapi juga menuntut beban komputasi yang jauh lebih ringan. Oleh karena itu, MLR dipilih sebagai model final yang diimplementasikan ke dalam arsitektur sistem perangkat lunak akhir.

### 3.4 Evaluasi Kinerja Model Final (MLR)
Setelah algoritma *Multiple Linear Regression* (MLR) terpilih sebagai pemodelan komputasi yang paling optimal melalui proses *benchmarking*, tahapan selanjutnya adalah melakukan pembedahan mendalam terhadap metrik kinerja akhir yang dihasilkan. Evaluasi ini difokuskan pada interpretasi besaran tingkat kesalahan (*error rate*) dan seberapa representatif model tersebut dalam menjelaskan dinamika kualitas udara di lapangan.

#### 3.4.1 Analisis Tingkat Kesalahan (MAE, RMSE, dan MAPE)
Tingkat deviasi atau penyimpangan prediksi algoritma terhadap nilai aktual dihitung menggunakan tiga metrik utama. Berdasarkan hasil pengujian sistem, model MLR mencatatkan nilai *Mean Absolute Error* (MAE) sebesar 10,45. Angka ini mengindikasikan bahwa secara rata-rata, tebakan prediksi indeks polusi udara untuk hari esok hanya meleset sekitar 10 hingga 11 poin AQI dari kenyataan sebenarnya. Mengingat rentang indeks AQI berkisar dari 0 hingga lebih dari 200, tingkat kemelesetan 10 poin tergolong sangat kecil dan berada pada toleransi keamanan lingkungan yang dapat diandalkan.

Lebih lanjut, model menghasilkan nilai *Root Mean Squared Error* (RMSE) sebesar 14,50. Selisih yang relatif sempit antara nilai MAE (10,45) dan RMSE (14,50) ini membuktikan bahwa algoritma bekerja dengan sangat stabil. Artinya, model hampir tidak pernah menghasilkan tebakan prediksi yang melenceng secara ekstrem (anomali fatal) yang dapat memicu hukuman (penalti) tinggi pada perhitungan matematis kuadratik RMSE. Stabilitas prediksi ini diperkuat oleh nilai *Mean Absolute Percentage Error* (MAPE) sebesar 14,01%, yang mengonfirmasi bahwa akurasi model memiliki rasio keberhasilan prediksi di atas 85% untuk tata kota yang dinamis.

**Tabel 3.5 Kriteria Evaluasi MAPE (Lewis, 1982)**

| MAPE (%) | Kategori Kemampuan Prediksi |
| :--- | :--- |
| <10 | Sangat Akurat |
| **10-20** | **Baik** |
| 20-50 | Cukup |
| >50 | Tidak Akurat |

#### 3.4.2 Analisis Kekuatan Prediksi (R-Squared)
Kapasitas algoritma dalam mengidentifikasi pola kausalitas dievaluasi menggunakan metrik koefisien determinasi atau $R^2$ (*R-Squared*). Model regresi final mencatatkan perolehan skor $R^2$ sebesar 0.72. Secara akademis, perolehan metrik ini dapat diterjemahkan bahwa 72% dari total varians atau fluktuasi pergerakan kualitas udara (AQI) pada keesokan harinya berhasil dipelajari, ditangkap, dan dijelaskan secara murni oleh kombinasi sembilan fitur meteorologi cuaca yang diinputkan hari ini.

Sisa varians sebesar 28% mengindikasikan keberadaan faktor-faktor eksternal lain di luar batasan model seperti intervensi kebijakan ganjil-genap kendaraan, pergeseran jadwal operasional industri lokal, atau kejadian kebakaran yang turut memengaruhi kadar polutan udara di luar kebiasaan iklim alami.

#### 3.4.3 Visualisasi Kecocokan Model (Line Plot)
Untuk memvalidasi perbandingan metrik secara visual, dilakukan *plotting* atau pemetaan kurva grafik deret waktu (*time-series*) yang menyandingkan garis data nilai AQI faktual dengan garis hasil tebakan prediksi model.

![Gambar 3.5 Grafik Perbandingan AQI Aktual dengan Hasil Prediksi](Gambar%203.5.png)

*(Gambar 3.5 Grafik Perbandingan AQI Aktual dengan Hasil Prediksi)*

Berdasarkan Gambar 3.5, terlihat bahwa pergerakan garis hasil prediksi model (warna merah) secara responsivitas mampu menempel dan mengikuti lekukan tren garis data observasi riil (warna biru). Algoritma menunjukkan tingkat kepekaan yang presisi dalam mendeteksi pola turunnya kualitas udara pada musim kemarau dan membersihnya udara akibat curah hujan, sehingga menjadikan model ini sangat layak untuk diimplementasikan ke tahap *deployment* publik.

### 3.5 Implementasi dan Deployment Sistem
Tahap akhir dari siklus pengembangan model *Machine Learning* adalah operasionalisasi atau *deployment*, di mana algoritma komputasi yang telah dievaluasi diintegrasikan ke dalam sebuah ekosistem perangkat lunak agar dapat diakses secara publik. Implementasi sistem ini dirancang menggunakan pendekatan arsitektur terdistribusi untuk menjamin keandalan dan kecepatan respons aplikasi.

#### 3.5.1 Arsitektur Sistem Microservices
Untuk mencegah pembebanan komputasi yang berlebihan pada satu server, sistem dikembangkan dengan arsitektur *microservices*. Arsitektur ini secara tegas memisahkan beban kerja antara mesin pengolah logika kecerdasan buatan di sisi *backend* dan mesin perender antarmuka visual di sisi *frontend*. Pendekatan ini memastikan bahwa proses kalkulasi matriks aljabar dari algoritma regresi tidak akan menghambat atau memperlambat interaksi pengguna pada halaman situs web.

![Gambar 3.6 Diagram Arsitektur Website](Gambar%203.6.png)

*(Gambar 3.6 Diagram Arsitektur Website)*

#### 3.5.2 Pengembangan Machine Learning API (Backend)
Model *Multiple Linear Regression* (MLR) terpilih dan objek `StandardScaler` yang telah diubah ke dalam format berkas pickle (`.pkl`) dijalankan di dalam sebuah server Python. Server ini direkayasa menggunakan framework FastAPI untuk membungkus model tersebut menjadi sebuah REST API (*Representational State Transfer Application Programming Interface*).

Untuk memfasilitasi komunikasi lintas domain (CORS) dengan aman, diterapkan konfigurasi *middleware* yang mengizinkan *frontend* untuk mengirimkan data cuaca dalam format JSON. Kumpulan skrip *backend* ini beserta daftar dependensi pustakanya (`requirements.txt`) kemudian diunggah dan di-*deploy* ke dalam server komputasi awan Render (render.com). Platform ini bertindak sebagai wadah eksekusi yang selalu aktif menerima permintaan (*request*) perhitungan dari antarmuka pengguna kapan saja.

#### 3.5.3 Integrasi Antarmuka Pengguna (Frontend)
Sebagai medium interaksi dengan pengguna akhir, antarmuka portal prakiraan polusi udara dibangun menggunakan framework Next.js. Halaman web ini dirancang untuk menangkap input data cuaca dari pengguna (atau satelit), yang kemudian ditransmisikan secara asinkron (menggunakan fungsi `fetch`) menuju endpoint atau prediksi pada server *backend*.

Setelah server *backend* mengembalikan hasil kalkulasi tebakan AQI esok hari, nilai tersebut dirender dan divisualisasikan secara dinamik pada layar pengguna. Seluruh kode sumber *frontend* ini di-*deploy* menggunakan infrastruktur Edge Network dari Vercel (vercel.com) untuk memastikan waktu muat (*loading time*) antarmuka yang sangat cepat dan responsif.

![Gambar 3.7 Halaman Depan Website](Gambar%203.7.png)

*(Gambar 3.7 Halaman Depan Website)*

Sinergi antara Next.js di infrastruktur Vercel dan FastAPI di infrastruktur Render menghasilkan sistem prakiraan berbasis kecerdasan buatan yang komprehensif, tangguh, dan dapat diakses secara publik dengan performa tinggi. Antarmuka portal prakiraan polusi udara Jakarta ini dapat diakses secara publik melalui tautan https://jakarta-aqi.vercel.app/.

---

## 4. KESIMPULAN

Berdasarkan serangkaian eksperimen pemodelan deret waktu untuk kualitas udara, dapat disimpulkan bahwa prinsip kebaruan data (*data recency*) memiliki peran krusial dalam menghasilkan prediksi yang akurat. Penggunaan dataset yang lebih mutakhir pada rentang waktu 2024-2025 terbukti berhasil meminimalisasi efek *concept drift* serta gangguan anomali pembatasan aktivitas sosial di masa pandemi. Hasil ini berlawanan dengan hipotesis kuantitas data, di mana penambahan data historis yang masif dari tahun 2021 hingga 2023 justru mengurangi akurasi prediksi karena pola korelasi lingkungan yang lama sudah tidak relevan lagi dengan dinamika kondisi tata kota saat ini.

Dari segi pendekatan algoritmik, karakteristik korelasi antara variabel cuaca dan polutan udara teridentifikasi memiliki hubungan yang linear. Fenomena ini menjadikan algoritma *Multiple Linear Regression* (MLR) tampil sebagai solusi komputasi yang paling optimal dan efisien dibandingkan algoritma lain yang lebih kompleks. Melalui pengujian komparatif, model MLR secara konsisten berhasil mengungguli performa pemodelan *Support Vector Regression* (SVR) maupun *Extreme Gradient Boosting* (XGBoost) dengan mencatatkan tingkat kesalahan absolut rata-rata (MAE) sebesar 10.45, akar rata-rata kuadrat kesalahan (RMSE) sebesar 14.50, rata-rata persentase kesalahan absolut (MAPE) sebesar 14.01%, dan akurasi pengenalan pola (*R-Squared*) mencapai 0.72, sekaligus memastikan model terhindar dari risiko penghafalan data (*overfitting*).

Pada tahap operasionalisasi komputasi, keandalan model regresi ini berhasil direalisasikan ke ranah publik melalui implementasi arsitektur perangkat lunak berbasis *microservices*. Model MLR final dibungkus menjadi REST API menggunakan framework FastAPI dan dieksekusi pada infrastruktur server komputasi Render sebagai *backend* mandiri. Server *backend* tersebut kemudian diintegrasikan secara asinkron dengan portal antarmuka interaktif yang dibangun menggunakan Next.js pada jaringan Vercel di sisi *frontend*. Pemisahan beban kerja ini secara efektif menghasilkan ekosistem aplikasi web prakiraan kualitas udara yang responsif, berkinerja tinggi, dan mampu menjalankan kalkulasi matriks aljabar tanpa menghambat pengalaman interaksi pengguna.

---

## REFERENSI

* Al-Saeedi, K., Fish, A., Zhou, D., Tsakiri, K., & Marsellos, A. (2026). Multi-Scale Decomposition and Autocorrelation Modeling for Classical and Machine Learning-Based Time Series Forecasting. *Mathematics*. https://doi.org/10.3390/math14020283
* Anggraini, T., Irie, H., Sakti, A., & Wikantika, K. (2025). Global Air Quality Index Prediction Using Integrated Spatial Observation Data and Geographics Machine Learning. *Science of Remote Sensing*. https://doi.org/10.1016/j.srs.2025.100197
* Bose, A., & Chowdhury, I. R. (2023). Investigating the association between air pollutants' concentration and meteorological parameters in a rapidly growing urban center of West Bengal, India: a statistical modeling-based approach. *Modeling Earth Systems and Environment*, 9, 2877-2892. https://doi.org/10.1007/s40808-022-01670-6
* Donnelly, A., Misstear, B., & Broderick, B. (2015). Real time air quality forecasting using integrated parametric and non-parametric regression techniques. *Atmospheric Environment*, 103, 53-65. https://doi.org/10.1016/j.atmosenv.2014.12.011
* Faldo, R., Mandala, S., Astuti, R. P., Prihatmanto, A., & Zahid, M. M. S. (2025). APD-BayNet: Jakarta Air Quality Index Prediction Using Bayesian Optimized Tabnet. *IEEE Access*, 13, 57734-57752. https://doi.org/10.1109/access.2025.3555961
* Landgren, A. K., Johnsen, P. P., & Strüber, D. (2025). Cross-platform edge deployment of machine learning models: a model-driven approach. *Software and Systems Modeling*, 25, 163 - 187. https://doi.org/10.1007/s10270-025-01273-6
* Lewis, C. D. (1982). *Industrial and business forecasting methods: A practical guide to exponential smoothing and curve fitting*. Butterworth Scientific.
* Li, Y., & Li, R. (2023). A hybrid model for daily air quality index prediction and its performance in the face of impact effect of COVID-19 lockdown. *Process Safety and Environmental Protection*, 176, 673-684. https://doi.org/10.1016/j.psep.2023.06.021
* Persis, J. D., & Amar, A. B. (2022). Predictive modeling and analysis of air quality Visualizing before and during COVID-19 scenarios. *Journal of Environmental Management*, 327, 116911. https://doi.org/10.1016/j.jenvman.2022.116911
* Saiohai, J., Bualert, S., Thongyen, T., Duangmal, K., Choomanee, P., & Szymanski, W. (2023). Statistical PM2.5 Prediction in an Urban Area Using Vertical Meteorological Factors. *Atmosphere*. https://doi.org/10.3390/atmos14030589
* Singh, S., & Suthar, G. (2024). Machine learning and deep learning approaches for PM2.5 prediction: a study on urban air quality in Jaipur, India. *Earth Science Informatics*, 18. https://doi.org/10.1007/s12145-024-01648-1
* Varshney, D., Ekbal, A., & Cambria, E. (2022). Ambient air pollutants concentration prediction during the COVID-19: A method based on transfer learning. *Knowledge-Based Systems*, 258, 109996. https://doi.org/10.1016/j.knosys.2022.109996
* Xie, Y., & Tummala, S. (2025). Machine Learning for Sensor Analytics: A Comprehensive Review and Benchmark of Boosting Algorithms in Healthcare, Environmental, and Energy Applications. *Sensors (Basel, Switzerland)*, 25. https://doi.org/10.3390/s25237294
* Zeng, J., Zhang, D., Peng, A., Zhang, X., He, S., Wang, Y., Liu, X., Bi, H., Li, Y., Cai, C., Zhang, C., Du, Y., Zhu, J., Mo, P., Huang, Z., Zeng, Q., Shi, S., Qin, X.-T., Yu, Z., ... Wang, H. (2025). DeePMD-kit v3: A Multiple-Backend Framework for Machine Learning Potentials. *Journal of Chemical Theory and Computation*, 21, 4375-4385. https://doi.org/10.1021/acs.jctc.5c00340
* Zhao, R., Gu, X., Xue, B., Zhang, J., & Ren, W. (2018). Short period PM2.5 prediction based on multivariate linear regression model. *PLOS ONE*, 13. https://doi.org/10.1371/journal.pone.0201011
* Zhao, Z., Wu, J., Cai, F., Zhang, S., & Wang, Y.-G. (2023). A hybrid deep learning framework for air quality prediction with spatial autocorrelation during the COVID-19 pandemic. *Scientific Reports*, 13. https://doi.org/10.1038/s41598-023-28287-8