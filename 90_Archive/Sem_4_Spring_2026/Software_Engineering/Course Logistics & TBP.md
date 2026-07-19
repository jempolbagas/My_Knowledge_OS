---
title: "[SE] Course Logistics & TBP"
course: Software Engineering
tags: ["software-engineering", "logistics"]
aliases: ["[SE] Course Logistics & TBP"]
created: "2026-03-12"
type: Logistics
topic: "Overview & Course Introduction"
semester: 4
status: 🌿 incubating
---

# Course Logistics & Team Based Project (TBP) - Software Engineering

**Reference:** Slides Pertemuan 1 — Overview SE & Kontrak Kuliah, oleh Haryono Setiadi
**Source:** [[20_Brain_Atlas/30_Reference_Lib/PDFs/SE/[SE] 1 - .pdf|Pertemuan_1.pdf]]
**Terkait:** [[20_Brain_Atlas/20_Concepts/Software_Engineering/Software Engineering Course Overview|Software Engineering Course Overview]]

---

## 1. Kontrak Kuliah — Struktur, Penilaian, dan Aturan

### 1.1 CPMK (Capaian Pembelajaran Mata Kuliah)

Ada dua target kompetensi utama yang harus dikuasai di akhir semester:

- **CPMK 351:** Mahasiswa mampu memahami konsep **Process Model** dalam Software Engineering — termasuk waterfall, iteratif, agile, dan mengetahui kapan masing-masing model paling tepat digunakan.
- **CPMK 352:** Mahasiswa mampu membuat rancangan aplikasi sistem cerdas menggunakan model dalam rekayasa perangkat lunak — mulai dari fase requirements hingga deployment.

Output akhirnya bukan sekadar pemahaman teoritis, melainkan kemampuan untuk mempraktikkannya dalam Team Based Project sepanjang semester.

### 1.2 Struktur Perkuliahan (3 SKS + 1 SKS)

Mata kuliah ini terdiri dari dua komponen yang saling melengkapi:

**Teori (3 SKS):** Kelas reguler yang mencakup konsep SE dan process model, diskusi kelas dengan metode Case Method, studi literatur dan analisis kasus, serta UTS & UAS yang berbasis pemahaman konsep (bukan hafalan).

**Praktikum (1 SKS):** Sesi kerja tim untuk Team Based Project (TBP) dengan 5 milestone sepanjang semester, demo produk dan review artefak, dalam 12 pertemuan praktikum yang terstruktur.

Prinsip pentingnya: **materi teori yang dipelajari di kelas langsung dipraktikkan di sesi praktikum di minggu yang sama.** Ini bukan kuliah teori yang terpisah dari praktik — keduanya dirancang sebagai satu kesatuan pembelajaran yang terintegrasi.

### 1.3 Skema Penilaian

| Komponen | Bobot | Keterangan |
|---|---|---|
| Team Based Project (TBP) | **40%** | Proyek kelompok dengan 5 milestone |
| Case Method | 20% | 4 sesi analisis kasus terstruktur |
| UTS | 15% | Ujian Tengah Semester berbasis pemahaman |
| UAS | 15% | Ujian Akhir Semester komprehensif |
| Tugas Individu | 10% | Latihan mandiri penguatan konsep |

TBP memiliki bobot terbesar (40%), yang berarti konsistensi kerja tim sepanjang semester sangat menentukan nilai akhir. Ini bukan komponen yang bisa "dikejar" di akhir semester — 5 milestone tersebar sepanjang semester dan setiap milestone memiliki bobotnya sendiri.

### 1.4 Case Method

Case Method adalah metode pembelajaran berbasis studi kasus nyata yang digunakan di 4 sesi khusus sepanjang semester. Setiap sesi, mahasiswa menganalisis skenario proyek software nyata dan menghasilkan **1 halaman analisis terstruktur** — bukan makalah panjang, tapi analisis singkat yang tajam dan berisi reasoning yang kuat.

Yang dinilai **bukan hafalan definisi**, melainkan kualitas reasoning: *mengapa* kamu memilih pendekatan tertentu? *Apa* trade-off-nya? Tidak ada jawaban benar-salah mutlak — yang penting adalah argumen logis yang didukung pemahaman konsep SE.

### 1.5 Aturan Kelas

**Kehadiran:** Keterlambatan lebih dari 15 menit dianggap tidak hadir. Kehadiran minimum mengikuti kebijakan universitas.

**Partisipasi Aktif:** Bertanya, menjawab, dan berpendapat di kelas menjadi catatan penilaian soft skill. Kelas ini bukan kuliah satu arah — diskusi dan interaksi sangat dihargai.

**Menghargai Presentasi Tim Lain:** Saat tim lain sedang presentasi, berikan feedback yang konstruktif. Tidak bermain HP atau mengabaikan presentasi bukan sekadar sopan santun — ini adalah bentuk profesionalisme yang dilatih sejak dini.

### 1.6 Integritas Akademik

**Yang dilarang:**
- **Plagiarisme dokumen:** Menyalin SRS atau laporan milik tim lain.
- **Plagiarisme kode:** Copy-paste kode tanpa memahaminya dan tanpa memberikan atribusi kepada sumbernya.
- **Fabrication:** Membuat data palsu dalam artefak atau laporan.
- **Free-rider:** Tercantum nama di tim tapi tidak berkontribusi nyata.

**Yang diharapkan:**
- Selalu cantumkan referensi jika menggunakan sumber dari luar.
- Pahami setiap baris kode yang disubmit — karena saat demo, dosen akan bertanya.
- Gunakan AI secara bertanggung jawab (lihat seksi AI Usage).
- Jujur dalam peer evaluation.

Ada satu risiko nyata yang perlu diperhatikan: jika kode di-copy dari internet tanpa benar-benar dipahami, saat demo dosen bertanya "bagaimana bagian ini bekerja?", tidak bisa menjelaskan — dan nilai milestone bisa menjadi 0. Lebih baik memiliki fitur yang sedikit tapi benar-benar dipahami, daripada banyak fitur yang tidak bisa dijelaskan.

---

## 2. Team Based Project (TBP) — Milestone & Workflow

### 2.1 Timeline 12 Sesi Praktikum

Dua belas sesi praktikum dibagi menjadi 5 milestone dengan fokus yang berbeda di setiap blok:

| Sesi | Fokus Milestone | Deliverable Utama |
|---|---|---|
| P1 – P3 | **M1: Requirements** | Bentuk tim, pilih studi kasus, definisi requirements, buat SRS & product backlog awal |
| P4 – P5 | **M2: Design** | Buat UML-lite, desain UI wireframe, susun ERD, review desain antar tim |
| P6 – P8 | **M3: Implementation** | Implementasi fitur inti, integrasi komponen cerdas, iterasi prototype |
| P9 – P10 | **M4: Testing** | Tulis test case manual, buat unit test minimal, bug fixing |
| P11 – P12 | **M5: Polish & Deploy** | Polish UI, finalisasi dokumentasi, siapkan demo script, submit AI log |

Tim yang mengikuti timeline ini secara konsisten hampir selalu berhasil menyelesaikan proyek dengan baik. Masalah terbesar biasanya terjadi ketika tim menunda pekerjaan milestone awal dan mencoba mengerjakannya semua di akhir semester.

### 2.2 Peran dalam Tim

Setiap anggota tim harus memiliki peran yang jelas agar tidak ada yang saling menunggu. Peran bersifat fleksibel — satu orang boleh merangkap lebih dari satu peran:

- **Koordinator / PM (Project Manager):** Mengelola timeline dan product backlog, memastikan semua anggota on-track, menjadi titik komunikasi utama tim.
- **Developer:** Menulis kode, mengimplementasi fitur, dan mengintegrasikan komponen-komponen yang dikerjakan anggota berbeda.
- **QA / Docs:** Bertanggung jawab atas testing, dokumentasi, dan memastikan kualitas semua artefak yang disubmit.

### 2.3 Standar Repo & Git Workflow

Semua tim wajib menggunakan GitHub dengan workflow dasar berikut:

- **Satu repo per tim** dengan semua anggota memiliki akses sebagai contributor, dan issue board diaktifkan untuk task tracking.
- **Branch → Pull Request → Review:** Jangan push langsung ke `main`. Buat branch terpisah per fitur, submit Pull Request (PR), dan review dilakukan oleh minimal satu anggota lain sebelum merge. Ini mensimulasikan workflow yang digunakan di hampir semua tim software profesional.
- **Commit message yang jelas:** Contoh yang baik: `feat: add login validation`, `fix: resolve null pointer in payment module`. Contoh yang buruk: `fix stuff`, `update`, `wkwkwk`. Commit message yang baik membuat riwayat proyek bisa dibaca seperti cerita — memudahkan debugging dan review di kemudian hari.

**PR Checklist sebelum merge:**
- Kode bisa dijalankan tanpa error
- Tidak ada credentials atau token yang ter-expose di kode
- Penamaan variabel dan fungsi konsisten
- Ada komentar untuk logika yang kompleks

### 2.4 Bukti (Evidence) yang Dinilai

Penilaian TBP berbasis bukti nyata — bukan klaim lisan. Lima jenis evidence yang harus ada:

1. **Link Repo:** Repository GitHub aktif dengan commit history yang menunjukkan kontribusi setiap anggota tim.
2. **Screenshot Run/Test:** Bukti visual bahwa aplikasi berjalan dan test berhasil dieksekusi.
3. **Dokumen SRS/UML/ERD:** File artefak desain tersimpan rapi di folder `/docs` dalam repository.
4. **Test Case & Unit Test:** File test case manual dan script unit test yang bisa di-run ulang oleh siapapun.
5. **AI-Usage Log:** Catatan penggunaan AI yang berisi: tanggal, tools yang dipakai, prompt yang diberikan, output yang diterima, dan bagaimana output tersebut diverifikasi atau dimodifikasi.

### 2.5 Project Spec Minimal

Untuk menjaga kesetaraan antar tim, semua proyek TBP harus memenuhi spesifikasi minimal berikut:

1. **Minimal 3 role user** yang berbeda dalam sistem (contoh: admin, user biasa, moderator).
2. **Minimal 2–3 fitur inti end-to-end** yang berjalan lengkap dari input hingga output — bukan setengah jadi atau menggunakan data dummy.
3. **1 komponen "cerdas" level beginner** — bisa berupa rule-based system, simple scoring, atau integrasi dengan AI API yang tersedia.
4. **Artefak wajib lengkap:** SRS, UML-lite, ERD, testing documentation, dan README harus tersedia di repository.

Scope ini dirancang agar beginner-friendly namun cukup menantang untuk merasakan proses Software Engineering secara utuh dan bermakna.
