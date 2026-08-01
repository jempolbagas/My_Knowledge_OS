---
type: generated_reading
title: Single Board Computers Architecture and Use Cases
topic: Single Board Computer (SBC)
requested_on: 2026-07-28
prompt: Apasih Single Board Computer atau SBC itu?
status: done
tags:
  - hardware
  - sbc
  - computer-science
  - embedded-systems
promoted_to:
  - "[[Single Board Computer]]"
---

## The reading

### Pengertian Single Board Computer (SBC)
Single-Board Computer (SBC) adalah sistem komputer utuh di mana seluruh komponen utama—termasuk mikroprosesor, memori RAM, pengontrol masukan/keluaran (I/O), dan antarmuka jaringan—terintegrasi pada satu papan sirkuit cetak (*Printed Circuit Board* / PCB) tunggal. Berbeda dari PC desktop konvensional yang bersifat modular dengan slot ekspansi terpisah (PCIe, slot RAM, socket CPU), SBC mengadopsi pendekatan terintegrasi dan non-modular untuk efisiensi ruang, konsumsi daya, dan biaya produksi.

### Arsitektur dan Komponen Utama
SBC umumnya mengintegrasikan beberapa elemen arsitektur berikut:
1. **System on Chip (SoC):** Sirkuit terpadu yang mengemas CPU (mayoritas berbasis arsitektur ARM, RISC-V, atau x86 hemat daya), GPU, DSP, serta pengontrol memori/bus ke dalam satu cip silikon tunggal.
2. **Memori Utama (RAM):** Memori LPDDR yang terpatri langsung pada PCB tanpa slot SODIMM/DIMM tambahan.
3. **Penyimpanan (*Storage*):**
   * Media kartu microSD untuk kepraktisan penukaran OS.
   * Modul eMMC (*embedded MultiMediaCard*) untuk reliabilitas dan kecepatan I/O lebih tinggi.
   * Antarmuka PCIe / M.2 NVMe pada SBC performa tinggi (seperti Orange Pi 5 atau Raspberry Pi 5).
4. **General Purpose Input/Output (GPIO) Pins:** Header pin fisik yang menyediakan akses langsung ke bus komunikasi tingkat rendah (I2C, SPI, UART, PWM) untuk mengontrol sensor, aktuator, dan komponen elektronik luar.
5. **Konektivitas dan Antarmuka Peripheral:** Wi-Fi, Bluetooth, Gigabit Ethernet, USB 2.0/3.0, output display (HDMI/micro-HDMI/MIPI DSI), serta konektor kamera (MIPI CSI).

### Perbandingan SBC dengan PC Konvensional
* **Dimensi & Bentuk:** SBC berukuran ringkas (lazimnya sebesar kartu kredit), sedangkan PC memerlukan casing modular yang jauh lebih besar.
* **Efisiensi Daya:** SBC beroperasi pada rentang daya 2W – 15W (bisa menggunakan daya USB/Power Bank), dibanding PC yang membutuhkan 50W – 500W+.
* **Aksesibilitas Perangkat Keras:** SBC dilengkapi pin GPIO langsung untuk integrasi sistem tertanam (*embedded system*), sedangkan PC berinteraksi dengan dunia luar melalui port standar seperti USB atau Serial.
* **Upgradeability:** SBC tidak memungkinkan penggantian/upgrade CPU atau RAM secara mandiri.

### Ekosistem dan Variasi Perangkat
1. **Raspberry Pi Series:** Pelopor SBC populer dengan ekosistem software dan komunitas terbesar. Ideal untuk pembelajaran, IoT, dan server rumahan.
2. **Orange Pi Series:** Alternatif berkinerja komputasi tinggi dengan rasio *price-to-performance* tinggi, sering dilengkapi akselerator NPU lokal.
3. **BeagleBone Series:** SBC kelas otomasi industri dengan modul PRU (*Programmable Real-Time Unit*) untuk eksekusi tugas penentuan waktu presisi (*real-time deterministic*).
4. **NVIDIA Jetson Series:** SBC khusus *Edge AI* dan robotika otonom dengan akselerasi GPU CUDA/TensorRT terintegrasi.

---

## Related Generated Readings
- [[Virtual_Private_Server_Architecture_and_Mechanics]]
- [[Post_Training_Quantization_End_to_End_Guide]]
- [[Model_Parameters_Explained]]

## Concepts to extract
- [x] [[Single Board Computer]]
