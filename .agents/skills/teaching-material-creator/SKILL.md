---
name: teaching-material-creator
description: Multi-step workflow for creating teaching packages (Materi Ajar & LKPD/Soal Evaluasi) separated into subject subfolders in 10 Spaces/12 Teaching.
---

# Teaching Material Creator Skill

Skill ini digunakan saat pengguna meminta untuk membuat bahan ajar, modul ajar, handout, LKPD, atau latihan soal berdasarkan catatan/sumber di dalam vault.

## Aturan & Konvensi Penyusunan:

### 1. Pemisahan Berkas Berdasarkan Subjek & Konvensi Penamaan

Selalu pisahkan antara Materi Ajar dan Lembar Aktivitas/Soal ke dalam subfolder subjek masing-masing (misalnya: `Social_Studies`, `Science`, `Biology`, dll.) menggunakan format **`snake_case`** dengan akhiran jenjang pendidikan (**`_SMP`** atau **`_SMA`**):

* **File Utama (Materi Ajar / Handout / Modul Ajar):**
  * **Lokasi & Penamaan:** `10 Spaces/12 Teaching/30 Sources/<Subject>/<Judul_Topik>_<Level>.md` *(tanpa imbuhan `Materi_`, wajib menyertakan akhiran `_SMP` atau `_SMA`)*.
    - Contoh: `Pengenalan_Sel_SMP.md`, `Dinamika_Gerak_SMA.md`
  * **Konvensi Judul:**
    - **Frontmatter Title (`title:`):** Clean title tanpa awalan `"Materi Ajar:"` (contoh: `title: "Pengenalan Sel — Unit Terkecil Kehidupan"`).
    - **H1 Header (`#`):** `# <Judul Topik> — <Subtitle Hook> <Emoji>` (contoh: `# Pengenalan Sel — Keliling Dunia Mikroskopis! 🦠✨`).
  * **Konten:** Diperluas secara mendalam dan terstruktur (definisi, konsep, tingkatan, klasifikasi, contoh real, analisis bab per bab, hingga aspek ekologis/aplikatif).
  * **Ketentuan Format:** 
    - **Jangan** menyertakan outline slide presentasi kecuali diminta secara eksplisit oleh pengguna.
    - **Visualisasi & Diagram:**
      - Utamakan penggunaan aset gambar visual berkualitas tinggi (disimpan di folder terpusat vault `30 Assets/`, dibuat via `generate_image` atau hasil pencarian web) dibandingkan blok kode Mermaid atau diagram ASCII art. Sematkan di dalam catatan menggunakan sintaks gambar Obsidian (`![[<nama_aset>.ext]]`).
      - **Standar Desain:** Clean Light / Academic Mode (latar belakang putih atau krem lembut, tipografi gelap kontras tinggi, highlight aksen yang cerah).
      - **Estetika Layout:** Kartu infografis vektor sudut membulat (rounded vector cards) yang terstruktur dengan bayangan lembut, panah penghubung yang bersih, dan hirarki visual yang kuat.
      - **Kebijakan Rasio Aspek (Aspect Ratio):** Rasio adaptif — 16:9 lanskap untuk alur proses/mindmap lebar; 3:4 potret untuk alur vertikal bertingkat yang tinggi.
      - **Konvensi Penamaan di `30 Assets/`:** Gunakan format `<type>_<subject>_<topic>_<descriptor>.ext` (huruf kecil `snake_case`), di mana `<type>` menentukan jenis aset (`diagram_` untuk flowchart, `chart_` untuk grafik/kurva, `mindmap_` untuk pohon konsep, `infographic_` untuk ringkasan visual, `illustration_` untuk grafik konsep; contoh: `mindmap_economics_national_income_dashboard.jpg`). Dilarang keras membuat folder `30 Assets` lokal di dalam sub-space.

* **File Praktik (LKPD & Soal Evaluasi):**
  * **Lokasi & Penamaan:** 
    - **LKPD / Worksheet:** `10 Spaces/12 Teaching/40 Practice/<Subject>/LKPD_<Judul_Topik>_<Level>.md` (contoh: `LKPD_Pengenalan_Sel_SMP.md`)
    - **Paket Evaluasi / Soal Ulangan:** `10 Spaces/12 Teaching/40 Practice/<Subject>/Soal_<Judul_Topik>_<Level>.md` (contoh: `Soal_Dinamika_Gerak_SMA.md`)
  * **Konvensi Judul:**
    - **Frontmatter Title (`title:`):** `title: "LKPD: <Judul Topik>"` atau `title: "Soal Evaluasi: <Judul Topik>"`.
    - **H1 Header (`#`):** `# Lembar Kerja Peserta Didik (LKPD): <Judul Topik>` atau `# Paket Soal Evaluasi: <Judul Topik>`.
  * **Konten:** 
    1. Lembar Kerja Peserta Didik (LKPD: Aktivitas Kelompok, Tabel Klasifikasi, Matriks Komparasi, Studi Kasus HOTS).
    2. Latihan Soal Mandiri (Pilihan Ganda HOTS & Soal Uraian Penalaran).
    3. Kunci Jawaban Lengkap, Pembahasan, & Rubrik Penilaian.

### 2. Penyesuaian Target Audiens
* Pastikan materi dan tingkat kesulitan soal disesuaikan dengan jenjang target peserta didik (SD, SMP, atau SMA).
* Jika diminta atau untuk target peserta didik SMA/muda, gunakan **gaya bahasa yang santai, chill, dan komunikatif** (dengan analogi kehidupan sehari-hari yang relatable seperti dompet pribadi, uang saku, atau konteks populer), namun tetap mempertahankan presisi, keakuratan akademik, dan kelengkapan materi.

### 3. Frontmatter & Metadata
Gunakan frontmatter standar untuk setiap berkas yang dibuat:
* `title`, `type` (`materi` | `master-dashboard` | `lkpd` | `soal-evaluasi`), `subject`, `level` (`smp` | `sma`), `target_audience`, `created`, `sources` (menggunakan wikilinks `[[...]]` ke catatan sumber), dan `tags`.

### 4. Workflow Modularisasi Topik Besar (Big Topic Modularization)
Jika topik materi ajar mencakup cakupan luas (>200-300 baris atau memuat 3+ sub-bahasan utama), gunakan pendekatan **Modularisasi** dengan aturan berikut:

1. **Pengelompokan Subfolder Terdedikasi (`30 Sources/`):**
   * Buat subfolder khusus nama topik di bawah folder subjek: `10 Spaces/12 Teaching/30 Sources/<Subject>/<Nama_Topik>/` (misal: `Social_Studies/Pendapatan_Nasional/`).
   * Seluruh berkas materi (Master Dashboard & Sub-Modul) disimpan di dalam subfolder terdedikasi ini.

2. **Master Dashboard Note (`<Nama_Topik>_<Level>.md`):**
   * Berfungsi sebagai indeks navigasi dan pusat kontrol materi (misal: `Pendapatan_Nasional_SMA.md`).
   * **Struktur Wajib:** Overview Eksekutif, Peta Konsep Utama / Infografis Visual (Menggunakan Aset Gambar Visual di `30 Assets/` yang dibuat via `generate_image` sesuai standar visual `GEMINI.md`, disematkan dengan `![[<nama_aset>.ext]]`), Tabel Navigasi Modul dengan Wikilinks `[[...]]`, dan Cheatsheet Formula Gabungan.

3. **Penamaan Sub-Modul Ringkas & Berfokus Judul:**
   * Nama berkas sub-modul harus ringkas dalam `snake_case` dengan akhiran level (contoh: `Konsep_Pendapatan_Nasional_SMA.md`, `Pendapatan_Per_Kapita_SMA.md`, `Distribusi_Pendapatan_SMA.md`).

4. **Penempatan Berkas Praktik / LKPD (`40 Practice/`):**
   * Berkas LKPD (`LKPD_<Nama_Topik>_<Level>.md`) & Soal (`Soal_<Nama_Topik>_<Level>.md`) **tetap berada di folder utama** `10 Spaces/12 Teaching/40 Practice/<Subject>/` (tanpa membuat subfolder) agar seragam dengan LKPD lain.
   * Daftarkan Master Dashboard & seluruh Sub-Modul di bagian `sources:` pada frontmatter LKPD.
   * Tambahkan bilah navigasi Wikilinks interaktif di bagian paling atas dokumen LKPD.

5. **Bilah Navigasi Antar-Modul (Cross-Module Navigation):**
   * Di bagian atas dan bawah setiap sub-modul, sertakan bilah navigasi cepat (misal: `[[<Nama_Topik>_<Level>|🏠 Master Dashboard]] | Modul Ini | [[<Submodul_Berikutnya>_<Level>]] | [[LKPD_<Nama_Topik>_<Level>]]`).

