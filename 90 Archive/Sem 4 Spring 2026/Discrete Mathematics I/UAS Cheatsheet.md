---
title: Cheatsheet UAS Matematika Diskrit 1
course: Matematika Diskrit 1
tags: ["discrete-mathematics", "cheatsheet", "exam-prep"]
aliases: ["UAS Diskrit 1", "Cheatsheet Diskrit"]
created: "2026-06-22"
---

# Cheatsheet UAS Matematika Diskrit 1

> [!important]
> **Identitas Mahasiswa**
> Nama: [Isi Nama Kamu]
> NIM: [Isi NIM Kamu]
> *Ketentuan: Maksimal 1 halaman A4 bolak-balik, boleh bawa kalkulator.*

---

## 1. Fungsi Pembangkit (Generating Functions)

Fungsi pembangkit biasa (ordinary generating function) dari barisan $(a_0, a_1, a_2, \dots)$ adalah deret formal:
$$G(x) = \sum_{n=0}^{\infty} a_n x^n = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \dots$$

### Deret Dasar & Identitas Penting
*   **Barisan Konstan $(1, 1, 1, \dots)$:** $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$
*   **Barisan Geometris $(1, a, a^2, a^3, \dots)$:** $\frac{1}{1-ax} = \sum_{n=0}^{\infty} a^n x^n$
*   **Barisan Linear $a_n = n$:** $\frac{x}{(1-x)^2} = \sum_{n=0}^{\infty} n x^n$
*   **Barisan Kuadrat $a_n = n^2$:** $\frac{x(1+x)}{(1-x)^3} = \sum_{n=0}^{\infty} n^2 x^n$
*   **Teorema Binomial Negatif:** $\frac{1}{(1-x)^k} = \sum_{n=0}^{\infty} \binom{n+k-1}{k-1} x^n$
*   **Fungsi Eksponensial (untuk barisan $a_n = \frac{1}{n!}$):** $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$

---

## 2. Relasi Rekurensi (Recurrence Relations)

### A. Homogen Linier dengan Polinomial Karakteristik
Bentuk umum: $a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k}$. 
Persamaan karakteristik: $r^k - c_1 r^{k-1} - c_2 r^{k-2} - \dots - c_k = 0$.
*   **Kasus 1: Akar berbeda ($r_i$ distinct):** $a_n = \alpha_1 r_1^n + \alpha_2 r_2^n + \dots + \alpha_k r_k^n$
*   **Kasus 2: Akar kembar (multiplisitas $m$):** Bagian solusinya menjadi: $(\alpha_1 + \alpha_2 n + \alpha_3 n^2 + \dots + \alpha_m n^{m-1}) r_1^n$

### B. Non-Homogen Linier
Bentuk umum: $a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k} + F(n)$. 
Solusi total: $a_n = a_n^{(h)} + a_n^{(p)}$ (Solusi Homogen + Solusi Partikular).

> [!tip]
> ### Cookbook: Tebakan Solusi Partikular $a_n^{(p)}$
> Gunakan tabel di bawah ini untuk menentukan bentuk tebakan $a_n^{(p)}$ berdasarkan fungsi non-homogen $F(n)$:
> 
> | Bentuk $F(n)$ | Kondisi Basis $s$ pada Persamaan Karakteristik | Bentuk Tebakan Solusi Partikular $a_n^{(p)}$ |
> | :--- | :--- | :--- |
> | $c \cdot s^n$ | $s$ **bukan** akar karakteristik | $A \cdot s^n$ |
> | $c \cdot s^n$ | $s$ **adalah** akar karakteristik dengan kelipatan $m$ | $n^m \cdot A \cdot s^n$ |
> | $P_d(n) = b_d n^d + \dots + b_0$ | $1$ **bukan** akar karakteristik | $A_d n^d + \dots + A_0$ |
> | $P_d(n) = b_d n^d + \dots + b_0$ | $1$ **adalah** akar karakteristik dengan kelipatan $m$ | $n^m (A_d n^d + \dots + A_0)$ |
> | $P_d(n) \cdot s^n$ | $s$ **bukan** akar karakteristik | $(A_d n^d + \dots + A_0) s^n$ |
> | $P_d(n) \cdot s^n$ | $s$ **adalah** akar karakteristik dengan kelipatan $m$ | $n^m (A_d n^d + \dots + A_0) s^n$ |

---

## 3. Prinsip Inklusi-Eksklusi (PIE)

### Rumus Umum Gabungan
*   **3 Himpunan:** $|A \cup B \cup C| = \sum |A_i| - \sum |A_i \cap A_j| + |A \cap B \cap C|$
*   **4 Himpunan:** $|A \cup B \cup C \cup D| = \sum |A_i| - \sum |A_i \cap A_j| + \sum |A_i \cap A_j \cap A_k| - |A \cap B \cap C \cap D|$

> [!important]
> ### Cookbook: Jumlah Solusi Persamaan dengan Batas Atas
> Untuk mencari banyaknya solusi bilangan bulat dari $x_1 + x_2 + \dots + x_k = N$ dengan syarat $0 \le x_i \le c_i$:
> 
> 1. **Cari Ukuran Semesta ($|S|$):** Jumlah cara membagikan tanpa batas atas:
>    $$|S| = \binom{N + k - 1}{k - 1}$$
> 2. **Definisikan Sifat Pelanggaran ($P_i$):** Kondisi di mana variabel melanggar batas atas, yaitu $x_i \ge c_i + 1$.
> 3. **Hitung Jumlah Cara Melanggar ($|P_i|$ dan Irisannya):**
>    * Untuk menghitung $|P_i|$, lakukan substitusi $y_i = x_i - (c_i + 1) \ge 0$. Persamaan menjadi $y_i + \sum_{j \neq i} x_j = N - (c_i + 1)$. Cari solusinya:
>      $$|P_i| = \binom{N - (c_i + 1) + k - 1}{k - 1}$$
>    * Untuk irisan sifat (misalnya $|P_i \cap P_j|$), kurangkan ruas kanan dengan semua batas pelanggaran yang aktif:
>      $$\text{Sisa Objek} = N - \sum_{\text{aktif}} (c_x + 1)$$
>      Jika Sisa Objek $< 0$, maka jumlah cara melanggar untuk irisan tersebut adalah $0$.
> 4. **Gunakan PIE untuk Mencari Solusi Valid:**
>    $$N(\text{valid}) = |S| - \sum |P_i| + \sum |P_i \cap P_j| - \sum |P_i \cap P_j \cap P_k| + \dots$$

---

## 4. Verifikasi Sifat Relasi (Relations Checklist)

Relasi biner $R$ pada himpunan $A$ dapat diuji sifat-sifatnya secara cepat menggunakan representasi Matriks ($M_R$) atau Graf Berarah (Digraph) lewat tabel checklist berikut:

| Sifat Relasi | Definisi Formal | Verifikasi pada Matriks $M_R$ | Verifikasi pada Digraph |
| :--- | :--- | :--- | :--- |
| **Refleksif** | $\forall a \in A, (a,a) \in R$ | Elemen diagonal utama semuanya bernilai $1$. | Setiap simpul (node) wajib memiliki *self-loop*. |
| **Simetris** | $aRb \implies bRa$ | Matriks bersifat simetris terhadap diagonal utama ($M_R = M_R^T$). | Jika ada panah dari $a$ ke $b$, wajib ada panah balik dari $b$ ke $a$. |
| **Antisimetris** | $(aRb \land bRa) \implies a=b$ | Untuk elemen di luar diagonal ($i \neq j$), jika $M_R[i,j]=1$ maka $M_R[j,i]$ wajib $0$. | Tidak boleh ada panah bolak-balik antara dua simpul berbeda. |
| **Transitif** | $(aRb \land bRc) \implies aRc$ | Hitung $M_{R^2} = M_R \odot M_R$. Wajib berlaku $M_{R^2} \le M_R$ (jika $M_{R^2}[i,j]=1$ maka $M_R[i,j]=1$). | Jika ada rute 2 langkah dari $a \to b \to c$, wajib ada panah langsung dari $a \to c$. |

### A. Operasi Relasi & Representasi
*   **Komposisi Relasi ($R^2 = R \circ R$):** Direpresentasikan dengan perkalian boolean matriks $M_{R^2} = M_R \odot M_R$.
    $$(M_R \odot M_R)[i, j] = \bigvee_{k=1}^{n} (M_R[i, k] \land M_R[k, j])$$
*   **Proyeksi Database ($P_{i_1, i_2, \dots, i_m}$):** Mengambil kolom-kolom tertentu dari relasi n-ary dan **menghilangkan duplikasi baris** yang dihasilkan.
    $$\text{Catatan: } P(R \cap S) \neq P(R) \cap P(S) \text{ secara umum (cukup } P(R \cap S) \subseteq P(R) \cap P(S)\text{)}.$$

---

## 5. Partial Orderings (Poset) & Chains

Relasi $R$ pada himpunan $S$ disebut **Partial Ordering** (Urutan Parsial) jika $R$ bersifat **Refleksif, Antisimetris, dan Transitif**. Himpunan $S$ bersama relasi $R$ disebut **Poset** $(S, R)$.

*   **Comparable:** Dua elemen $a$ dan $b$ dalam poset disebut comparable jika $aRb$ atau $bRa$. Jika tidak keduanya, maka disebut **Incomparable**.
*   **Chain (Rantai):** Subhimpunan dari poset di mana **setiap dua elemen di dalamnya saling comparable** (merupakan total ordering lokal).
*   **Antichain:** Subhimpunan dari poset di mana **setiap dua elemen berbeda di dalamnya saling incomparable**.

> [!example]
> ### Contoh Poset Pembagian (Divisibility)
> Misalkan Himpunan $S = \{1, 2, 3, 4, 6, 12\}$ dengan relasi pembagian $\mid$ (di mana $a \mid b$ berarti $a$ membagi habis $b$).
> *   **Poset:** $(S, \mid)$ adalah poset karena bersifat refleksif ($a \mid a$), antisimetris ($a \mid b \land b \mid a \implies a=b$), dan transitif ($a \mid b \land b \mid c \implies a \mid c$).
> *   **Comparable:** $2$ dan $6$ comparable ($2 \mid 6$). Sedangkan $2$ dan $3$ **incomparable** ($2 \nmid 3$ dan $3 \nmid 2$).
> *   **Chain (Rantai):** $C = \{1, 2, 4, 12\}$ adalah chain karena semua elemen saling membagi ($1 \mid 2 \mid 4 \mid 12$).
> *   **Antichain:** $A = \{4, 6\}$ adalah antichain karena $4 \nmid 6$ dan $6 \nmid 4$ (keduanya incomparable).
