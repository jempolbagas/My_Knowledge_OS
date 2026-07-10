---
title: "(CN-14) Keamanan Jaringan Lecture Notes"
course: ""
tags: []
aliases: ["(CN-14) Keamanan Jaringan Lecture Notes"]
created: "2026-06-24"
---
# Materi: Keamanan Jaringan

**Mata Kuliah:** Jaringan Komputer Genap 2025/2026  
**Program Studi:** Informatika UNS  
**Dosen:** Herdito Ibnu Dewangkoro  

---

## 1. Security Threats and Vulnerabilities (Ancaman dan Kerentanan Keamanan)

### Jenis-jenis Threat (Ancaman)
Serangan pada jaringan (network attack) dapat bersifat merusak dan mengakibatkan kerugian waktu serta uang, seringkali karena kerusakan atau pencurian informasi/aset penting. 

Penyusup (intruder) yang memperoleh akses ke jaringan dengan memodifikasi atau mengeksploitasi kerentanan perangkat lunak disebut sebagai **threat actor**. Akses ini bisa didapat melalui kerentanan perangkat lunak (software vulnerabilities), serangan perangkat keras (hardware attack), atau dengan menebak *username* dan *password* pengguna.

Setelah *threat actor* memperoleh akses ke jaringan, terdapat 4 jenis ancaman yang dapat terjadi:
1. **Pencurian informasi (information theft)**
2. **Kehilangan data dan manipulasi data (data loss and manipulation)**
3. **Pencurian identitas (identity theft)**
4. **Gangguan layanan (disruption of service)**

### Jenis-jenis Vulnerability (Kerentanan)
Vulnerability atau kerentanan adalah tingkat kelemahan (weakness) dalam suatu jaringan atau perangkat. Terdapat 3 jenis kerentanan utama:
1. **Kerentanan teknologi (technological vulnerabilities):** Kelemahan pada protokol TCP/IP, sistem operasi, dan peralatan jaringan.
2. **Kerentanan konfigurasi (configuration vulnerabilities):** Akun pengguna yang tidak aman, kata sandi sistem yang mudah ditebak, layanan internet yang salah konfigurasi, pengaturan bawaan (default settings) yang tidak aman, dan peralatan jaringan yang salah konfigurasi.
3. **Kerentanan kebijakan keamanan (security policy vulnerabilities):** Kurangnya kebijakan keamanan tertulis, faktor politik, instalasi/perubahan perangkat yang tidak sesuai SOP, dan tidak adanya perencanaan pemulihan bencana (*disaster recovery*).

### Physical Security (Keamanan Fisik)
Selain ancaman siber, terdapat ancaman yang berkaitan dengan keamanan fisik (physical threat), antara lain:
1. **Ancaman perangkat keras (hardware threat):** Kerusakan fisik pada server, router, switch, instalasi kabel, dan workstation.
2. **Ancaman lingkungan (environmental threat):** Suhu ekstrem (terlalu panas/dingin) atau kelembaban ekstrem.
3. **Ancaman listrik (electrical threat):** Lonjakan tegangan, tegangan yang tidak mencukupi, daya yang tidak terkondisi, dan kehilangan daya total.
4. **Ancaman pemeliharaan (maintenance threat):** Penanganan komponen listrik yang buruk, kurangnya suku cadang penting, dan pengkabelan yang tidak rapi/baik.

---

## 2. Network Attack (Serangan Jaringan)

### Malicious Software (Malware)
Malware adalah kode atau perangkat lunak yang dirancang secara khusus untuk merusak, mengganggu, mencuri, atau melakukan tindakan tidak sah pada data, host, atau jaringan. Malware dapat menyebar melalui jaringan.

Jenis-jenis malware meliputi:
*   **Viruses:** Menyebar dengan menyisipkan salinan dirinya ke dalam program lain. Menyebar dari satu komputer ke komputer lain dan meninggalkan infeksi di sepanjang perjalanannya.
*   **Worms:** Mirip dengan virus karena dapat mereplikasi diri dan menyebabkan kerusakan. Namun, *worm* adalah perangkat lunak mandiri (standalone) yang tidak memerlukan file host atau bantuan manusia untuk menyebar.
*   **Trojan Horses:** Perangkat lunak berbahaya yang terlihat sah (legitimate). Trojan tidak mereproduksi dengan menginfeksi file lain, melainkan harus menyebar melalui interaksi pengguna, seperti membuka lampiran email atau mengunduh file dari internet.

### Kategori-kategori Network Attack
Selain malware, serangan jaringan dikategorikan menjadi tiga:
1. **Reconnaissance attack:** Melibatkan pengidentifikasian dan pemetaan sistem, layanan (service), atau kerentanan.
2. **Access attack:** Memanipulasi data, akses sistem, atau hak istimewa pengguna secara tidak sah. Serangan ini mengeksploitasi kerentanan pada layanan autentikasi, FTP, dan web untuk mendapatkan akses ke akun, database rahasia, dan informasi sensitif.
3. **Denial of service (DoS):** Bertujuan menonaktifkan atau merusak jaringan, sistem, atau layanan agar tidak dapat digunakan oleh pengguna yang sah.

---

## 3. Mitigasi Network Attack

Untuk melindungi jaringan dari berbagai ancaman dan serangan, beberapa langkah mitigasi dapat dilakukan:

### 1. Melakukan Backup
*   Mencadangkan (backup) konfigurasi dan data perangkat adalah cara paling efektif untuk melindungi dari kehilangan data.
*   Harus dilakukan secara berkala sesuai dengan Standard Operating Procedure (SOP) keamanan.
*   Data backup sebaiknya disimpan di luar lokasi (offsite) untuk melindungi media backup jika terjadi bencana pada fasilitas utama.

### 2. Melakukan Upgrade, Update, dan Patch
*   Terus memperbarui versi perangkat lunak antivirus.
*   Mengunduh *security update* dari vendor sistem operasi dan mengunduh *patch* untuk menambal sistem yang rentan.
*   Jika sistem operasi sudah mencapai *End of Support* (misalnya Windows 10 pada Oktober 2025), pengguna harus melakukan *upgrade* ke sistem operasi yang lebih baru dan didukung.

### 3. Menerapkan Authentication, Authorization, dan Accounting (AAA)
Layanan keamanan jaringan AAA menyediakan *framework* untuk menyiapkan kontrol akses (access control) pada perangkat jaringan. Konsep AAA dapat dianalogikan seperti penggunaan kartu kredit:
*   **Authentication (Siapa Anda?):** Mengontrol dan memverifikasi siapa saja yang diizinkan untuk mengakses jaringan.
*   **Authorization (Apa yang bisa Anda lakukan/habiskan?):** Menentukan tindakan apa saja yang dapat dilakukan pengguna saat mengakses jaringan.
*   **Accounting (Apa yang sudah Anda lakukan/belanjakan?):** Membuat catatan tentang apa saja yang dilakukan pengguna selama berada di dalam jaringan.

### 4. Firewall
*   Berada di antara dua jaringan atau lebih untuk mengendalikan lalu lintas (traffic) dan mencegah akses yang tidak sah.
*   **Aturan Dasar Firewall:**
    *   Mengizinkan *traffic* dari pengguna di jaringan internal (inside network) untuk keluar menuju internet dan kembali.
    *   Menolak *traffic* yang diinisiasi dari jaringan luar (internet) yang mencoba masuk ke jaringan internal secara tidak sah.
