---
title: "[CN] Assignment 1 - Model OSI Layer"
course: Computer Networks
tags: ["computer-networks", "networking", "osi-model", "layered-architecture", "assignment"]
aliases: ["[CN] Assignment 1 - Model OSI Layer"]
created: "2026-03-26"
type: Assignment
topic: Network Architecture
semester: 4
---
# Model OSI Layer

## Daftar Isi
1. [[#Pengertian Model OSI]]
2. [[#Kenapa Model OSI Penting?]]
3. [[#Pengelompokan Layer]]
4. [[#Penjelasan 7 Layer OSI]]
	1. [[#Layer 1 — Physical Layer]]
	2. [[#Layer 2 — Data Link Layer]]
	3. [[#Layer 3 — Network Layer]]
	4. [[#Layer 4 — Transport Layer]]
	5. [[#Layer 5 — Session Layer]]
	6. [[#Layer 6 — Presentation Layer]]
	7. [[#Layer 7 — Application Layer]]
5. [[#Contoh Alur Komunikasi Mengirim Email]]
6. [[#Model OSI vs TCP/IP]]
7. [[#Kesimpulan]]
8. [[#Daftar Pustaka]]

## Pengertian Model OSI

Model OSI (*Open Systems Interconnection*) itu pada dasarnya adalah sebuah kerangka konseptual yang dipakai untuk menjelaskan bagaimana komunikasi data terjadi di dalam jaringan komputer. Model ini membagi proses komunikasi jaringan jadi **7 lapisan** (layer), dimana tiap layer memiliki tugas dan tanggung jawab masing-masing.

Model ini pertama kali dikembangkan oleh ISO (*International Organization for Standardization*) dan mulai diperkenalkan tahun 1983 oleh para perwakilan perusahaan komputer dan telekomunikasi besar. Setahun kemudian, tahun 1984, model ini resmi diadopsi sebagai standar internasional (Imperva, n.d.). Latar belakang dibuatnya model ini adalah karena di akhir tahun 1970-an, banyak produsen yang membuat solusi jaringan masing-masing  alias *proprietary*, sehingga sistem-sistem tersebut tidak bisa saling berkomunikasi satu sama lain (Raza, n.d.).

Perlu dicatat bahwa internet modern sebenarnya tidak berbasis langsung pada model OSI, melainkan pada model TCP/IP yang lebih sederhana. Tapi model OSI tetap banyak digunakan karena sangat membantu untuk memvisualisasikan dan memahami bagaimana jaringan itu bekerja (Imperva, n.d.).

## Kenapa Model OSI Penting?

Ada beberapa alasan kenapa model OSI ini masih relevan dan penting untuk dipelajari:

- **Mempermudah troubleshooting** — Dengan adanya pembagian 7 layer, kita bisa lebih mudah mengidentifikasi di layer mana tepatnya sebuah masalah jaringan terjadi. Misalnya, kalau masalahnya ada di kabel, berarti itu masalah Physical Layer. Kalau masalahnya ada di routing, berarti itu masalah Network Layer (Fortinet, n.d.).
- **Standarisasi komunikasi** — Model ini jadi semacam "bahasa universal" di dunia networking. Jadi, ketika seorang network engineer berkata *"ada masalah di Layer 3"*, semua orang langsung paham yang dimaksud itu Network Layer (Raza, n.d.).
- **Pengembangan modular** — Developer bisa fokus mengembangkan teknologi di satu layer tanpa perlu mengubah layer lainnya. Misalnya, developer aplikasi tidak perlu paham detail transmisi fisik di layer bawah (Raza, n.d.).
- **Keamanan** — Model ini juga berguna untuk strategi keamanan jaringan. Serangan di tiap layer itu berbeda-beda, sehingga penanganannya juga harus disesuaikan. Contohnya, serangan DDoS bisa terjadi di layer 3/4 (menghabiskan bandwidth) atau di layer 7 (membanjiri aplikasi dengan request) (Check Point, n.d.).

## Pengelompokan Layer

Menurut Raza (n.d.), ketujuh layer OSI ini bisa dikelompokkan jadi 3 kategori besar:

1. **Software Layers** (Layer 5, 6, 7) — Layer Application, Presentation, dan Session yang menangani hal-hal di tingkat software.
2. **Heart of OSI / Transport** (Layer 4) — Layer Transport yang jadi jembatan antara software layers dan hardware layers.
3. **Hardware Layers** (Layer 1, 2, 3) — Layer Physical, Data Link, dan Network yang berurusan dengan transmisi data secara fisik.

Data bergerak dua arah melalui layer-layer ini. Tiap layer berkomunikasi dengan layer di atas dan bawahnya.

## Penjelasan 7 Layer OSI

### Layer 1 — Physical Layer

Physical Layer adalah layer paling bawah yang berurusan langsung dengan perangkat keras dan media transmisi fisik. Di layer ini, data dikirim dan diterima dalam bentuk sinyal mentah berupa bit — bisa berupa sinyal listrik, cahaya, atau gelombang radio (Imperva, n.d.).

Beberapa hal yang ditangani di layer ini antara lain:
- Konversi data menjadi bit dan sebaliknya
- Pengaturan kecepatan transmisi (*bit rate*)
- Sinkronisasi antara pengirim dan penerima
- Penentuan mode transmisi: simplex (satu arah saja), half-duplex (dua arah tapi bergantian), atau full-duplex (dua arah bersamaan) (Raza, n.d.)
- Topologi jaringan (bus, star, ring, mesh)

Contoh komponen yang termasuk di Physical Layer ini adalah kabel (twisted pair, coaxial, fiber optic), hub, repeater, NIC (Network Interface Card), dan juga frekuensi radio untuk wireless (Raza, n.d.). Teknologi seperti Wi-Fi (IEEE 802.11) dan berbagai standar Ethernet juga beroperasi di layer ini.

Biasanya jika ada masalah konektivitas, hal pertama yang diperiksa adalah Physical Layer — apakah kabelnya rusak, apakah lampu indikator menyala, apakah ada daya, dan lain-lain (Raza, n.d.).

### Layer 2 — Data Link Layer

Naik satu tingkat, Data Link Layer ini bertanggung jawab untuk transfer data antar perangkat yang terhubung dalam **jaringan lokal (LAN)** yang sama. Sinyal listrik yang diterima dari Physical Layer diterjemahkan jadi logika digital di layer ini (Codecademy, n.d.).

PDU (*Protocol Data Unit*) di layer ini disebut **frame**, yang terdiri dari header, data, dan footer.

Data Link Layer punya dua sublayer penting:
1. **LLC (Logical Link Control)** — Bertugas membangun koneksi logis antar perangkat dan menangani flow control serta error control.
2. **MAC (Media Access Control)** — Mengontrol bagaimana perangkat mengakses media jaringan. Di sinilah **MAC address** digunakan, yaitu alamat unik 48-bit dalam format hexadecimal yang dimiliki tiap perangkat di jaringan lokal (Codecademy, n.d.).

Beberapa fungsi penting lainnya:
- **Framing** — Mengemas paket data dengan header dan trailer berisi MAC address serta kode pengecekan error
- **Error detection** — Menggunakan *Cyclic Redundancy Check* (CRC) buat mendeteksi frame yang rusak (Raza, n.d.)
- **Access control** — Mengatur perangkat mana yang boleh mengirim data. Untuk Ethernet digunakan CSMA/CD, sedangkan untuk Wi-Fi digunakan CSMA/CA (Raza, n.d.)

Protokol yang beroperasi di layer ini antara lain Ethernet, IEEE 802.11 (Wi-Fi), ARP (*Address Resolution Protocol*), PPP (*Point-to-Point Protocol*), dan HDLC (Codecademy, n.d.; Raza, n.d.).

### Layer 3 — Network Layer

Kalau Data Link Layer menghubungkan perangkat dalam satu jaringan yang sama, maka Network Layer inilah yang menghubungkan **antar jaringan** yang berbeda. Istilahnya, di sinilah terjadi *internetworking* (Codecademy, n.d.).

PDU di layer ini disebut **packet**. Tugas utama Network Layer adalah **routing** — mencari jalur terbaik supaya paket data bisa sampai ke tujuan. Layer ini menggunakan **alamat IP** sebagai identitas logis perangkat di jaringan (Fortinet, n.d.).

Fungsi-fungsi penting Network Layer:
- **Logical addressing** — Menggunakan alamat IP. IPv4 pakai format 32-bit, sementara IPv6 pakai 128-bit (Raza, n.d.)
- **Routing** — Menentukan jalur paling optimal untuk mengirim data melalui jaringan-jaringan yang terhubung
- **Fragmentasi dan reassembly** — Kalau ukuran paket terlalu besar melebihi MTU (*Maximum Transmission Unit*), paket akan dipecah lalu disusun ulang di tujuan (Codecademy, n.d.; Raza, n.d.)

Protokol-protokol yang bekerja di layer ini:
- **IP** (Internet Protocol) — Protokol utama untuk routing
- **ICMP** — Untuk pelaporan error jaringan (misalnya saat kita melakukan `ping`)
- **IPSec** — Versi IP yang lebih aman karena menggunakan enkripsi
- **RIP, BGP, EIGRP** — Protokol-protokol routing (Codecademy, n.d.)

Satu hal yang perlu diketahui, di Network Layer keandalan pengiriman tidak dijamin. Walaupun banyak protokol yang menawarkan pengiriman yang reliable, pengirim belum tentu mendapat konfirmasi pengiriman (Raza, n.d.).

### Layer 4 — Transport Layer

Transport Layer ini sering disebut sebagai "jantung" dari model OSI. Layer ini jadi penghubung antara layer-layer atas yang bersifat abstrak (Layer 5-7) dengan layer-layer bawah yang berurusan dengan komunikasi fisik (Layer 1-3) (Codecademy, n.d.).

PDU di layer ini disebut **segment** (untuk TCP) atau **datagram** (untuk UDP).

Fungsi utama Transport Layer:
- **Segmentasi dan reassembly** — Memecah data jadi bagian-bagian kecil dan memberi nomor urut, lalu menyusunnya kembali di sisi penerima
- **Flow control** — Memastikan data tidak dikirim terlalu cepat sehingga penerima kewalahan
- **Error control** — Mengecek apakah data terkirim dengan benar menggunakan checksum. Kalau ada yang rusak, dilakukan retransmisi (Fortinet, n.d.; Raza, n.d.)

Ada dua jenis layanan di Transport Layer:

**1. Connection-oriented (TCP)**
TCP (*Transmission Control Protocol*) adalah protokol yang berorientasi koneksi. Sebelum mengirim data, TCP melakukan **Three-Way Handshake** dulu untuk membangun koneksi. Data dibagi menjadi segmen bernomor, setiap segmen harus di-*acknowledge*, dan kalau ada yang hilang akan dikirim ulang. TCP cocok untuk aplikasi yang butuh keandalan seperti web browsing, email, dan transfer file (Codecademy, n.d.; Raza, n.d.).

**2. Connectionless (UDP)**
UDP (*User Datagram Protocol*) tidak membangun koneksi terlebih dahulu. Begitu ada request, server langsung mengirim data tanpa peduli apakah data sampai ke tujuan atau tidak. UDP lebih cepat tapi kurang reliable. Cocok untuk aplikasi real-time seperti video streaming, online gaming, dan VoIP (Codecademy, n.d.; Raza, n.d.).

Soal port, di layer ini ada pembagian:
- Port 0–1023: *Well-Known Ports* (HTTP port 80, HTTPS port 443, SSH port 22, DNS port 53, dll)
- Port 1024–49.151: *Registered Ports*
- Port 49.152–65.535: *Private/Dynamic Ports*

Ketika TCP dan IP digunakan bersama, kombinasi alamat IP dan port number disebut **socket**. Misalnya `8.8.8.8:443` artinya komunikasi ke alamat IP `8.8.8.8` di port `443` (Codecademy, n.d.).

### Layer 5 — Session Layer

Session Layer mengatur pembukaan, pengelolaan, dan penutupan *communication session* antara dua perangkat. "*Session*" di sini maksudnya adalah waktu antara dibukanya dan ditutupnya sebuah koneksi (Fortinet, n.d.).

Fungsi-fungsinya:
- **Membuka session** — Memulai koneksi antara aplikasi lokal dan remote
- **Menjaga session** — Memastikan koneksi tetap terbuka selama data masih perlu dikirim
- **Sinkronisasi dan checkpoint** — Kalau sedang mengirim file besar dan tiba-tiba koneksi terputus, checkpoint memungkinkan transmisi dilanjutkan tanpa harus mengulang dari awal (Fortinet, n.d.; Raza, n.d.)
- **Menutup session** — Menutup koneksi setelah selesai supaya resource tidak terbuang

Analoginya seperti percakapan telepon. Kita mengangkat telepon (membuka session), berbicara (active session), lalu menutup telepon (menutup sesi) (Codecademy, n.d.).

Mode komunikasi di layer ini ada dua:
- **Half-duplex** — Dua arah, tetapi bergantian (seperti walkie-talkie)
- **Full-duplex** — Dua arah bersamaan (seperti telepon biasa)

Protokol yang ada di layer ini termasuk RPC (*Remote Procedure Call*), PPTP, NetBIOS, dan SDP (Codecademy, n.d.; Raza, n.d.).

### Layer 6 — Presentation Layer

Presentation Layer ini tugasnya menyiapkan data supaya bisa dipahami oleh Application Layer. Kadang disebut juga *syntax layer* karena berurusan dengan format dan sintaks data (Raza, n.d.).

Fungsi utamanya ada tiga:
1. **Translasi data** — Mengonversi data antar format yang berbeda, misalnya dari EBCDIC ke ASCII. Ini penting supaya data yang dikirim dari satu sistem bisa dibaca oleh sistem lain yang mungkin punya cara encoding berbeda (Raza, n.d.).
2. **Kompresi data** — Mengurangi ukuran data untuk mempercepat transmisi. Data dikompres sebelum dikirim dan didekompresi di tujuan (Fortinet, n.d.).
3. **Enkripsi dan dekripsi** — Di sinilah fungsi enkripsi sebenarnya berada. Protokol seperti SSL dan TLS bekerja di layer ini untuk mengamankan data yang dikirim lewat jaringan (Codecademy, n.d.).

Format dan protokol yang beroperasi di layer ini antara lain ASCII, JPEG, GIF, PNG, MPEG untuk format data, serta TLS dan SSL untuk enkripsi (Codecademy, n.d.).

### Layer 7 — Application Layer

Application Layer adalah layer paling atas yang paling dekat dengan pengguna. Tapi perlu diingat, **aplikasi itu sendiri bukan bagian dari layer ini**. Yang termasuk di layer ini adalah protokol dan layanan yang dipakai oleh aplikasi untuk melakukan komunikasi jaringan (Codecademy, n.d.; Raza, n.d.).

Contohnya, web browser seperti Chrome atau Firefox bukan bagian dari Application Layer. Tapi protokol HTTP yang digunakan oleh browser tersebut untuk mengakses halaman web, itulah yang ada di Application Layer. Jadi HTTP bisa dipakai oleh browser apa saja — tidak eksklusif untuk satu browser tertentu (Codecademy, n.d.).

Fungsi-fungsi di Application Layer:
- Identifikasi ketersediaan resource sebelum memulai komunikasi
- Layanan directory untuk mengelola informasi perangkat dan user di jaringan
- Sinkronisasi komunikasi antar aplikasi (Raza, n.d.)

Protokol-protokol utama di layer ini:
- **HTTP/HTTPS** — Untuk komunikasi web (port 80/443)
- **FTP** — Transfer file (port 20-21)
- **SMTP** — Pengiriman email (port 25)
- **DNS** — Menerjemahkan nama domain ke alamat IP (port 53)
- **POP3/IMAP** — Untuk mengambil email (port 110/143)
- **SSH** — Remote access yang aman (port 22)
- **SNMP** — Monitoring dan manajemen jaringan (Imperva, n.d.; Raza, n.d.)

## Contoh Alur Komunikasi: Mengirim Email

Supaya lebih gampang dipahami, berikut ini adalah contoh bagaimana model OSI bekerja saat mengirim email (berdasarkan penjelasan Imperva, n.d. dan Raza, n.d.):

**Proses pengiriman:**
1. **Layer 7** — Email client (misalnya Outlook) menggunakan SMTP untuk menyiapkan pesan email
2. **Layer 6** — Pesan diformat, dikompres, dan dienkripsi
3. **Layer 5** — Sesi dibuka antara server email pengirim dan penerima
4. **Layer 4** — Data email dipecah jadi segmen-segmen kecil oleh TCP
5. **Layer 3** — Setiap paket dikasih alamat IP sumber dan tujuan, lalu dirouting
6. **Layer 2** — MAC address digunakan untuk menangani perjalanan paket di jaringan lokal
7. **Layer 1** — Data diubah jadi sinyal listrik dan dikirim lewat kabel

**Proses penerimaan:**
Prosesnya terbalik — sinyal dikembalikan jadi data di Layer 1, lalu naik terus sampai Layer 7 dimana email muncul di inbox penerima.

## Model OSI vs TCP/IP

Selain model OSI, ada juga model TCP/IP yang sebenarnya lebih tua dan dibuat oleh US Department of Defense. Model TCP/IP lebih sederhana karena cuma punya **4 layer** (Imperva, n.d.; Check Point, n.d.):

| OSI Model | TCP/IP Model |
|---|---|
| Layer 7 — Application | Application Layer |
| Layer 6 — Presentation | (digabung ke Application) |
| Layer 5 — Session | (digabung ke Application) |
| Layer 4 — Transport | Transport Layer |
| Layer 3 — Network | Internet Layer |
| Layer 2 — Data Link | Network Access Layer |
| Layer 1 — Physical | (digabung ke Network Access) |

Jadi intinya, TCP/IP menggabungkan Layer 5, 6, 7 jadi satu Application Layer, dan menggabungkan Layer 1, 2 jadi satu Network Access Layer (Imperva, n.d.).

Perbedaan utama keduanya:
- **OSI** itu lebih bersifat teoritis dan *protocol-independent*, cocok untuk memahami konsep jaringan secara umum
- **TCP/IP** lebih praktis dan langsung memetakan ke protokol nyata yang digunakan di internet saat ini
- Di TCP/IP, hampir semua aplikasi menggunakan semua layer. Di OSI, hanya layer 1-3 yang wajib untuk komunikasi data dasar (Imperva, n.d.; Check Point, n.d.)

Model TCP/IP inilah yang jadi tulang punggung internet modern karena fokusnya yang lebih praktis. Tapi model OSI tetap penting sebagai alat pembelajaran dan pemahaman arsitektur jaringan (Raza, n.d.).

## Kesimpulan

Model OSI adalah kerangka kerja yang sangat berguna untuk memahami bagaimana komunikasi data terjadi di jaringan komputer. Dengan pembagian 7 layer yang jelas, model ini membantu kita untuk bisa memvisualisasikan alur data, melakukan troubleshooting secara sistematis, dan memahami di mana berbagai protokol dan teknologi jaringan beroperasi.

Walaupun dalam praktiknya yang lebih banyak digunakan adalah model TCP/IP, pemahaman tentang model OSI tetap menjadi fondasi yang penting dalam mempelajari jaringan komputer.

---

## Daftar Pustaka

- Codecademy Team. (n.d.). *OSI Model: Complete Guide to the 7 Network Layers*. Codecademy. Diakses pada 26 Maret 2026, dari https://www.codecademy.com/article/osi-model-complete-guide-to-the-7-network-layers
- Check Point Software. (n.d.). *What is the OSI Model? Understanding the 7 Layers*. Check Point Cyber Hub. Diakses pada 26 Maret 2026, dari https://www.checkpoint.com/cyber-hub/network-security/what-is-the-osi-model-understanding-the-7-layers/
- Fortinet. (n.d.). *What is the OSI Model? 7 Network Layers Explained*. Fortinet CyberGlossary. Diakses pada 27 Maret 2026, dari https://www.fortinet.com/resources/cyberglossary/osi-model
- Imperva. (n.d.). *What is OSI Model | 7 Layers Explained*. Imperva Learning Center. Diakses pada 27 Maret 2026, dari https://www.imperva.com/learn/application-security/osi-model/
- Raza, M. (n.d.). *Understanding the OSI Model*. BMC Blogs. Diakses pada 27 Maret 2026, dari https://www.bmc.com/blogs/osi-model-7-layers/

## Kontribusi
Bagas Aditama Suryo Nugroho (L0124042) :
- Mencari sumber referensi
- Mengekstrak isi dari referensi
- Membuat outline dokumen
- Menulis dan melengkapi outline yang sudah dibuat menjadi dokumen yang terstruktur
- Mengecek kembali dokumen