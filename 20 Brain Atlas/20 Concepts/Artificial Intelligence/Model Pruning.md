---
aliases: [Pruning]
tags: [artificial-intelligence, model-compression, machine-learning]
status: active
---

# Model Pruning

**Model Pruning** (Pemangkasan Model) adalah sebuah teknik kompresi model *Machine Learning* dan *Deep Learning* yang bertujuan untuk mengurangi jumlah [[Model Parameters|parameter]] (bobot/neuron) di dalam sebuah *neural network*. Teknik ini sangat relevan dalam *deployment* model komputasi biomedik pada perangkat dengan memori dan komputasi terbatas (seperti perangkat diagnostik *point-of-care* atau *wearables*).

Pruning bekerja dengan cara mengidentifikasi dan membuang koneksi atau neuron yang dianggap "kurang penting" atau memiliki kontribusi yang sangat kecil terhadap hasil prediksi akhir. 

## Cara Kerja Pruning
Dalam sebuah jaringan saraf tiruan, tidak semua bobot (*weights*) memiliki peran yang sama pentingnya. Banyak bobot yang nilainya mendekati nol. Pruning mendeteksi bobot-bobot ini dan menghapusnya dari arsitektur model (membuatnya menjadi nol mutlak), sehingga menghasilkan matriks yang renggang (*sparse matrix*).

Terdapat dua pendekatan utama dalam pruning:
1. **Unstructured Pruning (Pemangkasan Tidak Terstruktur):** Menghapus bobot individu secara acak berdasarkan ambang batas (*threshold*) tertentu (misalnya, menghapus semua bobot di bawah nilai 0.001). Meskipun mengurangi ukuran, pendekatan ini seringkali tidak mempercepat waktu inferensi pada CPU/GPU konvensional karena perangkat keras tersebut dirancang untuk operasi matriks padat (*dense matrix*).
2. **Structured Pruning (Pemangkasan Terstruktur):** Menghapus seluruh neuron, *channel*, atau filter sekaligus. Cara ini langsung mengubah dimensi matriks arsitektur jaringan, sehingga secara langsung mempercepat komputasi pada *hardware* standar.

## Dampak dan Kekurangan
* **Penurunan Akurasi:** Membuang terlalu banyak bobot dapat menyebabkan penurunan akurasi secara drastis, terutama jika fitur penting yang diandalkan model ikut terhapus.
* **Kebutuhan Retraining:** Setelah pruning dilakukan, model sering kali mengalami *accuracy drop*. Untuk mengembalikan performanya, model harus menjalani proses pelatihan ulang parsial (*fine-tuning*) menggunakan *dataset* asli. Proses ini dinamakan **Iterative Pruning**.

## Relevansi dengan Komputasi Biomedik
Dalam komputasi biomedik, model AI sering digunakan untuk analisis citra medis (MRI, X-Ray) atau pemrosesan sinyal biologis (EKG). Model-model ini biasanya sangat besar. Pruning memungkinkan model medis canggih dipampatkan agar dapat dijalankan pada perangkat keras di rumah sakit atau perangkat *wearable* tanpa memerlukan koneksi ke *cloud server*, menjaga privasi data pasien sekaligus menghemat biaya infrastruktur.
