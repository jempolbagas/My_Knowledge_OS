# Panduan Tanya Jawab (Q&A) Presentasi Tugas Besar AI
**Prediksi Kualitas Udara Harian Berbasis Faktor Cuaca di Jakarta Menggunakan Multiple Linear Regression**

Panduan ini disusun untuk mempersiapkan Anda (Bagas, Raditya, dan Syaikhasril) menghadapi berbagai kemungkinan pertanyaan dari dosen penguji atau audiens saat presentasi tugas besar.

---

## 📌 Kategori 1: Latar Belakang & Intuisi Fisik (Cuaca vs. AQI)

### 1. Mengapa memprediksi kualitas udara berdasarkan faktor cuaca (meteorologi)? Apa kaitan logisnya?
* **Jawaban Inti:** Kualitas udara tidak hanya dipengaruhi oleh emisi polutan (sumber industri/kendaraan), tetapi juga secara signifikan dikontrol oleh parameter cuaca yang menentukan apakah polutan tersebut akan terdispersi, mengendap, atau justru bereaksi menjadi polutan baru di atmosfer.
* **Penjelasan Detil:**
  * **Angin (Wind Speed):** Bertindak sebagai "pembersih alami" yang mendispersikan partikel polusi. Jika angin kencang, AQI cenderung rendah (bersih).
  * **Curah Hujan (Precipitation):** Melakukan pencucian udara melalui proses *wet deposition* (partikel debu PM2.5 terikat air hujan dan jatuh ke tanah).
  * **Suhu & Radiasi:** Bertindak sebagai katalis. Radiasi matahari yang kuat memicu reaksi fotokimia antara gas nitrogen oksida ($NO_x$) dan VOC membentuk **Ozon Permukaan ($O_3$)** yang meningkatkan AQI.
  * **Kelembapan & Awan:** Kelembapan tinggi membuat partikel PM2.5 menyerap uap air, menjadi berat, dan terjebak di dekat permukaan tanah. Awan bertindak sebagai peneduh yang menghambat pembentukan ozon.
* **Tips Presentasi:** Gunakan analogi **"Wadah Kaca Raksasa"** (kubah Jakarta). Polusi diisi terus oleh kendaraan, tetapi cuaca (hujan, angin, panas) adalah tombol pengontrol apakah wadah itu dibersihkan atau ditutup rapat.

---

## 📌 Kategori 2: Pra-Pemrosesan Data & Asumsi Klasik

### 2. Apa itu teknik *Time-Series Shifting* yang kalian lakukan? Mengapa itu perlu?
* **Jawaban Inti:** *Time-Series Shifting* adalah proses menggeser nilai variabel target (AQI) naik satu hari ($t+1$) sehingga sejajar dengan fitur cuaca hari ini ($t$). Ini diperlukan karena tujuan model adalah **prakiraan (forecasting H+1)**.
* **Penjelasan Detil:** Jika kita memprediksi AQI hari ini menggunakan cuaca hari ini, model tidak akan berguna secara praktis karena data cuaca harian baru lengkap di akhir hari. Dengan menggeser target, data cuaca yang terukur sepanjang hari ini digunakan untuk memprediksi indeks kualitas udara esok hari, memberikan sistem peringatan dini (*early warning*).
* **Tips Presentasi:** Tegaskan bahwa baris terakhir pada dataset dihapus setelah *shifting* karena tidak memiliki target AQI esok harinya (bernilai `NaN`).

### 3. Mengapa kalian melakukan Standardisasi Fitur (`StandardScaler`)? Bukankah Regresi Linear secara teoritis tidak sensitif terhadap skala fitur untuk menghasilkan prediksi?
* **Jawaban Inti:** Standardisasi (Z-Score Scaling) dilakukan untuk dua alasan utama: keadilan *benchmarking* antar algoritma, dan kemudahan interpretasi bobot koefisien.
* **Penjelasan Detil:**
  1. **Keadilan Benchmarking:** Model pembanding seperti SVR (Support Vector Regression) sangat sensitif terhadap perbedaan skala karena menggunakan perhitungan jarak matematis. Jika tidak di-scale, fitur berskala besar (seperti Tekanan Udara $\approx 1000\text{ hPa}$) akan mendominasi fitur kecil (seperti Curah Hujan $0-10\text{ mm}$).
  2. **Interpretasi Koefisien:** Setelah distandardisasi ke skala yang sama (mean=0, std=1), nilai koefisien $\beta$ pada MLR dapat dibandingkan secara langsung untuk menentukan variabel mana yang memiliki dampak paling kuat terhadap AQI.
* **Tips Presentasi:** Tunjukkan rumus Z-score: $Z = \frac{x - \mu}{\sigma}$ untuk menunjukkan pemahaman matematis Anda.

### 4. Bagaimana kalian mendeteksi multikolinearitas? Mengapa itu berbahaya bagi model regresi linear?
* **Jawaban Inti:** Kami mendeteksinya menggunakan matriks korelasi Pearson. Multikolinearitas adalah hubungan linier yang terlalu kuat antar-variabel independen (fitur), yang membuat koefisien regresi menjadi tidak stabil, bias, dan sulit diinterpretasikan.
* **Penjelasan Detil:** Korelasi tertinggi terjadi antara suhu udara rata-rata (*temperature_2m_mean*) dan kelembaban relatif (*relative_humidity_2m_mean*) dengan nilai koefisien $-0.75$. Nilai ini masih berada di bawah ambang batas kritis (umumnya $0.80$ atau $0.90$). Oleh karena itu, asumsi klasik terpenuhi dan tidak ada masalah multikolinearitas ekstrem.
* **Tips Presentasi:** Katakan: *"Jika dua variabel sangat berkorelasi (seperti suhu dan kelembapan), model akan kesulitan memisahkan pengaruh individu dari masing-masing variabel terhadap AQI. Namun, pengujian kami membuktikan korelasi keduanya masih dalam batas aman (-0.75)."*

---

## 📌 Kategori 3: Eksperimen Utama (Concept Drift & Data Recency)

### 5. Mengapa dataset rentang pendek (2024-2025) menghasilkan performa lebih baik ($R^2=0.72$) dibanding data historis panjang 2021-2025 ($R^2=0.62$)? Bukankah lebih banyak data harusnya lebih baik?
* **Jawaban Inti:** Karena adanya fenomena **Concept Drift** (pergeseran konsep) akibat anomali pandemi COVID-19 pada tahun 2021-2022.
* **Penjelasan Detil:**
  * Pada tahun 2021 hingga pertengahan 2022, Jakarta menerapkan PPKM/Lockdown. Emisi kendaraan bermotor dan industri turun drastis (hingga 50%).
  * Akibatnya, hubungan alami antara cuaca dan polusi terganggu. Cuaca panas kering yang biasanya menghasilkan polusi tinggi justru menghasilkan polusi rendah karena sumber emisinya tidak ada.
  * Pola anomali masa lalu ini menjadi **noise** (gangguan) bagi model jika dipaksakan untuk memprediksi kondisi masa kini (2024-2025) di mana aktivitas perkotaan sudah normal kembali.
* **Tips Presentasi:** Ini adalah poin emas presentasi Anda. Jelaskan bahwa dalam pemodelan lingkungan yang dinamis, **kebaruan data (*data recency*)** jauh lebih penting daripada kuantitas data historis belaka.

---

## 📌 Kategori 4: Pemodelan & Uji Komparasi (Benchmarking)

### 6. Mengapa Multiple Linear Regression (MLR) bisa mengalahkan algoritma kompleks seperti XGBoost dan SVR dalam pengujian kalian?
* **Jawaban Inti:** Hubungan fisik antara cuaca harian dan polusi udara Jakarta memiliki karakteristik dasar yang dominan linear, dan dataset yang digunakan relatif kecil (731 baris). Model kompleks cenderung mengalami *overfitting* pada skenario ini.
* **Penjelasan Detil:**
  * **Overfitting pada XGBoost:** XGBoost bekerja berdasarkan *decision trees* yang membuat batas keputusan bertingkat (non-linear). Pada data berukuran kecil dengan pola linear kuat, XGBoost cenderung "menghafal" noise pada data latih secara berlebihan (*overthinking*), sehingga gagal menggeneralisasi dengan baik pada data uji baru.
  * **SVR dengan Kernel RBF:** Mencoba memetakan data ke ruang dimensi yang lebih tinggi secara non-linear, yang sebenarnya tidak diperlukan karena pola dasarnya linear, sehingga performanya kalah tipis dari MLR.
* **Tips Presentasi:** Sebutkan hasil skornya secara spesifik: MLR ($R^2 = 0.72$), SVR ($R^2 = 0.69$), XGBoost ($R^2 = 0.66$).

### 7. Jelaskan arti matematis dari model regresi linear berganda kalian!
* **Jawaban Inti:** Model kami merumuskan prediksi sebagai penjumlahan bobot linier dari 7 parameter cuaca:
  $$\text{AQI}_{t+1} = \beta_0 + \beta_1\text{RH}_t + \beta_2\text{P}_t + \beta_3\text{T}_t + \beta_4\text{WS}_t + \beta_5\text{SP}_t + \beta_6\text{CC}_t + \beta_7\text{SR}_t$$
* **Penjelasan Detil:**
  * $\beta_0$ (Intercept) adalah nilai baseline AQI esok hari jika semua fitur cuaca yang terstandardisasi bernilai 0.
  * Koefisien $\beta_1 \dots \beta_7$ menunjukkan arah dan kekuatan pengaruh. Contohnya, kecepatan angin ($WS$) memiliki koefisien negatif (korelasi -0.38), artinya setiap kenaikan kecepatan angin akan menurunkan nilai AQI esok hari secara linier.
* **Tips Presentasi:** Jelaskan bahwa tanda positif/negatif pada koefisien langsung mencerminkan hubungan fisika atmosfer (misalnya: curah hujan naik $\rightarrow$ polusi turun $\rightarrow$ koefisien negatif).

---

## 📌 Kategori 5: Metrik Evaluasi & Hasil

### 8. Bagaimana cara kalian membaca performa model dari nilai MAE (10.45), RMSE (14.50), dan MAPE (14.01%)?
* **Jawaban Inti:**
  * **MAE (10.45):** Tebakan prediksi indeks polusi udara esok hari rata-rata meleset sekitar 10.45 poin AQI dari nilai aktualnya. Ini tingkat meleset yang aman karena rentang AQI sangat lebar (0-300+).
  * **RMSE (14.50):** Nilainya dekat dengan MAE, membuktikan model kita stabil dan jarang membuat prediksi salah yang bernilai ekstrem (karena RMSE memberi penalti kuadrat pada error besar).
  * **MAPE (14.01%):** Berdasarkan kriteria evaluasi Lewis (1982), nilai MAPE di rentang 10-20% dikategorikan sebagai **"Prakiraan Baik (Good Forecast)"**.
* **Tips Presentasi:** Tampilkan tabel kriteria MAPE Lewis untuk memperkuat argumentasi akademis Anda.

### 9. Skor $R^2$ model kalian adalah 0.72. Ke mana sisa 28%-nya? Mengapa tidak bisa 100% (1.0)?
* **Jawaban Inti:** Nilai $R^2 = 0.72$ berarti 72% variasi naik-turunnya AQI esok hari dipengaruhi oleh 7 faktor cuaca hari ini. Sisa 28% variasi disebabkan oleh faktor eksternal non-cuaca yang tidak masuk dalam model.
* **Penjelasan Detil:** Faktor eksternal tersebut meliputi aktivitas manusia seperti volume lalu lintas harian (efek kebijakan ganjil-genap), aktivitas emisi industri, pembakaran sampah ilegal, atau kebakaran hutan regional yang tidak dapat diprediksi hanya lewat data meteorologi murni.
* **Tips Presentasi:** Katakan: *"Model tidak mungkin 100% karena kualitas udara adalah interaksi kompleks antara faktor alam (cuaca) dan aktivitas manusia. Menjelaskan 72% variasi hanya dengan faktor cuaca adalah pencapaian yang sangat baik untuk model prediktif."*

---

## 📌 Kategori 6: Arsitektur Sistem & Deployment

### 10. Mengapa kalian mendesain sistem dengan arsitektur terdistribusi (Microservices) memisahkan Frontend dan Backend? Kenapa tidak disatukan saja (Monolith)?
* **Jawaban Inti:** Untuk menjamin pemisahan beban kerja (*separation of concerns*), skalabilitas, dan kecepatan waktu muat (*loading time*) aplikasi bagi pengguna.
* **Penjelasan Detil:**
  * **Backend (FastAPI di Render):** Fokus sepenuhnya mengeksekusi komputasi aljabar regresi linear dengan memuat file pickle (`.pkl`) model dan scaler secara asinkron.
  * **Frontend (Next.js di Vercel):** Fokus pada rendering visual antarmuka pengguna agar situs web terasa instan, interaktif, dan responsif.
  * **Manfaat:** Jika backend mengalami overload karena permintaan prediksi yang tinggi, tampilan halaman web frontend tidak akan mengalami *freezing* atau macet karena proses render antarmuka dan komputasi regresi berada di infrastruktur server yang berbeda.
* **Tips Presentasi:** Tunjukkan diagram arsitektur sistem (Vercel ↔ Render) untuk menunjukkan bahwa proyek ini tidak hanya berhenti di notebook, tetapi sampai ke tahap produksi/siap pakai oleh publik.

### 11. Bagaimana FastAPI backend memuat model MLR yang sudah dilatih di Python notebook?
* **Jawaban Inti:** Model MLR dan objek `StandardScaler` yang sudah dilatih diekspor dari notebook menggunakan library `pickle` (atau `joblib`) ke dalam berkas biner `.pkl`.
* **Penjelasan Detil:** Di server FastAPI backend, file `.pkl` tersebut dimuat (*load*) saat startup server ke dalam memori. Ketika menerima data cuaca input baru dalam format JSON dari frontend Next.js, backend langsung melakukan proses standardisasi data dan inferensi prediksi menggunakan model yang dimuat tadi secara instan tanpa perlu melatih ulang model.
* **Tips Presentasi:** Sebutkan berkas spesifiknya: `model.pkl` dan `scaler.pkl`.
