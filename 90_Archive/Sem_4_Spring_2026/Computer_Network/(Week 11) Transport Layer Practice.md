---
title: "Transport Layer Guided Practice: Soal Latihan & Pembahasan Komprehensif"
course: Jaringan Komputer
tags: ["#computer-networks", "#transport-layer", "#practice", "#week-11"]
aliases: ["Latihan Soal Transport Layer (Week 11)", "Transport Layer Practice Week 11"]
created: "2026-06-25"
---

# Transport Layer Guided Practice: Soal Latihan & Pembahasan Komprehensif (Week 11)

Halo! Selamat datang di dokumen latihan soal terbimbing untuk materi **Transport Layer (Week 11)**. 

Dokumen ini dirancang khusus untuk membantumu menguasai tipe-tipe soal ujian yang paling sering keluar mengenai protokol transport (TCP dan UDP), lengkap dengan analisis logika mendalam, rumus formal LaTeX, dan trik menghindari jebakan ujian. 

Gunakan dokumen ini sebagai pendamping belajar setelah kamu membaca [[(Week 11) Transport Layer Complete Guide|Transport Layer Complete Guide (Week 11)]], ya!

---

## Soal 1: Analisis Jalur Transmisi TCP & Kehilangan Paket (Sequence/ACK Numbers)

### Soal
Host A mengirimkan data ke Host B menggunakan protokol TCP. Koneksi telah terbentuk (*established*). Host A memiliki data berukuran total $1200 \text{ byte}$ yang akan dikirimkan dalam tiga segmen berurutan dengan ukuran masing-masing $400 \text{ byte}$. Nomor urut awal (*Sequence Number*) segmen pertama ditentukan sebesar **`1001`**.

Dalam proses transmisi, segmen kedua mengalami kehilangan paket (*packet loss*) di pertengahan jalur akibat gangguan interferensi media. Sementara itu, segmen pertama dan segmen ketiga berhasil diterima dengan selamat oleh Host B.

1. Tentukan nilai *Sequence Number* (Seq) dan rentang byte data untuk ketiga segmen yang dikirim oleh Host A.
2. Jelaskan urutan respon *Acknowledgment Number* (ACK) yang dikirimkan oleh Host B setelah menerima masing-masing segmen tersebut.
3. Terangkan bagaimana mekanisme pengiriman ulang (*retransmission*) dipicu pada skenario ini (apakah melalui RTO Timeout atau Fast Retransmit) beserta nilai parameter segmen yang dikirim ulang.

---

### Pembahasan

#### 1. Intuition & Case Analysis
Halo kawan! Di soal ini, kunci utamanya adalah menyadari bahwa **TCP melacak byte data secara individual, bukan nomor paket segmen**. 
* Jika segmen pertama membawa data berukuran $400 \text{ byte}$ dan dimulai dari nomor $1001$, artinya segmen tersebut berisi byte nomor $1001$ sampai $1400$. 
* Segmen berikutnya (segmen kedua) otomatis akan mulai dari byte setelahnya, yaitu $1401$.
* Karena segmen kedua hilang di jalan, Host B akan mendeteksi adanya lubang (*gap*) di memori penyangganya saat segmen ketiga (membawa byte $1801-2200$) tiba. 
* Sifat pengakuan TCP adalah **Cumulative Acknowledgment (ACK Kumulatif)**. Penerima hanya akan mengirim ACK untuk byte berurutan terkecil yang belum ia terima. Jadi, ketika menerima segmen ketiga yang melompati segmen kedua, Host B akan teriak: *"Eh, saya masih nunggu byte 1401 lho!"*, yang menghasilkan segmen ACK duplikat.

#### 2. Theoretical Analysis & Logical Solution

##### Bagian A: Pemetaan Parameter Segmen Host A
Total data yang dikirim adalah $1200 \text{ byte}$, dibagi menjadi 3 segmen dengan ukuran masing-masing $400 \text{ byte}$:
* **Segmen 1:**
  - $\text{Sequence Number (Seq)}_1 = 1001$
  - Panjang Data $(\text{Length})_1 = 400 \text{ byte}$
  - Rentang byte data: $[1001, 1400]$
* **Segmen 2:**
  - $\text{Sequence Number (Seq)}_2 = \text{Seq}_1 + \text{Length}_1 = 1001 + 400 = 1401$
  - Panjang Data $(\text{Length})_2 = 400 \text{ byte}$
  - Rentang byte data: $[1401, 1800]$
* **Segmen 3:**
  - $\text{Sequence Number (Seq)}_3 = \text{Seq}_2 + \text{Length}_2 = 1401 + 400 = 1801$
  - Panjang Data $(\text{Length})_3 = 400 \text{ byte}$
  - Rentang byte data: $[1801, 2200]$

##### Bagian B: Urutan Respon ACK Host B
* **Ketika Segmen 1 tiba di Host B:**
  Host B menerima byte data $[1001, 1400]$ dengan sukses dan berurutan. Byte berikutnya yang diharapkan adalah $1400 + 1 = 1401$.
  Host B mengirimkan: **$\text{ACK} = 1401$**.
* **Ketika Segmen 2 hilang di jalan:**
  Host B tidak menerima paket apa pun untuk byte $[1401, 1800]$, sehingga tidak ada respon ACK yang dipicu oleh kejadian ini.
* **Ketika Segmen 3 tiba di Host B:**
  Host B menerima byte $[1801, 2200]$. Namun, karena byte $[1401, 1800]$ belum datang, ada *gap* data. TCP tidak boleh mengirim $\text{ACK} = 2201$. Host B harus memperingatkan pengirim tentang byte terkecil yang hilang dengan mengirimkan ACK duplikat:
  Host B mengirimkan: **$\text{ACK} = 1401$** (ini terhitung sebagai **Duplicate ACK ke-1**).

##### Bagian C: Pemicu Mekanisme Retransmisi
* Algoritma **Fast Retransmit** hanya akan aktif jika pengirim menerima **3 Duplicate ACKs** secara berturut-turut (total menerima 4 buah ACK bernilai sama).
* Dalam kasus ini, Host A hanya menerima:
  1. $\text{ACK} = 1401$ (ACK asli hasil Segmen 1).
  2. $\text{ACK} = 1401$ (Duplicate ACK ke-1 hasil Segmen 3).
* Karena jumlah *Duplicate ACK* yang diterima kurang dari 3 ($1 < 3$), maka **Fast Retransmit tidak akan dipicu**.
* Pemulihan paket yang hilang akan mengandalkan **RTO (Retransmission Timeout)**. Ketika timer khusus untuk Segmen 2 yang dinyalakan Host A habis masa berlakunya (*expired*), Host A akan mengirimkan ulang Segmen 2 dengan parameter:
  - $\text{Sequence Number} = 1401$
  - $\text{Length} = 400 \text{ byte}$
* Setelah segmen retransmisi ini tiba di Host B, celah memori $[1401, 1800]$ terisi penuh. Karena byte $[1801, 2200]$ sudah tersimpan di buffer penerima sebelumnya, Host B kini memiliki seluruh data lengkap dari byte $1001$ hingga $2200$. 
* Host B akan mengirimkan ACK kumulatif baru: **$\text{ACK} = 2201$**.

#### 3. Tips & Traps
> [!warning] **Jebakan Ujian: Menentukan Pemicu Retransmisi**
> Banyak mahasiswa langsung menjawab "Fast Retransmit" begitu melihat ada kata "kehilangan paket dan ada segmen yang lolos setelahnya". Ingat aturan baku ini: **Fast Retransmit butuh minimal 3 Duplicate ACKs**. 
> 
> Jika paket yang dikirimkan sedikit (misalnya hanya 3 segmen seperti di soal ini), maka jumlah segmen setelah paket yang hilang tidak akan cukup untuk menghasilkan 3 Duplicate ACKs. Walhasil, kita kudu bersabar menunggu timer RTO habis untuk memicu pengiriman ulang. Jangan sampai salah analisis di lembar ujian ya!

---

## Soal 2: TCP Sliding Window & Flow Control

### Soal
Host A dan Host B terhubung melalui koneksi TCP. Host B mengalokasikan memori penyangga penerima (*Receive Buffer / RcvBuffer*) sebesar **$8000 \text{ byte}$**. Saat ini, status data pada Host B adalah sebagai berikut:
- Byte data terakhir yang telah diterima dengan sukses dari kabel jaringan ($\text{LastByteReceived}$) adalah nomor **`6500`**.
- Byte data terakhir yang telah dibaca dan diambil oleh aplikasi internal ($\text{LastByteRead}$) adalah nomor **`4000`**.

1. Tentukan nilai kapasitas jendela penerima ($\text{Receiver Window / rwnd}$) yang akan diiklankan oleh Host B kepada Host A pada segmen pengakuan (ACK) berikutnya.
2. Jika Host A kemudian mengirimkan segmen baru berisi data sebesar **$1500 \text{ byte}$** sebelum aplikasi di Host B membaca data lagi dari penyangga, hitung nilai $\text{LastByteReceived}$ yang baru dan hitung sisa kapasitas $\text{rwnd}$ setelah segmen baru tersebut tiba di Host B.
3. Jelaskan apa yang terjadi jika aplikasi di Host B terus mendiamkan buffer sehingga nilai $\text{rwnd}$ menyusut hingga **$0 \text{ byte}$**, serta terangkan mekanisme yang digunakan TCP untuk memulihkan transmisi data agar tidak terkunci selamanya (*deadlock*).

---

### Pembahasan

#### 1. Intuition & Case Analysis
Bayangkan memori buffer penerima itu seperti sebuah **gudang penyimpanan**. 
* Truk pengirim (Host A) menaruh barang di gudang ($\text{LastByteReceived}$).
* Pemilik gudang (Aplikasi Host B) mengambil barang dari gudang untuk diproses ($\text{LastByteRead}$).
* Sisa ruang kosong di gudang inilah yang disebut **Receiver Window (`rwnd`)**. 
* Truk pengirim tidak boleh membawa barang melebihi kapasitas ruang kosong gudang tersebut agar barang tidak tumpah ke jalan (*buffer overflow*).
* Jika gudang penuh (`rwnd = 0`), truk berhenti mengirim, tetapi dia akan terus mengetuk pintu gudang secara berkala (mengirim paket probe 1-byte) untuk menanyakan: *"Apakah gudang sudah ada yang kosong?"*.

#### 2. Theoretical Analysis & Logical Solution

##### Bagian A: Menghitung rwnd Awal Host B
* Diketahui parameter awal:
  - $\text{RcvBuffer} = 8000 \text{ byte}$
  - $\text{LastByteReceived} = 6500$
  - $\text{LastByteRead} = 4000$
* Jumlah byte data yang mengendap di buffer (sudah diterima tapi belum dibaca aplikasi):
  $$\text{DataMengendap} = \text{LastByteReceived} - \text{LastByteRead} = 6500 - 4000 = 2500 \text{ byte}$$
* Kapasitas ruang kosong jendela penerima (`rwnd`) yang diiklankan:
  $$\text{rwnd} = \text{RcvBuffer} - \text{DataMengendap}$$
  $$\text{rwnd} = 8000 - 2500 = \mathbf{5500 \text{ byte}}$$
  Maka, Host B akan mengiklankan **$\text{rwnd} = 5500 \text{ byte}$** pada segmen ACK berikutnya.

##### Bagian B: Dampak Pengiriman Segmen Baru 1500 Byte
* Host A melihat bahwa ia masih boleh mengirim hingga $5500 \text{ byte}$ data. Karena ia hanya mengirim $1500 \text{ byte}$ ($1500 \le 5500$), data tersebut aman diterima oleh buffer Host B.
* Nilai byte terakhir yang diterima ($\text{LastByteReceived}$) bergeser naik:
  $$\text{LastByteReceived}_{\text{baru}} = \text{LastByteReceived}_{\text{lama}} + 1500 = 6500 + 1500 = \mathbf{8000}$$
* Karena aplikasi di Host B belum membaca data baru dari buffer, nilai $\text{LastByteRead}$ tetap bernilai $4000$.
* Jumlah data mengendap yang baru di buffer:
  $$\text{DataMengendap}_{\text{baru}} = \text{LastByteReceived}_{\text{baru}} - \text{LastByteRead} = 8000 - 4000 = 4000 \text{ byte}$$
* Sisa kapasitas window penerima (`rwnd`) yang baru:
  $$\text{rwnd}_{\text{baru}} = \text{RcvBuffer} - \text{DataMengendap}_{\text{baru}} = 8000 - 4000 = \mathbf{4000 \text{ byte}}$$

##### Bagian C: Solusi Kondisi Zero Window (rwnd = 0)
* Jika aplikasi Host B berhenti membaca buffer sementara Host A terus mengirim data, seluruh kapasitas buffer akan terisi penuh ($\text{LastByteReceived} - \text{LastByteRead} = \text{RcvBuffer}$), sehingga Host B akan mengirimkan nilai **$\text{rwnd} = 0 \text{ byte}$**.
* Host A akan segera **menghentikan seluruh pengiriman data**.
* Untuk mencegah kondisi saling menunggu selamanya (*deadlock*) akibat potensi hilangnya segmen pembaruan window dari Host B, TCP mengaktifkan **Persist Timer** di sisi pengirim (Host A):
  1. Ketika timer habis, Host A mengirimkan segmen khusus berukuran **$1 \text{ byte}$** yang disebut **Zero Window Probe**.
  2. Host B dipaksa untuk merespon segmen probe ini dengan mengirimkan ACK.
  3. ACK balasan dari Host B akan memuat status kapasitas buffer terbaru (`rwnd`).
  4. Laju pengiriman data normal akan dilanjutkan segera setelah Host A menerima ACK dengan nilai $\text{rwnd} > 0$.

#### 3. Tips & Traps
> [!tip] **Obsidian Tip: Hati-Hati dengan Pengurangan Byte**
> Ingat rumus dasarnya: data yang mengendap adalah selisih $\text{LastByteReceived}$ dan $\text{LastByteRead}$. Jangan sekali-kali mengurangkan langsung $\text{LastByteReceived}$ dengan ukuran total buffer, karena aplikasi penerima selalu membaca data secara paralel sehingga membebaskan kembali ruang memori buffer!

---

## Soal 3: TCP Congestion Control State Trace

### Soal
Sebuah koneksi TCP Reno memiliki nilai ambang batas awal kemacetan (*Slow Start Threshold / ssthresh*) sebesar **$16 \text{ MSS}$** (Maximum Segment Size). Pada saat sesi pengiriman dimulai (Ronde Transmisi 1), nilai jendela kemacetan (*Congestion Window / cwnd*) diinisialisasi sebesar **$1 \text{ MSS}$**.

Jelaskan perilaku perubahan nilai $\text{cwnd}$ dan $\text{ssthresh}$ dari ronde ke ronde (Ronde 1 s.d. 12) dengan kondisi peristiwa sebagai berikut:
1. Mulai dari Ronde 1 hingga Ronde 5, pengiriman berjalan lancar tanpa ada packet loss.
2. Pada akhir transmisi Ronde 5 (saat segmen sedang dikirim), terjadi peristiwa **Timeout** yang dideteksi oleh pengirim.
3. Setelah pemulihan dari peristiwa Timeout tersebut, transmisi berjalan normal kembali hingga akhir Ronde 10.
4. Pada transmisi Ronde 10, terdeteksi kehilangan paket kembali, namun kali ini melalui **Triple Duplicate ACKs**.

Tuliskan tabel pelacakan nilai $\text{cwnd}$ dan $\text{ssthresh}$ untuk setiap ronde transmisi (Ronde 1 hingga Ronde 12) beserta penjelasan fase kontrol kongesti yang aktif pada ronde tersebut.

---

### Pembahasan

#### 1. Intuition & Case Analysis
Halo teman-teman! Pelacakan kontrol kongesti TCP Reno ini sangat logis jika kita memegang teguh aturan transisinya:
* **Fase Slow Start:** Berjalan saat $\text{cwnd} < \text{ssthresh}$. Nilai `cwnd` dilipatgandakan setiap RTT (ronde transmisi).
* **Fase Congestion Avoidance:** Aktif saat $\text{cwnd} \ge \text{ssthresh}$. Nilai `cwnd` naik secara linier ($+1$ MSS per ronde).
* **Efek Timeout (Kemacetan Parah):** Ambang batas dipotong setengah dari window saat ini ($\text{ssthresh} = \text{cwnd} / 2$), window di-reset total ($\text{cwnd} = 1 \text{ MSS}$), dan kita kembali ke fase **Slow Start**.
* **Efek Triple Duplicate ACKs (Kemacetan Ringan):** Ambang batas dipotong setengah dari window saat ini ($\text{ssthresh} = \text{cwnd} / 2$), nilai window disamakan dengan ambang batas baru ($\text{cwnd} = \text{ssthresh}$), dan kita langsung masuk ke fase **Congestion Avoidance / Fast Recovery** pada ronde berikutnya tanpa mengulang dari 1 MSS.

#### 2. Theoretical Analysis & Logical Solution

Mari kita runtut nilai $\text{cwnd}$ dan $\text{ssthresh}$ dari ronde ke ronde:

* **Ronde 1:** $\text{cwnd} = 1 \text{ MSS}, \text{ssthresh} = 16$. 
  Fase: **Slow Start** (karena $1 < 16$). Transmisi sukses. $\text{cwnd}$ ronde berikutnya dilipatgandakan menjadi $2 \text{ MSS}$.
* **Ronde 2:** $\text{cwnd} = 2 \text{ MSS}, \text{ssthresh} = 16$.
  Fase: **Slow Start**. Transmisi sukses. $\text{cwnd}$ ronde berikutnya menjadi $4 \text{ MSS}$.
* **Ronde 3:** $\text{cwnd} = 4 \text{ MSS}, \text{ssthresh} = 16$.
  Fase: **Slow Start**. Transmisi sukses. $\text{cwnd}$ ronde berikutnya menjadi $8 \text{ MSS}$.
* **Ronde 4:** $\text{cwnd} = 8 \text{ MSS}, \text{ssthresh} = 16$.
  Fase: **Slow Start**. Transmisi sukses. $\text{cwnd}$ ronde berikutnya menjadi $16 \text{ MSS}$.
* **Ronde 5:** $\text{cwnd} = 16 \text{ MSS}, \text{ssthresh} = 16$.
  Fase: **Slow Start $\rightarrow$ Congestion Avoidance** (karena nilai `cwnd` sudah menyentuh `ssthresh`). Namun, pada akhir transmisi ronde ini terdeteksi **Timeout**.
  - Hitung parameter baru untuk ronde berikutnya:
    $$\text{ssthresh}_{\text{baru}} = \frac{\text{cwnd}}{2} = \frac{16}{2} = 8 \text{ MSS}$$
    $$\text{cwnd}_{\text{baru}} = 1 \text{ MSS}$$
  - Sistem kembali ke fase **Slow Start**.
* **Ronde 6:** $\text{cwnd} = 1 \text{ MSS}, \text{ssthresh} = 8$.
  Fase: **Slow Start** (karena $1 < 8$). Transmisi sukses. $\text{cwnd}$ ronde berikutnya menjadi $2 \text{ MSS}$.
* **Ronde 7:** $\text{cwnd} = 2 \text{ MSS}, \text{ssthresh} = 8$.
  Fase: **Slow Start**. Transmisi sukses. $\text{cwnd}$ ronde berikutnya menjadi $4 \text{ MSS}$.
* **Ronde 8:** $\text{cwnd} = 4 \text{ MSS}, \text{ssthresh} = 8$.
  Fase: **Slow Start**. Transmisi sukses. $\text{cwnd}$ ronde berikutnya menjadi $8 \text{ MSS}$.
* **Ronde 9:** $\text{cwnd} = 8 \text{ MSS}, \text{ssthresh} = 8$.
  Fase: **Congestion Avoidance** (karena $\text{cwnd} \ge \text{ssthresh}$ yaitu $8 \ge 8$). Mulai dari sini, kenaikan bersifat linier ($+1$ MSS per ronde). Transmisi sukses. $\text{cwnd}$ ronde berikutnya menjadi $8 + 1 = 9 \text{ MSS}$.
* **Ronde 10:** $\text{cwnd} = 9 \text{ MSS}, \text{ssthresh} = 8$.
  Fase: **Congestion Avoidance**. Pada akhir transmisi ronde ini, terdeteksi **Triple Duplicate ACKs**.
  - Hitung parameter baru untuk ronde berikutnya menggunakan aturan TCP Reno:
    $$\text{ssthresh}_{\text{baru}} = \frac{\text{cwnd}}{2} = \frac{9}{2} = 4.5 \rightarrow \mathbf{4 \text{ MSS}} \text{ (dibulatkan ke bawah)}$$
    $$\text{cwnd}_{\text{baru}} = \text{ssthresh}_{\text{baru}} = \mathbf{4 \text{ MSS}}$$
  - Sistem langsung masuk ke fase **Congestion Avoidance** (Fast Recovery) untuk ronde berikutnya.
* **Ronde 11:** $\text{cwnd} = 4 \text{ MSS}, \text{ssthresh} = 4$.
  Fase: **Congestion Avoidance**. Transmisi sukses. Kenaikan linier, sehingga $\text{cwnd}$ ronde berikutnya menjadi $4 + 1 = 5 \text{ MSS}$.
* **Ronde 12:** $\text{cwnd} = 5 \text{ MSS}, \text{ssthresh} = 4$.
  Fase: **Congestion Avoidance**. Transmisi sukses. Kenaikan linier, sehingga $\text{cwnd}$ ronde berikutnya menjadi $6 \text{ MSS}$.

##### Tabel Pelacakan Transmisi Lengkap:

| Ronde Transmisi | cwnd (MSS) | ssthresh (MSS) | Fase Kontrol Kongesti Aktif | Peristiwa Jaringan |
| :---: | :---: | :---: | :--- | :--- |
| **1** | 1 | 16 | Slow Start | Transmisi Sukses |
| **2** | 2 | 16 | Slow Start | Transmisi Sukses |
| **3** | 4 | 16 | Slow Start | Transmisi Sukses |
| **4** | 8 | 16 | Slow Start | Transmisi Sukses |
| **5** | 16 | 16 | Slow Start $\rightarrow$ Congestion Avoidance | **Timeout** terdeteksi pada akhir ronde |
| **6** | 1 | 8 | Slow Start (Reset) | Transmisi Sukses |
| **7** | 2 | 8 | Slow Start | Transmisi Sukses |
| **8** | 4 | 8 | Slow Start | Transmisi Sukses |
| **9** | 8 | 8 | Congestion Avoidance | Transmisi Sukses |
| **10** | 9 | 8 | Congestion Avoidance | **Triple Duplicate ACKs** terdeteksi |
| **11** | 4 | 4 | Congestion Avoidance (Fast Recovery) | Transmisi Sukses |
| **12** | 5 | 4 | Congestion Avoidance | Transmisi Sukses |

#### 3. Tips & Traps
> [!important] **Jebakan Ujian: Titik Transisi Slow Start ke Congestion Avoidance**
> Perhatikan perpindahan dari Ronde 8 ke Ronde 9. Pada akhir Ronde 8, nilai `cwnd` bernilai $8$ dan `ssthresh` bernilai $8$. Karena nilai window sudah menyentuh batas threshold, maka untuk Ronde 9 kenaikan tidak boleh dilipatgandakan menjadi 16, melainkan **wajib naik secara linier sebesar $+1$ menjadi 9**. 
> 
> Ini adalah salah satu kesalahan paling fatal dan paling sering terjadi saat mahasiswa terburu-buru mengerjakan soal hitungan kongesti di lembar jawaban ujian!

---
Semoga pembahasan latihan soal terbimbing ini bisa mempertajam kemampuan analisismu dan membantumu mendapatkan nilai sempurna di ujian Jaringan Komputer! Jangan lupa untuk mencoba mencoret-coret sendiri hitungannya di kertas buram ya! Semangat! 🚀
