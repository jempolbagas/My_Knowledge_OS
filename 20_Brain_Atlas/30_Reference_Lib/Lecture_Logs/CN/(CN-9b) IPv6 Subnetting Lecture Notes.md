---
title: "(CN-9b) IPv6 Subnetting Lecture Notes"
course: ""
tags: []
aliases: ["(CN-9b) IPv6 Subnetting Lecture Notes"]
created: "2026-06-24"
---
# Materi Pembelajaran: IPv6 – Subnetting

**Mata Kuliah:** Jaringan Komputer (Genap 2025/2026)  
**Program Studi:** Informatika UNS  
**Pengajar:** Herdito Ibnu Dewangkoro  

---

## 1. Konsep Dasar Subnetting IPv6

Protokol IPv6 secara inheren dirancang dengan mempertimbangkan kebutuhan *subnetting*. Tidak seperti IPv4 di mana *subnetting* sering kali melibatkan perhitungan peminjaman bit *host* yang rumit, IPv6 menyediakan kolom khusus yang disebut **Subnet ID** dalam struktur Global Unicast Address (GUA).

### Struktur Alamat IPv6 (Prefix /64)
Sebuah alamat IPv6 standar untuk sebuah subjaringan biasanya menggunakan *prefix* `/64`, yang didefinisikan oleh IETF sebagai ukuran subnet terkecil yang digunakan secara lokal (terutama untuk mendukung konfigurasi otomatis / SLAAC).

Struktur alamatnya terdiri dari 128 bit yang dibagi menjadi tiga bagian utama:
*   **Global Routing Prefix (48 bit):** Diberikan oleh ISP atau *registry* internet. Identitas jaringan global.
*   **Subnet ID (16 bit):** Area yang digunakan oleh administrator jaringan lokal untuk membuat *subnet*. Terletak di antara Global Routing Prefix dan Interface ID.
*   **Interface ID (64 bit):** Setara dengan *Host ID* pada IPv4, digunakan untuk mengidentifikasi antarmuka perangkat secara unik pada jaringan lokal.

**Formula Subnetting Standar:**  
`48-bit Global Routing Prefix` + `16-bit Subnet ID` = **`/64 Prefix`**

---

## 2. Contoh Perhitungan Subnetting IPv6

Misalkan Anda diberikan sebuah Global Routing Prefix **`2001:db8:acad::/48`** dengan panjang Interface ID sebesar 64 bit. Bagaimana kita melakukan *subnetting* untuk menghasilkan *prefix* `/64`?

### A. Jumlah Subnet yang Dihasilkan
*   Total panjang alamat IPv6 = 128 bit.
*   Bit untuk *Interface ID* = 64 bit.
*   Bit untuk *Global Routing Prefix* = 48 bit.
*   Panjang bit *Subnet ID* = 128 - 64 - 48 = **16 bit**.

Dengan 16 bit *Subnet ID*, Anda dapat menghasilkan **65.536 subnet** (didapatkan dari perhitungan $2^{16}$).  
Nilai *Subnet ID* ini akan di- *increment* dalam bentuk heksadesimal, mulai dari `0000` hingga `ffff`.

**Daftar Subnet yang Terbentuk:**
1. `2001:db8:acad:0000::/64`
2. `2001:db8:acad:0001::/64`
3. `2001:db8:acad:0002::/64`
4. `2001:db8:acad:0003::/64`
5. ... dan seterusnya hingga `2001:db8:acad:ffff::/64`

### B. Jumlah IP Address per Subnet
Untuk setiap subnet tunggal, jumlah alamat IP yang tersedia untuk antarmuka (*host*) dihitung dari *Interface ID* yang berjumlah 64 bit:  
**Jumlah IP** = $2^{64}$ (Mendukung hingga sekitar 18 kuintiliun alamat *host* per subnet).

---

## 3. Studi Kasus: Alokasi Subnet

Misalkan terdapat sebuah topologi jaringan yang membutuhkan **5 subnet**:
*   4 subnet dialokasikan untuk jaringan LAN.
*   1 subnet dialokasikan untuk *serial link* (koneksi antar *router* R1 dan R2).

Dari blok alamat `2001:0db8:acad::/48`, administrator mengalokasikan 5 subnet secara berurutan menggunakan *Subnet ID* `0001` hingga `0005`.

**Alokasi Subnet:**
*   **LAN 1 (R1 G0/0/0):** `2001:db8:acad:1::/64`
*   **LAN 2 (R1 G0/0/1):** `2001:db8:acad:2::/64`
*   **Link Serial (R1-R2 S0/1/0):** `2001:db8:acad:3::/64`
*   **LAN 3 (R2 G0/0/0):** `2001:db8:acad:4::/64`
*   **LAN 4 (R2 G0/0/1):** `2001:db8:acad:5::/64`

### Rincian Host IP dalam Satu Subnet
Mari kita ambil subnet pertama yaitu **`2001:db8:acad:0001::/64`**. Alamat IP (*host*) yang memungkinkan di dalam *subnet* ini adalah dari semua bit 0 hingga semua bit F pada *Interface ID*:
*   IP Awal: `2001:db8:acad:0001:0000:0000:0000:0000` (atau disingkat menjadi `2001:db8:acad:1::`)
*   IP Kedua: `2001:db8:acad:0001:0000:0000:0000:0001` (`2001:db8:acad:1::1`)
*   IP Ketiga: `2001:db8:acad:0001:0000:0000:0000:0002` (`2001:db8:acad:1::2`)
*   ...
*   IP Terakhir: `2001:db8:acad:0001:ffff:ffff:ffff:ffff` (`2001:db8:acad:1:ffff:ffff:ffff:ffff`)

---

## 4. Konfigurasi Router pada Subnet IPv6

Berikut adalah contoh konfigurasi CLI (Command Line Interface) pada antarmuka *Router* (misal Router R1 pada Cisco IOS) untuk menerapkan alamat IPv6 ke setiap antarmuka berdasarkan alokasi *subnet* di atas.

```bash
! Konfigurasi untuk Interface LAN 1
R1(config)# interface gigabitethernet 0/0/0
R1(config-if)# ipv6 address 2001:db8:acad:1::1/64
R1(config-if)# no shutdown
R1(config-if)# exit

! Konfigurasi untuk Interface LAN 2
R1(config)# interface gigabitethernet 0/0/1
R1(config-if)# ipv6 address 2001:db8:acad:2::1/64
R1(config-if)# no shutdown
R1(config-if)# exit

! Konfigurasi untuk Interface Serial (Ke arah R2)
R1(config)# interface serial 0/1/0
R1(config-if)# ipv6 address 2001:db8:acad:3::1/64
R1(config-if)# no shutdown
R1(config-if)# exit
```

Pastikan melakukan *no shutdown* agar antarmuka tersebut aktif (*up*).
