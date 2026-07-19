---
title: Tugas_UAS_Matematika_Diskrit_1
course: Discrete Mathematics
tags: []
aliases: ["Tugas_UAS_Matematika_Diskrit_1"]
created: "2026-06-21"
---
# Tugas UAS Matematika Diskrit 1

**Dikumpulkan:** Jumat, 26 Juni 2026

### Ketentuan Pelaksanaan UAS:
1. Mahasiswa diperbolehkan membawa *cheatsheet* yang hanya berupa 1 halaman A4.
2. Pada lembar *cheatsheet* harus diberi nama dan NIM masing-masing.
3. Mahasiswa diperbolehkan membawa kalkulator.

---

### SOAL

1. **Tentukan *generating functions* dari barisan berikut:**
   - a. $(2, 2, 2, 2, 2, \dots)$
   - b. $(0, 0, \dots)$
   - c. $a_n = n + 2$
   - d. $(2, -1, 5, 7, 17, \dots)$

2. **Tentukan solusi eksplisit dari *recurrence relation* berikut dengan menggunakan polinomial karakteristik:**
   - a. $a_n = 6a_{n-1} - 9a_{n-2}$ dengan $a_0 = 1$ dan $a_1 = 6$
   - b. $a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3}$ dengan $a_0 = 2$, $a_1 = 5$, dan $a_2 = 15$
   - c. $a_n = -3a_{n-1} - 3a_{n-2} - a_{n-3}$ dengan $a_0 = 1$, $a_1 = -2$, dan $a_2 = -1$

3. **Tentukan solusi eksplisit dari *recurrence relation* berikut:**
   - a. $a_n = 8a_{n-1} + 10^{n-1}$ dengan $a_0 = 1$ dan $a_1 = 9$
   - b. $a_n = 3a_{n-1} - 2a_{n-2} + C_1^n$ dengan $a_0 = 0$ dan $a_1 = 1$
   - c. $a_n = 4a_{n-1} - 4a_{n-2} + 2^n$ dengan $a_0 = 0$ dan $a_1 = 1$

4. Dalam sebuah program studi Informatika, terdapat 175 mahasiswa mengambil mata kuliah *Data Mining*, dan 225 mahasiswa mengambil mata kuliah Metode Numerik. Jika terdapat 50 mahasiswa yang mengambil kedua mata kuliah, maka berapakah jumlah mahasiswa pada program studi Informatika? Ilustrasikan dengan menggunakan diagram venn!

5. Tentukan berapa banyak bilangan bulat positif yang tidak lebih dari 1000 yang habis dibagi oleh 5, 7, atau 11!

6. Berikan formula (rumus) untuk menentukan banyaknya anggota dari gabungan empat buah himpunan!

7. Dengan menggunakan prinsip *inclusion-exclusion*, berapa banyak solusi dari $x_1 + x_2 + x_3 = 11$, ketika $x_1$, $x_2$, dan $x_3$ merupakan bilangan bulat non-negatif dengan $x_1 \le 3$, $x_2 \le 4$, dan $x_3 \le 6$?

8. Berapa banyak bilangan bulat positif kurang dari 10.000 yang bukan merupakan pangkat dua atau lebih tinggi dari suatu bilangan bulat?

9. **Tentukan apakah relasi $R$ pada himpunan bilangan bulat bersifat refleksif, simetris, antisimetris, dan/atau transitif, ketika $(x,y) \in R$ jika dan hanya jika:**
   - a. $x \neq y$
   - b. $x = y^2$

10. **Perhatikan relasi berikut pada himpunan bilangan real:**
    - $R_1 = \{(a,b) \in \mathbb{R}^2 \mid a > b\}$
    - $R_2 = \{(a,b) \in \mathbb{R}^2 \mid a \ge b\}$
    - $R_3 = \{(a,b) \in \mathbb{R}^2 \mid a < b\}$
    - $R_4 = \{(a,b) \in \mathbb{R}^2 \mid a \le b\}$
    
    **Tentukan:**
    - a. $R_1 \cup R_3$
    - b. $R_2 \oplus R_4$
    - c. $R_2 \circ R_4$

11. **Tentukan tabel yang diperoleh jika *projection* $P_{1,2}$ diterapkan pada relasi pada tabel berikut:**

| Student | Major | Course |
| --- | --- | --- |
| Joko | Biology | BA 290 |
| Joko | Biology | MD 451 |
| Markus | Physics | PY 182 |
| Markus | Physics | CT 212 |
| Shiren | Computer Science | BG 215 |
| Shiren | Computer Science | CS 812 |
| Steve | Mathematics | MD 712 |


12. Berikan contoh untuk menunjukkan bahwa jika $R$ dan $S$ keduanya merupakan relasi $n$-ary, maka $P_{i_1, i_2, \dots, i_m}(R \cap S)$ mungkin berbeda dari $P_{i_1, i_2, \dots, i_m}(R) \cap P_{i_1, i_2, \dots, i_m}(S)$!

13. Tentukan matriks yang merepresentasikan relasi $R^2$ jika $R$ memiliki representasi matriks ($M_R$) sebagai berikut:
    $$M_R = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 0 \end{bmatrix}$$

14. **Sebutkan daftar *ordered pairs* pada relasi yang direpresentasikan pada *directed graph* berikut:**
    - a. *(Graf berarah dengan simpul a, b, c, d)* 
    - b. *(Graf berarah dengan simpul a, b, c, d)*

15. Diberikan himpunan bilangan asli $\mathbb{N}$, dengan relasi biner $R$ yang didefinisikan sebagai berikut:
    $(\forall a, b \in \mathbb{N}) \, aRb \text{ jika dan hanya jika } a \mid b$
    Apakah $R$ merupakan relasi *partial orderings* pada $\mathbb{N}$? Berikan penjelasannya!

16. Diketahui himpunan $A = \{a, b, c, d\}$ dengan definisi relasi *partial orderings* pada $A$ sebagai berikut:  
    $R = \{(a, a), (a, b), (a, c), (a, d), (b, b), (b, d), (c, c), (c, d), (d, d)\}$  
    Tentukan 3 buah himpunan yang merupakan *chain*!
