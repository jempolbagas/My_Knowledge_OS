---
title: "Semester 5 Preparation Guide"
type: PrepGuide
semester: 5
tags: ["college", "semester-5", "prep-checklist"]
created: "2026-07-31"
updated: "2026-08-13"
---

# 📚 Panduan Persiapan Semester 5 (Gasal 2026/2027)

Panduan ini disusun untuk membantu kamu mempersiapkan **Semester 5 (Gasal 2026/2027)** secara optimal. Berdasarkan data dari [[Official_KRS_Semester_5|KRS Resmi Smt 5]], kamu secara resmi mengambil **22 SKS** (33.00 ECTS) yang terdiri dari 8 mata kuliah.

---

## 🎯 Ringkasan Beban Akademik Resmi (22 SKS / 33.00 ECTS)

| Kode / Abbr | Nama Mata Kuliah | Kelas | Bobot | Course Hub | Silabus (RPS) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **BIOCOMP** | Komputasi Biomedik | A | 3 SKS | [[Biomedical Computing Overview]] | [[BioComp Syllabus]] |
| **IMPROC** | Pengolahan Citra Digital | B | 3 SKS | [[Image Processing Overview]] | [[Improc Syllabus]] |
| **DISTSYS** | Sistem Terdistribusi | B | 3 SKS | [[Distributed Systems Overview]] | [[DistSys Syllabus]] |
| **HCI** | Interaksi Manusia & Komputer | B | 2 SKS | [[HCI Overview]] | [[HCI Syllabus]] |
| **COMVIS** | Computer Vision | A | 3 SKS | [[Computer Vision Overview]] | [[ComVis Syllabus]] |
| **SIGPRO** | Pengolahan Sinyal Digital | A | 3 SKS | [[Digital Signal Processing Overview]] | [[SigPro Syllabus]] |
| **DATMIN** | Data Mining | C | 3 SKS | [[Data Mining Overview]] | [[DatMin Syllabus]] |
| **ENTRE** | Kewirausahaan | A2 | 2 SKS | [[Entrepreneurship Overview]] | [[Entre Syllabus]] |

---

## 📌 Checklist Persiapan Utama (To-Do List)

> [!success]
> Status KRS telah disetujui DPA Ery Permana Yudha, S.Kom., M.Kom. rincian berkas tersimpan di [[Official_KRS_Semester_5]].

### 1. Administrasi & KRS
- [x] **Konsultasi KRS:** Verifikasi pengisian KRS dengan DPA (Ery Permana Yudha, S.Kom., M.Kom.).
- [x] **KRS Online:** Pengisian KRS selesai disetujui portal UNS (22 SKS / 33.00 ECTS).
- [x] **Dokumentasi Vault:** Arsip resmi KRS disimpan di [[Official_KRS_Semester_5]].

### 2. Pengadaan Buku & Literatur Utama
*Daftar pustaka wajib yang digunakan oleh dosen pengampu semester ini:*
- [ ] **Komputasi Biomedik (BIOMED):** Dapatkan *Biomedical Signal and Image Processing* oleh Kayvan Najarian atau *Bioinformatics: Sequence and Genome Analysis* oleh David W. Mount.
- [ ] **Pengolahan Citra Digital (PCD):** Dapatkan buku *Digital Image Processing* (4th ed.) oleh Rafael C. Gonzalez & Richard E. Woods.
- [ ] **Sistem Terdistribusi (DS):** Dapatkan buku *Distributed Systems* (4th ed.) oleh Maarten van Steen & Andrew S. Tanenbaum.
- [ ] **Interaksi Manusia & Komputer (IMK):** Dapatkan buku *Interaction Design: Beyond Human-Computer Interaction* oleh Preece, Rogers, Sharp atau Jeff Johnson *Designing With The Mind In Mind*.
- [ ] **Computer Vision (CV):** Dapatkan buku *Computer Vision: Algorithms and Applications* (2nd ed.) oleh Richard Szeliski atau *Deep Learning for Computer Vision* oleh Adrian Rosebrock.
- [ ] **Pengolahan Sinyal Digital (DSP):** Dapatkan buku *Digital Signal Processing: Principles, Algorithms, and Applications* oleh John G. Proakis & Dimitris G. Manolakis.
- [ ] **Data Mining (DM):** Dapatkan buku *Introduction to Data Mining* oleh Pang-Ning Tan dkk atau *Data Mining: Concepts and Techniques* oleh Jiawei Han.
- [ ] **Kewirausahaan (KWU):** Dapatkan buku *The Lean Startup* oleh Eric Ries & *Business Model Generation* oleh Alexander Osterwalder.

### 3. Review Materi Prasyarat (Hubungan dengan Vault)
Sebelum kuliah dimulai, luangkan waktu untuk membaca ulang catatan yang sudah ada di vault kamu:
- [ ] **Matematika & Matriks (Untuk PCD & CV):** Baca ulang [[Matriks]] untuk menyegarkan ingatan tentang perkalian matriks, transpose, determinan, dan invers.
- [ ] **Pemrograman Jaringan (Untuk Sistem Terdistribusi):** Baca ulang [[(CN-12) Pemrograman Jaringan Lecture Notes]] terutama bagian Socket TCP/UDP di Python.
- [ ] **Kalkulus & Respon Frekuensi (Untuk DSP):** Tinjau ulang konsep deret Fourier, transformasi sinyal, dan bilangan kompleks.
- [ ] **PyTorch / NumPy (Untuk Computer Vision & Data Mining):** Tinjau ulang [[Vectorization in NumPy]] dan dasar-dasar pemrosesan array/tensor.

### 4. Setup Environment & Tools Praktikum
- [ ] **PCD & Computer Vision:** Siapkan Python Virtual Environment (`venv` / `conda`) dengan library `opencv-python`, `torch`, `torchvision`, `scikit-image`, `albumentations`.
- [ ] **Pengolahan Sinyal Digital & Komputasi Biomedik:** Install library `scipy`, `librosa`, `wfdb` (Waveform Database untuk Biosinyal), `mne` (untuk EEG), dan `matplotlib`.
- [ ] **Data Mining:** Siapkan Jupyter Notebook/Lab dengan `pandas`, `scikit-learn`, `seaborn`, `xgboost`.
- [ ] **Sistem Terdistribusi:** Install Docker Desktop, gRPC tools (`grpcio`, `protobuf`), dan Go/Python environment.
- [ ] **Kewirausahaan:** Siapkan template Figma/Canva untuk Business Model Canvas (BMC) & Pitch Deck presentation.

---

## 📊 Detail Komposisi Penilaian & Strategi Kuliah

| Mata Kuliah | Tugas / Kuis | Case Method | Team Project | UTS | UAS | Strategi Kunci |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Komputasi Biomedik** | 15% | 30% | - | 25% | 30% | Kuasai ekstraksi fitur biosinyal & segmentasi citra MRI/CT. |
| **Pengolahan Citra Digital** | Tugas (Ada) | - | - | UTS (Ada) | UAS (Ada) | Latihan pemrograman konvolusi spatial & Fourier Transform. |
| **Sistem Terdistribusi** | 10% | 25% | 25% | 20% | 20% | Fokus pada tugas gRPC/Socket & konsensus Raft/Paxos. |
| **Interaksi Manusia & Komputer** | - | 10% | 50% | 20% | 20% | Proyek kelompok UX/UI bernilai 50%. Buat prototype Figma yang presisi. |
| **Computer Vision** | 15% | 35% | - | 25% | 25% | Pahami deteksi fitur lokal (SIFT/ORB) dan training model YOLO/CNN. |
| **Pengolahan Sinyal Digital** | 20% | - | 20% | 30% | 30% | Kuasai perhitungan Z-Transform, FFT, & perancangan filter FIR/IIR. |
| **Data Mining** | - | - | - | 50% | 50% | Latihan soal-soal hitungan manual & implementasi scikit-learn. |
| **Kewirausahaan** | 20% | - | 40% | 20% | 20% | Susun BMC yang tervalidasi dan Pitch Deck produk technopreneur. |

---

## 📅 Rencana Kegiatan 3 Minggu Pertama Kuliah

* **Minggu 1:**
  * **BIOMED:** Kontrak kuliah & Karakteristik Data Biosinyal/Medis.
  * **PCD:** Pengenalan Pengolahan Citra Digital & Matriks Citra.
  * **DS:** Overview of Distributed Systems & Arsitektur Client-Server.
  * **IMK:** Konsep dasar IMK, Usability, dan Human Factors.
  * **CV:** Geometri Pembentukan Citra & Model Kamera Pinhole.
  * **DSP:** Pengenalan Sinyal Diskrit & Operasi Sinyal Waktu Diskrit.
  * **DM:** Latar belakang, peran utama, dan tahapan CRISP-DM.
  * **KWU:** Mindset Technopreneurship & Identifikasi Masalah Pasar.
* **Minggu 2:**
  * **BIOMED:** Pra-pengolahan Biosinyal ECG/EEG (Filtering Noise).
  * **PCD:** Akuisisi Citra, Sampling, Kuantisasi, & Model Warna.
  * **DS:** Socket Programming & RPC/gRPC Fundamentals.
  * **IMK:** User-Centered Design (UCD) & Evaluasi Heuristik.
  * **CV:** Operasi Filter Spasial & Deteksi Tepi (Canny, Sobel).
  * **DSP:** Sistem LTI Diskrit & Konvolusi Waktu Diskrit.
  * **DM:** Pengenalan Data Preprocessing & Cleaning.
  * **KWU:** Customer Discovery & Validasi Masalah Konsumen.
* **Minggu 3:**
  * **BIOMED:** Ekstraksi Fitur Sinyal Domain Waktu & Frekuensi.
  * **PCD:** Transformasi Intensitas Citra (Histogram Equalization).
  * **DS:** Waktu & Sinkronisasi (Lamport Timestamps, Vector Clocks).
  * **IMK:** Information Architecture & Low-Fidelity Wireframing.
  * **CV:** Ekstraksi Fitur Lokal (SIFT, SURF, ORB Feature Matching).
  * **DSP:** Teorema Sampling Nyquist & Analisis Aliasing.
  * **DM:** Metrik Evaluasi Model Klasifikasi & Clustering.
  * **KWU:** Penyusunan Business Model Canvas (BMC) & Value Proposition.
