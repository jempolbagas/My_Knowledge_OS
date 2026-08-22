---
title: "Latihan Soal Terbimbing: Relasi (Relations)"
course: Discrete Mathematics I
tags: ["discrete-mathematics", "math", "relations", "practice"]
aliases: ["Latihan Relasi", "Soal Relasi"]
created: "2026-06-21"
---

# Latihan Soal Terbimbing: Relasi (Relations)

Halo! Selamat datang di lembar latihan soal terbimbing untuk materi **Relasi (Relations)**. Di sini, kita bakal menguji pemahaman kita terhadap konsep-konsep teoritis relasi yang sudah kita pelajari di [[Complete Guide|Panduan Lengkap: Relasi]].

Biar belajarnya makin mantap, setiap soal di bawah ini disajikan dengan:
1. **Pertanyaan Formal:** Ditulis secara formal matematis sebagaimana tipe soal yang biasa keluar di ujian (UTS/UAS).
2. **Intuisi & Analisis Kasus:** Penjelasan dengan bahasa santai untuk membedah logika soal sebelum masuk ke rumus.
3. **Solusi Matematis Formal:** Langkah demi langkah pembuktian dan perhitungan menggunakan notasi matematika dan LaTeX yang presisi.
4. **Tips & Jebakan:** Catatan penting mengenai kesalahan umum yang sering dilakukan mahasiswa.

Yuk, langsung kita bongkar soal-soalnya!

---

## 1. Analisis & Pembuktian Sifat-Sifat Relasi

> [!example] Soal 1: Membuktikan Sifat Relasi pada Himpunan Tak Hingga
> **Pertanyaan:**
> Misalkan $\mathbb{Z}$ adalah himpunan semua bilangan bulat. Sebuah relasi biner $R$ didefinisikan pada $\mathbb{Z}$ sebagai berikut:
> Untuk setiap $a, b \in \mathbb{Z}$, $a \mathrel{R} b$ jika dan hanya jika $3 \mid (a - b)$ (artinya $a - b$ habis dibagi oleh $3$).
> 
> Buktikan secara formal apakah relasi $R$ bersifat:
> a. Refleksif
> b. Simetris
> c. Antisimetris
> d. Transitif
> 
> ---
> 
> **Pembahasan:**
> 
> ### 1. Intuisi & Analisis Kasus
> Di soal pertama ini, kita disuruh ngecek sifat-sifat relasi di himpunan bilangan bulat $\mathbb{Z}$. Hubungan relasinya itu $a \mathrel{R} b$ kalau selisih mereka, yaitu $a-b$, adalah kelipatan 3 (habis dibagi 3).
> 
> Biar gampang dapet *feel*-nya, mari kita ceki-ceki pake angka acak dulu:
> - Ambil $7$ dan $4$. Selisihnya $7 - 4 = 3$. Karena $3$ habis dibagi $3$, maka $(7, 4) \in R$ alias $7 \mathrel{R} 4$.
> - Ambil $5$ dan $2$. Selisihnya $5 - 2 = 3$. Sama, berarti $5 \mathrel{R} 2$.
> - Ambil $5$ dan $1$. Selisihnya $5 - 1 = 4$. Karena $4$ tidak habis dibagi $3$, maka $(5, 1) \notin R$.
> 
> Nah, dari sini kita kudu buktiin sifatnya secara umum pake variabel (misal $a, b, c$), nggak boleh cuma pake contoh angka kalau mau membuktikan sifat itu **benar**. Sebaliknya, kalau mau menyangkal (menyatakan sifat itu **salah**), kita cukup kasih **satu contoh penyangkal** (*counterexample*) aja.
> 
> ### 2. Solusi Matematis Formal
> Definisi relasi: $a \mathrel{R} b \iff a - b = 3k$ untuk suatu bilangan bulat $k \in \mathbb{Z}$.
> 
> **a. Refleksif:**
> Kita harus membuktikan bahwa untuk setiap $a \in \mathbb{Z}$, berlaku $(a, a) \in R$.
> - Ambil sembarang $a \in \mathbb{Z}$. Kita periksa nilai $a - a$:
>   $$a - a = 0$$
> - Karena $0 = 3 \times 0$ dan $0 \in \mathbb{Z}$, maka $3 \mid (a - a)$.
> - Dengan demikian, $(a, a) \in R$ untuk setiap $a \in \mathbb{Z}$.
> - **Kesimpulan:** Relasi $R$ bersifat **refleksif**.
> 
> **b. Simetris:**
> Kita harus membuktikan bahwa jika $(a, b) \in R$, maka $(b, a) \in R$.
> - Asumsikan $(a, b) \in R$. Berdasarkan definisi relasi, maka $3 \mid (a - b)$, yang berarti terdapat bilangan bulat $k$ sedemikian rupa sehingga:
>   $$a - b = 3k$$
> - Kita ingin memeriksa nilai $b - a$:
>   $$b - a = -(a - b) = -(3k) = 3(-k)$$
> - Karena $k \in \mathbb{Z}$, maka $-k$ juga pasti bilangan bulat ($-k \in \mathbb{Z}$). Oleh karena itu, $3 \mid (b - a)$, yang berarti $(b, a) \in R$.
> - **Kesimpulan:** Relasi $R$ bersifat **simetris**.
> 
> **c. Antisimetris:**
> Kita periksa apakah jika $(a, b) \in R$ dan $(b, a) \in R$, maka $a = b$.
> - Mari kita cari contoh penyangkal (*counterexample*).
> - Ambil $a = 4$ dan $b = 1$.
>   - $4 - 1 = 3 = 3(1) \implies 3 \mid (4 - 1) \implies (4, 1) \in R$.
>   - $1 - 4 = -3 = 3(-1) \implies 3 \mid (1 - 4) \implies (1, 4) \in R$.
> - Namun, jelas bahwa $4 \neq 1$.
> - Karena kita menemukan pasangan $a, b$ di mana $a \mathrel{R} b$ dan $b \mathrel{R} a$ tetapi $a \neq b$, maka relasi $R$ **tidak bersifat antisimetris**.
> 
> **d. Transitif:**
> Kita harus membuktikan bahwa jika $(a, b) \in R$ dan $(b, c) \in R$, maka $(a, c) \in R$.
> - Asumsikan $(a, b) \in R$ dan $(b, c) \in R$. Berdasarkan definisi, maka terdapat bilangan bulat $k_1$ dan $k_2$ sedemikian rupa sehingga:
>   $$a - b = 3k_1$$
>   $$b - c = 3k_2$$
> - Kita ingin menunjukkan bahwa $a - c$ adalah kelipatan 3. Kita jumlahkan kedua persamaan di atas:
>   $$(a - b) + (b - c) = 3k_1 + 3k_2$$
>   $$a - c = 3(k_1 + k_2)$$
> - Karena $k_1, k_2 \in \mathbb{Z}$, maka $(k_1 + k_2) \in \mathbb{Z}$. Oleh karena itu, $3 \mid (a - c)$, yang berarti $(a, c) \in R$.
> - **Kesimpulan:** Relasi $R$ bersifat **transitif**.
> 
> ### 3. Tips & Jebakan
> > [!warning] Jebakan Antisimetris
> > Banyak yang keliru mengira "antisimetris" itu adalah kebalikan mutlak dari "simetris" (artinya kalau simetris pasti gak antisimetris, dan sebaliknya). Padahal nggak gitu lho! Ada relasi yang simetris sekaligus antisimetris (contoh: relasi identitas $a = b$), dan ada yang tidak dua-duanya (seperti relasi $R$ di atas). Ingat baik-baik definisinya: antisimetris melarang adanya hubungan bolak-balik *kecuali* jika elemennya sama.

---

## 2. Relasi n-ary dan Operasi Database Relasional

> [!example] Soal 2: Operasi Aljabar Relasional pada Basis Data
> **Pertanyaan:**
> Misalkan terdapat tiga buah domain (himpunan) sebagai berikut:
> - $\text{NIM} = \{101, 102, 103\}$
> - $\text{Nama} = \{\text{'Andi'}, \text{'Budi'}, \text{'Cici'}\}$
> - $\text{Mata\_Kuliah} = \{\text{'Matdis I'}, \text{'Struktur Data'}, \text{'Basis Data'}\}$
> 
> Diberikan relasi ternary (3-ary) $R \subseteq \text{NIM} \times \text{Nama} \times \text{Mata\_Kuliah}$ yang menyatakan data pengambilan mata kuliah oleh mahasiswa:
> $$R = \{(101, \text{'Andi'}, \text{'Matdis I'}), (101, \text{'Andi'}, \text{'Basis Data'}), (102, \text{'Budi'}, \text{'Matdis I'}), (103, \text{'Cici'}, \text{'Struktur Data'})\mathbb{\}}$$
> 
> Serta sebuah relasi biner $S \subseteq \text{Mata\_Kuliah} \times \text{Dosen}$ yang menyatakan dosen pengampu mata kuliah:
> $$S = \{(\text{'Matdis I'}, \text{'Dr. Heri'}), (\text{'Struktur Data'}, \text{'Dr. Saptono'}), (\text{'Basis Data'}, \text{'Dr. Retno'})\mathbb{\}}$$
> 
> Tentukan hasil dari operasi-operasi aljabar relasional berikut:
> a. Operasi seleksi $\sigma_{\text{Mata\_Kuliah} = \text{'Matdis I'}}(R)$
> b. Operasi proyeksi $\Pi_{\text{Nama}, \text{Mata\_Kuliah}}(R)$
> c. Operasi join $R \bowtie S$ (natural join berdasarkan atribut $\text{Mata\_Kuliah}$)
> 
> ---
> 
> **Pembahasan:**
> 
> ### 1. Intuisi & Analisis Kasus
> Bayangin kita lagi ngerjain tugas database tapi versi matematika diskrit. Konsep tabel database itu sebenarnya adalah relasi n-ary di mana baris-baris data adalah tuple-tuple di dalam relasi tersebut.
> 
> - **Seleksi ($\sigma$):** Ini mirip perintah `WHERE` di SQL. Kita cuma memfilter baris-baris (tuple) yang memenuhi kriteria tertentu. Kolomnya tetap lengkap, cuma barisnya aja yang tersaring.
> - **Proyeksi ($\Pi$):** Ini mirip perintah `SELECT nama, matkul` di SQL. Kita cuma mengambil kolom tertentu aja dan membuang kolom sisanya. Ingat, karena hasil proyeksi adalah sebuah *himpunan*, kalau ada baris duplikat setelah kolom lain dibuang, kita kudu menulisnya **satu kali saja** (duplikat dieliminasi!).
> - **Join ($\bowtie$):** Ini menggabungkan dua tabel berdasarkan kolom yang namanya sama (dalam hal ini `Mata_Kuliah`). Tiap tuple dari $R$ yang punya nama matkul tertentu ditempelkan dengan tuple dari $S$ yang punya nama matkul yang cocok.
> 
> ### 2. Solusi Matematis Formal
> 
> **a. Seleksi $\sigma_{\text{Mata\_Kuliah} = \text{'Matdis I'}}(R)$:**
> Kita memfilter tuple $(x_1, x_2, x_3) \in R$ yang komponen ketiganya ($\text{Mata\_Kuliah}$) bernilai `'Matdis I'`.
> Tuple-tuple yang memenuhi kriteria adalah:
> 1. $(101, \text{'Andi'}, \text{'Matdis I'})$
> 2. $(102, \text{'Budi'}, \text{'Matdis I'})$
> 
> Sehingga hasil operasinya adalah:
> $$\sigma_{\text{Mata\_Kuliah} = \text{'Matdis I'}}(R) = \{(101, \text{'Andi'}, \text{'Matdis I'}), (102, \text{'Budi'}, \text{'Matdis I'})\mathbb{\}}$$
> 
> **b. Proyeksi $\Pi_{\text{Nama}, \text{Mata\_Kuliah}}(R)$:**
> Kita mengambil komponen kedua (Nama) dan ketiga (Mata_Kuliah) dari setiap tuple di $R$.
> Pemetaan dari masing-masing tuple $R$:
> - $(101, \text{'Andi'}, \text{'Matdis I'}) \to (\text{'Andi'}, \text{'Matdis I'})$
> - $(101, \text{'Andi'}, \text{'Basis Data'}) \to (\text{'Andi'}, \text{'Basis Data'})$
> - $(102, \text{'Budi'}, \text{'Matdis I'}) \to (\text{'Budi'}, \text{'Matdis I'})$
> - $(103, \text{'Cici'}, \text{'Struktur Data'}) \to (\text{'Cici'}, \text{'Struktur Data'})$
> 
> Karena tidak ada pasangan yang sama (duplikat), semua pasangan dimasukkan ke dalam himpunan hasil:
> $$\Pi_{\text{Nama}, \text{Mata\_Kuliah}}(R) = \{(\text{'Andi'}, \text{'Matdis I'}), (\text{'Andi'}, \text{'Basis Data'}), (\text{'Budi'}, \text{'Matdis I'}), (\text{'Cici'}, \text{'Struktur Data'})\mathbb{\}}$$
> 
> **c. Join $R \bowtie S$:**
> Kita mencocokkan atribut $\text{Mata\_Kuliah}$ antara relasi $R$ (komponen ke-3) dan relasi $S$ (komponen ke-1). Hasil dari natural join adalah 4-tuple dengan format $(\text{NIM}, \text{Nama}, \text{Mata\_Kuliah}, \text{Dosen})$.
> - Tuple $(101, \text{'Andi'}, \text{'Matdis I'})$ dari $R$ cocok dengan $(\text{'Matdis I'}, \text{'Dr. Heri'})$ dari $S$ $\to (101, \text{'Andi'}, \text{'Matdis I'}, \text{'Dr. Heri'})$
> - Tuple $(101, \text{'Andi'}, \text{'Basis Data'})$ dari $R$ cocok dengan $(\text{'Basis Data'}, \text{'Dr. Retno'})$ dari $S$ $\to (101, \text{'Andi'}, \text{'Basis Data'}, \text{'Dr. Retno'})$
> - Tuple $(102, \text{'Budi'}, \text{'Matdis I'})$ dari $R$ cocok dengan $(\text{'Matdis I'}, \text{'Dr. Heri'})$ dari $S$ $\to (102, \text{'Budi'}, \text{'Matdis I'}, \text{'Dr. Heri'})$
> - Tuple $(103, \text{'Cici'}, \text{'Struktur Data'})$ dari $R$ cocok dengan $(\text{'Struktur Data'}, \text{'Dr. Saptono'})$ dari $S$ $\to (103, \text{'Cici'}, \text{'Struktur Data'}, \text{'Dr. Saptono'})$
> 
> Sehingga hasil join-nya adalah:
> $$R \bowtie S = \{
>   (101, \text{'Andi'}, \text{'Matdis I'}, \text{'Dr. Heri'}), 
>   (101, \text{'Andi'}, \text{'Basis Data'}, \text{'Dr. Retno'}), 
>   (102, \text{'Budi'}, \text{'Matdis I'}, \text{'Dr. Heri'}), 
>   (103, \text{'Cici'}, \text{'Struktur Data'}, \text{'Dr. Saptono'})
> \mathbb{\}}$$
> 
> ### 3. Tips & Jebakan
> > [!tip] Eliminasi Duplikat pada Proyeksi
> > Di database relasional teoritis, hasil dari proyeksi $\Pi$ **harus berupa himpunan matematika**. Himpunan tidak boleh mengandung elemen duplikat. Jadi kalau misal kita memproyeksikan kolom NIM dari relasi $R$, meskipun NIM 101 muncul dua kali di relasi asal, di hasil akhir $\Pi_{\text{NIM}}(R)$ kita cuma nulis $\{101, 102, 103\}$ (tidak boleh $\{101, 101, 102, 103\}$). Ceki-ceki lagi jawabanmu pas ujian ya!

---

## 3. Transitive Closure & Algoritma Warshall

> [!example] Soal 3: Menghitung Transitive Closure dengan Algoritma Warshall
> **Pertanyaan:**
> Diberikan sebuah himpunan $A = \{1, 2, 3, 4\}$ dan sebuah relasi biner $R$ pada $A$ yang didefinisikan oleh graf berarah sebagai berikut:
> 
> ```mermaid
> graph LR
>     1 --> 2
>     2 --> 3
>     3 --> 4
>     4 --> 1
> ```
> 
> Tentukan *transitive closure* dari relasi $R$, dilambangkan dengan $R^*$, menggunakan **Algoritma Warshall** langkah-demi-langkah dengan menuliskan matriks transisi $W^{(0)}, W^{(1)}, W^{(2)}, W^{(3)}, \text{dan } W^{(4)}$.
> 
> ---
> 
> **Pembahasan:**
> 
> ### 1. Intuisi & Analisis Kasus
> Mencari *transitive closure* secara manual di graf kecil mungkin gampang, tinggal nyari "siapa bisa nyampe ke siapa lewat jalan mana aja". Tapi kalau grafnya gede atau kalau dosen minta nunjukin langkah Algoritma Warshall, kita kudu pakai cara matriks.
> 
> Algoritma Warshall ini bekerja secara bertahap. Misalkan simpul-simpul kita adalah $1, 2, 3, 4$.
> - Matriks awal $W^{(0)}$ adalah matriks representasi relasi asli $R$.
> - Untuk membuat matriks $W^{(k)}$ dari $W^{(k-1)}$, aturan gampangnya begini: kita cek simpul $k$ sebagai **perantara**. Jika ada jalan dari simpul $i$ ke simpul $k$ (artinya $W^{(k-1)}[i,k] = 1$) DAN ada jalan dari simpul $k$ ke simpul $j$ (artinya $W^{(k-1)}[k,j] = 1$), maka kita tambahkan jalan langsung dari $i$ ke $j$ di matriks $W^{(k)}$ (kita set $W^{(k)}[i,j] = 1$).
> 
> Mari kita lakukan secara bertahap untuk $k = 1, 2, 3, 4$!
> 
> ### 2. Solusi Matematis Formal
> Simpul pada himpunan $A$ adalah $1, 2, 3, 4$.
> Relasi awal $R = \{(1, 2), (2, 3), (3, 4), (4, 1)\}$.
> 
> **Langkah 0: Matriks Awal $W^{(0)}$**
> Matriks ketetanggaan awal dari relasi $R$ adalah:
> $$W^{(0)} = \begin{bmatrix}
> 0 & 1 & 0 & 0 \\
> 0 & 0 & 1 & 0 \\
> 0 & 0 & 0 & 1 \\
> 1 & 0 & 0 & 0
> \end{bmatrix}$$
> 
> **Langkah 1: Menghitung $W^{(1)}$ (Simpul 1 sebagai perantara)**
> Kita periksa baris dan kolom ke-1 dari $W^{(0)}$. 
> - Kolom ke-1 memiliki nilai 1 di baris ke-4 ($W^{(0)}[4,1] = 1$). 
> - Baris ke-1 memiliki nilai 1 di kolom ke-2 ($W^{(0)}[1,2] = 1$).
> - Maka kita harus menetapkan nilai 1 pada koordinat $(4,2)$ di matriks $W^{(1)}$.
> $$W^{(1)} = \begin{bmatrix}
> 0 & 1 & 0 & 0 \\
> 0 & 0 & 1 & 0 \\
> 0 & 0 & 0 & 1 \\
> 1 & \mathbf{1} & 0 & 0
> \end{bmatrix}$$
> 
> **Langkah 2: Menghitung $W^{(2)}$ (Simpul 2 sebagai perantara)**
> Kita gunakan $W^{(1)}$. Kita cari mana saja baris $i$ yang memiliki nilai 1 di kolom 2, dan kolom $j$ mana saja yang memiliki nilai 1 di baris 2.
> - Kolom ke-2 memiliki nilai 1 di baris 1 dan baris 4. 
> - Baris ke-2 memiliki nilai 1 di kolom 3.
> - Maka kita tambahkan nilai 1 pada koordinat $(1,3)$ dan $(4,3)$ di matriks $W^{(2)}$.
> $$W^{(2)} = \begin{bmatrix}
> 0 & 1 & \mathbf{1} & 0 \\
> 0 & 0 & 1 & 0 \\
> 0 & 0 & 0 & 1 \\
> 1 & 1 & \mathbf{1} & 0
> \end{bmatrix}$$
> 
> **Langkah 3: Menghitung $W^{(3)}$ (Simpul 3 sebagai perantara)**
> Kita gunakan $W^{(2)}$. 
> - Kolom ke-3 memiliki nilai 1 di baris 1, 2, dan 4. 
> - Baris ke-3 memiliki nilai 1 di kolom 4.
> - Maka kita tambahkan nilai 1 pada koordinat $(1,4)$, $(2,4)$, dan $(4,4)$ di matriks $W^{(3)}$.
> $$W^{(3)} = \begin{bmatrix}
> 0 & 1 & 1 & \mathbf{1} \\
> 0 & 0 & 1 & \mathbf{1} \\
> 0 & 0 & 0 & 1 \\
> 1 & 1 & 1 & \mathbf{1}
> \end{bmatrix}$$
> 
> **Langkah 4: Menghitung $W^{(4)}$ (Simpul 4 sebagai perantara)**
> Kita gunakan $W^{(3)}$. 
> - Kolom ke-4 memiliki nilai 1 di baris 1, 2, 3, dan 4. 
> - Baris ke-4 memiliki nilai 1 di kolom 1, 2, 3, dan 4.
> - Karena simpul 4 terhubung dari semua simpul dan terhubung ke semua simpul, maka untuk setiap baris $i$ dan kolom $j$, $W^{(4)}[i,j]$ akan menjadi 1.
> $$W^{(4)} = \begin{bmatrix}
> \mathbf{1} & 1 & 1 & 1 \\
> \mathbf{1} & \mathbf{1} & 1 & 1 \\
> \mathbf{1} & \mathbf{1} & \mathbf{1} & 1 \\
> 1 & 1 & 1 & 1
> \end{bmatrix}$$
> 
> Matriks $W^{(4)}$ adalah matriks final dari *transitive closure* $R^*$.
> Himpunan relasi dari $R^*$ adalah:
> $$R^* = \{(a, b) \mid a, b \in \{1, 2, 3, 4\}\}$$
> 
> ### 3. Tips & Jebakan
> > [!important] Cara Cepat Warshall di Kertas Cakar
> > Biar nggak pusing ngecek satu-satu sel matriks, di langkah $k$, cari posisi angka 1 di kolom $k$ dan baris $k$. Misalkan di $W^{(k-1)}$, angka 1 di kolom $k$ ada di baris-baris $I = \{i_1, i_2, \dots\}$, dan angka 1 di baris $k$ ada di kolom-kolom $J = \{j_1, j_2, \dots\}$. Kita tinggal melakukan perkalian silang (*cross product*) dari indeks-indeks tersebut, lalu langsung set koordinat $(i, j)$ tersebut bernilai 1. Cara ini jauh lebih hemat waktu dan mengurangi risiko salah hitung pas ujian!

---

## 4. Relasi Ekivalen, Kelas Ekivalen, & Partisi

> [!example] Soal 4: Membuktikan Relasi Ekivalen dan Hubungannya dengan Partisi Himpunan
> **Pertanyaan:**
> Misalkan $\mathbb{Z}$ adalah himpunan bilangan bulat. Sebuah relasi biner $R$ pada $\mathbb{Z}$ didefinisikan sebagai kekongruenan modulo 4:
> $$a \mathrel{R} b \iff a \equiv b \pmod 4$$
> 
> a. Buktikan secara formal bahwa relasi $R$ merupakan relasi ekivalen.
> b. Tentukan kelas-kelas ekivalen yang terbentuk dari relasi $R$.
> c. Tunjukkan secara formal bahwa kelas-kelas ekivalen tersebut membentuk partisi pada himpunan $\mathbb{Z}$.
> 
> ---
> 
> **Pembahasan:**
> 
> ### 1. Intuisi & Analisis Kasus
> Relasi ekivalen itu relasi yang mirip hubungan kesamaan ($=$), dia punya sifat RST (Refleksif, Simetris, Transitif).
> 
> Modulo 4 artinya sisa pembagian oleh 4. Bilangan bulat kalau dibagi 4 pasti sisanya cuma ada 4 kemungkinan: $0, 1, 2,$ atau $3$.
> - **Kelas ekivalen** $[r]$ itu isinya semua angka yang kalau dibagi 4 sisanya $r$. Jadi angka $0, 4, 8, -4$ bakal kumpul di kelas $[0]$. Angka $1, 5, 9, -3$ di kelas $[1]$, dan seterusnya.
> - **Partisi** itu artinya pembagian wilayah. Kalau kita gabungin kelas $[0], [1], [2], [3]$, kita dapet lagi seluruh bilangan bulat $\mathbb{Z}$. Dan nggak ada satu pun bilangan bulat yang punya dua sisa pembagian berbeda (artinya irisan antar kelas itu pasti kosong).
> 
> ### 2. Solusi Matematis Formal
> 
> **a. Bukti Relasi Ekivalen:**
> Untuk membuktikan $R$ adalah relasi ekivalen, kita harus menunjukkan sifat Refleksif, Simetris, dan Transitif.
> 
> 1. **Refleksif:**
>    - Ambil sembarang $a \in \mathbb{Z}$. Jelas bahwa $a - a = 0$.
>    - Karena $0 = 4 \times 0$, maka $4 \mid (a - a)$, yang berarti $a \equiv a \pmod 4$.
>    - Dengan demikian, $(a, a) \in R$ untuk setiap $a \in \mathbb{Z}$. (Refleksif terbukti)
> 2. **Simetris:**
>    - Asumsikan $a \mathrel{R} b$. Maka $a \equiv b \pmod 4$, yang berarti terdapat $k \in \mathbb{Z}$ sehingga:
>      $$a - b = 4k$$
>    - Kita peroleh $b - a = -(a - b) = -4k = 4(-k)$.
>    - Karena $k \in \mathbb{Z}$, maka $-k \in \mathbb{Z}$. Oleh karena itu, $b \equiv a \pmod 4$, yang berarti $b \mathrel{R} a$. (Simetris terbukti)
> 3. **Transitif:**
>    - Asumsikan $a \mathrel{R} b$ dan $b \mathrel{R} c$.
>    - Maka terdapat $k_1, k_2 \in \mathbb{Z}$ sedemikian rupa sehingga:
>      $$a - b = 4k_1 \quad \text{dan} \quad b - c = 4k_2$$
>    - Jika kita jumlahkan kedua persamaan tersebut:
>      $$(a - b) + (b - c) = 4k_1 + 4k_2$$
>      $$a - c = 4(k_1 + k_2)$$
>    - Karena $k_1 + k_2 \in \mathbb{Z}$, maka $a - c$ habis dibagi 4, yang berarti $a \equiv c \pmod 4$, atau $a \mathrel{R} c$. (Transitif terbukti)
> 
> Karena memenuhi sifat refleksif, simetris, dan transitif, maka $R$ adalah **relasi ekivalen**.
> 
> **b. Kelas-Kelas Ekivalen:**
> Kelas ekivalen dari elemen $a \in \mathbb{Z}$ didefinisikan sebagai $[a] = \{x \in \mathbb{Z} \mid x \mathrel{R} a\}$.
> Berdasarkan sisa pembagian oleh 4, terdapat 4 kelas ekivalen yang unik:
> - $[0] = \{x \in \mathbb{Z} \mid x \equiv 0 \pmod 4\} = \{\dots, -8, -4, 0, 4, 8, \dots\} = \{4k \mid k \in \mathbb{Z}\}$
> - $[1] = \{x \in \mathbb{Z} \mid x \equiv 1 \pmod 4\} = \{\dots, -7, -3, 1, 5, 9, \dots\} = \{4k + 1 \mid k \in \mathbb{Z}\}$
> - $[2] = \{x \in \mathbb{Z} \mid x \equiv 2 \pmod 4\} = \{\dots, -6, -2, 2, 6, 10, \dots\} = \{4k + 2 \mid k \in \mathbb{Z}\}$
> - $[3] = \{x \in \mathbb{Z} \mid x \equiv 3 \pmod 4\} = \{\dots, -5, -1, 3, 7, 11, \dots\} = \{4k + 3 \mid k \in \mathbb{Z}\}$
> 
> **c. Bukti Partisi Himpunan:**
> Misalkan $\mathcal{P} = \{[0], [1], [2], [3]\}$. Untuk menunjukkan $\mathcal{P}$ adalah partisi dari $\mathbb{Z}$, kita harus membuktikan dua syarat:
> 
> 1. **Saling Lepas (Pairwise Disjoint):** $[i] \cap [j] = \emptyset$ jika $i \neq j$ untuk $i, j \in \{0, 1, 2, 3\}$.
>    - *Bukti:* Andaikan terdapat $x \in [i] \cap [j]$ dengan $i \neq j$.
>    - Maka $x \equiv i \pmod 4$ dan $x \equiv j \pmod 4$.
>    - Berdasarkan sifat transitif kekongruenan, maka $i \equiv j \pmod 4$, yang berarti $4 \mid (i - j)$.
>    - Namun, karena $i, j \in \{0, 1, 2, 3\}$, selisih $|i - j|$ berada di rentang $[1, 3]$. Tidak ada bilangan di rentang ini yang habis dibagi 4 selain 0. Kontradiksi.
>    - Maka haruslah $[i] \cap [j] = \emptyset$.
> 
> 2. **Menyeluruh (Collective Exhaustive):** $\bigcup_{i=0}^{3} [i] = \mathbb{Z}$.
>    - *Bukti:* 
>      - Jelas bahwa $\bigcup_{i=0}^{3} [i] \subseteq \mathbb{Z}$ karena setiap kelas ekivalen berisi bilangan bulat.
>      - Untuk membuktikan $\mathbb{Z} \subseteq \bigcup_{i=0}^{3} [i]$, ambil sembarang $n \in \mathbb{Z}$. Berdasarkan Algoritma Pembagian (*Division Algorithm*), $n$ dapat ditulis secara unik sebagai:
>        $$n = 4q + r \quad \text{di mana } q \in \mathbb{Z} \text{ dan } r \in \{0, 1, 2, 3\}$$
>      - Ini berarti $n - r = 4q$, sehingga $n \equiv r \pmod 4$, yang berarti $n \in [r]$.
>      - Karena $r \in \{0, 1, 2, 3\}$, maka $n \in \bigcup_{i=0}^{3} [i]$.
>      - Maka terbukti bahwa gabungan seluruh kelas ekivalen mengembalikan himpunan $\mathbb{Z}$.
> 
> Dengan demikian, $\mathcal{P} = \{[0], [1], [2], [3]\}$ adalah **partisi** dari $\mathbb{Z}$.
> 
> ### 3. Tips & Jebakan
> > [!tip] Hubungan Dua Arah Ekivalensi-Partisi
> > Ingat teorema fundamental ini: Setiap relasi ekivalen pada himpunan $S$ menghasilkan sebuah partisi pada $S$, dan sebaliknya, setiap partisi pada $S$ mendefinisikan sebuah relasi ekivalen pada $S$. Jadi, kalau kamu disuruh bikin partisi, cari aja relasi ekivalennya, kelas ekivalennya otomatis jadi blok-blok partisinya!
