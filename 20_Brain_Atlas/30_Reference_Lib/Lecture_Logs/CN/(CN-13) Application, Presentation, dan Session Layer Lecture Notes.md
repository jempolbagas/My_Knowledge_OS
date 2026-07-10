---
title: "(CN-13) Application, Presentation, dan Session Layer Lecture Notes"
course: ""
tags: []
aliases: ["(CN-13) Application, Presentation, dan Session Layer Lecture Notes"]
created: "2026-06-24"
---
# Materi Pembelajaran: Application, Presentation, dan Session Layer

**Mata Kuliah:** Jaringan Komputer (Genap 2025/2026)  
**Institusi:** Informatika UNS  
**Berdasarkan Presentasi Oleh:** Herdito Ibnu Dewangkoro  

---

## 1. Pendahuluan: Model OSI vs TCP/IP

Dalam arsitektur jaringan komputer, tiga layer teratas pada model OSI (Open Systems Interconnection)—yaitu **Application Layer (Layer 7)**, **Presentation Layer (Layer 6)**, dan **Session Layer (Layer 5)**—mendefinisikan berbagai fungsi spesifik. Pada model TCP/IP, ketiga fungsi layer OSI ini digabungkan ke dalam satu layer komprehensif yang disebut sebagai **Application Layer**.

---

## 2. Mengenal Layer 5, 6, dan 7 pada Model OSI

### Application Layer (Layer 7)
Application layer berfungsi menyediakan *interface* (antarmuka) antara aplikasi yang digunakan oleh pengguna untuk berkomunikasi dan jaringan dasar tempat pesan tersebut dikirimkan (*underlying network*). Layer ini adalah lapisan yang paling dekat dengan pengguna akhir.

*   **Protokol Utama:** HTTP, FTP, TFTP, IMAP, DNS, DHCP, POP, dan SMTP.

### Presentation Layer (Layer 6)
Presentation layer bertanggung jawab atas format dan representasi data. Fungsi utamanya meliputi:
1.  **Memformat/Mempresentasikan Data:** Mengubah data pada *source device* (perangkat sumber) ke dalam format yang dapat diterima dan dibaca oleh *destination device* (perangkat tujuan).
2.  **Kompresi Data:** Mengurangi ukuran data dengan metode tertentu agar dapat ditransmisikan lebih efisien dan kemudian didekompresi di perangkat tujuan.
3.  **Enkripsi & Dekripsi:** Mengamankan data dengan mengenkripsinya untuk transmisi jaringan dan mendekripsinya kembali setelah data diterima.

*   **Standar Format Video:** Matroska Video (MKV), Motion Picture Experts Group (MPG), QuickTime Video (MOV).
*   **Standar Format Grafis:** Graphics Interchange Format (GIF), Joint Photographic Experts Group (JPG), Portable Network Graphics (PNG).

### Session Layer (Layer 5)
Session layer bertugas mengelola koneksi antar aplikasi. Fungsi utamanya meliputi:
1.  Menciptakan dan memelihara dialog atau koneksi antara aplikasi sumber dan aplikasi tujuan.
2.  Menangani pertukaran informasi untuk memulai dialog, menjaganya tetap aktif, serta me-*restart* *session* (sesi) yang terganggu atau tidak aktif dalam jangka waktu lama.

---

## 3. TCP/IP Application Layer Protocol

Protokol application layer pada TCP/IP menentukan format dan informasi kontrol yang dibutuhkan untuk berbagai fungsi komunikasi internet. Agar komunikasi dapat terjalin dengan sukses, protokol pada *source host* dan *destination host* harus saling kompatibel.

Beberapa contoh protokol kunci beserta alokasi *port* yang digunakan:
*   **DNS (Domain Name System):** TCP/UDP Port 53. Berfungsi untuk menerjemahkan nama domain (seperti `cisco.com`) menjadi *IP address* berupa angka.
*   **DHCP (Dynamic Host Configuration Protocol):** UDP Port 67 (Server) / Port 68 (Client). Berfungsi menetapkan *IP address* secara dinamis kepada host, yang dapat digunakan kembali jika sudah tidak dibutuhkan.
*   **HTTP (Hypertext Transfer Protocol):** TCP Port 80, 8080. Menyediakan seperangkat aturan untuk bertukar teks, gambar, suara, video, dan berkas multimedia lainnya di World Wide Web (WWW).

---

## 4. Protokol Web: HTTP, HTTPS, dan HTML

Saat seorang pengguna mengetikkan URL (Uniform Resource Locator) di dalam *web browser*, browser tersebut membuat koneksi ke web server menggunakan protokol HTTP.

### Proses Mengakses Web Page
Misalkan pengguna ingin mengakses: `http://www.cisco.com/index.html`
1.  **Interpretasi URL:** Browser menginterpretasikan URL menjadi tiga bagian:
    *   Protokol: `http`
    *   Nama Server / Domain: `www.cisco.com`
    *   Nama File Spesifik: `index.html`
2.  **Resolusi DNS & Request:** Browser akan memeriksa dengan DNS *name server* untuk mengubah `www.cisco.com` menjadi *IP address* numerik. Setelah IP ditemukan, klien (browser) mengirimkan **GET request** ke server untuk meminta file `index.html`.
3.  **Response Server:** Server web menerima *request* dan membalas dengan mengirimkan kode HTML (*Hypertext Markup Language*) ke browser. Response ini biasanya diawali dengan header `HTTP/1.1 200 OK`.
4.  **Rendering (Pemrosesan):** Browser kemudian menguraikan kode HTML tersebut dan memformat teks, gambar, serta tata letak sehingga halaman web dapat ditampilkan di jendela browser.

### HTTP vs HTTPS dan Tipe Pesan
*   **HTTP vs HTTPS:** HTTP adalah protokol *request/response* dasar yang tidak aman. Untuk komunikasi yang aman di internet, digunakan **HTTPS (HTTP Secure)**, yang akan mengenkripsi data yang dipertukarkan.
*   **Jenis Pesan HTTP Umum:**
    *   `GET`: Klien meminta data (seperti halaman web HTML) dari *web server*.
    *   `POST`: Klien mengunggah data ke server, seperti ketika mengisi formulir web.
    *   `PUT`: Klien mengunggah *resource* atau konten (seperti gambar) ke *web server*.

---

## 5. Protokol Email

Email beroperasi menggunakan metode *store-and-forward* untuk mengirimkan pesan elektronik melalui jaringan. Pesan disimpan di dalam basis data pada *mail server*. Untuk mengelola lalu lintas email, jaringan komputer memanfaatkan tiga protokol utama:

### 1. SMTP (Simple Mail Transfer Protocol)
*   **Fungsi:** Digunakan untuk **mengirim** email.
*   **Proses:** *Client* yang mengirim pesan akan terhubung ke *SMTP process* server melalui **Port 25**. Pesan tersebut dikirimkan ke server, yang selanjutnya akan meletakkannya di *local account* jika alamat penerima ada di *server* yang sama. Jika beda, server akan meneruskan (*forward*) pesan ke mail server lain.
*   Jika server tujuan sedang sibuk atau luring (*offline*), SMTP akan menunda pengiriman dan mencoba kembali mengirimkannya di lain waktu.

### 2. POP / POP3 (Post Office Protocol)
*   **Fungsi:** Digunakan klien untuk **menerima** (mengambil) email dari *mail server*.
*   **Proses:** Server POP biasanya berjalan secara pasif mendengarkan *request* di **TCP Port 110**. Setelah terhubung, klien dan server bertukar perintah.
*   **Karakteristik:** Email diunduh ke aplikasi klien dan **dihapus dari server**. Hal ini tidak disarankan bagi pengguna atau perusahaan yang membutuhkan solusi pencadangan (*backup*) terpusat.

### 3. IMAP (Internet Message Access Protocol)
*   **Fungsi:** Protokol alternatif untuk **menerima** atau mengakses pesan email.
*   **Karakteristik:** Tidak seperti POP, saat menggunakan IMAP, aplikasi klien hanya mengunduh *salinan* dari pesan tersebut. Pesan aslinya akan **tetap tersimpan di server** sampai dihapus secara manual. Hal ini memungkinkan pengguna mengakses email yang sama dari perangkat yang berbeda (sinkronisasi multi-perangkat).
