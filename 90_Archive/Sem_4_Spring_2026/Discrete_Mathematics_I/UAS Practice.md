---
title: Latihan Soal Terbimbing Persiapan UAS Matematika Diskrit 1
course: Matematika Diskrit 1
tags: ["discrete-mathematics", "practice", "exam-prep"]
aliases: ["Latihan UAS Diskrit 1", "Solusi Latihan UAS"]
created: "2026-06-22"
---

# Latihan Soal Terbimbing Persiapan UAS Matematika Diskrit 1

Yo! File ini dibuat khusus buat ngebongkar semua soal latihan UAS yang dikasih sama dosen kamu. Kita bakal bahas satu per satu pakai format **3-bagian** yang mantap: intuisi santai buat ngebangun logika, solusi formal matematika pakai LaTeX biar dosen terpukau, dan tips/jebakan biar kamu nggak blunder pas ujian besok. 

Yuk, ceki-ceki pembahasannya!

---

## Soal 1: Fungsi Pembangkit (Generating Functions)

**Tentukan *generating functions* dari barisan berikut:**
*   a. $(2, 2, 2, 2, 2, \dots)$
*   b. $(0, 0, \frac{1}{2!}, \frac{1}{3!}, \frac{1}{4!}, \dots)$
*   c. $a_n = n + 2$
*   d. $(2, -1, 5, -7, 17, \dots)$

### Pembahasan Soal 1.a: $(2, 2, 2, 2, 2, \dots)$

#### 1. Intuisi & Analisis Kasus
Ini barisan konstan yang isinya angka 2 terus-menerus. Kita tahu kalau barisan $(1, 1, 1, \dots)$ fungsi pembangkitnya itu $\frac{1}{1-x}$. Karena semuanya dikali 2, ya tinggal kita kalikan 2 aja fungsi pembangkit dasarnya. Simpel banget, kan?

#### 2. Solusi Matematis Formal
Berdasarkan definisi deret kuasa formal untuk OGF $G(x)$ dengan suku $a_n = 2$:
$$G(x) = \sum_{n=0}^{\infty} 2 x^n = 2 \sum_{n=0}^{\infty} x^n$$
Karena deret geometri tak hingga $\sum_{n=0}^{\infty} x^n$ konvergen ke $\frac{1}{1-x}$ untuk $|x| < 1$, diperoleh bentuk tertutup:
$$G(x) = \frac{2}{1-x}, \quad \text{dengan daerah kekonvergenan } |x| < 1$$

#### 3. Tips & Jebakan
> [!tip]
> Selalu cek indeks mulainya barisan. Di sini karena deretnya mulai dari indeks $n=0$ tanpa pergeseran, kita bisa langsung pakai formula dasar $\frac{1}{1-x}$.

---

### Pembahasan Soal 1.b: $(0, 0, \frac{1}{2!}, \frac{1}{3!}, \frac{1}{4!}, \dots)$

#### 1. Intuisi & Analisis Kasus
Kalau kita lihat ada penyebut faktorial ($2!, 3!, 4!$), otak kita kudu langsung konek ke fungsi eksponensial $e^x$. 
Ingat deret Maclaurin untuk $e^x$:
$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$$
Barisan kita adalah $(0, 0, \frac{1}{2!}, \frac{1}{3!}, \dots)$, artinya suku ke-0 ($a_0$) dan suku ke-1 ($a_1$) bernilai 0. Maka kita tinggal kurangi aja $e^x$ dengan dua suku pertamanya, yaitu $1$ dan $x$.

#### 2. Solusi Matematis Formal
Definisi OGF $G(x)$ untuk barisan $(0, 0, \frac{1}{2!}, \frac{1}{3!}, \dots)$:
$$G(x) = \sum_{n=2}^{\infty} \frac{x^n}{n!}$$
Mengingat ekspansi deret Maclaurin untuk $e^x$:
$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \sum_{n=2}^{\infty} \frac{x^n}{n!} \implies \sum_{n=2}^{\infty} \frac{x^n}{n!} = e^x - 1 - x$$
Diperoleh bentuk tertutup OGF:
$$G(x) = e^x - 1 - x, \quad \text{untuk } x \in \mathbb{R}$$

#### 3. Tips & Jebakan
> [!warning]
> Hati-hati! Beberapa mahasiswa sering keliru mengira barisan dengan faktorial otomatis harus diselesaikan pakai *Exponential Generating Function* (EGF). Kecuali soal secara eksplisit meminta EGF, selalu asumsikan soal meminta *Ordinary Generating Function* (OGF) biasa, di mana kita mengalikan barisan dengan $x^n$, bukan $\frac{x^n}{n!}$.

---

### Pembahasan Soal 1.c: $a_n = n + 2$

#### 1. Intuisi & Analisis Kasus
Barisannya kalau kita jabarkan adalah $(2, 3, 4, 5, \dots)$. Suku umumnya $a_n = n + 2$. Kita bisa pecah deretnya jadi penjumlahan dua bagian: bagian pertama untuk $n$ (yang fungsi pembangkit dasarnya adalah $\frac{x}{(1-x)^2}$) dan bagian kedua untuk konstan 2 (yang fungsi pembangkit dasarnya $\frac{2}{1-x}$). Setelah itu tinggal disamakan penyebutnya.

#### 2. Solusi Matematis Formal
Fungsi pembangkit biasa $G(x)$ untuk $a_n = n+2$ didefinisikan sebagai:
$$G(x) = \sum_{n=0}^{\infty} (n + 2) x^n = \sum_{n=0}^{\infty} n x^n + 2 \sum_{n=0}^{\infty} x^n$$

Kita turunkan bentuk $\sum_{n=0}^{\infty} n x^n$ dari deret geometri dasar untuk $|x| < 1$:
$$
\begin{aligned}
\sum_{n=0}^{\infty} x^n = \frac{1}{1-x} &\implies \frac{d}{dx} \left( \sum_{n=0}^{\infty} x^n \right) = \frac{d}{dx} (1-x)^{-1} \\
&\implies \sum_{n=1}^{\infty} n x^{n-1} = \frac{1}{(1-x)^2} \\
&\implies \sum_{n=0}^{\infty} n x^n = \frac{x}{(1-x)^2} \quad (\text{kedua ruas dikali } x)
\end{aligned}
$$

Substitusikan hasil di atas dan deret geometri $2 \sum x^n = \frac{2}{1-x}$ ke persamaan awal:
$$G(x) = \frac{x}{(1-x)^2} + \frac{2}{1-x} = \frac{x + 2(1-x)}{(1-x)^2} = \frac{2-x}{(1-x)^2}, \quad \text{untuk } |x| < 1$$

#### 3. Tips & Jebakan
> [!tip]
> Cara alternatif: Kamu juga bisa menulis $(n+2)x^n$ sebagai turunan. 
> Deretnya adalah $2 + 3x + 4x^2 + 5x^3 + \dots = \frac{d}{dx}\left( 2x + \frac{3}{2}x^2 + \dots \right)$. Tapi memecah deret seperti solusi formal di atas jauh lebih cepat dan minim resiko salah hitung!

---

### Pembahasan Soal 1.d: $(2, -1, 5, -7, 17, \dots)$

#### 1. Intuisi & Analisis Kasus
Mari kita ceki-ceki polanya. Suku-sukunya berselang-seling tanda dan nilainya tumbuh mendekati perpangkatan 2.
- $a_0 = 2 = 1 + 1 = (-2)^0 + 1$
- $a_1 = -1 = -2 + 1 = (-2)^1 + 1$
- $a_2 = 5 = 4 + 1 = (-2)^2 + 1$
- $a_3 = -7 = -8 + 1 = (-2)^3 + 1$
- $a_4 = 17 = 16 + 1 = (-2)^4 + 1$
Ketemu! Rumus suku umumnya adalah $a_n = (-2)^n + 1$. 
Untuk mencari fungsi pembangkitnya, kita tinggal pecah jadi deret geometri $(-2)^n$ dan deret geometri konstan $1^n$.

#### 2. Solusi Matematis Formal
Dengan suku umum $a_n = (-2)^n + 1$, OGF $G(x)$ didefinisikan sebagai:
$$G(x) = \sum_{n=0}^{\infty} \left( (-2)^n + 1 \right) x^n = \sum_{n=0}^{\infty} (-2x)^n + \sum_{n=0}^{\infty} x^n$$
Mengingat kedua deret geometri tak hingga tersebut konvergen pada daerah bersama $|x| < \frac{1}{2}$:
$$
\begin{aligned}
G(x) &= \frac{1}{1+2x} + \frac{1}{1-x} \\
&= \frac{(1-x) + (1+2x)}{(1+2x)(1-x)} \\
&= \frac{2+x}{1+x-2x^2}, \quad \text{untuk } |x| < \frac{1}{2}
\end{aligned}
$$

#### 3. Tips & Jebakan
> [!warning]
> Menemukan pola barisan seperti ini butuh ketelitian tinggi. Kalau tandanya selang-seling, curigai ada faktor $(-r)^n$. Di soal aslinya, ada minus di angka 7 (yaitu $-7$), jangan sampai abai dengan tanda minus tersebut!

---

## Soal 2: Relasi Rekurensi Homogen

**Tentukan solusi eksplisit dari *recurrence relation* berikut dengan menggunakan polinomial karakteristik:**
*   a. $a_n = 6a_{n-1} - 9a_{n-2}$ dengan $a_0 = 1$ dan $a_1 = 6$
*   b. $a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3}$ dengan $a_0 = 2$, $a_1 = 5$, dan $a_2 = 15$
*   c. $a_n = -3a_{n-1} - 3a_{n-2} - a_{n-3}$ dengan $a_0 = 1$, $a_1 = -2$, dan $a_2 = -1$

### Pembahasan Soal 2.a: $a_n = 6a_{n-1} - 9a_{n-2}$

#### 1. Intuisi & Analisis Kasus
Ini adalah relasi rekurensi homogen linear derajat 2. Kita tinggal buat polinomial karakteristiknya $r^2 - 6r + 9 = 0$. Wah, ini kan bentuk kuadrat sempurna $(r-3)^2 = 0$. Jadi, kita punya akar kembar $r = 3$. 
Ingat cheatsheet! Kalau akar kembar, solusinya berbentuk $a_n = (C_1 + C_2 n) 3^n$. Tinggal kita cari konstanta $C_1$ dan $C_2$ pakai nilai awal.

#### 2. Solusi Matematis Formal
Bentuk standar: $a_n - 6a_{n-1} + 9a_{n-2} = 0$. Substitusikan $a_n = r^n$:
$$r^2 - 6r + 9 = 0 \implies (r-3)^2 = 0$$
Diperoleh akar kembar $r = 3$ ($m=2$). Solusi umumnya:
$$a_n = (C_1 + C_2 n) 3^n$$
Gunakan nilai awal $a_0 = 1$ dan $a_1 = 6$ untuk mencari konstanta:
- $n=0 \implies a_0 = C_1 = 1$
- $n=1 \implies a_1 = 3(C_1 + C_2) = 6 \implies C_1 + C_2 = 2 \implies C_2 = 1$

$\therefore$ Solusi eksplisit relasi rekurensi tersebut adalah:
$$a_n = (1 + n) 3^n, \quad \text{untuk } n \ge 0$$

#### 3. Tips & Jebakan
> [!warning]
> Jangan lupa mengalikan suku kedua dengan $n$ ketika ada akar kembar! Kalau kamu cuma tulis $a_n = C_1 3^n + C_2 3^n$, solusinya bakal salah total karena itu setara dengan satu konstanta tunggal saja.

---

### Pembahasan Soal 2.b: $a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3}$

#### 1. Intuisi & Analisis Kasus
Derajatnya naik jadi 3, jadi kita bakal punya persamaan kubik: $r^3 - 6r^2 + 11r - 6 = 0$. 
Untuk mencari akar-akarnya, coba-coba tebak nilai pembagi dari konstanta ujungnya (yaitu $-6$). Pembaginya bisa $\pm 1, \pm 2, \pm 3$.
Jika kita masukkan $r=1$: $1 - 6 + 11 - 6 = 0$. Wah, hoki langsung dapet! Berarti $r-1$ adalah salah satu faktornya. Setelah difaktorkan, ternyata akar-akarnya adalah 1, 2, dan 3. Solusi umumnya: $a_n = C_1 1^n + C_2 2^n + C_3 3^n$.

#### 2. Solusi Matematis Formal
Bentuk standar: $a_n - 6a_{n-1} + 11a_{n-2} - 6a_{n-3} = 0 \implies r^3 - 6r^2 + 11r - 6 = 0$.
Berdasarkan Teorema Akar Rasional, uji pembagi dari $-6$. Untuk $r=1$:
$$1^3 - 6(1)^2 + 11(1) - 6 = 0 \implies (r-1) \text{ adalah faktor.}$$
Menggunakan metode Horner:
```
  r = 1 |  1   -6   11   -6
        |       1   -5    6
        -------------------
           1   -5    6    0  (Sisa = 0)
```
Hasil bagi $r^2 - 5r + 6 = (r-2)(r-3) = 0$. Diperoleh akar real berbeda: $r_1=1, r_2=2, r_3=3$.
Solusi umum: $a_n = C_1 + C_2 2^n + C_3 3^n$.
Gunakan nilai awal ($a_0=2, a_1=5, a_2=15$) untuk menyusun sistem persamaan:
$$
\begin{aligned}
C_1 + C_2 + C_3 &= 2 \quad \text{--- (A)} \\
C_1 + 2C_2 + 3C_3 &= 5 \quad \text{--- (B)} \\
C_1 + 4C_2 + 9C_3 &= 15 \quad \text{--- (C)}
\end{aligned}
$$
Eliminasi variabel:
*   $\text{(B)} - \text{(A)} \implies C_2 + 2C_3 = 3 \quad \text{--- (D)}$
*   $\text{(C)} - \text{(B)} \implies 2C_2 + 6C_3 = 10 \implies C_2 + 3C_3 = 5 \quad \text{--- (E)}$
*   $\text{(E)} - \text{(D)} \implies C_3 = 2$
*   Substitusi ke $\text{(D)} \implies C_2 + 4 = 3 \implies C_2 = -1$
*   Substitusi ke $\text{(A)} \implies C_1 - 1 + 2 = 2 \implies C_1 = 1$

$\therefore$ Solusi eksplisit relasi rekurensi tersebut adalah:
$$a_n = 1 - 2^n + 2 \cdot 3^n, \quad \text{untuk } n \ge 0$$

#### 3. Tips & Jebakan
> [!tip]
> Pembagian polinomial (metode Horner) sangat berguna untuk mereduksi derajat persamaan karakteristik dari kubik ke kuadrat. Kuasai metode Horner agar tidak habis waktu menebak-nebak akar persamaan derajat 3!

---

### Pembahasan Soal 2.c: $a_n = -3a_{n-1} - 3a_{n-2} - a_{n-3}$

#### 1. Intuisi & Analisis Kasus
Persamaan karakteristiknya adalah $r^3 + 3r^2 + 3r + 1 = 0$. Kamu kudu jeli melihat ini sebagai ekspansi binomial $(r+1)^3 = 0$. Berarti kita punya satu akar kembar tiga (tripel) yaitu $r = -1$.
Berdasarkan aturan akar kembar, solusinya berbentuk $a_n = (C_1 + C_2 n + C_3 n^2) (-1)^n$. Tinggal kita cari konstanta $C_1, C_2, C_3$ pakai nilai-nilai awal yang ada.

#### 2. Solusi Matematis Formal
Bentuk standar: $a_n + 3a_{n-1} + 3a_{n-2} + a_{n-3} = 0 \implies r^3 + 3r^2 + 3r + 1 = 0$.
Berdasarkan ekspansi binomial $(r+1)^3 = 0$, diperoleh akar kembar $r = -1$ ($m=3$).
Solusi umum:
$$a_n = \left(C_1 + C_2 n + C_3 n^2\right) (-1)^n$$
Gunakan nilai awal $a_0 = 1, a_1 = -2, a_2 = -1$ untuk menyusun sistem persamaan:
- $n=0 \implies C_1 = 1$
- $n=1 \implies -(C_1 + C_2 + C_3) = -2 \implies 1 + C_2 + C_3 = 2 \implies C_2 + C_3 = 1 \quad \text{--- (A)}$
- $n=2 \implies C_1 + 2C_2 + 4C_3 = -1 \implies 1 + 2C_2 + 4C_3 = -1 \implies C_2 + 2C_3 = -1 \quad \text{--- (B)}$

Eliminasi:
*   $\text{(B)} - \text{(A)} \implies C_3 = -2$
*   Substitusi ke $\text{(A)} \implies C_2 - 2 = 1 \implies C_2 = 3$

$\therefore$ Solusi eksplisit akhirnya adalah:
$$a_n = \left(1 + 3n - 2n^2\right) (-1)^n, \quad \text{untuk } n \ge 0$$

#### 3. Tips & Jebakan
> [!warning]
> Hati-hati dengan tanda negatif pada basis $(-1)^n$. Ketika $n$ ganjil, hasilnya negatif; ketika $n$ genap, hasilnya positif. Lupa mendistribusikan tanda negatif dari $(-1)^n$ saat mencari konstanta adalah kesalahan yang paling sering terjadi!

---

## Soal 3: Relasi Rekurensi Non-Homogen

**Tentukan solusi eksplisit dari *recurrence relation* berikut:**
*   a. $a_n = 8a_{n-1} + 10^{n-1}$ dengan $a_0 = 1$ dan $a_1 = 9$
*   b. $a_n = 3a_{n-1} - 2a_{n-2} + C_1^n$ dengan $a_0 = 0$ dan $a_1 = 1$
*   c. $a_n = 4a_{n-1} - 4a_{n-2} + 2^n$ dengan $a_0 = 0$ dan $a_1 = 1$

### Pembahasan Soal 3.a: $a_n = 8a_{n-1} + 10^{n-1}$

#### 1. Intuisi & Analisis Kasus
Ini rekurensi non-homogen dengan bagian non-homogen $F(n) = 10^{n-1} = \frac{1}{10} 10^n$. 
Pertama, kita selesaikan bagian homogennya dulu: $a_n - 8a_{n-1} = 0 \implies r - 8 = 0 \implies r = 8$. Solusi homogennya $a_n^{(h)} = C \cdot 8^n$.
Kedua, cari solusi partikular $a_n^{(p)}$. Karena basis dari $F(n)$ adalah $10$, dan 10 **bukan** akar karakteristik homogen (akarnya cuma 8), kita bisa tebak solusi partikularnya berbentuk $a_n^{(p)} = P \cdot 10^n$. Kita substitusikan tebakan ini ke persamaan rekurensi asli untuk mencari nilai $P$.

#### 2. Solusi Matematis Formal
**1. Solusi Homogen ($a_n^{(h)}$):**
$a_n - 8a_{n-1} = 0 \implies r - 8 = 0 \implies r = 8 \implies a_n^{(h)} = C_1 8^n$

**2. Solusi Partikular ($a_n^{(p)}$):**
Dengan $F(n) = 10^{n-1} = \frac{1}{10} 10^n$, dan basis $10 \neq 8$, tebak $a_n^{(p)} = P \cdot 10^n$. Substitusikan ke rekurensi:
$$P \cdot 10^n = 8 \left( P \cdot 10^{n-1} \right) + 10^{n-1} \implies 10P = 8P + 1 \implies P = \frac{1}{2}$$
$$\implies a_n^{(p)} = \frac{1}{2} 10^n = 5 \cdot 10^{n-1}$$

**3. Solusi Total & Nilai Awal:**
$$a_n = C_1 8^n + \frac{1}{2} 10^n$$
Dengan $a_0 = 1 \implies C_1 + \frac{1}{2} = 1 \implies C_1 = \frac{1}{2}$.

$\dots$ Solusi eksplisit relasi rekurensi tersebut adalah:
$$a_n = \frac{1}{2} 8^n + \frac{1}{2} 10^n = 4 \cdot 8^{n-1} + 5 \cdot 10^{n-1}, \quad \text{untuk } n \ge 0$$
*(Verifikasi untuk $n=0$: $a_0 = \frac{1}{2} + \frac{1}{2} = 1$; verifikasi untuk $n=1$: $a_1 = 4 + 5 = 9$. Jawaban konsisten.)*

#### 3. Tips & Jebakan
> [!tip]
> Mengubah bentuk $10^{n-1}$ menjadi $\frac{1}{10} 10^n$ di awal akan mempermudah kalkulasi aljabar saat melakukan substitusi solusi partikular.

---

### Pembahasan Soal 3.b: $a_n = 3a_{n-1} - 2a_{n-2} + C_1^n$

#### 1. Intuisi & Analisis Kasus
Tunggu, apa itu $C_1^n$? Di kampus-kampus Indonesia, notasi $C_r^n$ itu merujuk pada kombinasi $_nC_r$ atau $\binom{n}{r}$. Jadi:
$$C_1^n = \binom{n}{1} = n$$
Persamaan kita sebenarnya adalah $a_n = 3a_{n-1} - 2a_{n-2} + n$.
1.  **Homogen:** $r^2 - 3r + 2 = 0 \implies (r-1)(r-2) = 0 \implies r = 1, 2$. Solusi homogen: $a_n^{(h)} = C_1 + C_2 2^n$.
2.  **Partikular:** $F(n) = n$ adalah polinomial derajat 1. Basisnya tersirat adalah $1^n$ (karena $n \cdot 1^n$). Karena nilai $1$ merupakan akar karakteristik homogen dengan kelipatan $m=1$, tebakan dasar kita $(A n + B)$ harus dikalikan dengan $n^1$. Maka tebakannya menjadi $a_n^{(p)} = n(An + B) = An^2 + Bn$.

#### 2. Solusi Matematis Formal
**1. Solusi Homogen ($a_n^{(h)}$):**
$a_n - 3a_{n-1} + 2a_{n-2} = 0 \implies r^2 - 3r + 2 = 0 \implies (r-1)(r-2) = 0 \implies a_n^{(h)} = C_1 + C_2 2^n$

**2. Solusi Partikular ($a_n^{(p)}$):**
Dengan non-homogen $F(n) = C_1^n = n = n \cdot 1^n$. Karena basis $1$ merupakan akar homogen ($m=1$), tebak:
$$a_n^{(p)} = n(An + B) = An^2 + Bn$$
Substitusikan ke relasi rekurensi $a_n - 3a_{n-1} + 2a_{n-2} = n$:
$$\left(An^2 + Bn\right) - 3\left(A(n-1)^2 + B(n-1)\right) + 2\left(A(n-2)^2 + B(n-2)\right) = n$$
$$An^2 + Bn - 3A(n^2 - 2n + 1) - 3B(n-1) + 2A(n^2 - 4n + 4) + 2B(n-2) = n$$
$$-2A n + (5A - B) = n$$
Samakan koefisien kedua ruas:
- Koefisien $n$: $-2A = 1 \implies A = -\frac{1}{2}$
- Konstanta: $5A - B = 0 \implies B = 5A = -\frac{5}{2}$
$$\implies a_n^{(p)} = -\frac{1}{2}n^2 - \frac{5}{2}n$$

**3. Solusi Total & Nilai Awal:**
$$a_n = C_1 + C_2 2^n - \frac{1}{2}n^2 - \frac{5}{2}n$$
Gunakan $a_0 = 0$ dan $a_1 = 1$:
- $n=0 \implies C_1 + C_2 = 0 \implies C_2 = -C_1$
- $n=1 \implies C_1 + 2C_2 - 3 = 1 \implies C_1 + 2C_2 = 4 \implies C_1 = -4, C_2 = 4$

$\therefore$ Solusi eksplisit lengkapnya adalah:
$$a_n = 2^{n+2} - \frac{1}{2}n^2 - \frac{5}{2}n - 4, \quad \text{untuk } n \ge 0$$

#### 3. Tips & Jebakan
> [!warning]
> **Jebakan Ujian:** Banyak mahasiswa lupa mengalikan tebakan dengan $n$ karena tidak sadar bahwa basis dari polinomial $n$ adalah $1^n$, dan angka 1 merupakan akar dari persamaan karakteristik homogen. Selalu periksa apakah $r=1$ adalah akar homogen saat menghadapi bagian non-homogen berupa polinomial!

---

### Pembahasan Soal 3.c: $a_n = 4a_{n-1} - 4a_{n-2} + 2^n$

#### 1. Intuisi & Analisis Kasus
1.  **Homogen:** $r^2 - 4r + 4 = 0 \implies (r-2)^2 = 0$. Kita punya akar ganda $r = 2$ dengan multiplisitas $m=2$. Solusi homogen: $a_n^{(h)} = (C_1 + C_2 n) 2^n$.
2.  **Partikular:** Bagian non-homogennya adalah $F(n) = 2^n$. Wah, basisnya adalah 2, yang merupakan akar karakteristik homogen dengan kelipatan $m=2$. Berarti tebakan awal kita $P \cdot 2^n$ harus dikalikan dengan $n^2$. Tebakan solusi partikularnya menjadi $a_n^{(p)} = P \cdot n^2 \cdot 2^n$.

#### 2. Solusi Matematis Formal
**1. Solusi Homogen ($a_n^{(h)}$):**
$a_n - 4a_{n-1} + 4a_{n-2} = 0 \implies r^2 - 4r + 4 = 0 \implies (r-2)^2 = 0 \implies a_n^{(h)} = (C_1 + C_2 n) 2^n$

**2. Solusi Partikular ($a_n^{(p)}$):**
Dengan $F(n) = 2^n$, basis $2$ adalah akar homogen ($m=2$). Tebak:
$$a_n^{(p)} = P n^2 2^n$$
Substitusikan ke relasi rekurensi $a_n - 4a_{n-1} + 4a_{n-2} = 2^n$:
$$P n^2 2^n - 4 \left( P(n-1)^2 2^{n-1} \right) + 4 \left( P(n-2)^2 2^{n-2} \right) = 2^n$$
Bagi kedua ruas dengan $2^{n-2}$:
$$4 P n^2 - 8 P (n-1)^2 + 4 P (n-2)^2 = 4 \implies P \left[ n^2 - 2(n^2 - 2n + 1) + (n^2 - 4n + 4) \right] = 1$$
$$P \cdot [2] = 1 \implies P = \frac{1}{2} \implies a_n^{(p)} = n^2 2^{n-1}$$

**3. Solusi Total & Nilai Awal:**
$$a_n = (C_1 + C_2 n) 2^n + n^2 2^{n-1}$$
Gunakan $a_0 = 0$ dan $a_1 = 1$:
- $n=0 \implies C_1 = 0$
- $n=1 \implies C_2 \cdot 2 + 1 = 1 \implies C_2 = 0$

$\therefore$ Solusi eksplisit relasi rekurensi tersebut adalah:
$$a_n = n^2 2^{n-1}, \quad \text{untuk } n \ge 0$$

#### 3. Tips & Jebakan
> [!tip]
> Karena konstanta homogennya bernilai 0 ($C_1 = C_2 = 0$), solusi akhir kita murni hanya berupa komponen partikular. Hasil ini memang tidak biasa, tapi secara matematis terbukti valid jika kita uji suku demi suku!

---

## Soal 4: Diagram Venn & Prinsip Inklusi-Eksklusi

**Dalam sebuah program studi Informatika, terdapat 175 mahasiswa mengambil mata kuliah *Data Mining*, dan 225 mahasiswa mengambil mata kuliah Metode Numerik. Jika terdapat 50 mahasiswa yang mengambil kedua mata kuliah, maka berapakah jumlah mahasiswa pada program studi Informatika? Ilustrasikan dengan menggunakan diagram venn!**

### 1. Intuisi & Analisis Kasus
Ini adalah aplikasi dasar dari prinsip inklusi-eksklusi untuk 2 himpunan. Kalau kita jumlahkan mahasiswa Data Mining (175) dan Metode Numerik (225) secara langsung, mahasiswa yang mengambil keduanya (50 orang) bakal terhitung dua kali (*double counting*). Makanya kita harus kurangi hasil penjumlahan tersebut dengan jumlah mahasiswa yang mengambil keduanya.

### 2. Solusi Matematis Formal
Misalkan $A$ dan $B$ berturut-turut adalah himpunan mahasiswa *Data Mining* dan Metode Numerik. Dari soal diperoleh:
$$|A| = 175, \quad |B| = 225, \quad |A \cap B| = 50$$
Berdasarkan Prinsip Inklusi-Eksklusi (PIE):
$$|A \cup B| = |A| + |B| - |A \cap B| = 175 + 225 - 50 = 350$$
$\therefore$ Jumlah total mahasiswa Informatika adalah $350$ orang.

**Ilustrasi Diagram Venn:**
```mermaid
graph TD
    classDef default fill:#1e1e2e,stroke:#cdd6f4,stroke-width:2px,color:#cdd6f4;
    subgraph semesta ["Semesta Informatika (Total = 350)"]
        A["DM Saja (125)"] --- AB["DM & MetNum (50)"] --- B["MetNum Saja (175)"]
    end
```

### 3. Tips & Jebakan
> [!tip]
> Saat menggambar diagram Venn di lembar jawaban ujian, pastikan kamu menuliskan angka di masing-masing daerah secara spesifik: 
> - Bagian lingkaran Data Mining saja: $175 - 50 = 125$.
> - Bagian tengah (irisan): $50$.
> - Bagian lingkaran Metode Numerik saja: $225 - 50 = 175$.
> Jumlah totalnya: $125 + 50 + 175 = 350$.

---

## Soal 5: Bilangan yang Habis Dibagi 5, 7, atau 11

**Tentukan berapa banyak bilangan bulat positif yang tidak lebih dari 1000 yang habis dibagi oleh 5, 7, atau 11!**

### 1. Intuisi & Analisis Kasus
"Tidak lebih dari 1000" berarti kita meninjau rentang $[1, 1000]$. Bilangan yang habis dibagi $d$ di antara 1 sampai $N$ banyaknya ada $\lfloor N/d \rfloor$. Kita definisikan tiga himpunan untuk masing-masing pembagi (5, 7, dan 11). Karena ada bilangan yang habis dibagi lebih dari satu angka (misal habis dibagi 35, yaitu kelipatan 5 dan 7), kita harus gunakan rumus PIE untuk 3 himpunan.

### 2. Solusi Matematis Formal
Misalkan semesta $S = \{x \in \mathbb{Z}^+ \mid x \le 1000\}$ ($|S| = 1000$). Definisikan $A_d$ sebagai himpunan bilangan bulat di $S$ yang habis dibagi $d$. Maka $|A_d| = \lfloor \frac{1000}{d} \rfloor$.
Kardinalitas masing-masing himpunan (menggunakan KPK untuk irisan karena pembaginya saling prima):
*   $|A_5| = 200, \quad |A_7| = 142, \quad |A_{11}| = 90$
*   $|A_5 \cap A_7| = |A_{35}| = \lfloor \frac{1000}{35} \rfloor = 28$
*   $|A_5 \cap A_{11}| = |A_{55}| = \lfloor \frac{1000}{55} \rfloor = 18$
*   $|A_7 \cap A_{11}| = |A_{77}| = \lfloor \frac{1000}{77} \rfloor = 12$
*   $|A_5 \cap A_7 \cap A_{11}| = |A_{385}| = \lfloor \frac{1000}{385} \rfloor = 2$

Berdasarkan rumus PIE untuk tiga himpunan:
$$
\begin{aligned}
|A_5 \cup A_7 \cup A_{11}| &= (|A_5| + |A_7| + |A_{11}|) - (|A_5 \cap A_7| + |A_5 \cap A_{11}| + |A_7 \cap A_{11}|) + |A_5 \cap A_7 \cap A_{11}| \\
&= (200 + 142 + 90) - (28 + 18 + 12) + 2 \\
&= 432 - 58 + 2 = 376
\end{aligned}
$$
$\therefore$ Ada $376$ bilangan bulat positif yang habis dibagi 5, 7, atau 11.

### 3. Tips & Jebakan
> [!warning]
> Lambang $\lfloor \cdot \rfloor$ adalah fungsi floor (pembulatan ke bawah). Pastikan kamu membulatkan hasil bagi ke bawah, bukan ke atas atau pembulatan terdekat biasa! Contoh: $1000/7 \approx 142.857 \implies \lfloor 142.857 \rfloor = 142$.

---

## Soal 6: Rumus Gabungan Empat Himpunan

**Berikan formula (rumus) untuk menentukan banyaknya anggota dari gabungan empat buah himpunan!**

### 1. Intuisi & Analisis Kasus
Ini adalah generalisasi dari prinsip inklusi-eksklusi untuk $n=4$. Polanya selalu sama:
1.  Jumlahkan ukuran masing-masing himpunan tunggal ($+$).
2.  Kurangi dengan semua kombinasi irisan 2 himpunan ($-$).
3.  Jumlahkan kembali dengan semua kombinasi irisan 3 himpunan ($+$).
4.  Kurangi dengan irisan dari keempat himpunan sekaligus ($-$).

### 2. Solusi Matematis Formal
Misalkan empat buah himpunan tersebut masing-masing adalah $A$, $B$, $C$, dan $D$. Berdasarkan **Prinsip Inklusi-Eksklusi (PIE)**, formula untuk menghitung banyaknya anggota dari gabungan keempat himpunan tersebut disusun dengan menjumlahkan ukuran himpunan tunggal, mengurangkan irisan berpasangan (derajat 2), menambahkan irisan tiga himpunan (derajat 3), dan mengurangkan irisan keempat himpunan sekaligus (derajat 4):

$$
\begin{aligned}
|A \cup B \cup C \cup D| = & \left( |A| + |B| + |C| + |D| \right) \\
& - \left( |A \cap B| + |A \cap C| + |A \cap D| + |B \cap C| + |B \cap D| + |C \cap D| \right) \\
& + \left( |A \cap B \cap C| + |A \cap B \cap D| + |A \cap C \cap D| + |B \cap C \cap D| \right) \\
& - |A \cap B \cap C \cap D|
\end{aligned}
$$

Suku-suku di atas dapat dikelompokkan berdasarkan jumlah himpunan yang diiriskan:
1. Ukuran individu: $\binom{4}{1} = 4$ suku.
2. Irisan 2 himpunan: $\binom{4}{2} = 6$ suku (tanda negatif).
3. Irisan 3 himpunan: $\binom{4}{3} = 4$ suku (tanda positif).
4. Irisan 4 himpunan: $\binom{4}{4} = 1$ suku (tanda negatif).

### 3. Tips & Jebakan
> [!tip]
> Biar nggak ada irisan yang terlewat, kamu bisa cek jumlah suhunya pakai kombinasi:
> - Irisan 2 himpunan: ada $\binom{4}{2} = 6$ suku.
> - Irisan 3 himpunan: ada $\binom{4}{3} = 4$ suku.
> - Irisan 4 himpunan: ada $\binom{4}{4} = 1$ suku.
> Total suku di ruas kanan harus pas!

---

## Soal 7: Jumlah Solusi Persamaan dengan Pembatas (PIE)

**Dengan menggunakan prinsip *inclusion-exclusion*, berapa banyak solusi dari $x_1 + x_2 + x_3 = 11$, ketika $x_1$, $x_2$, dan $x_3$ merupakan bilangan bulat non-negatif dengan $x_1 \le 3$, $x_2 \le 4$, dan $x_3 \le 6$?**

### 1. Intuisi & Analisis Kasus
Kita mau menaruh 11 objek identik ke dalam 3 wadah dengan kapasitas terbatas. 
- Semesta $S$ adalah total cara tanpa batas atas (cuma dibatasi $x_i \ge 0$). Rumusnya pakai kombinasi berulang bintang dan batang (*stars and bars*).
- Kita definisikan sifat pelanggaran:
  - $P_1$: wadah 1 jebol ($x_1 \ge 4$)
  - $P_2$: wadah 2 jebol ($x_2 \ge 5$)
  - $P_3$: wadah 3 jebol ($x_3 \ge 7$)
Kita hitung jumlah solusi yang melanggar masing-masing sifat ini dengan melakukan translasi variabel (misal $y_1 = x_1 - 4 \ge 0$), lalu gabungkan menggunakan PIE untuk membuang solusi ilegal.

### 2. Solusi Matematis Formal
Dengan Teorema *Stars and Bars*, banyaknya solusi non-negatif persamaan $x_1 + x_2 + x_3 = N$ adalah $\binom{N + k - 1}{k - 1}$.
Kardinalitas semesta (tanpa batas atas):
$$|S| = \binom{11 + 3 - 1}{3 - 1} = \binom{13}{2} = 78$$

Definisikan sifat pelanggaran batas atas:
*   $P_1: x_1 \ge 4 \implies y_1 + x_2 + x_3 = 7 \implies |P_1| = \binom{7+3-1}{3-1} = \binom{9}{2} = 36$
*   $P_2: x_2 \ge 5 \implies x_1 + y_2 + x_3 = 6 \implies |P_2| = \binom{6+3-1}{3-1} = \binom{8}{2} = 28$
*   $P_3: x_3 \ge 7 \implies x_1 + x_2 + y_3 = 4 \implies |P_3| = \binom{4+3-1}{3-1} = \binom{6}{2} = 15$

Hitung irisan pelanggaran (translasi bersama):
*   $|P_1 \cap P_2|: x_1 \ge 4 \land x_2 \ge 5 \implies y_1 + y_2 + x_3 = 2 \implies |P_1 \cap P_2| = \binom{2+3-1}{3-1} = \binom{4}{2} = 6$
*   $|P_1 \cap P_3|: x_1 \ge 4 \land x_3 \ge 7 \implies y_1 + x_2 + y_3 = 0 \implies |P_1 \cap P_3| = \binom{0+3-1}{3-1} = \binom{2}{2} = 1$
*   $|P_2 \cap P_3| = 0$ (karena batas minimal $5 + 7 = 12 > 11$)
*   $|P_1 \cap P_2 \cap P_3| = 0$ (karena batas minimal $4 + 5 + 7 = 16 > 11$)

Berdasarkan rumus PIE:
$$
\begin{aligned}
N &= |S| - (|P_1| + |P_2| + |P_3|) + (|P_1 \cap P_2| + |P_1 \cap P_3| + |P_2 \cap P_3|) - |P_1 \cap P_2 \cap P_3| \\
&= 78 - (36 + 28 + 15) + (6 + 1 + 0) - 0 = 6
\end{aligned}
$$
$\therefore$ Ada $6$ solusi valid yang memenuhi seluruh batasan.

#### 3. Tips & Jebakan
> [!tip]
> Karena jumlah solusinya sedikit (hanya 6), kamu bisa dengan cepat memverifikasi secara manual saat ujian untuk memastikan jawabanmu benar!
> Pasangan $(x_1, x_2, x_3)$ yang valid adalah: 
> $(3, 4, 4), (3, 3, 5), (3, 2, 6), (2, 4, 5), (2, 3, 6),$ dan $(1, 4, 6)$.

---

## Soal 8: Bilangan Bukan Pangkat Dua atau Lebih Tinggi

**Berapa banyak bilangan bulat positif kurang dari 10.000 yang bukan merupakan pangkat dua atau lebih tinggi dari suatu bilangan bulat?**

### 1. Intuisi & Analisis Kasus
"Kurang dari 10.000" artinya kita meninjau rentang $[1, 9999]$.
Kita cari total bilangan pangkat sempurna dalam rentang ini dengan meninjau basis pangkat prima saja ($p = 2, 3, 5, 7, 11, 13$), lalu gunakan PIE untuk membuang irisan (seperti bilangan perpangkatan 6 yang merupakan pangkat 2 sekaligus pangkat 3). Terakhir, kita kurangkan semesta (9999) dengan total bilangan pangkat sempurna tersebut.

### 2. Solusi Matematis Formal
Misalkan semesta $U = \{1, 2, \dots, 9999\}$ ($|U| = 9999$). Kita cari bilangan yang berbentuk pangkat sempurna $x^k$ ($k \ge 2$) dengan menganalisis eksponen berupa bilangan prima $p \in \{2, 3, 5, 7, 11, 13\}$ (karena basis terkecil $2^{17} > 10000$).

Definisikan $S_p$ sebagai himpunan bilangan pangkat $p$ dengan basis $x \ge 2$:
*   $|S_2| = \lfloor \sqrt{9999} \rfloor - 1 = 99 - 1 = 98$
*   $|S_3| = \lfloor \sqrt[3]{9999} \rfloor - 1 = 21 - 1 = 20$
*   $|S_5| = \lfloor \sqrt[5]{9999} \rfloor - 1 = 6 - 1 = 5$
*   $|S_7| = \lfloor \sqrt[7]{9999} \rfloor - 1 = 3 - 1 = 2$
*   $|S_{11}| = \lfloor \sqrt[11]{9999} \rfloor - 1 = 2 - 1 = 1$
*   $|S_{13}| = \lfloor \sqrt[13]{9999} \rfloor - 1 = 2 - 1 = 1$

Hitung irisan yang menghasilkan pangkat komposit (basis $x \ge 2$):
*   $|S_2 \cap S_3| = |S_6| = \lfloor \sqrt[6]{9999} \rfloor - 1 = 4 - 1 = 3$
*   $|S_2 \cap S_5| = |S_{10}| = \lfloor \sqrt[10]{9999} \rfloor - 1 = 2 - 1 = 1$
*   Irisan lainnya bernilai kosong karena basis terkecil $2^{14} > 10000$.

Berdasarkan PIE, jumlah pangkat sempurna dengan basis $x \ge 2$ adalah:
$$
\begin{aligned}
|\bigcup_{p} S_p| &= \sum |S_p| - (|S_2 \cap S_3| + |S_2 \cap S_5|) \\
&= (98 + 20 + 5 + 2 + 1 + 1) - (3 + 1) = 123
\end{aligned}
$$
Masukkan kembali angka 1 (karena $1 = 1^2$):
$$\text{Total pangkat sempurna} = 123 + 1 = 124$$
Banyaknya bilangan yang **bukan** pangkat sempurna:
$$|U| - \text{Total pangkat sempurna} = 9999 - 124 = 9875$$

Jadi, ada $9875$ bilangan bulat positif kurang dari 10.000 yang bukan merupakan pangkat sempurna.

### 3. Tips & Jebakan
> [!warning]
> **Jebakan Definisi 1:** Apakah 1 dianggap sebagai pangkat sempurna? Ya, karena $1 = 1^2$ (pangkat dua dari bilangan bulat 1). Pastikan kamu memasukkan angka 1 ke dalam hitungan pengurang!
> **Jebakan Batas Kurang Dari:** Soal meminta bilangan "kurang dari 10.000", artinya angka 10.000 sendiri tidak masuk ke dalam semesta yang dihitung!

---

## Soal 9: Sifat-Sifat Relasi Integral

**Tentukan apakah relasi $R$ pada himpunan bilangan bulat bersifat refleksif, simetris, antisimetris, dan/atau transitif, ketika $(x,y) \in R$ jika dan hanya jika:**
*   a. $x \neq y$
*   b. $x = y^2$

### Pembahasan Soal 9.a: $x \neq y$

#### 1. Intuisi & Analisis Kasus
Relasinya adalah "tidak sama dengan".
- **Refleksif:** Apakah setiap angka tidak sama dengan dirinya sendiri? Jelas salah, karena $x = x$.
- **Simetris:** Jika $x \neq y$, apakah pasti $y \neq x$? Ya, jelas benar.
- **Antisimetris:** Jika $x \neq y$ dan $y \neq x$, apakah haruslah $x = y$? Lah, kontradiksi dong. Berarti tidak antisimetris.
- **Transitif:** Jika $x \neq y$ dan $y \neq z$, apakah pasti $x \neq z$? Belum tentu! Contohnya $1 \neq 2$ dan $2 \neq 1$, tapi ternyata $1 = 1$. Jadi tidak transitif.

#### 2. Solusi Matematis Formal
Definisikan relasi $R = \{(x,y) \in \mathbb{Z}^2 \mid x \neq y\}$.
*   **Refleksif:** Tidak. $\forall x \in \mathbb{Z}, (x,x) \in R \iff x \neq x$ (kontradiksi). Contoh penyangkal: $(1,1) \notin R$ karena $1 = 1$.
*   **Simetris:** Ya. $\forall x,y \in \mathbb{Z}$, jika $(x,y) \in R \implies x \neq y \implies y \neq x \implies (y,x) \in R$.
*   **Antisimetris:** Tidak. $\forall x,y \in \mathbb{Z}$, $(x,y) \in R \land (y,x) \in R \implies x \neq y \land y \neq x$, yang tidak mengimplikasikan $x = y$. Contoh penyangkal: $x=1, y=2 \implies (1,2) \in R \land (2,1) \in R$, tetapi $1 \neq 2$.
*   **Transitif:** Tidak. $\forall x,y,z \in \mathbb{Z}$, $(x,y) \in R \land (y,z) \in R \implies x \neq y \land y \neq z \not\implies x \neq z$. Contoh penyangkal: $x=1, y=2, z=1 \implies (1,2) \in R \land (2,1) \in R$, tetapi $(1,1) \notin R$.

---

### Pembahasan Soal 9.b: $x = y^2$

#### 1. Intuisi & Analisis Kasus
- **Refleksif:** Apakah semua bilangan bulat sama dengan kuadrat dirinya sendiri? Nggak dong, $2 \neq 2^2 = 4$.
- **Simetris:** Jika $x = y^2$, apakah pasti $y = x^2$? Nggak, $4 = 2^2$ tapi $2 \neq 4^2 = 16$.
- **Antisimetris:** Jika $x = y^2$ dan $y = x^2$, maka $x = (x^2)^2 = x^4$. Bilangan bulat yang memenuhi hanya $x=0$ atau $x=1$. Pada kedua kasus ini, terbukti $x = y$. Jadi relasi ini antisimetris.
- **Transitif:** Jika $x = y^2$ dan $y = z^2$, apakah $x = z^2$? Nggak dong, malah $x = (z^2)^2 = z^4$.

#### 2. Solusi Matematis Formal
Definisikan relasi $R = \{(x,y) \in \mathbb{Z}^2 \mid x = y^2\}$.
*   **Refleksif:** Tidak. $\forall x \in \mathbb{Z}, (x,x) \in R \iff x = x^2 \iff x(x-1) = 0$, yang hanya benar jika $x \in \{0, 1\}$. Contoh penyangkal: untuk $x=2 \in \mathbb{Z}$, $2 \neq 2^2 \implies (2,2) \notin R$.
*   **Simetris:** Tidak. $\forall x,y \in \mathbb{Z}$, $(x,y) \in R \implies x = y^2 \not\implies y = x^2$. Contoh penyangkal: $x=4, y=2 \implies (4,2) \in R$ (karena $4=2^2$), tetapi $(2,4) \notin R$ (karena $2 \neq 4^2$).
*   **Antisimetris:** Ya. $\forall x,y \in \mathbb{Z}$, jika $(x,y) \in R \land (y,x) \in R$:
    $$\begin{aligned}
    x = y^2 \;\land\; y = x^2 &\implies x = (x^2)^2 \implies x^4 - x = 0 \\
    &\implies x(x^3 - 1) = 0 \implies x = 0 \lor x = 1 \quad (\because x \in \mathbb{Z})
    \end{aligned}$$
    - Jika $x = 0 \implies y = 0^2 = 0 \implies x = y$.
    - Jika $x = 1 \implies y = 1^2 = 1 \implies x = y$.
    Karena untuk setiap kasus diperoleh $x = y$, relasi bersifat antisimetris.
*   **Transitif:** Tidak. $\forall x,y,z \in \mathbb{Z}$, jika $(x,y) \in R \land (y,z) \in R \implies x=y^2 \;\land\; y=z^2 \implies x = (z^2)^2 = z^4 \not\implies x = z^2$. Contoh penyangkal: $x=16, y=4, z=2 \implies (16,4) \in R \land (4,2) \in R$, tetapi $(16,2) \notin R$ karena $16 \neq 2^2$.

#### 3. Tips & Jebakan
> [!tip]
> Menunjukkan sifat antisimetris secara matematis sering kali membingungkan. Ingat definisi: jika premis $(x,y) \in R \land (y,x) \in R$ tidak pernah terpenuhi untuk elemen yang berbeda ($x \neq y$), maka secara *vacuously true* sifat antisimetris tetap terpenuhi!

---

## Soal 10: Operasi Relasi pada Bilangan Real

**Perhatikan relasi berikut pada himpunan bilangan real:**
*   $R_1 = \{(a,b) \in \mathbb{R}^2 \mid a > b\}$
*   $R_2 = \{(a,b) \in \mathbb{R}^2 \mid a \ge b\}$
*   $R_3 = \{(a,b) \in \mathbb{R}^2 \mid a < b\}$
*   $R_4 = \{(a,b) \in \mathbb{R}^2 \mid a \le b\}$

**Tentukan:**
*   a. $R_1 \cup R_3$
*   b. $R_2 \oplus R_4$
*   c. $R_2 \circ R_4$

### Pembahasan Soal 10.a: $R_1 \cup R_3$

#### 1. Intuisi & Analisis Kasus
$R_1$ ($a > b$) dan $R_3$ ($a < b$). Gabungannya adalah semua pasangan real kecuali yang nilainya sama ($a = b$).

#### 2. Solusi Matematis Formal
Berdasarkan definisi gabungan dan hukum trikotomi $\mathbb{R}$:
$$\begin{aligned}
R_1 \cup R_3 &= \{(a,b) \in \mathbb{R}^2 \mid a > b\} \cup \{(a,b) \in \mathbb{R}^2 \mid a < b\} \\
&= \{(a,b) \in \mathbb{R}^2 \mid a > b \lor a < b\} \\
&= \{(a,b) \in \mathbb{R}^2 \mid a \neq b\}
\end{aligned}$$

---

### Pembahasan Soal 10.b: $R_2 \oplus R_4$

#### 1. Intuisi & Analisis Kasus
$R_2 \oplus R_4$ ($a \ge b \oplus a \le b$). Gabungannya seluruh $\mathbb{R}^2$, irisannya $a=b$. Jadi sisanya $a \neq b$.

#### 2. Solusi Matematis Formal
Berdasarkan definisi $A \oplus B = (A \cup B) \setminus (A \cap B)$:
1. $R_2 \cup R_4 = \mathbb{R}^2$ (karena $\forall a,b: a \ge b \lor a \le b$).
2. $R_2 \cap R_4 = \{(a,b) \in \mathbb{R}^2 \mid a = b\}$ (karena $a \ge b \land a \le b \iff a = b$).

Dengan demikian:
$$R_2 \oplus R_4 = \mathbb{R}^2 \setminus \{(a,b) \in \mathbb{R}^2 \mid a = b\} = \{(a,b) \in \mathbb{R}^2 \mid a \neq b\}$$

---

### Pembahasan Soal 10.c: $R_2 \circ R_4$

#### 1. Intuisi & Analisis Kasus
$(a,c) \in R_2 \circ R_4 \iff \exists b: a \le b \land c \le b$. Selalu ada $b = \max(a, c)$, jadi hasilnya seluruh $\mathbb{R}^2$.

#### 2. Solusi Matematis Formal
Berdasarkan definisi komposisi relasi:
$$R_2 \circ R_4 = \{(a,c) \in \mathbb{R}^2 \mid \exists b \in \mathbb{R} \text{ s.t. } a \le b \land c \le b\}$$
Untuk setiap $(a,c) \in \mathbb{R}^2$, pilih $b = \max(a,c)$. Karena $b \ge a$ dan $b \ge c$, maka eksistensi $b$ terjamin. Maka:
$$R_2 \circ R_4 = \mathbb{R}^2$$

#### 3. Tips & Jebakan
> [!tip]
> Ingat aturan urutan pengerjaan komposisi relasi $S \circ R$: kita jalani relasi $R$ dulu baru kemudian relasi $S$. Jadi, cari $b$ yang menghubungkan $a \to^R b \to^S c$.

---

## Soal 11: Proyeksi Relasi Database

**Tentukan tabel $P_{1,2}$ dari relasi:**

| Student | Major | Course |
| --- | --- | --- |
| Joko | Biology | BA 290 |
| Joko | Biology | MD 451 |
| Markus | Physics | PY 182 |
| ... | ... | ... |

### 1. Intuisi & Analisis Kasus
Proyeksi $P_{1,2}$ mengambil kolom Student dan Major. Baris duplikat setelah proyeksi harus dihapus.

### 2. Solusi Matematis Formal
$P_{1,2}(R) = \{(t_1, t_2) \mid \exists t_3: (t_1, t_2, t_3) \in R\}$.
*   (Joko, Biology, BA290) & (Joko, Biology, MD451) $\to$ (Joko, Biology)
*   (Markus, Physics, PY182) & (Markus, Physics, CT212) $\to$ (Markus, Physics)
*   (Shiren, CS, BG215) & (Shiren, CS, CS812) $\to$ (Shiren, CS)
*   (Steve, Math, MD712) $\to$ (Steve, Math)

| Student | Major |
| --- | --- |
| Joko | Biology |
| Markus | Physics |
| Shiren | Computer Science |
| Steve | Mathematics |

### 3. Tips & Jebakan
> [!warning]
> Nggak menghapus baris duplikat adalah kesalahan fatal. Himpunan dalam matematika diskrit tidak boleh memiliki elemen ganda!

---

## Soal 12: Contoh Proyeksi Irisan Relasi n-ary

**Contoh: $P_{i_1, \dots, i_m}(R \cap S) \neq P_{i_1, \dots, i_m}(R) \cap P_{i_1, \dots, i_m}(S)$!**

### 1. Intuisi & Analisis Kasus
Buat $R$ dan $S$ punya proyeksi sama di satu kolom, tapi nilai di kolom lain berbeda, sehingga irisan $R \cap S$ kosong.

### 2. Solusi Matematis Formal
Misalkan $R = \{(1, 2)\}$ dan $S = \{(1, 3)\}$. Proyeksi kolom ke-1 ($P_1$):
*   $R \cap S = \emptyset \implies P_1(R \cap S) = \emptyset$.
*   $P_1(R) = \{1\}, P_1(S) = \{1\} \implies P_1(R) \cap P_1(S) = \{1\}$.
Karena $\emptyset \neq \{1\}$, terbukti $P_1(R \cap S) \neq P_1(R) \cap P_1(S)$.

### 3. Tips & Jebakan
> [!tip]
> Selalu pilih ukuran relasi terkecil untuk *counterexample*.

---

## Soal 13: Matriks Relasi Kuadrat

**Tentukan $M_{R^2}$ jika $M_R = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 0 \end{bmatrix}$!**

### 1. Intuisi & Analisis Kasus
$M_{R^2} = M_R \odot M_R$ dengan operasi (AND, OR). Simpul $i$ ke $j$ bernilai 1 jika ada jalur 2 langkah.

### 2. Solusi Matematis Formal
$m_{ij} = \bigvee_{k=1}^{3} (M_{ik} \land M_{kj})$:
*   Baris 1: $(0,1,0) \odot M_R = (0, 1, 1)$
*   Baris 2: $(0,1,1) \odot M_R = (1, 1, 1)$
*   Baris 3: $(1,0,0) \odot M_R = (0, 1, 0)$

$$M_{R^2} = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix}$$

### 3. Tips & Jebakan
> [!tip]
> Trik graf: cari jalur 2 langkah dari $i$ ke $j$. Contoh: $1 \to 2 \to 2 \implies m_{12}=1$.

---

## Soal 14: Ordered Pairs dari Directed Graph

*(Graf a & b)*

### 1. Intuisi & Analisis Kasus
$(x,y) \in R$ jika ada panah dari $x$ ke $y$.

### 2. Solusi Matematis Formal
*   $R_a = \{(a, b), (b, a), (b, b), (c, a), (c, c), (c, d), (d, d)\}$
*   $R_b = \{(b, a), (a, c), (c, d), (d, b)\}$

### 3. Tips & Jebakan
> [!warning]
> Perhatikan arah panah! Panah $c \to a$ adalah $(c, a)$.

---

## Soal 15: Relasi Pembagian pada Bilangan Asli (Poset)

**Apakah $aRb \iff a \mid b$ pada $\mathbb{N}$ merupakan *partial orderings*?**

### 1. Intuisi & Analisis Kasus
Buktikan 3 sifat: refleksif, antisimetris, dan transitif.

### 2. Solusi Matematis Formal
1.  **Refleksif:** $a = 1 \cdot a \implies a \mid a$.
2.  **Antisimetris:** $a \mid b \land b \mid a \implies b=ka, a=mb \implies a=mka \implies mk=1$. Untuk $m,k \in \mathbb{N}$, maka $m=k=1 \implies a=b$.
3.  **Transitif:** $a \mid b \land b \mid c \implies b=pa, c=qb \implies c=(qp)a \implies a \mid c$.
Terbukti $R$ adalah *partial orderings*.

### 3. Tips & Jebakan
> [!warning]
> Antisimetris di $\mathbb{N}$ benar, tapi di $\mathbb{Z}$ salah ($2 \mid -2$ dan $-2 \mid 2$, tapi $2 \neq -2$).

---

## Soal 16: Menentukan Chain dari Poset

**Tentukan 3 buah *chain* dari poset $A=\{a, b, c, d\}$ dengan relasi $R$!**

### 1. Intuisi & Analisis Kasus
*Chain* adalah subhimpunan yang semua elemennya saling sebanding.

### 2. Solusi Matematis Formal
Subhimpunan $C$ disebut **chain** jika: $\forall x, y \in C, (x,y) \in R \lor (y,x) \in R$.
Pada poset $(A, R)$:
*   $a$ dan $d$ sebanding dengan semua elemen.
*   $b, d$ sebanding; $c, d$ sebanding; tapi $b, c$ tidak sebanding.

3 contoh *chain*:
1.  $C_1 = \{a, b, d\}$ (pasangan $(a,b), (b,d), (a,d) \in R$).
2.  $C_2 = \{a, c, d\}$ (pasangan $(a,c), (c,d), (a,d) \in R$).
3.  $C_3 = \{a, b\}$ (pasangan $(a,b) \in R$).

### 3. Tips & Jebakan
> [!tip]
> Selalu berikan chain maksimal untuk nilai penuh!

---

## Soal 17: Radius & Interval Kekonvergenan Deret Faktorial

**Tentukan radius dan interval konvergen dari deret berikut:**
$$\sum_{n=0}^{\infty} n! (2x+1)^n$$

### 1. Intuisi & Analisis Kasus
Ada faktorial $n!$ di dalam deret kita. Faktorial itu tumbuhnya cepet banget, lho! Nah, kalau kita punya deret pangkat yang dikali dengan $n!$, dia bakal gampang banget divergen (alias meledak ke tak hingga) untuk hampir semua nilai $x$. Satu-satunya cara biar deret ini nggak meledak adalah kalau suku $(2x+1)$ nilainya tepat $0$. Kalau $(2x+1) = 0$, semua suku setelah suku pertama bakal jadi $0$, jadinya deretnya konvergen. 
Untuk membuktikannya secara formal, kita kudu pake **Uji Rasio (Ratio Test)**. Yuk, kita bongkar hitung-hitungannya!

### 2. Solusi Matematis Formal
Gunakan Uji Rasio untuk menguji kekonvergenan absolut deret $u_n(x) = n! (2x+1)^n$:
$$
\begin{aligned}
L &= \lim_{n \to \infty} \left| \frac{u_{n+1}(x)}{u_n(x)} \right| = \lim_{n \to \infty} \left| \frac{(n+1)! (2x+1)^{n+1}}{n! (2x+1)^n} \right| \\
&= \lim_{n \to \infty} (n+1) |2x+1|
\end{aligned}
$$

Analisis hasil limit $L$:
1. Jika $2x+1 \neq 0 \iff x \neq -\frac{1}{2}$, maka $L = \infty > 1$ (deret divergen).
2. Jika $2x+1 = 0 \iff x = -\frac{1}{2}$, deret menjadi $\sum_{n=0}^{\infty} n! (0)^n = 1 + 0 + 0 + \dots = 1$ (deret konvergen).

$\therefore$ Radius kekonvergenan $R = 0$ dan interval kekonvergenan adalah $\left\{-\frac{1}{2}\right\}$ (atau $x = -\frac{1}{2}$).

### 3. Tips & Jebakan
> [!warning]
> **Jebakan $0^0$:** Di matematika, khususnya pada deret pangkat, kita mendefinisikan $0^0 = 1$ untuk suku pertama deret ($n=0$). Jangan terkecoh mengira deretnya tidak terdefinisi atau langsung bernilai $0$ ya!
> **Kecepatan Tumbuh Faktorial:** Ingat cheatsheet instan ini: kalau deret pangkat memuat faktorial di pembilang tanpa ada pembagi yang sebanding (seperti faktorial lain di penyebut), radius kekonvergenannya hampir pasti $R = 0$.

---

## Soal 18: Radius & Interval Kekonvergenan Deret Alternating

**Tentukan radius dan interval konvergen dari deret berikut:**
$$\sum_{n=1}^{\infty} \frac{x^{2n}}{(-3)^n}$$

### 1. Intuisi & Analisis Kasus
Coba perhatikan pangkat dari $x$, di situ tertulis $x^{2n}$, bukan $x^n$. Berarti deret ini cuma berisi pangkat-pangkat genap ($x^2, x^4, x^6, \dots$). Di penyebutnya ada $(-3)^n$, yang artinya tanda deretnya bakal selang-seling (alternating) positif-negatif. 
Sama kayak soal sebelumnya, senjata utama kita buat nyari batas kekonvergenan deret adalah **Uji Rasio**. Setelah dapet interval terbukanya, kita kudu ceki-ceki juga nilai di titik-titik ujung (boundary) interval tersebut secara manual untuk memastikan apakah titik ujungnya ikut konvergen atau malah divergen.

### 2. Solusi Matematis Formal
Gunakan Uji Rasio untuk menguji kekonvergenan absolut deret $a_n(x) = \frac{x^{2n}}{(-3)^n}$:
$$
L = \lim_{n \to \infty} \left| \frac{a_{n+1}(x)}{a_n(x)} \right| = \lim_{n \to \infty} \left| \frac{x^{2(n+1)}}{(-3)^{n+1}} \cdot \frac{(-3)^n}{x^{2n}} \right| = \lim_{n \to \infty} \left| \frac{x^2}{-3} \right| = \frac{x^2}{3}
$$
Deret konvergen mutlak jika $L < 1 \iff \frac{x^2}{3} < 1 \iff x^2 < 3 \iff |x| < \sqrt{3}$. Maka $R = \sqrt{3}$.

Uji kekonvergenan pada titik-titik ujung interval ($x = \pm\sqrt{3}$):
* Untuk $x = \pm\sqrt{3}$, suku deret menjadi:
  $$\frac{(\pm\sqrt{3})^{2n}}{(-3)^n} = \frac{3^n}{(-3)^n} = (-1)^n$$
* Deret $\sum_{n=1}^{\infty} (-1)^n$ divergen karena $\lim_{n\to\infty} (-1)^n \neq 0$ (Uji Divergensi).

$\therefore$ Radius kekonvergenan $R = \sqrt{3}$ dan interval kekonvergenan adalah $(-\sqrt{3}, \sqrt{3})$ atau $-\sqrt{3} < x < \sqrt{3}$.

### 3. Tips & Jebakan
> [!warning]
> **Jebakan Pangkat Genap:** Ketika kamu menyederhanakan $\frac{x^{2(n+1)}}{x^{2n}}$, hasilnya adalah $x^2$, bukan $x$! Jangan sampai ceroboh dan menulis limitnya sebagai $\frac{|x|}{3}$ ya.
> **Selalu Tes Titik Ujung:** Nilai $R$ saja belum cukup untuk menentukan interval kekonvergenan. Kamu wajib mensubstitusikan nilai titik ujung $x = \pm R$ kembali ke deret awal untuk mengecek kekonvergenan di perbatasan.

---

## Soal 19: Deret Taylor untuk $f(x) = e^{-x}$

**Tentukan deret Taylor untuk:**
$$f(x) = e^{-x}$$
**pada $x = -4$**

### 1. Intuisi & Analisis Kasus
Deret Taylor itu sebenarnya cara kita mendekati suatu fungsi menggunakan penjumlahan polinomial tak hingga yang berpusat di suatu titik $x = a$. Rumus umumnya adalah:
$$T(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n$$
Di sini, fungsi kita adalah $f(x) = e^{-x}$ dan pusatnya $a = -4$. Langkah pertamanya simpel banget: kita cari pola turunan ke-$n$ dari $f(x)$, terus kita masukin nilai $x = -4$. Terakhir, tinggal susun semuanya ke rumus umum deret Taylor.

### 2. Solusi Matematis Formal
Cari turunan ke-$n$ dari $f(x) = e^{-x}$ dan evaluasi di $x = -4$:
$$f^{(n)}(x) = (-1)^n e^{-x} \implies f^{(n)}(-4) = (-1)^n e^4$$

Substitusikan hasil ke dalam rumus umum deret Taylor di $a = -4$:
$$
\begin{aligned}
T(x) &= \sum_{n=0}^{\infty} \frac{f^{(n)}(-4)}{n!} (x + 4)^n = \sum_{n=0}^{\infty} \frac{(-1)^n e^4}{n!} (x + 4)^n \\
&= e^4 - e^4(x+4) + \frac{e^4}{2!}(x+4)^2 - \frac{e^4}{3!}(x+4)^3 + \dots
\end{aligned}
$$

### 3. Tips & Jebakan
> [!tip]
> **Trik Tanda Negatif:** Perhatikan pola tandanya yang selang-seling ($+ , - , + , - , \dots$) karena adanya faktor $(-1)^n$. Hal ini disebabkan oleh aturan rantai (chain rule) saat menurunkan $e^{-x}$ berulang kali. Pastikan kamu teliti menuliskan $(-1)^n$ pada bentuk deretnya!

---

## Soal 20: Deret Taylor untuk $f(x) = \frac{1}{x^2}$

**Tentukan deret Taylor untuk:**
$$f(x) = \frac{1}{x^2}$$
**pada $x = -1$**

### 1. Intuisi & Analisis Kasus
Fungsi kita kali ini berbentuk pecahan: $f(x) = x^{-2}$, dan kita pengen bikin deret Taylor-nya di sekitar $x = -1$.
Sama kayak soal sebelumnya, kita kudu cari pola turunan ke-$n$ dari $f(x)$, lalu evaluasi nilainya di $x = -1$. Karena turunan dari $x^{-2}$ bakal menghasilkan koefisien yang terus bertambah besar (akibat perkalian eksponen negatif saat diturunkan), kita bakal nemuin faktorial lagi di hasil akhirnya. 
Sebagai cara alternatif untuk verifikasi, kita juga bisa pakai manipulasi deret geometri dasar lewat substitusi variabel, lho. Tapi biar dosen kamu senang, mari kita pake cara turunan formal dulu ya!

### 2. Solusi Matematis Formal
**Metode 1: Turunan Formal**
Tentukan turunan ke-$n$ dari $f(x) = x^{-2}$ dan nilainya di $x = -1$:
$$f^{(n)}(x) = (-1)^n (n+1)! x^{-(n+2)} \implies f^{(n)}(-1) = (-1)^n (n+1)! (-1)^{-(n+2)} = (n+1)!$$

Substitusikan ke rumus deret Taylor di $a = -1$:
$$
\begin{aligned}
T(x) &= \sum_{n=0}^{\infty} \frac{f^{(n)}(-1)}{n!} (x + 1)^n = \sum_{n=0}^{\infty} \frac{(n+1)!}{n!} (x+1)^n \\
&= \sum_{n=0}^{\infty} (n+1)(x+1)^n = 1 + 2(x+1) + 3(x+1)^2 + 4(x+1)^3 + \dots
\end{aligned}
$$

**Metode 2: Verifikasi dengan Deret Geometri**
Mulai dari deret geometri dasar untuk $|u| < 1$:
$$
\begin{aligned}
\frac{1}{1-u} = \sum_{n=0}^{\infty} u^n &\implies \frac{d}{du}\left(\frac{1}{1-u}\right) = \frac{1}{(1-u)^2} = \sum_{n=0}^{\infty} (n+1) u^n
\end{aligned}
$$
Substitusi $u = x+1$ (sehingga $(1-u)^2 = (-x)^2 = x^2$):
$$\frac{1}{x^2} = \sum_{n=0}^{\infty} (n+1) (x+1)^n$$

### 3. Tips & Jebakan
> [!warning]
> **Hati-hati tanda minus pangkat genap/ganjil:** Saat ngerjain $(-1)^{-(n+2)}$, pastikan kamu memecahnya dengan benar seperti $(-1)^{-n} \cdot (-1)^{-2}$. Karena $(-1)^{-2} = \frac{1}{(-1)^2} = 1$, maka tanda negatif di bagian ini hilang. Banyak mahasiswa sering salah tanda di sini karena kurang teliti dengan aljabar perpangkatan negatif.

---

## Soal 21: Deret Maclaurin dari $f(x) = \sin(x^2)$

**Tentukan deret Maclaurin dari fungsi:**
$$f(x) = \sin(x^2)$$

### 1. Intuisi & Analisis Kasus
Deret Maclaurin sebenarnya adalah kasus khusus dari deret Taylor yang titik pusatnya ada di $x = 0$ ($a = 0$). 
Kalau kita mau ngerjain soal ini pakai turunan langsung satu per satu, beuh, bakal repot banget lho! Kenapa? Karena kita harus pakai aturan perkalian (product rule) yang makin lama makin panjang saat menurunkan $\sin(x^2)$ berulang kali.
Untungnya, ada jalan pintas yang super elegan! Kita tahu deret Maclaurin dari fungsi dasar $\sin(u)$. Karena deret $\sin(u)$ konvergen untuk seluruh bilangan real $u$, kita tinggal ganti (substitusi) aja variabel $u$ dengan $x^2$. Cepat, bersih, dan bebas dari resiko salah hitung turunan!

### 2. Solusi Matematis Formal
Gunakan deret Maclaurin standar untuk $\sin(u)$ dan substitusi $u = x^2$:
$$
\begin{aligned}
\sin(u) &= \sum_{n=0}^{\infty} (-1)^n \frac{u^{2n+1}}{(2n+1)!} \\
\implies \sin(x^2) &= \sum_{n=0}^{\infty} (-1)^n \frac{(x^2)^{2n+1}}{(2n+1)!} = \sum_{n=0}^{\infty} (-1)^n \frac{x^{4n+2}}{(2n+1)!} \\
&= x^2 - \frac{x^6}{3!} + \frac{x^{10}}{5!} - \frac{x^{14}}{7!} + \dots
\end{aligned}
$$

### 3. Tips & Jebakan
> [!tip]
> **Gunakan Substitusi Lebih Cepat:** Jangan memaksakan diri menurunkan fungsi yang rumit secara langsung di lembar jawaban ujian jika fungsi tersebut merupakan komposisi dari fungsi dasar yang deretnya sudah kita ketahui (seperti $\sin(x)$, $\cos(x)$, $e^x$, atau $\ln(1+x)$). Teknik substitusi variabel seperti di atas sangat legal dan diakui secara akademis!
