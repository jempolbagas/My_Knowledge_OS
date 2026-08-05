# **CETAK BIRU KARYA TULIS ILMIAH**

**Judul Tentatif:** Rancang Bangun Arsitektur *Resilient Edge Computing* Berbasis Immutable OS dan TinyML untuk Inferensi Medis Mandiri di Fasilitas Kesehatan 3T

## **1\. Latar Belakang & Pernyataan Masalah**

Fasilitas Kesehatan Tingkat Pertama (FKTP) di daerah Tertinggal, Terdepan, dan Terluar (3T) Indonesia menghadapi konstrain infrastruktur yang parah:

> 1. **Fakir Bandwidth:** Koneksi internet terputus-putus, latensi tinggi, dan seringkali hanya mengandalkan jaringan 2G/3G atau VSAT berkuota rendah.  
> 2. **Perangkat Keras Usang (Resource-Constrained):** PC yang tersedia umumnya berspesifikasi rendah, berfungsi ganda untuk administrasi harian (SIMPUS), dan rentan *crash* jika dibebani komputasi berat.  
> 3. **Instabilitas Daya:** Pemadaman listrik sepihak dan fluktuasi voltase sering terjadi, meningkatkan risiko korupsi sistem operasi pada komputer.

Mendeploy model *Machine Learning* (ML) berbasis *Cloud* (tersentralisasi) tidak relevan karena isu latensi dan ketiadaan internet. Sebaliknya, mendeploy ML menggunakan arsitektur *Edge Container* tradisional (seperti Docker) di PC lokal Puskesmas akan memicu *bottleneck* memori dan melumpuhkan operasional.

## **2\. Tinjauan Kritis Arsitektur Konvensional (Devil's Advocate)**

Dalam menyusun KTI, bagian ini membuktikan bahwa penulis memahami kelemahan teknologi yang ada (menjawab pertanyaan: "Mengapa tidak pakai cara biasa saja?"):

> * **Kelemahan Docker/Container di 3T:** Menjalankan *daemon* Docker dan isolasi *namespace* Linux membawa *overhead* memori yang sangat tinggi. Di PC berspesifikasi rendah, ini memicu *Out-of-Memory* (OOM).  
> * **Kelemahan Model Standar (FP32):** Model ML konvensional beroperasi pada presisi *floating-point* 32-bit. Mengeksekusinya secara lokal tanpa akselerator grafis (GPU) akan menyebabkan latensi ekstrem dan pemanasan berlebih (*thermal throttling*) pada CPU.  
> * **Kelemahan Sinkronisasi Penuh:** Mengunduh model *update* berukuran ratusan Megabyte via jaringan 3T akan berujung pada *timeout* dan fragmentasi versi model.

## **3\. Desain Arsitektur Sistem Baru (Novelty)**

Sistem ini memisahkan model (*payload*) dari infrastruktur (*vehicle*). Berikut adalah 4 pilar arsitektur yang diusulkan:

### **A. Layer Hardware: *Immutable Edge Appliance***

> * **Desain:** Menggunakan *Single Board Computer* (SBC) hemat daya (misal: Raspberry Pi 4 atau serupa) sebagai server dedikasi terpisah dari PC administrasi.  
> * **Sistem Operasi:** Menggunakan *Immutable OS* (seperti Alpine Linux tipe *read-only*).  
> * **Keunggulan:** Tahan terhadap kerusakan OS akibat mati listrik mendadak. *Troubleshooting* cukup dilakukan dengan *Hard Reset* (cabut-pasang kabel daya).

### **B. Layer Eksekusi: Native ML Runtime (Tanpa Kontainer)**

> * **Desain:** Menghilangkan *overhead* kontainerisasi (Docker) maupun *sandbox* (WASM) untuk mengeksekusi inferensi langsung secara *native* (Host OS).  
> * **Runtime:** Menggunakan *engine* inferensi standar yang telah teroptimasi untuk ARM64 (seperti TensorFlow Lite atau ONNX Runtime).  
> * **Keunggulan:** Menghilangkan kompleksitas arsitektur berlapis, memberikan latensi prediksi tercepat (murni dari CPU tanpa terpotong *virtualization layer*), dan memaksimalkan RAM yang tersisa.

### **C. Layer Model: *TinyML Pipeline* (Integrasi Model Publik)**

Karena penelitian ini menggunakan model *pre-trained* (tidak membuat dataset sendiri), inovasi difokuskan pada manipulasi format model:

> 1. **Format Transisi:** Model publik diubah menjadi format standar **ONNX**.  
> 2. **Post-Training Quantization (PTQ):** Mengompresi presisi bobot model dari *float32* ke *int8*. Transformasi matematis dijalankan di server pusat menggunakan formula:  
>    ![][image1]  
>    *(Dimana ![][image2] adalah bobot asli, ![][image3] adalah skala, dan ![][image4] adalah titik-nol).*  
> * **Keunggulan:** Ukuran model menyusut hingga 75%, memungkinkan inferensi latensi rendah murni pada prosesor *low-end*.

### **D. Layer Jaringan: *Delta-Update Protocol***

> * **Desain:** Pembaruan bobot model dari pusat Kemenkes tidak lagi mengirimkan file .onnx secara utuh.  
> * **Mekanisme:** Menggunakan algoritma *binary diffing* (seperti bsdiff) untuk menghitung dan mengirimkan selisih (*delta*) matriks bobot antara versi lama dan baru.  
> * **Keunggulan:** Memangkas ukuran pembaruan jaringan dari satuan Megabyte menjadi Kilobyte, sangat resisten terhadap koneksi internet lambat.

## **4\. Metodologi Evaluasi (Systems Benchmarking)**

KTI ini berfokus pada **Rekayasa Sistem (Systems Engineering)**, bukan akurasi diagnosis medis. Oleh karena itu, pengujian dilakukan dengan membandingkan tiga skenario arsitektur menjalankan satu model *pre-trained* yang sama:

> * **Skenario A (Pengujian Bandwidth):** Sinkronisasi *Full Model Update* (transfer utuh) vs *Delta-Update* (hanya mentransfer perbedaan *byte*).  
> * **Skenario B (Pengujian Hardware):** Eksekusi Model Asli (FP32) vs Model Terkuantisasi (INT8) secara *Native* di Raspberry Pi 4.  
> * **Skenario C (Pengujian Reliabilitas Listrik):** Simulasi *Hard Power-Off* paksa pada OS Standar (Raspbian) vs *Immutable OS* (Alpine Linux).

**Metrik Kuantitatif yang akan diukur dan disajikan sebagai hasil penelitian:**

> 1. *Memory Footprint* (Megabyte) \- Membuktikan efisiensi RAM.  
> 2. *Inference Latency* (Milidetik) \- Membuktikan kecepatan prediksi di Edge.  
> 3. *CPU Utilization* (%) \- Membuktikan ringannya komputasi.  
> 4. *Update Payload Size* (Kilobyte) \- Membuktikan penghematan bandwidth via Delta-Update.

## **5\. Kesimpulan KTI**

Arsitektur yang diusulkan menggeser paradigma dari "memaksakan komputasi berat ke Edge" menjadi "merestrukturisasi komputasi agar sesuai dengan Edge". Pendekatan integratif antara *Immutable OS*, *Native ML Runtime*, TinyML, dan *Delta-Update* ini menawarkan kerangka kerja infrastruktur yang pragmatis, hemat biaya, dan *bulletproof* untuk digitalisasi layanan medis di wilayah paling terisolasi di Indonesia.

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAZCAYAAAAFbs/PAAAAn0lEQVR4XmNgGAUjD+QA8VYgPgXEk4DYDog3APEhIE5FUgcGuUBcA2XzAvE/IL4ExPxAfA+IL0Pl4GA9EDNC2QpA/B+IC4CYHYjnAXEAVA4rWAXEj9EFkQEXA8SUaCBmAeJ3QLwISd4fiGOQ+AxeDBAnFEIl/gBxJ1ROBoj3ADEPlA8GII9tA+JNQDwFiK2B+DwQb2SA2CSPUDoKBgsAALpBGiLrlN6FAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAaCAYAAACHD21cAAAA3ElEQVR4Xu3QsY4BURSA4SPZKLawFdW2WyLRUIhks6VO7Q0UXoAt2QfYhGjFC0isRKJHQSQSGj21SlaW/5or7pylVYg/+Yo5Z+4wI/Lodn2gixEG6CCKNiLOfb7KWCDmzJLYYOrMfKWxR1wvqIUvPTxVxx+e9YK+kdHDU2ZpfrGHd/E/4AUB59rXG9biHTZ+MUTWvelaIeTRwFy8B+zk8nsfu/aZq+IdLuqFKYy+HtpS4h3M6YXJ/LWJHtoqWCKoF6YmtijJ+Us+oYAVEnb2rx+84hNjzKyanT+60w5g7iek98V0vgAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAZCAYAAAA4/K6pAAAA2klEQVR4Xu3Sv6tBYRzH8ecWlzIoShlEucvdbGzKYLX6C0xi8h/4d+56R2W4wx3IwGZApKQMCiU/3sc5Ts/zJYyG86nXcD7fp059n0cpL++ZOk6OJQboO7ZO33RP30kbXeTwofVlHPADn9YbiWGMqOhL2OMXn2JmpIKa6IrYoYWgmN3E+nNA+85jgz+EtP6lZLFGB2Exe5oMVsrevNzHw3xhjhES5uiyn4bojCSVfQMzpMUsgglSoncTxxALfGu9HwX08K/1N7Gu6KjspU0115dnPaCqe9qLF5EzRqwq072QBEMAAAAASUVORK5CYII=>

---

## 🔗 Keterkaitan & Navigasi Riset
- [[Riset Index]]
- [[Cetak Biru KTI]]
- [[WebAssembly_vs_Docker]]
- [[WebAssembly_Sandboxing]]
- [[Post-Training Quantization]]
- [[Single Board Computer]]
