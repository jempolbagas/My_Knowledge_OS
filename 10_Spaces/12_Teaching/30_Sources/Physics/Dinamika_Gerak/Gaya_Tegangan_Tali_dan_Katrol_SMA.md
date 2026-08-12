---
title: "Gaya Tegangan Tali & Sistem Katrol — Rahasia Kerja Ringan Beban Berat!"
level: sma
target_audience: "SMA Kelas XI"
created: 2026-08-05
sources:
  - "[[Gaya dan Hukum Newton]]"
tags:
  - "teaching-material"
  - "physics"
  - "sma"
  - "dinamika-gerak"
  - "gaya-tegangan-tali"
  - "katrol"
  - "atwood"
  - "multi-body-dynamics"
---

# BAB 1: Gaya Tegangan Tali & Katrol — Rahasia Kerja Ringan Beban Berat! 🏗️🪢

> 📍 **Navigasi Modul Dinamika Gerak:**  
> [[Dinamika_Gerak_SMA|🏠 Master Dashboard]] | [[Gaya_Berat_SMA|1. Gaya Berat]] | [[Gaya_Normal_SMA|2. Gaya Normal]] | [[Gaya_Gesek_SMA|3. Gaya Gesek]] | **[4. Tegangan Tali & Katrol]** | [[Gaya_Sentripetal_SMA|5. Gaya Sentripetal]] | 📝 [[LKPD_Dinamika_Gerak_SMA|LKPD Terpadu]]

Pernah ngeliat derek konstruksi ngangkat beban beton ber-ton-ton dengan santai? Atau pernah nimba air di sumur pakai katrol? Gimana caranya tali tipis dan roda katrol bisa bikin beban berat berasa ringan?

Yuk, kita bongkar rahasia fisika di balik **gaya tegangan tali** dan **sistem katrol** yang bikin pekerjaan berat di dunia teknik jadi jauh lebih mudah!

---

## 1. Identitas Modul & Tujuan Pembelajaran 🎯

### Identitas Modul:
* **Mata Pelajaran:** Fisika
* **Kelas / Fase:** XI / Fase F
* **Materi Pokok:** Dinamika Gerak Lurus (Sistem Banyak Benda / *Multi-Body Dynamics*)
* **Sub-Materi:** Gaya Tegangan Tali ($\vec{T}$), Sistem Balok Berdampingan (Gaya Kontak), Mesin Atwood, Katrol & Bidang (Licin & Kasar), serta Katrol Bergerak & Keuntungan Mekanis (*Mechanical Advantage*).

### Tujuan Pembelajaran:
Setelah mempelajari modul ini, kamu diharapkan jago dalam:
1. **Memahami** konsep fisis Gaya Tegangan Tali ($\vec{T}$) sebagai pengirim gaya internal dan menganalisis konsekuensi asumsi tali ideal (tanpa massa & tak mulur).
2. **Menganalisis** interaksi gaya kontak aksi-reaksi ($P_{ij}$) pada sistem benda berdampingan yang didorong gaya luar di lantai licin maupun kasar.
3. **Menurunkan** persamaan percepatan ($a$) dan tegangan tali ($T$) pada Mesin Atwood (*Atwood Machine*) memakai Hukum II Newton secara sistematis.
4. **Memprediksi dan menghitung** dinamika sistem kombinasi katrol pada bidang datar dan bidang miring (kasus licin dan kasar).
5. **Menganalisis** kinematika terikat (*constrained motion*) dan dinamika pada sistem katrol bergerak (*movable pulley*) serta menghitung Keuntungan Mekanis (*Mechanical Advantage*) katrol majemuk.

---

## 2. Konsep Gaya Tegangan Tali ($\vec{T}$) & Asumsi Tali Ideal 🪢

### A. Pengertian & Asal-usul Tegangan Tali
Waktu kamu menarik benda pakai tali, kabel, atau rantai, gaya tarik kamu bakal disalurkan dari ujung satu ke ujung lainnya lewat tali tersebut. Nah, gaya tarik yang bekerja sepanjang tali ini kita sebut **Gaya Tegangan Tali** ($\vec{T}$, singkatan dari *Tension*).

Kalau diintip pakai mikroskop super canggih, tegangan tali ini sebenarnya berasal dari **gaya tarik-menarik antarmolekul** (gaya elektromagnetik) penyusun tali tersebut. 

> 💡 **Analogy Time!**  
> Bayangkan molekul-molekul tali seperti **rantai manusia yang saling bergandengan tangan erat-erat**. Ketika kedua ujung tali ditarik ke luar, jarak antarmolekul merenggang sedikit dari posisi santainya. Molekul-molekul ini pun langsung mengeluarkan gaya pemulih buat menarik teman di sebelahnya agar bergandengan erat kembali!

![[diagram_physics_tegangan_tali_internal.webp]]

> [!IMPORTANT]
> **Aturan Emas Vektor Tegangan Tali:**  
> **Gaya tegangan tali SELALU digambar mengarah MENJAUHI benda!**  
> Tali itu benda fleksibel: **hanya bisa menarik, NGGAK BISA mendorong** (*strings can pull, but cannot push*). Jadi, waktu menggambar Diagram Gaya Bebas (*Free Body Diagram* / FBD), panah gaya tegangan tali $\vec{T}$ pada suatu benda selalu ditarik keluar menjauhi benda tersebut menyusuri lintasan tali.

### B. Idealisi Fisika: Asumsi Tali Ideal
Dalam penyelesaian soal fisika, kita sering memakai model **Tali Ideal** supaya perhitungan aljabar kita nggak ribet tanpa menghilangkan prinsip utamanya. Ciri-ciri tali ideal ada dua:

1. **Tali Tanpa Massa ($m_{\text{tali}} = 0$):**
   * **Dampaknya:** Gaya tegangan tali di sepanjang serat tali nilainya **seragam/sama besar** dari ujung satu ke ujung lainnya, asal nggak ada gaya luar yang menarik bagian tengah tali.
   * Kalau tali melewati katrol ideal (licin dan tanpa massa), tegangan tali di sebelah kiri dan kanan katrol nilainya **pasti sama** ($T_1 = T_2 = T$).

2. **Tali Tak-Mulur / Tak-Regang (*Inextensible*, $\Delta L = 0$):**
   * **Dampaknya:** Panjang tali total selalu konstan sepanjang waktu.
   * **Konsekuensi Gerak:** Kalau benda A terhubung langsung dengan benda B lewat tali ideal yang tegang, maka perpindahan ($x$), kecepatan ($v$), dan besarnya percepatan ($a$) dari benda A dan B **wajib persis sama** ($a_A = a_B = a$).

---

## 3. Sistem Benda Berdampingan (Gaya Kontak Aksi-Reaksi) 🤝

Sebelum masuk ke katrol, yuk kita kepoin dulu sistem *multi-body* paling simpel: balok-balok yang saling nempel di atas lantai lalu didorong gaya horizontal $F$.

![[diagram_physics_tegangan_tali_benda_berdampingan.webp]]

### A. Penurunan Kasus Lantai Licin
Misalkan ada tiga balok bermassa $m_1$, $m_2$, dan $m_3$ berjejer di lantai licin, lalu balok $m_1$ didorong gaya $F$ ke kanan.

1. **Pandang Sebagai Satu Super-Benda (Sistem Utuh):**  
   Karena ketiga balok bergerak bareng dengan percepatan yang sama ($a$), kita bisa menganggap ketiganya sebagai satu gabungan benda bermassa total $M = m_1 + m_2 + m_3$.
   $$\Sigma F_x = M_{\text{total}} \cdot a$$
   $$F = (m_1 + m_2 + m_3) a \implies a = \frac{F}{m_1 + m_2 + m_3}$$

2. **Bedah FBD Per Benda (Menghitung Gaya Kontak $P_{ij}$):**  
   Gaya $P_{ij}$ adalah gaya dorong kontak dari benda $i$ ke benda $j$. Sesuai Hukum III Newton (Aksi-Reaksi), besar $P_{12} = P_{21}$ dan $P_{23} = P_{32}$.

   * **FBD Balok $m_1$:**  
     Didorong $F$ ke kanan, dan ditahan gaya kontak balik dari balok 2 ke kiri ($P_{21}$).
     $$\Sigma F_{x,1} = m_1 a \implies F - P_{21} = m_1 a \implies P_{21} = F - m_1 a$$
     Substitusikan $a = \frac{F}{m_1 + m_2 + m_3}$:
     $$P_{21} = F - m_1 \left(\frac{F}{m_1 + m_2 + m_3}\right) = F \left(1 - \frac{m_1}{m_1 + m_2 + m_3}\right)$$
     $$P_{12} = P_{21} = \frac{m_2 + m_3}{m_1 + m_2 + m_3} F$$

   * **FBD Balok $m_3$:**  
     Balok 3 cuma didorong ke kanan oleh balok 2 lewat gaya $P_{23}$.
     $$\Sigma F_{x,3} = m_3 a \implies P_{23} = m_3 a = \frac{m_3}{m_1 + m_2 + m_3} F$$

### B. Kasus Lantai Kasar (Koefisien Gesek $\mu_k$)
Kalau lantainya kasar dengan koefisien gesek kinetis $\mu_k$:
* Tiap balok kena gaya gesek: $f_{k,1} = \mu_k m_1 g$, $f_{k,2} = \mu_k m_2 g$, $f_{k,3} = \mu_k m_3 g$.
* Total gaya gesek: $f_{k,\text{total}} = \mu_k (m_1 + m_2 + m_3) g$.
* Percepatan sistem menjadi:
  $$a = \frac{F - \mu_k (m_1 + m_2 + m_3) g}{m_1 + m_2 + m_3} = \frac{F}{m_1 + m_2 + m_3} - \mu_k g$$

---

## 4. Mesin Atwood: Katrol Tetap Licin ⚖️

Mesin Atwood (*Atwood Machine*) diciptakan oleh fisikawan Inggris George Atwood pada tahun 1784. Dulu, alat ini dibuat buat "memperlambat" gerak jatuh bebas akibat gravitasi supaya hukum-hukum gerak Newton bisa diukur dengan teliti di laboratorium!

![[diagram_physics_tegangan_tali_mesin_atwood.webp]]

### A. Asumsi Sistem Mesin Atwood Ideal
1. Katrol tetap licin tanpa gesekan dan massanya diabaikan ($I_{\text{katrol}} = 0$).
2. Tali ideal (tanpa massa dan tak mulur), jadi $T_1 = T_2 = T$ dan percepatan kedua beban sama ($a_1 = a_2 = a$).
3. Misalkan $m_2 > m_1$, maka $m_2$ bakal meluncur turun dan $m_1$ terangkat naik!

### B. Penurunan Rumus Percepatan ($a$) & Tegangan Tali ($T$)
Yuk, kita gambar FBD untuk masing-masing beban:

1. **Analisis Benda 1 ($m_1$ bergerak NAIK):**  
   Arah naik kita beri tanda positif (+).
   $$\Sigma F_{y,1} = m_1 a \implies T - m_1 g = m_1 a \quad \text{--- (Persamaan 1)}$$

2. **Analisis Benda 2 ($m_2$ bergerak TURUN):**  
   Arah turun kita beri tanda positif (+).
   $$\Sigma F_{y,2} = m_2 a \implies m_2 g - T = m_2 a \quad \text{--- (Persamaan 2)}$$

3. **Mencari Percepatan Sistem ($a$):**  
   Jumlahkan (Persamaan 1) dan (Persamaan 2) untuk mengeliminasi variabel $T$:
   $$(T - m_1 g) + (m_2 g - T) = m_1 a + m_2 a$$
   $$m_2 g - m_1 g = (m_1 + m_2) a$$
   $$(m_2 - m_1) g = (m_1 + m_2) a$$
   
   $$\bbox[10px,border:2px solid #10b981]{a = \left( \frac{m_2 - m_1}{m_1 + m_2} \right) g}$$

4. **Mencari Tegangan Tali ($T$):**  
   Substitusikan nilai $a$ ke Persamaan 1:
   $$T = m_1 g + m_1 a = m_1 g + m_1 \left( \frac{m_2 - m_1}{m_1 + m_2} \right) g$$
   $$T = m_1 g \left( 1 + \frac{m_2 - m_1}{m_1 + m_2} \right) = m_1 g \left( \frac{m_1 + m_2 + m_2 - m_1}{m_1 + m_2} \right)$$
   
   $$\bbox[10px,border:2px solid #10b981]{T = \left( \frac{2 m_1 m_2}{m_1 + m_2} \right) g}$$

5. **Gaya Pada Poros Katrol ($F_K$):**  
   Poros katrol ditahan oleh penyangga atap. Karena dua utas tali menahan beban ke bawah dengan tegangan masing-masing $T$:
   $$F_K = 2T = \left( \frac{4 m_1 m_2}{m_1 + m_2} \right) g$$

> [!TIP]
> **Cek Logika Fisika (*Limiting Cases Check*):**
> * Kalau $m_1 = m_2 = m \implies a = \frac{0}{2m}g = 0$ (Sistem diam atau bergerak konstan / setimbang!).
> * Kalau $m_1 \ll m_2$ (misal $m_1 \to 0$) $\implies a \to g$ (Benda 2 jatuh bebas seperti tanpa tali!).
> * Besarnya $T$ selalu berada di antara $m_1 g$ dan $m_2 g$ ($m_1 g < T < m_2 g$).

---

## 5. Kombinasi Katrol & Bidang (Datar & Miring, Licin & Kasar) 📐

Sistem banyak benda sering menggabungkan balok yang meluncur di meja/bidang miring dengan beban yang menggantung vertikal.

![[diagram_physics_tegangan_tali_meja_katrol.webp]]

### Kasus A: Bidang Datar & Beban Menggantung

1. **Sub-Kasus Meja Licin:**
   * Balok 1 ($m_1$) di meja licin, Balok 2 ($m_2$) menggantung.
   * Gaya penggerak utama cuma berat beban 2 ($m_2 g$).
   * Persamaan Sistem:
     $$a = \frac{\Sigma F_{\text{penggerak}}}{M_{\text{total}}} = \frac{m_2 g}{m_1 + m_2}$$
     $$T = m_1 a = \frac{m_1 m_2 g}{m_1 + m_2}$$

2. **Sub-Kasus Meja Kasar ($\mu_s$ & $\mu_k$):**
   * Gaya gesek kinetis menahan balok 1: $f_k = \mu_k N_1 = \mu_k m_1 g$.
   * **Syarat gerak:** Supaya sistem bisa jalan dari posisi diam, harus berlaku $m_2 g > f_{s,\max} \implies m_2 > \mu_s m_1$.
   * Kalau bergerak, percepatannya:
     $$a = \frac{m_2 g - \mu_k m_1 g}{m_1 + m_2}$$
     $$T = m_2 (g - a) = m_1 (\mu_k g + a)$$

---

### Kasus B: Bidang Miring Bersudut $\theta$ & Beban Menggantung

![[diagram_physics_tegangan_tali_bidang_miring_katrol.webp]]

Pada bidang miring dengan sudut elevasi $\theta$:
* Urai gaya berat $m_1$: komponen sejajar bidang $w_{1x} = m_1 g \sin \theta$, komponen tegak lurus bidang $w_{1y} = m_1 g \cos \theta \implies N_1 = m_1 g \cos \theta$.

1. **Sub-Kasus Bidang Miring Licin:**
   * Tentukan siapa penarik yang lebih kuat:
     * Jika $m_2 g > m_1 g \sin \theta \implies m_2$ TURUN, $m_1$ NAIK menyusuri bidang miring:
       $$a = \frac{m_2 g - m_1 g \sin \theta}{m_1 + m_2}$$
       $$T = \frac{m_1 m_2 g (1 + \sin \theta)}{m_1 + m_2}$$
     * Jika $m_2 g < m_1 g \sin \theta \implies m_1$ MELUNCUR TURUN bidang miring, $m_2$ NAIK vertikal:
       $$a = \frac{m_1 g \sin \theta - m_2 g}{m_1 + m_2}$$

2. **Sub-Kasus Bidang Miring Kasar ($\mu_k$):**
   * Besar gaya gesek kinetis: $f_k = \mu_k N_1 = \mu_k m_1 g \cos \theta$.
   * Kalau $m_2$ turun ($m_1$ naik bidang), gaya gesek $f_k$ melawan gerak (menunjuk ke bawah bidang):
     $$a = \frac{m_2 g - m_1 g \sin \theta - \mu_k m_1 g \cos \theta}{m_1 + m_2} = \frac{m_2 - m_1 (\sin \theta + \mu_k \cos \theta)}{m_1 + m_2} g$$

---

## 6. Sistem Katrol Bergerak (*Movable Pulley*) & Keuntungan Mekanis ⚙️

### A. Kinematika Terikat (*Constrained Motion*) Katrol Bergerak
Katrol bergerak (*movable pulley*) adalah katrol yang ikut berpindah tempat sewaktu beban diangkat. Coba deh perhatikan strukturnya:

![[diagram_physics_tegangan_tali_katrol_bergerak.webp]]

Panjang tali $L$ yang mengikat sistem memenuhi:
$$L = x_1 + 2 x_2 + \text{konstanta}$$

Diturunkan dua kali terhadap waktu ($t$):
1. **Perpindahan:** $\Delta x_1 = 2 \Delta x_2$ (Ujung tali ditarik 2 meter, katrol bergerak cuma naik 1 meter!).
2. **Kecepatan:** $v_1 = 2 v_2$.
3. **Percepatan:**
   $$\bbox[10px,border:2px solid #3b82f6]{a_1 = 2 a_2 \quad \text{atau} \quad a_2 = \frac{a_1}{2}}$$

> [!IMPORTANT]
> **Aturan Emas Katrol Bergerak:**  
> Beban yang menempel pada katrol bergerak akan bergerak dengan **percepatan setengah** dari percepatan ujung tali bebas yang ditarik ($a_{\text{beban}} = \frac{1}{2} a_{\text{kuasa}}$). Sebagai imbalannya, kamu harus menarik tali **dua kali lebih panjang**!

### B. Analisis Dinamika & Keuntungan Mekanis (*Mechanical Advantage*)
Tinjau gaya pada katrol bergerak ideal ($m_{\text{katrol}} = 0$):
* Ada dua utas tali yang menahan katrol bergerak ke atas dengan tegangan $T$.
* Beban $m_2$ menarik ke bawah dengan gaya $T_2 = m_2 g$.
* Dalam keadaan setimbang:
  $$\Sigma F_y = 0 \implies 2T - T_2 = 0 \implies T = \frac{T_2}{2} = \frac{m_2 g}{2}$$

**Keuntungan Mekanis (KM):**
Keuntungan mekanis adalah perbandingan antara gaya beban yang diangkat dengan gaya kuasa/tarikan yang kita keluarkan:

$$\text{KM} = \frac{F_{\text{beban}}}{F_{\text{kuasa}}} = \frac{m_2 g}{T} = \frac{m_2 g}{\frac{1}{2} m_2 g} = 2$$

> **Mantap kan?** Dengan 1 katrol bergerak, kamu cuma butuh mengeluarkan gaya **setengah dari berat beban**! Beban 100 N bisa diangkat cuma dengan gaya 50 N!

### C. Ringkasan Keuntungan Mekanis Katrol Majemuk (*Takal*)
Pada sistem katrol majemuk (*Block and Tackle System*):
$$\text{KM} = n \quad \text{(dengan } n = \text{jumlah segmen tali yang menopang katrol bergerak)}$$
$$\text{Hubungan Percepatan:} \quad a_{\text{kuasa}} = n \cdot a_{\text{beban}}$$

---

## 7. Cheatsheet Formula & 4 Langkah Emas Problem Solving 🚀

### A. Cheatsheet Ringkas
| Sistem Multi-Body | Percepatan ($a$) | Tegangan Tali ($T$) / Gaya Kontak |
| :--- | :--- | :--- |
| **Balok Berdampingan (Licin)** | $a = \frac{F}{m_1 + m_2 + m_3}$ | $P_{12} = \frac{m_2 + m_3}{m_1 + m_2 + m_3} F$ |
| **Mesin Atwood (Ideal)** | $a = \left(\frac{m_2 - m_1}{m_1 + m_2}\right) g$ | $T = \left(\frac{2 m_1 m_2}{m_1 + m_2}\right) g$ |
| **Meja Datar Licin + Beban Menggantung** | $a = \frac{m_2 g}{m_1 + m_2}$ | $T = \frac{m_1 m_2 g}{m_1 + m_2}$ |
| **Meja Datar Kasar ($\mu_k$) + Beban Menggantung**| $a = \frac{m_2 - \mu_k m_1}{m_1 + m_2} g$ | $T = m_1 (\mu_k g + a)$ |
| **Katrol Bergerak Tunggal** | $a_{\text{tali}} = 2 a_{\text{beban}}$ | $T_{\text{kuasa}} = \frac{1}{2} m_{\text{beban}} g$ (Kondisi Diam) |

---

### B. 4 Langkah Emas Menyelesaikan Soal Dinamika Multi-Body

![[diagram_physics_tegangan_tali_4step_flowchart.webp]]

1. **Langkah 1 (FBD Spasial):** Gambar Diagram Gaya Bebas (*Free Body Diagram*) terpisah untuk tiap massa. Cantumkan semua gaya kontak ($N, T, f, P$) dan gaya berat ($w = mg$).
2. **Langkah 2 (Orientasi Arah):** Tentukan arah "positif" yang konsisten mengikuti alur gerak sistem. (Gaya yang searah gerak diberi tanda positif +).
3. **Langkah 3 (Hukum II Newton per Benda):** Susun persamaan $\Sigma F_i = m_i a_i$. Jika ada katrol bergerak, sertakan hubungan $a_1 = n \cdot a_2$.
4. **Langkah 4 (Substitusi / Eliminasi Aljabar):** Jumlahkan semua persamaan untuk menghilangkan gaya internal ($T$ atau $P$), dapatkan nilai percepatan ($a$), lalu hitung besar tegangan tali!

---

> **Yuk, Refleksi Sejenak!**  
> Fisika itu bukan sekadar menghafal rumus, tapi seni memahami bagaimana alam bekerja. Dari derek pelabuhan raksasa sampai timba sumur tradisional, prinsip gaya tegangan tali dan katrol membuktikan bahwa dengan sedikit trik fisika, beban seberat apa pun bisa kita taklukkan. *Keep practicing, stay curious, and enjoy physics!* 🚀✨

---

## 📝 Navigasi Modul & Lembar Kerja Terkait
* **Navigasi Topic Dinamika Gerak:**
  - 🏠 [[Dinamika_Gerak_SMA|Master Dashboard Dinamika Gerak]]
  - 📄 [[Gaya_Berat_SMA|Modul 1: Gaya Berat]]
  - 📄 [[Gaya_Normal_SMA|Modul 2: Gaya Normal]]
  - 📄 [[Gaya_Gesek_SMA|Modul 3: Gaya Gesek]]
  - 📄 [[Gaya_Sentripetal_SMA|Modul 5: Gaya Sentripetal]]
* **Lembar Kerja & Soal Evaluasi:**
  - 📝 [[LKPD_Gaya_Tegangan_Tali_dan_Katrol_SMA]]
  - 📝 [[LKPD_Dinamika_Gerak_SMA]] (LKPD Terpadu)
  - 🍎 [[index_teaching|Teaching Resources Hub]]
