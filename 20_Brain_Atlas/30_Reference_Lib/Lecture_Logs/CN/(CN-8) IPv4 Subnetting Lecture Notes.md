---
title: "(CN-8) IPv4 Subnetting Lecture Notes"
course: ""
tags: []
aliases: ["(CN-8) IPv4 Subnetting Lecture Notes"]
created: "2026-06-24"
---
# IPv4 Subnetting & VLSM Material Resource

**Mata Kuliah:** Jaringan Komputer Genap 2025/2026  
**Dosen:** Herdito Ibnu Dewangkoro  
**Program Studi:** Informatika UNS  

## 1. Konsep Dasar IPv4 Subnetting
Subnetting adalah proses yang membagi network menjadi bagian-bagian yang lebih kecil yang disebut subnet. Sebelum melakukan subnetting, ada dua hal yang harus diperhatikan: jumlah alamat host yang diperlukan untuk setiap network dan jumlah individual subnet yang dibutuhkan.

## 2. Perhitungan Subnetting
Perhitungan subnetting didasarkan pada peminjaman bit (borrowing bits) dari porsi host untuk dijadikan bagian dari porsi network. Berikut adalah rumus utamanya:
* **Jumlah Subnet:** Dihitung dengan 2^n, di mana n adalah jumlah bit network yang dipinjam.
* **Jumlah Host:** Dihitung dengan 2^h - 2, di mana h adalah jumlah sisa bit host. (Dua bit terakhir tidak dapat digunakan sebagai host address karena dialokasikan untuk Network Address dan Broadcast Address).

## 3. Studi Kasus Subnetting Tradisional

### Kasus A: Membuat 100 Subnet pada Prefix /16
Suatu perusahaan besar (large enterprise) memerlukan 100 subnet dan memiliki private address 172.16.0.0/16. Untuk mendapatkan 100 subnet, kita perlu meminjam 7 bit host (2^7 = 128 subnet). Hal ini mengubah prefix awal /16 menjadi prefix baru /23 (16 + 7).

### Kasus B: Membuat 1000 Subnet pada Prefix /8
Suatu Small ISP memerlukan 1000 subnet untuk klien yang memiliki network address 10.0.0.0/8. Persyaratan ini dapat dipenuhi dengan meminjam 10 bit host (2^10 = 1024 subnet). Prefix barunya menjadi /18 (8 + 10).

### Kasus C: Mengefisienkan IPv4 untuk 5 Cabang
Organisasi perusahaan dialokasikan public network address 172.16.0.0/22 oleh ISP (memiliki 10 host bit, menyediakan 1022 alamat host). Terdapat 5 site dan 5 koneksi internet ke ISP, sehingga dibutuhkan total 10 subnet. Subnet terbesar (Corporate Headquarters) membutuhkan 40 host address.

Untuk mengakomodasi 40 host, dibutuhkan minimal 6 host bit (2^6 - 2 = 62 host). Dengan meminjam 4 bit dari porsi host (2^4 = 16 subnet), organisasi tersebut memiliki cukup subnet untuk 10 area (dengan sisa 6 subnet untuk ekspansi). Panjang prefix berubah dari /22 menjadi /26 (22 + 4), dengan subnet mask 255.255.255.192.

## 4. Variable Length Subnet Mask (VLSM)
Penerapan subnetting tradisional sering kali tidak efisien dan menyebabkan pemborosan IP address (wasted addresses). Sebagai contoh, point-to-point connection pada koneksi WAN hanya memerlukan 2 host IP address. Jika menggunakan subnet /27 (yang menyediakan 30 host per subnet), setiap koneksi WAN akan membuang 28 address (30 - 2 = 28).

VLSM (Variable Length Subnet Mask) dikembangkan untuk menghindari pemborosan IP address dengan memungkinkan administrator melakukan subnetting pada subnet yang sudah ada, menghasilkan subnet dengan berbagai macam ukuran (Subnets of Varying Sizes).

**Aturan Utama VLSM:** Saat menggunakan VLSM, selalu mulai dengan memenuhi persyaratan host terbesar, dan teruskan subnetting hingga persyaratan host terkecil terpenuhi.

## 5. Contoh Penerapan VLSM
Sebuah perusahaan dengan network address 192.168.1.0/24 memerlukan 5 subnet dengan spesifikasi: 3 subnet dengan 62 host, dan 2 subnet dengan 30 host. Kita memulai dari kebutuhan host terbesar.

### Langkah 1: Memenuhi Kebutuhan 3 Subnet dengan 62 Host
Dari prefix /24, kita meminjam 2 bit menjadi /26. Hal ini menghasilkan 4 subnet (2^2 = 4) dengan masing-masing 62 host (2^6 - 2 = 62).
* 192.168.1.0/26 (Digunakan untuk 62 host)
* 192.168.1.64/26 (Digunakan untuk 62 host)
* 192.168.1.128/26 (Digunakan untuk 62 host)
* 192.168.1.192/26 (Sisa subnet yang akan di-subnet kembali)

### Langkah 2: Memenuhi Kebutuhan 2 Subnet dengan 30 Host
Sisa subnet 192.168.1.192/26 di-subnet lagi dengan meminjam 1 bit untuk menjadi prefix /27. Hal ini menghasilkan 2 subnet (2^1 = 2) dengan masing-masing 30 host (2^5 - 2 = 30).
* 192.168.1.192/27 (Digunakan untuk 30 host)
* 192.168.1.224/27 (Digunakan untuk 30 host)
