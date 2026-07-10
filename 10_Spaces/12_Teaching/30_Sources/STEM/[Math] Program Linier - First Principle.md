---
title: "[Math] Program Linier - First Principle"
course: ""
tags: ["math", "algebra", "optimization", "first-principle"]
aliases: ["[Math] Program Linier - First Principle"]
created: "2026-05-12"
date: "2026-05-12"
---

# 🎯 Program Linier - Pendekatan First Principle

Ketika mendengar kata "Program Linier", banyak siswa langsung membayangkan grafik rumit dengan banyak garis bersilangan dan mencari titik potong. Tapi, mari kita bongkar konsep ini sampai ke akar paling dasarnya (First Principle).

## 1. Dekonstruksi Istilah
Sebelum masuk ke rumus, apa sebenarnya arti dari kedua kata ini?

- **Program:** Dalam konteks matematika abad pertengahan abad ke-20 (saat ilmu ini dikembangkan, sebelum komputer populer), kata "program" berarti **perencanaan** atau **pembuatan jadwal**. Ini tentang bagaimana kita mengatur strategi untuk mendapatkan hasil terbaik.
- **Linier:** Artinya **berjalan lurus** atau proporsional secara konstan. Jika membuat 1 potong kue butuh 2 butir telur, maka membuat 10 kue pasti butuh 20 telur. Tidak ada diskon kuantitas, tidak ada efek eksponensial. Hubungannya selalu konsisten dan bila digambar akan berupa garis lurus.

Jadi, **Program Linier** secara sederhana adalah: **Cara merencanakan keputusan terbaik di dunia di mana segala sesuatunya bertambah atau berkurang secara proporsional dan konstan.**

---

## 2. Tiga Elemen Fundamental (Membangun dari Nol)

Semua masalah program linier di dunia nyata (dari merencanakan produksi pabrik mobil sampai menentukan jualan penjual gorengan) selalu dibangun di atas 3 pilar fundamental ini:

### A. Variabel Keputusan (Apa yang bisa kita atur?)
Di dunia nyata, kita harus membuat pilihan. 
* "Berapa banyak porsi tempe ($x$) dan tahu ($y$) yang harus saya goreng hari ini?"
Nilai $x$ dan $y$ inilah yang ada di dalam kendali penuh kita. Kita yang memutuskan.

### B. Kendala / Keterbatasan (Apa yang membatasi kita?)
Kita tidak hidup di dunia fantasi. Sumber daya selalu terbatas. 
* Modal kita cuma Rp100.000. 
* Waktu masak kita cuma 3 jam. 
* Kapasitas wajan cuma muat 50 gorengan sekaligus.

Karena sifatnya "batas maksimal" (uang/kapasitas) atau "syarat minimal" (harus terpenuhi syarat gizi), maka bahasa matematika yang tepat untuk menerjemahkan kendala bukanlah persamaan ($=$), melainkan **pertidaksamaan** ($\le$ atau $\ge$). Kita boleh menggunakan modal *kurang dari* Rp100.000, tapi secara logis tidak mungkin *lebih dari* itu. Pertidaksamaan-pertidaksamaan inilah yang pada akhirnya akan mengurung opsi kita dan membentuk "kandang" imajiner yang disebut **Daerah Penyelesaian (Feasible Region)**.

### C. Fungsi Objektif (Apa tujuan akhir kita?)
Apa gunanya merencanakan kalau tidak ada tujuan? 
Setiap pengambilan keputusan yang rasional pasti punya satu dari dua tujuan dasar ini:
1. **Memaksimalkan** sesuatu yang menguntungkan (Profit, hasil panen, jumlah pengunjung).
2. **Meminimalkan** sesuatu yang merugikan/beban (Biaya pengeluaran, waktu tempuh, jarak).
Fungsi tujuan ini biasanya ditulis dalam bentuk $f(x,y) = ax + by$.

---

## 3. Pertanyaan Kritis: Mengapa Jawabannya Selalu Berada di Titik Sudut?

Ini adalah "Aha! moment" paling penting dari Program Linier. Kalau kamu menggambar grafik daerah penyelesaian dari sistem pertidaksamaan di atas, daerah tersebut akan membentuk sebuah bangun datar segi-banyak (poligon). 

**Pertanyaannya: Mengapa nilai optimal (maksimum atau minimum) selalu berada di titik pojok/sudut dari bangun tersebut, dan tidak pernah berada pas di tengah-tengah area arsiran?**

**Analogi First-Principle:**
Bayangkan kamu sedang berada di dalam sebuah ruangan tertutup berbentuk segi enam yang tidak beraturan. Ruangan tertutup ini adalah Daerah Penyelesaian (ruang di mana kamu diizinkan bergerak sesuai aturan kendala). 
Tujuan kamu (Fungsi Objektif) adalah satu: **Berjalan sejauh mungkin ke arah Utara** (menganalogikan mencari nilai setinggi mungkin).

Apa yang secara logis akan kamu lakukan?
1. Kamu akan mulai melangkah ke arah Utara.
2. Selama kamu masih berada di *tengah ruangan*, kamu sadar bahwa kondisimu belum maksimal. Kamu bebas melangkah lebih jauh.
3. Kamu terus berjalan sampai akhirnya dahimu **mentok menabrak dinding ruangan sebelah utara**. (Dinding adalah garis pembatas pertidaksamaan).
4. Apakah pencarianmu otomatis berhenti di situ? Belum tentu. Jika dinding yang kamu tabrak posisinya miring, kamu masih bisa menggeser tubuhmu merayap menyusuri dinding tersebut sejauh mungkin ke ujung dinding yang lebih mengarah ke Utara.
5. Kamu akan terus menggeser badan di sepanjang dinding sampai akhirnya kamu **terjebak di sudut (pojokan)** tempat dinding yang kamu susuri bertemu dengan dinding lain. 

Di titik pertemuan dinding (sudut) itulah, kamu benar-benar terkunci. Kamu tidak bisa lagi bergerak lebih ke Utara sedikitpun tanpa menjebol dinding (melanggar kendala). **Itulah nilai mutlak maksimummu!**

Karena semua garis pembatas (kendala) dan arah tujuan kita bersifat lurus (linier), maka dorongan untuk mencari nilai yang "paling besar" atau "paling kecil" akan selalu mendorong posisi kita mentok ke arah ujung-ujung batas kawasan, alias **titik ekstrim atau titik potong**.

---

## Kesimpulan

Mempelajari Program Linier bukanlah sekadar menghafal cara menggambar garis pembatas dan mengarsir daerah bersilangan. Pada esensi paling dasarnya, Program Linier adalah **seni mencari "titik mentok terbaik"** di dalam sebuah "kandang keterbatasan". 

Kita memiliki kebebasan memilih kombinasi angka (variabel keputusan), dan kita terus mendorong pilihan tersebut setinggi mungkin (memaksimalkan fungsi) sampai kita benar-benar dipaksa berhenti oleh realitas hidup (titik sudut dari garis-garis kendala).
