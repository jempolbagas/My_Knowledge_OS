---
title: "[DM1] Assignment - Tugas Tengah Semester"
course: Discrete Mathematics I
tags: ["discrete-mathematics", "math", "assignment"]
aliases: ["[DM1] Assignment - Tugas Tengah Semester"]
created: "2026-04-30"
type: Assignment
---

# Penyelesaian Soal Tugas Tengah Semester
**Mata Kuliah:** Matematika Diskrit I
**Tahun Ajaran:** 2025/2026

---

### Soal 1
**Pertanyaan:** Perhatikan program berikut yang digunakan untuk sorting menjadi increasing order. Pada baris ke-8 merupakan proses perbandingan, hitunglah berapa kali proses perbandingan terjadi pada baris ke-8 tersebut?
**Jawaban:** 
Pada algoritma sorting tersebut, proses perbandingan `arr[j] > arr[j + 1]` terjadi di dalam nested loop. 
Untuk array berukuran $n$:
- Iterasi $i = 0$, $j$ berjalan dari $0$ sampai $n - 2$ (terjadi $n - 1$ perbandingan).
- Iterasi $i = 1$, $j$ berjalan dari $0$ sampai $n - 3$ (terjadi $n - 2$ perbandingan).
- Dan seterusnya.
Secara _worst-case_ (jika elemen di-swap setiap saat dan loop tidak pernah `break` lebih awal), jumlah perbandingan maksimal adalah deret aritmatika:
$(n - 1) + (n - 2) + \dots + 1 = \frac{n(n - 1)}{2}$ kali perbandingan.
Namun, karena ada optimasi di mana loop berhenti jika tidak ada proses _swap_, jika array sejak awal sudah terurut (best-case), maka iterasi hanya terjadi sekali sebanyak $n-1$ perbandingan.
Jadi, rentang banyaknya perbandingan adalah dari $n-1$ kali hingga $\frac{n(n - 1)}{2}$ kali bergantung pada urutan array awal.

---

### Soal 2
**Pertanyaan:** Diketahui $A = \{0,1,2\}$, $B = \{0,1\}$, dan $C = \{1,2\}$. Maka tentukan Cartesian product $A \times B \times C$!
**Jawaban:**
Cartesian product $A \times B \times C = \{(a,b,c) \mid a \in A, b \in B, c \in C\}$.
Kombinasi elemen-elemennya adalah:
- (0, 0, 1), (0, 0, 2)
- (0, 1, 1), (0, 1, 2)
- (1, 0, 1), (1, 0, 2)
- (1, 1, 1), (1, 1, 2)
- (2, 0, 1), (2, 0, 2)
- (2, 1, 1), (2, 1, 2)

Total terdapat $3 \times 2 \times 2 = 12$ elemen.

---

### Soal 3
**Pertanyaan:** Misalkan $A$, $B$, dan $C$ merupakan himpunan, buktikan bahwa $\overline{A \cup (B \cap C)} = \overline{A} \cap (\overline{B} \cup \overline{C})$!
**Jawaban:**
Kita dapat menggunakan Hukum De Morgan secara bertahap.
Hukum De Morgan berbunyi: $\overline{X \cup Y} = \overline{X} \cap \overline{Y}$ dan $\overline{X \cap Y} = \overline{X} \cup \overline{Y}$.
Pertama, aplikasikan Hukum De Morgan pada operasi gabungan yang paling luar:
$\overline{A \cup (B \cap C)} = \overline{A} \cap \overline{(B \cap C)}$
Selanjutnya, aplikasikan Hukum De Morgan pada komplemen irisan $B$ dan $C$:
$\overline{(B \cap C)} = \overline{B} \cup \overline{C}$
Substitusikan bentuk ini kembali ke persamaan sebelumnya:
$\overline{A \cup (B \cap C)} = \overline{A} \cap (\overline{B} \cup \overline{C})$
(Terbukti)

---

### Soal 4
**Pertanyaan:** Gambarkan diagram Venn dari kombinasi himpunan $A$, $B$, dan $C$ berikut:
a. $A \cap (B - C)$
b. $\overline{A} \cap \overline{B} \cap \overline{C}$
**Jawaban:**
a. $A \cap (B - C)$ merepresentasikan area yang berada di dalam himpunan A sekaligus di dalam himpunan B, namun *tidak termasuk* dalam himpunan C. Pada diagram Venn 3 himpunan, ini adalah irisan antara A dan B yang dipotong/dihilangkan area lingkar C-nya.
b. $\overline{A} \cap \overline{B} \cap \overline{C}$ ekuivalen dengan $\overline{A \cup B \cup C}$. Area ini merepresentasikan ruang semesta di luar ketiga lingkaran $A$, $B$, dan $C$. (Daerah di luar seluruh himpunan yang ada).

*(Catatan: Gambaran visual disesuaikan dengan deskripsi di atas).*

---

### Soal 5
**Pertanyaan:** Tentukan apakah fungsi $f(x) = x^2$ dari himpunan integers menuju ke himpunan integers merupakan *one-to-one*?
**Jawaban:**
Sebuah fungsi dikatakan *one-to-one* (injektif) jika untuk setiap $x_1 \neq x_2$, berlaku $f(x_1) \neq f(x_2)$.
Misalkan kita mengambil dua bilangan bulat yang berbeda, yaitu $x_1 = 2$ dan $x_2 = -2$.
Kita hitung nilai fungsinya:
- $f(2) = 2^2 = 4$
- $f(-2) = (-2)^2 = 4$
Karena $f(2) = f(-2)$ meskipun $2 \neq -2$, maka terdapat lebih dari satu input yang dipetakan ke output yang sama. Oleh karena itu, fungsi $f(x) = x^2$ untuk himpunan bilangan bulat **bukan** merupakan fungsi *one-to-one*.

---

### Soal 6
**Pertanyaan:** Tentukan $f \circ g$ dan $g \circ f$ untuk $f(x)$ dan $g(x)$ berikut:
a. $f(x) = x^2 + 1$ dan $g(x) = x^3 + 4x^2 - 2x + 1$
b. $f(x) = 4x^2 + 3x + 2$ dan $g(x) = 2x^2 - 2x + 9$

**Jawaban:**
**a.** 
- $f \circ g = f(g(x)) = (x^3 + 4x^2 - 2x + 1)^2 + 1$
- $g \circ f = g(f(x)) = (x^2 + 1)^3 + 4(x^2 + 1)^2 - 2(x^2 + 1) + 1$

**b.**
- $f \circ g = f(g(x)) = 4(2x^2 - 2x + 9)^2 + 3(2x^2 - 2x + 9) + 2$
- $g \circ f = g(f(x)) = 2(4x^2 + 3x + 2)^2 - 2(4x^2 + 3x + 2) + 9$

---

### Soal 7
**Pertanyaan:** Tunjukkan bahwa $f(x) = 5x^2 + 10x + 3$ merupakan $O(x^2)$!
**Jawaban:**
Untuk membuktikan bahwa $f(x) = O(x^2)$, kita harus mencari konstanta riil $C$ dan $k$ sehingga $|5x^2 + 10x + 3| \le C|x^2|$ untuk semua $x > k$.
Untuk mempermudah, asumsikan $x > 1$. Maka berlaku $x < x^2$ dan $1 < x^2$.
Sehingga, kita bisa membatasi fungsinya:
$|5x^2 + 10x + 3| \le 5x^2 + 10x^2 + 3x^2$
$5x^2 + 10x + 3 \le 18x^2$
Dengan memilih $C = 18$ dan $k = 1$, kita telah membuktikan bahwa $|5x^2 + 10x + 3| \le 18|x^2|$ untuk setiap $x > 1$.
Maka, $f(x) = 5x^2 + 10x + 3$ merupakan $O(x^2)$ terbukti benar.

---

### Soal 8
**Pertanyaan:** Periksa apakah $x^3 + 2x^2 + 3$ merupakan $O(x^2)$!
**Jawaban:**
Jika fungsi tersebut adalah $O(x^2)$, maka harus terdapat konstanta $C$ dan $k$ sehingga:
$x^3 + 2x^2 + 3 \le Cx^2$ untuk setiap $x > k$.
Jika kita bagi kedua ruas dengan $x^2$ (untuk $x > 0$), kita dapatkan:
$x + 2 + \frac{3}{x^2} \le C$
Saat nilai $x$ tumbuh membesar menuju tak hingga ($x \to \infty$), nilai ruas kiri juga akan ikut membesar menuju tak hingga, sehingga tidak akan ada konstanta riil tunggal $C$ mana pun yang dapat membatasi pertumbuhan ruas kiri tersebut.
Karena syarat batasan konstan asimtotik dilanggar, maka $x^3 + 2x^2 + 3$ **bukan** merupakan $O(x^2)$.

---

### Soal 9
**Pertanyaan:** Berapakah kompleksitas terburuk dari *bubble sort* dalam hal banyaknya perbandingan yang terjadi dalam algoritma?
**Jawaban:**
Pada *bubble sort*, *worst-case* (kasus terburuk) terjadi ketika array berurutan secara terbalik. Pada iterasi pertama butuh $n-1$ perbandingan, iterasi kedua $n-2$ perbandingan, dan seterusnya hingga $1$ perbandingan.
Jumlah perbandingan totalnya adalah deret:
$(n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2} = \frac{1}{2}n^2 - \frac{1}{2}n$
Dengan mengabaikan koefisien dan konstanta dominan terkecil, kompleksitas terburuk dari proses perbandingan *bubble sort* adalah **$O(n^2)$**.

---

### Soal 10
**Pertanyaan:** Dengan menggunakan *mathematical induction* tunjukkan bahwa 
$1 + 2 + 2^2 + \dots + 2^n = 2^{n+1} - 1$ untuk semua bilangan *integers nonnegative* $n$!
**Jawaban:**
**Langkah Basis (Basis Step):**
Untuk $n = 0$:
- Ruas Kiri: $2^0 = 1$
- Ruas Kanan: $2^{0+1} - 1 = 2^1 - 1 = 1$
Keduanya sama, basis step terbukti benar.

**Langkah Induksi (Inductive Step):**
Asumsikan bahwa pernyataan benar untuk $n = k$, yaitu:
$1 + 2 + 2^2 + \dots + 2^k = 2^{k+1} - 1$
Akan dibuktikan bahwa pernyataan benar untuk $n = k+1$, yaitu:
$1 + 2 + 2^2 + \dots + 2^k + 2^{k+1} = 2^{(k+1)+1} - 1 = 2^{k+2} - 1$

Mari kita kerjakan dari ruas kiri untuk $n = k+1$:
$= (1 + 2 + 2^2 + \dots + 2^k) + 2^{k+1}$
Substitusikan dengan asumsi induktif:
$= (2^{k+1} - 1) + 2^{k+1}$
$= 2 \times 2^{k+1} - 1$
$= 2^{k+2} - 1$

Karena kita mendapatkan hasil yang setara dengan ruas kanan untuk $n = k+1$, maka berdasarkan induksi matematika, proposisi tersebut benar untuk semua $n \ge 0$.

---

### Soal 11
**Pertanyaan:** Buktikan bahwa $2^n > n^2$ jika $n$ merupakan bilangan *integer* yang lebih besar dari 4!
**Jawaban:**
Kita buktikan menggunakan induksi matematika.

**Langkah Basis:** Untuk $n = 5$ (karena $n > 4$):
- $2^5 = 32$
- $5^2 = 25$
Karena $32 > 25$, basis step bernilai benar.

**Langkah Induksi:** Asumsikan pernyataan benar untuk $n = k$ (dengan $k \ge 5$), yaitu $2^k > k^2$.
Kita harus membuktikan kebenarannya untuk $n = k+1$, yaitu $2^{k+1} > (k+1)^2$.
Berangkat dari ekspresi $2^{k+1}$:
$2^{k+1} = 2 \cdot 2^k$
Berdasarkan asumsi $2^k > k^2$, kita peroleh:
$2^{k+1} > 2k^2$

Sekarang kita perlu membandingkan apakah $2k^2 \ge (k+1)^2$ untuk $k \ge 5$.
$2k^2 - (k+1)^2 = 2k^2 - (k^2 + 2k + 1) = k^2 - 2k - 1$
Dapat kita faktorkan menjadi $k(k-2) - 1$.
Untuk nilai terkecil $k=5$, ekspresi ini bernilai $5(3) - 1 = 14 > 0$. Oleh karena itu $2k^2 > (k+1)^2$ adalah benar.
Maka kita memiliki alur ketidaksamaan:
$2^{k+1} > 2k^2 > (k+1)^2$
Jadi terbukti bahwa $2^{k+1} > (k+1)^2$, menuntaskan pembuktian induktifnya.

---

### Soal 12
**Pertanyaan:** Gunakan *strong induction* untuk menunjukkan bahwa jika anda dapat berlari sejauh satu mil atau dua mil, dan jika anda selalu dapat berlari sejauh dua mil lagi setelah anda mencapai jumlah mil tertentu, maka anda dapat berlari sejauh berapa pun mil!
**Jawaban:**
Misalkan $P(n)$ adalah proposisi "anda dapat berlari sejauh $n$ mil". Kita akan membuktikan ini untuk setiap integer $n \ge 1$.

**Langkah Basis:**
Berdasarkan premis soal, Anda dapat berlari 1 mil dan 2 mil. Maka, $P(1)$ bernilai benar, dan $P(2)$ juga bernilai benar.

**Langkah Induksi (*Strong Induction*):**
Asumsikan bahwa $P(i)$ benar untuk setiap angka mulai dari $i = 1$ hingga $i = k$ (dengan $k \ge 2$).
Kita wajib membuktikan bahwa hal ini juga menjamin kebenaran untuk $P(k+1)$.
Dari premis, Anda selalu dapat berlari 2 mil lagi setelah mencapai jumlah mil tertentu. Karena $k \ge 2$, maka $(k+1) \ge 3$, sehingga kita dapat mengevaluasi posisi dua mil sebelumnya: $(k+1) - 2 = k - 1$.
Karena $k-1 \ge 1$, berdasarkan asumsi induksi kuat, $P(k-1)$ terjamin kebenarannya (anda pasti dapat berlari sejauh $k-1$ mil). 
Oleh karena Anda selalu bisa berlari tambahan jarak dua mil lagi sesudah jarak ini, maka $(k-1) + 2 = k+1$. 
Jadi, Anda dipastikan dapat berlari sejauh $k+1$ mil ($P(k+1)$ terbukti). Berdasarkan *strong induction*, hal ini membuktikan Anda dapat mencapai jarak integer berapapun.

---

### Soal 13
**Pertanyaan:** Sebutkan $f(1)$, $f(2)$, $f(3)$, dan $f(4)$ jika $f(n)$ didefinisikan secara rekursif oleh $f(0) = 1$ dan untuk $n = 0,1,2, \dots$
a. $f(n + 1) = 3f(n)$
b. $f(n + 1) = 3f(n) + 7$
c. $f(n + 1) = f(n)^2 - 2f(n) + 1$

**Jawaban:**
**a. $f(n + 1) = 3f(n)$**
- $f(0) = 1$
- $f(1) = 3(1) = 3$
- $f(2) = 3(3) = 9$
- $f(3) = 3(9) = 27$
- $f(4) = 3(27) = 81$

**b. $f(n + 1) = 3f(n) + 7$**
- $f(0) = 1$
- $f(1) = 3(1) + 7 = 10$
- $f(2) = 3(10) + 7 = 37$
- $f(3) = 3(37) + 7 = 118$
- $f(4) = 3(118) + 7 = 361$

**c. $f(n + 1) = f(n)^2 - 2f(n) + 1$** (dapat diubah menjadi $(f(n) - 1)^2$)
- $f(0) = 1$
- $f(1) = (1 - 1)^2 = 0$
- $f(2) = (0 - 1)^2 = 1$
- $f(3) = (1 - 1)^2 = 0$
- $f(4) = (0 - 1)^2 = 1$

---

### Soal 14
**Pertanyaan:** Terdapat suatu fungsi rekursif yang disebut dengan fungsi McCarthy. Fungsi tersebut didefinisikan secara rekursif sebagai berikut :
$M(n) = \begin{cases} n - 10, & n > 100 \\ M(M(n + 11)), & n \le 100 \end{cases}$
Tentukan implementasi dalam *pseudocode* untuk algoritma rekursif tersebut!
**Jawaban:**
Implementasi dalam struktur *pseudocode*:

```pascal
procedure McCarthy(n: integer)
    if n > 100 then
        return n - 10
    else
        return McCarthy(McCarthy(n + 11))
```

---

### Soal 15
**Pertanyaan:** Suatu perusahaan baru dengan dua karyawan, Sanchez dan Patel, menyewa satu lantai gedung dengan 12 kantor. Berapa banyak cara untuk menetapkan kantor yang berbeda untuk kedua karyawan ini?
**Jawaban:**
Terdapat urutan/perbedaan peruntukan kantor (*order matters*), karena kantor yang ditempati Sanchez dan Patel bisa dibedakan status penempatannya.
- Pilihan untuk Sanchez = 12 kantor.
- Pilihan untuk Patel (dengan satu sudah dipakai) = 11 kantor.
Maka banyaknya cara adalah permutasi $P(12, 2) = 12 \times 11 = 132$ cara.

---

### Soal 16
**Pertanyaan:** Terdapat empat rute utama dari Boston menuju Detroit dan enam rute dari Detroit menuju Los Angeles. Berapa banyak rute utama mobil dari Boston menuju Los Angeles melalui Detroit?
**Jawaban:**
Menggunakan Aturan Perkalian (*The Product Rule*) karena pergerakan dilakukan secara sekuensial:
Banyak rute = (Rute Boston-Detroit) $\times$ (Rute Detroit-LA)
Banyak rute = $4 \times 6 = 24$ rute kemungkinan kombinasi jalur.

---

### Soal 17
**Pertanyaan:** Berapa banyak *license plates* yang dapat dibuat menggunakan dua huruf besar diikuti empat angka atau dua angka diikuti empat huruf besar?
**Jawaban:**
(Total Huruf Besar $A-Z$ = 26; Total Angka $0-9$ = 10). Karena soal tidak membatasi perulangan, maka pengulangan diizinkan (*with replacement*).

- **Skenario 1 (2 Huruf, 4 Angka):** $26^2 \times 10^4 = 676 \times 10.000 = 6.760.000$ variasi.
- **Skenario 2 (2 Angka, 4 Huruf):** $10^2 \times 26^4 = 100 \times 456.976 = 45.697.600$ variasi.

Karena formasi dihubungkan dengan kata **"ATAU"**, kedua skenario bersifat terpisah dan digabungkan melalui Aturan Penjumlahan (*The Sum Rule*).
Total plat nomor: $6.760.000 + 45.697.600 = 52.457.600$ variasi.

---

### Soal 18
**Pertanyaan:** Berapa banyak angka yang harus dipilih dari himpunan $\{1,2,3,4,5,6\}$ untuk menjamin bahwa setidaknya satu pasang angka berjumlah 7?
**Jawaban:**
Mari kita identifikasi pasangan angka dari himpunan tersebut yang bila dijumlahkan bernilai 7:
(1, 6), (2, 5), (3, 4).
Terdapat 3 pasangan eksklusif (*Pigeonholes* atau sarang burung).
Berdasarkan *The Pigeonhole Principle*, jika kita memilih 4 angka secara bebas (Merpati), maka pasti akan ada minimal dua angka yang ditarik dari pasangan yang sama (karena hanya ada 3 pasangan). Dua angka dari satu kelompok sarang yang sama tersebut sudah pasti berjumlah 7.
Jadi, Anda harus memilih minimal **4 angka** untuk mendapat jaminan absolut ini.

---

### Soal 19
**Pertanyaan:** Berapa banyak cara untuk memilih lima pemain dari tim tenis yang beranggotakan 10 orang untuk melakukan perjalanan ke pertandingan di sekolah lain?
**Jawaban:**
Karena kita hanya peduli pada siapa saja yang tergabung di dalam tim terpilih, bukan susunan letak mereka (*order does not matter*), maka digunakan Kombinasi:
$C(10, 5) = \frac{10!}{5!(10-5)!} = \frac{10 \times 9 \times 8 \times 7 \times 6}{5 \times 4 \times 3 \times 2 \times 1} = \frac{30.240}{120} = 252$
Jadi, terdapat 252 kelompok cara kombinasi tim tenis.

---

### Soal 20
**Pertanyaan:** Pada sebuah babak final sebuah turnamen, tim pemenang adalah tim yang pertama sekali memenangkan 2 pertandingan secara berurutan atau tim yang pertama sekali memenangkan 4 pertandingan. Tentukan banyak cara turnamen yang dapat terjadi!
**Jawaban:**
Misalkan kedua tim adalah Tim A dan Tim B.
Ada dua syarat turnamen diakhiri: mendapatkan skor kemenangan berurutan (`AA` atau `BB`) atau mencapai total kemenangan empat kali di suatu masa pertarungan. Untuk menghindari penghentian awal (kemenangan 2x berturut-turut), urutan harus secara mutlak berselang-seling (contoh: ABAB...).
Kita dapat menguraikan susunan (*string*) hasil menang berdasarkan panjang permainan:

- Berhenti di Pertandingan ke-2: `AA`, `BB`
- Berhenti di Pertandingan ke-4: `ABAA`, `BABB`
- Berhenti di Pertandingan ke-6: `ABABAA`, `BABABB`
- Berhenti di Pertandingan ke-7: `ABABABA` (A mencapai skor 4 total), `BABABAB` (B mencapai skor 4 total).

Tercatat tidak ada cabang probabilitas lain karena selain model sekuens di atas, permainan dipastikan telah berhenti lebih dini.
Sehingga, total terdapat **8 cara turnamen** bisa berlangsung.
