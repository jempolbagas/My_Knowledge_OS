---
title: "LKPD & Soal Evaluasi: Kaidah Pencacahan & Kombinatorika"
level: sma
target_audience: "SMA Kelas 12"
created: 2026-08-09
sources:
  - "[[Kaidah Pencacahan dan Kombinatorika SMA]]"
tags:
  - practice-material
  - mathematics
  - lkpd
  - pencacahan
  - permutasi
  - kombinasi
  - binomial-newton
---

# Lembar Kerja Peserta Didik (LKPD) & Soal Evaluasi: Kaidah Pencacahan & Kombinatorika 🎯

**Mata Pelajaran:** Matematika (Wajib)  
**Kelas / Semester:** XII / Ganjil  
**Materi Pokok:** Kaidah Pencacahan (Filling Slots), Permutasi, Kombinasi, & Binomial Newton HOTS  
**Alokasi Waktu:** $2 \times 45\text{ Menit}$ (Pertemuan Praktik & Evaluasi)

---

## Bagian 1: Lembar Kerja Peserta Didik (LKPD)

### 📌 Petunjuk Umum:
1. Bentuk kelompok diskusi yang terdiri dari 4–5 orang siswa.
2. Selesaikan setiap aktivitas eksplorasi berikut dengan cermat dan berkolaborasi.
3. Diskusikan hasil temuan kelompokmu sebelum mempresentasikannya di depan kelas.

---

### Aktivitas 1: Eksplorasi Kaidah Pencacahan & Pembedaan Metode
Analisis skenario kasus di bawah ini dan tentukan metode pencacahan yang tepat!

#### Skenario Kasus:
1. **Kasus A (Plat Nomor Identitas):** Panitia mau membuat nomor identitas 3 digit dari angka $\{1, 2, 3, 4, 5, 6, 7\}$ yang nilainya **lebih besar dari 400** dan **tidak berulang**.
2. **Kasus B (Spanduk Pensi):** Menyusun huruf dari kata **"MATEMATIKA"**.
3. **Kasus C (Tim Utusan):** Memilih 3 siswa dari 7 calon pengurus untuk menjadi juru bicara tanpa jabatan khusus.

#### Tugas Diskusi Kelompok:
1. Pada **Kasus A**:
   - Berapa pilihan angka yang memenuhi syarat untuk posisi ratusan?
   - Mengapa posisi puluhan dan satuan berkurang satu demi satu?
   - Hitung total banyaknya nomor identitas yang dapat dibentuk!
2. Pada **Kasus B**:
   - Sebutkan huruf yang kembar beserta jumlahnya!
   - Hitung susunan kata berbeda yang dapat dibuat!
3. Pada **Kasus C**:
   - Apakah urutan pemanggilan mempengaruhi anggota tim yang terbentuk? (*Ya / Tidak*)
   - Gunakan permutasi atau kombinasi? Hitung hasilnya!

---

### Aktivitas 2: Matriks Komparasi Permutasi vs Kombinasi

Lengkapi matriks di bawah ini untuk mengklasifikasikan jenis rumus yang harus digunakan!

| No | Skenario Kasus | Tipe Masalah | Rumus Matematis |
| :---: | :--- | :---: | :---: |
| **1** | Memilih Ketua, Sekretaris, Bendahara dari 10 calon. | Permutasi $r$ dari $n$ | $_n P_r = \frac{n!}{(n-r)!}$ |
| **2** | Menyusun 6 orang duduk mengelilingi meja bundar. | Permutasi Siklis | $P_{\text{siklis}} = (n-1)!$ |
| **3** | Memilih 5 pemain inti basket dari 9 calon pemain. | Kombinasi | $_n C_r = \frac{n!}{(n-r)! r!}$ |
| **4** | Menyusun kata berbeda dari kata **"BASSABASSI"**. | Permutasi Unsur Sama | $P = \frac{n!}{k_1! k_2! \dots}$ |
| **5** | Mencari suku konstan (bebas dari $x$) pada $(x^2 + 2/x)^9$. | Binomial Newton HOTS | $\text{Pangkat } x = 0 \implies r = 6$ |

---

### Aktivitas 3: Studi Kasus HOTS — Formasi Tim E-Sports & Permutasi Siklis Berdampingan 🎮🎓

#### Deskripsi Kasus:
Sebuah klub e-sports sekolah beranggotakan **6 pemain Laki-laki** dan **4 pemain Perempuan**.
1. **Tantangan 1 (Formasi Tim Kombinasi):** Akan dipilih 4 orang pemain yang wajib terdiri dari **2 Laki-laki dan 2 Perempuan**. Ada berapa banyak pilihan tim yang mungkin terbentuk?
2. **Tantangan 2 (Permutasi Siklis Syarat Khusus):** Saat rapat strategi, 6 orang pemain duduk mengelilingi meja bundar. Jika **Kapten dan Wakil Kapten harus selalu duduk berdampingan**, hitung banyaknya susunan posisi duduk yang mungkin!

---

## Bagian 2: Latihan Soal Mandiri & Evaluasi

### A. Soal Pilihan Ganda (HOTS)

1. Banyak cara memilih pemain inti tim basket (5 orang) dari 9 calon pemain adalah...  
   A. $36$  
   B. $72$  
   C. $126$  
   D. $1.512$  
   E. $3.024$

2. Banyaknya kata/susunan huruf berbeda yang dapat dibentuk dari kata **"BASSABASSI"** adalah...  
   A. $1.260$  
   B. $2.520$  
   C. $6.300$  
   D. $12.600$  
   E. $25.200$

3. Dari angka-angka $\{1, 2, 3, 4, 5, 6, 7\}$ akan dibentuk bilangan 3 digit yang **nilainya lebih besar dari 400** dan **tanpa angka berulang**. Banyaknya bilangan yang terbentuk adalah...  
   A. $60$  
   B. $90$  
   C. $120$  
   D. $150$  
   E. $210$

4. Nilai dari suku bebas dari $x$ (suku konstan) pada penjabaran aljabar $\left(x^2 + \frac{2}{x}\right)^9$ adalah...  
   A. $672$  
   B. $1.344$  
   C. $2.688$  
   D. $5.376$  
   E. $10.752$

5. Enam orang anggota keluarga duduk mengelilingi meja makan bundar. Banyak susunan posisi duduk melingkar yang dapat dibuat adalah...  
   A. $24$  
   B. $120$  
   C. $360$  
   D. $720$  
   E. $5.040$

6. Banyaknya cara memilih 3 pengurus (Ketua, Sekretaris, Bendahara) dari 8 calon pengurus adalah...  
   A. $56$  
   B. $112$  
   C. $336$  
   D. $672$  
   E. $6.720$

7. Banyak susunan kata berbeda yang dapat dibentuk dari kata **"MATEMATIKA"** adalah...  
   A. $151.200$  
   B. $302.400$  
   C. $604.800$  
   D. $1.209.600$  
   E. $3.628.800$

8. Dari 10 orang calon anggota tim olimpiade, akan dikirim 4 orang sebagai delegasi sekolah. Banyak cara memilih delegasi tersebut adalah...  
   A. $120$  
   B. $210$  
   C. $252$  
   D. $420$  
   E. $5.040$

9. Sebuah PIN 4 digit akan dibuat dari angka $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$. Jika angka **boleh berulang**, banyaknya PIN yang dapat dibentuk adalah...  
   A. $5.040$  
   B. $7.290$  
   C. $9.000$  
   D. $10.000$  
   E. $65.610$

10. Nilai koefisien suku yang memuat $x^6$ pada penjabaran $(x + 2)^8$ adalah...  
    A. $28$  
    B. $56$  
    C. $112$  
    D. $224$  
    E. $448$

---

### B. Soal Uraian Penalaran (Problem Solving)

1. **(Filling Slots & Syarat Khusus)**  
   Dari 8 siswa berprestasi (5 laki-laki dan 3 perempuan), akan dipilih pengurus harian OSIS (Ketua, Sekretaris, Bendahara). Berapa banyak susunan pengurus yang dapat dibentuk jika jabatan **Ketua wajib diisi oleh siswa perempuan**?

2. **(Binomial Newton HOTS — Suku Bebas $x$)**  
   Tentukan nilai dari suku konstan (suku yang tidak memuat variabel $x$) dalam ekspansi aljabar $\left(2x^3 - \frac{1}{x^2}\right)^5$!

3. **(Permutasi Siklis Berdampingan)**  
   Ada 7 orang pengurus OSIS (termasuk Ketua dan Sekretaris) yang duduk mengelilingi meja bundar. Jika **Ketua dan Sekretaris harus selalu duduk berdampingan**, berapa banyak susunan posisi duduk yang mungkin terjadi?

4. **(Kombinasi Bersyarat Pembentukan Komite)**  
   Dari sekelompok ahli yang terdiri dari 5 orang dokter dan 4 orang insinyur, akan dibentuk tim peneliti beranggotakan 5 orang. Jika tim tersebut harus terdiri dari **minimal 3 orang dokter**, tentukan banyaknya susunan tim yang dapat dibentuk!

5. **(Permutasi Unsur Sama HOTS)**  
   Berapa banyak susunan huruf dari kata **"MISSISSIPPI"** yang dapat dibentuk?

---

## Bagian 3: Kunci Jawaban & Pembahasan Lengkap

### Kunci Jawaban Pilihan Ganda:
1. **C ($126$)** $\implies _9 C_5 = \frac{9!}{4! \cdot 5!} = 126$.
2. **D ($12.600$)** $\implies P = \frac{10!}{2! \cdot 3! \cdot 4! \cdot 1!} = 12.600$.
3. **C ($120$)** $\implies 4 \times 6 \times 5 = 120$.
4. **D ($5.376$)** $\implies \binom{9}{6} 2^6 = 84 \times 64 = 5.376$.
5. **B ($120$)** $\implies P_{\text{siklis}} = (6-1)! = 5! = 120$.
6. **C ($336$)** $\implies _8 P_3 = \frac{8!}{5!} = 8 \times 7 \times 6 = 336$.
7. **A ($151.200$)** $\implies n=10, M=2, A=3, T=2 \implies \frac{10!}{2! \cdot 3! \cdot 2!} = 151.200$.
8. **B ($210$)** $\implies _{10} C_4 = \frac{10!}{6! \cdot 4!} = 210$.
9. **D ($10.000$)** $\implies P_{\text{berulang}} = 10^4 = 10.000$.
10. **C ($112$)** $\implies \binom{8}{2} x^6 (2)^2 = 28 \times 4 = 112$.

---

### Pembahasan Soal Uraian:

1. **Pengurus OSIS Ketua Perempuan:**  
   - Ketua $= 3\text{ pilihan}$ (perempuan).
   - Sisa 2 posisi (Sekretaris & Bendahara) dipilih dari sisa 7 orang $\implies _7 P_2 = 7 \times 6 = 42$.  
   - Total susunan $= 3 \times 42 = 126\text{ cara}$.

2. **Binomial Newton Suku Bebas $x$:**  
   - Ekspansi $\left(2x^3 - x^{-2}\right)^5$.
   - $\text{Suku} = \binom{5}{r} (2x^3)^{5-r} (-x^{-2})^r = \binom{5}{r} 2^{5-r} (-1)^r x^{15 - 5r}$.
   - Bebas dari $x \implies 15 - 5r = 0 \implies r = 3$.
   - Nilai suku $= \binom{5}{3} 2^{5-3} (-1)^3 = 10 \times 4 \times (-1) = -40$.

3. **Permutasi Siklis Berdampingan:**  
   - Ketua & Sekretaris diikat $= 1$ elemen. Total elemen $= (7 - 2) + 1 = 6$ elemen.
   - Permutasi siklis 6 elemen $= (6-1)! = 5! = 120$.
   - Posisi internal Ketua & Sekretaris $= 2! = 2$.
   - Total $= 120 \times 2 = 240\text{ cara}$.

4. **Kombinasi Tim Minimal 3 Dokter:**  
   - Kasus 1: 3 Dokter & 2 Insinyur $\implies _5 C_3 \times _4 C_2 = 10 \times 6 = 60$.
   - Kasus 2: 4 Dokter & 1 Insinyur $\implies _5 C_4 \times _4 C_1 = 5 \times 4 = 20$.
   - Kasus 3: 5 Dokter & 0 Insinyur $\implies _5 C_5 \times _4 C_0 = 1 \times 1 = 1$.
   - Total cara $= 60 + 20 + 1 = 81\text{ cara}$.

5. **Permutasi Kata MISSISSIPPI:**  
   - Total huruf $n = 11$. Huruf M $= 1$, I $= 4$, S $= 4$, P $= 2$.
   - $P = \frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = \frac{39.916.800}{1 \times 24 \times 24 \times 2} = 34.650\text{ susunan}$.

---

## Bagian 4: Rubrik Penilaian

$$\text{Nilai Akhir (NA)} = \text{Skor PG (Maks 50)} + \text{Skor Uraian (Maks 50)} \quad (\text{Skala } 0 - 100)$$

| Rentang Nilai | Predikat | Keterangan Ketercapaian |
| :---: | :---: | :--- |
| $85 - 100$ | **A (Sangat Baik)** | Sangat mahir memahami kaidah pencacahan, permutasi, kombinasi, dan Binomial Newton HOTS. |
| $75 - 84$ | **B (Baik)** | Sudah tuntas memahami konsep dasar dan mampu menyelesaikan soal cerita kombinatorika. |
| $65 - 74$ | **C (Cukup)** | Memahami permutasi/kombinasi dasar, perlu bimbingan pada Binomial Newton & syarat khusus. |
| $< 65$ | **D (Perlu Bimbingan)** | Memerlukan remedial dan pendampingan khusus. |
