---
type: note
space: Gemastik_KTI
tags: [gemastik, evaluasi, kritik, arsitektur]
created: 2026-07-29
status: pending-action
source: agent-review
---

# Kritik & Evaluasi Cetak Biru KTI

Review kritis terhadap [[Cetak Biru KTI]]. Jadikan bahan diskusi tim sebelum mulai menulis draf.

---

## Yang Kuat

- Problem nyata dan well-defined — tiga pain point (bandwidth, hardware, listrik) terdokumentasi dengan baik
- Stack teknologi koheren — WebAssembly + TinyML + Delta-Update saling melengkapi
- Framing *Systems Engineering* (bukan akurasi klinis) adalah keputusan paling cerdas — menghindari jebakan "butuh dataset medis dan validasi klinis"
- Seksi Devil's Advocate menunjukkan kematangan argumentasi

---

## Yang Perlu Dihadapi

### 1. Scope Terlalu Ambisius

Empat layer sekaligus (Immutable OS, WasmEdge + WASI-NN, PTQ pipeline, Delta-Update) masing-masing adalah proyek semester sendiri. Kalau diimplementasikan setengah-setengah, tidak ada yang terlihat rigorous di depan juri.

> [!important] Rekomendasi
> Pilih **dua layer paling novel**, gali dalam-dalam. Kandidat terkuat: **WasmEdge + WASI-NN + quantized ONNX**. Delta-Update dan Immutable OS bisa jadi *design consideration*, bukan fokus benchmarking utama.

---

### 2. Use Case Klinis Masih Abstrak

"Inferensi Klinis" — inferensi untuk kondisi apa? TB screening dari chest X-ray? Malaria dari blood smear? Diabetes risk dari data tabular?

Ini bukan detail kecil. Pilihan model menentukan:
- Input requirement → hardware implication berbeda (kamera vs sensor)
- Dampak quantization terhadap akurasi (model vision jauh lebih sensitif ke PTQ dari model tabular)
- Relevansi klinis argumen di depan juri non-teknis

Tanpa use case spesifik, paper terasa seperti solusi yang mencari masalah.

> [!important] Action item
> Tentukan **satu kondisi medis, satu model pre-trained** sebelum apapun ditulis.

---

### 3. Immutable OS dan WebAssembly adalah Argumen Terpisah

Immutable OS (Alpine Linux read-only) menyelesaikan *power stability problem* — independen dari mengapa WebAssembly lebih baik dari Docker. Mencampurkan keduanya dalam satu layer arsitektur bisa dibaca sebagai kebingungan konseptual oleh juri yang teliti.

Keduanya valid, tapi harus dipresentasikan sebagai dua keputusan desain yang masing-masing punya justifikasi sendiri.

---

### 4. WASI-NN di ARM adalah Risiko Teknis Nyata

WasmEdge dengan backend WASI-NN (TFLite/OpenVINO) di ARM masih experimental. Dukungan untuk RPi 4 tidak selalu stabil tergantung versi.

> [!warning] Risiko
> Kalau stack ini tidak bisa compile atau crash di tengah pengerjaan, seluruh Layer Eksekusi runtuh. **Lakukan proof of concept WasmEdge + WASI-NN di RPi 4 sebelum commit ke arsitektur ini.**

---

### 5. Baseline Docker Perlu Dipertanyakan

Skenario B menggunakan Docker di RPi 4 sebagai baseline "Konvensional". Valid secara teknis, tapi Docker bukan yang dipakai di Puskesmas sekarang — jadi perbandingannya terasa artificial bagi praktisi.

Alternatif baseline yang lebih relevan secara praktis:
- **Skenario A:** Native Python execution (kondisi eksisting paling realistis)
- **Skenario B:** ONNX Runtime standard tanpa containerization
- **Skenario C:** WasmEdge + WASI-NN + quantized model (usulan)

---

## Tiga Hal yang Harus Diselesaikan Sebelum Mulai Menulis Draf

| # | Task | Status |
|---|------|--------|
| 1 | Tentukan use case klinis spesifik — satu model, satu kondisi medis | ☐ |
| 2 | Proof of concept: WasmEdge + WASI-NN berjalan di RPi 4 | ☐ |
| 3 | Putuskan scope final: berapa layer yang jadi fokus benchmarking? | ☐ |

> [!warning] Jangan finalisasi judul sebelum ketiga hal ini selesai.
> Judul mengikuti metodologi, bukan sebaliknya.
