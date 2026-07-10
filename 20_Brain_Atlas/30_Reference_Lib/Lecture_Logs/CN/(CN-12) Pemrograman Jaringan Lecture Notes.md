---
title: "(CN-12) Pemrograman Jaringan Lecture Notes"
course: ""
tags: []
aliases: ["(CN-12) Pemrograman Jaringan Lecture Notes"]
created: "2026-06-24"
---
# Pemrograman Jaringan dengan Python

**Mata Kuliah:** Jaringan Komputer Genap 2025/2026 | Informatika UNS  
**Pengampu:** Herdito Ibnu Dewangkoro

---

## A. Pendahuluan

Kita akan mengimplementasikan TCP dan UDP pada pemrograman jaringan sederhana menggunakan *socket programming* di bahasa pemrograman Python.

*   **Socket** merupakan jembatan yang menghubungkan suatu aplikasi berbasis jaringan dengan protokol TCP/UDP.
*   Ada dua paradigma utama dalam pemrograman jaringan, yaitu sebagai **server** dan sebagai **client**.
*   Sangat direkomendasikan untuk menjalankan program pada sistem operasi Linux.
*   Gunakan `Ctrl + c` pada Linux atau `Ctrl + PauseBreak` pada Windows untuk memberikan *KeyboardInterrupt* (menghentikan program secara paksa).

---

## B. Implementasi TCP

Protokol TCP (Transmission Control Protocol) bersifat *connection-oriented*, yang berarti koneksi harus dibangun terlebih dahulu sebelum pertukaran data dapat dilakukan.

### Alur Komunikasi TCP:
1.  **Server:** `socket()` -> `bind()` -> `listen()` -> `accept()` *(menunggu koneksi dari client)*
2.  **Client:** `socket()` -> `connect()` *(membangun koneksi / establish connection dengan server)*
3.  **Pertukaran Data:** 
    * Client menggunakan `send()` dan Server menggunakan `recv()`.
    * Server merespons dengan `send()` dan Client menggunakan `recv()`.
4.  **Selesai:** Kedua belah pihak memanggil `close()` untuk mengakhiri koneksi.

### a. Kode TCP Server

```python
import socket, sys

# AF_INET untuk IPv4
# TCP => pakai SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip address dan port server
s.bind(('127.0.0.1', 1234))

# listen(1) berarti hanya dapat menangani 1 koneksi dan akan membuat koneksi lain mengantri
s.listen(1)

try:
    while True:
        client_sock, client_addr = s.accept()
        print("ip dan port client: ", client_addr)
        
        # TCP => pakai recv
        data = client_sock.recv(65535)
        print("data yg diterima: ", data)
        
        # b berarti string diinterpretasikan sebagai bytes daripada characters
        client_sock.send(b"kirim balik ke client >> " + data)
        client_sock.close()

except KeyboardInterrupt:
    s.close()
    print("program tcp server dimatikan")
    sys.exit(0)
```

### b. Kode TCP Client

```python
import socket

# AF_INET untuk IPv4
# TCP => pakai SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# membuat koneksi, masukkan ip address dan port server
s.connect(('127.0.0.1', 1234))

# b berarti string diinterpretasikan sebagai bytes daripada characters
s.send(b"Halo semua, ini pakai TCP!!")

# TCP => pakai recv
data = s.recv(65535)
print("data yg dikirim balik server: ", data)

s.close()
print("program tcp client selesai")
```

---

## C. Implementasi UDP

Protokol UDP (User Datagram Protocol) bersifat *connectionless*, yang berarti data dapat langsung dikirim tanpa perlu membangun koneksi secara spesifik (tidak ada proses `listen` atau `accept`).

### Alur Komunikasi UDP:
1.  **Server:** `socket()` -> `bind()` -> `recvfrom()` *(menunggu data masuk)*
2.  **Client:** `socket()` -> `sendto()` *(mengirim data ke alamat server)*
3.  **Pertukaran Data:**
    * Server menerima data dan alamat pengirim melalui `recvfrom()`, lalu membalas menggunakan `sendto()`.
    * Client menerima balasan menggunakan `recvfrom()`.
4.  **Selesai:** Kedua belah pihak memanggil `close()`.

### a. Kode UDP Server

```python
import socket, sys

# AF_INET untuk IPv4
# UDP => pakai SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ip address dan port server
s.bind(('127.0.0.1', 4321))

try:
    while True:
        # UDP => pakai recvfrom
        data, client_addr = s.recvfrom(65535)
        print("data yg diterima: ", data)
        print("ip dan port client: ", client_addr)
        
        # b berarti string diinterpretasikan sebagai bytes daripada characters
        s.sendto(b"kirim balik ke client >> " + data, client_addr)

except KeyboardInterrupt:
    s.close()
    print("program udp server dimatikan")
    sys.exit(0)
```

### b. Kode UDP Client

```python
import socket

# AF_INET untuk IPv4
# UDP => pakai SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Tidak seperti TCP, di UDP bisa tidak pakai connect, UDP adalah connectionless protocol
# b berarti string diinterpretasikan sebagai bytes daripada characters
s.sendto(b"Halo semua, ini pakai UDP!!", ('127.0.0.1', 4321))

# UDP => pakai recvfrom
data, server_addr = s.recvfrom(65535)
print("data yg dikirim balik server: ", data)
print("ip dan port server yg ngirim balik data: ", server_addr)

s.close()
print("program udp client selesai")
```

---

## D. Referensi

**Materi:**
* [Developer Quectel: TCP/UDP Network Protocols](https://developer.quectel.com/doc/quecpython/Application_guide/en/network-comm/net-protocols/tcp-udp.html)
* [Suhu.co.id: Mengenal Socket Programming, Pengertian dan Kelebihannya](https://suhu.co.id/berita/mengenal-socket-programming-pengertian-dan-kelebihannya)

**Kode Program:**
* [GitHub: studiawan/progjar/](https://github.com/studiawan/progjar/)
