---
aliases: [U-Net, UNet]
tags: [artificial-intelligence, computer-vision, deep-learning, neural-networks, u-net]
status: active
source: "[[Encoder Decoder Image Segmentation Deep Dive]]"
---

# U-Net Architecture

**U-Net Architecture** adalah jaringan saraf konvolusional simetris yang dirancang oleh Olaf Ronneberger et al. (2015) untuk segmentasi citra presisi tinggi, khususnya pada domain biomedis dengan ketersediaan sampel latih terbatas.

## Struktur Anatomi (Bentuk Huruf "U")
1. **Contracting Path (Encoder):** Blok konvolusi $3 \times 3$ ganda yang diikuti *Max Pooling* $2 \times 2$ (stride 2) untuk mereduksi dimensi spasial dan melipatgandakan kanal fitur.
2. **Bottleneck:** Lapisan representasi laten dengan resolusi terendah dan kedalaman channel tertinggi.
3. **Expanding Path (Decoder):** Blok *Up-convolution* ($2 \times 2$ transposed conv) yang merekonstruksi dimensi spasial kembali ke ukuran asal.
4. **Skip Connections (Concatenation):** Menyalin seluruh *feature map* dari level encoder langsung ke level decoder yang bersesuaian, lalu menggabungkannya sepanjang dimensi kanal (*channel concatenation*).

## Signifikansi & Keunggulan
* **Presisi Batas Objek:** Penggabungan fitur resolusi tinggi dari encoder mempertahankan detail kontur tepi sel atau batas organ yang biasanya hilang saat downsampling.
* **Efisiensi Data:** Mampu mencapai generalisasi tinggi dengan augmentasi data elastis pada dataset medis berukuran kecil.
