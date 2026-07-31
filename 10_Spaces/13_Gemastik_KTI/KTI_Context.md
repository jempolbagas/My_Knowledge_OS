---
type: context
space: Gemastik_KTI
last_updated: 2026-07-29
---

# KTI Context — Gemastik 2026

> File ini dibaca agen AI setiap kali sesi kerja berkaitan dengan KTI.
> Update file ini seiring project berkembang. Jaga agar tetap ringkas dan akurat.

## Topik & Judul

- **Judul sementara:** *(dalam diskusi — lihat [[Pertimbangan Judul dan Metodologi]])*
- **Bidang:** Systems Engineering, Edge Computing, Healthcare IT
- **Kata kunci utama:** Resilient Edge, Immutable OS, TinyML, Delta-Update, Edge Computing, 3T, Inferensi Klinis, Offline-first

## Tim

| Nama  | Role                  |
| ----- | --------------------- |
| Alfin | Ketua / penulis utama |
| Bagas | Riset                 |
| Lia   | Riset                 |

## Argumen Utama (Central Claim)

> Isi dengan thesis/klaim utama KTI setelah topik ditentukan.
> Contoh format: "Kami berargumen bahwa X dapat menyelesaikan Y karena Z."

Arah riset (Pivot disetujui): Kombinasi **Immutable OS** (mengatasi instabilitas listrik), **Native ML Runtime + Quantization** (mengatasi limitasi hardware), dan **Delta-Update** (mengatasi limitasi bandwidth) membentuk arsitektur *Resilient Edge* yang viable untuk fasilitas kesehatan 3T.

## Pertanyaan Riset

1. Bagaimana Immutable OS dapat menjaga reliabilitas sistem edge dari risiko korupsi data akibat pemutusan daya paksa di daerah 3T?
2. Seberapa efisien mekanisme Delta-Update dalam mereduksi konsumsi bandwidth saat sinkronisasi pembaruan model klinis?
3. Apakah performa inferensi native dengan model terkuantisasi INT8 di perangkat keras terbatas (RPi 4) memenuhi syarat latensi untuk penggunaan klinis?

## Status Saat Ini

- **Fase:** Rancang Bangun (Arsitektur Resilient Edge tanpa WASM)
- **Bottleneck:** Penentuan satu model klinis/kondisi medis spesifik untuk pengujian baseline
- **Deadline terdekat:** *(isi)*

## Konsep Kunci (Brain Atlas Links)

> Wikilinks ke Concept notes yang menjadi fondasi argumen KTI.
> Update seiring riset berjalan.

*(belum ada — isi setelah topik ditentukan)*

## Sumber Utama (Library Links)

> Wikilinks ke Library notes paper/artikel yang paling sentral.

*(belum ada)*

## Catatan untuk Agen

- Ketika membantu riset KTI, prioritaskan relevansi dengan **argumen utama** di atas.
- Kalau ada konsep baru yang muncul dari diskusi, sarankan apakah layak dipromote ke `20_Concepts/`.
- Draf KTI disimpan di `20_Draf/` — jangan buat konten draf di luar folder itu.
