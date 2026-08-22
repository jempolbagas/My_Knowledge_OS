---
aliases: [Quantization]
tags: [artificial-intelligence, model-compression, machine-learning]
status: active
---

# Model Quantization

**Model Quantization** (Kuantisasi Model) adalah teknik kompresi *Machine Learning* yang menurunkan tingkat presisi (resolusi bit) dari angka yang digunakan untuk menyimpan bobot (*weights*) dan aktivasi di dalam sebuah model. 

Teknik ini menjadi fondasi penting untuk membawa model-model berukuran masif agar dapat dijalankan di lingkungan *edge computing*, termasuk perangkat medis (*IoMT - Internet of Medical Things*).

## Mekanisme Quantization
Secara standar, model *deep learning* dilatih menggunakan presisi angka desimal tinggi, yaitu **32-bit floating-point (FP32)**. Quantization memampatkan representasi angka ini ke format yang lebih kecil dan lebih efisien, seperti:
* **16-bit floating-point (FP16 / BF16)**
* **8-bit integer (INT8)**
* **4-bit integer (INT4)**

Tidak seperti [[Model Pruning]] yang membuang jumlah parameter, Quantization mempertahankan **seluruh** parameter, namun mengecilkan ukuran memori (*footprint*) dari masing-masing parameter.

Penurunan presisi ini melibatkan proses pemetaan (*mapping*) dari rentang nilai FP32 yang kontinu ke dalam rentang nilai diskrit (seperti -128 hingga 127 pada INT8). Hal ini menggunakan parameter seperti [[Scale Factor and Zero-Point]].

## Dampak dan Kekurangan
* **Quantization Noise (Error Pembulatan):** Penurunan resolusi bit secara matematis akan menyebabkan selisih nilai antara model asli dan model terkuantisasi. Akumulasi error ini dapat menyebabkan akurasi prediksi menurun atau model menjadi berhalusinasi.
* **Sensitivitas Terhadap Outliers:** Dalam model besar (seperti LLM), sering terdapat nilai aktivasi yang jauh melebihi rata-rata (*outliers*). Quantization standar dapat memotong ekstremitas ini, merusak fungsi inti model.
* **Kebutuhan Data Kalibrasi:** Pada teknik [[Post-Training Quantization]] (PTQ), diperlukan sekumpulan data sampel kecil untuk mengkalibrasi pembulatan agar meminimalkan *error*. Jika data kalibrasi tidak representatif, performa model akan anjlok.

## Relevansi dengan Komputasi Biomedik
Data komputasi biomedik (seperti analisis urutan genom atau prediksi lipatan protein) membutuhkan komputasi yang intensif. Mengkuantisasi model-model ini menjadi INT8 memungkinkan proses inferensi dijalankan di perangkat portabel dengan latensi yang sangat rendah dan konsumsi daya baterai yang sangat hemat. Selain itu, operasi matematika integer-rendah dieksekusi jauh lebih cepat oleh prosesor modern dibandingkan operasi *floating-point*.
