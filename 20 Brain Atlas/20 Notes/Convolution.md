---
type: note
title: "Convolution"
subject: "Mathematics"
created: 2026-09-03
prerequisites:
  - "[[Calculus for Machine Learning]]"
tags:
  - mathematics
  - signal-processing
  - deep-learning
  - computer-vision
---

Konvolusi (*convolution*) adalah operasi matematika fundamental yang memadukan dua fungsi ($f$ dan $g$) untuk menghasilkan fungsi ketiga yang mendeskripsikan bagaimana bentuk satu fungsi dimodifikasi atau "dilewati" oleh fungsi lainnya seiring waktu atau ruang. Dalam pemrosesan sinyal fisik, konvolusi merepresentasikan respons sistem linier invarian waktu (*Linear Time-Invariant* / LTI) terhadap sinyal input sembarang melalui akumulasi respons impuls, sedangkan dalam visi komputer dan deep learning (CNN), konvolusi berfungsi sebagai ekstraktor fitur berbasis filter geser (*sliding window dot product*) yang memanfaatkan sifat *weight sharing* dan *translation equivariance*.

## Intuisi Dasar: Apa yang Sebenarnya Dilakukan Konvolusi?

Secara intuisi, konvolusi adalah **rata-rata berbobot yang berjalan** (*moving weighted average*) atau proses pencampuran (*blending*).

Bayangkan Anda meneteskan tinta ke dalam aliran air:
1. Tetesan tinta pertama masuk dan mulai menyebar (meluruh seiring waktu).
2. Tetesan kedua masuk semenit kemudian dan mulai menyebar dengan cara yang sama.
3. Di sembarang titik waktu $t$, kepekatan tinta di air adalah **superposisi akumulatif** dari seluruh sisa penyebaran tetesan-tetesan di masa lalu.

Satu fungsi merepresentasikan **rangkaian stimulus/input** ($f$), dan fungsi kedua merepresentasikan **respons karakteristik atau filter pembaur** ($g$). Konvolusi menghitung efek total akumulatif dari stimulus yang telah terfilter tersebut.

---

## Formulasi Matematis: Mengapa Ada Operasi "Flip & Slide"?

Secara formal, konvolusi kontinu antara dua fungsi $f(t)$ dan $g(t)$ didefinisikan sebagai:

$$ (f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau $$

Dan untuk sinyal diskret $x[n]$ dan respons impuls $h[n]$:

$$ (x * h)[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] $$

Terdapat 4 langkah mekanis dalam integral/penjumlahan ini:
1. **Substitusi Variabel:** Ganti variabel waktu menjadi variabel dummy integrasi ($\tau$ atau $k$).
2. **Flip (Pembalikan):** $g(\tau) \rightarrow g(-\tau)$.
3. **Shift (Pergeseran):** Geser sejauh $t$ menjadi $g(t - \tau)$.
4. **Multiply & Integrate/Sum:** Kalikan $f(\tau)$ dengan $g(t - \tau)$ lalu integralkan/jumlahkan seluruh domain.

```
f(τ)          : [====== Input Signal ======]
g(-τ)         : [ Filter Dibalik ]  (Flip)
g(t - τ)      :      ---> [ Filter Bergerak Sejauh t ] (Shift)
Overlap Area  :           [ Perkalian & Akumulasi ]  (Multiply & Sum)
```

### Mengapa Harus Di-Flip ($g(t - \tau)$)?
Banyak orang bingung mengapa argumennya $t - \tau$ (negatif $\tau$), bukan $t + \tau$.

Alasan fisisnya adalah **kausalitas dan jejak waktu lampau**:
- Misalkan waktu saat ini adalah $t = 10$.
- Input yang terjadi pada waktu $\tau = 7$ terjadi **$3$ satuan waktu yang lalu** ($t - \tau = 10 - 7 = 3$).
- Efek dari input tersebut pada saat ini dinilai berdasarkan respons sistem setelah berumur 3 satuan waktu, yaitu $h(3) = h(t - \tau)$.
- Input yang baru saja terjadi ($\tau = 10$) memiliki delay $0$, sehingga dievaluasi pada $h(0)$.
- Karena input masa lalu yang lebih lama mengalami delay lebih besar, filter $h$ harus dibaca mundur dari masa lalu ke masa kini, yang setara secara geometris dengan **membalik (*flip*) fungsi**.

---

## Dua Domain Utama: Signal Processing vs. Deep Learning

| Aspek | Signal Processing (LTI Systems) | Deep Learning / Computer Vision (CNN) |
| :--- | :--- | :--- |
| **Domain** | Waktu 1D / Ruang Frekuensi | Spasial 2D / Citra RGB 3D / Tensor |
| **Operasi Matematis** | Konvolusi Murni (dengan Flip) | *Cross-Correlation* (tanpa Flip) |
| **Filter / Kernel** | Didesain analitis (misal Gaussian, Sinc) | Dipelajari otomatis via [[Backpropagation]] |
| **Tujuan Utama** | Filtering sinyal, simulasi respons sistem fisik | Ekstraksi fitur visual (tepi, tekstur, pola hierarkis) |

### Mengapa Deep Learning Tidak Melakukan "Flip"?
Dalam implementasi framework deep learning (PyTorch, TensorFlow), layer `Conv2d` secara teknis menghitung **Cross-Correlation**:

$$ S(i, j) = (I * K)(i, j) = \sum_{m} \sum_{n} I(i + m, j + n) K(m, n) $$

Alasannya pragmatis:
Kernel $K$ berisi bobot acak yang dipelajari selama pelatihan. Jika kernel dibalik sebelum pelatihan, gradient descent hanya akan mempelajari orientasi bobot yang terbalik pula. Tidak ada perbedaan representasi atau performa model jika membalik matriks bobot sebelum dikalikan karena nilai bobotnya sendiri dioptimasi secara otomatis oleh loss function.

---

## Worked Example 1: Konvolusi Diskret 1D Langkah demi Langkah

Misalkan sinyal input $x = [1, 2, 3]$ dan respons impuls filter $h = [1, -1]$.
Panjang output konvolusi: $L_y = L_x + L_h - 1 = 3 + 2 - 1 = 4$ elemen.

Langkah komputasi:
- **Balik $h$:** $h[-k] = [-1, 1]$ (pivot di elemen index 0, yaitu 1).
- Geser $h[n - k]$ terhadap $x[k]$ untuk $n = 0, 1, 2, 3$:

1. Untuk $n = 0$:
   $$ y[0] = x[0] \cdot h[0] = 1 \cdot 1 = 1 $$
2. Untuk $n = 1$:
   $$ y[1] = x[0] \cdot h[1] + x[1] \cdot h[0] = (1 \cdot -1) + (2 \cdot 1) = -1 + 2 = 1 $$
3. Untuk $n = 2$:
   $$ y[2] = x[1] \cdot h[1] + x[2] \cdot h[0] = (2 \cdot -1) + (3 \cdot 1) = -2 + 3 = 1 $$
4. Untuk $n = 3$:
   $$ y[3] = x[2] \cdot h[1] = 3 \cdot -1 = -3 $$

Hasil: $y = [1, 1, 1, -3]$.
Operasi ini setara dengan menghitung diferensial diskret (mendeteksi perubahan lokal sinyal).

---

## Worked Example 2: Konvolusi 2D pada Citra (Edge Detection)

Pada pengolahan citra, konvolusi 2D meluncurkan jendela kernel kecil di atas matriks piksel:

Misalkan patch citra berukuran $3 \times 3$ dan kernel deteksi tepi vertikal (Sobel-like):

$$ \text{Image Patch } I = \begin{bmatrix} 10 & 10 & 0 \\ 10 & 10 & 0 \\ 10 & 10 & 0 \end{bmatrix}, \quad \text{Kernel } K = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix} $$

Perkalian elemen-demi-elemen (*element-wise product*) dan penjumlahannya:
$$
\begin{aligned}
\text{Output} &= (10 \cdot -1) + (10 \cdot 0) + (0 \cdot 1) \\
&\quad + (10 \cdot -2) + (10 \cdot 0) + (0 \cdot 2) \\
&\quad + (10 \cdot -1) + (10 \cdot 0) + (0 \cdot 1) \\
&= -10 + 0 + 0 - 20 + 0 + 0 - 10 + 0 + 0 = -40
\end{aligned}
$$

Nilai mutlak $|-40|$ yang besar menunjukkan adanya transisi tajam (garis tepi vertikal) antara kolom 2 dan kolom 3.

---

## Teorema Konvolusi (Convolution Theorem)

Salah satu sifat paling revolusioner dari konvolusi dalam matematika dan komputasi adalah kaitannya dengan **Transformasi Fourier** ($\mathcal{F}$):

$$ \mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\} $$

> [!important] Konvolusi di Domain Ruang/Waktu = Perkalian Biasa di Domain Frekuensi
> Jika Anda memiliki sinyal berukuran $N$ dan kernel berukuran $N$:
> - Komputasi konvolusi langsung membutuhkan kompleksitas waktu $\mathcal{O}(N^2)$.
> - Mengubah kedua sinyal ke domain frekuensi via Fast Fourier Transform (FFT), mengalikannya secara titik-demi-titik, lalu mengembalikan via IFFT hanya membutuhkan kompleksitas $\mathcal{O}(N \log N)$.

Hal inilah yang memungkinkan pemfilteran audio real-time dan komputasi citra resolusi tinggi berjalan efisien.

---

> [!abstract]- Quick Reference
> - **Definisi Kontinu:** $(f * g)(t) = \int_{-\infty}^\infty f(\tau) g(t - \tau) d\tau$
> - **Definisi Diskret:** $(x * h)[n] = \sum_{k=-\infty}^\infty x[k] h[n - k]$
> - **Ukuran Output 1D:** $\text{len}(y) = \text{len}(x) + \text{len}(h) - 1$
> - **Ukuran Output 2D (dengan Padding $P$ dan Stride $S$):**
>   $$ O = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1 $$
> - **Sifat Aljabar:**
>   - Komutatif: $f * g = g * f$
>   - Asosiatif: $f * (g * h) = (f * g) * h$
>   - Distributif: $f * (g + h) = (f * g) + (f * h)$
> - **Convolution Theorem:** $\mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\}$

---

> [!question]- Practice
> **Soal 1:** Jika sinyal $x = [2, 4]$ dikonvolusikan dengan $h = [3, 1]$, berapakah nilai sinyal output $y$?
> > [!check]- Answer
> > Panjang output: $2 + 2 - 1 = 3$ elemen.
> > - $y[0] = 2 \cdot 3 = 6$
> > - $y[1] = (2 \cdot 1) + (4 \cdot 3) = 2 + 12 = 14$
> > - $y[2] = 4 \cdot 1 = 4$
> >
> > Jadi $y = [6, 14, 4]$.
>
> **Soal 2:** Sebuah citra berukuran $32 \times 32$ diproses oleh layer konvolusi dengan kernel $5 \times 5$, padding $P = 0$, dan stride $S = 1$. Berapa dimensi spasial output feature map-nya?
> > [!check]- Answer
> > Menggunakan rumus:
> > $$ O = \frac{W - K + 2P}{S} + 1 = \frac{32 - 5 + 0}{1} + 1 = 27 + 1 = 28 $$
> > Output berdimensi $28 \times 28$.

---

> [!info]- Going Deeper
> - **Hubungan dengan Teori Peluang:** Penjumlahan dua variabel acak independen kontinu $Z = X + Y$ memiliki fungsi kepekatan peluang (*probability density function* / PDF) yang merupakan hasil konvolusi dari PDF masing-masing: $f_Z(z) = (f_X * f_Y)(z)$.
> - **Koneksi Arsitektur:** Lihat penerapannya pada arsitektur ekstraksi visual di [[Neural Networks]] dan [[Image Segmentation Architecture]].
