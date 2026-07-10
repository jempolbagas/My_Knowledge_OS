---
title: "(CN-11) Transport Layer Lecture Notes"
course: ""
tags: []
aliases: ["(CN-11) Transport Layer Lecture Notes"]
created: "2026-06-24"
---
# Materi Pembelajaran: Transport Layer

**Program Studi:** Informatika UNS  
**Mata Kuliah:** Jaringan Komputer Genap 2025/2026  
**Dosen Pengampu:** Herdito Ibnu Dewangkoro  

---

## 1. Pengantar Transportasi Data

Transport Layer merupakan lapisan krusial dalam model TCP/IP yang bertindak sebagai penghubung antara Application layer dengan layer-layer di bawahnya (Internet dan Network Access). Lapisan ini bertanggung jawab penuh atas transmisi data dalam jaringan.

### Tanggung Jawab Utama Transport Layer
Transport layer memiliki beberapa fungsi dan tanggung jawab utama untuk memastikan komunikasi antar host berjalan lancar:
* **Melacak individual conversation:** Memantau komunikasi data spesifik antara aplikasi pada source dan destination.
* **Segmentasi data dan menyusun kembali segment:** Memecah data besar dari application layer menjadi bagian-bagian kecil (segment) agar mudah ditransmisikan, lalu merakitnya kembali di sisi penerima.
* **Menambahkan informasi header:** Menyisipkan header pada setiap segment yang berisi informasi rute, kontrol, dan identifikasi.
* **Mengidentifikasi, memisahkan, dan mengelola beberapa conversation:** Memastikan data dari berbagai aplikasi tidak tercampur.
* **Multiplexing:** Memungkinkan komunikasi dari conversation yang berbeda untuk disisipkan dan dikirimkan secara bersamaan pada jaringan fisik yang sama.

### Protokol Transport Layer
IP (Internet Protocol) hanya bertugas untuk merutekan paket, namun tidak menentukan *bagaimana* transportasi paket tersebut berlangsung. Protokol pada Transport layer-lah yang menentukan cara mentransfer pesan antar host serta mengelola kebutuhan keandalan (*reliability*) komunikasi. Terdapat dua protokol utama:
1. **Transmission Control Protocol (TCP)**
2. **User Datagram Protocol (UDP)**

---

## 2. Transmission Control Protocol (TCP)

TCP adalah protokol yang menyediakan keandalan (*reliability*) tinggi dan kontrol aliran (*flow control*). Karena sifatnya ini, TCP sangat cocok untuk aplikasi yang tidak mentolerir kehilangan data.

### Karakteristik dan Operasi Dasar TCP
* **Connection-Oriented:** TCP harus terlebih dahulu membuat koneksi (*established connection*) antara pengirim dan penerima sebelum data ditransmisikan.
* **Stateful Protocol:** Melacak status sesi komunikasi secara terus-menerus.
* **Penomoran dan Pelacakan:** Memberi nomor urut (*sequence number*) pada segment dan melacak segment yang dikirim.
* **Acknowledgment:** Mengakui (memberi konfirmasi) data yang telah berhasil diterima.
* **Retransmission:** Mengirim ulang data yang tidak mendapat pengakuan (*acknowledgment*) setelah rentang waktu tertentu.
* **Sequencing:** Menyusun dan mengurutkan kembali data yang mungkin tiba dalam urutan yang acak/salah.
* **Flow Control:** Mengirim data pada laju (*rate*) yang efisien dan dapat ditangani oleh penerima, mencegah terjadinya beban berlebih (overload) memori dan pemrosesan pada host tujuan.

### Format TCP Header (20 Bytes)
TCP memiliki struktur header yang lebih kompleks untuk mendukung fitur-fiturnya:

| TCP Header Field | Deskripsi |
| :--- | :--- |
| **Source Port (16-bit)** | Mengidentifikasi aplikasi pengirim berdasarkan nomor port. |
| **Destination Port (16-bit)** | Mengidentifikasi aplikasi penerima berdasarkan nomor port. |
| **Sequence Number (32-bit)** | Digunakan untuk tujuan perakitan kembali (reassembly) data. |
| **Acknowledgment Number (32-bit)** | Menunjukkan bahwa data telah diterima dan byte selanjutnya yang diharapkan dari sumber. |
| **Header Length (4-bit)** | Dikenal sebagai "data offset", menunjukkan panjang dari TCP segment header. |
| **Reserved (6-bit)** | Dipesan untuk penggunaan di masa mendatang. |
| **Control Bits (6-bit)** | Berisi bit codes (flags) yang mengindikasikan tujuan dan fungsi dari segment TCP. |
| **Window Size (16-bit)** | Mengindikasikan jumlah byte yang dapat diterima pada satu waktu (untuk *flow control*). |
| **Checksum (16-bit)** | Digunakan untuk pengecekan error pada header segment dan data. |
| **Urgent (16-bit)** | Menunjukkan jika data yang terkandung bersifat mendesak (*urgent*). |

### Aplikasi yang Menggunakan TCP
TCP digunakan untuk layanan yang menuntut pengiriman yang andal tanpa data yang hilang atau rusak:
* **HTTP / HTTPS:** World Wide Web
* **FTP:** File Transfer Protocol
* **SMTP / IMAP:** Pengiriman Email
* **SSH:** Secure Shell

---

## 3. User Datagram Protocol (UDP)

UDP adalah protokol alternatif yang jauh lebih sederhana, cepat, namun tidak memberikan jaminan paket akan sampai ke tujuan secara utuh. 

### Karakteristik dan Operasi Dasar UDP
* **Low Overhead:** Hanya memiliki *overhead* (beban jaringan tambahan) yang sangat kecil, datagram header yang ringan, dan tanpa *network management traffic*.
* **Connectionless:** Tidak melakukan negosiasi *established connection* sebelum mengirimkan data.
* **Stateless:** Tidak melacak informasi yang dikirim/diterima antara klien dan server.
* **Best-Effort Delivery:** Mengirim data sebaik mungkin tanpa meminta pengakuan (acknowledgment) bahwa data telah sampai di tujuan.
* **No Retransmission & No Sequencing:** Segment yang hilang di tengah jalan tidak akan dikirim ulang. Data direkonstruksi hanya berdasarkan urutan kedatangannya saja, bukan urutan pengirimannya.

### Format UDP Header (8 Bytes / 64 bits)
Header UDP jauh lebih sederhana dibanding TCP karena hanya berisi 4 *field* utama:

| UDP Header Field | Deskripsi |
| :--- | :--- |
| **Source Port (16-bit)** | Mengidentifikasi aplikasi sumber (pengirim). |
| **Destination Port (16-bit)** | Mengidentifikasi aplikasi tujuan (penerima). |
| **Length (16-bit)** | Menunjukkan total panjang dari UDP datagram (header + data). |
| **Checksum (16-bit)** | Pengecekan error sederhana untuk header datagram dan datanya. |

### Aplikasi yang Menggunakan UDP
UDP adalah pilihan ideal bagi aplikasi yang membutuhkan kecepatan tinggi, dapat menoleransi hilangnya sebagian data, dan membutuhkan *delay* yang sangat minimal:
* **Multimedia & Streaming:** Voice over IP (VoIP), Video Conferencing, dan Live Video Streaming.
* **Request & Reply Sederhana:** Domain Name System (DNS), Dynamic Host Configuration Protocol (DHCP).
* **Aplikasi yang Menangani Keandalannya Sendiri:** Simple Network Management Protocol (SNMP), Trivial File Transfer Protocol (TFTP).

---

## 4. Kesimpulan: Pemilihan TCP vs UDP

Pemilihan antara TCP dan UDP bergantung sepenuhnya pada kebutuhan aplikasi yang berjalan di layer atasnya:

* **Pilih TCP jika:** Penting bagi aplikasi agar **semua** data sampai dengan utuh, diproses dalam urutan yang benar, dan tidak ada data yang terlewat (Reliable, Acknowledges, Resends, Sequenced).
* **Pilih UDP jika:** Aplikasi memerlukan transmisi yang cepat dengan delay seminimal mungkin, pengiriman data bersifat membalas permintaan singkat (*request-and-reply*), dan kehilangan sedikit frame/data tidak merusak fungsionalitas utama (Fast, Low overhead, No Acks, Best-effort).
