---
title: "(CN-7) IPv4 Lecture Notes"
course: ""
tags: []
aliases: ["(CN-7) IPv4 Lecture Notes"]
created: "2026-06-23"
---
# Ringkasan Materi Perkuliahan: Internet Protocol Version 4 (IPv4)

**Mata Kuliah:** Jaringan Komputer (Genap 2025/2026)  
**Program Studi:** Informatika UNS  
**Dosen Pengampu:** Herdito Ibnu Dewangkoro  

---

## 1. Pengantar Internet Protocol (IP)

Internet Protocol (IP) merupakan protokol yang beroperasi pada **Layer 3 (Network Layer)** dalam model OSI. Protokol ini memuat informasi pengalamatan (*addressing*) serta beberapa informasi kontrol tertentu yang memungkinkan paket data dirutekan (*routing*) dari satu jaringan ke jaringan lainnya. Versi Internet Protocol yang paling sering digunakan dalam jaringan komputer saat ini adalah **IPv4** dan **IPv6**.

---

## 2. Konversi Bilangan Desimal - Biner

Pemahaman mengenai konversi sistem bilangan desimal ke biner dan sebaliknya sangat krusial dalam mempelajari IPv4 karena seluruh operasi pengalamatan dan *subnetting* dilakukan dalam representasi biner 32-bit.

### A. Konversi Biner ke Desimal
Proses dilakukan dengan mengalikan setiap bit biner dengan nilai perpangkatan basis dua ($2^n$) sesuai dengan posisi bit tersebut (dimulai dari indeks 0 dari kanan).

**Contoh 1:**
$$\begin{aligned}
(11111000)_2 &= (1 \times 2^7) + (1 \times 2^6) + (1 \times 2^5) + (1 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (0 \times 2^1) + (0 \times 2^0) \\
&= 128 + 64 + 32 + 16 + 8 + 0 + 0 + 0 \\
&= (248)_{10}
\end{aligned}$$

**Contoh 2:**
$$\begin{aligned}
(11111111)_2 &= (1 \times 2^7) + (1 \times 2^6) + (1 \times 2^5) + (1 \times 2^4) + (1 \times 2^3) + (1 \times 2^2) + (1 \times 2^1) + (1 \times 2^0) \\
&= 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 \\
&= (255)_{10}
\end{aligned}$$

### B. Konversi Desimal ke Biner
Proses dilakukan dengan membagi bilangan desimal secara berulang dengan basis 2, kemudian mencatat sisa hasil baginya hingga hasil baginya mencapai 0. Hasil biner dibaca dari sisa pembagian paling akhir (bawah) ke paling awal (atas).

**Contoh:** Konversi $(224)_{10}$ ke biner:
* $224 \div 2 = 112$ sisa $0$
* $112 \div 2 = 56$ sisa $0$
* $56 \div 2 = 28$ sisa $0$
* $28 \div 2 = 14$ sisa $0$
* $14 \div 2 = 7$ sisa $0$
* $7 \div 2 = 3$ sisa $1$
* $3 \div 2 = 1$ sisa $1$
* $1 \div 2 = 0$ sisa $1$

Dibaca dari bawah ke atas, maka $(224)_{10} = (11100000)_2$. *(Catatan: Ditulis lengkap 8-bit menjadi `11100000`)*.

---

## 3. Struktur Alamat IPv4

Alamat IPv4 terdiri dari struktur **32-bit biner** yang dibagi menjadi 4 bagian kelompok (masing-masing 8 bit atau dinamakan *oktet*), yang dipisahkan oleh tanda titik (*dotted decimal notation*).

### A. Network Portion dan Host Portion
Setiap alamat IPv4 dibagi menjadi dua bagian utama:
1. **Network Portion (Bagian Jaringan):** Mengidentifikasi jaringan spesifik tempat perangkat berada.
2. **Host Portion (Bagian Host):** Mengidentifikasi perangkat spesifik (host) di dalam jaringan tersebut.

Untuk mengidentifikasi batas antara *network portion* dan *host portion*, digunakan suatu nilai parameter pembatas yang disebut **Subnet Mask**.

### B. Subnet Mask dan Operasi ANDing
Subnet Mask membandingkan setiap bitnya dengan alamat IP (bit-by-bit). Proses matematis untuk mengidentifikasi alamat jaringan ini menggunakan logika Boolean yang disebut **ANDing**. 

Aturan dasar logika **AND**:
* $1 \text{ AND } 1 = 1$
* $1 \text{ AND } 0 = 0$
* $0 \text{ AND } 1 = 0$
* $0 \text{ AND } 0 = 0$

Jika hasil operasi ANDing antara dua buah host address menghasilkan nilai *Network Address* yang sama, maka kedua perangkat tersebut berada dalam satu segmen jaringan yang sama. Sebaliknya, jika hasilnya berbeda, maka berada di jaringan berbeda dan memerlukan router agar dapat saling berkomunikasi.

**Contoh Visual Operasi ANDing:**
* **IPv4 Host Address:** `192.168.10.10` $\rightarrow$ `11000000.10101000.00001010.00001010`
* **Subnet Mask:** `255.255.255.0` $\rightarrow$ `11111111.11111111.11111111.00000000`
* **Hasil (Network Address):** `192.168.10.0` $\rightarrow$ `11000000.10101000.00001010.00000000`

### C. Panjang Prefix (Prefix Length / CIDR Notation)
Selain menggunakan representasi bilangan desimal dan biner, penyajian subnet mask dapat diringkas menggunakan **Panjang Prefix**. Panjang prefix ditulis menggunakan notasi garis miring (`/`) yang diikuti oleh bilangan desimal yang menyatakan **jumlah bit bernilai 1 di dalam subnet mask biner**.

| Subnet Mask Desimal | Subnet Mask Biner (32-bit Address) | Panjang Prefix |
| :--- | :--- | :--- |
| 255.0.0.0 | `11111111.00000000.00000000.00000000` | `/8` |
| 255.255.0.0 | `11111111.11111111.00000000.00000000` | `/16` |
| 255.255.255.0 | `11111111.11111111.11111111.00000000` | `/24` |
| 255.255.255.128 | `11111111.11111111.11111111.10000000` | `/25` |
| 255.255.255.192 | `11111111.11111111.11111111.11000000` | `/26` |
| 255.255.255.224 | `11111111.11111111.11111111.11100000` | `/27` |
| 255.255.255.240 | `11111111.11111111.11111111.11110000` | `/28` |
| 255.255.255.248 | `11111111.11111111.11111111.11111000` | `/29` |
| 255.255.255.252 | `11111111.11111111.11111111.11111100` | `/30` |

### D. Tiga Jenis Alamat dalam Satu Subnet
Dalam satu subnet terdapat tiga kategori alamat fungsional:
1. **Network Address:** Alamat yang merepresentasikan jaringan. Bit pada host portion bernilai **semua 0** (`All 0s`).
2. **Host Address:** Alamat yang dapat dikonfigurasikan pada interface perangkat (komputer, router, printer, dll).
   * **First Host Address:** Alamat host pertama (`All 0s dan akhiran 1`).
   * **Last Host Address:** Alamat host terakhir (`All 1s dan akhiran 0`).
3. **Broadcast Address:** Alamat khusus yang digunakan untuk mengirim paket ke seluruh host dalam satu subnet. Bit pada host portion bernilai **semua 1** (`All 1s`).

**Rumus Perhitungan Jumlah Perangkat (Host):**
$$\text{Jumlah Host} = 2^{(32 - \text{Panjang Prefix})} - 2$$
*(Dikurangi 2 karena Alamat Network dan Alamat Broadcast tidak boleh dipasang pada perangkat).*

**Contoh Kasus pada Jaringan `192.168.10.0/24`:**
* **Subnet Mask:** `255.255.255.0`
* **Network Address:** `192.168.10.0`
* **First Host Address:** `192.168.10.1`
* **Last Host Address:** `192.168.10.254`
* **Broadcast Address:** `192.168.10.255`
* **Total Host Valid:** $2^{(32-24)} - 2 = 2^8 - 2 = 256 - 2 = 254$ host.

Semakin panjang prefix yang digunakan, maka jumlah bit host akan semakin sedikit, yang berakibat pada berkurangnya jumlah host yang tersedia per subnet.

---

### E. Latihan Soal Mandiri
**Soal:** Diketahui sebuah server memiliki alamat IPv4 `6.6.6.10` dengan subnet mask `255.255.255.248`. Tentukan:
1. Alamat IPv4 tersebut dalam bentuk biner.
2. Subnet mask dalam bentuk biner.
3. Subnet mask dalam bentuk prefix.
4. Network address dalam bentuk desimal.
5. Jumlah host dalam satu subnet.
6. Broadcast address dalam bentuk desimal.

**Jawaban Pembahasan:**
1. **IPv4 biner:** `00000110.00000110.00000110.00001010`
2. **Subnet mask biner:** `11111111.11111111.11111111.11111000`
3. **Prefix:** `/29` (karena total bit bernilai satu ada sebanyak 29).
4. **Network address:** Hasil ANDing antara `00001010` (10) dan `11111000` (248) pada oktet terakhir menghasilkan `00001000` (8). Jadi, Network Address desimalnya adalah **`6.6.6.8`**.
5. **Jumlah host:** $2^{(32-29)} - 2 = 2^3 - 2 = 8 - 2 = \mathbf{6}$ **host**.
6. **Broadcast address:** Mengubah sisa 3 bit terakhir host portion menjadi bernilai 1 (`00001000` $\rightarrow$ `00001111` = 15). Maka Broadcast Address desimalnya adalah **`6.6.6.15`**.

---

## 4. Jenis-Jenis Alamat IPv4

### A. Public vs Private IPv4 Address
Berdasarkan standar **RFC 1918**, alamat IPv4 dibagi menjadi dua kelompok fungsional:
1. **Public IP Address:** Alamat yang unik secara global, diregistrasikan secara resmi, dan dapat dirutekan secara langsung di internet antar router Internet Service Provider (ISP).
2. **Private IP Address:** Blok alamat yang digunakan secara bebas oleh organisasi untuk jaringan internal (intranet). Alamat ini bersifat tidak unik secara global dan **tidak dapat dirutekan di internet**.

**Rentang Alamat IP Private (RFC 1918):**
* `10.0.0.0/8` (Rentang: `10.0.0.0` s.d. `10.255.255.255`)
* `172.16.0.0/12` (Rentang: `172.16.0.0` s.d. `172.31.255.255`)
* `192.168.0.0/16` (Rentang: `192.168.0.0` s.d. `192.168.255.255`)

 agar perangkat dengan IP private dapat berkomunikasi ke internet, digunakan mekanisme **NAT (Network Address Translation)** yang biasanya dikonfigurasikan di router perbatasan jaringan untuk menerjemahkan source IP private menjadi public IP address sebelum dialihkan ke ISP.

### B. Alamat IP dengan Penggunaan Spesial
1. **Loopback Address (`127.0.0.0/8`):** Umumnya direpresentasikan dengan alamat `127.0.0.1`. Digunakan oleh host untuk mengarahkan lalu lintas data ke dirinya sendiri guna menguji fungsionalitas dan konfigurasi *stack* software TCP/IP internal lokal.
2. **Link-Local Address (`169.254.0.0/16`):** Dikenal sebagai **APIPA (Automatic Private IP Addressing)**. Alamat ini akan secara otomatis diisikan (*self-assigned*) secara mandiri oleh sistem operasi (seperti Windows DHCP Client) ketika komputer dikonfigurasi otomatis namun gagal memperoleh respon dari DHCP Server di jaringan tersebut.
   * *Catatan:* **DHCP Server** merupakan layanan otomatis pengisian alamat IP secara dinamis kepada client.

### C. Classful vs Classless Addressing
Secara historis (**RFC 790 pada tahun 1981**), pengalamatan IP dibagi dalam skema kelas (*Classful Addressing*):
* **Kelas A (`0.0.0.0/8` - `127.0.0.0/8`):** Menyediakan jaringan skala masif ($16.777.214$ host/net). Porsi alokasi total sebesar 50% dari IP yang ada.
* **Kelas B (`128.0.0.0/16` - `191.255.0.0/16`):** Menyediakan jaringan menengah ($65.534$ host/net). Porsi alokasi sebesar 25%.
* **Kelas C (`192.0.0.0/24` - `223.255.255.0/24`):** Menyediakan jaringan skala kecil ($254$ host/net). Porsi alokasi sebesar 12.5%.
* **Kelas D (`224.0.0.0` - `239.255.255.255`):** Digunakan khusus untuk keperluan komunikasi **Multicast** (tidak memiliki subnet mask biasa).
* **Kelas E (`240.0.0.0` - `255.255.255.255`):** Berstatus **Reserved** (dicadangkan untuk penggunaan masa depan dan eksperimental).

> **Penting:** Dikarenakan skema *Classful* mengakibatkan pemborosan alokasi IP yang sangat besar, industri jaringan beralih sepenuhnya menggunakan sistem **Classless Addressing**, yang mengabaikan batasan baku kelas A, B, maupun C melalui pemanfaatan teknik CIDR dan VLSM.

### D. Manajemen Alamat IP Global
Lembaga internasional utama yang bertugas mengelola tata kelola alokasi alamat IP sedunia adalah **IANA (Internet Assigned Numbers Authority)**. IANA mendistribusikan blok-blok IP ke dalam 5 entitas regional regional yang dikenal sebagai **RIR (Regional Internet Registry)**:
1. **AfriNIC:** Kawasan Afrika.
2. **APNIC:** Kawasan Asia Pasifik (termasuk Indonesia).
3. **ARIN:** Kawasan Amerika Utara.
4. **LACNIC:** Kawasan Amerika Latin dan Karibia.
5. **RIPE NCC:** Kawasan Eropa, Timur Tengah, dan Asia Tengah.

---

## 5. Segmentasi Jaringan (Network Segmentation)

### A. Broadcast Domain dan Masalahnya
Banyak protokol jaringan fundamental yang bergantung penuh pada pengiriman paket data bertipe *broadcast* atau *multicast* (misalnya: protokol **ARP** untuk pemetaan MAC address atau proses **DHCP Discover** untuk mencari letak server IP otomatis).

Perangkat **Switch** di jaringan LAN berfungsi meneruskan lalu lintas *broadcast* ke seluruh port interface aktif yang dimilikinya (kecuali port asal paket tersebut datang). Satu-satunya perangkat interkoneksi utama yang secara bawaan bertugas membatasi dan menghentikan pengiriman paket broadcast agar tidak menyebar ke area luar jaringan lain adalah **Router**. Setiap interface fisik pada router bertindak sebagai batas akhir pembatas dari sebuah **Broadcast Domain**.

Masalah utama pada struktur *Broadcast Domain* berskala terlalu besar (misal satu segmen jaringan berisi ratusan hingga ribuan perangkat) adalah kemunculan **excessive broadcast** (lalu lintas broadcast berlebihan) yang menghabiskan bandwidth jaringannya dan menurunkan performa pemrosesan CPU di setiap *end-device*.

### B. Solusi Subnetting
Solusi mengatasi masalah tersebut adalah memperkecil ukuran broadcast domain dengan memecah satu jaringan besar menjadi sub-jaringan yang lebih kecil, melalui proses yang disebut dengan **Subnetting**.

Sebagai contoh, alokasi awal satu segmen jenuh `172.16.0.0/16` yang melayani 400 pengguna dalam satu broadcast domain, dipecah (didistribusikan ulang) ke dalam dua sub-jaringan yang lebih ringkas dan terpisah, contohnya:
* `172.16.0.0/24` (melayani maksimum 200 pengguna)
* `172.16.1.0/24` (melayani maksimum 200 pengguna)

### C. Alasan Utama Segmentasi Jaringan
Segmentasi jaringan memberikan beberapa keuntungan penting dalam operasional pengelolaan infrastruktur IT:
1. **Peningkatan Kinerja Jaringan:** Mengurangi akumulasi kepadatan lalu lintas (*traffic data*) yang berlebihan sehingga performa transmisi lebih optimal.
2. **Penerapan Kebijakan Keamanan (Security):** Memudahkan administrator jaringan memisahkan hak akses dan menerapkan filter firewall antar subnet yang berbeda.
3. **Isolasi Masalah:** Mempersempit cakupan perangkat yang terdampak apabila terjadi anomali atau gangguan lalu lintas jaringan (seperti akibat fenomena *broadcast storm* atau serangan malware).

### D. Metode Pengelompokan Subnetting
Dalam praktiknya, pemisahan subnet dapat diatur berdasarkan kriteria taktis organisasi berikut:
* **Berdasarkan Lokasi Geografis / Fisik:** Contohnya membagi alokasi IP berdasarkan lantai gedung kerja (`LAN 1: Lantai 1`, `LAN 2: Lantai 2`, dst).
* **Berdasarkan Grup Organisasi / Fungsi Kerja:** Contohnya memisahkan akses departemen kerja di perusahaan (`Subnet Administrasi`, `Subnet Kemahasiswaan`, `Subnet HRD`, `Subnet Akuntansi`).
* **Berdasarkan Tipe Perangkat (Device Type):** Contohnya memisahkan alokasi antara perangkat pengguna umum dengan perangkat infrastruktur inti internal (`Subnet khusus Host PC/Laptop`, `Subnet khusus Seluruh Server`, `Subnet khusus Printer Jaringan`).
