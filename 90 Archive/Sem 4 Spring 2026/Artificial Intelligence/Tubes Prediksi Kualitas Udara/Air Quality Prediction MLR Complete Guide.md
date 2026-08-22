---
title: "Complete Guide: Prediksi Kualitas Udara Jakarta dengan Multiple Linear Regression"
course: "Artificial Intelligence"
tags:
  - college/study-guide
  - machine-learning
  - multiple-linear-regression
  - concept-drift
aliases:
  - Panduan Lengkap Prediksi Kualitas Udara
created: 2026-07-01
---

# Complete Guide: Prediksi Kualitas Udara Jakarta Menggunakan Multiple Linear Regression

Selamat datang di panduan belajar lengkap, gaes! Panduan ini dirancang khusus untuk membantu kita memahami seluruh materi tugas besar prediksi kualitas udara Jakarta secara mendalam dan dari nol. Kita bakal bongkar semua konsep mulai dari intuisi cuaca, cara kerja matematika di balik regresi linear, fenomena *concept drift* akibat pandemi, perbandingan algoritma, sampai arsitektur aplikasinya.

---

## Bab 1: Intuisi Kualitas Udara dan Faktor Cuaca

Sebelum masuk ke rumus matematika dan *coding*, kita kudu paham dulu hubungan fisik antara cuaca dan kualitas udara di dunia nyata. 

> [!INFO]
> **Analogi Wadah Kaca Raksasa:**
> Bayangkan kota Jakarta berada di dalam sebuah kubah atau wadah kaca raksasa. Asap dari jutaan sepeda motor, mobil, dan cerobong pabrik di sekitarnya terus ditiupkan ke dalam wadah ini setiap hari. 
> Cuaca bertindak sebagai **tombol pengontrol** kondisi wadah kaca tersebut: apakah udara kotor di dalamnya akan dibersihkan, diencerkan, atau justru diperangkap hingga semakin pekat.

Berikut adalah bagaimana masing-masing parameter cuaca memengaruhi kualitas udara (AQI):

1. **Suhu Udara (Temperature - °C) & Radiasi Gelombang Pendek (Shortwave Radiation - $\text{MJ/m}^2$):**
   * *Mental Model:* Suhu dan radiasi adalah "kompor pemanas" dalam wadah.
   * *Logika Fisik:* Paparan radiasi matahari yang kuat dan suhu tinggi akan mempercepat reaksi kimia di atmosfer. Gas-gas polutan primer (seperti nitrogen oksida dari knalpot) bereaksi dengan senyawa organik mudah menguap (VOC) membentuk polutan sekunder yang sangat berbahaya, yaitu **Ozon Permukaan ($O_3$)**. Semakin panas hari, reaksi pembentukan ozon ini semakin cepat, sehingga AQI cenderung naik.

2. **Kecepatan Angin (Wind Speed - m/s):**
   * *Mental Model:* Angin adalah "kipas angin raksasa" yang meniup polusi keluar wadah.
   * *Logika Fisik:* Ini adalah parameter pembersih utama. Ketika angin berhembus kencang, partikel polusi di udara Jakarta akan tersebar (*dispersion*) ke wilayah lain atau ke atas atmosfer, sehingga konsentrasi polutan lokal menurun drastis. Jika angin tenang (*calm wind*), polusi akan terjebak di tempat asal dan terus menumpuk.

3. **Curah Hujan (Precipitation - mm):**
   * *Mental Model:* Hujan adalah "shower penyiram debu".
   * *Logika Fisik:* Air hujan yang jatuh ke bumi akan menabrak dan menangkap partikel polutan padat yang melayang di udara (seperti PM2.5 dan PM10). Partikel-partikel ini ikut larut dan jatuh ke tanah dalam proses yang disebut **wet deposition** (pencucian udara). Makanya, setelah hujan lebat, langit Jakarta biasanya terlihat jauh lebih bersih dan biru.

4. **Kelembaban Relatif (Relative Humidity - %):**
   * *Mental Model:* Kelembaban adalah "kabut basah yang lengket".
   * *Logika Fisik:* Ketika kelembapan udara sangat tinggi, udara dipenuhi oleh uap air. Partikel debu halus (PM2.5) cenderung menyerap uap air ini, ukurannya membesar (higroskopis), dan tetap melayang dekat dengan permukaan tanah karena udara menjadi berat. Namun, kelembaban yang sangat tinggi juga sering kali berasosiasi dengan cuaca mendung atau hujan yang justru bisa menurunkan polusi.

5. **Tutupan Awan (Cloud Cover - %):**
   * *Mental Model:* Awan adalah "payung peneduh" wadah.
   * *Logika Fisik:* Jika awan mendung menutupi langit, radiasi matahari yang sampai ke permukaan bumi berkurang drastis. Akibatnya, suhu udara turun dan reaksi fotokimia pembentukan ozon permukaan terhambat. Ini menjelaskan mengapa tutupan awan memiliki hubungan negatif dengan AQI (awan naik, AQI turun).

---

## Bab 2: Membongkar Multiple Linear Regression (MLR)

Sekarang kita masuk ke aspek kecerdasan buatan (*Machine Learning*). Model utama yang kita gunakan adalah **Multiple Linear Regression (Regresi Linear Berganda)**.

> [!INFO]
> **Analogi Resep Masakan:**
> Bayangkan kita ingin membuat masakan dengan rasa yang pas (Target: Nilai AQI). 
> Untuk menghasilkan rasa tersebut, kita memasukkan beberapa bumbu (Variabel Independen: Suhu, Hujan, Kecepatan Angin, dsb.).
> Tugas algoritma Regresi Linear adalah **mencari takaran sendok (Bobot/Koefisien $\beta$)** yang pas untuk setiap bumbu, agar tebakan rasa masakan kita mendekati rasa aslinya.

### A. Persamaan Matematis MLR
Secara formal, model prediksi kualitas udara harian Jakarta dirumuskan sebagai berikut:

$$\text{AQI}_{t+1} = \beta_0 + \beta_1\text{RH}_t + \beta_2\text{P}_t + \beta_3\text{T}_t + \beta_4\text{WS}_t + \beta_5\text{SP}_t + \beta_6\text{CC}_t + \beta_7\text{SR}_t + \epsilon$$

*Dengan:*
* $\text{AQI}_{t+1}$: Nilai *Air Quality Index* esok hari ($t+1$) $\rightarrow$ **Variabel Dependen (Y)**.
* $\text{RH}_t$: Kelembaban relatif rata-rata hari ini ($t$).
* $\text{P}_t$: Total curah hujan hari ini.
* $\text{T}_t$: Suhu rata-rata hari ini.
* $\text{WS}_t$: Kecepatan angin rata-rata hari ini.
* $\text{SP}_t$: Tekanan udara permukaan rata-rata hari ini (*Surface Pressure*).
* $\text{CC}_t$: Tutupan awan rata-rata hari ini (*Cloud Cover*).
* $\text{SR}_t$: Total radiasi gelombang pendek hari ini (*Shortwave Radiation*).
* $\beta_0$: **Konstanta / Intercept** (Nilai baseline AQI jika seluruh parameter cuaca bernilai nol).
* $\beta_1 \dots \beta_7$: **Koefisien Regresi** yang menunjukkan kekuatan dan arah pengaruh tiap parameter cuaca terhadap AQI.
* $\epsilon$: **Residual / Error** (Perbedaan antara AQI aktual dengan hasil prediksi model).

### B. Mengapa Hubungan Cuaca dan Polusi Bersifat Linear?
Regresi linear berasumsi bahwa hubungan antar-variabel berupa garis lurus. Di dunia nyata, dinamika atmosfer memang banyak yang bersifat linier langsung:
* Jika kecepatan angin naik 2 kali lipat, volume dispersi udara kotor juga naik secara proporsional.
* Jika curah hujan bertambah, tingkat pencucian partikel debu halus juga naik secara linier.
Hal inilah yang membuat pendekatan linier sederhana (MLR) sangat cocok dan efektif untuk kasus ini.

---

## Bab 3: Pra-Pemrosesan Data (Data Preprocessing)

Sebelum data dimasukkan ke dalam model MLR, ada beberapa tahap pengolahan data mentah agar algoritma tidak salah arah saat belajar.

### 1. Pergeseran Deret Waktu (*Time-Series Shifting*)
Tujuan aplikasi kita adalah memberikan **prakiraan (forecast H+1)**. Artinya, hari ini kita ingin tahu berapa AQI untuk besok.
* Jika kita menggunakan data cuaca tanggal 1 Juli untuk memprediksi AQI tanggal 1 Juli, model tidak bisa dipakai untuk masa depan karena data cuaca baru lengkap di penghujung hari.
* Solusinya, kita lakukan *shifting* (pergeseran) pada target $Y$. Nilai AQI tanggal 2 Juli disejajarkan dengan data cuaca tanggal 1 Juli di dalam baris dataset. 
* Baris data terakhir pada dataset terpaksa dihapus karena tidak memiliki pasangan target AQI untuk keesokan harinya.

### 2. Standarisasi Fitur (*Z-Score Scaling*)
Fitur cuaca kita memiliki rentang angka (*magnitudo*) yang sangat berbeda jauh:
* Tekanan udara bernilai sekitar $1008 \text{ hPa}$.
* Curah hujan bernilai antara $0 \text{ s.d. } 50 \text{ mm}$.
* Suhu udara bernilai sekitar $25 \text{ s.d. } 32 \text{ }^\circ\text{C}$.

> [!IMPORTANT]
> **Kenapa Standard Scaling Kudu Dilakukan?**
> Jika data langsung dilatih tanpa scaling, algoritma regresi linear akan menganggap variabel dengan angka besar (seperti Tekanan Udara $1000+$) jauh lebih penting dibandingkan variabel berangka kecil (seperti Curah Hujan $0-10$), hanya karena ukuran angkanya. Padahal pengaruh curah hujan bisa jadi jauh lebih krusial.
>
> Kita menggunakan metode standardisasi Z-Score untuk mengubah rata-rata variabel menjadi 0 dan standar deviasinya menjadi 1:
> $$Z = \frac{x - \mu}{\sigma}$$
> *Di mana $x$ adalah nilai asli, $\mu$ adalah rata-rata variabel, dan $\sigma$ adalah standar deviasi.*

### 3. Uji Asumsi Klasik: Multikolinearitas
Multikolinearitas adalah kondisi di mana ada dua atau lebih variabel independen (fitur cuaca) yang saling berkorelasi sangat kuat satu sama lain.
* *Analogi:* Jika kita memasukkan garam dapur dan air laut ke dalam masakan, keduanya memberikan rasa asin yang sama. Model akan bingung menentukan bumbu mana yang sebenarnya memberikan kontribusi rasa asin tersebut.
* *Di Kasus Kita:* Suhu rata-rata dan kelembaban relatif memiliki korelasi negatif yang kuat sebesar $-0.75$. Ketika suhu naik, kelembaban biasanya turun. Namun, karena nilainya masih di bawah batas kritis $0.80$, kedua variabel ini aman digunakan bersamaan tanpa merusak kestabilan model MLR.

---

## Bab 4: Konsep Utama - *Concept Drift* & *Data Recency*

Ini adalah bagian paling penting dari penelitian kita, yang menjadi *selling point* utama laporan tugas besar ini!

> [!INFO]
> **Definisi Concept Drift:**
> *Concept drift* adalah perubahan pola hubungan antara variabel input (fitur cuaca) dan target (AQI) yang terjadi seiring waktu akibat adanya faktor eksternal di luar model.

```
Pola Data Masa Pandemi (2021-2022)       Pola Data Normal/Sekarang (2024-2025)
[Lockdown / Jalanan Sepi]                [Aktivitas Normal / Jalanan Macet]
        │                                         │
        ▼                                         ▼
Cuaca Panas ──► Polusi Rendah             Cuaca Panas ──► Polusi Sangat Tinggi
(Karena tidak ada emisi)                 (Emisi menumpuk + reaksi ozon cepat)
```

### A. Mengapa Menambahkan Data Historis Malah Memperburuk Model?
Dalam machine learning tradisional, ada anggapan umum: *"Semakin banyak data latihan, semakin pintar modelnya."* Namun eksperimen kita membuktikan hal sebaliknya:
* **Model 2021-2025 (Historis Panjang):** Akurasi $R^2 = 0.62$, MAE $= 12.94$.
* **Model 2024-2025 (Data Baru):** Akurasi $R^2 = 0.72$, MAE $= 10.45$.

**Alasan Ilmiahnya:**
1. Pada tahun 2021-2022, Jakarta menerapkan kebijakan pembatasan aktivitas sosial (PPKM/Lockdown) akibat pandemi COVID-19. Volume kendaraan bermotor turun drastis, menurunkan emisi polusi hingga 50%.
2. Korelasi alami cuaca dan polusi terganggu. Cuaca panas kering yang harusnya memicu polusi tinggi, justru menghasilkan polusi rendah karena sumber emisinya (kendaraan) tidak beroperasi di jalan.
3. Pola anomali masa lalu ini menjadi **noise** (gangguan) bagi model jika digunakan untuk memprediksi kondisi masa kini (2024-2025) yang aktivitas transportasinya sudah kembali padat dan normal.
4. Eksperimen ini menyimpulkan bahwa **kebaruan data (*data recency*) jauh lebih penting dibandingkan kuantitas data** untuk model prediksi lingkungan perkotaan yang dinamis.

---

## Bab 5: Benchmarking Algoritma (MLR vs SVR vs XGBoost)

Kita membandingkan tiga algoritma machine learning yang berbeda filosofi kerjanya:

| Algoritma | Karakteristik Utama | Keunggulan | Kelemahan |
| :--- | :--- | :--- | :--- |
| **Multiple Linear Regression (MLR)** | Menarik garis lurus linear yang meminimalkan kuadrat error residual. | Sangat ringan, mudah diinterpretasikan, tidak mudah *overfitting*. | Tidak bisa menangkap hubungan non-linear yang kompleks. |
| **Support Vector Regression (SVR)** | Mencari garis pembatas (*hyperplane*) dengan margin toleransi ($\epsilon$). | Kuat terhadap pencilan (*outliers*), fleksibel dengan trik kernel. | Butuh penyetelan parameter yang rumit, lambat pada data besar. |
| **Extreme Gradient Boosting (XGBoost)** | Kumpulan pohon keputusan (*decision trees*) yang dilatih berurutan untuk memperbaiki error pohon sebelumnya. | Sangat akurat untuk pola data kompleks non-linear. | Rentan mengalami *overfitting* (terlalu menghafal data latihan). |

### Mengapa MLR Menang Telah di Eksperimen Kita?
Berdasarkan hasil uji coba, MLR memimpin dengan $R^2$ tertinggi ($0.72$) dan MAE terendah ($10.45$).
* Hubungan fisik antara cuaca harian dan polusi udara Jakarta memiliki karakteristik dasar yang dominan linear.
* Dataset kita bersih dan memiliki ukuran relatif kecil (sekitar $731$ baris). Algoritma kompleks seperti XGBoost memerlukan data yang sangat besar untuk menghindari bias. Pada data kecil, XGBoost mengalami **overfitting**—ia menghafal pola data latihan secara detail namun gagal melakukan generalisasi dengan baik pada data uji baru.

---

## Bab 6: Metrik Evaluasi Model

Untuk mengukur seberapa hebat tebakan model kita, digunakan empat metrik evaluasi standar:

1. **Mean Absolute Error (MAE):**
   * *Rumus:* $\text{MAE} = \frac{1}{n}\sum_{i=1}^{n} \lvert y_i - \hat{y}_i \rvert$
   * *Arti Fisis:* Rata-rata selisih mutlak antara nilai prediksi ($\hat{y}$) dan nilai aktual ($y$). MAE kita sebesar **10.45** menunjukkan bahwa tebakan model rata-rata meleset sekitar 10 poin AQI dari kenyataan.

2. **Root Mean Squared Error (RMSE):**
   * *Rumus:* $\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$
   * *Arti Fisis:* Mirip dengan MAE, tetapi memberikan hukuman (penalti) yang jauh lebih berat untuk kesalahan prediksi yang bernilai besar (karena dikuadratkan). RMSE kita yang bernilai **14.50** (tidak jauh dari MAE) menunjukkan model kita stabil dan jarang membuat prediksi yang salah secara ekstrem.

3. **Mean Absolute Percentage Error (MAPE):**
   * *Rumus:* $\text{MAPE} = \frac{100\%}{n}\sum_{i=1}^{n}\left| \frac{y_i - \hat{y}_i}{y_i} \right|$
   * *Arti Fisis:* Persentase kesalahan rata-rata model. Nilai MAPE kita sebesar **14.01%** masuk dalam kategori **"Prakiraan Baik (Good Forecast)"** berdasarkan kriteria standar industri (skala 10% - 20%).

4. **Koefisien Determinasi ($R^2$):**
   * *Rumus:* $R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}$
   * *Arti Fisis:* Mengukur seberapa baik variasi target dapat dijelaskan oleh fitur cuaca. Nilai $R^2 = 0.72$ berarti **72% variabilitas AQI esok hari** berhasil dijelaskan secara statistik oleh 7 parameter cuaca hari ini. Sisanya 28% dipengaruhi faktor luar (kebijakan lalu lintas, aktivitas industri, dll.).

---

## Bab 7: Arsitektur Microservices Deployment

Tugas besar ini diselesaikan hingga tahap implementasi aplikasi berbasis web yang bisa diakses publik menggunakan arsitektur **microservices**:

```mermaid
graph TD
    User["Pengguna (Browser)"] ──►|"Akses Antarmuka"| Vercel["Frontend (Next.js di Vercel)"]
    Vercel ──►|"Kirim Data Cuaca (JSON)"| Render["Backend (FastAPI di Render)"]
    Render ──►|"Muat Model MLR (.pkl)"| ML["Prediksi MLR Model"]
    ML ──►|"Kembalikan Nilai AQI Prediksi"| Render
    Render ──►|"Respon Data API"| Vercel
    Vercel ──►|"Render Halaman Web Dinamis"| User
```

### Mengapa Memisahkan Backend dan Frontend?
* **FastAPI (Backend - Render):** Berfungsi sebagai mesin pengolah prediksi. FastAPI sangat cepat dan asinkron, bertugas memuat file model regresi linear dalam format berkas pickle (`.pkl`) dan melakukan kalkulasi matematika saat dipanggil.
* **Next.js (Frontend - Vercel):** Berfungsi sebagai perancang visual antarmuka pengguna. Next.js ditaruh di server Vercel agar halaman web dapat dimuat dengan instan oleh browser pengguna.
* **Keuntungan Utama:** Pemisahan beban kerja (*separation of concerns*). Jika terjadi lonjakan pengguna yang membuka web, beban komputasi perhitungan regresi tidak akan membuat tampilan halaman web menjadi lambat atau macet (*freezing*).
