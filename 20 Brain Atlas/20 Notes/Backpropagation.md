---
type: note
title: "Backpropagation"
subject: "Machine Learning"
created: 2026-09-03
prerequisites:
  - "[[Neural Networks]]"
tags:
  - deep-learning
  - neural-networks
  - optimization
  - calculus
---

Backpropagation (backward propagation of errors) adalah algoritma komputasi efisien berbasis aturan rantai kalkulus (*chain rule*) untuk menghitung gradien fungsi rugi (*loss function*) terhadap setiap bobot dan bias dalam jaringan saraf tiruan (*neural network*). Algoritma ini menjadi fondasi pelatihan model *deep learning* modern karena mampu menurunkan kompleksitas komputasi turunan parsial jutaan hingga miliaran parameter dari yang semula eksponensial/polinomial tinggi ($\mathcal{O}(P^2)$) menjadi linear terhadap jumlah parameter ($\mathcal{O}(P)$) dengan memanfaatkan *dynamic programming* (caching aktivasi forward).

## Intuisi: Masalah Pembagian Tanggung Jawab (*Credit Assignment*)

Bayangkan sebuah lini dapur restoran (*assembly line*) dengan 3 koki berurutan:
1. **Koki 1 (Layer 1):** Meracik bumbu dasar daging berdasarkan bahan mentah $x$.
2. **Koki 2 (Layer 2):** Mengolah saus dengan melipatgandakan bumbu dari Koki 1 sebesar $w_2$.
3. **Koki 3 (Layer Output):** Melakukan plating dan sentuhan akhir garam sebesar $w_3$, menghasilkan burger ($\hat{y}$).

Ketika burger dicicipi oleh *quality control*, ternyata burger **keasinan 4 gram** dari target ($y$). Ini adalah **Loss ($\mathcal{L}$)**.

Masalah utama: **Siapa yang bertanggung jawab atas keasinan tersebut, dan seberapa besar porsi kesalahannya masing-masing?**

Backpropagation bekerja mundur dari meja saji ke dapur belakang:
- Manajer memeriksa **Koki 3** terlebih dahulu: "Berapa garam yang kamu masukkan di akhir?" $\rightarrow$ dihitung gradien koki 3.
- Lalu mundur ke **Koki 2**: "Seberapa pekat sausmu saat kamu oper ke Koki 3?" Karena Koki 3 hanya meneruskan hasil Koki 2, porsi kesalahan Koki 2 dihitung **melalui** koneksinya ke Koki 3.
- Terakhir ke **Koki 1**: Kesalahan Koki 1 dihitung dengan merambatkan dampak kesalahannya yang sudah digandakan oleh Koki 2 dan 3.

Setelah setiap koki menerima slip "porsi kesalahan" masing-masing (gradien), barulah mereka menyesuaikan takaran bumbu untuk hidangan berikutnya (update bobot via Optimizer).

## Mengapa Bukan Naive Differentiation?

Jaringan saraf pada dasarnya adalah komposisi fungsi bersarang:
$$ \hat{y} = f_L(W^{[L]} f_{L-1}(W^{[L-1]} \dots f_1(W^{[1]} x + b^{[1]}) \dots + b^{[L-1]}) + b^{[L]}) $$

Untuk memperbarui parameter via *Gradient Descent* ($W \leftarrow W - \eta \frac{\partial \mathcal{L}}{\partial W}$), kita wajib mengetahui sensitivitas loss $\mathcal{L}$ terhadap setiap parameter individu.

Jika kita menggunakan pendekatan beda hingga numerik (*finite difference*):
$$ \frac{\partial \mathcal{L}}{\partial w_i} \approx \frac{\mathcal{L}(w_i + \epsilon) - \mathcal{L}(w_i)}{\epsilon} $$
Kita harus melakukan satu kali evaluasi forward pass penuh per parameter. Untuk model dengan 100 juta parameter, satu langkah iterasi gradien akan membutuhkan 100 juta kali forward pass. 

Backpropagation menyelesaikan seluruh gradien parameter hanya dalam **satu kali forward pass** (untuk menyimpan nilai perantara / aktivasi) dan **satu kali backward pass** (merambatkan error dari layer output ke layer input secara rekursif).

## Siklus Komputasi: Forward vs. Backward Pass

Pelatihan satu batch data berjalan dalam dua fase simetris:

```
[ Input x ] ──> (Layer 1) ──> (Layer 2) ──> [ Output ŷ ] ──> Loss L
                   │             │                               │
             Cache: a^[1], z^[1] Cache: a^[2], z^[2]             │
                   ▲             ▲                               ▼
                   │             │                            dL/dŷ
[ dL/dW^[1] ] <── 𝛿^[1] <────── 𝛿^[2] <─────────────────────── 𝛿^[L]
               (Backward Pass via Chain Rule)
```

### 1. Forward Pass (Forward Propagation)
Data input dialirkan maju untuk menghitung nilai pre-aktivasi $z$ dan aktivasi $a$ pada setiap layer $l \in [1, L]$:
$$ z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]} $$
$$ a^{[l]} = \sigma^{[l]}(z^{[l]}) $$
*Catatan:* $a^{[0]} = x$. Semua nilai $z^{[l]}$ dan $a^{[l]}$ disimpan (*cached*) di memori karena mutlak dibutuhkan saat menghitung turunan parsial di fase backward.

### 2. Backward Pass (Mekanisme Rantai Error $\delta$)
Kita mendefinisikan sinyal error pada layer $l$ sebagai:
$$ \delta^{[l]} = \frac{\partial \mathcal{L}}{\partial z^{[l]}} $$

Dengan aturan rantai kalkulus:
1. **Error pada Layer Output ($l = L$):**
   $$ \delta^{[L]} = \nabla_{a^{[L]}} \mathcal{L} \odot \sigma'^{[L]}(z^{[L]}) $$
   *Simbol $\odot$ adalah Hadamard product (perkalian elemen-demi-elemen).*

2. **Propagasi Error ke Layer Tersembunyi ($l < L$):**
   $$ \delta^{[l]} = \left( (W^{[l+1]})^T \delta^{[l+1]} \right) \odot \sigma'^{[l]}(z^{[l]}) $$
   Matriks transposisi $(W^{[l+1]})^T$ bertindak sebagai distributor error mundur yang membagi kontribusi kesalahan sebanding dengan bobot koneksinya.

3. **Gradien Terhadap Parameter:**
   $$ \frac{\partial \mathcal{L}}{\partial W^{[l]}} = \delta^{[l]} (a^{[l-1]})^T $$
   $$ \frac{\partial \mathcal{L}}{\partial b^{[l]}} = \delta^{[l]} $$

## Worked Example: Jaringan Minimalis (1-1-1)

Untuk melihat mekanismenya secara konkret tanpa kerumitan matriks, amati jaringan 3-neuron skalar:
- Input: $x = 2$
- Target asli: $y = 1$
- Bobot awal: $w_1 = 0.5$, $w_2 = -0.5$
- Bias: $b_1 = 0$, $b_2 = 0$
- Aktivasi: Hidden menggunakan Linear identity $\sigma(z) = z$ ($\sigma'(z) = 1$), output linear.
- Loss: Mean Squared Error $\mathcal{L} = \frac{1}{2}(\hat{y} - y)^2$

### Langkah 1: Forward Pass
$$ z_1 = w_1 x = (0.5)(2) = 1.0 \implies a_1 = 1.0 $$
$$ z_2 = w_2 a_1 = (-0.5)(1.0) = -0.5 \implies \hat{y} = -0.5 $$
$$ \mathcal{L} = \frac{1}{2}(-0.5 - 1)^2 = \frac{1}{2}(-1.5)^2 = 1.125 $$

### Langkah 2: Backward Pass (Menghitung Gradien)
Kita ingin mencari $\frac{\partial \mathcal{L}}{\partial w_2}$ dan $\frac{\partial \mathcal{L}}{\partial w_1}$.

**Untuk $w_2$ (Output layer):**
$$ \frac{\partial \mathcal{L}}{\partial \hat{y}} = (\hat{y} - y) = -0.5 - 1 = -1.5 $$
$$ \delta_2 = \frac{\partial \mathcal{L}}{\partial z_2} = \frac{\partial \mathcal{L}}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2} = -1.5 \cdot 1 = -1.5 $$
$$ \frac{\partial \mathcal{L}}{\partial w_2} = \delta_2 \cdot a_1 = -1.5 \cdot 1.0 = -1.5 $$

**Untuk $w_1$ (Hidden layer):**
$$ \delta_1 = \frac{\partial \mathcal{L}}{\partial z_1} = \delta_2 \cdot w_2 \cdot \sigma'(z_1) = (-1.5) \cdot (-0.5) \cdot 1 = 0.75 $$
$$ \frac{\partial \mathcal{L}}{\partial w_1} = \delta_1 \cdot x = 0.75 \cdot 2 = 1.5 $$

### Langkah 3: Update Bobot (Learning Rate $\eta = 0.1$)
$$ w_2 \leftarrow w_2 - \eta \frac{\partial \mathcal{L}}{\partial w_2} = -0.5 - (0.1)(-1.5) = -0.5 + 0.15 = -0.35 $$
$$ w_1 \leftarrow w_1 - \eta \frac{\partial \mathcal{L}}{\partial w_1} = 0.5 - (0.1)(1.5) = 0.5 - 0.15 = 0.35 $$

Jika kita tes forward pass kembali dengan bobot baru:
$$ z_1 = 0.35 \times 2 = 0.7 $$
$$ \hat{y} = -0.35 \times 0.7 = -0.245 $$
$$ \mathcal{L}_{\text{baru}} = \frac{1}{2}(-0.245 - 1)^2 \approx 0.775 \quad (\text{turun dari } 1.125) $$

## Hambatan Nyata: Vanishing & Exploding Gradients

Karena backpropagation mengalikan matriks bobot dan turunan aktivasi lapis demi lapis:
$$ \delta^{[1]} \propto \prod_{k=2}^{L} W^{[k]} \sigma'^{[k-1]}(z^{[k-1]}) $$

- **Vanishing Gradients:** Bila menggunakan fungsi aktivasi seperti Sigmoid ($\sigma'(z) \le 0.25$) atau Tanh, perkalian angka pecahan berulang pada arsitektur dalam ($L \gg 10$) membuat $\delta$ di layer awal mendekati 0. Akibatnya, layer awal berhenti belajar. Solusi: aktivasi ReLU ($f'(z) \in \{0, 1\}$), *Residual Connections* (ResNet), dan normalisasi (BatchNorm/LayerNorm).
- **Exploding Gradients:** Bila eigen value $W > 1$, perkalian berulang meledakkan gradien menjadi `NaN` atau nilai ekstrem. Solusi: *Gradient Clipping* dan inisialisasi bobot terkalibrasi (He / Xavier initialization).

> [!abstract]- Quick Reference
> | Simbol / Operasi | Rumus Vektor / Matriks | Dimensi ($n^{[l]} \times n^{[l-1]}$) |
> | :--- | :--- | :--- |
> | **Pre-aktivasi Forward** | $z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}$ | $(n^{[l]} \times 1)$ |
> | **Output Error** | $\delta^{[L]} = \nabla_{a^{[L]}} \mathcal{L} \odot \sigma'^{[L]}(z^{[L]})$ | $(n^{[L]} \times 1)$ |
> | **Hidden Error** | $\delta^{[l]} = \left( (W^{[l+1]})^T \delta^{[l+1]} \right) \odot \sigma'^{[l]}(z^{[l]})$ | $(n^{[l]} \times 1)$ |
> | **Gradien Bobot** | $\frac{\partial \mathcal{L}}{\partial W^{[l]}} = \delta^{[l]} (a^{[l-1]})^T$ | $(n^{[l]} \times n^{[l-1]})$ |
> | **Gradien Bias** | $\frac{\partial \mathcal{L}}{\partial b^{[l]}} = \delta^{[l]}$ | $(n^{[l]} \times 1)$ |
> | **Update Aturan (SGD)** | $\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}$ | Sesuai dimensi parameter |

> [!question]- Practice
> **Soal 1:** Sebuah neuron memiliki aktivasi Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$. Jika saat forward pass nilai aktivasi neuron tersebut adalah $a = 0.8$, berapakah nilai turunan $\sigma'(z)$ pada titik tersebut tanpa menghitung nilai $z$ terlebih dahulu?
> 
> > [!check]- Answer
> > Karakteristik turunan Sigmoid adalah $\sigma'(z) = \sigma(z)(1 - \sigma(z)) = a(1 - a)$.
> > Maka $\sigma'(z) = 0.8 \times (1 - 0.8) = 0.8 \times 0.2 = \mathbf{0.16}$.
> 
> **Soal 2:** Mengapa memori GPU sering kali habis (*Out of Memory*) saat fase backward pass, padahal forward pass berjalan lancar?
> 
> > [!check]- Answer
> > Saat forward pass, framework komputasi (seperti PyTorch/TensorFlow) harus menahan (*cache*) seluruh tensor aktivasi intermediate ($a^{[l]}$ dan $z^{[l]}$) di VRAM agar bisa dipakai menghitung $\frac{\partial \mathcal{L}}{\partial W^{[l]}} = \delta^{[l]} (a^{[l-1]})^T$ saat backward pass. Jika batch size atau kedalaman layer terlalu besar, akumulasi tensor yang di-cache di VRAM inilah yang memicu OOM.

> [!info]- Going Deeper
> - **Automatic Differentiation (Reverse-Mode vs. Forward-Mode):** Backpropagation secara formal merupakan implementasi spesifik dari *Reverse-Mode Automatic Differentiation*. Untuk fungsi dengan banyak input dan satu skalar output (seperti loss $\mathcal{L}$), Reverse-Mode jauh lebih efisien daripada Forward-Mode.
> - **Hessian & Orde Dua:** Metode orde kedua (seperti Newton-Raphson) mempertimbangkan kelengkungan permukaan error via matriks Hessian $\nabla^2 \mathcal{L}$, namun komputasi $\mathcal{O}(P^2)$ membuatnya tidak praktis untuk deep learning skala besar.
