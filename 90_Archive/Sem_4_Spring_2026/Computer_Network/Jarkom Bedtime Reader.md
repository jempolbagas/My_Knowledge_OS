---
title: "Jarkom Bedtime Reader: Dongeng Santai Pembina Mental Model (Week 7-14)"
course: Jaringan Komputer
tags: ["#computer-networks", "#bedtime-reading", "#analogy", "#conceptual"]
aliases: ["Dongeng Jarkom", "Bacaan Santai Jaringan Komputer"]
created: "2026-06-25"
---

# Jarkom Bedtime Reader: Dongeng Santai Pembina Mental Model (Week 7 - Week 14)

Halo! Capek abis ngeliat deretan biner, subnetting mask, sama baris kode Python yang bikin pening? Tarik selimut, rebahan yang nyaman, dan mari kita obrolin konsep-konsep Jaringan Komputer lewat dongeng santai. 

Di sini, kita tidak cuma membaca dongeng analogi saja. Di setiap akhir cerita, ada kotak informasi khusus **"Riilnya di Jaringan"** yang memuat definisi formal, nomor port, nama protokol, status koneksi, dan perintah CLI asli. Jadi, sambil santai membangun intuisi, kamu juga otomatis menghafal jawaban teknis jika besok tipe ujiannya adalah **isian singkat atau esai**. 🛌✨

---

## 📬 Dongeng 1 (Week 7 & 8): Rumah IPv4, NAT si Penjaga Kos, dan Kapling Jaringan

Bayangkan dunia jaringan komputer itu adalah sebuah **Kota Pos Raksasa**.

Setiap perangkat komputer (HP, laptop, server) adalah **rumah-rumah** di kota tersebut. Biar kurir pos (yang kita sebut **Router**) bisa ngirim surat kita tanpa nyasar, setiap rumah kudu punya nomor alamat yang unik. Di era awal, kota ini menggunakan sistem nomor rumah yang disebut **IPv4**. 

Sistem IPv4 ini memakai panjang nomor 32-bit. Di dunia nyata, ini kayak sistem plat nomor kendaraan yang terbatas. Dulu, sang perancang kota mikir, *"Ah, 4 miliar alamat mah cukup banget buat seumur hidup!"*. Tapi mereka lupa kalau di masa depan, satu orang tidak cuma punya satu PC, tapi juga punya HP, jam tangan pintar, lampu pintar, bahkan kulkas pintar yang semuanya butuh nomor rumah! Walhasil, nomor rumah IPv4 di kota ini **habis lho!**

### NAT: Si Penjaga Kos-Kosan Pintar
Karena nomor rumah habis tapi penduduk baru terus berdatangan, para insinyur menciptakan sistem kos-kosan bernama **NAT (Network Address Translation)**.

Bayangkan satu rumah besar menyewa satu nomor IP publik resmi (misal: Jalan Mawar No. 10). Di dalam rumah itu, ada puluhan kamar kos. Penjaga kos memberikan nomor internal sendiri ke setiap kamar (misal: Kamar 101, Kamar 102). Nomor internal ini adalah **Private IP** (seperti blok `192.168.x.x`). 
* Kalau kamu yang ada di Kamar 101 mau belanja online, paket belanjaanmu dikirim dengan alamat asal Jalan Mawar No. 10.
* Kurir paket cuma tahu Jalan Mawar No. 10. Begitu paket sampai di gerbang, **Penjaga Kos (NAT Router)** memeriksa catatannya: *"Oh, paket ini ternyata punya si Kamar 101!"*, lalu meneruskannya ke kamarmu.
* Sistem ini menyelamatkan kita dari kepunahan IP, tapi bikin komunikasi jadi ribet karena orang luar tidak bisa langsung menge-bel pintu kamarmu secara langsung tanpa lewat si penjaga kos.

### Subnetting: Membagi Kapling Tanah
Bagaimana dengan **Subnetting**? Bayangkan kamu punya sebidang tanah raksasa yang belum disekat. Kalau ada 1.000 orang tinggal di sana tanpa sekat, suasana bakal bising banget! Setiap kali ada satu orang teriak (**Broadcast Packet**), 999 orang lainnya bakal keganggu tidurnya.

Makanya, kita lakukan **Subnetting**—yaitu membangun tembok-tembok pembatas untuk membagi tanah raksasa tadi menjadi kompleks-kompleks perumahan kecil (subjaringan). Tembok pembatas ini dijaga oleh pintu gerbang (**Default Gateway**) yang dikelola oleh Router. Sekarang, kalau di Kompleks A ada yang teriak, suaranya cuma kedengaran di Kompleks A saja. Kompleks B dan C tetap tenang dan bisa tidur nyenyak!

> [!info] **Riilnya di Jaringan (Konsep Teknis Asli untuk Ujian Isian):**
> * **Internet Protocol Version 4 (IPv4):** Protokol Layer 3 yang menggunakan pengalamatan **32-bit** (4 Byte) yang ditulis dalam desimal bertitik (*dotted decimal*). Menyediakan maksimal sekitar $2^{32} \approx 4,29 \text{ miliar}$ alamat.
> * **Network portion vs Host portion:** Batas pemisah antara porsi jaringan dan porsi host ditentukan oleh bit biner `1` pada **Subnet Mask**. Komputer mencari Network ID menggunakan operasi logika biner **AND** (ANDing) antara IP Address dan Subnet Mask.
> * **Private IP Address (RFC 1918):** Rentang IP khusus untuk jaringan lokal internal yang tidak dirutekan (*non-routable*) di internet publik:
>   - **Kelas A:** `10.0.0.0/8` (`10.0.0.0` s.d. `10.255.255.255`)
>   - **Kelas B:** `172.16.0.0/12` (`172.16.0.0` s.d. `172.31.255.255`)
>   - **Kelas C:** `192.168.0.0/16` (`192.168.0.0` s.d. `192.168.255.255`)
> * **IP Penggunaan Spesial:**
>   - **Loopback Address (`127.0.0.0/8`):** Digunakan untuk menguji tumpukan (*stack*) TCP/IP internal mesin itu sendiri tanpa mengirim data ke kartu jaringan fisik.
>   - **APIPA / Link-Local (`169.254.0.0/16`):** IP otomatis mandiri yang diberikan oleh OS ketika komputer gagal menghubungi DHCP Server.
> * **3 Jenis Alamat dalam Subnet:**
>   - **Network ID:** Alamat pengenal segmen jaringan (bit host `0` semua).
>   - **Broadcast ID:** Alamat untuk mengirim paket ke semua host di subnet (bit host `1` semua).
>   - **Host ID Range:** Alamat valid yang bisa dipasang di perangkat komputer.
>   - *Rumus Host Valid:* $2^{(32 - \text{Prefix Length})} - 2$.
> * **Subnetting Tradisional vs VLSM:**
>   - **Subnetting Tradisional:** Membagi satu blok IP menjadi subnet-subnet berukuran sama rata.
>   - **VLSM (Variable Length Subnet Mask):** Membagi subjaringan dengan ukuran bervariasi sesuai kebutuhan riil host demi menghemat IP.
>   - *Aturan VLSM:* Kebutuhan subjaringan wajib diurutkan secara **descending (dari kebutuhan host terbesar ke terkecil)** sebelum dihitung.
>   - *Trik Magic Number:* $\text{Magic Number} = 256 - \text{Mask Desimal Oktet Terakhir}$. Kelipatan angka ini menentukan batas-batas Network Address berikutnya.

---

## 🚀 Dongeng 2 (Week 9a & 9b): Era Galactic IPv6 dan Rumah yang Membangun Dirinya Sendiri

Karena kota IPv4 sudah terlalu padat dan pengap dengan sistem kos-kosan NAT, para perancang membangun **Planet Megapolitan Baru** yang bernama **IPv6**.

Planet ini luasnya minta ampun! Dengan panjang alamat 128-bit, jumlah alamat uniknya ada 340 desiliun. Analogi populernya, angka ini cukup buat ngasih IP address unik ke setiap butir pasir di seluruh bumi, bahkan masih sisa banyak! Di planet baru ini, kita tidak butuh lagi penjaga kos (NAT). Semua perangkat, dari HP-mu sampai sensor lampu jalan, bisa punya alamat GPS publiknya sendiri secara langsung. Komunikasi kembali menjadi *end-to-end* yang cepat dan bebas hambatan.

### SLAAC: Rumah yang Membangun Alamatnya Sendiri
Hebatnya lagi, di dunia IPv6, perangkat kita tidak perlu manja nungguin server DHCP buat ngasih alamat IP. Begitu dicolok ke jaringan, perangkat kita bakal teriak ke router terdekat (**Router Solicitation**): *"Halo, aku baru bangun nih! Aku ada di kompleks mana ya?"*

Router bakal membalas (**Router Advertisement**): *"Halo anak muda! Kamu ada di kompleks `2001:db8:acad:1::/64`."*

Setelah tahu alamat kompleksnya, si perangkat bakal menggunakan metode **SLAAC** untuk membuat nomor rumahnya sendiri. Bagaimana caranya biar tidak bentrok sama tetangga? Perangkat menggunakan cetak biru fisik bawaan lahirnya, yaitu **MAC Address** kartu jaringannya. 
* MAC Address ini dibelah jadi dua di tengah-tengah.
* Disisipkan kode rahasia `fffe` di sela-sela pembelahan.
* Lalu bit ke-7 dari kirinya dibalik (proses menari **EUI-64**). 
* Gabungkan dengan alamat kompleks dari router, dan taraaa! Jadilah alamat IP unik dunia yang siap dipakai. Praktis banget, kan? Nggak ada lagi drama rebutan IP bentrok!

> [!info] **Riilnya di Jaringan (Konsep Teknis Asli untuk Ujian Isian):**
> * **IPv6 Address:** Protokol Layer 3 menggunakan pengalamatan **128-bit** (16 Byte) yang ditulis menggunakan **8 hextet bilangan heksadesimal** dipisahkan titik dua (`:`). Tiap 1 digit hex $= 4\text{ bit biner}$ (nibble).
> * **Strategi Transisi IPv4 ke IPv6:**
>   - **Dual Stack:** Perangkat menjalankan tumpukan protokol IPv4 dan IPv6 secara bersamaan.
>   - **Tunneling:** Membungkus paket IPv6 di dalam payload header IPv4 untuk melewati jaringan IPv4 murni.
>   - **Translation (NAT64):** Menerjemahkan header paket IPv6 menjadi paket IPv4 secara dinamis di router gateway.
> * **Aturan Kompresi Penulisan IPv6:**
>   - *Aturan 1:* Membuang angka nol di depan (*leading zeros*) pada hextet. (Contoh: `0db8` menjadi `db8`).
>   - *Aturan 2:* Mengganti kelompok hextet berisi nol semua yang berurutan dengan tanda titik dua ganda (`::`). Hanya boleh digunakan **maksimal satu kali** per alamat IP untuk menghindari ambiguitas dekompresi.
> * **Tipe Komunikasi IPv6:** Unicast (one-to-one), Multicast (one-to-many), dan Anycast (one-to-nearest). **Tidak ada broadcast** di IPv6.
> * **Dua Jenis IP Unicast Utama pada Interface:**
>   - **Global Unicast Address (GUA):** IP Publik global internet. Menggunakan rentang prefix **`2000::/3`** (hextet pertama berkisar antara `2000` s.d. `3fff`). Memiliki struktur: *Global Routing Prefix (48 bit) + Subnet ID (16 bit) + Interface ID (64 bit)*.
>   - **Link-Local Address (LLA):** IP komunikasi internal satu LAN lokal yang bersifat *non-routable*. Menggunakan rentang prefix **`fe80::/10`** (praktiknya selalu berawalan `fe80::/64`). LLA wajib dimiliki setiap interface IPv6 dan digunakan sebagai alamat **Default Gateway** bagi client.
> * **Metode Autokonfigurasi Dinamis (ICMPv6):**
>   - **SLAAC:** Host menggunakan prefix dari Router Advertisement (RA) dan membuat Interface ID sendiri (via EUI-64 atau acak). Tidak melibatkan DHCPv6 Server sama sekali.
>   - **Stateless DHCPv6:** Host membuat IP sendiri lewat SLAAC, tetapi meminta DNS Server dari DHCPv6.
>   - **Stateful DHCPv6:** Host menyerahkan seluruh konfigurasi IP dan DNS ke DHCPv6 Server (mirip cara kerja DHCPv4).
> * **Algoritma EUI-64:** MAC Address 48-bit (12 digit hex) dibelah di tengah, disisipkan nilai heksadesimal **`FFFE`** di tengahnya, lalu **membalik bit ke-7** (Universal/Local bit) pada oktet pertama. (Misal: hex `00` biner `00000000` dibalik bit ke-7 menjadi `00000010` hex `02`).
> * **Solicited-Node Multicast Address:** Digunakan untuk proses Neighbor Discovery. Menggabungkan prefix tetap **`ff02::1:ff00:0/104`** dengan **24-bit terakhir (6 digit hex terakhir)** dari alamat IP unicast target. (Template akhir: `ff02::1:ffXX:XXXX`).
> * **Cisco CLI Command Aktifkan Perutean IPv6:** Router **wajib** mengeksekusi perintah konfigurasi global: `ipv6 unicast-routing`. Jika lupa, router tidak akan meneruskan paket IPv6 dan tidak mengirim pesan RA.
> * **Prefix Subnetting Standar IPv6:** Selalu menggunakan prefix **`/64`** untuk subjaringan LAN lokal agar autokonfigurasi SLAAC tidak rusak.

---

## 🏥 Dongeng 3 (Week 10): ICMP si P3K Jaringan dan Detektif Ping/Traceroute

Di kota pos raksasa ini, kadang-kadang kecelakaan jaringan bisa terjadi. Ada kabel yang putus, ada rumah yang roboh, atau ada paket yang terlalu berat sampai jembatannya ambruk. Siapa yang bertugas melaporkan kecelakaan ini? Dialah **ICMP (Internet Control Message Protocol)**, sang petugas medis dan pemberi laporan darurat di Layer 3.

IP address itu ibarat kurir yang cuek bebek. Tugasnya cuma bawa paket dan jalan terus. Kalau di tengah jalan ada jembatan putus, si kurir IP bakal menge-drop paket itu ke jurang begitu saja tanpa ngabarin si pengirim. Untungnya, di samping kurir IP selalu ada petugas **ICMP** yang siap mencatat kejadian itu dan mengirim surat laporan medis (**Error Reporting**) kembali ke si pengirim asli: *"Woi, paketmu terpaksa dibuang di Router B karena jalan menuju tujuan tidak ditemukan (Destination Unreachable)!"*

### Path MTU Discovery (PMTUD): Uji Tinggi Jembatan
ICMP juga punya trik pintar bernama **PMTUD**. Bayangkan kamu mau ngirim truk kontainer melewati rute berlereng gunung yang banyak jembatan layangnya, tapi kamu tidak tahu berapa tinggi maksimal jembatan terendah di rute itu.

Caranya: Kamu pasang stiker di trukmu bertuliskan **Don't Fragment (DF) = 1** (Jangan bongkar muatan truk ini!). 
* Kamu kirim truk berukuran besar.
* Begitu truk sampai di jembatan layang yang agak rendah di Router C, truknya tidak bisa lewat. Karena stikernya bilang tidak boleh dibongkar, Router C terpaksa menghancurkan truk tersebut dan mengirim laporan ICMP: *"Trukmu terlalu tinggi! Jembatanku cuma muat tinggi X!"*
* Kamu ganti trukmu dengan ukuran X, lalu kirim lagi. Proses ini diulangi sampai trukmu bisa lewat dengan aman sampai tujuan tanpa mentok lagi.

### Detektif Ping dan Traceroute
Petugas ICMP ini juga yang menjadi motor di balik alat detektif favorit kita: **Ping** dan **Traceroute**.
* **Ping:** Ini kayak kamu melempar bola tenis ke tembok tetangga sambil teriak *"Halo!"* (**Echo Request**). Kalau temboknya memantulkan bola itu kembali ke kamu dengan suara *"Halo juga!"* (**Echo Reply**), kamu tahu tetanggamu ada di rumah dan sehat walafiat.
* **Traceroute:** Ini trik detektif paling seru. Kamu mau tahu rute jalan mana saja yang dilewati paketmu menuju Google. Kamu kirim paket pertama dengan **TTL (Time to Live) = 1** (Paket ini cuma boleh hidup melewati 1 gerbang pos). Router pertama yang menerima paket ini bakal mengurangi TTL-nya menjadi 0, membuang paket tersebut karena "waktunya habis", dan dengan sopan mengirim surat belasungkawa ICMP ke kamu: *"Maaf, paketmu mati di gerbang saya (IP Router 1)."* 
  Kamu catat IP itu. Lalu kamu kirim paket kedua dengan **TTL = 2**. Paket lewat gerbang 1, sisa TTL = 1. Paket masuk gerbang 2, TTL dikurangi jadi 0, paket mati lagi di sana. Gerbang 2 mengirim surat belasungkawa: *"Paketmu mati di tempat saya (IP Router 2)."* Kamu ulangi ini terus sampai paketmu akhirnya sukses menyentuh server Google. Kreatif banget, kan?

> [!info] **Riilnya di Jaringan (Konsep Teknis Asli untuk Ujian Isian):**
> * **Internet Control Message Protocol (ICMP):** Protokol kontrol di Layer 3 yang bertugas mengirimkan umpan balik (*feedback*) operasional dan laporan kesalahan (*error reporting*) jaringan.
> * **Format Header ICMP:** Memiliki ukuran **8 Byte** yang terdiri dari field: **Type** (1 Byte - kategori pesan), **Code** (1 Byte - detail pesan), dan **Checksum** (2 Byte - deteksi kerusakan header).
> * **Klasifikasi Tipe & Kode ICMP Kritis (Sering Keluar Ujian):**
>   - **Type 3 (IPv4) / Type 1 (IPv6):** *Destination Unreachable* (Tujuan Tidak Dapat Dijangkau).
>     - *Code 0:* Net Unreachable (Rute ke jaringan tidak ada di routing table).
>     - *Code 1:* Host Unreachable (Target fisik mati/kabel putus).
>     - *Code 3:* Port Unreachable (Protokol transport/aplikasi tujuan mati - khas pada UDP).
>   - **Type 11:** *Time Exceeded* (TTL paket telah habis menjadi 0 saat dikurangi router).
>   - **Type 8 / Type 128:** *Echo Request* (Pesan Ping keluar).
>   - **Type 0 / Type 129:** *Echo Reply* (Balasan pesan Ping masuk).
> * **Path MTU Discovery (PMTUD):** Mekanisme mendeteksi ukuran MTU (*Maximum Transmission Unit*) terkecil di sepanjang jalur routing tanpa fragmentasi dengan menyetel bit **DF (Don't Fragment) = 1** pada header IP. Router yang mentok akan membalas dengan ICMP **Type 3 Code 4** (Fragmentation Needed).
> * **ICMPv6 Neighbor Discovery Protocol (NDP):** Pengganti fungsi ARP di IPv6 yang berjalan di atas ICMPv6 dengan 4 pesan utama:
>   - **Router Solicitation (RS - Tipe 133)** & **Router Advertisement (RA - Tipe 134)** untuk deteksi router.
>   - **Neighbor Solicitation (NS - Tipe 135)** & **Neighbor Advertisement (NA - Tipe 136)** untuk resolusi MAC address dan proses **Duplicate Address Detection (DAD)**.
> * **Diagnostik Ping vs Traceroute:**
>   - **Ping:** Menggunakan transaksi ICMP Echo Request dan Echo Reply untuk menguji konektivitas dan mengukur **RTT (Round Trip Time)**.
>   - **Traceroute:** Mengirim paket secara berurutan dengan menaikkan TTL secara bertahap ($1, 2, 3...$) untuk memicu balasan ICMP **Time Exceeded (Type 11)** dari setiap router di jalur data.
>   - *Perbedaan Sistem Operasi:* Windows (`tracert`) mengirim paket **ICMP Echo Request**, sedangkan Linux/Unix (`traceroute`) mengirim paket **UDP port tinggi (33434+)**.

---

## 🤝 Dongeng 4 (Week 11): TCP vs UDP (Kurir Premium vs Teriak Megafon)

Di Layer 4 (Transport Layer), ada dua raksasa yang menguasai pengiriman data dengan filosofi hidup yang bertolak belakang: **TCP** dan **UDP**.

```text
Filosofi TCP: "Biar lambat asal selamat, tertib, dan terdokumentasi dengan tanda tangan basah."
Filosofi UDP: "Pokoknya kirim! Cepat, tanpa beban, urusan sampai atau tidak itu takdir."
```

### Analogi TCP: Layanan Kurir Premium
TCP adalah layanan kurir paket pos tercatat yang super protektif. Sebelum ngirim surat cinta, TCP kudu bikin kesepakatan dulu lewat ritual **Three-Way Handshake**:
1. Kamu kirim surat pembuka: *"Halo, aku mau ngobrol nih! Denger suaraku tidak? (SYN)"*
2. Lawan bicaramu membalas: *"Halo juga! Iya denger kok. Suaraku denger tidak? (SYN-ACK)"*
3. Kamu jawab lagi: *"Sip, denger jelas! Yuk kita mulai ngobrol. (ACK)"*

Setelah sepakat, setiap paket yang dikirim bakal dikasih nomor urut (**Sequence Number**). Penerima wajib membalas dengan **Acknowledgment (ACK)** yang mengonfirmasi bahwa paket dengan nomor sekian sudah diterima dengan selamat. Kalau ada paket yang hilang di jalan, pengirim bakal tahu karena tidak menerima ACK hingga batas waktu tertentu (**RTO**), dan otomatis mengirim ulang paket yang hilang tadi.

TCP juga punya fitur **Flow Control** agar tidak menenggelamkan penerima dalam banjir data. Penerima bakal teriak: *"Woi, memoriku sisa X nih (Window Size), jangan kirim lebih dari itu ya!"*. TCP juga mengatur **Congestion Control** (Kontrol Kemacetan). Jika TCP mendeteksi ada kemacetan di internet (lewat paket yang hilang), TCP bakal langsung ngerem kecepatannya secara drastis (Slow Start) lalu menaikkannya perlahan lagi demi menjaga ketertiban lalu lintas.

### Analogi UDP: Teriak Lewat Megafon
Di sisi lain, UDP adalah cowok cuek yang berteriak lewat megafon di tengah stadion yang ramai. UDP tidak peduli apakah kamu mendengar suaranya, apakah kamu sedang ke toilet, atau apakah suaranya terdistorsi angin. UDP langsung memancarkan suaranya begitu saja. 

UDP tidak butuh jabat tangan awal, tidak punya nomor urut, tidak melacak kehilangan data, dan tidak peduli dengan kemacetan. 
* *Kenapa kita masih butuh UDP?* Karena UDP **sangat cepat dan ringan!** Header UDP cuma 8 byte, bandingkan dengan TCP yang minimal 20 byte. 
* Untuk aplikasi real-time seperti game online (di mana kamu butuh posisi karakter musuh ter-update *sekarang juga*, persetan dengan posisi 2 detik lalu yang sempat lag) atau panggilan telepon VoIP, UDP adalah raja yang tak tergantikan.

> [!info] **Riilnya di Jaringan (Konsep Teknis Asli untuk Ujian Isian):**
> * **User Datagram Protocol (UDP):** Protokol transport **Connectionless** dan **Unreliable** (tidak menjamin data sampai). Memiliki ukuran header **tetap 8 Byte** dengan 4 field: *Source Port, Destination Port, Length, dan Checksum*.
> * **Transmission Control Protocol (TCP):** Protokol transport **Connection-Oriented** dan **Reliable** (menjamin data sampai). Memiliki ukuran header **minimal 20 Byte** yang memuat nomor port, *Sequence Number (SEQ)*, *Acknowledgment Number (ACK)*, serta Flags bit kontrol.
> * **Siklus Hidup Koneksi TCP (States):**
>   - **Inisiasi (Three-Way Handshake):** `LISTEN` (Server pasif) $\rightarrow$ `SYN_SENT` (Klien kirim SYN) $\rightarrow$ `SYN_RCVD` (Server terima SYN, kirim SYN-ACK) $\rightarrow$ `ESTABLISHED` (Klien terima SYN-ACK, kirim ACK final. Sesi data dimulai).
>   - **Terminasi (Four-Way Handshake):** `FIN_WAIT_1` $\rightarrow$ `CLOSE_WAIT` (Penerima pasif bersiap tutup) $\rightarrow$ `FIN_WAIT_2` $\rightarrow$ `LAST_ACK` $\rightarrow$ `TIME_WAIT` $\rightarrow$ `CLOSED`.
>   - *State TIME_WAIT:* State penutupan aktif berdurasi **2 * MSL (Maximum Segment Lifetime)** untuk memastikan ACK terakhir diterima dengan selamat oleh penerima dan membersihkan segmen lama agar tidak menabrak koneksi baru.
> * **Kontrol Aliran & Kemacetan TCP:**
>   - **Flow Control (Sliding Window):** Pengirim menyesuaikan laju pengiriman berdasarkan kapasitas buffer kosong penerima yang dikabarkan lewat field **Window Size** di header TCP.
>   - **Congestion Control (Cwnd):** Pengirim melacak kemacetan jaringan melalui ukuran variabel **Congestion Window (cwnd)**.
>   - **Tahapan Congestion Control:**
>     1. **Slow Start:** cwnd naik secara **eksponensial** setiap RTT hingga menyentuh batas **ssthresh**.
>     2. **Congestion Avoidance:** cwnd naik secara **linear** ($+1$ MSS per RTT) setelah melampaui ssthresh.
>     3. **Fast Retransmit:** Mengirim ulang segmen secara langsung tanpa menunggu timer RTO habis jika mendeteksi **3 Duplicate ACKs**.
>     4. **Fast Recovery:** Fase pasca Fast Retransmit (TCP Reno) di mana ssthresh diturunkan setengahnya dan langsung melanjutkan ke fase Congestion Avoidance (tidak mengulang dari Slow Start).

---

## ☎️ Dongeng 5 (Week 12): Memahami Soket Python Lewat Analogi Telepon Kantor

Sekarang mari kita turun ke dunia pemrograman jaringan. Apa sih sebenarnya **Socket** itu?

Bayangkan **Socket** itu adalah **pesawat telepon** di mejamu. Socket adalah jembatan penghubung (API) antara aplikasimu dengan kabel-kabel telepon bawah tanah (protokol TCP/IP di kernel sistem operasi).

### Alur Kerja Socket TCP Server (Resepsionis Kantor):
1. **`socket()`**: Kantor membeli unit pesawat telepon baru dari toko.
2. **`bind()`**: Kantor mendaftarkan nomor telepon resmi ke perusahaan telekomunikasi (misal: "Telepon ini nomornya adalah `192.168.1.10` port `80`").
3. **`listen()`**: Resepsionis menekan tombol "Call Waiting" agar telepon bisa menerima antrean panggilan masuk dari luar.
4. **`accept()`**: Resepsionis menunggu telepon berdering. Begitu ada telepon masuk dari klien, resepsionis mengangkatnya, menyapa hangat, lalu **mengalihkan panggilan tersebut ke saluran ekstensi baru khusus** untuk mengobrol berdua dengan klien tersebut. Pesawat telepon utama di meja resepsionis kembali bebas menunggu panggilan klien berikutnya.
5. **`send()` & `recv()`**: Mengobrol bertukar suara (mengirim dan menerima bytes).
6. **`close()`**: Menutup gagang telepon setelah selesai mengobrol.

### Alur Kerja Socket TCP Client (Penelepon):
1. **`socket()`**: Klien membeli HP baru.
2. **`connect()`**: Klien menekan nomor telepon server dan menekan tombol panggil. Proses ini memicu Three-Way Handshake di latar belakang. Begitu terhubung, percakapan dimulai.

### Tips Misteri Ujian: Mengapa ada "Address already in use"?
Pernah mengalami error ini pas praktikum pemrograman soket Python? 
Ini terjadi karena setelah server dimatikan secara paksa, sistem operasi masih menahan port tersebut dalam status **`TIME_WAIT`** selama beberapa menit (Four-Way Handshake pemutusan TCP belum selesai sempurna). OS sengaja menahan port itu agar paket-paket lama yang tersesat di internet tidak nyasar masuk ke koneksi baru.
* *Solusinya:* Kita memanggil perintah sakti `SO_REUSEADDR` untuk memaksa sistem operasi melepaskan port tersebut seketika agar kita bisa langsung menjalankan server kembali tanpa menunggu timer OS habis.

> [!info] **Riilnya di Jaringan (Konsep Teknis Asli untuk Ujian Isian):**
> * **Socket API:** Antarmuka logika pemrograman aplikasi (API) yang disediakan sistem operasi untuk membolehkan aplikasi berinteraksi dengan protokol transport (Layer 4) di dalam kernel.
> * **Urutan Panggilan System Call (API Lifecycle) Ujian:**
>   - **TCP Server:** `socket()` $\rightarrow$ `bind()` $\rightarrow$ `listen()` $\rightarrow$ `accept()` [fungsi blocking, mengembalikan soket koneksi baru khusus klien] $\rightarrow$ `recv()` / `send()` $\rightarrow$ `close()`.
>   - **TCP Client:** `socket()` $\rightarrow$ `connect()` [memicu handshake 3-way] $\rightarrow$ `send()` / `recv()` $\rightarrow$ `close()`.
>   - **UDP Server:** `socket()` $\rightarrow$ `bind()` $\rightarrow$ `recvfrom()` [blocking, mengembalikan data & tuple IP/port asal] $\rightarrow$ `sendto()` $\rightarrow$ `close()`.
>   - **UDP Client:** `socket()` $\rightarrow$ `sendto()` $\rightarrow$ `recvfrom()` $\rightarrow$ `close()`.
> * **Parameter Socket Python (`AF_INET` & `SOCK_STREAM`):**
>   - `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` membuat soket **IPv4 TCP**.
>   - `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` membuat soket **IPv4 UDP**.
> * **Aturan Pengiriman Tipe Data Jaringan:** Data dikirim dalam format **Bytes**, bukan String biasa.
>   - *Sebelum kirim:* String kudu diubah ke bytes via `.encode('utf-8')`.
>   - *Setelah terima:* Bytes diubah kembali ke string via `.decode('utf-8')`.
> * **Mengatasi Error Port Terkunci (Address already in use):** Menggunakan opsi socket reuse address sebelum melakukan bind di server:
>   `server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`.

---

## 🍽️ Dongeng 6 (Week 13): Restoran Layer Aplikasi (DNS, DHCP, HTTP/HTTPS, & Email)

Jika layer-layer di bawahnya bertugas mengurus pengiriman fisik paket, **Layer Aplikasi (Layer 5-7 OSI)** adalah **pelayan restoran** yang menyajikan hidangan langsung ke hadapan pelanggan.

### DNS: Buku Telepon Kuning Raksasa
Manusia itu pintar mengingat nama (seperti `google.com`), tapi sangat payah mengingat angka (seperti `142.251.12.100`). Komputer sebaliknya. Makanya kita butuh **DNS (Domain Name System)**, buku telepon raksasa yang terdistribusi di internet.
* Saat kamu mengetik `uns.ac.id`, komputer bertanya ke Local Resolver DNS-mu (**Recursive Query**): *"Aku kudu nyari jawaban mutlak nih, tolong cariin IP domain ini!"*
* Local Resolver, jika belum tahu jawabannya, akan melakukan investigasi mandiri (**Iterative Query**) dengan bertanya bertahap:
  1. Tanya ke **Root Server**: *"Eh, tahu IP `uns.ac.id` tidak?"* $\rightarrow$ Root menjawab: *"Tidak tahu, tapi ini alamat server `.id` (TLD Server), coba tanya ke sana."*
  2. Tanya ke **TLD Server (.id)**: *"Eh, tahu IP `uns.ac.id`?"* $\rightarrow$ TLD menjawab: *"Tidak tahu juga, tapi ini alamat Authoritative Server milik UNS (`ns1.uns.ac.id`), coba tanya ke sana."*
  3. Tanya ke **Authoritative Server UNS**: *"Eh, tahu IP `uns.ac.id`?"* $\rightarrow$ UNS menjawab: *"Ya tahu lah, ini IP resminya: `X.X.X.X`!"*
* Local Resolver memberikan IP itu ke komputermu, dan browser-mu bisa membuka web kampus dengan sukses.

### DHCP: Resepsionis Hotel Pembagi Kunci
Saat kamu masuk ke lobi hotel (terhubung ke Wi-Fi cafe), kamu tidak bisa langsung masuk kamar tanpa kunci. Kamu menghampiri meja resepsionis (**DHCP Server**) untuk meminta kamar lewat ritual **D-O-R-A**:
1. **Discover (Klien teriak):** *"Ada resepsionis di sini? Aku butuh kunci kamar kosong!"*
2. **Offer (Resepsionis menawarkan):** *"Ada! Ini kunci Kamar 305 lagi kosong buat kamu."*
3. **Request (Klien memesan):** *"Oke, aku ambil Kamar 305 ya!"* (Klien teriak keras agar resepsionis lain di lobi tahu kamarnya sudah laku).
4. **Acknowledge (Resepsionis mencatat):** *"Sip! Kamar 305 resmi atas namamu selama 24 jam ke depan (Lease Time)."*
* *Apa yang terjadi setelah 12 jam (50% Lease Time)?* Klien secara sopan menghampiri resepsionis asal (**T1 - Unicast**) untuk meminta perpanjangan sewa: *"Pak, boleh nambah sewa Kamar 305-nya?"*. Jika resepsionisnya tidur atau tidak membalas, klien akan menunggu hingga jam ke-21 (87.5% Lease Time) lalu berteriak keras ke seluruh staf hotel (**T2 - Broadcast**) mencari siapa saja resepsionis cadangan yang bisa memperpanjang sewanya.

### HTTP/1.1 vs HTTP/2 vs HTTP/3
* **HTTP/1.1 (Satu-satu):** Ini seperti pelayan restoran yang cuma bisa membawa satu piring pesanan setiap kali bolak-balik dari dapur ke mejamu. Sangat lambat karena piring kedua harus menunggu piring pertama sampai di mejamu (**Head-of-Line Blocking**).
* **HTTP/2 (Banyak Piring Sekaligus):** Pelayan sekarang memakai nampan besar sehingga bisa membawa banyak piring pesanan (gambar, teks, CSS) sekaligus dalam satu kali perjalanan (**Multiplexing**). Tapi sialnya, nampan ini dibawa melewati pintu dapur TCP. Jika pelayan tersandung di pintu dapur (1 paket TCP hilang), seluruh nampan tertahan di pintu dapur sampai masalahnya beres.
* **HTTP/3 (Nampan Mandiri QUIC):** Pelayan beralih menggunakan pintu dapur UDP melalui protokol **QUIC**. Sekarang, setiap piring pesanan dibawa oleh robot kecil masing-masing secara mandiri. Jika robot 1 jatuh tersandung, robot-robot lainnya tetap jalan terus menyajikan makanan ke mejamu tanpa terganggu sama sekali.

### HTTPS: Perisai Diplomat
HTTPS mengamankan HTTP lewat bantuan **SSL/TLS**. 
Bayangkan kamu mau mengirim pesan rahasia lewat kurir pos yang tidak bisa dipercaya.
* **Handshake Awal (Enkripsi Asimetris):** Kamu mengirim kotak peti terbuka dengan gembok yang kuncinya hanya kamu yang pegang (**Public Key**). Penerima memasukkan "kunci rahasia bersama" (**Symmetric Key**) ke dalam peti, mengunci gemboknya, lalu mengirim peti itu kembali ke kamu. Karena gemboknya terkunci dan kuncinya ada di tanganmu, tidak ada penyadap di jalan yang bisa membuka peti itu.
* **Percakapan Utama (Enkripsi Simetris):** Sekarang, kamu dan penerima sudah sama-sama memegang salinan "kunci rahasia bersama" tersebut. Kalian bisa saling mengirim pesan rahasia dengan gembok biasa secara cepat karena tidak perlu repot-repot bertukar kunci baru lagi.

> [!info] **Riilnya di Jaringan (Konsep Teknis Asli untuk Ujian Isian):**
> * **3 Layer Teratas Model OSI:** Digabung menjadi satu layer (**Application Layer**) pada model TCP/IP.
>   - **Session Layer (Layer 5):** Mengelola sesi komunikasi. Memiliki fitur penting **Checkpointing & Synchronization** untuk menjaga kelangsungan transfer data besar saat jaringan labil.
>   - **Presentation Layer (Layer 6):** Representasi data. Melakukan **Serialisasi** (JSON/XML), **Enkripsi** (SSL/TLS), dan **Kompresi** (Lossless vs Lossy).
>   - **Application Layer (Layer 7):** Protokol antarmuka software (HTTP, DNS, SMTP).
> * **Domain Name System (DNS - Port 53 UDP/TCP):**
>   - **Recursive Query:** Query di mana resolver berkewajiban mencari jawaban IP mutlak sampai dapat.
>   - **Iterative Query:** Query rujukan bertahap dari resolver ke Root DNS, TLD DNS, dan Authoritative DNS.
>   - **Tipe Resource Records (RR):** **A** (IPv4), **AAAA** (IPv6), **CNAME** (Alias), **MX** (Mail server), **NS** (Name server), **TXT** (Teks tambahan).
> * **DHCP (Port 67/68 UDP):**
>   - **DORA Transaction:** **Discover** (Klien broadcast mencari server) $\rightarrow$ **Offer** (Server menawarkan parameter IP) $\rightarrow$ **Request** (Klien broadcast meminta IP yang dipilih) $\rightarrow$ **Acknowledge** (Server mengonfirmasi sewa IP).
>   - **Lease Renewal Status:**
>     - **T1 (50% lease time):** Klien mengirim DHCP Request secara **unicast** ke server asal.
>     - **T2 (87.5% lease time):** Klien mengirim DHCP Request secara **broadcast** ke seluruh jaringan mencari server cadangan.
> * **Evolusi Protokol Web (HTTP - Port 80, HTTPS - Port 443):**
>   - **HTTP/1.1:** Rentan terhadap **Head-of-Line (HoL) Blocking** di level aplikasi akibat satu request menyumbat request berikutnya di satu antrean.
>   - **HTTP/2:** Mengatasi HoL aplikasi dengan **Multiplexing** di atas satu koneksi TCP. Namun tetap terkena HoL di level transport jika ada paket TCP yang hilang di jaringan.
>   - **HTTP/3:** Berjalan di atas **UDP** menggunakan protokol **QUIC**. Mengeliminasi HoL transport sepenuhnya dan mendukung fitur **Connection Migration**.
>   - **HTTPS Security:** Mengamankan transaksi data dengan enkripsi **asimetris** (Public/Private Key) saat proses TLS Handshake awal, dan berganti ke enkripsi **simetris** (Session Key bersama) untuk lalu lintas data utama.
> * **Protokol Email:**
>   - **SMTP (Port 25 / Secure 587):** Protokol pengiriman email (*push* dari client ke server atau server ke server).
>   - **POP3 (Port 110 / Secure 995):** Protokol penarikan email (*pull*). Mengunduh email lalu menghapusnya dari server secara default.
>   - **IMAP (Port 143 / Secure 993):** Protokol penarikan email yang melakukan sinkronisasi salinan email dinamis lintas perangkat.

---

## 🛡️ Dongeng 7 (Week 14): Menjaga Kastil Keamanan Jaringan dari Gempuran Bandit

Bayangkan jaringan internal perusahaanmu adalah sebuah **Kastil Abad Pertengahan** yang menyimpan harta karun emas (data raksasa).

* **Threat (Ancaman):** Ini adalah kelompok **bandit** yang berkeliaran di luar hutan (aktor peretas) atau badai petir yang bisa menyambar kastil (bencana alam).
* **Vulnerability (Kerentanan):** Ini adalah **celah rahasia** di bawah tembok kastil yang rapuh, atau pintu gerbang belakang yang lupa dikunci oleh penjaga malam (salah konfigurasi / bug software).

### Pasukan Monster: Virus, Worm, dan Trojan
Peretas memiliki pasukan monster digital dengan cara kerja yang unik:
* **Virus:** Ini seperti **parasit tanaman**. Dia tidak bisa hidup sendiri dan butuh menempel pada inang (file exe atau dokumen word). Dia juga butuh manusia untuk menyebarkannya (kamu harus klik/buka file terinfeksi itu agar virusnya aktif dan merusak isi kastil).
* **Worm:** Ini adalah **hantu gentayangan** yang sangat mandiri. Dia tidak butuh inang dan tidak butuh interaksi manusia. Dia bisa mendeteksi pintu kastil yang terbuka di malam hari, merangkak masuk sendiri, menduplikasi diri menjadi jutaan hantu, lalu merangkak keluar lewat port jaringan untuk menyerang kastil-kastil tetangga dalam sekejap.
* **Trojan Horse:** Ini adalah **kado misterius** yang diletakkan di depan gerbang kastil. Penjaga kastil melihatnya dan berpikir, *"Wah, kado patung kuda yang indah! Mari kita bawa masuk ke dalam kastil."* (Kamu menginstal aplikasi game gratisan yang ternyata palsu). Begitu malam tiba dan semua orang tertidur, bandit-bandit di dalam patung keluar dan membukakan pintu gerbang utama kastil untuk pasukan peretas di luar.

### TCP SYN Flood: Taktik Pengepungan DoS
Bagaimana peretas melumpuhkan pertahanan kastil? Salah satu taktik licik mereka adalah **TCP SYN Flood**.
Peretas mengirimkan ribuan kurir ke gerbang kastil. Kurir itu mengetuk gerbang dan teriak: *"Halo, saya mau masuk! (SYN)"*. 

Penjaga gerbang membuka pintu, memberikan formulir pendaftaran, dan menunggu kurir menandatanganinya (**SYN-ACK**). 
Namun, kurir-kurir palsu tersebut langsung lari pergi begitu saja tanpa menandatangani formulir. Penjaga gerbang tetap berdiri memegang formulir kosong tersebut sambil menunggu si kurir kembali (**Half-Open state**). Karena ada ribuan kurir palsu yang melakukan ini bersamaan, semua penjaga gerbang sibuk memegang formulir kosong hingga kelelahan, dan ketika ada tamu nyata yang sah datang mengetuk pintu, gerbang kastil sudah tidak bisa dibuka lagi karena semua penjaga sudah mogok kerja (**Denial of Service**).

### Gerbang Keamanan: AAA Framework
Untuk mengamankan kastil, raja menerapkan sistem gerbang masuk **AAA**:
1. **Authentication (Autentikasi):** Penjaga gerbang bertanya: *"Siapa kamu? Tunjukkan KTP kastilmu!"* (Verifikasi password/token).
2. **Authorization (Otorisasi):** Setelah KTP terbukti sah, penjaga memberikan pin tamu berwarna kuning: *"Kamu hanya boleh berjalan-jalan di taman, dilarang masuk ke ruang penyimpanan harta emas!"* (Penetapan hak akses).
3. **Accounting (Audit):** Di setiap sudut kastil ada juru tulis yang mencatat semua langkahmu: *"Tamu A masuk ke taman pukul 10:00, Tamu A mencoba membuka pintu emas pukul 10:15 (Ditolak)"*. (Pencatatan log aktivitas).

### Penjaga Gerbang: Stateless, Stateful, dan Next-Gen Firewall
Kastil menempatkan penjaga gerbang yang disebut **Firewall**:
* **Stateless Firewall (Paling Cuek):** Penjaga gerbang ini hanya memeriksa daftar nama hitam. Setiap kali ada orang lewat, dia mencocokkan dengan daftar kertasnya tanpa peduli apakah orang itu baru saja keluar kastil atau bukan. Sangat mudah dikelabui.
* **Stateful Firewall (Pintar):** Penjaga gerbang ini mencatat siapa saja penghuni kastil yang baru keluar berbelanja ke pasar luar dalam sebuah buku catatan (**State Table**). Begitu ada orang dari luar mau masuk membawa belanjaan, penjaga memeriksa bukunya: *"Oh iya betul, kamu tadi penghuni kamar 202 yang keluar jam 9 pagi buat beli sayur. Silakan masuk!"*. Jika ada orang luar mencoba menyelinap masuk tanpa ada catatan keluar sebelumnya, penjaga langsung menangkapnya.
* **Next-Generation Firewall (Sangat Sakti):** Ini adalah penjaga gerbang dengan kekuatan sensor X-Ray (**Deep Packet Inspection**). Dia tidak cuma memeriksa KTP dan catatan keluar-masuk, tapi dia menggeledah sampai ke dalam isi tas belanjaanmu, mencium apakah ada racun tersembunyi, mendeteksi jika kamu menyamar sebagai tukang sayur padahal membawa senjata tajam, dan memantau gerak-gerik mencurigakan secara real-time. Kastil pun dijamin aman dari segala ancaman!

> [!info] **Riilnya di Jaringan (Konsep Teknis Asli untuk Ujian Isian):**
> * **Threat vs Vulnerability:**
>   - **Threat (Ancaman):** Segala hal potensial dari luar yang bisa merugikan sistem (malware, peretas, hacker).
>   - **Vulnerability (Kerentanan):** Kelemahan intrinsik dari dalam sistem (bug kode, salah konfigurasi password default).
> * **Perbedaan Virus, Worm, dan Trojan:**
>   - **Virus:** Butuh inang (*host file*) untuk menumpang hidup dan memerlukan tindakan aktif manusia untuk menyebar.
>   - **Worm:** Aplikasi mandiri (*standalone*) yang menyebar otomatis secara agresif melintasi port jaringan tanpa campur tangan manusia.
>   - **Trojan:** Mengelabui pengguna dengan menyamar sebagai program berguna padahal membawa payload berbahaya (*backdoor*).
> * **TCP SYN Flood DoS Attack:** Eksploitasi kegagalan jabat tangan 3 arah TCP dengan mengirim paket SYN massal memakai spoofed IP sehingga port server tertahan menggantung di state **`SYN_RCVD` (half-open)** hingga memori habis. Mitigasi: mengaktifkan fitur **SYN Cookies** pada firewall.
> * **AAA Security Framework:**
>   - **Authentication:** Verifikasi identitas (*siapa kamu?*).
>   - **Authorization:** Pembatasan hak akses (*apa yang boleh kamu lakukan?*).
>   - **Accounting:** Pencatatan log aktivitas audit (*apa saja yang sudah kamu lakukan?*).
> * **Protokol AAA: RADIUS vs TACACS+:**
>   - **RADIUS:** Menggunakan protokol transport **UDP**, hanya mengenkripsi field password, dan menggabungkan Authentication & Authorization.
>   - **TACACS+:** Menggunakan protokol transport **TCP (Port 49)**, mengenkripsi **seluruh isi paket data**, dan memisahkan modul AAA secara ketat dan modular.
> * **Teknologi Firewall:**
>   - **Stateless (Packet Filtering):** Menyaring paket secara independen berdasarkan informasi header Layer 3 & Layer 4 (IP & Port) tanpa mengingat status sesi koneksi.
>   - **Stateful Inspection:** Memiliki **State Table** untuk memantau status sesi aktif dan meloloskan paket respon dari luar hanya jika ada koneksi sah yang diinisiasi dari dalam LAN.
>   - **Next-Generation Firewall (NGFW):** Firewall modern terintegrasi dengan kemampuan **Deep Packet Inspection (DPI)** untuk menyaring isi payload aplikasi, **IPS** inline, dekripsi **SSL/TLS**, dan **Application Awareness**.

---

Nah, itulah dongeng lengkap petualangan kita di dunia Jaringan Komputer dari Week 7 sampai Week 14. 

Semoga semua analogi cerita ini menempel erat di kepalamu, membantu membentuk *mental model* yang kuat, dan membuatmu siap melibas ujian dengan santai. Sekarang, matikan layar gadgetmu, tarik napas dalam-dalam, dan selamat tidur! Semoga sukses ujiannya besok ya! 💤🚀🛡️
