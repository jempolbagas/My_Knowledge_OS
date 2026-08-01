---
title: "Semester 5 Preparation Guide"
type: PrepGuide
semester: 5
tags: ["college", "semester-5", "prep-checklist"]
created: "2026-07-31"
---

# 📚 Panduan Persiapan Semester 5 (Fall 2026)

Panduan ini disusun untuk membantu kamu mempersiapkan **Semester 5 (Fall 2026)** secara optimal. Berdasarkan data dari [[00_Semester_5_Dashboard|Semester 5 Dashboard]], kamu akan mengambil **23 SKS** yang terdiri dari 6 mata kuliah utama semester 5 dan 2 mata kuliah perbaikan (retake) dari semester 3.

---

## 🎯 Ringkasan Beban Akademik (23 SKS)

| Kode / Abbr | Nama Mata Kuliah | Bobot | Tipe | Hub Mata Kuliah | Silabus (RPS) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **DS** | Distributed Systems | 3 SKS | Utama (Smt 5) | [[Distributed Systems Overview]] | [[Distributed Systems Syllabus]] |
| **CRYPTO** | Cryptography | 3 SKS | Utama (Smt 5) | [[Cryptography Overview]] | [[Cryptography Syllabus]] |
| **IP** | Image Processing | 3 SKS | Utama (Smt 5) | [[Image Processing Overview]] | [[Image Processing Syllabus]] |
| **DM** | Data Mining | 3 SKS | Utama (Smt 5) | [[Data Mining Overview]] | [[Data Mining Syllabus]] |
| **HCI** | Human & Computer Interaction | 2 SKS | Utama (Smt 5) | [[HCI Overview]] | [[Human Computer Interaction Syllabus]] |
| **NETMGMT** | Network Management | 3 SKS | Utama (Smt 5) | [[Network Management Overview]] | [[Network Management Syllabus]] |
| **NM** | Numerical Methods | 3 SKS | ⚠️ Retake (Smt 3) | [[Numerical Methods Overview]] | [[Numerical Methods Syllabus]] |
| **OS** | Operating Systems | 3 SKS | ⚠️ Retake (Smt 3) | [[Operating Systems Overview]] | [[Operating Systems Syllabus]] |

---

## 📌 Checklist Persiapan Utama (To-Do List)

> [!important]
> Tugas-tugas di bawah ini akan otomatis terdeteksi di [[00_Semester_5_Dashboard|Semester 5 Dashboard]] kamu karena menggunakan format tugas Obsidian.

### 1. Administrasi & KRS
- [ ] **Konsultasi KRS:** Hubungi Dosen Pembimbing Akademik (DPA) untuk verifikasi persetujuan retake 2 matkul (Numerical Methods & Operating Systems) bersamaan dengan 5 matkul utama.
- [ ] **KRS Online:** Lakukan pengisian KRS pada portal akademik UNS (estimasi Awal-Pertengahan Agustus 2026) dan pastikan bentrok jadwal diminimalisir.
- [ ] **Persetujuan KRS:** Pastikan status KRS berubah menjadi disetujui/aktif oleh DPA.

### 2. Pengadaan Buku & Literatur Utama
*Daftar pustaka wajib yang digunakan oleh dosen pengampu semester ini:*
- [ ] **Sistem Terdistribusi:** Dapatkan buku *Distributed Systems* (4th ed.) oleh M. van Steen & A.S. Tanenbaum.
- [ ] **Kriptografi:** Dapatkan buku *Cryptography: Theory and Practice* oleh Douglas Stinson atau *Cryptography and Network Security* oleh William Stallings.
- [ ] **Pengolahan Citra Digital (PCD):** Dapatkan buku *Digital Image Processing* oleh Gonzalez & Woods (2018/2021).
- [ ] **Data Mining:** Dapatkan buku *Introduction to Data Mining* oleh Pang-Ning Tan atau *Data Mining: Concepts and Techniques* oleh Jiawei Han.
- [ ] **Sistem Operasi (Retake):** Dapatkan buku *Operating System Concepts Essentials* oleh Abraham Silberschatz.
- [ ] **Interaksi Manusia & Komputer (IMK):** Dapatkan buku *Interaction Design: Beyond Human-Computer Interaction* oleh Jennifer Preece dkk atau buku Jeff Johnson *Designing With The Mind In Mind*.
- [ ] **Metode Numerik (Retake):** Dapatkan buku *Applied Numerical Methods with MATLAB* oleh S. C. Chapra.
- [ ] **Manajemen Jaringan:** Dapatkan materi *Introduction to Networks v7* dan *Switching, Routing, and Wireless Essentials v7* dari Cisco Networking Academy.

### 3. Review Materi Prasyarat (Hubungan dengan Vault)
Sebelum kuliah dimulai, luangkan waktu 1-2 jam untuk membaca ulang catatan yang sudah ada di vault kamu:
- [ ] **Matematika & Matriks (Untuk PCD & Metode Numerik):** Baca ulang [[Matriks]] untuk menyegarkan ingatan tentang perkalian matriks, transpose, determinan, dan invers.
- [ ] **Pemrograman Jaringan (Untuk Sistem Terdistribusi):** Baca ulang [[(CN-12) Pemrograman Jaringan Lecture Notes]] terutama bagian implementasi Socket TCP/UDP di Python karena akan langsung diuji di awal minggu perkuliahan.
- [ ] **Manajemen & Protokol Jaringan (Untuk Manajemen Jaringan):** Pelajari kembali [[(CN-7) IPv4 Lecture Notes]], [[(CN-8) IPv4 Subnetting Lecture Notes]], [[(CN-12) Pemrograman Jaringan Lecture Notes]], dan [[(CN-14) Keamanan Jaringan Lecture Notes]].
- [ ] **Dasar Keamanan & Enkripsi (Untuk Kriptografi):** Tinjau ulang konsep [[Symmetric vs. Asymmetric Encryption]], [[CIA Triad]], dan [[Cybersecurity Roadmap]] untuk memahami posisi kriptografi dalam keamanan informasi.
- [ ] **Konsep Dasar SO (Untuk Retake Operating Systems):** Pelajari konsep proses, threads, dan CPU scheduling di internet atau dari sisa catatan semester 3 untuk bersiap menghadapi *Team Based Project* (bobot 20% di SO).

### 4. Setup Environment & Tools Praktikum
- [ ] **Metode Numerik & PCD:** Pastikan MATLAB terinstall atau siapkan environment Python dengan library `numpy`, `scipy`, `matplotlib`, dan `opencv-python`.
- [ ] **Data Mining:** Siapkan environment Python (Anaconda/Jupyter Notebook) dan install library analisis data (`pandas`, `numpy`, `scikit-learn`, `seaborn`).
- [ ] **Sistem Terdistribusi:** Pastikan Docker Desktop terinstall di laptop untuk simulasi cluster/sandbox container terdistribusi.
- [ ] **Manajemen Jaringan:** Pastikan Cisco Packet Tracer atau GNS3 serta Wireshark terinstall untuk simulasi jaringan dan analisis traffic.

---

## 📊 Detail Komposisi Penilaian & Strategi Kuliah

Berikut adalah bobot penilaian dari silabus masing-masing mata kuliah untuk menyusun strategi belajarmu:

| Mata Kuliah | Tugas / Kuis | Case Method | Team Project | UTS | UAS | Strategi Kunci |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Distributed Systems** | 10% / 0% | 25% | 25% | 20% | 20% | Fokus pada proyek tim dan tugas pemrograman socket. |
| **Cryptography** | 10% / 0% | 10% | 0% | 40% (Teori 1&2) | 40% (UAS+Teori 3) | Ujian tertulis sangat mendominasi (80%). Kuasai matematika teori bilangan. |
| **Image Processing** | Tugas (Ada) | - | - | UTS (Ada) | UAS (Ada) | Latihan membuat program transformasi citra dan deteksi tepi sejak dini. |
| **Data Mining** | - | - | - | 50% | 50% | Ujian tertulis UTS/UAS 100% total bobot. Latihan soal-soal hitungan CRISP-DM dan algoritma klasifikasi/clustering. |
| **HCI / IMK** | - | 10% | 50% | 20% | 20% | *Team Based Project* bernilai setengah dari total nilai. Pilih kelompok proyek yang solid sejak minggu ke-1. |
| **Network Management** | 0% / 0% | 30% | 70% | 0% | 0% | Total nilai dari *Team Based Project* (70%) dan *Case Method* (30%). Kuasai VLAN, routing, IDS, dan simulasi. |
| **Numerical Methods** | - | - | - | 45% | 55% | Ujian tertulis UTS/UAS 100% total bobot. Pahami galat (error), iterasi SPL, dan akar non-linear. |
| **Operating Systems** | 5% | - | 35% | 30% | 30% | Proyek tim (35%) dan ujian tertulis sangat penting. Pahami manajemen memori dan sinkronisasi proses. |

---

## 📅 Rencana Kegiatan 3 Minggu Pertama Kuliah

Berikut gambaran materi yang akan langsung kamu hadapi di awal semester:

*   **Minggu 1:**
    *   **DS:** Kontrak kuliah & *Overview of Distributed Systems*.
    *   **CRYPTO:** Kriptografi Klasik & Modern (Operasi Bit, LFSR, Block Cipher) beserta Teori Bilangan pendukung.
    *   **IP:** Kontrak Kuliah & Pengenalan Pengolahan Citra Digital.
    *   **DM:** Latar belakang, peran utama, dan penerapan Data Mining.
    *   **HCI:** Konsep dasar IMK, Usability, dan User Experience.
    *   **NM:** Perhitungan galat (error) relatif dan rambatan galat.
    *   **OS:** Pendahuluan SO, Sejarah, Struktur Kernel & Layanan SO.
*   **Minggu 2:**
    *   **DS:** *Architecture of Distributed Systems*.
    *   **CRYPTO:** Teori Bilangan Lanjutan, Algoritma DES & AES.
    *   **IP:** Akuisisi Citra, Sampling & Kuantisasi, Dasar Matematika Citra (Matriks & Vektor).
    *   **DM:** Pengenalan Tools Data Mining & CRISP-DM Process.
    *   **HCI:** Konsep Interaksi & Pengenalan Evaluasi Desain.
    *   **NM:** Pengenalan Galat Numerik dan konversi sistem bilangan.
    *   **OS:** Manajemen Proses & Diagram State Proses.
*   **Minggu 3:**
    *   **DS:** *Processes in Distributed Systems* (Virtualization, Clients, Servers, Code Migration).
    *   **CRYPTO:** Kriptografi Kunci Publik (RSA, Diffie-Hellman, ElGamal) bagian 1.
    *   **IP:** Transformasi Intensitas Citra (Citra Negatif, Log, Gamma, Contrast Stretching).
    *   **DM:** Metrik Evaluasi Model Data Mining.
    *   **HCI:** *Product Discovery* & Konseptualisasi Interaksi.
    *   **NM:** Penyelesaian Sistem Persamaan Linear (SPL) secara Numerik (Metode Iteratif).
    *   **OS:** *Process Control Block* (PCB), Pengalihan Proses, dan Penciptaan Proses.
