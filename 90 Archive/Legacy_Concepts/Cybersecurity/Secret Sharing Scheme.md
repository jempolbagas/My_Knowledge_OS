---
type: concept
subject: Cybersecurity
source_hash: "66e12d9252a0cc3e9ac35ebb4ee78657"
source: "[[Single Secret Sharing CRT Shamir XOR]]"
created: 2026-08-05
---

# Secret Sharing Scheme (SSS)

**Secret Sharing Scheme (SSS)** adalah metode kriptografi untuk membagi sebuah rahasia $I$ menjadi beberapa bagian terkode (*shares*) yang didistribusikan kepada beberapa partisipan. 

## Karakteristik Utama
- **Keamanan Terdistribusi:** Tidak ada satu partisipan pun yang memegang rahasia secara utuh. Satu lembar *share* secara terpisah tidak mengungkapkan informasi rahasia (*perfect security*).
- **Rekonstruksi Presisi:** Rahasia hanya dapat dipulihkan ketika jumlah *share* yang memenuhi syarat (*access structure* atau *threshold*) digabungkan menggunakan algoritma tertentu (seperti polinomial, matriks, atau aritmatika modulo).

## Klasifikasi SSS
1. **Single Secret Sharing:** Mendistribusikan satu data rahasia tunggal ke dalam $n$ share.
2. **Multi Secret Sharing:** Mendistribusikan beberapa data rahasia sekaligus ke dalam himpunan share.
3. **Threshold Scheme $(t, n)$:** Cukup $t$ dari $n$ share yang dibutuhkan untuk memulihkan rahasia ($t \le n$).
