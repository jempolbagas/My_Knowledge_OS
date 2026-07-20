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
  * **Ketentuan Format:** **Jangan** menyertakan outline slide presentasi kecuali diminta secara eksplisit oleh pengguna.

* **File Praktik (LKPD & Soal Evaluasi):**
  * **Lokasi:** `10_Spaces/12_Teaching/40_Practice/<Subject>/LKPD_dan_Soal_<Judul_Materi>.md`
  * **Konten:** 
    1. Lembar Kerja Peserta Didik (LKPD: Aktivitas Kelompok, Tabel Klasifikasi, Matriks Komparasi, Studi Kasus HOTS).
    2. Latihan Soal Mandiri (Pilihan Ganda HOTS & Soal Uraian Penalaran).
    3. Kunci Jawaban Lengkap, Pembahasan, & Rubrik Penilaian.

### 2. Penyesuaian Target Audiens
* Pastikan materi dan tingkat kesulitan soal disesuaikan dengan jenjang target peserta didik (SD, SMP, atau SMA).

### 3. Frontmatter & Metadata
Gunakan frontmatter standar untuk setiap berkas yang dibuat:
* `title`, `target_audience`, `created`, `sources` (menggunakan wikilinks `[[...]]` ke catatan sumber), dan `tags`.
