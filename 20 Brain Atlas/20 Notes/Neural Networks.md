---
type: note
title: "Neural Networks"
subject: "Machine Learning"
created: 2026-09-03
prerequisites:
  - "[[Calculus for Machine Learning]]"
tags:
  - deep-learning
  - machine-learning
  - linear-algebra
  - foundations
---

Neural Network (Jaringan Saraf Tiruan) pada dasarnya adalah **mesin aproksimasi fungsi matematis universal** (*Universal Function Approximator*). Alih-alih meniru biologi otak secara harfiah, jaringan ini bekerja sebagai rangkaian perkalian matriks, pergeseran bias, dan pemetaan non-linear yang memetakan vektor input $x \in \mathbb{R}^n$ menjadi vektor output $\hat{y} \in \mathbb{R}^m$ melalui pembelajaran representasi berlapis (*hierarchical representation*).

## Anatomi Unit Terkecil: Satu Neuron Buatan

Satu neuron buatan (sering disebut Perceptron atau unit komputasi) hanyalah model **Regresi Linear** yang dipasangi **sakelar non-linear**:

```
x1 ──(w1)──\
x2 ──(w2)────> [ Sum: z = Σ(w_i * x_i) + b ] ──> [ Aktivasi: a = σ(z) ] ──> Output a
x3 ──(w3)──/
```

Secara matematis, satu neuron melakukan dua operasi berurutan:
1. **Kombinasi Linear (Pre-aktivasi $z$):**
   $$ z = \sum_{i=1}^{n} w_i x_i + b = w^T x + b $$
   - **Input ($x_i$):** Fitur numerik data (misal: luas tanah, jumlah kamar tidur). **Sifat: Tetap** (data fakta dari dunia nyata, tidak diubah oleh algoritma).
   - **Bobot ($w_i$ - Weight):** Tingkat pengaruh atau signifikansi fitur terhadap keputusan akhir. **Sifat: Berubah/Dilatih** (diputar nilainya untuk mencari akurasi tertinggi).
   - **Bias ($b$):** Titik potong (*intercept*) yang menggeser fungsi agar tidak selalu terikat di titik origin $(0,0)$. **Sifat: Berubah/Dilatih** (ikut digeser oleh algoritma bersama bobot).

> [!important] Data vs. Parameter
> - **Tetap:** Data Input ($x$) dan Target Asli ($y$). Algoritma tidak boleh mengubah fakta data.
> - **Diubah-ubah (*Learnable Parameters*):** Bobot ($W$) dan Bias ($b$). Keduanya adalah "kenop" yang disesuaikan oleh optimizer saat training.

2. **Transformasi Non-linear (Aktivasi $a$):**
   $$ a = \sigma(z) $$
   Fungsi aktivasi memetakan nilai linear $z$ ke domain tertentu (misalnya $0$ sampai $1$ pada Sigmoid, atau $\max(0, z)$ pada ReLU).

## Mengapa Fungsi Aktivasi Wajib Ada?

Tanpa fungsi aktivasi, berapapun dalamnya (*depth*) jaringan yang dibuat, model tersebut secara matematis **hanya setara dengan satu lapis regresi linear**.

Buktinya:
Jika layer 1 adalah $z_1 = W_1 x$ dan layer 2 adalah $z_2 = W_2 z_1$:
$$ z_2 = W_2 (W_1 x) = (W_2 W_1) x = W_{\text{gabungan}} x $$
Dua matriks perkalian berturut-turut hanyalah sebuah matriks baru. Jaringan tanpa aktivasi tidak akan pernah bisa mempelajari hubungan non-linear (seperti pola melingkar, XOR, atau persepsi visual). Fungsi aktivasi memberikan kemampuan "menekuk" dan "melipat" ruang fitur agar data yang tidak terpisahkan secara linear (*linearly non-separable*) dapat dipisahkan.

## Struktur Berlapis & Anatomi Dense Layer

Dalam arsitektur klasik Multilayer Perceptron (MLP), lapisan-lapisan penyusunnya disebut **Dense Layer** (atau *Fully Connected Layer* / *Linear Layer*).

### Mengapa Disebut "Dense" (Padat)?
Disebut *dense* karena **setiap neuron di lapisan ini memiliki sambungan kabel/bobot ke SELURUH neuron di lapisan sebelumnya**. Tidak ada input yang dilewati atau diabaikan secara spasial.

```
Layer Sebelumnya (Input x)        Lapisan Dense (Output y)
       ( x1 ) ───────────┬───────────> ( y1 )
               ╲       ╱   ╲       ╱
                ╲     ╱     ╲     ╱
       ( x2 ) ───┼───┼───────┼───┼───> ( y2 )
                ╱     ╲     ╱     ╲
               ╱       ╲   ╱       ╲
       ( x3 ) ───────────┴───────────> ( y3 )
   [Setiap input terhubung ke semua neuron output = Densely Connected]
```

Secara matematis, satu Dense layer mengeksekusi operasi aljabar linear:
$$ y = \sigma(W x + b) $$

**Keterangan variabel:**
- $x \in \mathbb{R}^n$: Vektor input berukuran $n$.
- $W \in \mathbb{R}^{m \times n}$: Matriks bobot berukuran $m \times n$, di mana $m$ adalah jumlah neuron pada layer saat ini dan $n$ adalah jumlah neuron dari layer sebelumnya.
- $b \in \mathbb{R}^m$: Vektor bias berukuran $m$.
- $\sigma(\cdot)$: Fungsi aktivasi non-linear (misal ReLU, Sigmoid, Softmax).
- $y \in \mathbb{R}^m$: Vektor output representasi baru.

### Peran dan Batasan Dense Layer
1. **Wajib Flatten:** Dense layer tidak memahami konsep baris, kolom, atau kanal (2D/3D). Jika inputnya berupa citra atau spektrogram, data harus diratakan (*flatten*) menjadi vektor 1D terlebih dahulu.
2. **Koneksi Global:** Cocok untuk data tabular atau fitur abstrak yang sudah tidak terikat koordinat fisik tertentu.
3. **Peran dalam CNN:** Dalam visi komputer, lapisan konvolusi ([[Convolutional Layer]]) bertugas di depan sebagai *feature extractor*, sedangkan Dense layer diletakkan di bagian paling akhir sebagai *classifier head* untuk memetakan kombinasi fitur abstrak menjadi probabilitas kelas (misal: memprediksi apakah gambar tersebut mobil, kucing, atau pesawat).

## Hierarki Representasi: Dari Tepi ke Objek

Neural network modern menyusun neuron dalam tiga jenis lapisan fungsional:
- **Input Layer:** Tempat data mentah masuk (tidak ada komputasi bobot di sini).
- **Hidden Layer(s):** Lapisan perantara tempat fitur diekstraksi. Semakin dalam layer, semakin abstrak konsep yang dipelajari:
  - Layer 1: Garis tepi, sudut, kontras cahaya.
  - Layer 2: Pola geometris, tekstur gabungan (misal hidung, mata, sudut pintu).
  - Layer 3+: Objek utuh (wajah, mobil, teks).
- **Output Layer:** Menghasilkan prediksi akhir (probabilitas kelas untuk klasifikasi, nilai kontinu untuk regresi).

### Fitur Emergent & Fenomena "Black-Box"
Kita **tidak pernah secara eksplisit menyuruh** jaringan: *"Layer 1 tolong deteksi garis, Layer 2 tolong deteksi roda."*
- **Sifat *Emergent*:** Fitur berjenjang terbentuk secara otomatis murni sebagai efek samping optimasi matematis meminimalkan Loss function di layer paling ujung.
- **Apakah Kita Tahu Apa yang Dideteksi Tiap Layer?**
  - **Secara default (in practice):** Sering kali dianggap *black-box* karena satu neuron bisa merespons banyak konsep sekaligus (*polysemanticity*) akibat kompresi ruang representasi vektor (*superposition*).
  - **Secara analisis (*Mechanistic Interpretability* & *Feature Visualization*):** Kita bisa membedah isi layer. Pada CNN, visualisasi aktivasi membuktikan filter layer awal konsisten membentuk filter Gabor (tepi/sudut). Pada model bahasa (LLM), interpretability membedah sirkuit neuron yang mendeteksi konsep sintaksis, logika penalaran, atau entitas tertentu.

## Siklus Belajar Neural Network

Neural network belajar melalui loop 3 tahap sederhana yang diulang ribuan/jutaan kali:
1. **Menebak (Forward Pass):** Masukkan data $x$, hitung $z$ dan $a$ sampai ke layer output, menghasilkan tebakan $\hat{y}$.
2. **Mengukur Kesalahan (Loss Function):** Hitung jarak selisih antara tebakan $\hat{y}$ dengan kenyataan target $y$ menggunakan fungsi seperti MSE atau Cross-Entropy:
   $$ \mathcal{L}(y, \hat{y}) $$
3. **Mengoreksi Kenop Bobot (Backward Pass & Optimizer):**
   - Hitung gradien sensitivitas kesalahan terhadap setiap bobot via [[Backpropagation]].
   - Geser nilai bobot berlawanan arah dengan gradien via algoritma Optimizer (misal Gradient Descent):
     $$ W \leftarrow W - \eta \nabla_W \mathcal{L} $$

> [!abstract]- Quick Reference
> | Konsep | Persamaan Matematika | Peran Konseptual |
> | :--- | :--- | :--- |
> | **Pre-aktivasi** | $z = Wx + b$ | Proyeksi linear / kombinasi bobot |
> | **Aktivasi (ReLU)** | $a = \max(0, z)$ | Memberikan sifat non-linearitas |
> | **Aktivasi (Sigmoid)** | $a = \frac{1}{1 + e^{-z}}$ | Memampatkan nilai ke probabilitas $(0, 1)$ |
> | **Loss (MSE)** | $\mathcal{L} = \frac{1}{2}(\hat{y} - y)^2$ | Menghitung penalti kesalahan kuadrat |
> | **Update (SGD)** | $W \leftarrow W - \eta \frac{\partial \mathcal{L}}{\partial W}$ | Koreksi parameter menuju titik minimum error |

> [!question]- Practice
> **Soal 1:** Jika sebuah neural network memiliki 5 hidden layer dengan masing-masing 100 neuron, tetapi seluruh fungsi aktivasinya dihilangkan (hanya $a = z$), model tersebut setara dengan model apa?
> 
> > [!check]- Answer
> > Model tersebut secara matematis reduksi menjadi **satu model Regresi Linear tunggal**. Perkalian matriks linear berulang kali $W_5 \cdot W_4 \cdot W_3 \cdot W_2 \cdot W_1$ menghasilkan satu matriks transformasi linear tunggal $W_{\text{final}}$.
> 
> **Soal 2:** Apa fungsi dari parameter bias ($b$) jika kita sudah memiliki bobot ($w$)?
> 
> > [!check]- Answer
> > Tanpa bias ($b=0$), fungsi garis keputusan $z = wx$ akan selalu dipaksa melewati titik pusat koordinat origin $(0,0)$. Bias memberi kebebasan translasi/pergeseran garis ke kiri-kanan atau atas-bawah pada bidang ruang fitur.

> [!info]- Going Deeper
> - **Universal Approximation Theorem (Cybenko, 1989):** Membuktikan bahwa feedforward neural network dengan hanya satu hidden layer dan fungsi aktivasi non-linear mampu mengaproksimasi fungsi kontinu apapun dengan tingkat presisi berapapun, asalkan jumlah neuron di hidden layer cukup besar.
> - **Koneksi Lanjutan:** Untuk memahami bagaimana jaringan ini mencari tahu bagian mana dari bobot yang harus diubah saat terjadi kesalahan prediksi, pelajari mekanisme [[Backpropagation]].
