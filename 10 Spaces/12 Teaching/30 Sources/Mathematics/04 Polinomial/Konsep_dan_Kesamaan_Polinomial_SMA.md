---
title: "Konsep Dasar dan Kesamaan Polinomial"
type: materi
subject: Mathematics
level: sma
target_audience: "SMA Kelas 11"
created: 2026-08-20
sources:
  - "[[Suku Banyak Polinomial SMA]]"
tags:
  - teaching-material
  - mathematics
  - suku-banyak
  - polinomial
  - kesamaan-polinomial
---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | Modul Ini | [[Metode_Horner_dan_Operasi_SMA|Metode Horner ➡️]] | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]

# Konsep Dasar dan Kesamaan Polinomial — Berkenalan dengan Suku Banyak! 🚀

Halo teman-teman! Saat mendengar kata **Polinomial** atau **Suku Banyak**, mungkin pikiranmu langsung terbayang rumus-rumus panjang dengan pangkat tinggi. Tapi tenang saja! Di modul ini, kita akan bedah materi ini dari dasar.

---

## 1. Kenalan dengan Suku Banyak (Polinomial)

### Apa sih Suku Banyak itu?
Secara bahasa, **Polinomial** berasal dari kata *Poly* (banyak) dan *Nomial* (suku/nama). 

> **Definisi:**  
> **Suku banyak (Polinomial)** adalah suatu bentuk aljabar yang terdiri dari penjumlahan atau pengurangan suku-suku dengan variabel berpangkat **bilangan bulat positif (tak-negatif)**.

Contoh sederhana dalam kehidupan sehari-hari: ketika kamu merancang volume kotak kardus kemasan, menghitung keuntungan variabel bisnis, atau memodelkan lintasan kurva, kamu sedang menggunakan konsep polinomial!

---

## 2. Anatomi & Bentuk Umum Polinomial

Bentuk umum dari suatu polinomial derajat $n$ dengan satu variabel $x$ dituliskan sebagai berikut:

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + a_{n-2} x^{n-2} + \dots + a_1 x + a_0$$

Mari kita bedah komponen-komponennya:
* **Variabel ($x$):** Simbol atau lambang yang nilainya bisa berubah-ubah.
* **Derajat ($n$):** Pangkat **tertinggi** dari variabel $x$. Syaratnya $n \in \{0, 1, 2, 3, \dots\}$ (bilangan cacah/bulat tak-negatif).
* **Suku Utama ($a_n x^n$):** Suku yang memuat variabel berpangkat tertinggi.
* **Koefisien Utama ($a_n$):** Angka di depan variabel berpangkat tertinggi ($a_n \neq 0$).
* **Koefisien-koefisien ($a_{n-1}, a_{n-2}, \dots, a_1$):** Angka-angka yang menempel di depan variabel $x$.
* **Suku Tetap / Konstanta ($a_0$):** Suku berpangkat nol ($x^0 = 1$), yaitu angka jomblo tanpa variabel $x$.

> **Contoh Cepat:**  
> Diketahui polinomial: $P(x) = 5x^4 - 3x^3 + 2x - 7$
> * **Derajat polinomial:** $4$ (karena pangkat tertinggi $x$ adalah 4).
> * **Koefisien Utama:** $5$
> * **Koefisien $x^3$:** $-3$
> * **Koefisien $x^2$:** $0$ *(suku $x^2$ tidak ditulis, artinya koefisiennya 0!)*
> * **Koefisien $x$:** $2$
> * **Suku Tetap (Konstanta):** $-7$

---

## 3. Aturan & Syarat Bentuk Polinomial

Tidak semua bentuk aljabar disebut polinomial! Ada syarat tegas yang harus dipenuhi:

| Syarat Polinomial | Contoh Polinomial (Boleh ✅) | Contoh Bukan Polinomial (Tidak Boleh ❌) | Alasan |
| :--- | :--- | :--- | :--- |
| **1. Pangkat berupa bilangan bulat $\ge 0$** | $x^3 + 2x^2 - 5$ | $x^{\frac{1}{2}} + 3x$ atau $\sqrt{x} + 2$ | Pangkat berupa pecahan ($\frac{1}{2}$). |
| **2. Variabel tidak berada di penyebut** | $\frac{1}{4}x^2 + 5x$ | $\frac{3}{x} + x^2$ | $\frac{3}{x} = 3x^{-1}$ (pangkat negatif). |
| **3. Jumlah suku terbatas** | $x^5 - 2x^3 + 1$ | $1 + x + x^2 + x^3 + \dots$ | Jumlah suku tak terbatas (deret). |
| **4. Bebas fungsi trigonometri/logaritma** | $x^2 \sin(30^\circ) + 4$ | $\sin(x) + x^2$ | Variabel $x$ berada di dalam fungsi trigonometri. |

---

## 4. Kesamaan Polinomial (Identitas) ⚖️

Pernahkah kamu melihat lambang tiga garis horizontal "$\equiv$"? Itu disebut lambang **Kesamaan** atau **Identitas**.

> Dua buah polinomial $f(x)$ dan $g(x)$ dikatakan **sama / identik** (ditulis $f(x) \equiv g(x)$) jika dan hanya jika keduanya memiliki **derajat yang sama** dan **koefisien dari variabel berpangkat sejenis adalah sama**.

Artinya, ruas kiri dan ruas kanan itu sebenarnya benda yang persis sama, hanya bentuk penampilannya yang berbeda!

### Aturan Kesamaan
Jika:
$$ax^3 + bx^2 + cx + d \equiv px^3 + qx^2 + rx + s$$
Maka berlaku:
* $a = p$
* $b = q$
* $c = r$
* $d = s$

### 📝 Contoh Soal Kesamaan: Pecahan Parsial

Kesamaan polinomial sangat sering digunakan dalam pemecahan pecahan (pecahan parsial) yang sering keluar di soal-soal HOTS.

**Soal:**  
Tentukan nilai $A$ dan $B$ agar kesamaan berikut bernilai benar:
$$\frac{7x - 1}{x^2 - x - 6} \equiv \frac{A}{x - 3} + \frac{B}{x + 2}$$

**Penyelesaian:**
1. Samakan penyebut di ruas kanan agar wujudnya sama dengan penyebut di ruas kiri:
   $$\frac{7x - 1}{(x - 3)(x + 2)} \equiv \frac{A(x + 2) + B(x - 3)}{(x - 3)(x + 2)}$$
2. Karena penyebutnya sudah sama, maka pembilangnya pasti identik!
   $$7x - 1 \equiv A(x + 2) + B(x - 3)$$
3. **Trik Substitusi Pembuat Nol:** Untuk mencari nilai $A$ dan $B$, substitusikan nilai $x$ yang membuat salah satu faktor menjadi nol.
   * Supaya $B$ hilang, masukkan $x = 3$:
     $$7(3) - 1 = A(3 + 2) + B(3 - 3)$$
     $$21 - 1 = 5A \implies 20 = 5A \implies \mathbf{A = 4}$$
   * Supaya $A$ hilang, masukkan $x = -2$:
     $$7(-2) - 1 = A(-2 + 2) + B(-2 - 3)$$
     $$-14 - 1 = -5B \implies -15 = -5B \implies \mathbf{B = 3}$$

Jadi, nilai $A = 4$ dan $B = 3$. Keren kan triknya?

---

[[Suku Banyak Polinomial SMA|🏠 Master Dashboard]] | Modul Ini | [[Metode_Horner_dan_Operasi_SMA|Metode Horner ➡️]] | [[LKPD Suku Banyak Polinomial SMA|📝 LKPD Suku Banyak]]
