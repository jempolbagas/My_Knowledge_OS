---
name: self-study-creator
description: Workflow for converting raw inbox items, external sources, or notes into comprehensive, approachable self-study readings with active recall questions in 10_Knowledge_OS.
---

# Self-Study Material Creator Skill

Skill ini digunakan saat pengguna meminta untuk membuat bahan bacaan/materi belajar mandiri (*Generated Reading*) berdasarkan catatan di inbox (`00_Inbox/`), artikel/paper eksternal, atau catatan vault lainnya.

## Aturan & Konvensi Penyusunan:

### 1. Kedalaman & Gaya Bahasa (Depth & Tone)
* **Panjang & Komprehensif**: Mengikuti standar `99_Configs/Depth_Standard.md`. Jangan membuat rangkuman pendek/abstrak 3–5 poin. Bacaan harus mengulas konsep secara utuh, *first-principles*, serta menyajikan mekanisme inti dan tabel komparasi jika terdapat variasi/pilihan yang dibandingkan.
* **Approachable Tone**: Menggunakan gaya bahasa yang komunikatif, intuitif, dan mudah dicerna (menggunakan analogi visual, contoh dunia nyata, dan penjelasan *step-by-step* tanpa mengorbankan kedalaman teknis).

### 2. Struktur Berkas Generated Reading
* **Lokasi Penyimpanan**: `20_Brain_Atlas/10_Library/Generated_Readings/<Subject>/Readings_<Judul_Materi>.md` (atau di `10_Spaces/11_College/` jika terkait tugas/matakuliah spesifik).
* **Paragraf Pembuka**: Satu paragraf ringkasan mendalam yang berdiri sendiri (digunakan untuk indeks SQLite `vault_summary.json`).
* **Bagian Utama Bacaan (`## The Reading`)**: Subbab bertingkat (`###`) yang mengurai konsep dari intuisi inti hingga detail mekanisme teknis.
* **Section Active Recall (`## Active Recall & Self-Assessment`)**:
  * 3–5 pertanyaan penalaran/sintesis mandiri.
  * Kunci jawaban/pembahasan dibungkus dalam tag HTML foldable (`<details><summary>Jawaban & Pembahasan</summary>...</details>`).
* **Checklist Konsep Ekstraksi (`## Concepts to Extract`)**:
  * Daftar calon *Concept Note* berupa checklist wikilink (`- [ ] [[Nama_Konsep]]`). **Tidak** langsung membuat berkas konsep baru secara otomatis.

### 3. Frontmatter & Metadata
Gunakan frontmatter standar:
```yaml
---
title: "Readings: <Judul Materi>"
subject: "<Subject>"
notes_by: agent
status: done
sources:
  - "[[Judul_Notes_Inbox_atau_Source]]"
promoted_to: []
tags:
  - generated-reading
  - self-study
---
```

### 4. Manajemen Berkas Sumber (Inbox Archiving)
* Setelah *Generated Reading* selesai dibuat dan diverifikasi:
  * Jika berkas sumber utama berasal dari `00_Inbox/`, pindahkan berkas sumber tersebut ke `90_Archive/Inbox_Processed/<Judul_Berkas>.md`.
  * Pastikan tautan `sources:` di frontmatter merujuk dengan tepat.
