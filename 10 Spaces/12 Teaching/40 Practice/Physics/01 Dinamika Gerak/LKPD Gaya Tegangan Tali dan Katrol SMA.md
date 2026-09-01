---
title: "LKPD: Gaya Tegangan Tali & Katrol"
level: sma
target_audience: "SMA Kelas XI"
created: 2026-08-05
sources:
  - "[[Gaya Tegangan Tali dan Katrol SMA]]"
tags:
  - "lkpd"
  - "soal-evaluasi"
  - "fisika"
  - "sma"
  - "dinamika-gerak"
  - "katrol"
  - "atwood"
  - "multi-body-dynamics"
---

# Lembar Kerja Peserta Didik (LKPD): Gaya Tegangan Tali & Katrol 📝

Halo Guys! Siap buat menguji pemahaman kamu tentang gaya tegangan tali dan sistem katrol? 

Di lembar kerja ini, kamu bareng kelompok kamu bakal diajak membedah kasus katrol majemuk, melakukan eksperimen virtual simulasi Mesin Atwood, sampai menganalisis sistem crane raksasa pelabuhan! Setelah itu, ada tantangan soal mandiri buat melatih ketajaman penalaran kamu. *Yuk, langsung kita mulai!* 🏗️🪢

---

## Bagian I: Lembar Kerja Peserta Didik (LKPD) 🤝

### Identitas Kelompok:
* **Nama Kelompok:** ___________________________
* **Anggota Kelompok:**
  1. ________________________________________
  2. ________________________________________
  3. ________________________________________
  4. ________________________________________
* **Kelas / Semester:** XI / Ganjil

---

### Aktivitas 1: Bedah FBD Sistem Katrol Majemuk & Kinematika Terikat 🔍

#### 1. Tantangan Konseptual
Perhatikan gambar sistem katrol majemuk berikut yang menghubungkan Beban A ($m_A$) dan Beban B ($m_B$). Katrol 1 dipasang tetap di atap, sedangkan Katrol 2 adalah katrol bergerak yang langsung menggantungkan Beban B.

```
          /////// Atap //──────┐
             │                 │
             │ (Katrol 1)      │
           ┌─┴─┐               │
           │ O │               │
           └─┬─┘               │
             │               ┌─┴─┐
             │               │ O │ (Katrol 2 - Bergerak)
             │               └─┬─┘
           ┌─┴─┐               │
           │mA │             ┌─┴─┐
           └───┘             │mB │
                             └───┘
```

#### 2. Misi Kelompok Kamu:
1. **Gambar Diagram Gaya Bebas (FBD) Lengkap:**
   * Tunjukkan vektor gaya berat $w_A$ dan tegangan tali $T_1$ pada Beban A.
   * Tunjukkan vektor gaya berat $w_B$ dan gaya yang menopang katrol bergerak (Katrol 2).
   * Gambarkan panah gaya tegangan tali $T$ yang membelit Katrol 1 dan Katrol 2.
2. **Buktikan Hubungan Kinematika Terikat:**
   Jika Beban B bergerak naik sejauh $y_B$, buktikan secara matematis bahwa Beban A bakal bergerak turun sejauh $y_A = 2 y_B$, sehingga percepatannya memenuhi $a_A = 2 a_B$!
3. **Formulasikan Persamaan Gerak:**
   Tuliskan persamaan Hukum II Newton ($\Sigma F = m \cdot a$) untuk Beban A dan Beban B, lalu turunkan rumus percepatan $a_B$ dalam variabel $m_A, m_B,$ dan $g$!

---

### Aktivitas 2: Eksperimen Virtual Simulasi Mesin Atwood 💻✨

#### 1. Tujuan Eksperimen
* Menghitung percepatan sistem Mesin Atwood secara eksperimental dan teoritis.
* Menganalisis pengaruh selisih massa $(m_2 - m_1)$ terhadap percepatan sistem dan tegangan tali.
* Menentukan nilai percepatan gravitasi ($g$) dari data eksperimen.

#### 2. Alat dan Bahan (Simulasi PhET / OPhysics)
1. Perangkat Komputer / Tablet dengan koneksi internet.
2. Software Simulasi Fisika Mesin Atwood (*PhET / OPhysics Interactive Atwood Machine*).
3. Stopwatch digital (terintegrasi dalam simulasi).
4. Penggaris / mistar skala panjang ($s = 1{,}0\text{ m}$).

#### 3. Langkah Kerja Eksperimen:
1. Atur jarak tempuh lintasan vertikal beban $m_2$ sejauh $s = 1{,}0\text{ m}$.
2. Patok massa $m_1 = 100\text{ gram} = 0{,}10\text{ kg}$.
3. Variasikan massa $m_2$ berturut-turut: $120\text{ g}$, $140\text{ g}$, $160\text{ g}$, $180\text{ g}$, hingga $200\text{ g}$.
4. Lepaskan sistem dari posisi diam ($v_0 = 0$), lalu ukur dan catat waktu tempuh ($t$) sampai beban $m_2$ menyentuh dasar. Ulangi 3 kali percobaan untuk tiap variasi massa dan hitung waktu rata-ratanya ($t_{\text{rerata}}$).
5. Hitung percepatan eksperimen memakai rumus GLBB: $a_{\text{exp}} = \frac{2s}{t_{\text{rerata}}^2}$.
6. Hitung percepatan teori memakai rumus: $a_{\text{th}} = \left(\frac{m_2 - m_1}{m_1 + m_2}\right) g$ (gunakan $g = 9{,}8\text{ m/s}^2$).

#### 4. Tabel Data Pengamatan

| Percobaan Ke- | $m_1$ (kg) | $m_2$ (kg) | $(m_2 - m_1)$ (kg) | $(m_1 + m_2)$ (kg) | $t_1$ (s) | $t_2$ (s) | $t_3$ (s) | $t_{\text{rerata}}$ (s) | $a_{\text{exp}}$ ($\text{m/s}^2$) | $a_{\text{th}}$ ($\text{m/s}^2$) | Persentase Galat (%) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0,10 | 0,12 | 0,02 | 0,22 | | | | | | | |
| 2 | 0,10 | 0,14 | 0,04 | 0,24 | | | | | | | |
| 3 | 0,10 | 0,16 | 0,06 | 0,26 | | | | | | | |
| 4 | 0,10 | 0,18 | 0,08 | 0,28 | | | | | | | |
| 5 | 0,10 | 0,20 | 0,10 | 0,30 | | | | | | | |

*Catatan Rumus Persentase Galat:* $\text{Galat} = \left| \frac{a_{\text{th}} - a_{\text{exp}}}{a_{\text{th}}} \right| \times 100\%$

#### 5. Pertanyaan Diskusi Kelompok:
1. Berdasarkan data pengamatan kelompokmu, gimana hubungan antara selisih massa $(m_2 - m_1)$ dengan percepatan sistem?
2. Buatlah grafik hubungan antara rasio massa $\left(\frac{m_2 - m_1}{m_1 + m_2}\right)$ pada sumbu-X terhadap percepatan $a_{\text{exp}}$ pada sumbu-Y. Berapa kemiringan (*slope*) dari grafik tersebut? Apakah nilainya mendekati percepatan gravitasi $g$?
3. Coba sebutkan faktor-faktor fisis di dunia nyata yang bikin nilai $a_{\text{exp}}$ sedikit lebih kecil daripada $a_{\text{th}}$!

---

### Aktivitas 3: Studi Kasus STEM / Industri — Sistem Derek Katrol Pelabuhan 🚢🏗️

#### Konteks Industri:
Pelabuhan Peti Kemas Tanjung Priok memakai *crane* industri berbasis sistem katrol majemuk (*Block and Tackle*) untuk memindahkan kontainer logistik bermassa total $M = 12.000\text{ kg}$ (12 ton) dari kapal kargo ke atas dermaga.

```
       [Mesin Winch (Kuasa F)] ════ (Katrol Majemuk 4 Tali) ════ [Kontainer M = 12 ton]
```

Spesifikasi teknis tali baja yang dipakai:
* Jumlah segmen tali yang menopang katrol bergerak: $n = 4$.
* Batas Kekuatan Putus Tali (*Breaking Strength*): $F_{\text{max}} = 40.000\text{ N}$ per helai tali.
* Faktor Keselamatan Industri (*Safety Factor* / SF): Minimum 1,5 (Tegangan kerja aman maksimum $T_{\text{aman}} = \frac{F_{\text{max}}}{\text{SF}}$).
* Gunakan $g = 10\text{ m/s}^2$.

#### Misi Analisis Kasus:
1. **Analisis Keseimbangan Statis:**  
   Berapa gaya kuasa minimum ($F_{\text{kuasa}}$) yang harus dikeluarkan mesin motor *winch* crane untuk menahan kontainer menggantung diam di udara?
2. **Analisis Keamanan Operasional (Safety Audit):**  
   Apakah tali baja pelabuhan tersebut aman dipakai untuk mengangkat kontainer dalam kondisi diam ditinjau dari faktor keselamatan kerja (SF)? Jelaskan perhitunganmu!
3. **Analisis Akselerasi Maksimum:**  
   Berapa percepatan naik maksimum ($a_{\text{maks}}$) yang diperbolehkan waktu crane menarik kontainer ke atas agar tali baja **nggak putus** (tidak melebihi $T_{\text{aman}}$)?

---

## Bagian II: Latihan Soal Mandiri 🧠🔥

Saatnya menguji kemampuan fisikamu secara mandiri! Kerjakan soal-soal tantangan berikut dengan cermat dan teliti.

### A. Pilihan Ganda (5 Soal HOTS)

**Soal 1 (Balok Berdampingan & Gaya Gesek)**  
Tiga buah balok $m_1 = 2\text{ kg}$, $m_2 = 3\text{ kg}$, dan $m_3 = 5\text{ kg}$ diletakkan berdampingan di atas lantai horizontal kasar dengan koefisien gesek kinetis $\mu_k = 0{,}2$. Gaya horizontal $F = 50\text{ N}$ didorongkan pada balok $m_1$ ke kanan. Jika $g = 10\text{ m/s}^2$, besar gaya dorong kontak antar-permukaan balok $m_2$ dan balok $m_3$ ($P_{23}$) adalah...  
A. $10\text{ N}$  
B. $15\text{ N}$  
C. $20\text{ N}$  
D. $25\text{ N}$  
E. $30\text{ N}$

---

**Soal 2 (Mesin Atwood Diberi Gaya Luar Tambahan)**  
Sebuah Mesin Atwood ideal memiliki dua massa $m_1 = 3\text{ kg}$ dan $m_2 = 5\text{ kg}$ yang dihubungkan dengan tali ideal melalui katrol licin tanpa massa. Selain gaya berat, benda $m_1$ ditarik ke bawah oleh gaya luar vertikal konstan $F_{\text{luar}} = 10\text{ N}$. Jika $g = 10\text{ m/s}^2$, besar tegangan tali $T$ dalam sistem adalah...  
A. $27{,}5\text{ N}$  
B. $32{,}5\text{ N}$  
C. $37{,}5\text{ N}$  
D. $43{,}75\text{ N}$  
E. $47{,}5\text{ N}$

---

**Soal 3 (Kombinasi Bidang Miring Kasar & Katrol Vertikal)**  
Sebuah balok $A$ bermassa $m_A = 4\text{ kg}$ berada di atas bidang miring kasar dengan sudut elevasi $\theta = 37^\circ$ ($\sin 37^\circ = 0{,}6; \cos 37^\circ = 0{,}8$). Balok A dihubungkan oleh tali ideal yang melewati katrol licin di puncak bidang miring ke beban $B$ bermassa $m_B = 6\text{ kg}$ yang menggantung secara vertikal. Koefisien gesek kinetis antara balok A dan bidang miring adalah $\mu_k = 0{,}25$. Percepatan gerak sistem ($g = 10\text{ m/s}^2$) sebesar...  
A. $1{,}8\text{ m/s}^2$  
B. $2{,}8\text{ m/s}^2$  
C. $3{,}4\text{ m/s}^2$  
D. $4{,}2\text{ m/s}^2$  
E. $5{,}0\text{ m/s}^2$

---

**Soal 4 (Katrol Bergerak & Kinematika Terikat)**  
Sebuah sistem katrol terdiri dari katrol tetap dan katrol bergerak licin tanpa massa. Ujung tali katrol bergerak menopang beban $M = 12\text{ kg}$, sedangkan ujung tali bebas melewati katrol tetap ditarik oleh kuasa $F$. Jika beban $M$ terangkat ke atas dengan percepatan $a_M = 2\text{ m/s}^2$ ($g = 10\text{ m/s}^2$), maka besar gaya tarik $F$ yang bekerja pada ujung tali bebas adalah...  
A. $36\text{ N}$  
B. $48\text{ N}$  
C. $72\text{ N}$  
D. $96\text{ N}$  
E. $144\text{ N}$

---

**Soal 5 (Dinamika Mesin Atwood di Dalam Lift Dipercepat)**  
Sebuah laboratorium Mesin Atwood (dengan massa $m_1 = 2\text{ kg}$ dan $m_2 = 4\text{ kg}$) dipasang di dalam sebuah lift yang sedang bergerak naik ke atas dengan percepatan konstan $a_L = 2\text{ m/s}^2$. Percepatan gerak relatif massa $m_2$ terhadap katrol di dalam lift tersebut ($g = 10\text{ m/s}^2$) adalah...  
A. $2{,}0\text{ m/s}^2$  
B. $3{,}0\text{ m/s}^2$  
C. $4{,}0\text{ m/s}^2$  
D. $5{,}0\text{ m/s}^2$  
E. $6{,}0\text{ m/s}^2$

---

### B. Soal Uraian Penalaran (5 Soal Essay)

**Soal Uraian 1 (Tiga Balok Berdampingan dengan Dorongan Miring)**  
Tiga buah balok $m_1 = 1\text{ kg}$, $m_2 = 2\text{ kg}$, dan $m_3 = 3\text{ kg}$ berada berdampingan di atas lantai datar licin. Balok $m_1$ didorong oleh gaya $F = 20\text{ N}$ yang membentuk sudut $\alpha = 60^\circ$ miring ke bawah terhadap garis horizontal ($\cos 60^\circ = 0{,}5; \sin 60^\circ = 0{,}866$). Hitunglah:  
a. Percepatan gerak ketiga balok.  
b. Gaya dorong kontak antar balok 1 dan 2 ($P_{12}$).  
c. Gaya dorong kontak antar balok 2 dan 3 ($P_{23}$).

---

**Soal Uraian 2 (Pembacaan Timbangan Pegas Penyangga Mesin Atwood)**  
Sebuah Mesin Atwood ideal terdiri dari dua massa $m_A = 3\text{ kg}$ dan $m_B = 7\text{ kg}$ yang terhubung tali melalui katrol licin tak bermassa. Poros katrol tersebut digantungkan pada atap laboratorium melalui sebuah timbangan pegas ideal (skala dalam Newton). Hitunglah:  
a. Percepatan gerak kedua beban dan besar tegangan tali penghubung.  
b. Angka yang ditunjukkan oleh timbangan pegas penyangga katrol saat sistem sedang bergerak! (Gunakan $g = 9{,}8\text{ m/s}^2$).

---

**Soal Uraian 3 (Dua Bidang Miring Saling Membelakangi / Double Inclined Plane)**  
Dua buah benda $m_1 = 5\text{ kg}$ dan $m_2 = 10\text{ kg}$ diletakkan pada sistem dua bidang miring licin yang saling membelakangi dan terhubung oleh katrol di puncaknya. Sudut kemiringan bidang sebelah kiri tempat $m_1$ berada adalah $\theta_1 = 30^\circ$, sedangkan sudut kemiringan bidang sebelah kanan tempat $m_2$ berada adalah $\theta_2 = 53^\circ$ ($\sin 30^\circ = 0{,}5; \sin 53^\circ = 0{,}8$). Hitunglah:  
a. Arah gerak dan percepatan sistem ($g = 10\text{ m/s}^2$).  
b. Besar tegangan tali penghubung kedua benda.

---

**Soal Uraian 4 (Sistem Katrol Majemuk Maju / Differential Pulley)**  
Dua benda $m_1 = 8\text{ kg}$ dan $m_2 = 2\text{ kg}$ dirangkai dengan katrol bergerak dan katrol tetap licin tanpa massa. Tali melilit katrol bergerak yang menopang $m_1$, lalu melewati katrol tetap menuju $m_2$.  
a. Tuliskan hubungan kinematika percepatan antara $a_1$ dan $a_2$.  
b. Susunlah sistem persamaan gerak Newton untuk kedua benda.  
c. Hitunglah nilai percepatan masing-masing benda dan tegangan tali ($g = 10\text{ m/s}^2$).

---

**Soal Uraian 5 (Ambang Batas Gerak & Koefisien Gesek Statis Minimum)**  
Sebuah balok $m_1 = 5\text{ kg}$ berada pada bidang datar kasar yang dihubungkan tali ideal melewati katrol di tepi meja ke beban $m_2 = 3\text{ kg}$ yang menggantung vertikal.  
a. Tentukan nilai koefisien gesek statis minimum ($\mu_{s,\text{min}}$) agar sistem tetap diam (setimbang statis).  
b. Jika tiba-tiba ditambahkan beban tambahan $m_3 = 2\text{ kg}$ menumpuk di atas beban $m_2$ (sehingga total massa yang menggantung jadi $5\text{ kg}$) dan koefisien gesek kinetis meja adalah $\mu_k = 0{,}3$, hitunglah percepatan gerak sistem sekarang!

---

## Bagian III: Kunci Jawaban, Pembahasan, & Rubrik Penilaian 📐🔑

### A. Kunci Jawaban & Pembahasan Pilihan Ganda

1. **Jawaban: D ($25\text{ N}$)**  
   * **Pembahasan Detail:**  
     * Massa total $M = 2 + 3 + 5 = 10\text{ kg}$.  
     * Total gaya gesek kinetis $f_k = \mu_k M g = 0{,}2 \times 10 \times 10 = 20\text{ N}$.  
     * Percepatan sistem:  
       $$a = \frac{F - f_k}{M} = \frac{50 - 20}{10} = 3\text{ m/s}^2$$  
     * Gaya dorong $P_{23}$ adalah gaya yang mendorong balok $m_3$ meluncur di atas lantai kasar:  
       $$\Sigma F_{x,3} = m_3 a \implies P_{23} - f_{k,3} = m_3 a$$  
       $$f_{k,3} = \mu_k m_3 g = 0{,}2 \times 5 \times 10 = 10\text{ N}$$  
       $$P_{23} = m_3 a + f_{k,3} = (5 \times 3) + 10 = 15 + 10 = 25\text{ N}$$

2. **Jawaban: D ($43{,}75\text{ N}$)**  
   * **Pembahasan Detail:**  
     * FBD Benda 1 ($m_1 = 3\text{ kg}$): Gaya total ke bawah $= m_1 g + F_{\text{luar}} = (3 \times 10) + 10 = 40\text{ N}$.  
     * FBD Benda 2 ($m_2 = 5\text{ kg}$): Gaya berat ke bawah $= m_2 g = 50\text{ N}$.  
     * Karena $m_2 g (50\text{ N}) > (m_1 g + F_{\text{luar}}) (40\text{ N})$, benda 2 turun dan benda 1 naik.  
     * Percepatan sistem:  
       $$a = \frac{m_2 g - (m_1 g + F_{\text{luar}})}{m_1 + m_2} = \frac{50 - 40}{3 + 5} = \frac{10}{8} = 1{,}25\text{ m/s}^2$$  
     * Tegangan tali $T$:  
       $$T = m_2 g - m_2 a = 50 - (5 \times 1{,}25) = 50 - 6{,}25 = 43{,}75\text{ N}$$  
       *(Tinjau Benda 1:* $T - (m_1 g + F_{\text{luar}}) = m_1 a \implies T - 40 = 3(1{,}25) \implies T = 43{,}75\text{ N}$).

3. **Jawaban: B ($2{,}8\text{ m/s}^2$)**  
   * **Pembahasan Detail:**  
     * Komponen berat balok A sejajar bidang miring: $w_{Ax} = m_A g \sin 37^\circ = 4 \times 10 \times 0{,}6 = 24\text{ N}$.  
     * Gaya normal balok A: $N_A = m_A g \cos 37^\circ = 4 \times 10 \times 0{,}8 = 32\text{ N}$.  
     * Gaya gesek kinetis A: $f_k = \mu_k N_A = 0{,}25 \times 32 = 8\text{ N}$.  
     * Gaya penarik benda B: $w_B = m_B g = 6 \times 10 = 60\text{ N}$.  
     * Karena $w_B (60\text{ N}) > w_{Ax} (24\text{ N})$, benda B turun dan A naik bidang miring. Gaya gesek $f_k$ mengarah ke bawah bidang miring.  
     * Percepatan sistem:  
       $$a = \frac{w_B - w_{Ax} - f_k}{m_A + m_B} = \frac{60 - 24 - 8}{4 + 6} = \frac{28}{10} = 2{,}8\text{ m/s}^2$$

4. **Jawaban: C ($72\text{ N}$)**  
   * **Pembahasan Detail:**  
     * Katrol bergerak menopang beban $M = 12\text{ kg}$.  
     * Hukum II Newton untuk katrol bergerak bermassa $M$:  
       $$2T - M g = M a_M$$  
       $$2T - (12 \times 10) = 12 \times 2$$  
       $$2T - 120 = 24 \implies 2T = 144 \implies T = 72\text{ N}$$  
     * Karena kuasa $F$ ditarik pada ujung tali yang sama, maka $F = T = 72\text{ N}$.

5. **Jawaban: C ($4{,}0\text{ m/s}^2$)**  
   * **Pembahasan Detail:**  
     * Dalam kerangka non-inersia lift yang dipercepat ke atas dengan $a_L = 2\text{ m/s}^2$, gravitasi efektif di dalam lift menjadi:  
       $$g_{\text{efektif}} = g + a_L = 10 + 2 = 12\text{ m/s}^2$$  
     * Percepatan relatif Mesin Atwood di dalam lift:  
       $$a_{\text{rel}} = \left(\frac{m_2 - m_1}{m_1 + m_2}\right) g_{\text{efektif}} = \left(\frac{4 - 2}{2 + 4}\right) \times 12 = \frac{2}{6} \times 12 = 4{,}0\text{ m/s}^2$$

---

### B. Pembahasan Lengkap Soal Uraian

**Uraian 1:**  
a. Komponen gaya horizontal efektif: $F_x = F \cos 60^\circ = 20 \times 0{,}5 = 10\text{ N}$.  
   Percepatan sistem: $a = \frac{F_x}{m_1 + m_2 + m_3} = \frac{10}{1 + 2 + 3} = \frac{10}{6} = 1{,}67\text{ m/s}^2$.  
b. Gaya dorong kontak $P_{12}$ (mendorong balok 2 dan 3):  
   $$P_{12} = (m_2 + m_3) a = (2 + 3) \times 1{,}67 = 8{,}33\text{ N}$$  
c. Gaya dorong kontak $P_{23}$ (mendorong balok 3):  
   $$P_{23} = m_3 a = 3 \times 1{,}67 = 5{,}0\text{ N}$$

---

**Uraian 2:**  
a. Diketahui $m_A = 3\text{ kg}, m_B = 7\text{ kg}, g = 9{,}8\text{ m/s}^2$.  
   $$a = \left(\frac{7 - 3}{3 + 7}\right) \times 9{,}8 = \frac{4}{10} \times 9{,}8 = 3{,}92\text{ m/s}^2$$  
   $$T = \left(\frac{2 \times 3 \times 7}{3 + 7}\right) \times 9{,}8 = \frac{42}{10} \times 9{,}8 = 41{,}16\text{ N}$$  
b. Pembacaan timbangan pegas penopang katrol ($F_{\text{pegas}}$):  
   $$F_{\text{pegas}} = 2T = 2 \times 41{,}16\text{ N} = 82{,}32\text{ N}$$

---

**Uraian 3:**  
a. Gaya penarik sisi kiri: $w_{1x} = m_1 g \sin 30^\circ = 5 \times 10 \times 0{,}5 = 25\text{ N}$.  
   Gaya penarik sisi kanan: $w_{2x} = m_2 g \sin 53^\circ = 10 \times 10 \times 0{,}8 = 80\text{ N}$.  
   Karena $w_{2x} (80\text{ N}) > w_{1x} (25\text{ N})$, sistem bergerak **ke kanan (benda 2 meluncur turun, benda 1 tertarik naik)**.  
   $$a = \frac{w_{2x} - w_{1x}}{m_1 + m_2} = \frac{80 - 25}{5 + 10} = \frac{55}{15} = 3{,}67\text{ m/s}^2$$  
b. Tegangan tali $T$:  
   $$T = w_{1x} + m_1 a = 25 + (5 \times 3{,}67) = 25 + 18{,}33 = 43{,}33\text{ N}$$

---

**Uraian 4:**  
a. Kinematika terikat: Tali melilit katrol bergerak $m_1$, sehingga $a_2 = 2 a_1$ (percepatan $m_2$ dua kali percepatan $m_1$).  
b. Persamaan Newton:  
   * Katrol $m_1$: $2T - m_1 g = m_1 a_1 \implies 2T - 80 = 8 a_1$.  
   * Massa $m_2$: $m_2 g - T = m_2 a_2 \implies 20 - T = 2 (2 a_1) = 4 a_1 \implies T = 20 - 4 a_1$.  
c. Substitusikan $T$ ke persamaan katrol $m_1$:  
   $$2(20 - 4 a_1) - 80 = 8 a_1 \implies 40 - 8 a_1 - 80 = 8 a_1 \implies -40 = 16 a_1$$  
   *(Nilai negatif artinya asumsi arah terbalik: $m_2$ terlalu ringan sehingga $m_1$ turun dan $m_2$ naik!)*  
   Percepatan $a_1 = \frac{40}{16} = 2{,}5\text{ m/s}^2$ ($m_1$ turun) dan $a_2 = 5{,}0\text{ m/s}^2$ ($m_2$ naik). Tegangan tali $T = 20 + 2(5) = 30\text{ N}$.

---

**Uraian 5:**  
a. Syarat tepat akan bergerak (setimbang statis):  
   $$m_2 g = f_{s,\max} \implies m_2 g = \mu_s m_1 g \implies \mu_s = \frac{m_2}{m_1} = \frac{3}{5} = 0{,}60$$  
b. Total massa menggantung baru $m_2' = 5\text{ kg}$.  
   $$a = \frac{m_2' g - \mu_k m_1 g}{m_1 + m_2'} = \frac{(5 \times 10) - (0{,}3 \times 5 \times 10)}{5 + 5} = \frac{50 - 15}{10} = 3{,}5\text{ m/s}^2$$

---

### C. Rubrik Penilaian & Pedoman Penskoran 💯

#### 1. Pembobotan Nilai Evaluasi
* **Pilihan Ganda (5 Soal):** Bobot 40% (8% per soal benar).
* **Soal Uraian (5 Soal):** Bobot 60% (12% per soal dengan rincian kriteria).

#### 2. Kriteria Penskoran Soal Uraian (Skor Maksimal = 12 Per Soal)

| Indikator Penilaian | Skor Maksimal | Deskripsi Penilaian |
| :--- | :---: | :--- |
| **FBD & Identifikasi Variabel** | 3 | Menggambar Diagram Gaya Bebas (FBD) dengan tepat dan menuliskan variabel diketahui/ditanya secara lengkap. |
| **Formulasi Hukum Newton** | 3 | Menuliskan persamaan $\Sigma F = m \cdot a$ serta hubungan kinematika terikat yang akurat. |
| **Substitusi & Kalkulasi Aljabar** | 4 | Melakukan perhitungan aljabar/substitusi dengan teliti tanpa kesalahan hitung. |
| **Hasil Akhir & Satuan SI** | 2 | Menyebutkan angka hasil akhir disertai satuan SI yang benar. |

$$\text{Nilai Akhir (NA)} = \left( \sum \text{Skor PG} \times 8 \right) + \left( \frac{\sum \text{Skor Uraian}}{60} \times 60 \right)$$
