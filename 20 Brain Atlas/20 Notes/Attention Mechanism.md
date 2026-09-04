---
type: note
title: "Attention Mechanism"
subject: "Machine Learning"
created: 2026-09-03
prerequisites:
  - "[[Neural Networks]]"
  - "[[Convolution]]"
  - "[[Dot Product]]"
tags:
  - deep-learning
  - attention
  - transformer
  - computer-vision
  - nlp
---

Mekanisme atensi (*attention mechanism*) adalah metode komputasi dalam deep learning yang memungkinkan model memusatkan "fokus" secara dinamis pada bagian data tertentu yang paling relevan dengan konteks saat itu, alih-alih memperlakukan seluruh input secara seragam. Jika lapisan konvolusi ([[Convolutional Layer]]) terkunci pada jendela spasial lokal yang kaku ($3 \times 3$) dan Dense layer ([[Neural Networks]]) memproses seluruh input dengan bobot tetap yang statis, atensi menghitung **bobot relevansi dinamis** antar-elemen (kata, token, atau *patch* citra) saat data mengalir (*runtime*). Mekanisme ini memecahkan problem dependensi jarak jauh (*long-range dependencies*) dan menjadi fondasi utama revolusi arsitektur Transformer di NLP maupun Computer Vision (Vision Transformer).

---

## Masalah yang Dipecahkan: Mengapa Konvolusi & RNN Kurang Efektif?

Sebelum atensi diciptakan, pemrosesan data sekuensial dan citra menghadapi dua kendala struktural:

1. **Bottleneck Memori pada RNN/LSTM:**
   RNN memproses data langkah demi langkah ($t_1 \to t_2 \to t_3 \to \dots$). Informasi dari awal kalimat dikompresi ke dalam satu vektor *hidden state* kecil. Akibatnya, pada kalimat panjang (50+ kata), informasi di awal kalimat memudar (*vanishing gradient* / lupa konteks).
2. **Keterbatasan Spasial Lokal pada Konvolusi:**
   Konvolusi hanya bisa menghubungkan piksel yang berdekatan ($3 \times 3$). Untuk menghubungkan piksel di pojok kiri atas dengan pojok kanan bawah, jaringan harus ditumpuk puluhan layer agar *receptive field*-nya mencapai ujung seberang. Ini lambat dan rentan kehilangan detail halus.

Atensi memotong rantai ini dengan menghubungkan **setiap elemen langsung ke semua elemen lainnya** dalam satu langkah komputasi ($\mathcal{O}(1)$ jalur komunikasi).

---

## Mental Model & Analogi: Mesin Pencari YouTube / Perpustakaan

Untuk memahami bagaimana atensi bekerja, gunakan analogi **sistem pencarian informasi**:

Bayangkan Anda sedang mencari materi belajar di platform video:
1. **Query ($Q$ - Kata Kunci Pencarian):**
   Apa yang sedang Anda butuhkan saat ini? (Misal: *"resep rendang padang"*).
2. **Key ($K$ - Label / Judul / Tag Video):**
   Identitas atau deskripsi singkat dari setiap video yang tersimpan di database.
3. **Value ($V$ - Isi Konten Video Sebenarnya):**
   Materi audio-visual asli di dalam video tersebut.

Proses yang terjadi:
- Sistem membandingkan **Query ($Q$)** Anda dengan seluruh **Key ($K$)** di database menggunakan perkalian titik (*dot product*) untuk mengukur tingkat kecocokan.
- Hasil kecocokan dinormalisasi menjadi persentase relevansi via Softmax:
  - Video A (Tag: *"resep rendang daging empuk"*): Relevansi **85%**.
  - Video B (Tag: *"kuliner khas padang"*): Relevansi **12%**.
  - Video C (Tag: *"cara servis motor"*): Relevansi **3%**.
- Anda menyerap informasi **Value ($V$)** dari masing-masing video secara proporsional sesuai persentase relevansinya:
  $$ \text{Informasi Akhir} = (0.85 \times \text{Isi A}) + (0.12 \times \text{Isi B}) + (0.03 \times \text{Isi C}) $$

Dalam neural network, $Q$, $K$, dan $V$ bukan teks string, melainkan **vektor numerik** yang diproyeksikan dari data input melalui matriks bobot yang dilatih.

---

## Formulasi Matematika: Scaled Dot-Product Attention

Bentuk kanonik dari atensi (Vaswani et al., 2017) dirumuskan sebagai:

$$ \text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V $$

**Keterangan variabel:**
- $Q \in \mathbb{R}^{N \times d_k}$: Matriks *Query* ($N$ elemen query, masing-masing berdimensi $d_k$).
- $K \in \mathbb{R}^{M \times d_k}$: Matriks *Key* ($M$ elemen key, berdimensi $d_k$).
- $V \in \mathbb{R}^{M \times d_v}$: Matriks *Value* ($M$ elemen value, berdimensi $d_v$).
- $K^T$: Transposisi matriks Key sehingga dimensi menjadi $d_k \times M$, memungkinkan perkalian matriks dengan $Q$.
- $d_k$: Dimensi vektor dari Key (dan Query).
- $\sqrt{d_k}$: Faktor penskalaan (*scaling factor*).
- $\text{softmax}(\cdot)$: Fungsi normalisasi baris agar total bobot atensi bernilai $1$ (probabilitas distribusi).

---

## Mengapa Rumusnya Dibuat Seperti Itu? (Bedah Logika Perhitungan)

Setiap operasi dalam rumus tersebut memiliki alasan fisis-matematis yang sangat spesifik:

### 1. Mengapa Perkalian Titik ($Q K^T$)?
Sama seperti intuisi pada filter konvolusi, **perkalian titik ([[Dot Product]]) adalah alat pengukur kemiripan (*similarity score*) antar-vektor**:
$$ q \cdot k = \|q\| \|k\| \cos(\theta) $$
Jika vektor Query dan vektor Key memiliki arah yang selaras, nilai dot product-nya sangat besar positif. Jika tidak nyambung, nilainya mendekati nol atau negatif. Matriks hasil kali $Q K^T$ berukuran $N \times M$ adalah **tabel skor kecocokan** antara setiap Query ke seluruh Key.

### 2. Mengapa Dibagi $\sqrt{d_k}$ (Scaling Factor)?
Tanpa pembagian ini, jika dimensi vektor $d_k$ sangat besar (misal $d_k = 64$ atau $512$):
- Nilai hasil kali $Q K^T$ merupakan penjumlahan dari $d_k$ suku acak.
- Varians dari hasil perkalian titik tersebut akan meledak sebanding dengan $d_k$.
- Angka yang sangat besar ini akan masuk ke fungsi Softmax.
- **Efek Bahaya Softmax Saturated:** Softmax pada nilai-nilai ekstrem akan menghasilkan distribusi yang sangat tajam (satu nilai mendekati $1$, sisanya hampir $0$). Pada kondisi ini, turunan/gradien Softmax mendekati nol, menyebabkan **gradien lenyap (*vanishing gradient*)** saat [[Backpropagation]].
- Membagi dengan $\sqrt{d_k}$ menormalkan kembali varians menjadi $1$, menjaga gradien tetap mengalir stabil saat training.

### 3. Mengapa Diterapkan Softmax?
Skor kecocokan setelah diskalakan masih berupa angka riil sembarang ($-\infty$ sampai $+\infty$). Softmax mengubah baris-baris tersebut menjadi:
1. Angka non-negatif ($[0, 1]$).
2. Jumlah totalnya persis $1$ ($100\%$).
Ini mengubah skor menjadi **koefisien pembobotan (*attention weights*)**.

### 4. Mengapa Dikalikan dengan $V$?
Perkalian $\text{Softmax}(\dots) \times V$ adalah operasi **rata-rata berbobot (*weighted average*)**:
Setiap vektor representasi output dibentuk dari percampuran informasi seluruh Value ($V$), di mana porsi masing-masing Value ditentukan oleh bobot atensi yang telah dihitung.

---

## Worked Example: Perhitungan Numerik Langkah demi Langkah

Misalkan kita memiliki 2 token (misal: "Bank" dan "Sungai") dengan dimensi fitur $d_k = 2$.

Diberikan:
$$ Q = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}, \quad K = \begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix}, \quad V = \begin{bmatrix} 10 & 0 \\ 0 & 20 \end{bmatrix} $$

### Langkah 1: Hitung Skor Kecocokan ($Q K^T$)
Transposisi $K$:
$$ K^T = \begin{bmatrix} 1 & 0 \\ 1 & 2 \end{bmatrix} $$

Perkalian $Q K^T$:
$$ S = Q K^T = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} (1\cdot 1 + 0\cdot 1) & (1\cdot 0 + 0\cdot 2) \\ (0\cdot 1 + 2\cdot 1) & (0\cdot 0 + 2\cdot 2) \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 2 & 4 \end{bmatrix} $$

### Langkah 2: Skalakan dengan $\sqrt{d_k} = \sqrt{2} \approx 1.414$
$$ S_{\text{scaled}} = \frac{S}{\sqrt{2}} = \begin{bmatrix} \frac{1}{1.414} & \frac{0}{1.414} \\ \frac{2}{1.414} & \frac{4}{1.414} \end{bmatrix} \approx \begin{bmatrix} 0.707 & 0 \\ 1.414 & 2.828 \end{bmatrix} $$

### Langkah 3: Terapkan Softmax per Baris
Untuk baris pertama $[0.707, 0]$:
$$ e^{0.707} \approx 2.028, \quad e^0 = 1.0 \implies \text{Total} = 3.028 $$
$$ A_{11} = \frac{2.028}{3.028} \approx 0.67, \quad A_{12} = \frac{1.0}{3.028} \approx 0.33 $$

Untuk baris kedua $[1.414, 2.828]$:
$$ e^{1.414} \approx 4.112, \quad e^{2.828} \approx 16.912 \implies \text{Total} = 21.024 $$
$$ A_{21} = \frac{4.112}{21.024} \approx 0.20, \quad A_{22} = \frac{16.912}{21.024} \approx 0.80 $$

Matriks Bobot Atensi ($A$):
$$ A = \begin{bmatrix} 0.67 & 0.33 \\ 0.20 & 0.80 \end{bmatrix} $$

### Langkah 4: Kalikan dengan Value ($V$)
$$ \text{Output} = A V = \begin{bmatrix} 0.67 & 0.33 \\ 0.20 & 0.80 \end{bmatrix} \begin{bmatrix} 10 & 0 \\ 0 & 20 \end{bmatrix} = \begin{bmatrix} (0.67 \times 10) & (0.33 \times 20) \\ (0.20 \times 10) & (0.80 \times 20) \end{bmatrix} = \begin{bmatrix} 6.7 & 6.6 \\ 2.0 & 16.0 \end{bmatrix} $$

Perhatikan bagaimana token ke-2 mengambil $80\%$ informasi dari $V_2$ dan $20\%$ dari $V_1$ secara dinamis.

---

## Dua Jenis Atensi Utama: Self-Attention vs. Cross-Attention

| Jenis Atensi | Sumber $Q$ | Sumber $K$ dan $V$ | Peran Fungsional |
| :--- | :--- | :--- | :--- |
| **Self-Attention** | Sequence A | Sequence A yang sama | Elemen saling berinteraksi di dalam satu kalimat/citra yang sama untuk memahami konteks internal. |
| **Cross-Attention** | Sequence A (Decoder) | Sequence B (Encoder) | Menghubungkan dua domain data berbeda (misal: mencocokkan teks terjemahan target dengan teks sumber, atau teks prompt ke piksel citra pada Stable Diffusion). |

---

> [!abstract]- Quick Reference
> - **Rumus Inti:**
>   $$ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V $$
> - **Query ($Q$):** Apa yang dicari oleh elemen saat ini.
> - **Key ($K$):** Label identitas yang ditawarkan elemen lain.
> - **Value ($V$):** Konten informasi aktual yang akan diambil.
> - **Peran $\sqrt{d_k}$:** Mencegah varians dot product meledak agar Softmax tidak jenuh (*prevent vanishing gradient*).
> - **Kompleksitas Komputasi:** $\mathcal{O}(N^2)$ terhadap panjang sekuens $N$, karena setiap elemen mengatensi seluruh elemen lainnya.

---

> [!question]- Practice
> **Soal 1:** Jika kita meningkatkan dimensi $d_k$ dari 64 menjadi 1024 tetapi menghapus pembagi $\sqrt{d_k}$ pada formula atensi, apa akibat fisis yang terjadi pada pelatihan model saat proses backpropagation?
> > [!check]- Answer
> > Nilai dot product $Q K^T$ akan memiliki varians yang sangat besar ($\sim 1024$). Ketika angka-angka besar ini dimasukkan ke fungsi Softmax, output Softmax akan menjadi vektor one-hot ekstrem ($1$ pada nilai terbesar, $0$ pada lainnya). Pada daerah jenuh ini, turunan matematis dari Softmax bernilai mendekati nol. Akibatnya, gradien yang dialirkan mundur saat [[Backpropagation]] akan lenyap (*vanishing gradient*), menghentikan proses pembelajaran bobot.
>
> **Soal 2:** Apa perbedaan mendasar antara bobot pada lapisan konvolusi dengan bobot atensi pada *self-attention*?
> > [!check]- Answer
> > Bobot pada lapisan konvolusi bersifat **statis dan lokal**: nilai kernel $3 \times 3$ dipelajari saat training lalu dibekukan saat inferensi, dan hanya beroperasi pada piksel tetangga terdekat. Sebaliknya, bobot pada *self-attention* bersifat **dinamis dan global**: nilai bobot dihitung ulang secara dinamis untuk setiap pasangan input saat inferensi berlangsung (*data-dependent weights*), dan dapat menghubungkan dua elemen di lokasi sejauh apapun secara langsung.

---

> [!info]- Going Deeper
> - **Multi-Head Attention (MHA):** Alih-alih hanya satu set $(Q, K, V)$, data diproyeksikan ke dalam $h$ sub-ruang berbeda secara paralel. Ini memungkinkan model memperhatikan aspek yang berbeda secara bersamaan (misal satu *head* fokus pada subjek kalimat, *head* lain fokus pada relasi tempat).
> - **Vision Transformers (ViT):** Citra diiris menjadi petak-petak kecil (*patches*, misal $16 \times 16$ piksel), diratakan menjadi token vektor, lalu diproses menggunakan Self-Attention penuh, mengalahkan dominasi CNN murni pada dataset skala besar.
