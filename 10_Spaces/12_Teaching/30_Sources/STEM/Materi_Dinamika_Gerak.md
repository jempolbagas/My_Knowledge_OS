---
title: "Materi Ajar: Dinamika Gerak Partikel (Hukum Newton & Aplikasinya)"
target_audience: "SMA Kelas XI"
created: 2026-08-03
sources:
  - "[[Gaya dan Hukum Newton]]"
  - "[[Gerak Lurus]]"
  - "[[Gerak Lurus Berubah Beraturan (GLBB)]]"
tags:
  - fisika
  - dinamika-gerak
  - hukum-newton
  - kelas-11
  - modul-ajar
---

# Modul Ajar Terpadu: Dinamika Gerak Partikel

## 1. Pendahuluan & Capaian Pembelajaran

### 1.1 Orientasi Umum
Dinamika gerak merupakan cabang mekanika klasik yang mempelajari gerak suatu benda dengan memperhitungkan penyebab terjadinya gerak tersebut, yaitu **Gaya** ($\vec{F}$). Berbeda dengan Kinematika yang hanya mendeskripsikan posisi, kecepatan, dan percepatan tanpa memedulikan penyebab gerak, Dinamika menelaah hubungan kausalitas antara besaran fisis gaya, massa ($m$), dan respons gerak berupa percepatan ($\vec{a}$).

### 1.2 Capaian Pembelajaran (CP) / Tujuan Pembelajaran
Setelah mempelajari materi ini, peserta didik kelas XI diharapkan mampu:
1. Menganalisis konsep hukum-hukum Newton (Hukum I, II, dan III Newton) serta menerapkannya pada fenomena kehidupan sehari-hari.
2. Memprediksi dan menghitung besaran-besaran fisis (percepatan, tegangan tali, gaya normal, dan gaya gesek) pada berbagai sistem mekanika (bidang datar, bidang miring, sistem katrol, dan gerak dalam lift).
3. Menggambar Diagram Bebas Benda (*Free-Body Diagram* / FBD) secara akurat sebagai alat bantu pemecahan masalah fisika.
4. Menganalisis miskonsepsi umum terkait konsep gaya dan gerak melalui pendekatan nalar ilmiah.

---

## 2. Hakikat Gaya & Diagram Bebas Benda (Free-Body Diagram)

### 2.1 Definisi Gaya
Gaya ($\vec{F}$) adalah dorongan atau tarikan yang bekerja pada suatu benda yang dapat menyebabkan perubahan bentuk, ukuran, posisi, maupun keadaan gerak benda (kecepatan). Gaya merupakan **besaran vektor**, sehingga memiliki besar (magnitudo) dan arah. Satuan SI untuk gaya adalah **Newton (N)**, di mana $1\text{ N} = 1\text{ kg}\cdot\text{m/s}^2$.

### 2.2 Jenis-Jenis Gaya Khusus

#### A. Gaya Berat ($\vec{W}$)
Gaya tarik bumi (gravitasi) yang bekerja pada suatu benda bermassa. Direction gaya berat **selalu tegak lurus mengarah ke pusat bumi (ke bawah)**.
$$\vec{W} = m \cdot \vec{g}$$
*Keterangan:* $m$ = massa benda (kg), $g$ = percepatan gravitasi ($\text{m/s}^2$).

#### B. Gaya Normal ($\vec{N}$)
Gaya kontak yang dikerjakan oleh permukaan bidang terhadap benda yang menyentuhnya. Direction gaya normal **selalu tegak lurus keluar dari bidang sentuh**.
- Bidang datar datar: $N = W = mg$ (jika tidak ada gaya luar vertikal lain).
- Bidang miring dengan sudut $\theta$: $N = W \cos\theta = mg \cos\theta$.

#### C. Gaya Gesekan ($\vec{f}$)
Gaya yang timbul akibat interaksi dua permukaan yang saling bersentuhan. Arah gaya gesek **selalu berlawanan dengan arah kecenderungan gerak benda**.
1. **Gaya Gesek Statis ($f_s$):** Gaya gesek yang bekerja saat benda belum bergerak.
   - Nilai maksimum gaya gesek statis: $f_{s,\text{maks}} = \mu_s \cdot N$.
   - Jika gaya tarik $F \le f_{s,\text{maks}}$, benda **diam** dan $f_s = F$.
2. **Gaya Gesek Kinetis ($f_k$):** Gaya gesek yang bekerja saat benda sudah dalam keadaan bergerak.
   - $f_k = \mu_k \cdot N$ (di mana $\mu_k < \mu_s$).

#### D. Gaya Tegangan Tali ($\vec{T}$)
Gaya tarik yang ditransmisikan melalui tali, kawat, atau kabel ketika ditarik oleh gaya dari arah berlawanan. Gaya tegangan tali selalu bekerja menjauhi benda yang ditinjau.

#### E. Gaya Sentripetal ($\vec{F}_c$)
Resultan gaya yang mengarah ke pusat lintasan melingkar yang menyebabkan benda mengalami gerak melingkar.
$$F_c = m a_c = m \frac{v^2}{r} = m \omega^2 r$$

---

## 3. Hukum-Hukum Newton tentang Gerak

```
+-------------------------------------------------------------------------+
|                           HUKUM-HUKUM NEWTON                            |
+-----------------------------+-----------------------------+-------------+
|        Hukum I Newton       |       Hukum II Newton       | Hukum III N |
|     (Hukum Kelembaman)      |    (Hubungan F, m, dan a)   | (Aksi-Reak) |
+-----------------------------+-----------------------------+-------------+
|    "Benda cenderung         | "Percepatan sebanding dg    | "F_aksi =   |
|     mempertahankan kondisi  |  resultan gaya dan ber-     |  -F_reaksi" |
|     geraknya (diam/GLB)"    |  banding terbalik massa"    |             |
|                             |                             | Bekerja pd  |
|      \sum \vec{F} = 0       |     \sum \vec{F} = m \vec{a}| dua benda   |
|   => a = 0 (diam/GLB)       |                             | berbeda.    |
+-----------------------------+-----------------------------+-------------+
```

### 3.1 Hukum I Newton (Inersia / Kelembaman)
> *"Setiap benda akan tetap diam atau bergerak lurus beraturan (GLB) jika tidak ada gaya luar yang bekerja padanya, atau jika resultan gaya yang bekerja pada benda sama dengan nol."*

$$\sum \vec{F} = 0 \implies \vec{a} = 0 \quad (\text{Benda Diam atau Gerak Lurus Beraturan})$$

* **Kerangka Acuan Inersial:** Kerangka acuan yang tidak mengalami percepatan (diam atau bergerak dengan kecepatan konstan). Hukum I dan II Newton hanya berlaku secara eksplisit pada kerangka acuan inersial.
* **Aplikasi Nyata:**
  - Penumpang mobil terdorong ke depan saat mobil direm mendadak.
  - Memukul bagian bawah botol saus agar saus di dalamnya mengalir keluar akibat sifat kelembaman saus.

### 3.2 Hukum II Newton (Percepatan)
> *"Percepatan sebuah benda sebanding dengan resultan gaya yang bekerja pada benda tersebut dan berbanding terbalik dengan massa benda."*

$$\sum \vec{F} = m \cdot \vec{a} \implies \vec{a} = \frac{\sum \vec{F}}{m}$$

* **Bentuk Komponen 2D:**
  $$\sum F_x = m a_x \quad \text{dan} \quad \sum F_y = m a_y$$
* **Catatan Penting:** Gaya memicu perubahan kecepatan (percepatan), bukan mempertahankan kecepatan. Tanpa resultan gaya, kecepatan benda bersifat konstan.

### 3.3 Hukum III Newton (Aksi - Reaksi)
> *"Ketika suatu benda mengerjakan gaya pada benda kedua (gaya aksi), benda kedua akan mengerjakan gaya yang besarnya sama tetapi arahnya berlawanan pada benda pertama (gaya reaksi)."*

$$\vec{F}_{\text{aksi}} = -\vec{F}_{\text{reaksi}}$$

* **Ciri-ciri Pasangan Gaya Aksi-Reaksi:**
  1. Besarnya **sama**.
  2. Arahnya **berlawanan** ($180^\circ$).
  3. Bekerja pada **dua benda yang berbeda** (tidak saling meniadakan dalam satu benda).
  4. Merupakan jenis gaya yang **sejenis** (sama-sama gaya kontak atau gaya medan).

---

## 4. Analisis Sistem Dinamika Populer

### 4.1 Benda pada Bidang Datar (Kasus Kasar & Membentuk Sudut $\theta$)
Sebuah benda bermassa $m$ ditarik gaya $F$ yang membentuk sudut $\theta$ terhadap bidang datar kasar dengan koefisien gesek $\mu_k$.

1. **Komponen Gaya Vertikal ($y$-axis):**
   $$\sum F_y = 0 \implies N + F \sin\theta - W = 0 \implies N = mg - F \sin\theta$$
2. **Gaya Gesek Kinetis:**
   $$f_k = \mu_k N = \mu_k (mg - F \sin\theta)$$
3. **Persamaan Gerak Horizontal ($x$-axis):**
   $$\sum F_x = m a \implies F \cos\theta - f_k = m a$$
   $$a = \frac{F \cos\theta - \mu_k (mg - F \sin\theta)}{m}$$

---

### 4.2 Benda pada Bidang Miring (Kasus Kasar)
Benda bermassa $m$ meluncur turun pada bidang miring kasar dengan sudut kemiringan $\theta$.

```
         /|
        / |
       /  |
      /   |
     /    |
    /_____|  \theta
```

1. **Uraian Gaya:**
   - Komponen searah bidang miring (sejajar gerak): $W_x = mg \sin\theta$ (mengarah ke bawah).
   - Komponen tegak lurus bidang miring: $W_y = mg \cos\theta$.
2. **Keseimbangan Vertikal (Tegak lurus bidang miring):**
   $$N = W_y = mg \cos\theta$$
3. **Gaya Gesek:**
   $$f_k = \mu_k N = \mu_k mg \cos\theta$$
4. **Percepatan Meluncur Turun:**
   $$\sum F = m a \implies mg \sin\theta - f_k = m a$$
   $$a = g(\sin\theta - \mu_k \cos\theta)$$

*Syarat benda bergerak meluncur turun:* $\tan\theta > \mu_s$.

---

### 4.3 Sistem Katrol (Mesin Atwood)
Dua benda bermassa $m_1$ dan $m_2$ ($m_2 > m_1$) dihubungkan dengan tali ideal melalui katrol licin dan massa katrol diabaikan.

```
       [KATROL]
        /    \
       /      \
     [m1]    [m2]  (m2 turun, m1 naik)
```

1. **Tinjauan Benda 1 ($m_1$ naik):**
   $$\sum F_1 = m_1 a \implies T - m_1 g = m_1 a \quad \text{--- (1)}$$
2. **Tinjauan Benda 2 ($m_2$ turun):**
   $$\sum F_2 = m_2 a \implies m_2 g - T = m_2 a \quad \text{--- (2)}$$
3. **Eliminasi / Penggabungan Sistem:**
   $$a = \left( \frac{m_2 - m_1}{m_1 + m_2} \right) g$$
4. **Tegangan Tali ($T$):**
   $$T = \frac{2 m_1 m_2}{m_1 + m_2} g$$

---

### 4.4 Gerak Semu dalam Lift (Desakan Kaki / Berat Semu)
Seseorang bermassa $m$ berdiri di atas timbangan di dalam lift. Berat sesungguhnya adalah $W = mg$. Berat semu yang terbaca pada timbangan adalah gaya normal $N$.

| Kondisi Lift | Persamaan Hukum II Newton ($\sum F_y = m a$) | Berat Semu / Desakan Kaki ($N$) | Sensasi Fisik |
| :--- | :--- | :--- | :--- |
| **Diam / Kecepatan Konstan** | $N - mg = 0$ | $N = mg$ | Normal |
| **Naik Dipercepat** ($a \uparrow$) | $N - mg = m a$ | $N = m(g + a)$ | Merasa Lebih Berat |
| **Naik Diperlambat** ($a \downarrow$) | $N - mg = -m a$ | $N = m(g - a)$ | Merasa Lebih Ringan |
| **Turun Dipercepat** ($a \downarrow$) | $mg - N = m a$ | $N = m(g - a)$ | Merasa Lebih Ringan |
| **Turun Diperlambat** ($a \uparrow$) | $N - mg = m a$ | $N = m(g + a)$ | Merasa Lebih Berat |
| **Tali Lift Putus** ($a = g \downarrow$) | $mg - N = mg$ | $N = 0$ | Bobot Kosong (*Weightlessness*) |

---

## 5. Miskonsepsi Umum & Klarifikasi Ilmiah

| Miskonsepsi Peserta Didik | Pembetulan Konsep Ilmiah |
| :--- | :--- |
| **1. "Benda yang sedang bergerak pasti sedang dikenai gaya dorong."** | **Salah.** Sesuai Hukum I Newton, benda yang sedang bergerak dengan kecepatan konstan tidak memerlukan gaya dorong. Gaya diperlukan untuk **mengubah** kecepatan, bukan mempertahankan gerakan. |
| **2. "Gaya aksi dan gaya reaksi saling meniadakan sehingga resultannya nol."** | **Salah.** Gaya aksi dan reaksi bekerja pada **dua benda yang berbeda**, sehingga keduanya tidak dapat dijumlahkan dalam satu diagram gaya benda tunggal. |
| **3. "Gaya normal selalu sama besarnya dengan gaya berat ($N = W$)."** | **Salah.** Gaya normal $N$ bergantung pada tekanan kontak permukaan. Pada bidang miring $N = W \cos\theta$, dan pada lift yang berakselerasi $N \neq W$. |
| **4. "Gaya gesek statis selalu bernilai $\mu_s N$."** | **Salah.** $\mu_s N$ adalah batas **maksimum** gaya gesek statis. Sebelum mencapai batas tersebut, $f_s$ menyesuaikan besarnya gaya tarik horizontal yang diberikan ($f_s = F_{\text{luar}}$). |

---
*Dokumen ini disusun untuk mendukung pembelajaran Fisika SMA Kelas XI Kurikulum Merdeka.*
