---
type: generated_reading
subject: Mathematics
status: done
date_added: 2026-08-06
---

# Panduan Lengkap Chinese Remainder Theorem (CRT) & Reverse CRT

Chinese Remainder Theorem (CRT) dan Reverse CRT (RCRT) adalah konsep aljabar modular yang memungkinkan kita berpindah antara representasi satu bilangan utuh tunggal dan himpunan sisa bagi (residue) terhadap beberapa modulus yang saling [[Coprime]]. Teorema kuno ini memecahkan masalah rekonstruksi angka rahasia dari pecahan sisa baginya secara eksak dan *lossless*, sekaligus menjadi fondasi penting dalam kriptografi modern, komputasi paralel hardware (*Residue Number System*), serta skema pemecahan data rahasia (*Secret Sharing Scheme*).

---

## 1. Intuisi Dasar & Asal-usul CRT

Bayangkan kamu punya sekantong permen, tapi kamu lupa berapa jumlah pastinya. Saat permen itu kamu bagi ke kelompok 3 orang, sisa 1 permen. Pas kamu bagi ke kelompok 5 orang, sisa 4 permen. Dan pas dibagi ke kelompok 7 orang, sisa 5 permen. 

Pertanyaannya: **Berapa jumlah permen paling sedikit yang ada di kantongmu?**

Masalah ini pertama kali ditulis oleh matematikawan Tiongkok bernama Sunzi (Sun Tzu) pada abad ke-3 Masehi. CRT hadir untuk menjawab teka-teki seperti ini tanpa perlu kita menebak-nebak angka secara eksplisit dari 1 sampai ratusan.

Secara matematis, masalah di atas dituliskan dalam bentuk sistem [[Kongruensi_Modular]]:
$$x \equiv 1 \pmod 3$$
$$x \equiv 4 \pmod 5$$
$$x \equiv 5 \pmod 7$$

CRT menjamin bahwa selama pembaginya (yaitu 3, 5, dan 7) bersifat **pairwise [[Coprime]]** (tidak punya faktor persekutuan selain 1), pasti ada **satu solusi unik** $x$ di bawah perkalian total seluruh pembagi tersebut ($M = 3 \times 5 \times 7 = 105$).

---

## 2. Syarat & Konsep Aljabar Pendukung

Sebelum melangkah ke formula, ada tiga konsep kunci yang perlu kita pegang:

1. **[[Kongruensi_Modular]]:** 
   Pernyataan $a \equiv r \pmod m$ artinya jika $a$ dibagi $m$, sisa baginya adalah $r$.
2. **Modulo [[Coprime]]:** 
   Himpunan modulus $\{P_1, P_2, \dots, P_n\}$ wajib saling prima satu sama lain ($\gcd(P_i, P_j) = 1$ untuk $i \neq j$). Syarat ini penting agar informasi sisa bagi dari tiap basis tidak tumpang tindih.
3. **[[Invers_Modular]]:** 
   Invers modular dari $a \pmod m$ adalah angka $a^{-1}$ sedemikian hingga $(a \cdot a^{-1}) \equiv 1 \pmod m$. Angka ini bertindak sebagai "saklar pembuka" dalam memulihkan data asli.

---

## 3. Reverse CRT (RCRT): Memecah Angka Jadi Pecahan (Dekomposisi)

Banyak orang terkecoh antara CRT dan Reverse CRT. Biar gampang, kita bedakan arah jalannya:

- **Reverse CRT (RCRT) / Modulo Reduction:** 
  Proses **pemecahan** atau dekomposisi dari satu angka rahasia $I$ menjadi tuple pecahan sisa bagi $(r_1, r_2, \dots, r_n)$.
  $$r_i = I \bmod P_i \quad \text{untuk } i = 1, 2, \dots, n$$

Arah ini dinamakan *Reverse* dalam konteks rekonstruksi data/kriptografi karena kita mengambil data utuh lalu "memotong-motongnya" menjadi sisa-sisa kecil. 

Dalam pemetaan aljabar:
$$I \pmod M \xrightarrow{\text{Reverse CRT}} (r_1 \bmod P_1, r_2 \bmod P_2, \dots, r_n \bmod P_n)$$

---

## 4. Rekonstruksi CRT: Menyatukan Kembali Pecahan

Setelah angka dipotong menjadi pecahan $(r_1, r_2, \dots, r_n)$, **Reconstruction CRT** bertugas menggabungkannya kembali menjadi nilai utuh $I$.

Formula umum rekonstruksi CRT adalah:
$$I = \left( \sum_{i=1}^{n} r_i \cdot m_i \cdot m_i^{-1} \right) \bmod M$$

Di mana komponen-komponennya didefinisikan sebagai:
- **Modulus Total ($M$):** Perkalian seluruh basis, $M = \prod_{i=1}^n P_i$.
- **Sub-Modulus ($m_i$):** Perkalian seluruh basis *kecuali* basis ke-$i$, yaitu $m_i = \frac{M}{P_i}$.
- **Invers Modular ($m_i^{-1}$):** Nilai invers dari sub-modulus terhadap basisnya sendiri, yaitu $(m_i \cdot m_i^{-1}) \equiv 1 \pmod{P_i}$.

### Kenapa Formulanya Bekerja? (Trik Pembobot Saklar)
Perhatikan suku $r_i \cdot m_i \cdot m_i^{-1}$:
1. Jika dihitung terhadap $\pmod{P_i}$: Karena $m_i \cdot m_i^{-1} \equiv 1 \pmod{P_i}$, maka suku ini bernilai $r_i \cdot 1 = r_i$.
2. Jika dihitung terhadap $\pmod{P_j}$ (di mana $j \neq i$): Karena $m_i$ mengandung faktor $P_j$, maka $m_i \bmod P_j = 0$, sehingga suku ini otomatis bernilai $0$!

Artinya, setiap suku bertindak seperti "saklar pintar" yang hanya menyala pada posisi modulnya sendiri dan mati (jadi 0) pada posisi modul lainnya.

---

## 5. Walkthrough Perhitungan Nyata (Step-by-Step)

Mari kita selesaikan kasus permen Sunzi tadi dari awal sampai akhir!

- **Angka Rahasia Asli ($I$):** 19
- **Basis Modulus ($P$):** $P_1 = 3, P_2 = 5, P_3 = 7$
- **Modulus Total ($M$):** $M = 3 \times 5 \times 7 = 105$

### Tahap A: Reverse CRT (Dekomposisi)
Pecah $I = 19$ ke dalam tiap basis:
- $r_1 = 19 \bmod 3 = 1$
- $r_2 = 19 \bmod 5 = 4$
- $r_3 = 19 \bmod 7 = 5$

Kita dapatkan pecahan rahasia (*shares*): **$(1, 4, 5)$**.

### Tahap B: Rekonstruksi CRT

**Langkah 1: Hitung Sub-Modulus ($m_i = M / P_i$)**
- $m_1 = 105 / 3 = 35$
- $m_2 = 105 / 5 = 21$
- $m_3 = 105 / 7 = 15$

**Langkah 2: Cari Invers Modular ($y_i = m_i^{-1} \pmod{P_i}$)**
- Untuk $m_1 = 35 \pmod 3$: $35 \bmod 3 = 2$. Cari $y_1$ sedemikian hingga $2 \cdot y_1 \equiv 1 \pmod 3 \implies y_1 = 2$.
- Untuk $m_2 = 21 \pmod 5$: $21 \bmod 5 = 1$. Cari $y_2$ sedemikian hingga $1 \cdot y_2 \equiv 1 \pmod 5 \implies y_2 = 1$.
- Untuk $m_3 = 15 \pmod 7$: $15 \bmod 7 = 1$. Cari $y_3$ sedemikian hingga $1 \cdot y_3 \equiv 1 \pmod 7 \implies y_3 = 1$.

**Langkah 3: Hitung Nilai Akhir $I$**
$$I = (r_1 \cdot m_1 \cdot y_1 + r_2 \cdot m_2 \cdot y_2 + r_3 \cdot m_3 \cdot y_3) \bmod M$$
$$I = (1 \cdot 35 \cdot 2 + 4 \cdot 21 \cdot 1 + 5 \cdot 15 \cdot 1) \bmod 105$$
$$I = (70 + 84 + 75) \bmod 105$$
$$I = 229 \bmod 105 = 19$$

Hasilnya **100% presisi kembali ke 19**!

---

## 6. Aplikasi di Dunia Nyata

CRT dan Reverse CRT bukan sekadar teori matematika abstrak. Keduanya dipakai luas dalam komputasi modern:

1. **Secret Sharing Scheme (Asmuth-Bloom & Mignotte):**
   Memecah file atau matriks piksel gambar rahasia menjadi komponen sisa bagi. Tanpa jumlah *shares* minimum yang cukup, data rahasia tidak bisa direkonstruksi.
2. **Residue Number System (RNS) di Hardware Processor:**
   Dalam komputasi prosesor berkecepatan tinggi, menambahkan atau mengalikan angka ribuan bit sangatlah lambat. Dengan RCRT, angka rahasia besar dipecah jadi angka-angka kecil $r_i$, dihitung secara paralel di unit hardware independen, lalu di-rekonstruksi dengan CRT di akhir.
3. **Akselerasi Dekripsi RSA:**
   Pada kriptografi RSA, proses dekripsi $c^d \bmod N$ sangat berat jika $N$ berukuran 4096-bit. Dengan CRT, kalkulasi dibagi dua menjadi modulo $p$ dan modulo $q$ (di mana $N = p \cdot q$), yang membuat proses dekripsi hingga 4x lebih cepat.

---

## 7. Kesimpulan & Konsep Terkait

Reverse CRT adalah cara memecah data tunggal menjadi potongan sisa bagi terhadap basis-basis coprime, sedangkan CRT Reconstruction adalah cara ajaib menyatukan kembali potongan-potongan tersebut tanpa kehilangan sedikit pun data (*lossless*).

**Konsep Terkait di Vault:**
- [[Chinese_Remainder_Theorem]]
- [[Reverse_CRT]]
- [[Coprime]]
- [[Kongruensi_Modular]]
- [[Invers_Modular]]
- [[Single_Secret_Sharing_CRT_Shamir_XOR]]
