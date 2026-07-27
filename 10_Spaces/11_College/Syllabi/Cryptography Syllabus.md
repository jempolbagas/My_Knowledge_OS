---
title: "[CRYPTO] Syllabus - Cryptography"
course: "Cryptography"
tags: ["college", "syllabus", "rps", "semester-5"]
aliases: ["Crypto Syllabus", "Cryptography Syllabus", "[CRYPTO] Syllabus - Cryptography"]
created: "2026-07-27"
type: Syllabus
semester: 5
---

# RENCANA PEMBELAJARAN SEMESTER (RPS)
**PROGRAM STUDI INFORMATIKA**  
**FAKULTAS TEKNOLOGI INFORMASI DAN SAINS DATA**  
**UNIVERSITAS SEBELAS MARET**

---

## 1. Identitas Mata Kuliah

| Field | Detail |
| :--- | :--- |
| **Kode Mata Kuliah** | 12013130324 |
| **Nama Mata Kuliah** | Kriptografi |
| **Jenis Mata Kuliah** | Pilihan |
| **Semester** | 5 |
| **Bobot Mata Kuliah (SKS)** | 3 SKS |
| **a. Bobot Tatap Muka** | 3 SKS |
| **b. Bobot Praktikum** | 0 SKS |
| **c. Bobot Praktek Lapangan** | 0 SKS |
| **d. Bobot Simulasi** | 0 SKS |
| **Mata Kuliah Prasyarat** | - |
| **Tanggal Dibuat / Perbaikan** | 2023-08-26 / Perbaikan Ke-1 (Edit: 2023-08-26) |

### Identitas dan Validasi

*   **Dosen Pengembang RPS:** Prof. Drs. Bambang Harjito M.App.Sc., Ph.D.
*   **Koord. Kelompok Mata Kuliah:** Prof. Drs. Bambang Harjito M.App.Sc., Ph.D.
*   **Ketua Program Studi:** RISTU SAPTONO, S.Si., M.T., Ph.D.

---

## 2. Capaian Pembelajaran & Deskripsi Mata Kuliah

### Capaian Pembelajaran Lulusan (CPL) / Learning Outcome (LO)
*   **CPLO3:** Mampu menguasai dasar-dasar pengetahuan dan konsep-konsep teoritis bidang informatika, yang meliputi matematika, logika, algoritma, komputasi, struktur data, pemrograman, sistem komputer dan jaringan, pengolahan data, perangkat lunak, kecerdasan buatan, teori bahasa dan Automata, Statistika, dan analisis numerik.

### Capaian Pembelajaran Mata Kuliah (CPMK) / Bahan Kajian
Mahasiswa mampu melakukan pengamanan data dengan enkripsi maupun dekripsi terhadap suatu pesan dengan menggunakan metoda *private key system* maupun *public key system*, melakukan tanda tangan secara digital terhadap document dan mampu memahami pengembangan tentang *post-quantum cryptography*. Selanjutnya Mahasiswa mampu memahami tentang *Watermarking*.

### Deskripsi Mata Kuliah
Mahasiswa diajarkan menjelaskan konsep dasar kriptografi, menggunakan dasar matematika terutama teori bilangan, menggunakan *cryptosystem* baik *private* maupun *public* untuk keamanan data, menjelaskan teori informasi dalam kriptografi, melakukan *signature*, serta dapat mengembangkan konsep *post-quantum cryptography* dan mengenal *watermarking*.

---

## 3. Basis Penilaian

| Basis Penilaian | Komponen | Bobot |
| :--- | :--- | :--- |
| **a. Aktivitas Partisipatif (Case Method)** | Case Method | 30% |
| **b. Hasil Proyek (Team Based Project)** | Project | 40% |
| **c. Tugas** | Tugas | 10% |
| **d. Kuis** | Kuis | 0% |
| **e. UTS** | UTS | 0% |
| **f. UAS** | UAS | 20% |

---

## 4. Daftar Referensi

1. Douglas Stinson and Maura B. Paterson, *Cryptography: Theory and Practice*, CRC Press Taylor & Francis Group, 2019. [Link](https://www.amazon.com/Cryptography-Theory-Practice-Textbooks-Mathematics/dp/1138197017)
2. William Stallings, *Cryptography and Network Security Principles and Practices*, Fourth/Fifth Edition, Prentice Hall, 2011/2019.

---

## 5. Rencana Kegiatan Pembelajaran Mingguan

| Ming-gu | Kemampuan Akhir / Sub-CPMK (Kode CPL) | Materi Pokok | Referensi | Metode Pembelajaran (Luring/Daring) | Waktu | Pengalaman Belajar | Basis Penilaian | Teknik Penilaian | Indikator, Kriteria, (Tingkat Taksonomi) | Bobot |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| **1-4** | Mahasiswa dapat mengenal sejarah, definisi, konsep dasar kriptografi, serta urgensinya... menerapkan matematika teori bilangan, mengimplementasikan algoritma klasik & modern (DES, Bit, LFSR, Block cipher). *(KODE 3)* | Kriptografi Klasik modern (Operasi Bit, LFSR dan Block cipher), Algoritma AES, Algoritma DES | Cryptography: Theory and Practice | Studi Kasus, Pembelajaran Berbasis Masalah | 4 × 600 Menit | Pembelajaran berbasis masalah dengan memberikan soal teori bilangan untuk implementasi kriptografi klasik | Case Method | Tes Tertulis | 1. Dapat mendefinisikan kriptografi & aspek keamanan TI. Menerapkan teori grup & ring. Membuat penyandian klasik (substitusi, Vigenère, Hill, transposisi).<br>2. Menggunakan bit & XOR, menjelaskan stream/block cipher, & algoritma simetris. | 20% |
| **5-7** | Mahasiswa dapat menjelaskan & menggunakan algoritma kunci publik (asimetris) untuk keamanan TI, kunci privat & publik, konsep public key cryptosystem, RSA, Diffie-Hellman, ElGamal. *(KODE 3)* | Kunci privat & publik, Public Key Cryptosystem, Teorema Kecil Fermat, Sistem Kripto RSA, Protokol Diffie-Hellman, Sistem Kripto ElGamal | Cryptography: Theory and Practice | Studi Kasus, Pembelajaran Berbasis Proyek | 3 × 450 Menit | Pembelajaran berbasis masalah dengan contoh, latihan, serta implementasi dalam program | Tugas | Tes Tertulis | Dapat menjelaskan kunci publik & privat, Teorema Kecil Fermat & aplikasinya di $Z_n$, prinsip kerja RSA & pembuktian formal, Diffie-Hellman, serta ElGamal. | 10% |
| **8-10** | Mahasiswa mampu menjelaskan prinsip kerja Diffie-Hellman, ElGamal, serta menggunakan ECC untuk enkripsi/dekripsi. *(KODE 3)* | Protokol Diffie-Hellman, Sistem Kripto ElGamal, Lapangan Berhingga, Kurva Eliptik pada GF(p), Eliptic ElGamal, ECC | Cryptography: Theory and Practice | Studi Kasus, Pembelajaran Berbasis Proyek | 3 × 450 Menit | Pembelajaran berbasis masalah dengan contoh latihan, soal, & diterapkan dalam program | Case Method | Tes Tertulis | Menjelaskan prinsip & contoh penerapan Diffie-Hellman & ElGamal. Menjelaskan konsep lapangan berhingga, kurva eliptik pada GF(p), & penggunaannya dalam kriptografi. | 10% |
| **11-12** | Mahasiswa dapat melakukan kriptanalisis & menganalisis algoritma yang digunakan, konsep & cara kerja skema tanda tangan digital (DSS, RSA, Ong-Schnorr-Shamir, Batch verification). *(KODE 3)* | Konsep & cara kerja DSS, Skema Tanda Tangan Digital RSA, Skema Ong-Schnorr-Shamir, Metode verifikasi batch | Cryptography: Theory and Practice | Diskusi Kelompok, Studi Kasus | 2 × 300 Menit | Studi kasus dengan contoh soal & latihan yang diimplementasikan dalam program | UAS | Tes Tertulis | Menjelaskan konsep DSS, prinsip & cara kerja skema RSA & Ong-Schnorr-Shamir beserta contoh penerapannya, serta contoh verifikasi batch. | 20% |
| **13-15** | Mahasiswa dapat menjelaskan konsep Post Quantum Cryptography (NTRU Cryptosystem & turunannya). *(KODE 3)* | Konsep Lattice, Teori Ring, Kriptografi Asimetris, Post Quantum Cryptography (NTRU Cryptosystem & turunannya) | Cryptography: Theory and Practice | Pembelajaran Berbasis Proyek | 3 × 450 Menit | Pembelajaran berbasis masalah dengan memberikan contoh & soal | Team Based Project | Tes Tertulis | Memahami konsep Post-Quantum Cryptography, menerapkan proses Enkripsi & Dekripsi dari NTRU cryptosystem. | 40% |
| **16** | Dapat mengamankan data citra dengan teknik watermarking. *(KODE 3)* | Digital Watermarking Image (SVD Watermarking) | Cryptography and Network Security | Studi Kasus | 1 × 150 Menit | Studi kasus untuk mengimplementasikan watermark dalam citra | Case Method | Partisipasi | Dapat menyisipkan watermark ke dalam citra dan mengekstrak kembali watermark dari citra. | 0% |
