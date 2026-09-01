---
title: "Perbandingan Trigonometri dan Sudut Istimewa SMA"
type: materi
subject: Mathematics
level: sma
target_audience: "Siswa SMA Kelas 10 (Fase E), Guru Matematika, dan Pembelajar Mandiri"
created: 2026-09-01
sources:
  - "[[Trigonometri_SMA]]"
  - "[[Sudut_Berelasi_dan_Lingkaran_Satuan_SMA]]"
  - "[[LKPD_Trigonometri_SMA]]"
tags:
  - teaching/mathematics
  - mathematics/trigonometry
  - level/sma
  - topic/right-triangle-trig
---

> **Bilah Navigasi:**
> [[Trigonometri_SMA|🏠 Master Dashboard]] | **Modul 1: Rasio Dasar** | [[Sudut_Berelasi_dan_Lingkaran_Satuan_SMA|Modul 2: Sudut Berelasi ➡️]] | [[LKPD_Trigonometri_SMA|📝 LKPD]]

---

# Perbandingan Trigonometri dan Sudut Istimewa — Mengukur Dunia Lewat Rasio Segitiga 📐🏔️

Pernahkah kamu membayangkan bagaimana matematikawan dan surveyor zaman dulu bisa mengetahui tinggi Gunung Everest ($8.848\text{ m}$) atau jarak kapal di tengah laut lepas tanpa harus menarik pita meteran raksasa? Rahasianya ada pada satu prinsip geometris elegan: **kesebangunan pada segitiga siku-siku**. 

Kata **Trigonometri** berasal dari bahasa Yunani: *Trigonon* (tiga sudut/segitiga) dan *Metron* (pengukuran). Begitu satu sudut pada segitiga siku-siku terkunci, perbandingan antarpanjang sisinya akan selalu bernilai **tetap**, tidak peduli seberapa besar atau kecil ukuran segitiga tersebut diperbesar!

---

## 1. Anatomi Segitiga Siku-Siku & Nomenklatur Sisi

Perhatikan segitiga siku-siku $\triangle ABC$ dengan siku-siku di $C$ dan sudut acuan sebesar $\theta$ berada di titik sudut $A$.

![[diagram_mathematics_trigonometry_right_triangle.webp]]

Berdasarkan posisi sudut acuan $\theta$:
1. **Sisi Depan (Opposite / De):** Sisi yang berada persis di depan/seberang sudut $\theta$, yaitu sisi $BC$ (panjang $a$).
2. **Sisi Samping (Adjacent / Sa):** Sisi yang menempel langsung membentuk sudut $\theta$ selain sisi miring, yaitu sisi $AC$ (panjang $b$).
3. **Sisi Miring (Hypotenuse / Mi):** Sisi terpanjang yang selalu berada di hadapan sudut siku-siku $90^\circ$, yaitu sisi $AB$ (panjang $c$).

> [!WARNING]
> **Awas Jebakan Posisi Sudut!**
> Sisi "depan" dan "samping" tidaklah absolut, melainkan bergantung penuh pada **di mana sudut acuan $\theta$ diletakkan**. Jika sudut acuan dipindah ke titik $B$ ($\angle B = \beta$), maka sisi depannya berubah menjadi $AC$ dan sisi sampingnya menjadi $BC$. Namun, sisi miring (hipotenusa) **selalu tetap** berada di hadapan sudut siku-siku $90^\circ$.

---

## 2. Enam Rasio Trigonometri Dasar

Ada enam kemungkinan rasio perbandingan antara pasangan sisi-sisi segitiga siku-siku tersebut:

### A. Tiga Rasio Utama (Primary Ratios)

1. **Sinus ($\sin \theta$):** Perbandingan sisi depan terhadap sisi miring.
   $$\sin \theta = \frac{\text{Depan}}{\text{Miring}} = \frac{\text{De}}{\text{Mi}} = \frac{a}{c}$$
   *(Jembatan Keledai: **Sin-De-Mi**)*

2. **Kosinus ($\cos \theta$):** Perbandingan sisi samping terhadap sisi miring.
   $$\cos \theta = \frac{\text{Samping}}{\text{Miring}} = \frac{\text{Sa}}{\text{Mi}} = \frac{b}{c}$$
   *(Jembatan Keledai: **Cos-Sa-Mi**)*

3. **Tangen ($\tan \theta$):** Perbandingan sisi depan terhadap sisi samping.
   $$\tan \theta = \frac{\text{Depan}}{\text{Samping}} = \frac{\text{De}}{\text{Sa}} = \frac{a}{b}$$
   *(Jembatan Keledai: **Tan-De-Sa**)*

Hubungan penting:
$$\tan \theta = \frac{\sin \theta}{\cos \theta} = \frac{a/c}{b/c} = \frac{a}{b}$$

---

### B. Tiga Rasio Kebalikan (Reciprocal Ratios)

Tiga fungsi lainnya merupakan kebalikan (*multiplicative inverse*) langsung dari fungsi utama:

1. **Kosekan ($\csc \theta$ atau $\operatorname{cosec} \theta$):** Kebalikan dari Sinus.
   $$\csc \theta = \frac{1}{\sin \theta} = \frac{\text{Miring}}{\text{Depan}} = \frac{\text{Mi}}{\text{De}} = \frac{c}{a}$$

2. **Sekan ($\sec \theta$):** Kebalikan dari Kosinus.
   $$\sec \theta = \frac{1}{\cos \theta} = \frac{\text{Miring}}{\text{Samping}} = \frac{\text{Mi}}{\text{Sa}} = \frac{c}{b}$$

3. **Kotangen ($\cot \theta$):** Kebalikan dari Tangen.
   $$\cot \theta = \frac{1}{\tan \theta} = \frac{\text{Samping}}{\text{Depan}} = \frac{\text{Sa}}{\text{De}} = \frac{b}{a} = \frac{\cos \theta}{\sin \theta}$$

---

## 3. Mengapa Rasio Ini Bernilai Konstan? (Bukti Kesebangunan)

Bayangkan kita memiliki dua segitiga siku-siku dengan sudut lancip yang sama besar $\theta$, satu segitiga kecil $\triangle ABC$ dan satu segitiga raksasa $\triangle ADE$.

Berdasarkan dalil kesebangunan segitiga (*Sudut-Sudut-Sudut* atau $AAA$), jika dua pasang sudut bersesuaian sama besar ($90^\circ$ dan $\theta$), maka kedua segitiga tersebut **sebangun** ($\triangle ABC \sim \triangle ADE$).

Konsekuensinya, rasio sisi-sisi yang bersesuaian selalu sebanding:
$$\frac{BC}{AB} = \frac{DE}{AD} \implies \sin \theta \text{ segitiga kecil} = \sin \theta \text{ segitiga besar}$$

Artinya, nilai trigonometri **murni merupakan karakteristik sudut $\theta$**, bukan ukuran fisik bangunannya!

---

## 4. Deduksi Geometris Nilai Eksak Sudut Istimewa ($0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$)

Nilai sudut istimewa tidak boleh sekadar dihafal mati seperti mantra, melainkan dipahami asal-usul pembuktian geometrisnya.

### A. Sudut $45^\circ$ (Deduksi dari Segitiga Siku-Siku Sama Kaki)

Buat sebuah persegi dengan panjang sisi $1\text{ satuan}$, lalu potong secara diagonal. Kita memperoleh segitiga siku-siku sama kaki dengan sudut $45^\circ - 45^\circ - 90^\circ$.
* $\text{Sisi Depan} = 1$
* $\text{Sisi Samping} = 1$
* Menurut Teorema Pythagoras: $\text{Sisi Miring} = \sqrt{1^2 + 1^2} = \sqrt{2}$

Maka:
* $\sin 45^\circ = \frac{1}{\sqrt{2}} = \frac{1}{2}\sqrt{2}$
* $\cos 45^\circ = \frac{1}{\sqrt{2}} = \frac{1}{2}\sqrt{2}$
* $\tan 45^\circ = \frac{1}{1} = 1$

---

### B. Sudut $30^\circ$ dan $60^\circ$ (Deduksi dari Segitiga Sama Sisi)

Buat segitiga sama sisi dengan panjang setiap sisi $2\text{ satuan}$ (semua sudutnya $60^\circ$). Tarik garis tinggi dari salah satu titik puncak ke alas, sehingga membagi segitiga menjadi dua segitiga siku-siku simetris dengan sudut $30^\circ - 60^\circ - 90^\circ$.
* Panjang alas terbelah menjadi $1\text{ satuan}$.
* Panjang sisi miring tetap $2\text{ satuan}$.
* Tinggi segitiga dihitung dengan Pythagoras: $t = \sqrt{2^2 - 1^2} = \sqrt{3}$.

> [!NOTE]
> **Rasio Sisi Segitiga $30^\circ - 60^\circ - 90^\circ$:**
> $$\text{Panjang Sisi} \implies \text{Depan } 30^\circ : \text{Samping } 30^\circ : \text{Miring} = 1 : \sqrt{3} : 2$$

Dari sudut pandang $30^\circ$:
* $\text{Depan} = 1, \quad \text{Samping} = \sqrt{3}, \quad \text{Miring} = 2$
* $\sin 30^\circ = \frac{1}{2}$
* $\cos 30^\circ = \frac{\sqrt{3}}{2} = \frac{1}{2}\sqrt{3}$
* $\tan 30^\circ = \frac{1}{\sqrt{3}} = \frac{1}{3}\sqrt{3}$

Dari sudut pandang $60^\circ$:
* $\text{Depan} = \sqrt{3}, \quad \text{Samping} = 1, \quad \text{Miring} = 2$
* $\sin 60^\circ = \frac{\sqrt{3}}{2} = \frac{1}{2}\sqrt{3}$
* $\cos 60^\circ = \frac{1}{2}$
* $\tan 60^\circ = \frac{\sqrt{3}}{1} = \sqrt{3}$

---

### C. Sudut Ekstrem $0^\circ$ dan $90^\circ$ (Pendekatan Batas/Limit)

* **Ketika $\theta \to 0^\circ$:** Sisi depan memendek hingga mendekati $0$, sedangkan sisi samping panjangnya berhimpit dengan sisi miring ($\text{Sa} \to \text{Mi}$).
  $$\sin 0^\circ = \frac{0}{\text{Mi}} = 0, \quad \cos 0^\circ = \frac{\text{Mi}}{\text{Mi}} = 1, \quad \tan 0^\circ = \frac{0}{\text{Mi}} = 0$$
* **Ketika $\theta \to 90^\circ$:** Sisi depan berhimpit memanjang menyamai sisi miring ($\text{De} \to \text{Mi}$), sedangkan sisi samping lenyap mendekati $0$.
  $$\sin 90^\circ = \frac{\text{Mi}}{\text{Mi}} = 1, \quad \cos 90^\circ = \frac{0}{\text{Mi}} = 0, \quad \tan 90^\circ = \frac{\text{Mi}}{0} \to \text{Tak Terdefinisi} \ (\infty)$$

---

## 5. Aplikasi Nyata: Klinometer, Sudut Elevasi & Sudut Depresi

Dalam pengukuran geodesi dan kehidupan nyata, kita mengenal dua garis pandang:

![[diagram_mathematics_trigonometry_elevation_depression.webp]]

1. **Sudut Elevasi ($\alpha$):** Sudut yang dibentuk oleh garis horizontal bidang mata pengamat ke arah **atas** menuju puncak objek sasaran.
2. **Sudut Depresi ($\beta$):** Sudut yang dibentuk oleh garis horizontal bidang mata pengamat ke arah **bawah** menuju dasar/objek sasaran di bawah.

> [!IMPORTANT]
> **Rumus Mengukur Tinggi Objek (Klinometer):**
> Jika seorang pengamat dengan tinggi mata $h_{\text{mata}}$ berdiri sejauh $d$ dari kaki gedung dan memandang puncak gedung dengan sudut elevasi $\alpha$:
> $$\mathbf{\text{Tinggi Total Gedung } (H) = h_{\text{mata}} + (d \cdot \tan \alpha)}$$

---

## 6. Contoh Soal Berpola & Pembahasan Tuntas

### Contoh 1: Menentukan Rasio Lain dari Satu Rasio yang Diketahui
**Soal:** Diketahui $\tan \alpha = \frac{5}{12}$ dan $\alpha$ adalah sudut lancip. Tentukan nilai dari $\sin \alpha$, $\cos \alpha$, dan $\sec \alpha$.

**Langkah Penyelesaian:**
1. Berdasarkan definisi $\tan \alpha = \frac{\text{De}}{\text{Sa}} = \frac{5}{12}$, kita tetapkan:
   $$\text{Depan} = 5, \quad \text{Samping} = 12$$
2. Hitung sisi miring ($\text{Mi}$) menggunakan dalil Pythagoras:
   $$\text{Mi} = \sqrt{\text{De}^2 + \text{Sa}^2} = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$$
3. Evaluasi rasio yang diminta:
   $$\sin \alpha = \frac{\text{De}}{\text{Mi}} = \frac{5}{13}$$
   $$\cos \alpha = \frac{\text{Sa}}{\text{Mi}} = \frac{12}{13}$$
   $$\sec \alpha = \frac{1}{\cos \alpha} = \frac{13}{12}$$

---

### Contoh 2: Aplikasi Klinometer Mengukur Tinggi Tiang Bendera
**Soal:** Rian berdiri sejauh $15\text{ meter}$ dari tiang bendera. Dengan alat klinometer, ia mengukur sudut elevasi ke puncak tiang bendera sebesar $60^\circ$. Jika tinggi mata Rian dari tanah adalah $160\text{ cm}$ ($1,6\text{ m}$), berapa tinggi total tiang bendera tersebut?

**Langkah Penyelesaian:**
1. Identifikasi variabel:
   $$d = 15\text{ m}, \quad \alpha = 60^\circ, \quad h_{\text{mata}} = 1,6\text{ m}$$
2. Hitung tinggi segitiga di atas garis pandang ($y$):
   $$\tan 60^\circ = \frac{y}{d} \implies y = d \cdot \tan 60^\circ = 15 \cdot \sqrt{3} \approx 15 \cdot 1,732 = 25,98\text{ m}$$
3. Jumlahkan dengan tinggi badan/mata pengamat:
   $$H_{\text{total}} = y + h_{\text{mata}} = (15\sqrt{3} + 1,6)\text{ m} \approx 27,58\text{ m}$$

---

## 7. Ringkasan Konsep Inti

* Rasio trigonometri segitiga siku-siku beroperasi pada tiga komponen: $\text{De}$ (Depan), $\text{Sa}$ (Samping), dan $\text{Mi}$ (Miring).
* Kunci ingatan instan: **Sindemi**, **Cossami**, **Tandesa**.
* Sudut istimewa $30^\circ, 45^\circ, 60^\circ$ diturunkan secara eksak dari sifat simetri persegi dan segitiga sama sisi.
* Pada aplikasi lapangan, selalu tambahkan tinggi mata pengamat pada perhitungan tinggi total berbasis $\tan \alpha$.

---

> **Bilah Navigasi:**
> [[Trigonometri_SMA|🏠 Master Dashboard]] | **Modul 1: Rasio Dasar** | [[Sudut_Berelasi_dan_Lingkaran_Satuan_SMA|Modul 2: Sudut Berelasi ➡️]] | [[LKPD_Trigonometri_SMA|📝 LKPD]]
