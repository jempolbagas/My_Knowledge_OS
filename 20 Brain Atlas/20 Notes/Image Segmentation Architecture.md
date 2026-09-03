---
type: note
title: "Image Segmentation Architecture"
subject: "Computer Vision"
created: 2026-09-03
prerequisites:
  - "[[Neural Networks]]"
tags:
  - computer-vision
  - deep-learning
  - image-segmentation
  - encoder-decoder
---

Segmentasi citra adalah tugas visi komputer untuk melakukan klasifikasi tingkat piksel (*dense prediction*), di mana setiap piksel dalam citra berdimensi $H \times W$ dipetakan ke kelas semantik atau objek tertentu. Mayoritas arsitektur segmentasi dibangun di atas paradigma **Encoder-Decoder**, sebuah mekanisme yang menyeimbangkan dua kebutuhan berlawanan: abstraksi semantik global (*"objek apa ini?"*) dan lokalisasi spasial presisi (*"di mana batas pikselnya?"*).

```
Input (H x W x 3)
       │
   [ Encoder ]       ──> Ekstraksi fitur semantik, resolusi spasial turun (H/32, W/32), Channel naik
       │         \
       │       [Skip Connections] (Menyelamatkan koordinat batas presisi)
       ▼         /
   [ Decoder ]       ──> Rekonstruksi spasial bertahap kembali ke resolusi (H x W)
       │
Output Mask (H x W x K)
```

## Masalah Mendasar: Mengapa Klasifikasi Biasa Gagal?

Model klasifikasi standar (seperti ResNet atau VGG) dirancang untuk membuang dimensi spasial sepenuhnya. Di ujung jaringan klasifikasi, representasi 2D diratakan (*flattened*) atau di-pooling menjadi vektor 1D ($1 \times C$) sebelum masuk ke layer linear.

Pada segmentasi citra:
1. **Output wajib berupa peta 2D ($H \times W \times K$):** Lokasi geometris setiap piksel tidak boleh hilang.
2. **Konflik Resolusi vs. Semantik:** 
   - Untuk mengenali bahwa suatu piksel adalah bagian dari "bus kota", model butuh jangkauan pandang (*receptive field*) luas hingga ratusan piksel di sekitarnya.
   - Namun, untuk menentukan batas tepi jendela bus hingga ketelitian 1 piksel, model butuh resolusi spasial penuh tanpa kompresi.

## Paradigma Encoder-Decoder

Arsitektur segmentasi memecah alur komputasi menjadi dua fase yang bertemu pada sebuah titik kompresi (*bottleneck*):

```
Encoder (Downsampling)              Decoder (Upsampling)
H x W x 3  ───────────────────────────────> H x W x K
    │                                           ▲
    ▼                                           │
H/2 x W/2 x 64  ───────────────────────> H/2 x W/2 x 64
        │                                   ▲
        ▼                                   │
    H/4 x W/4 x 128  ───────────────> H/4 x W/4 x 128
            │                               ▲
            ▼                               │
        H/8 x W/8 x 256  ───────> H/8 x W/8 x 256
                │                       ▲
                ▼                       │
            [ Bottleneck: H/32 x W/32 x 512 ]
```

### 1. Encoder (Kompresi Spasial & Ekspansi Channel)
Encoder bertindak sebagai pengekstraksi fitur hierarkis (sering menggunakan *backbone* berbasis [[Residual Block|ResNet]], EfficientNet, atau Vision Transformer).
* **Mereduksi Dimensi Spasial ($H, W \downarrow$):** Menggunakan *strided convolution* atau *max pooling* untuk mengecilkan resolusi grid (misal $512 \times 512 \to 256 \to 128 \to \dots \to 16 \times 16$). Ini memperluas receptive field secara eksponensial dan memangkas biaya komputasi.
* **Meningkatkan Jumlah Channel ($C \uparrow$):** Menambah filter konvolusi (misal $3 \to 64 \to 128 \to 256 \to 512$). Setiap channel baru berfungsi sebagai detektor pola semantik tingkat tinggi (garis tepi $\to$ tekstur $\to$ bagian organ/komponen $\to$ identitas objek utuh).

> [!note] Apakah Segmentasi Terjadi di Encoder?
> **Tidak.** Di dalam encoder belum terjadi segmentasi sama sekali. Encoder murni melakukan **Feature Extraction**:
> 1. Encoder tidak menghasilkan masker dan belum memisahkan objek; koordinat piksel aslinya bahkan sudah terdistorsi akibat downsampling.
> 2. Yang dihasilkan hanyalah kumpulan deskriptor fitur (*"di area sekitar ini ada sinyal kuat untuk tekstur bulu dan kontras melingkar"*).
> 3. Keputusan klasifikasi per-piksel (*segmentasi aktual*) baru dieksekusi di ujung **Decoder** bersama **Prediction Head** ($1 \times 1$ convolution).

#### Peran Transfer Learning: Mengapa Meminjam Model ImageNet?
Dalam praktiknya, encoder segmentasi jarang dilatih dari nol (*from scratch*). Kebanyakan menggunakan model klasifikasi gambar yang sudah *pre-trained* pada dataset **ImageNet** (1,4+ juta gambar, 1.000 kelas objek):
* **Tugas Asli di ImageNet:** Model hanya dilatih menebak **1 label teks untuk satu gambar utuh** (misal: `"Golden Retriever"`). Model tidak pernah diminta menunjukkan koordinat $(x, y)$ objek ataupun memisahkan piksel anjing dari rumput.
* **Mengapa Tetap Dipakai?** Untuk bisa menebak 1.000 kelas objek yang rumit, jaringan terpaksa harus belajar memahami fitur visual fundamental (garis, sudut, tekstur, bentuk anatomis).
* **Mekanisme Transplantasi:** Kita memotong dan **membuang kepala klasifikasi** (lapisan output 1.000 kelas di ujung), mempertahankan "badan" pengekstraksi fiturnya sebagai **Encoder**, lalu menyambungkannya ke **Decoder baru** yang dilatih khusus memetakan piksel.

### 2. Bottleneck (Ruang Laten Kompresi)
Titik terdalam di mana feature map memiliki resolusi spasial terkecil namun kedalaman channel semantik paling kaya. Informasi redundan (seperti variasi pencahayaan dan derau piksel lokal) disaring, menyisakan representasi konsep esensial dari citra.

### 3. Decoder (Rekonstruksi & Proyeksi Masker)
Decoder bertugas mengembalikan dimensi spasial kembali ke ukuran input $H \times W$:
* **Upsampling:** Menggunakan *Bilinear Interpolation*, *Transposed Convolution* (Deconvolution), atau *PixelShuffle*.
* **Prediction Head:** Konvolusi akhir $1 \times 1$ yang memproyeksikan channel fitur ke sejumlah $K$ kelas target, lalu diaktivasi menggunakan **Softmax** (untuk multikelas yang saling eksklusif) atau **Sigmoid** (untuk segmentasi biner/multi-label per piksel).

## Anatomi Tensor: Spasial vs. Channel

Perubahan bentuk tensor di sepanjang jaringan mencerminkan pertukaran (*trade-off*) antara presisi koordinat dan kekayaan pemahaman semantik:

| Tahap | Dimensi Tensor | Makna Spasial ($H \times W$) | Makna Channel ($C$) |
| :--- | :--- | :--- | :--- |
| **Input Citra** | $512 \times 512 \times 3$ | **Sangat Presisi:** Memiliki $262.144$ koordinat piksel individual. | **Sangat Dangkal:** Hanya nilai intensitas warna dasar (Red, Green, Blue). |
| **Layer Awal** | $256 \times 256 \times 64$ | Presisi tinggi, sedikit kompresi. | Detektor tepi (*edge*), orientasi sudut, gradien kontras. |
| **Bottleneck** | $16 \times 16 \times 512$ | **Sangat Kasar:** $1$ sel grid mewakili area seluas $32 \times 32$ piksel asli. | **Sangat Kaya:** $512$ skor aktivasi konsep objek tingkat tinggi (roda, wajah, organ). |
| **Output Mask** | $512 \times 512 \times K$ | Direkonstruksi kembali ke koordinat piksel penuh. | Skor probabilitas bahwa piksel tersebut milik kelas ke-$k$. |

## Solusi Kehilangan Batas: Skip Connections

Kelemahan bawaan dari downsampling pada Encoder adalah **kehilangan detail batas spasial halus**. Saat Decoder merekonstruksi mask hanya dari bottleneck, batas objek akan tumpul atau bergeser.

**U-Net** mengatasi hal ini dengan **Skip Connections**:
* Saluran langsung menyambungkan feature map resolusi tinggi dari Encoder ke tahap Decoder yang memiliki dimensi setara (biasanya melalui operasi konkatenasi matriks).
* **Mekanisme kerja:** Decoder menerima dua sinyal sekaligus:
  1. Informasi semantik global dari jalur bawah (memahami *apa* objeknya).
  2. Informasi koordinat lokal dari jalur skip (memahami *di mana* batas tepinya).

## Spektrum Tugas Segmentasi

Arsitektur segmentasi disesuaikan dengan jenis label yang dihasilkan:
1. **Semantic Segmentation:** Setiap piksel diberi label kelas tanpa membedakan individu objek (misal: semua mobil diberi nilai kelas yang sama). Contoh arsitektur: *FCN, U-Net, DeepLabV3+, SegFormer*.
2. **Instance Segmentation:** Mendeteksi dan memisahkan setiap objek individual (*things*). Model membedakan "mobil 1" dan "mobil 2". Contoh arsitektur: *Mask R-CNN* (deteksi bounding box terlebih dahulu, kemudian masking).
3. **Panoptic Segmentation:** Menyatukan segmentasi semantik untuk latar belakang tak terhitung (*stuff*, seperti langit, jalan) dan segmentasi instans untuk objek diskret (*things*). Contoh arsitektur: *Mask2Former*.

> [!abstract]- Quick Reference
> * **Tujuan Utama:** Dense classification per piksel ($H \times W \times K$).
> * **Fungsi Encoder:** $H, W \downarrow$ (receptive field membesar, efisiensi memori), $C \uparrow$ (fitur semantik makin abstrak).
> * **Fungsi Decoder:** $H, W \uparrow$ (mengembalikan resolusi ke ukuran input), $C \downarrow$ (fokus ke pemetaan kelas).
> * **Fungsi Skip Connection:** Memulihkan informasi koordinat presisi dan tepian tajam yang terbuang saat downsampling di encoder.
> * **Fungsi Bottleneck:** Memaksa kompresi representasi agar model fokus pada esensi objek, bukan noise piksel.

> [!question]- Practice
> 1. Mengapa kita tidak memproses citra pada resolusi penuh $1024 \times 1024$ dari awal hingga akhir tanpa pernah melakukan downsampling?
> > [!check]- Answer
> > Dua alasan utama:
> > 1. **Beban Komputasi:** Biaya komputasi konvolusi berskala linear terhadap luas spasial ($H \times W \times C_{in} \times C_{out}$). Mempertahankan resolusi tinggi dengan ratusan channel di puluhan layer akan memicu *Out-Of-Memory* (OOM).
> > 2. **Keterbatasan Receptive Field:** Tanpa downsampling, kernel $3 \times 3$ hanya memperbesar jangkauan pandang secara linear yang lambat. Model akan gagal memahami konteks objek berukuran besar karena tidak bisa "melihat" hubungan antar-wilayah yang berjauhan.
>
> 2. Pada arsitektur U-Net, apa perbedaan informasi yang dibawa oleh jalur *Skip Connection* dibandingkan jalur utama yang datang dari *Bottleneck*?
> > [!check]- Answer
> > Jalur *Bottleneck* membawa representasi **semantik tingkat tinggi** (konsep objek global, namun kehilangan posisi spasial presisi akibat pooling). Jalur *Skip Connection* membawa representasi **spasial tingkat rendah** (koordinat tepat, tepi tajam, tekstur, namun minim pemahaman konteks semantik global). Keduanya digabungkan agar hasil segmentasi akurat secara kelas dan presisi secara batas piksel.
>
> 3. Apakah di dalam Encoder sudah terjadi proses segmentasi? Mengapa model klasifikasi ImageNet bisa langsung dicangkokkan menjadi Encoder segmentasi?
> > [!check]- Answer
> > **Tidak.** Encoder murni melakukan *feature extraction* tanpa menghasilkan masker atau memisahkan objek. Model ImageNet awalnya hanya dilatih menebak satu label per gambar utuh tanpa diminta memetakan piksel. Namun, proses tersebut melatih jaringan mengenali pola visual universal (tepi, tekstur, geometri). Kita membuang kepala klasifikasinya (layer 1000-kelas) dan memanfaatkan "badan"-nya sebagai Encoder, sedangkan keputusan klasifikasi per-piksel (*segmentasi aktual*) diserahkan ke Decoder dan Prediction Head.

> [!info]- Going Deeper
> * **ResUNet & Dual Skip Connections:** Menggabungkan long skip connections milik U-Net dengan short skip connections dari [[Residual Block]] di setiap tingkat resolusi encoder dan decoder.
> * **DeepLab & Atrous (Dilated) Convolutions:** Alternatif untuk memperlebar receptive field tanpa membuang resolusi spasial terlalu agresif via *Atrous Spatial Pyramid Pooling* (ASPP).
> * **Transformer-based Segmentation:** Pendekatan modern seperti *SegFormer* (hierarchical ViT) dan *Mask2Former* (mask classification dengan masked attention).
> * **Loss Functions Khusus Segmentasi:** Mengapa Cross-Entropy standar rentan bias pada *class imbalance* (misal: luas latar belakang 98% vs objek 2%), dan bagaimana *Dice Loss* serta *Focal Loss* menstabilkan gradien training.
