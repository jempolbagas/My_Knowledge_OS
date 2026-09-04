---
type: note
title: "Dot Product"
subject: "Mathematics"
created: 2026-09-03
prerequisites: []
tags:
  - mathematics
  - linear-algebra
  - machine-learning
  - computer-vision
  - deep-learning
---

Perkalian titik (*dot product* atau perkalian skalar) adalah operasi aljabar linier fundamental yang mengalikan dua vektor berdimensi sama untuk menghasilkan satu nilai skalar tunggal. Secara komputasi, dot product merupakan operasi *multiply-and-accumulate* (MAC) berbiaya rendah yang menjadi fondasi perangkat keras akselerator AI, sedangkan secara konseptual, ia adalah mekanisme universal untuk **mengukur keselarasan (*alignment*)**, **mendeteksi kemiripan pola (*pattern matching*)**, dan **memproyeksikan fitur**. Dari neuron tunggal pada jaringan saraf tiruan ([[Neural Networks]]), mekanisme atensi pada Transformer ([[Attention Mechanism]]), hingga filter ekstraksi fitur pada konvolusi citra ([[Convolution]], [[Convolutional Layer]]), dot product adalah mesin pembanding utama yang menggerakkan kecerdasan buatan dan visi komputer modern.

---

## Tiga Mental Model Dot Product

Untuk memahami dot product secara intuitif tanpa sekadar menghafal rumus perkalian elemen demi elemen, kita perlu melihatnya melalui tiga sudut pandang mental:

```
1. Geometris (Alignment & Bayangan)   : Seberapa searah dua panah ini?
2. Aljabar (Weighted Accumulation)   : Skor total dari pemasangan atribut.
3. Filter / Radar (Pattern Detector) : Seberapa cocok sinyal input dengan cetakan (template)?
```

### 1. Mental Model Geometris: Detektor Keselarasan & Proyeksi Bayangan

Secara geometris dalam ruang Euclidean berdimensi $n$, dot product didefinisikan sebagai hasil kali panjang kedua vektor dengan kosinus sudut apit di antara keduanya:

$$ \mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\| \|\mathbf{b}\| \cos\theta $$

> **Legenda Rumus:**
> - $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$: dua vektor input.
> - $\|\mathbf{a}\| = \sqrt{\sum a_i^2}$: magnitudo (panjang Euclidean / norm $L_2$) dari vektor $\mathbf{a}$.
> - $\|\mathbf{b}\| = \sqrt{\sum b_i^2}$: magnitudo dari vektor $\mathbf{b}$.
> - $\theta$: sudut apit terkecil antara $\mathbf{a}$ dan $\mathbf{b}$ ($0^\circ \le \theta \le 180^\circ$).

```
                 a
                /|
               / |
              /  |  (Cahaya tegak lurus b)
             /   |
            / θ  |
           +-----+------------> b
             proj_b(a)
```

Bayangkan lampu sorot diarahkan tegak lurus ke garis vektor $\mathbf{b}$. Vektor $\mathbf{a}$ akan menjatuhkan bayangan di sepanjang garis $\mathbf{b}$. 
- Panjang bayangan tersebut adalah proyeksi skalar: $\text{proj}_{\mathbf{b}}(\mathbf{a}) = \|\mathbf{a}\| \cos\theta$.
- Dot product $\mathbf{a} \cdot \mathbf{b}$ tidak lain adalah **panjang bayangan $\mathbf{a}$ dikalikan dengan panjang $\mathbf{b}$**.

Nilai kosinus $\cos\theta$ menentukan perilaku tanda dari dot product:
- **$\theta = 0^\circ$ ($\cos\theta = 1$):** Kedua vektor menunjuk persis ke arah yang sama. Nilai positif maksimal ($\|\mathbf{a}\| \|\mathbf{b}\|$). Keselarasan sempurna.
- **$0^\circ < \theta < 90^\circ$ ($\cos\theta > 0$):** Kedua vektor memiliki komponen arah yang serupa. Nilai bernilai positif.
- **$\theta = 90^\circ$ ($\cos\theta = 0$):** Kedua vektor saling tegak lurus (*ortogonal*). Bayangannya adalah sebuah titik berukuran nol. Keduanya tidak memiliki korelasi arah sama sekali.
- **$90^\circ < \theta < 180^\circ$ ($\cos\theta < 0$):** Kedua vektor berlawanan arah parsial. Nilai bernilai negatif.
- **$\theta = 180^\circ$ ($\cos\theta = -1$):** Kedua vektor bertolak belakang secara diametris. Nilai negatif minimal ($-\|\mathbf{a}\| \|\mathbf{b}\|$).

### 2. Mental Model Aljabar: Akumulasi Berbobot (*Multiply and Accumulate*)

Secara komponen koordinat, dot product menjumlahkan hasil kali elemen-elemen yang berpasangan:

$$ \mathbf{a} \cdot \mathbf{b} = \mathbf{a}^T \mathbf{b} = \sum_{i=1}^{n} a_i b_i = a_1 b_1 + a_2 b_2 + \dots + a_n b_n $$

> **Legenda Rumus:**
> - $a_i$: elemen skalar ke-$i$ dari vektor $\mathbf{a}$.
> - $b_i$: elemen skalar ke-$i$ dari vektor $\mathbf{b}$.
> - $n$: jumlah dimensi atau jumlah fitur.

Jika vektor $\mathbf{x}$ adalah **data** dan vektor $\mathbf{w}$ adalah **bobot prioritas (kepentingan)**, dot product merepresentasikan sistem penilaian skor terbobot (*weighted scoring system*).

#### Contoh Konkret: Rekomendasi Film
Misalkan kita mendeskripsikan preferensi pengguna dan karakteristik film dengan 3 fitur: `[Action, Komedi, Drama]` dengan skala skor $-1$ hingga $+1$:
- Profil User $\mathbf{u} = [0.9, -0.2, 0.8]$ (Suka action & drama, kurang suka komedi).
- Film A (Laga Dramatis) $\mathbf{f}_A = [0.8, -0.1, 0.9]$.
- Film B (Komedi Murni) $\mathbf{f}_B = [-0.1, 0.9, -0.2]$.

Kita hitung skor kecocokan dengan dot product:
$$ \mathbf{u} \cdot \mathbf{f}_A = (0.9)(0.8) + (-0.2)(-0.1) + (0.8)(0.9) = 0.72 + 0.02 + 0.72 = 1.46 $$
$$ \mathbf{u} \cdot \mathbf{f}_B = (0.9)(-0.1) + (-0.2)(0.9) + (0.8)(-0.2) = -0.09 - 0.18 - 0.16 = -0.43 $$

Hasil positif tinggi pada Film A ($+1.46$) menunjukkan kecocokan kuat, sedangkan nilai negatif pada Film B ($-0.43$) menunjukkan ketidakcocokan.

### 3. Mental Model Radar: *Template Matching* & Resonansi Fitur

Ketika sebuah vektor bobot $\mathbf{w}$ dilatih, vektor tersebut menjadi sebuah **cetakan pola (*template*)**. 
- Ketika input $\mathbf{x}$ memiliki bentuk profil yang identik (fitur tinggi bertemu bobot tinggi, fitur negatif bertemu bobot negatif), terjadi "resonansi konstruktif", menghasilkan nilai dot product yang sangat besar.
- Jika profil input tidak cocok dengan template, perkalian positif dan negatif akan saling meniadakan, menghasilkan dot product mendekati nol.
- **Inti gagasan:** Dot product adalah sebuah "filter penerima" yang memberi sinyal keras hanya jika sinyal yang lewat cocok dengan bentuk filter tersebut.

---

## Peran Sentral dalam Machine Learning & Deep Learning

### 1. Fondasi Neuron Buatan (*Artificial Neuron / Perceptron*)

Dalam arsitektur feedforward [[Neural Networks]], setiap neuron menerima masukan fitur $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$ dan memiliki bobot sinaptik $\mathbf{w} = [w_1, w_2, \dots, w_n]^T$ beserta skalar bias $b$. Komputasi tahap pertama neuron adalah menghitung pre-aktivasi $z$:

$$ z = \mathbf{w}^T \mathbf{x} + b = \left(\sum_{i=1}^n w_i x_i\right) + b $$

> **Legenda Rumus:**
> - $\mathbf{w}^T \mathbf{x}$: dot product antara vektor bobot $\mathbf{w}$ dan vektor input $\mathbf{x}$.
> - $b \in \mathbb{R}$: skalar bias yang menggeser bidang keputusan (*hyperplane*) menjauhi/mendekati titik origin.
> - $z \in \mathbb{R}$: nilai aktivasi linear sebelum dilewatkan ke fungsi aktivasi non-linear $\sigma(z)$ (misal ReLU atau Sigmoid).

Secara geometris, persamaan $\mathbf{w}^T \mathbf{x} + b = 0$ mendefinisikan sebuah bidang pembatas (*decision hyperplane*) dalam ruang fitur berdimensi $n$, di mana vektor $\mathbf{w}$ adalah vektor normal tegak lurus bidang tersebut. Dot product menentukan di sisi mana data $\mathbf{x}$ berada relatif terhadap bidang keputusan.

### 2. Pengukuran Kesamaan Semantik (*Cosine Similarity*)

Dalam pemrosesan bahasa alami (NLP) dan pencarian vektor (Vector Search / RAG), teks dikonversi menjadi representasi vektor numerik (*embedding*). Namun, dot product mentah memiliki kelemahan: **sensitif terhadap panjang vektor**. Vektor dengan kata yang diulang berkali-kali akan memiliki magnitudo besar dan memicu dot product tinggi, meskipun secara makna tidak lebih relevan.

Untuk mengisolasi murni arah konseptualnya, dot product dinormalisasi dengan panjang kedua vektor:

$$ \text{Cosine Similarity}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|} = \frac{\sum a_i b_i}{\sqrt{\sum a_i^2} \sqrt{\sum b_i^2}} = \cos\theta $$

> **Legenda Rumus:**
> - Nilai berkisar antara $[-1, 1]$.
> - Nilai $+1$: makna identik (vektor menunjuk ke arah yang sama persis).
> - Nilai $0$: tidak ada kesamaan makna semantik (ortogonal).
> - Nilai $-1$: makna bertolak belakang.

Jika seluruh vektor embedding telah dinormalisasi terlebih dahulu ke panjang satuan ($\|\mathbf{x}\| = 1$), maka **Cosine Similarity identik dengan Dot Product biasa**. Ini memungkinkan pencarian tetangga terdekat (KNN) berjalan luar biasa cepat di GPU melalui operasi perkalian matriks standar:

```python
import numpy as np

# Dua representasi embedding vektor ter-normalisasi (L2-norm = 1)
v_king = np.array([0.41, 0.82, 0.39])
v_queen = np.array([0.40, 0.84, 0.36])
v_apple = np.array([0.91, 0.12, -0.39])

# Normalisasi unit length
v_king /= np.linalg.norm(v_king)
v_queen /= np.linalg.norm(v_queen)
v_apple /= np.linalg.norm(v_apple)

sim_royalty = np.dot(v_king, v_queen)  # ~ 0.998 (Sangat mirip secara semantik)
sim_fruit = np.dot(v_king, v_apple)    # ~ 0.320 (Kurang relevan)
```

### 3. Mekanisme Atensi pada Transformer (*Scaled Dot-Product Attention*)

Dalam arsitektur Transformer ([[Attention Mechanism]]), seluruh pertukaran informasi antar-token digerakkan oleh dot product:

$$ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V $$

> **Legenda Rumus:**
> - $Q \in \mathbb{R}^{N \times d_k}$: matriks Query (pertanyaan/kebutuhan token).
> - $K \in \mathbb{R}^{M \times d_k}$: matriks Key (label/identitas kunci yang ditawarkan token lain).
> - $V \in \mathbb{R}^{M \times d_v}$: matriks Value (informasi konten yang akan diambil).
> - $d_k$: dimensi dari vektor query dan key.
> - $Q K^T$: matriks kesesuaian hasil perkalian titik berpasangan antara setiap vektor query terhadap semua vektor key.

```
Token "kucing" (Query)  ---> [ Dot Product dengan seluruh Key ] 
                              ├── Key "tidur" : Skalar tinggi  (relevan)
                              ├── Key "di"    : Skalar rendah  (fungsi kata)
                              └── Key "kursi" : Skalar tinggi  (lokasi objek)
```

**Mengapa harus dibagi $\sqrt{d_k}$?**
Jika dimensi vektor $d_k$ sangat besar (misal $d_k = 64$ atau $128$), jumlahan perkalian $q_i k_i$ memiliki variansi yang tumbuh sebanding dengan $d_k$. Dot product yang sangat besar akan mendorong fungsi $\text{softmax}$ ke wilayah jenuh di mana gradiennya hampir nol (*vanishing gradient*). Pembagian dengan $\sqrt{d_k}$ menstabilkan variansi kembali ke $1$.

---

## Peran dalam Pemrosesan Citra & Visi Komputer

### 1. Filter Konvolusi 2D sebagai *Sliding Window Dot Product*

Pada pengolahan citra digital dan Convolutional Neural Networks ([[Convolutional Layer]]), filter atau kernel bergerak di atas matriks piksel citra. Di setiap posisi jendela lokal, operasi yang dilakukan secara matematis adalah **perkalian titik Frobenius (*Frobenius inner product*)**:

$$ S(x, y) = (I * K)(x, y) = \sum_{u=-k}^{k} \sum_{v=-k}^{k} I(x + u, y + v) K(u, v) = \text{vec}(I_{\text{patch}}) \cdot \text{vec}(K) $$

> **Legenda Rumus:**
> - $I$: matriks intensitas citra (grayscale atau kanal warna).
> - $K$: matriks kernel/filter berukuran $(2k+1) \times (2k+1)$, misal $3 \times 3$.
> - $S(x, y)$: nilai piksel keluaran pada peta fitur (*feature map*).
> - $\text{vec}(\cdot)$: perataan (*flattening*) matriks 2D menjadi vektor 1D berukuran $9$.

#### Contoh Nyata: Deteksi Tepi Vertikal (Sobel Filter)
Kernel Sobel vertikal dirancang khusus untuk mencari perubahan tajam dari gelap ke terang pada arah horizontal:

$$ K_{\text{sobel}} = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix} $$

Mari uji kernel ini pada dua patch citra $3 \times 3$ yang berbeda:

**Kasus A: Patch memiliki tepi vertikal (kiri gelap $= 10$, kanan terang $= 200$)**
$$ I_A = \begin{bmatrix} 10 & 100 & 200 \\ 10 & 100 & 200 \\ 10 & 100 & 200 \end{bmatrix} $$
Dot product elemen-per-elemen:
$$ S_A = [(-1)(10) + (0)(100) + (1)(200)] \times 1 + [(-2)(10) + (0)(100) + (2)(200)] + [(-1)(10) + (0)(100) + (1)(200)] $$
$$ S_A = 190 + 380 + 190 = +760 \quad (\text{Respons Sangat Kuat!}) $$

**Kasus B: Patch memiliki warna seragam/homogen (semua piksel bernilai $100$)**
$$ I_B = \begin{bmatrix} 100 & 100 & 100 \\ 100 & 100 & 100 \\ 100 & 100 & 100 \end{bmatrix} $$
$$ S_B = [(-1)(100) + 0 + (1)(100)] + [(-2)(100) + 0 + (2)(100)] + [(-1)(100) + 0 + (1)(100)] = 0 $$

Patch homogen menghasilkan output $0$ karena bobot negatif dan positif pada kernel saling membatalkan. Ini membuktikan secara langsung bahwa **filter konvolusi adalah detektor pola yang dioperasikan lewat dot product**.

### 2. Pencocokan Template (*Template Matching*)

Dalam visi komputer klasik, untuk mendeteksi keberadaan objek tertentu (misalnya tanda rambu lalu lintas atau mata pada wajah), kita menggeser template citra $T$ berukuran $w \times h$ ke seluruh citra $I$ dan menghitung *Normalized Cross-Correlation* (NCC):

$$ \gamma(x, y) = \frac{\sum_{u, v} (I(x+u, y+v) - \bar{I}_{x,y})(T(u, v) - \bar{T})}{\sqrt{\sum_{u, v} (I(x+u, y+v) - \bar{I}_{x,y})^2 \sum_{u, v} (T(u, v) - \bar{T})^2}} $$

> **Legenda Rumus:**
> - $\bar{T}$: rata-rata intensitas template.
> - $\bar{I}_{x,y}$: rata-rata intensitas jendela citra lokal di sekitar $(x, y)$.
> - $\gamma(x, y) \in [-1, 1]$: skor korelasi. Puncak tertinggi $\gamma(x, y) \approx 1$ menunjukkan lokasi pasti objek berada.

Formulasi NCC di atas pada dasarnya adalah dot product antara citra lokal dan template yang telah dinormalisasi rata-ratanya dan dibagi norm-nya (*centered & normalized dot product*).

### 3. Model Pencahayaan Difus (*Lambert's Cosine Law*)

Dalam grafika komputer, rekonstruksi 3D (*photometric stereo*), dan estimasi pencahayaan citra, kecerahan permukaan suatu benda yang memantulkan cahaya difus (tak berkilau) dihitung dengan dot product antara vektor normal permukaan dengan vektor arah cahaya:

$$ I_D = I_L \cdot k_d \cdot \max(0, \mathbf{N} \cdot \mathbf{L}) $$

> **Legenda Rumus:**
> - $I_D$: intensitas pantulan cahaya yang ditangkap kamera/mata.
> - $I_L$: intensitas sumber cahaya datang.
> - $k_d \in [0, 1]$: koefisien refleksi difus material (*albedo*).
> - $\mathbf{N}$: vektor normal satuan tegak lurus bidang permukaan ($\|\mathbf{N}\| = 1$).
> - $\mathbf{L}$: vektor satuan penunjuk arah datang sumber cahaya ($\|\mathbf{L}\| = 1$).

```
           Cahaya (L)
              \  θ  Normal (N)
               \ | /
                \|/
    ============================= (Permukaan Objek)
```

- Ketika cahaya datang tegak lurus pada permukaan ($\theta = 0^\circ \implies \mathbf{N} \cdot \mathbf{L} = 1$), permukaan menerima energi foton per satuan luas paling padat sehingga tampak paling terang.
- Ketika cahaya datang menyerempet permukaan ($\theta = 90^\circ \implies \mathbf{N} \cdot \mathbf{L} = 0$), permukaan gelap.
- Nilai $\max(0, \cdot)$ mencegah dot product negatif ketika cahaya berada di belakang permukaan (*self-shadowing*).

---

> [!abstract]- Quick Reference
> 
> ### Definisi Matematis
> - **Bentuk Geometris:** $\mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\| \|\mathbf{b}\| \cos\theta$
> - **Bentuk Aljabar:** $\mathbf{a} \cdot \mathbf{b} = \mathbf{a}^T \mathbf{b} = \sum_{i=1}^n a_i b_i$
> - **Norm Euclidean:** $\|\mathbf{a}\| = \sqrt{\mathbf{a} \cdot \mathbf{a}}$
> - **Kosinus Sudut / Cosine Sim:** $\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$
> - **Proyeksi Skalar $\mathbf{a}$ ke $\mathbf{b}$:** $\text{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|}$
> - **Proyeksi Vektor $\mathbf{a}$ ke $\mathbf{b}$:** $\mathbf{a}_{\parallel} = \left(\frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|^2}\right) \mathbf{b}$
> 
> ### Sifat-Sifat Aljabar
> 1. **Komutatif:** $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$
> 2. **Distributif terhadap Penjumlahan:** $\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}$
> 3. **Homogenitas Skalar:** $(c\mathbf{a}) \cdot \mathbf{b} = c(\mathbf{a} \cdot \mathbf{b}) = \mathbf{a} \cdot (c\mathbf{b})$
> 4. **Definit Positif:** $\mathbf{a} \cdot \mathbf{a} \ge 0$, dan $\mathbf{a} \cdot \mathbf{a} = 0 \iff \mathbf{a} = \mathbf{0}$
> 5. **Ortogonalitas:** $\mathbf{a} \cdot \mathbf{b} = 0 \iff \mathbf{a} \perp \mathbf{b}$ (untuk vektor non-nol)
> 
> ### Kompleksitas Komputasi
> - Vektor panjang $n$: $\mathcal{O}(n)$ operasi perkalian dan penjumlahan (MAC).
> - Perkalian Matriks $A (m \times k)$ dan $B (k \times p)$: $m \times p$ operasi dot product $\implies \mathcal{O}(m \cdot k \cdot p)$.

---

> [!question]- Practice
> 
> ### Soal 1: Evaluasi Kemiripan Semantik Embedding
> Diberikan dua vektor embedding token dalam ruang 3-dimensi:
> $\mathbf{q} = [3, 0, 4]^T$ dan $\mathbf{k} = [0, 5, 12]^T$.
> 1. Hitung nilai dot product $\mathbf{q} \cdot \mathbf{k}$.
> 2. Hitung magnitudo $\|\mathbf{q}\|$ dan $\|\mathbf{k}\|$.
> 3. Tentukan Cosine Similarity antara kedua vektor tersebut.
> 
> > [!check]- Answer Soal 1
> > 1. **Dot Product:**
> >    $$\mathbf{q} \cdot \mathbf{k} = (3)(0) + (0)(5) + (4)(12) = 0 + 0 + 48 = 48$$
> > 2. **Magnitudo:**
> >    $$\|\mathbf{q}\| = \sqrt{3^2 + 0^2 + 4^2} = \sqrt{9 + 0 + 16} = \sqrt{25} = 5$$
> >    $$\|\mathbf{k}\| = \sqrt{0^2 + 5^2 + 12^2} = \sqrt{0 + 25 + 144} = \sqrt{169} = 13$$
> > 3. **Cosine Similarity:**
> >    $$\cos\theta = \frac{\mathbf{q} \cdot \mathbf{k}}{\|\mathbf{q}\| \|\mathbf{k}\|} = \frac{48}{5 \times 13} = \frac{48}{65} \approx 0.7385$$
> >    Kedua token memiliki keselarasan positif yang cukup kuat ($\sim 73.8\%$).
> 
> ---
> 
> ### Soal 2: Ekstraksi Fitur Tepi Horizontal pada Citra
> Sebuah filter detektor tepi horizontal sederhana memiliki bobot kernel:
> $$ K = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix} $$
> Hitung respon konvolusi (dot product) filter $K$ terhadap patch citra $I$:
> $$ I = \begin{bmatrix} 20 & 20 & 20 \\ 50 & 50 & 50 \\ 80 & 80 & 80 \end{bmatrix} $$
> 
> > [!check]- Answer Soal 2
> > Lakukan perkalian elemen per elemen dan jumlahkan:
> > - Baris 1: $(-1)(20) + (-1)(20) + (-1)(20) = -60$
> > - Baris 2: $(0)(50) + (0)(50) + (0)(50) = 0$
> > - Baris 3: $(1)(80) + (1)(80) + (1)(80) = +240$
> > 
> > $$ S = -60 + 0 + 240 = +180 $$
> > Nilai positif tinggi ($+180$) mengonfirmasi adanya transisi intensitas dari gelap ke terang sepanjang gradien vertikal (garis tepi horizontal terdeteksi).

---

> [!info]- Going Deeper
> - **Kernel Trick & Ruang Hilbert:** Pada Support Vector Machines (SVM) dan metode kernel, jika data tidak dapat dipisahkan secara linier pada ruang aslinya, data dipetakan ke ruang dimensi tak terhingga $\phi(\mathbf{x})$. Fungsi kernel $K(\mathbf{x}, \mathbf{z}) = \langle \phi(\mathbf{x}), \phi(\mathbf{z}) \rangle$ menghitung dot product di ruang dimensi tinggi tersebut tanpa pernah perlu menghitung koordinat $\phi(\mathbf{x})$ secara eksplisit.
> - **Generalisasi ke Ruang Fungsi (*Continuous Inner Product*):** Dalam analisis fungsional dan deret Fourier, perkalian titik antara dua fungsi kontinu $f(x)$ dan $g(x)$ pada interval $[a, b]$ dihitung via integral: $\langle f, g \rangle = \int_a^b f(x) g(x) dx$. Dua fungsi dikatakan ortogonal jika integral perkaliannya bernilai nol.
> - **Optimasi Hardware (Systolic Arrays & Tensor Cores):** Pada arsitektur perangkat keras modern seperti NVIDIA Tensor Core atau Google TPU, perkalian matriks besar dipecah menjadi ribuan operasi Multiply-Accumulate (MAC) serentak dalam matriks grid pipa data (*systolic array*), di mana setiap siklus clock mengeksekusi operasi dot product kecil $\mathbf{a} \cdot \mathbf{b} + c$.
