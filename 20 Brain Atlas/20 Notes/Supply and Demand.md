---
type: note
title: "Supply and Demand"
subject: "Economics"
created: 2026-09-05
prerequisites:
  - "[[Scarcity and Opportunity Cost]]"
tags:
  - economics
  - microeconomics
  - markets
---

Supply and Demand (penawaran dan permintaan) adalah model ekonomi mikro fundamental yang mendeskripsikan bagaimana interaksi antara konsumen (pembeli) dan produsen (penjual) di pasar kompetitif menentukan harga wajar suatu barang (*market price*) serta total kuantitas yang ditransaksikan. Model ini menunjukkan bagaimana sistem harga terdesentralisasi berfungsi sebagai sinyal informasi efisien untuk menyelesaikan masalah [[Scarcity and Opportunity Cost|kelangkaan sumber daya]] tanpa memerlukan otoritas perencana terpusat. Ketika pasar berada pada titik ekuilibrium, alokasi sumber daya mencapai efisiensi maksimal di mana surplus ekonomi total dimaksimalkan.

![[chart_economics_supply_demand_equilibrium.webp]]

## Teori Permintaan (Demand) & Kesediaan Membayar

Permintaan mencerminkan sejumlah barang atau jasa yang ingin dan mampu dibeli oleh konsumen pada berbagai tingkat harga dalam periode tertentu, dengan asumsi faktor lain konstan (*ceteris paribus*).

Kurva permintaan melandai turun dari kiri atas ke kanan bawah sesuai dengan **Hukum Permintaan (*Law of Demand*)**: semakin tinggi harga suatu barang ($P \uparrow$), semakin sedikit kuantitas yang diminta konsumen ($Q_d \downarrow$), dan sebaliknya. Fondasi dari hukum ini berakar pada:
1. **Diminishing Marginal Utility:** Setiap tambahan unit konsumsi memberikan kepuasan tambahan (*marginal utility*) yang semakin menurun, sehingga konsumen hanya bersedia membeli unit tambahan jika harganya lebih murah.
2. **Efek Substitusi (*Substitution Effect*):** Kenaikan harga barang membuat barang substitusinya relatif lebih murah, mendorong konsumen beralih ke barang alternatif.
3. **Efek Pendapatan (*Income Effect*):** Kenaikan harga menurunkan daya beli riil pendapatan nominal konsumen.

### Formulasi Matematis Permintaan
Bentuk fungsi permintaan linear umum:
$$ Q_d = a - bP $$

Fungsi permintaan invers (*Inverse Demand Function*):
$$ P = \frac{a}{b} - \frac{1}{b}Q_d $$

* **Variabel & Legenda:**
  * $Q_d$: Kuantitas barang yang diminta oleh konsumen.
  * $P$: Tingkat harga barang.
  * $a$: Kuantitas otonom (jumlah barang yang diminta ketika $P = 0$).
  * $b$: Koefisien sensitivitas respon kuantitas terhadap perubahan harga ($b = \left|\frac{dQ_d}{dP}\right| > 0$).
  * $\frac{1}{b}$: Kemiringan (*slope*) dari kurva permintaan invers.

## Teori Penawaran (Supply) & Biaya Marjinal

Penawaran merepresentasikan sejumlah barang atau jasa yang bersedia dan mampu diproduksi serta dijual oleh produsen pada berbagai tingkat harga dalam periode tertentu (*ceteris paribus*).

Kurva penawaran melandai naik dari kiri bawah ke kanan atas mengikuti **Hukum Penawaran (*Law of Supply*)**: semakin tinggi harga barang ($P \uparrow$), semakin banyak kuantitas yang ditawarkan produsen ($Q_s \uparrow$). Kurva penawaran sebuah perusahaan kompetitif pada dasarnya adalah bagian dari kurva **Biaya Marjinal (*Marginal Cost - MC*)** di atas titik tutup usaha (*shutdown point*). Karena produsen menghadapi hukum hasil lebih yang semakin berkurang (*law of diminishing marginal returns*), biaya untuk memproduksi satu unit tambahan cenderung meningkat, sehingga produsen memerlukan harga pasar yang lebih tinggi untuk menutupi biaya marjinal tersebut.

### Formulasi Matematis Penawaran
Bentuk fungsi penawaran linear umum:
$$ Q_s = c + dP $$

Fungsi penawaran invers (*Inverse Supply Function*):
$$ P = -\frac{c}{d} + \frac{1}{d}Q_s $$

* **Variabel & Legenda:**
  * $Q_s$: Kuantitas barang yang ditawarkan oleh produsen.
  * $P$: Tingkat harga barang di pasar.
  * $c$: Kuantitas dasar yang ditawarkan saat harga nol ($c$ bisa bernilai negatif yang menandakan produsen baru mau berproduksi jika harga berada di atas ambang minimum tertentu).
  * $d$: Koefisien sensitivitas respon penawaran terhadap harga ($d = \frac{dQ_s}{dP} > 0$).

## Ekuilibrium Pasar dan Mekanisme Pembersihan (*Market Clearing*)

Ekuilibrium pasar (*market equilibrium*) tercapai pada tingkat harga di mana kuantitas yang diminta oleh konsumen tepat sama dengan kuantitas yang bersedia ditawarkan oleh produsen:

$$ Q_d(P^*) = Q_s(P^*) = Q^* $$

Pada kondisi ini, pasar berada dalam keadaan bersih (*market clears*), tidak ada barang yang tersisa (*no surplus*) dan tidak ada konsumen yang kehabisan barang (*no shortage*).

### Dinamika Disekuilibrium
Jika pasar berada di luar harga ekuilibrium ($P \neq P^*$), mekanisme harga bekerja otomatis mengembalikan posisi ke titik $E$:

* **Kelebihan Penawaran (*Surplus / Excess Supply*):** Terjadi jika $P > P^*$, di mana $Q_s > Q_d$. Produsen menumpuk stok inventaris yang tak terjual. Untuk memotong kerugian, produsen bersaing menurunkan harga, mendorong kenaikan permintaan hingga kembali ke $P^*$.
* **Kelebihan Permintaan (*Shortage / Excess Demand*):** Terjadi jika $P < P^*$, di mana $Q_d > Q_s$. Terjadi antrean panjang dan kelangkaan barang di tingkat konsumen. Konsumen bersedia menawar dengan harga lebih tinggi, memberi insentif bagi produsen untuk menaikkan harga dan menambah produksi hingga kembali ke $P^*$.

## Movement Along the Curve vs. Shift of the Curve

Salah satu kesalahan paling fatal dalam analisis ekonomi adalah menyamakan perubahan jumlah yang diminta/ditawarkan dengan perubahan permintaan/penawaran itu sendiri.

![[diagram_economics_movement_vs_shift.webp]]

| Aspek | Movement Along the Curve | Shift of the Curve |
| :--- | :--- | :--- |
| **Definisi** | Pergerakan dari satu titik ke titik lain pada satu kurva yang sama. | Pergeseran seluruh garis kurva ke kanan (bertambah) atau ke kiri (berkurang). |
| **Penyebab Utama** | **Hanya** disebabkan oleh perubahan **Harga Barang Itu Sendiri ($P$)**. | Disebabkan oleh perubahan faktor **Non-Harga (Faktor Eksogen)**. |
| **Notasi Istilah** | Perubahan *Kuantitas yang Diminta / Ditawarkan* ($\Delta Q_d$ atau $\Delta Q_s$). | Perubahan *Permintaan / Penawaran* ($\Delta D$ atau $\Delta S$). |

### Faktor-Faktor Penggeser Kurva (Shifters):

1. **Penggeser Kurva Permintaan ($D$):**
   * **Pendapatan Konsumen:** Untuk barang normal, kenaikan pendapatan menggeser kurva ke kanan ($D \uparrow$). Untuk barang inferior, kenaikan pendapatan menggeser kurva ke kiri ($D \downarrow$).
   * **Harga Barang Terkait:** Kenaikan harga barang substitusi (misal kopi naik) menggeser kurva permintaan teh ke kanan. Kenaikan harga barang komplementer (misal bensin naik) menggeser permintaan mobil ke kiri.
   * **Selera & Preferensi:** Tren positif menggeser kurva ke kanan.
   * **Ekspektasi Masa Depan:** Dugaan harga barang akan naik besok mendorong belanja hari ini ($D \uparrow$).
   * **Jumlah Populasi Pembeli:** Pertumbuhan populasi menggeser kurva pasar ke kanan.

2. **Penggeser Kurva Penawaran ($S$):**
   * **Harga Input / Biaya Produksi:** Kenaikan upah buruh atau harga bahan baku meningkatkan biaya marjinal, menggeser kurva ke kiri ($S \downarrow$).
   * **Kemajuan Teknologi:** Inovasi mesin atau otomatisasi menekan biaya produksi, menggeser kurva ke kanan ($S \uparrow$).
   * **Pajak dan Subsidi Pemerintah:** Pajak per unit menggeser kurva penawaran ke atas/kiri; subsidi menggeser ke bawah/kanan.
   * **Ekspektasi Penjual & Jumlah Produsen:** Masuknya pemain industri baru memperbesar kapasitas penawaran pasar ($S \uparrow$).

## Efisiensi Kesejahteraan: Surplus Konsumen & Produsen

Pasar persaingan sempurna pada titik ekuilibrium memaksimalkan total surplus ekonomi (*Total Social Welfare*), mewujudkan efisiensi alokatif:

$$ \text{Total Welfare} (W) = \text{Consumer Surplus} (CS) + \text{Producer Surplus} (PS) $$

* **Consumer Surplus ($CS$):** Selisih antara kesediaan maksimum konsumen untuk membayar (*willingness to pay*) dengan harga aktual yang dibayarkan di pasar. Secara geometris, $CS$ adalah area segitiga di bawah kurva permintaan dan di atas garis harga ekuilibrium $P^*$:
  $$ CS = \int_0^{Q^*} (P_d(Q) - P^*) \, dQ $$
* **Producer Surplus ($PS$):** Selisih antara harga aktual yang diterima produsen dengan biaya marjinal minimum yang bersedia mereka terima. Secara geometris, $PS$ adalah area segitiga di atas kurva penawaran dan di bawah garis harga ekuilibrium $P^*$:
  $$ PS = \int_0^{Q^*} (P^* - P_s(Q)) \, dQ $$

Setiap intervensi buatan yang mendistorsi harga di luar $P^*$ (seperti kontrol harga *price ceiling* atau *price floor*) akan memangkas transaksi efisien dan melahirkan **Deadweight Loss ($DWL$)**, yaitu hilangnya surplus ekonomi yang tidak dinikmati oleh pihak mana pun.

---

## Worked Example: Kalkulasi Kuantitatif Ekuilibrium Pasar

Misalkan sebuah pasar komoditas memiliki fungsi permintaan dan penawaran sebagai berikut:
$$ Q_d = 500 - 4P $$
$$ Q_s = -100 + 6P $$

### 1. Menentukan Harga dan Kuantitas Ekuilibrium
Set kondisi ekuilibrium $Q_d = Q_s$:
$$ 500 - 4P = -100 + 6P $$
$$ 600 = 10P \implies P^* = 60 $$

Substitusikan $P^* = 60$ ke salah satu fungsi:
$$ Q^* = 500 - 4(60) = 500 - 240 = 260 \text{ unit} $$

### 2. Menghitung Consumer Surplus ($CS$) dan Producer Surplus ($PS$)
* **Cari harga reservasi permintaan (saat $Q_d = 0$):**
  $$ 0 = 500 - 4P_{max} \implies P_{max} = 125 $$
* **Cari harga minimum penawaran (saat $Q_s = 0$):**
  $$ 0 = -100 + 6P_{min} \implies P_{min} = \frac{100}{6} \approx 16{,}67 $$

* **Hitung $CS$:**
  $$ CS = \frac{1}{2} \times (P_{max} - P^*) \times Q^* = \frac{1}{2} \times (125 - 60) \times 260 = \frac{1}{2} \times 65 \times 260 = 8.450 $$
* **Hitung $PS$:**
  $$ PS = \frac{1}{2} \times (P^* - P_{min}) \times Q^* = \frac{1}{2} \times (60 - 16{,}67) \times 260 = \frac{1}{2} \times 43{,}33 \times 260 = 5.633{,}33 $$

Total Welfare pasar:
$$ W = CS + PS = 8.450 + 5.633{,}33 = 14.083{,}33 $$

---

> [!abstract]- Quick Reference
> * **Hukum Permintaan:** $P \uparrow \implies Q_d \downarrow$ (kemiringan negatif, didorong *diminishing marginal utility*).
> * **Hukum Penawaran:** $P \uparrow \implies Q_s \uparrow$ (kemiringan positif, didorong *increasing marginal cost*).
> * **Kondisi Ekuilibrium:** $Q_d(P^*) = Q_s(P^*)$.
> * **Surplus vs Shortage:** 
>   * $P > P^* \implies Q_s > Q_d$ (*Surplus*, harga tertekan turun).
>   * $P < P^* \implies Q_d > Q_s$ (*Shortage*, harga terdorong naik).
> * **Movement vs Shift:** Perubahan harga barang sendiri = *Movement along curve*; Perubahan faktor non-harga = *Shift of curve*.
> * **Efisiensi Alokatif:** Tercapai saat $P = MC$, memaksimalkan $CS + PS$ tanpa *deadweight loss*.

> [!question]- Practice
> **Soal 1:** Berdasarkan persamaan pasar pada contoh di atas ($Q_d = 500 - 4P$ dan $Q_s = -100 + 6P$), pemerintah menetapkan kebijakan harga batas atas (*Price Ceiling*) sebesar $P_c = 40$ untuk melindungi konsumen dari harga mahal.
> 1. Apakah terjadi kelebihan penawaran (*surplus*) atau kelebihan permintaan (*shortage*)? Berapa besarannya?
> 2. Berapa kuantitas riil yang benar-benar ditransaksikan di pasar setelah kebijakan tersebut?
> 
> > [!check]- Answer
> > **Langkah 1: Substitusikan $P_c = 40$ ke fungsi permintaan dan penawaran:**
> > $$ Q_d(40) = 500 - 4(40) = 500 - 160 = 340 \text{ unit} $$
> > $$ Q_s(40) = -100 + 6(40) = -100 + 240 = 140 \text{ unit} $$
> > 
> > **Langkah 2: Evaluasi Disekuilibrium:**
> > Karena $Q_d (340) > Q_s (140)$, terjadi **Kelebihan Permintaan (*Shortage*)**.
> > $$ \text{Besar Shortage} = Q_d - Q_s = 340 - 140 = 200 \text{ unit} $$
> > 
> > **Langkah 3: Kuantitas Transaksi Riil:**
> > Transaksi pasar dibatasi oleh sisi yang lebih pendek (*short-side rule*):
> > $$ Q_{transaksi} = \min(Q_d, Q_s) = \min(340, 140) = 140 \text{ unit} $$
> > Meskipun ada 340 permintaan, hanya 140 unit yang bersedia disediakan oleh produsen pada harga Rp 40. Kebijakan ini justru menurunkan kuantitas yang tersedia bagi publik dari semula 260 unit menjadi 140 unit, menciptakan antrean/pasar gelap dan *deadweight loss*.

> [!info]- Going Deeper
> * **The Use of Knowledge in Society (Friedrich Hayek - 1945):** Hayek berargumen bahwa harga pasar bukan sekadar alat pembayaran, melainkan mekanisme telekomunikasi terdesentralisasi yang merangkum miliaran bit informasi lokal yang tersebar. Tidak ada badan perencana pusat yang mampu meniru efisiensi adaptasi harga dalam merespon perubahan selera dan teknologi secara seketika.
> * **Walrasian vs Marshallian Price Adjustment:** Léon Walras memandang ekuilibrium tercapai lewat penyesuaian harga ketika terjadi selisih kuantitas (*tâtonnement* kuantitas mendorong harga). Sebaliknya, Alfred Marshall memandang produsen menyesuaikan kuantitas output berdasarkan selisih harga penawaran dan harga permintaan.
> * **Anomali Hukum Permintaan (Exceptions to Law of Demand):** 
>   * *Giffen Goods:* Barang inferior ekstrem di mana efek pendapatan negatif melebihi efek substitusi, sehingga ketika harga naik, konsumsi justru bertambah (misal kentang saat kelaparan besar di Irlandia).
>   * *Veblen Goods:* Barang mewah konsumsi mencolok (*conspicuous consumption*) di mana harga tinggi justru menaikkan status dan utilitas sosial pembelinya.
> * **Topik Lanjutan:** Lanjutkan pemahaman derajat sensitivitas kurva ke topik *Elasticity* (Elastisitas Harga Permintaan & Penawaran).
