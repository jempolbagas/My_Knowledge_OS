---
name: teaching-material-creator
description: Multi-step workflow for creating teaching packages (Materi Ajar & LKPD/Soal Evaluasi) separated into subject subfolders in 10_Spaces/12_Teaching.
---

# Teaching Material Creator Skill

Skill ini digunakan saat pengguna meminta untuk membuat bahan ajar, modul ajar, handout, LKPD, atau latihan soal berdasarkan catatan/sumber di dalam vault.

## Aturan & Konvensi Penyusunan:

### 1. Pemisahan Berkas Berdasarkan Subjek
Selalu pisahkan antara Materi Ajar dan Lembar Aktivitas/Soal ke dalam subfolder subjek masing-masing (misalnya: `Social_Studies`, `Science`, `Biology`, dll.):

* **File Utama (Materi Ajar / Handout / Modul Ajar):**
  * **Lokasi:** `10_Spaces/12_Teaching/30_Sources/<Subject>/Materi_<Judul_Materi>.md`
  * **Konten:** Diperluas secara mendalam dan terstruktur (definisi, konsep, tingkatan, klasifikasi, contoh real, analisis bab per bab, hingga aspek ekologis/aplikatif).
  * **Ketentuan Format:** 
    - **Jangan** menyertakan outline slide presentasi kecuali diminta secara eksplisit oleh pengguna.
    - **Visualisasi & Diagram:**
      - Gunakan diagram Mermaid (`mermaid` code block seperti `flowchart TD` atau `graph TD`) untuk visualisasi alur, hirarki, atau konsep terstruktur sederhana.
      - **Diagram Matematika Bertingkat / Kompleks (misal: Skema Selisih Bertingkat, Piramida Rumus):** Jangan paksa menggunakan Mermaid atau monospace text block jika tampilannya berantakan/kurang intuitif. Gunakan `generate_image` untuk membuat aset gambar diagram berkualitas tinggi, simpan ke folder terpusat vault `30_Assets/` (`30_Assets/<nama_aset>.jpg`), lalu sematkan di dalam catatan menggunakan sintaks gambar Obsidian (`![[<nama_aset>.jpg]]`). Dilarang membuat folder `30_Assets` lokal di dalam sub-space.


* **File Praktik (LKPD & Soal Evaluasi):**
  * **Lokasi:** `10_Spaces/12_Teaching/40_Practice/<Subject>/LKPD_dan_Soal_<Judul_Materi>.md`
  * **Konten:** 
    1. Lembar Kerja Peserta Didik (LKPD: Aktivitas Kelompok, Tabel Klasifikasi, Matriks Komparasi, Studi Kasus HOTS).
    2. Latihan Soal Mandiri (Pilihan Ganda HOTS & Soal Uraian Penalaran).
    3. Kunci Jawaban Lengkap, Pembahasan, & Rubrik Penilaian.

### 2. Penyesuaian Target Audiens
* Pastikan materi dan tingkat kesulitan soal disesuaikan dengan jenjang target peserta didik (SD, SMP, atau SMA).
* Jika diminta atau untuk target peserta didik SMA/muda, gunakan **gaya bahasa yang santai, chill, dan komunikatif** (dengan analogi kehidupan sehari-hari yang relatable seperti dompet pribadi, uang saku, atau konteks populer), namun tetap mempertahankan presisi, keakuratan akademik, dan kelengkapan materi.

### 3. Frontmatter & Metadata
Gunakan frontmatter standar untuk setiap berkas yang dibuat:
* `title`, `target_audience`, `created`, `sources` (menggunakan wikilinks `[[...]]` ke catatan sumber), dan `tags`.

### 4. Workflow Modularisasi Topik Besar (Big Topic Modularization)
Jika topik materi ajar mencakup cakupan luas (>200-300 baris atau memuat 3+ sub-bahasan utama), gunakan pendekatan **Modularisasi** dengan aturan berikut:

1. **Pengelompokan Subfolder Terdedikasi (`30_Sources/`):**
   * Buat subfolder khusus nama topik di bawah folder subjek: `10_Spaces/12_Teaching/30_Sources/<Subject>/<Nama_Topik>/` (misal: `Social_Studies/Pendapatan_Nasional/`).
   * Seluruh berkas materi (Master Dashboard & Sub-Modul) disimpan di dalam subfolder terdedikasi ini.

2. **Master Dashboard Note (`Materi_<Nama_Topik>.md`):**
   * Berfungsi sebagai indeks navigasi dan pusat kontrol materi.
   * **Struktur Wajib:** Overview Eksekutif, Peta Konsep Utama (Diagram Mermaid `graph TD`), Tabel Navigasi Modul dengan Wikilinks `[[...]]`, dan Cheatsheet Formula Gabungan.

3. **Penamaan Sub-Modul Ringkas & Berfokus Judul:**
   * Nama berkas sub-modul harus ringkas dan langsung berfokus pada judul topik/modulnya (contoh: `Materi_Konsep_Pendapatan_Nasional.md`, `Materi_Pendapatan_Per_Kapita.md`, `Materi_Distribusi_Pendapatan.md`). Hindari imbuhan nomor urut yang terlalu panjang.

4. **Penempatan Berkas Praktik / LKPD (`40_Practice/`):**
   * Berkas LKPD (`LKPD_dan_Soal_<Nama_Topik>.md`) **tetap berada di folder utama** `10_Spaces/12_Teaching/40_Practice/<Subject>/` (tanpa membuat subfolder) agar seragam dengan LKPD lain.
   * Daftarkan Master Dashboard & seluruh Sub-Modul di bagian `sources:` pada frontmatter LKPD.
   * Tambahkan bilah navigasi Wikilinks interaktif di bagian paling atas dokumen LKPD.

5. **Bilah Navigasi Antar-Modul (Cross-Module Navigation):**
   * Di bagian atas dan bawah setiap sub-modul, sertakan bilah navigasi cepat (misal: `[[Master_Dashboard]] | Modul Ini | [[Modul_Berikutnya]] | [[LKPD]]`).

