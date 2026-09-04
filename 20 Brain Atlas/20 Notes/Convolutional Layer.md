---
type: note
title: "Convolutional Layer"
subject: "Computer Vision"
created: 2026-09-03
prerequisites:
  - "[[Neural Networks]]"
  - "[[Convolution]]"
  - "[[Dot Product]]"
tags:
  - deep-learning
  - computer-vision
  - cnn
  - architecture
---

Lapisan konvolusi (*convolutional layer*) adalah unit pemrosesan fundamental dalam arsitektur Convolutional Neural Network (CNN) yang bertugas mengekstraksi fitur spasial lokal dari data terstruktur (seperti citra, audio, atau volume 3D). Berbeda dengan *fully connected (dense) layer* yang menghubungkan setiap neuron ke seluruh input secara global, lapisan konvolusi memanfaatkan sekumpulan matriks bobot berukuran kecil—disebut kernel atau filter—yang digeser melintasi input untuk menghitung perkalian titik ([[Dot Product]]) lokal. Mekanisme ini menerapkan dua prinsip utama: *sparse connectivity* (konektivitas lokal) dan *weight sharing* (berbagi bobot), sehingga mampu mengenali pola visual yang konsisten (*translation equivariance*) dengan jumlah parameter yang jauh lebih hemat.

## Mengapa Bukan Dense Layer Biasa?

Untuk memahami hakikat lapisan konvolusi, tinjau kegagalan struktural lapisan Dense (*fully connected*) saat memproses citra:

1. **Ledakan Parameter Komputasi:**
   Misalkan sebuah citra berukuran $1000 \times 1000$ dengan 3 channel warna (RGB) memiliki $3.000.000$ nilai piksel. Jika input ini dihubungkan langsung ke lapisan Dense pertama dengan hanya $1000$ neuron:
   $$ \text{Bobot} = 3.000.000 \times 1000 = 3.000.000.000 \text{ parameter} $$
   Tiga miliar parameter pada satu layer akan menghabiskan memori GPU dan menyebabkan *overfitting* fatal.

2. **Kehilangan Struktur Topologi Spasial:**
   Lapisan Dense mewajibkan input diratakan (*flatten*) menjadi vektor 1D. Proses perataan ini menghancurkan relasi kedekatan antar-piksel (piksel di koordinat $(x, y)$ kehilangan relasi geometris dengan $(x, y+1)$). Padahal, informasi visual sangat bergantung pada kedekatan lokal (*spatial locality*).

3. **Ketiadaan Invariansi Translasi:**
   Jika sebuah neuron Dense belajar mengenali mata kucing di pojok kiri atas, neuron tersebut tidak akan bisa mengenali mata kucing yang sama jika letaknya bergeser ke pojok kanan bawah. Model harus mempelajari ulang pola tersebut untuk setiap posisi piksel.

Lapisan konvolusi menyelesaikan ketiga problem ini secara elegan melalui **koneksi lokal** dan **berbagi parameter**.

---

## Mekanisme Operasional: Bagaimana Lapisan Konvolusi Bekerja?

Lapisan konvolusi memproses input bukan sebagai deretan neuron lepas, melainkan sebagai volume tensor.

### 1. Sparse Connectivity (Konektivitas Lokal)
Setiap neuron pada *feature map* (output) hanya terhubung ke wilayah kecil pada input yang disebut **receptive field**. Ukuran wilayah ini ditentukan oleh ukuran kernel (umumnya $3 \times 3$ atau $5 \times 5$). Piksel yang jauh tidak dihubungkan secara langsung di lapisan awal.

### 2. Weight Sharing (Pembagian Bobot)
Satu filter konvolusi berukuran $K \times K$ memiliki matriks bobot yang nilainya **tetap sama** saat digeser dari ujung kiri atas hingga kanan bawah citra. 
- Jika filter tersebut belajar mendeteksi tepi vertikal, maka filter yang sama akan memindai dan mendeteksi tepi vertikal di **seluruh** bagian gambar.
- Bobot kernel diperbarui secara simultan melalui gradien akumulatif via [[Backpropagation]].

## Intuisi Fisis: Dot Product sebagai "Stempel Pola" (*Pattern Matcher*)

Jika perkalian titik hanya dipandang sebagai hitungan aljabar biasa, esensi fisis konvolusi akan kabur. Secara vektor, perkalian titik $\vec{a} \cdot \vec{b} = \|\vec{a}\| \|\vec{b}\| \cos(\theta)$ mengukur **tingkat kemiripan arah / bentuk**:
- Pola identik $\to$ nilai positif maksimal (neuron "berteriak" / aktivasi meledak).
- Pola acak / tidak berhubungan $\to$ mendekati nol.
- Pola berlawanan arah $\to$ bernilai negatif.

### Contoh Nyata: Filter Pendeteksi Tepi Vertikal
Tinjau sebuah kernel $3 \times 3$ yang dirancang khusus:
```
Kernel:
-1   2  -1
-1   2  -1
-1   2  -1
```
- **Angka $+2$ di tengah bertindak sebagai *Exciter* (Penguat).**
- **Angka $-1$ di kiri-kanan bertindak sebagai *Inhibitor* (Penghukum/Peredam).**

1. **Menimpa Garis Vertikal Terang di Latar Gelap:**
   Kolom tengah bernilai $1$, kolom samping bernilai $0$:
   $$ \text{Output} = 3 \times [(-1 \cdot 0) + (2 \cdot 1) + (-1 \cdot 0)] = +6 $$
   Neuron menghasilkan aktivasi sangat tinggi $+6$—ia "menstabilo" keberadaan garis vertikal.
2. **Menimpa Area Hitam Kosong ($0$ semua):**
   $$ \text{Output} = 0 $$
   Neuron diam (tidak ada fitur menarik).
3. **Menimpa Bidang Putih Polos ($1$ semua):**
   $$ \text{Output} = 3 \times [(-1 \cdot 1) + (2 \cdot 1) + (-1 \cdot 1)] = 3 \times (0) = 0 $$
   Neuron tetap diam! Karena *exciter* ($+2$) dan *inhibitor* ($-1 - 1 = -2$) saling meniadakan secara presisi. Filter ini terbukti hanya merespons **kontras perubahan garis tepi**, bukan warna polos.

---

## Apa Saja yang Dikoreksi saat Backpropagation?

Dalam visi komputer (terutama segmentasi citra), parameter yang di-update oleh [[Backpropagation]] bukan hanya satu jenis:
1. **Elemen Bobot Kernel:** Angka-angka di dalam matriks kernel ($C_{in} \times K_h \times K_w$) itulah *weights* yang diputar nilainya agar membentuk filter pendeteksi pola yang optimal.
2. **Bias ($b$):** Satu skalar per filter untuk menggeser ambang batas aktivasi (*threshold*).
3. **Parameter Normalisasi (Batch Normalization / GroupNorm):** Parameter $\gamma$ (*scale*) dan $\beta$ (*shift*) yang dipelajari untuk menjaga stabilitas sebaran aktivasi antar-lapisan.
4. **Kernel Up-sampling (Transposed Convolution):** Pada arsitektur segmentasi (seperti [[Image Segmentation Architecture]]), decoder menggunakan kernel pembalik yang bobotnya juga dipelajari untuk merekonstruksi resolusi detail.
5. **Prediction Head ($1 \times 1$ Convolution):** Pengganti Dense layer di akhir segmentasi yang memetakan puluhan channel fitur menjadi $C$ label kelas per piksel.

---

## Dinamika Downsampling: Dimensi Spasial ($H, W \downarrow$) vs. Kedalaman Kanal ($C \uparrow$)

Selama tahap ekstraksi fitur (Encoder), terjadi pertukaran representasi yang disengaja: **mengorbankan resolusi fisik demi kedalaman makna semantik**.

```
Input Awal:                                    Lapisan Dalam (Bottleneck):
Resolusi Spasial Luas tapi Tipis               Resolusi Spasial Menciut tapi Sangat Tebal
  ┌─────────────────┐                                  ┌───┐
  │  512 x 512 px   │                                  │16x│
  │                 │        ───────────────>          │16 │
  └─────────────────┘                                  └───┘
   (3 Channel RGB)                                      (512 Feature Maps Berbeda)
```

- **Sumbu Spasial ($H, W$) Menjawab: *"DI MANA?" (Where)*:**
  Di awal, resolusi besar memberitahu koordinat fisik piksel dengan presisi, tetapi model belum paham konteks objeknya.
- **Sumbu Kanal ($C$) Menjawab: *"BENDA APA ITU?" (What)*:**
  Setiap 1 lembar feature map mewakili 1 konsep fitur unik (misal: channel 1 = pantulan logam, channel 50 = kurva roda, channel 512 = tekstur mata).
Semakin dalam jaringan, resolusi koordinat diperkecil agar beban komputasi terkendali dan receptive field meluas, sementara variasi kanal diperbanyak untuk memperkaya kosakata konsep visual model.

---

## Operasi Multi-Channel di Dunia Nyata (3D Tensor)

Banyak pemula membayangkan konvolusi hanya berupa matriks 2D yang meluncur di atas matriks 2D. Pada arsitektur nyata, konvolusi beroperasi pada **volume 3D**.

Misalkan input memiliki kedalaman channel $C_{in}$ (misal 3 channel untuk RGB, atau 64 channel dari layer sebelumnya):
- **Setiap 1 unit filter** sebenarnya berbentuk balok 3D berukuran $C_{in} \times K_h \times K_w$. Kedalaman filter selalu sama persis dengan kedalaman channel input.
- Filter menghitung perkalian titik pada seluruh channel secara simultan, menjumlahkan semua hasilnya, lalu menambahkan $1$ nilai bias skalar.
- Hasil dari 1 filter 3D adalah **satu lembar 2D feature map**.
- Jika lapisan konvolusi memiliki $C_{out}$ filter berbeda, maka lapisan tersebut akan menghasilkan $C_{out}$ lembar feature map yang ditumpuk menjadi tensor 3D baru: $[C_{out}, H_{out}, W_{out}]$.

```
[ Input Tensor ]             [ Sekumpulan Filter 3D ]                 [ Output Tensor ]
(C_in x H x W)               (C_out filter, masing-masing:           (C_out x H_out x W_out)
                             C_in x K_h x K_w)
     ┌───┐                          ┌───┐                                 ┌───┐
     │RGB│    *  [Filter 1]  ───>   │ 1 │ (Feature Map 1)                 │   │
     │   │       [Filter 2]  ───>   │ 2 │ (Feature Map 2)         ───>    │   │ (C_out channels)
     └───┘          ...                ...                                │   │
                 [Filter N]  ───>   │ N │ (Feature Map N)                 └───┘
```

---

## Formulasi Matematika & Aturan Dimensi

### 1. Perhitungan Ukuran Output Spasial
Dimensi spasial tinggi ($H_{out}$) dan lebar ($W_{out}$) dari feature map ditentukan oleh empat hiperparameter: ukuran input ($H, W$), ukuran kernel ($K$), jumlah padding ($P$), dan stride pergeseran ($S$):

$$ H_{out} = \left\lfloor \frac{H - K_h + 2P}{S} \right\rfloor + 1 $$
$$ W_{out} = \left\lfloor \frac{W - K_w + 2P}{S} \right\rfloor + 1 $$

**Keterangan variabel:**
- $H, W$: Tinggi dan lebar matriks input spasial.
- $K_h, K_w$: Tinggi dan lebar kernel (filter).
- $P$: Jumlah lapisan padding nol (*zero-padding*) yang ditambahkan di sisi luar input.
- $S$: *Stride*, yaitu besar langkah pergeseran kernel piksel demi piksel ($S=1$ geser satu piksel, $S=2$ melompati dua piksel).
- $\lfloor \cdot \rfloor$: Fungsi *floor* (pembulatan ke bawah).

### 2. Perhitungan Jumlah Parameter Bobot yang Dilatih
Jumlah parameter yang dapat dilatih (*learnable parameters*) pada satu lapisan konvolusi tidak bergantung pada resolusi spasial gambar ($H \times W$), melainkan hanya pada dimensi filter:

$$ \text{Total Parameter} = \Big( (C_{in} \times K_h \times K_w) + 1 \Big) \times C_{out} $$

**Keterangan variabel:**
- $C_{in}$: Jumlah channel input yang masuk ke lapisan.
- $K_h, K_w$: Dimensi spasial kernel.
- $+ 1$: Satu parameter bias untuk setiap filter.
- $C_{out}$: Jumlah filter yang digunakan (jumlah channel output yang dihasilkan).

---

## Worked Example: Menghitung Dimensi dan Parameter Layer Konvolusi

Misalkan sebuah model komputer visi menerima citra medis monokrom $1 \text{ channel}$ berukuran $128 \times 128$. Lapisan konvolusi pertama dikonfigurasi dengan:
- Jumlah filter output: $C_{out} = 16$
- Ukuran kernel: $K = 3 \times 3$
- Padding: $P = 1$ (Same padding)
- Stride: $S = 2$ (Downsampling)

### Langkah 1: Hitung Dimensi Output
$$ H_{out} = \left\lfloor \frac{128 - 3 + 2(1)}{2} \right\rfloor + 1 = \left\lfloor \frac{127}{2} \right\rfloor + 1 = 63 + 1 = 64 $$
$$ W_{out} = 64 $$
Tensor output yang keluar dari lapisan ini berukuran $[16, 64, 64]$.

### Langkah 2: Hitung Total Parameter Bobot
$$ \text{Bobot per filter} = C_{in} \times K_h \times K_w = 1 \times 3 \times 3 = 9 $$
$$ \text{Bias per filter} = 1 $$
$$ \text{Total parameter} = (9 + 1) \times 16 = 160 \text{ parameter} $$

> [!important] Efisiensi Ekstrem
> Lapisan ini berhasil mereduksi citra $128 \times 128$ dan mengekstrak 16 variasi fitur spasial yang berbeda hanya dengan **160 angka parameter**. Jika menggunakan Dense layer, ukuran bobot akan mencapai puluhan juta.

---

## Hierarki Representasi Visual

Ketika beberapa lapisan konvolusi ditumpuk secara berurutan bersama fungsi aktivasi non-linear (seperti ReLU), model secara otomatis membentuk representasi hierarkis:

1. **Lapisan Awal (Shallow Layers):** Receptive field kecil. Belajar mendeteksi fitur primitif: tepi garis lurus horizontal/vertikal, gradien warna, dan sudut tajam.
2. **Lapisan Menengah (Mid-level Layers):** Receptive field meluas. Menggabungkan tepian menjadi motif visual: tekstur, kurva, pola kisi, bentuk geometris dasar.
3. **Lapisan Dalam (Deep Layers):** Receptive field mencakup hampir seluruh citra. Menggabungkan motif menjadi bagian semantik objek: roda mobil, mata manusia, moncong hewan.
Arsitektur modern seperti [[Residual Block]] dan [[Image Segmentation Architecture]] memanfaatkan hierarki ini untuk klasifikasi dan segmentasi piksel presisi tinggi.

---

> [!abstract]- Quick Reference
> - **Fungsi Utama:** Ekstraktor fitur spasial lokal dengan efisiensi parameter tinggi.
> - **Dua Sifat Kunci:** *Sparse Connectivity* (receptive field terbatas) & *Weight Sharing* (filter yang sama digeser ke seluruh area).
> - **Dimensi Output Spasial:**
>   $$ O = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1 $$
> - **Total Parameter:**
>   $$ \text{Params} = (C_{in} \cdot K_h \cdot K_w + 1) \cdot C_{out} $$
> - **Peran Stride ($S > 1$):** Melakukan reduksi ukuran spasial (downsampling) tanpa perlu pooling terpisah.
> - **Peran Padding ($P$):** Menjaga dimensi batas dan mencegah informasi di pinggir citra hilang tergerus konvolusi berulang.

---

> [!question]- Practice
> **Soal 1:** Sebuah lapisan konvolusi menerima input tensor dengan bentuk $[64, 56, 56]$ (artinya 64 channels, dimensi spasial $56 \times 56$). Lapisan tersebut menerapkan 128 filter berukuran $3 \times 3$ dengan bias, padding $P = 1$, dan stride $S = 1$.
> a) Berapakah dimensi tensor output?
> b) Berapakah total parameter yang dapat dilatih (*trainable parameters*) pada lapisan tersebut?
> > [!check]- Answer
> > **a) Dimensi Output:**
> > $$ H_{out} = \left\lfloor \frac{56 - 3 + 2(1)}{1} \right\rfloor + 1 = 55 + 1 = 56 $$
> > Dimensi output spasial tetap $56 \times 56$. Karena terdapat 128 filter, dimensi output tensor adalah $[128, 56, 56]$.
> >
> > **b) Total Parameter:**
> > Tiap filter memiliki bobot: $C_{in} \times K_h \times K_w = 64 \times 3 \times 3 = 576$ bobot.
> > Ditambah 1 bias per filter = $577$ parameter per filter.
> > Total parameter untuk 128 filter:
> > $$ \text{Total} = 577 \times 128 = 73.856 \text{ parameter} $$
>
> **Soal 2:** Mengapa ukuran kedalaman (*depth*) dari sebuah kernel konvolusi harus selalu sama dengan jumlah channel input ($C_{in}$)?
> > [!check]- Answer
> > Karena operasi perkalian titik (*dot product*) konvolusi pada lapisan neural network harus memadukan informasi dari seluruh spektrum channel input pada patch spasial yang bersangkutan. Satu nilai pada feature map output merepresentasikan akumulasi sinyal dari seluruh channel input yang saling berkorelasi secara lokal.

---

> [!info]- Going Deeper
> - **$1 \times 1$ Convolution (Pointwise Convolution):** Konvolusi dengan kernel berukuran $1 \times 1$ tidak mengekstrak relasi spasial, melainkan berfungsi sebagai *channel pooling* atau proyeksi dimensi linier antar-channel untuk menghemat komputasi (digunakan secara ekstensif pada Inception dan ResNet bottleneck).
> - **Dilated (Atrous) Convolution:** Memperlebar receptive field tanpa menambah jumlah parameter dengan memberi celah (*holes*) antar bobot kernel (lihat penerapannya di [[Image Segmentation Architecture]]).
> - **Fondasi Matematika:** Lihat detail matematis pembalikan fungsi dan sifat aljabar konvolusi di [[Convolution]].
