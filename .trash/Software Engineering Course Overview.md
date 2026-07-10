---
title: "[SE] 1 - SE Overview"
course: Software Engineering
tags: ["software-engineering", "sdlc", "lecture-note"]
aliases: ["[SE] 1 - SE Overview"]
created: "2026-03-12"
type: Lecture
topic: "Overview & Course Introduction"
semester: 4
status: 🌿 incubating
---

# Overview Software Engineering & Kontrak Kuliah


**Reference:** Slides Pertemuan 1 — Overview SE & Kontrak Kuliah, oleh Haryono Setiadi
**Source:** [[Pertemuan_1.pdf]]
<!-- **Praktikum/Tugas Terkait:** [[Praktikum P1 — Pembentukan Tim & Setup Repo]] -->

---

## Daftar Isi

1. [[#1. Mengapa Software Engineering Berbeda dari Sekedar Coding ]]
2. [[#2. Apa Itu Software?]]
3. [[#3. Definisi dan Tujuan Software Engineering]]
4. [[#4. Mengapa RPL Krusial di Era Modern]]
5. [[#5. Masalah Klasik dalam Proyek Software]]
6. [[#6. Coding vs Software Engineering — Perbedaan Mindset]]
7. [[#7. Software Development Life Cycle (SDLC)]]
8. [[#8. Artefak Utama dalam SDLC]]
9. [[#9. Quality Baseline — Standar Minimum Produk]]
10. [[#10. Kontrak Kuliah — Struktur, Penilaian, dan Aturan]]
11. [[#11. Team Based Project (SDLC) — Milestone & Workflow]]
12. [[#12. Responsible AI-Assisted Development]]
13. [[#Summary — Key Concepts at a Glance]]
14. [[#Active Recall Questions]]

---

## 1. Mengapa Software Engineering Berbeda dari Sekedar Coding

Sebelum masuk ke definisi formal, penting untuk memahami *mengapa* mata kuliah ini ada dan apa yang membedakannya dari sekadar belajar menulis kode.

Ada sebuah fakta industri yang sering mengejutkan orang-orang di luar bidang ini: sebagian besar anggaran proyek IT tidak dihabiskan untuk *membangun* aplikasi baru. Justru proporsi terbesar uang tersedot untuk biaya **maintenance** — perbaikan, pemeliharaan, dan pembaruan setelah aplikasi selesai dirilis. Ini bukan kebetulan. Ini adalah konsekuensi langsung dari pembangunan software yang dilakukan tanpa pendekatan rekayasa yang disiplin sejak awal.

Fenomena ini mengajarkan satu pelajaran penting: **keputusan yang dibuat di awal pengembangan — seperti bagaimana requirements didefinisikan, bagaimana arsitektur dirancang, dan apakah ada dokumentasi yang memadai — akan menentukan seberapa mahal dan seberapa sulit software tersebut untuk dirawat di masa depan.** Software yang dibangun secara asal-asalan ("yang penting jalan dulu") akan terus menghasilkan masalah baru yang semakin mahal untuk diperbaiki seiring waktu.

Inilah alasan RPL (Rekayasa Perangkat Lunak) ada sebagai disiplin ilmu tersendiri: bukan untuk mengajarkan cara menulis kode, melainkan cara membangun sistem perangkat lunak yang **andal, terukur, dan berkelanjutan**.

Analogi yang diberikan dosen cukup kuat untuk dipahami:
- **Coding = Menyusun Batu Bata.** Ini adalah keterampilan dasar — siapapun bisa belajar menulis kode dalam hitungan minggu. Yang dilakukan adalah menyusun instruksi satu demi satu agar komputer menjalankan perintah tertentu.
- **Software Engineering = Merancang Jembatan.** Rekayasa ibarat merancang struktur jembatan yang harus tahan gempa selama 50 tahun. Ini membutuhkan ilmu yang mendalam, perhitungan yang cermat, standar keamanan yang ketat, dan disiplin proses yang konsisten. Seorang insinyur jembatan tidak hanya meletakkan batu satu per satu — dia merancang keseluruhan sistem, memastikan setiap komponen bekerja bersama, dan mempertimbangkan skenario kegagalan sebelum konstruksi bahkan dimulai.

---

## 2. Apa Itu Software?

Banyak orang secara intuitif menyamakan "software" dengan "kode program". Namun definisi klasik di bidang ini menegaskan bahwa software adalah entitas yang jauh lebih komprehensif. Software terdiri dari **tiga elemen tak terpisahkan**:

**Instruksi (Program)**
Ini adalah bagian yang paling familiar — sekumpulan logika terstruktur yang ketika dieksekusi akan menghasilkan fungsi dan kinerja sesuai kebutuhan pengguna. Ini adalah kode itu sendiri: algoritma, fungsi, dan alur kontrol yang menentukan apa yang dilakukan sistem.

**Struktur Data**
Program tidak bisa bekerja sendiri tanpa tempat untuk menyimpan dan memanipulasi informasi. Struktur data adalah mekanisme yang memungkinkan program mengolah data secara efisien dan akurat — mulai dari array dan linked list sederhana hingga database relasional yang kompleks. Tanpa struktur data yang dirancang dengan baik, program yang logikanya benar sekalipun bisa menjadi sangat lambat atau tidak bisa menangani data dalam skala besar.

**Dokumentasi**
Ini adalah elemen yang paling sering diabaikan oleh developer pemula, namun justru menjadi salah satu yang paling krusial dalam konteks tim dan jangka panjang. Dokumentasi mencakup manual panduan, diagram desain, komentar kode, dan semua artefak deskriptif lain yang menjelaskan operasi dan penggunaan sistem. Tanpa dokumentasi, pengetahuan tentang bagaimana sebuah sistem bekerja hanya ada di kepala orang yang membuatnya — dan ketika orang itu pergi, pengetahuan itu ikut hilang.

Ketiga elemen ini adalah satu kesatuan. Software yang hanya punya kode tanpa dokumentasi adalah software yang tidak bisa di-maintain. Software yang punya dokumentasi tapi struktur datanya buruk adalah software yang tidak bisa di-scale. Sebuah produk software yang baik harus memiliki ketiga elemen ini secara proporsional.

---

## 3. Definisi dan Tujuan Software Engineering

IEEE (Institute of Electrical and Electronics Engineers), salah satu badan standar paling berpengaruh di dunia teknologi, mendefinisikan Software Engineering melalui IEEE Standard 610.12 sebagai:

> *"The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software."*

Ada tiga kata kunci yang perlu dipahami secara mendalam dalam definisi ini:

- **Systematic (Sistematis):** Ada metodologi yang jelas dan terstruktur yang diikuti. Pengembangan tidak dilakukan secara acak berdasarkan intuisi semata, melainkan mengikuti proses yang telah terdefinisi — misalnya, requirements selalu dikumpulkan sebelum desain dimulai, dan testing dilakukan sebelum deployment.

- **Disciplined (Disiplin):** Metodologi tersebut diikuti secara konsisten, bahkan ketika ada tekanan deadline atau godaan untuk mengambil jalan pintas. Disiplin inilah yang membedakan software engineer profesional dari hobbyist. Seorang profesional tahu bahwa melompati langkah-langkah penting demi kecepatan jangka pendek hampir selalu menghasilkan masalah yang lebih besar di kemudian hari.

- **Quantifiable (Terukur):** Kemajuan dan kualitas dapat dievaluasi secara kuantitatif. Ini berarti ada metrik yang jelas: berapa banyak requirements yang sudah selesai diimplementasi? Berapa persentase kode yang sudah di-test? Berapa banyak bug yang ditemukan? Tanpa ukuran yang jelas, tidak mungkin mengetahui apakah proyek berjalan sesuai rencana.

**Tiga tujuan utama RPL** yang dijabarkan dari definisi ini adalah:
- **Kualitas Tinggi:** Produk yang dihasilkan minim bug dan benar-benar memenuhi kebutuhan pengguna — bukan hanya berjalan secara teknis, tapi sesuai dengan ekspektasi orang yang menggunakannya.
- **Tepat Waktu:** Delivery sesuai jadwal yang telah disepakati. Ini penting karena dalam konteks bisnis, keterlambatan produk bisa berarti kehilangan momentum pasar atau melanggar kontrak.
- **Sesuai Anggaran:** Biaya pengembangan tidak melebihi estimasi awal. Overrun anggaran adalah salah satu penyebab utama kegagalan proyek IT.

---

## 4. Mengapa RPL Krusial di Era Modern

Ekonomi dunia modern bergantung sepenuhnya pada software. Hampir setiap aspek kehidupan kita dikendalikan oleh perangkat lunak — sering kali tanpa kita sadari secara eksplisit. Beberapa contoh konkret yang diberikan:

**Transaksi Keuangan:** Setiap kali seseorang melakukan transfer via M-Banking atau membayar menggunakan e-wallet, triliunan rupiah diproses setiap harinya melalui algoritma-algoritma terenkripsi yang berjalan di latar belakang. Jika software ini gagal atau mengandung bug dalam kalkulasi keuangan, dampaknya bisa berupa kerugian finansial massal.

**Navigasi Penerbangan:** Sistem autopilot pesawat komersial mengandalkan jutaan baris kode untuk menjaga keselamatan penumpang di udara. Software dalam avionik harus memenuhi standar keandalan yang sangat tinggi karena kegagalan di sini berarti nyawa manusia.

**Keselamatan Berkendara:** Sistem pengereman ABS (Anti-lock Braking System) dan stability control di kendaraan modern digerakkan oleh embedded software. Sistem ini harus merespons dengan tepat dalam milidetik — ada tidak ada toleransi untuk bug.

Poin utamanya adalah: **jika software gagal, dampaknya bisa berupa kerugian finansial massal, kerusakan infrastruktur, atau bahkan hilangnya nyawa manusia.** Ini bukan hiperbola — ada banyak kasus nyata di mana bug software telah menyebabkan bencana berskala besar. Oleh karena itu, Software Engineering sebagai disiplin ilmu yang menekankan keandalan dan kualitas bukan sekadar akademis — ini adalah kebutuhan yang sangat nyata di industri.

---

## 5. Masalah Klasik dalam Proyek Software

Salah satu hal paling penting yang dibahas di pertemuan pertama ini adalah pengenalan terhadap **masalah-masalah yang paling sering membunuh proyek software**. Memahami ini sejak awal membantu kita mengerti mengapa setiap praktik dalam Software Engineering ada.

**Scope Creep**
Ini adalah kondisi di mana fitur terus bertambah tanpa kontrol yang memadai. Skenario umumnya: klien awalnya meminta fitur A, B, dan C. Tapi di tengah pengembangan, mereka bilang "oh, kalau bisa tambahkan juga fitur D". Lalu "kalau ada waktu, fitur E juga bagus". Tanpa mekanisme kontrol scope yang ketat, proyek menjadi membengkak, deadline terlewat, dan tim kewalahan. Solusinya adalah proses requirements yang jelas dan formal, serta Change Management yang disiplin.

**Salah Requirement**
Ini mungkin adalah masalah yang paling mahal: tim membangun fitur yang *teknis berjalan dengan sempurna*, tapi ternyata bukan itu yang dibutuhkan pengguna. Waktu dan effort berbulan-bulan terbuang sia-sia karena requirements tidak dikumpulkan dengan benar di awal. Ini menggarisbawahi betapa pentingnya fase requirements dalam SDLC — memahami *apa* yang harus dibangun sebelum mulai *bagaimana* membangunnya.

**Bug & Regression**
Ini adalah situasi di mana perbaikan satu bug justru memunculkan bug baru di tempat lain — biasanya karena tidak ada automated testing yang terstruktur. Tanpa test suite yang komprehensif, setiap perubahan kode adalah perubahan yang "blind" — developer tidak bisa tahu dengan yakin apakah perubahannya merusak sesuatu yang lain.

**Dokumentasi Nol**
Ketika tidak ada dokumentasi yang memadai, tidak ada yang benar-benar tahu bagaimana sistem bekerja kecuali orang yang menulisnya. Ini membuat handover (perpindahan kepemilikan sistem ke orang lain) menjadi hampir mustahil, dan maintenance menjadi mimpi buruk. Setiap bug fix atau feature tambahan butuh waktu lama hanya untuk memahami kode yang sudah ada.

Keempat masalah ini relevan tidak hanya di industri, tapi juga di konteks perkuliahan — hampir semua tugas kelompok yang kacau bisa ditelusuri ke salah satu (atau beberapa) dari masalah di atas.

---

## 6. Coding vs Software Engineering — Perbedaan Mindset

Perbedaan ini bukan sekadar soal skala, tapi soal **mindset dan cakupan tanggung jawab** yang fundamental berbeda.

| Aspek | Coding | Software Engineering |
|---|---|---|
| Fokus | Solusi teknis untuk satu masalah spesifik | Membangun produk yang dipakai banyak orang |
| Alur kerja | Input → Proses → Output | Requirements → Design → Build → Test → Deploy |
| Konteks tim | Biasanya individual | Tim multidisiplin |
| Definisi "selesai" | Saat *"it works"* | Saat *"kebutuhan user terpenuhi"* |
| Penekanan | Kode yang berjalan | Kualitas, proses, tim, dan dokumentasi |

Poin paling kritis dari tabel ini adalah definisi "selesai". Seorang coder menganggap tugasnya selesai ketika kode berjalan tanpa error. Seorang software engineer tahu bahwa kode yang berjalan hanyalah syarat perlu, bukan syarat cukup. Produk belum selesai sampai: kebutuhan user terpenuhi, sistem stabil dalam kondisi produksi, dan kode bisa di-maintain oleh orang lain.

Ini adalah **pergeseran perspektif yang paling penting** yang diharapkan terjadi pada mahasiswa setelah mengambil mata kuliah ini.

---

## 7. Software Development Life Cycle (SDLC)

SDLC adalah kerangka kerja yang mendefinisikan tahapan-tahapan dalam pengembangan software. Secara high-level, siklus ini terdiri dari fase-fase berikut yang saling berurutan dan — paling penting — **bersifat iteratif**:

```
Requirements → Design → Implement → Test → Release → Improve → (kembali ke Requirements)
```

Kata **iteratif** di sini krusial: artinya proses ini bukan waterfall satu arah yang kaku. Setelah release, tim belajar dari feedback pengguna, menemukan hal-hal yang perlu diperbaiki atau ditingkatkan, dan siklus dimulai kembali. Inilah mengapa software bisa terus berkembang dan diperbaiki dari versi ke versi.

Setiap fase memiliki tujuan yang spesifik:
- **Requirements:** Memahami *apa* yang harus dibangun dan *untuk siapa*. Ini adalah fase paling kritis karena kesalahan di sini adalah yang paling mahal untuk diperbaiki kemudian.
- **Design:** Merencanakan *bagaimana* sistem akan dibangun — arsitektur, database, antarmuka pengguna.
- **Implement:** Menulis kode berdasarkan desain yang sudah dibuat.
- **Test:** Memverifikasi bahwa implementasi sudah benar dan sesuai requirements.
- **Release:** Merilis produk ke pengguna nyata.
- **Improve:** Belajar dari feedback pengguna dan merencanakan iterasi berikutnya.

Dalam konteks proyek software, setiap milestone dipetakan ke fase tertentu dalam siklus ini — sehingga proyek tidak hanya menjadi tugas akhir, tapi menjadi simulasi nyata dari proses pengembangan software profesional.

---

## 8. Artefak Utama dalam SDLC

Setiap fase SDLC menghasilkan **artefak** — dokumen atau deliverable konkret yang membuktikan bahwa sebuah fase benar-benar dikerjakan dengan berpikir, bukan sekadar dilompati. Artefak bukan formalitas; masing-masing punya fungsi praktis yang nyata.

**01 — SRS Ringkas (Software Requirements Specification)**
SRS adalah dokumen yang mendefinisikan *apa* yang akan dibangun dan *untuk siapa*. Ini menjadi "kontrak" antara tim developer dengan pemangku kepentingan (stakeholders). Tanpa SRS yang jelas, semua orang di tim bisa memiliki pemahaman yang berbeda tentang apa yang sedang dibangun, yang berujung pada Scope Creep atau Salah Requirement.

**02 — UML-lite + ERD**
UML (Unified Modeling Language) adalah bahasa visual standar untuk menggambarkan desain sistem software. Dalam banyak proyek MVP, yang dibutuhkan adalah "UML-lite" — versi yang disederhanakan mencakup use case diagram (menggambarkan siapa melakukan apa), class diagram dasar (menggambarkan struktur objek), dan ERD (Entity Relationship Diagram) untuk menggambarkan skema database. Diagram-diagram ini membantu tim menyepakati desain sebelum coding dimulai, sehingga mengurangi rework.

**03 — Repo + Fitur Inti**
Ini adalah implementasi aktual — repository GitHub berisi kode yang berjalan end-to-end untuk fitur-fitur utama. "End-to-end" berarti fitur berfungsi lengkap dari sisi pengguna hingga database, bukan hanya tampilan frontend saja.

**04 — Test Case + Unit Test**
Test case manual adalah dokumen yang mendeskripsikan skenario testing untuk alur-alur utama aplikasi. Unit test adalah kode otomatis yang memverifikasi bahwa komponen-komponen kritis berfungsi dengan benar secara terisolasi. Keduanya bersama-sama memberikan jaring pengaman yang memungkinkan tim melakukan perubahan kode dengan lebih percaya diri.

**05 — README + Demo Script**
README adalah dokumentasi cara menjalankan aplikasi — *setup guide* yang memungkinkan siapapun bisa menjalankan proyek dari awal tanpa harus bertanya kepada pembuat. Demo Script adalah skenario terstruktur untuk presentasi akhir, memastikan demo berjalan lancar dan semua fitur penting diperlihatkan.

---

## 9. Quality Baseline — Standar Minimum Produk

Tim tidak perlu membuat software yang sempurna — tapi ada standar minimum yang harus dipenuhi agar produk dianggap layak dinilai. Ini disebut **quality baseline**:

**Validasi Input:** Semua form harus memvalidasi input pengguna. Jangan biarkan data kosong, format yang salah, atau input yang tidak sesuai masuk ke dalam sistem. Ini bukan hanya soal keamanan, tapi juga soal integritas data — data yang buruk di database akan menyebabkan masalah yang jauh lebih sulit untuk diperbaiki.

**Error Handling Dasar:** Ketika sesuatu berjalan salah, aplikasi harus menampilkan pesan error yang informatif dan ramah pengguna. Jangan biarkan pengguna melihat stack trace Python yang panjang atau blank page kosong. Error yang baik memberitahu pengguna apa yang salah dan — jika memungkinkan — apa yang bisa dilakukan.

**Struktur Kode yang Rapi:** Folder harus terorganisir secara logis, penamaan file dan variabel harus konsisten mengikuti konvensi yang disepakati tim, dan kode harus bisa dibaca oleh anggota tim lain tanpa harus bertanya kepada pembuatnya. Kode adalah komunikasi — tidak hanya dengan komputer, tapi dengan programmer lain (termasuk diri sendiri di masa depan).

**Minimal Testing:** Setidaknya ada test case manual untuk alur utama aplikasi, dan beberapa unit test untuk logika bisnis yang penting. Ini adalah standar minimum — bukan standard profesional penuh, tapi cukup untuk membuktikan bahwa testing tidak diabaikan sama sekali.

Prinsip yang ditekankan: **lebih baik fitur sedikit tapi berkualitas, daripada banyak fitur tapi rapuh.** Sebuah aplikasi dengan tiga fitur yang benar-benar bekerja dengan baik jauh lebih bernilai daripada aplikasi dengan sepuluh fitur yang setengah jadi dan penuh bug.

---

## Summary — Key Concepts at a Glance

| Konsep | Definisi / Penjelasan Singkat |
|---|---|
| Software Engineering | Penerapan pendekatan yang sistematis, disiplin, dan terukur dalam pengembangan, operasi, dan pemeliharaan software (IEEE 610.12) |
| Software | Entitas komprehensif yang terdiri dari tiga elemen: Instructions (Program), Data Structures, dan Documentation |
| SDLC | Software Development Life Cycle — siklus iteratif: Requirements → Design → Implement → Test → Release → Improve |
| Artefak | Deliverable konkret dari setiap fase SDLC (SRS, UML, ERD, Test Case, README) yang membuktikan proses berpikir terstruktur |
| Scope Creep | Penambahan fitur tanpa kontrol yang menyebabkan proyek membengkak dan deadline terlewat |
| Quality Baseline | Standar minimum kualitas: validasi input, error handling, struktur rapi, minimal testing |
| SDLC | Team Based Project — proyek kelompok dengan 5 milestone dan 12 sesi praktikum yang mensimulasikan proses SE nyata |
| AI-Usage Log | Catatan wajib penggunaan AI: tanggal, tools, prompt, output, dan cara verifikasi |

---

## Active Recall Questions

> [!question]- 1. Mengapa sebagian besar biaya proyek IT dihabiskan untuk *maintenance*, bukan pembangunan fitur baru? Dan apa hubungannya dengan pentingnya Software Engineering?
> Biaya maintenance yang tinggi adalah akibat langsung dari pembangunan software tanpa pendekatan rekayasa yang disiplin. Ketika requirements tidak jelas dari awal, sistem dibangun tanpa dokumentasi, dan tidak ada testing terstruktur, setiap perubahan kecil di kemudian hari bisa menyebabkan efek domino yang mahal. Software Engineering hadir sebagai solusi: dengan proses yang sistematis (SDLC), artefak yang terstruktur (SRS, UML, test case), dan standar kualitas yang jelas, biaya perbaikan di kemudian hari dapat ditekan secara signifikan.

> [!question]- 2. Seseorang berargumen: "Saya sudah bisa membuat aplikasi yang berjalan tanpa error. Berarti saya sudah melakukan Software Engineering." Apa yang salah dari argumen ini, dan bagaimana kamu akan meresponsnya?
> Argumen ini keliru karena menyamakan "kode yang berjalan" dengan "software yang baik". Software Engineering bukan tentang membuat kode yang berjalan — itu hanyalah kondisi minimum (necessary condition), bukan kondisi cukup (sufficient condition). Software Engineering berarti memastikan: (1) yang dibangun benar-benar sesuai kebutuhan pengguna, bukan hanya asumsi developer; (2) sistem bisa di-maintain oleh orang lain, bukan hanya pembuatnya; (3) ada proses yang terstruktur dari requirements hingga deployment; (4) ada dokumentasi yang memadai; dan (5) ada testing yang bisa membuktikan sistem bekerja dengan benar. Kode yang berjalan tanpa salah satu dari poin-poin ini adalah "coding", bukan "engineering".

> [!question]- 3. Dari empat masalah klasik proyek software (Scope Creep, Salah Requirement, Bug & Regression, Dokumentasi Nol), artefak-artefak apa dalam SDLC yang secara spesifik dirancang untuk mencegah masing-masing masalah tersebut?
> — **Scope Creep** dicegah oleh **SRS (Software Requirements Specification)** yang mendefinisikan dengan jelas apa yang akan dibangun dan apa yang *tidak* akan dibangun, serta proses formal untuk mengelola perubahan. — **Salah Requirement** dicegah oleh proses requirements gathering yang terstruktur, termasuk pembuatan use case diagram yang memastikan semua stakeholder memiliki pemahaman yang sama. — **Bug & Regression** dicegah oleh **Test Case dan Unit Test** — terutama automated testing yang memungkinkan tim mengetahui dengan cepat jika sebuah perubahan merusak fungsionalitas yang sudah ada sebelumnya. — **Dokumentasi Nol** dicegah oleh **README, Demo Script, komentar kode**, dan semua artefak dokumentasi lain yang memastikan pengetahuan tentang sistem tersimpan di luar kepala satu orang.

> [!question]- 4. Dalam konteks SDLC, mengapa aturan *"jangan push langsung ke main"* dan penggunaan Pull Request penting, bahkan untuk tim kecil beranggota 3-4 orang?
> Meskipun terasa berlebihan untuk tim kecil, aturan ini melatih dua hal penting. Pertama, **peer review** — ketika satu orang mengerjakan fitur dan orang lain mereview sebelum merge, ada potensi untuk menangkap bug atau desain yang buruk lebih awal, sebelum masalah tersebut ter-integrasi ke codebase utama. Kedua, **rekam jejak yang bersih** — riwayat commit dan PR yang terstruktur memudahkan proses debugging ("kapan bug ini masuk?"), demonstrasi kepada dosen tentang siapa berkontribusi apa, dan handover jika ada anggota tim yang perlu digantikan. Di industri, ini adalah standar non-negotiable — melatihnya sejak kuliah membangun muscle memory yang sangat berharga.

---

## Sumber

- Berasal dari: [[Course Overview - SE - 1]]
- Slides: Pertemuan 1 — Overview SE & Kontrak Kuliah, Haryono Setiadi, Rekayasa Perangkat Lunak, Universitas Sebelas Maret
- Referensi tambahan: IEEE Standard 610.12 — Standard Glossary of Software Engineering Terminology
- Referensi buku: Pressman, R.S. — *Software Engineering: A Practitioner's Approach* (classic reference untuk definisi dan konsep dasar SE)
