---
aliases: [Segmentasi Semantik, Pixel-level Classification]
tags: [artificial-intelligence, computer-vision, deep-learning, segmentation]
status: active
source: "[[Encoder Decoder Image Segmentation Deep Dive]]"
---

# Semantic Segmentation

**Semantic Segmentation** (Segmentasi Semantik) adalah tugas visi komputer (*computer vision*) tingkat tinggi yang memprediksi kategori kelas semantik untuk setiap piksel dalam sebuah citra. Berbeda dengan klasifikasi citra yang memberikan satu label untuk seluruh gambar, segmentasi menghasilkan peta partisi (*dense pixel mask*) berukuran $H \times W \times C$.

## Karakteristik Kunci
1. **Dense Prediction:** Setiap koordinat piksel $(x, y)$ diasosiasikan dengan satu label kelas target.
2. **Ketiadaan Pembedaan Instance:** Semua objek dari kelas yang sama (misalnya beberapa mobil di jalan) diberi label dan warna seragam yang identik, tanpa memisahkan identitas masing-masing individu objek (dibedakan pada *Instance Segmentation*).
3. **Arsitektur Standar:** Menggunakan paradigma [[Encoder-Decoder Architecture]], seperti [[U-Net Architecture]] dan DeepLab.

## Tantangan Utama
* **Kompromi Spasial vs Semantik:** Kebutuhan *receptive field* luas untuk memahami konteks objek berbenturan dengan kebutuhan resolusi spasial tinggi untuk batas piksel presisi.
* **Class Imbalance:** Area latar belakang (*background*) sering kali mendominasi luas citra dibanding objek target kecil, membutuhkan fungsi rugi khusus seperti [[Dice Loss]] atau Focal Loss.
