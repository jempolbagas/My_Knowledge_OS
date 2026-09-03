---
aliases: [Sørensen–Dice Loss, Soft Dice Loss]
tags: [artificial-intelligence, deep-learning, loss-functions, optimization, segmentation]
status: active
source: "[[Encoder Decoder Image Segmentation Deep Dive]]"
---

# Dice Loss

**Dice Loss** adalah fungsi objektif (*loss function*) berbasis wilayah (*region-based*) yang diturunkan dari koefisien kesamaan Sørensen–Dice untuk mengukur tingkat tumpang tindih (*overlap*) antara area mask segmentasi prediksi $\hat{Y}$ dan target sebenarnya $Y$.

## Formulasi Matematis

Koefisien Sørensen–Dice discrete didefinisikan sebagai:
$$\text{DSC} = \frac{2 |X \cap Y|}{|X| + |Y|}$$

Untuk pelatihan jaringan saraf secara *backpropagation*, digunakan formulasi kontinu diferensiabel (**Soft-Dice Loss**):
$$\mathcal{L}_{\text{Dice}} = 1 - \frac{2 \sum_{i=1}^N y_i \hat{p}_i + \epsilon}{\sum_{i=1}^N y_i + \sum_{i=1}^N \hat{p}_i + \epsilon}$$

di mana:
* $y_i \in \{0, 1\}$ adalah label ground truth piksel ke-$i$.
* $\hat{p}_i \in [0, 1]$ adalah probabilitas prediksi piksel ke-$i$.
* $\epsilon$ adalah konstanta penghalus (*smoothing factor*, misal $10^{-5}$) untuk menghindari pembagian dengan nol.

## Keunggulan
* **Imunitas terhadap Class Imbalance:** Tidak sensitif terhadap dominasi luas piksel latar belakang (*background*), karena loss dihitung dari proporsi perpotongan area objek, bukan akumulasi kesalahan piksel individual seperti pada Cross-Entropy Loss.
