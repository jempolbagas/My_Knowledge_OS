---
title: "[Math] Statistika - First Principle"
course: ""
tags: ["math", "statistics", "grade-10"]
aliases: ["[Math] Statistika - First Principle"]
created: "2026-05-12"
---

# Statistika: Memahami Dunia Melalui Data (Pendekatan First-Principle)

> [!info] Pendahuluan: Mengapa Kita Butuh Statistika?
> Bayangkan kamu berada di sebuah pasar yang sangat ramai. Orang-orang berlalu-lalang, berteriak menawarkan barang, tawar-menawar, cuaca berubah, dan suara bising di mana-mana. Jika seseorang bertanya, "Apa yang sebenarnya terjadi di pasar ini?", kamu tidak mungkin menceritakan setiap detail dari ribuan kejadian tersebut. Kamu butuh cara untuk **merangkum kekacauan menjadi informasi yang bisa dimengerti**. Itulah esensi dari **Statistika**.
> 
> Statistika lahir dari kebutuhan manusia untuk memahami dunia yang penuh variasi dan ketidakpastian dengan mengumpulkan, mengolah, dan menyajikan data sehingga kita bisa mengambil keputusan.

## 1. Populasi vs Sampel
Sebelum melangkah lebih jauh, kita harus paham dari mana data itu berasal.

*   **Populasi:** Keseluruhan objek yang ingin kita teliti. (Contoh: Seluruh siswa SMA di Indonesia).
*   **Sampel:** Sebagian kecil dari populasi yang kita ambil datanya untuk mewakili populasi tersebut. (Contoh: 1000 siswa SMA yang dipilih secara acak).

> [!question] Mengapa pakai sampel?
> Karena meneliti seluruh populasi seringkali memakan waktu, biaya, dan tenaga yang tidak masuk akal. Sampel adalah "jalan pintas" yang cerdas jika diambil dengan benar.

---

## 2. Penyajian Data: Mengubah Kekacauan Menjadi Pola
Data mentah yang baru dikumpulkan biasanya berantakan. Otak manusia sulit melihat pola pada deretan angka yang panjang. Oleh karena itu, kita harus menyajikannya secara visual.

### A. Data Tunggal
Data tunggal adalah data yang belum dikelompokkan ke dalam kelas-kelas interval. Cocok untuk jumlah data yang sedikit.

*   **Tabel:** Menyajikan data dalam baris dan kolom.
*   **Diagram Batang:** Membandingkan kategori (panjang batang = frekuensi).
*   **Diagram Garis:** Melihat tren atau perubahan dari waktu ke waktu.
*   **Diagram Lingkaran (Pie Chart):** Melihat proporsi atau persentase dari keseluruhan.

### B. Data Berkelompok
> [!note] Mengapa data harus dikelompokkan?
> Bayangkan kamu punya nilai ujian dari 1000 siswa dengan rentang 0 sampai 100. Jika dibuat tabel data tunggal, tabelnya akan sangat panjang (100 baris!). Otak kita kembali kebingungan.
> Solusinya: Kita kelompokkan data ke dalam "kamar-kamar" atau **kelas interval**. (Misal: nilai 0-10, 11-20, dst). Pengelompokan ini **mengorbankan sedikit detail (kita tidak tahu persis nilai tiap anak) demi mendapatkan gambaran besar (big picture) yang jauh lebih jelas.**

**Cara Menyajikan Data Berkelompok:**
1.  **Tabel Distribusi Frekuensi:** Tabel yang berisi kelas interval dan frekuensinya.
2.  **Histogram:** Mirip diagram batang, tapi batang-batangnya saling menempel (karena datanya kontinu/berkelanjutan antar kelas).
3.  **Poligon Frekuensi:** Garis yang menghubungkan titik tengah setiap puncak batang histogram.
4.  **Ogive (Grafik Frekuensi Kumulatif):** Menunjukkan jumlah total data yang berada di bawah atau di atas suatu nilai batas.

---

## 3. Ukuran Pemusatan Data: Mencari "Titik Gravitasi" Data
Jika kita harus mewakili seluruh kumpulan data hanya dengan **satu angka**, angka berapakah itu? Itulah yang disebut ukuran pemusatan data.

### A. Rata-rata (Mean)
> [!tip] First-Principle Mean
> Mean adalah konsep **"berbagi adil"**. Bayangkan ada 5 anak dengan jumlah permen berbeda. Jika semua permen dikumpulkan di tengah, lalu dibagikan kembali sama rata ke setiap anak, jumlah permen yang didapat setiap anak adalah **Mean**.

*   **Data Tunggal:**
    $$\bar{x} = \frac{\sum x_i}{n}$$
    *(Jumlahkan semua nilai, bagi dengan banyak data)*

*   **Data Berkelompok:**
    Karena kita tidak tahu nilai pastinya (hanya tahu rentang kelas), kita gunakan **titik tengah ($x_i$)** sebagai perwakilan setiap kelas.
    $$\bar{x} = \frac{\sum (f_i \cdot x_i)}{\sum f_i}$$
    *(Kalikan frekuensi kelas dengan titik tengahnya, jumlahkan, lalu bagi dengan total frekuensi)*

### B. Nilai Tengah (Median)
> [!tip] First-Principle Median
> Median adalah konsep **"pembatas dua kubu"**. Ia membagi data yang sudah diurutkan menjadi dua bagian yang persis sama banyak (50% di bawah, 50% di atas).
> 
> **Kapan median lebih baik dari mean?** Ketika ada pencilan (*outlier*). Jika 9 orang punya uang Rp10.000 dan 1 orang punya Rp1.000.000.000, mean-nya akan menjadi Rp100 juta lebih (sangat menipu!). Median akan tetap Rp10.000, memberikan gambaran yang lebih realistis tentang kondisi mayoritas.

*   **Data Tunggal:**
    Urutkan data dari terkecil ke terbesar, lalu cari nilai di posisi tengah.

*   **Data Berkelompok:**
    Katakanlah median jatuh di "kelas" tertentu. Di mana persisnya letak median dalam kelas itu? Kita asumsikan data menyebar merata di dalam kelas tersebut, sehingga kita gunakan interpolasi (perbandingan linier):
    $$Me = L_m + \left( \frac{\frac{n}{2} - F_{kum}}{f_m} \right) \cdot p$$
    Di mana:
    - $L_m$ = Tepi bawah kelas median
    - $n$ = Total frekuensi (banyak data)
    - $F_{kum}$ = Frekuensi kumulatif **sebelum** kelas median
    - $f_m$ = Frekuensi kelas median
    - $p$ = Panjang kelas (interval)

### C. Modus (Nilai Paling Populer)
> [!tip] First-Principle Modus
> Modus mencari "apa yang paling sering terjadi/muncul". Ini sangat berguna untuk data kategorikal (misal: warna mobil paling laris tidak bisa dicari rata-ratanya, tapi bisa dicari modusnya).

*   **Data Tunggal:** Cari data dengan frekuensi kemunculan terbanyak.
*   **Data Berkelompok:**
    Kita tahu kelas mana yang frekuensinya tertinggi. Tapi titik pastinya di mana? Tarik menarik terjadi dengan kelas tetangganya. Semakin besar frekuensi kelas sebelum/sesudahnya, titik modus akan semakin tertarik ke arah mereka.
    $$Mo = L_o + \left( \frac{d_1}{d_1 + d_2} \right) \cdot p$$
    Di mana:
    - $L_o$ = Tepi bawah kelas modus
    - $d_1$ = Selisih frekuensi kelas modus dengan kelas **sebelumnya**
    - $d_2$ = Selisih frekuensi kelas modus dengan kelas **sesudahnya**
    - $p$ = Panjang kelas

---

## 4. Ukuran Letak Data: Membedah Data Lebih Rinci
Jika median membelah data menjadi 2 bagian yang sama, bagaimana jika kita ingin membelahnya lebih detil?

### A. Kuartil (Membelah 4)
Membagi data yang terurut menjadi 4 bagian yang sama banyak (masing-masing 25%). Ada $Q_1$ (Kuartil Bawah), $Q_2$ (Median/Kuartil Tengah), dan $Q_3$ (Kuartil Atas).

*   **Data Tunggal:** Cari posisi letak $Q_i = \frac{i(n+1)}{4}$.
*   **Data Berkelompok:** Rumusnya persis seperti Median, hanya letaknya yang berubah.
    $$Q_i = L_q + \left( \frac{\frac{i \cdot n}{4} - F_{kum}}{f_q} \right) \cdot p \quad \text{untuk } i = 1, 2, 3$$

### B. Desil (Membelah 10) & Persentil (Membelah 100)
Konsepnya persis sama dengan Kuartil, hanya pembaginya yang berbeda.

*   **Desil (Data Berkelompok):**
    $$D_i = L_d + \left( \frac{\frac{i \cdot n}{10} - F_{kum}}{f_d} \right) \cdot p \quad \text{untuk } i = 1, 2, \dots, 9$$
*   **Persentil (Data Berkelompok):**
    $$P_i = L_p + \left( \frac{\frac{i \cdot n}{100} - F_{kum}}{f_p} \right) \cdot p \quad \text{untuk } i = 1, 2, \dots, 99$$

> [!example] Makna Persentil
> Jika kamu berada di persentil ke-90 pada sebuah ujian, itu berarti nilaimu lebih baik dari 90% peserta ujian lainnya.

---

## 5. Ukuran Penyebaran Data: Seberapa Berantakan Data Kita?
Hanya mengetahui rata-rata tidaklah cukup. Bayangkan dua negara dengan rata-rata pendapatan warga Rp 5.000.000/bulan.
- Negara A: Hampir semua warganya bergaji 5 juta. (Penyebaran kecil)
- Negara B: Setengahnya miskin (Rp 0), setengahnya konglomerat (Rp 10.000.000). Rata-ratanya tetap 5 juta! (Penyebaran besar)

Ukuran penyebaran memberi tahu kita seberapa "berantakan" atau "konsisten" data tersebut dari titik pusatnya.

### A. Jangkauan (Range) & Jangkauan Antarkuartil (Hamparan)
*   **Jangkauan (Range):** Selisih nilai terbesar dan terkecil.
    $$R = X_{max} - X_{min}$$
    Kelemahan: Sangat rentan terhadap outlier.
*   **Jangkauan Antarkuartil (Hamparan):** Selisih antara $Q_3$ dan $Q_1$. Mengukur rentang tempat 50% data di tengah berkumpul. Lebih kebal terhadap outlier.
    $$H = Q_3 - Q_1$$

### B. Simpangan Rata-rata (Mean Deviation)
> [!tip] First-Principle Simpangan Rata-rata
> Secara harfiah berarti: "Rata-rata dari jarak setiap data terhadap titik pusat (mean)". Karena jarak tidak mungkin negatif, kita gunakan nilai mutlak.

*   **Data Tunggal:**
    $$SR = \frac{\sum |x_i - \bar{x}|}{n}$$
*   **Data Berkelompok:**
    $$SR = \frac{\sum f_i \cdot |x_i - \bar{x}|}{\sum f_i}$$

### C. Ragam (Variansi) dan Simpangan Baku (Standar Deviasi)
Simpangan rata-rata bermasalah secara matematis karena menggunakan nilai mutlak (susah diturunkan dalam kalkulus). Oleh karena itu, ahli matematika mencari cara lain menghilangkan nilai negatif: **dikuadratkan**.

> [!tip] First-Principle Variansi & Standar Deviasi
> **Ragam (Variansi):** Adalah rata-rata dari "jarak kuadrat" setiap data ke mean. Karena satuannya menjadi kuadrat (misal data awalnya 'rupiah', ragamnya 'rupiah kuadrat'), angka ini sulit diinterpretasikan di dunia nyata.
> 
> **Simpangan Baku (Standar Deviasi):** Adalah akar dari Ragam. Kita mengakarkan kembali hasil ragam agar satuannya kembali seperti semula (kembali ke 'rupiah'). Ini adalah ukuran penyebaran yang paling standar dan sering dipakai.

*   **Ragam (Variansi) Data Tunggal:**
    $$S^2 = \frac{\sum (x_i - \bar{x})^2}{n}$$
*   **Ragam (Variansi) Data Berkelompok:**
    $$S^2 = \frac{\sum f_i \cdot (x_i - \bar{x})^2}{\sum f_i}$$

*   **Simpangan Baku ($S$ atau $\sigma$):**
    Cukup akarkan nilai ragam:
    $$S = \sqrt{S^2}$$

> [!info] Mengapa dibagi (n-1) pada populasi vs sampel?
> Pada praktiknya (terutama jika belajar statistika lebih lanjut), jika kita menghitung variansi untuk **sampel** (bukan seluruh populasi), pembaginya bukan $n$, melainkan $n-1$. Ini dilakukan untuk mengkoreksi *bias* agar perkiraan kita terhadap populasi lebih akurat. Namun untuk tingkat SMA, biasanya tetap menggunakan $n$ kecuali diminta spesifik variansi sampel.

---

## 6. Studi Kasus & Contoh Perhitungan (Data Berkelompok)
Agar tidak sekadar menghafal rumus, mari kita praktekkan pada data nyata. Berikut adalah data fiktif Nilai Ujian Matematika dari 40 siswa.

### Tabel Distribusi Frekuensi

| Nilai (Kelas) | Frekuensi ($f_i$) | Titik Tengah ($x_i$) | $f_i \cdot x_i$ | Frek. Kumulatif ($F_{kum}$) |
| :---: | :---: | :---: | :---: | :---: |
| 41 - 50 | 4 | 45.5 | 182 | 4 |
| 51 - 60 | 6 | 55.5 | 333 | 10 |
| 61 - 70 | 10 | 65.5 | 655 | 20 |
| 71 - 80 | 12 | 75.5 | 906 | 32 |
| 81 - 90 | 5 | 85.5 | 427.5 | 37 |
| 91 - 100 | 3 | 95.5 | 286.5 | 40 |
| **Total** | **$\sum f_i = 40$** | | **$\sum (f_i \cdot x_i) = 2790$** | |

> [!note] Panjang Kelas ($p$)
> Hati-hati! Panjang kelas dari 41 - 50 **bukanlah** $50 - 41 = 9$. Cara menghitungnya adalah menggunakan jari (41, 42, 43, 44, 45, 46, 47, 48, 49, 50) sehingga panjang kelasnya adalah **10**. 
> Atau secara matematis: Tepi Atas - Tepi Bawah = $50.5 - 40.5 = 10$.

### A. Menghitung Rata-rata (Mean)
Berdasarkan tabel di atas, perhitungannya sangat sederhana karena kita sudah mencari total $f_i \cdot x_i$.

$$\bar{x} = \frac{\sum (f_i \cdot x_i)}{\sum f_i} = \frac{2790}{40} = 69.75$$
Jadi, rata-rata nilai matematika di kelas tersebut adalah **69.75**.

### B. Menghitung Nilai Tengah (Median)
*   **Total data ($n$) = 40.** Median membelah data persis di tengah, yaitu letak data ke $\frac{40}{2} = 20$.
*   Lihat kolom **Frekuensi Kumulatif ($F_{kum}$)**. Data ke-20 terletak di kelas **61 - 70** (karena pada kelas ini frekuensi kumulatifnya genap mencapai angka 20).
*   **Kelas Median: 61 - 70**
    *   Tepi Bawah ($L_m$) = $61 - 0.5 = 60.5$
    *   Frek. kumulatif sebelum kelas median ($F_{kum}$) = $10$ (dari kelas 51-60)
    *   Frek. kelas median ($f_m$) = $10$
    *   Panjang kelas ($p$) = $10$

$$Me = L_m + \left( \frac{\frac{n}{2} - F_{kum}}{f_m} \right) \cdot p$$
$$Me = 60.5 + \left( \frac{20 - 10}{10} \right) \cdot 10 = 60.5 + (1) \cdot 10 = 70.5$$

### C. Menghitung Modus
*   Kelas dengan frekuensi terbanyak (paling populer) adalah **71 - 80** dengan frekuensi 12.
*   **Kelas Modus: 71 - 80**
    *   Tepi Bawah ($L_o$) = $71 - 0.5 = 70.5$
    *   $d_1$ (selisih dengan kelas sebelumnya/atasnya) = $12 - 10 = 2$
    *   $d_2$ (selisih dengan kelas sesudahnya/bawahnya) = $12 - 5 = 7$
    *   Panjang kelas ($p$) = $10$

$$Mo = L_o + \left( \frac{d_1}{d_1 + d_2} \right) \cdot p$$
$$Mo = 70.5 + \left( \frac{2}{2 + 7} \right) \cdot 10 = 70.5 + \frac{20}{9} = 70.5 + 2.22 = 72.72$$

### D. Cheat Sheet / Ringkasan

| Ukuran | Fungsi Utama | Kapan Digunakan? | Kelemahan |
| :--- | :--- | :--- | :--- |
| **Mean** | Mencari "titik berat" semua nilai | Distribusi data normal/merata | Sangat rentan jika ada *outlier* (nilai ekstrim) |
| **Median** | Membagi data 50/50 | Data memiliki *outlier* (karena kebal outlier) | Mengabaikan nilai aktual di ekor data |
| **Modus** | Menemukan nilai paling populer | Data kategorikal (warna, rasa, merk) | Kurang menggambarkan distribusi nilai numerik |
| **Simpangan Baku** | Mengukur rata-rata penyebaran | Melihat konsistensi kualitas/nilai | Perhitungan cukup rumit |