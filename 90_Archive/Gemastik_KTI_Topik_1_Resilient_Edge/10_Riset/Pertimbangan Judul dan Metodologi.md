---
type: note
space: Gemastik_KTI
tags: [gemastik, judul, brainstorming]
created: 2026-07-29
status: pending-decision
---

# Pertimbangan Judul & Metodologi KTI

Catatan dari sesi brainstorming awal. Jadikan bahan diskusi tim sebelum finalisasi judul.

---

## Kandidat Judul

### Judul Utama
> "Rancang Bangun Arsitektur Edge Computing Ultra-Ringan Berbasis WebAssembly dan TinyML untuk Inferensi Medis Mandiri di Fasilitas Kesehatan 3T"

**Masalah:**
- Delta-Update hilang dari judul — padahal itu salah satu dari tiga pilar utama
- "Inferensi Medis Mandiri" terlalu vague, inferensi untuk kondisi apa?

---

### Alternatif A (Benchmarking)
> "Analisis Komparatif Kinerja WebAssembly dan Kontainer Konvensional dalam Eksekusi TinyML pada Perangkat Edge Terbatas di Wilayah 3T"

**Masalah:**
- Docker/kontainer konvensional tidak bisa jalan di hardware ultra-constrained yang jadi target
- Juri yang paham sistem akan langsung pertanyakan validitas baseline perbandingannya
- **Kelemahan fatal — hindari framing ini**

---

### Alternatif B (Bandwidth)
> "Implementasi Protokol Delta-Update dan Runtime WebAssembly untuk Efisiensi Sinkronisasi Model Machine Learning di Fasilitas Kesehatan Fakir Bandwidth"

**Masalah:**
- Scope terlalu sempit — WebAssembly dan TinyML jadi terasa implementation detail, bukan kontribusi utama
- "Fakir Bandwidth" terlalu informal untuk judul KTI formal

---

### Alternatif C (Resiliensi)
> "Rancang Bangun Immutable Edge Appliance Berbasis TinyML untuk Menjamin Resiliensi Sistem Diagnosis Medis Offline di Daerah Tertinggal"

**Kekuatan:** "Immutable Edge Appliance" concrete dan memorable, "Offline" menekankan resiliensi

**Masalah:**
- WebAssembly hilang dari judul
- "Diagnosis Medis" implisit mengklaim akurasi klinis — burden pembuktian sangat berat untuk KTI mahasiswa

---

## Usulan Judul Baru (Gabungan)

> **"Rancang Bangun Edge Appliance Ultra-Ringan Berbasis WebAssembly dan TinyML dengan Mekanisme Delta-Update untuk Inferensi Klinis Offline di Fasilitas Kesehatan 3T"**

**Kenapa lebih baik:**
- Tiga pilar (WebAssembly + TinyML + Delta-Update) semua muncul di judul
- "Edge Appliance" lebih concrete dari "Arsitektur"
- "Inferensi Klinis" lebih spesifik dari "Medis Mandiri" tapi tidak mengklaim diagnosis
- "Offline" menekankan resiliensi tanpa perlu kata "Immutable"

---

## Pertanyaan Kritis yang Belum Dijawab

> [!important] Pertanyaan ini harus dijawab tim sebelum finalisasi judul

**Rancang Bangun sungguhan, atau Kajian/Simulasi?**

| | Rancang Bangun | Kajian / Simulasi |
|---|---|---|
| **Artinya** | Build prototipe yang benar-benar jalan di hardware nyata | Analisis, benchmark terkontrol, atau desain arsitektur teoritis |
| **Bukti yang dibutuhkan** | Hardware fisik + hasil pengukuran empiris | Data benchmark, studi literatur, analisis komparatif |
| **Juri bisa tanya** | "Tunjukkan prototipenya" | "Apa limitasi simulasi vs kondisi nyata?" |
| **Judul yang cocok** | "Rancang Bangun..." | "Analisis...", "Kajian...", "Perancangan..." |

**Inkonsistensi framing** (judul "Rancang Bangun" tapi isi kajian) adalah celah yang sering diserang juri saat presentasi.

**Pertanyaan konkret untuk tim:**
- Apakah kita punya akses ke hardware edge? (Raspberry Pi, SBC, ESP32, atau sejenisnya)
- Sejauh mana scope prototype — hanya proof-of-concept, atau end-to-end system?
- Kalau tidak ada hardware, metodologi apa yang akan kita pakai sebagai gantinya?

---

## Kesimpulan Sementara

Judul usulan gabungan di atas bisa jadi starting point. Tapi **finalisasi judul harus tunggu jawaban pertanyaan metodologi** — judul mengikuti metodologi, bukan sebaliknya.
