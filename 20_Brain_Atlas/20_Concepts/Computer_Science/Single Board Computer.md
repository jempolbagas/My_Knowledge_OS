---
type: concept
title: Single Board Computer
subject: Computer_Science
date_created: 2026-07-28
tags:
  - hardware
  - sbc
  - computer-architecture
  - computer-science
source: "[[Single_Board_Computers_Architecture_and_Use_Cases]]"
source_hash: "a2190a000e91a11a1dd81e8f243a0df0"
---

## The idea (one clear statement)
**Single-Board Computer (SBC)** adalah arsitektur komputer lengkap di mana seluruh elemen utama (SoC CPU/GPU, RAM, pengontrol I/O, dan jaringan) terintegrasi pada satu papan sirkuit tunggal tanpa slot ekspansi modular internal.

## Why it matters / how it connects
* **Trade-off Arsitektural:** Mengorbankan modularitas dan *upgradeability* demi mencapai efisiensi ruang, konsumsi daya sangat rendah (2W–15W), dan biaya produksi ekonomis.
* **Perjembatan Sistem Tertanam:** Menyediakan pin GPIO langsung (I2C, SPI, UART) yang menghubungkan sistem operasi tingkat tinggi (Linux) secara langsung dengan sensor dan perangkat keras fisik (*real-world interaction*).
* **Diversifikasi Spesialisasi:** Berkembang menjadi berbagai kategori terspesialisasi: general-purpose (Raspberry Pi), komputasi tinggi & NPU (Orange Pi), deterministik real-time industri (BeagleBone PRU), dan akselerasi Edge AI (NVIDIA Jetson).

## Related concepts
- [[Single_Board_Computers_Architecture_and_Use_Cases]]
