---
title: "Sinyal Bioelektrik (EKG, EEG, EMG)"
course: "Komputasi Biomedik"
course_abbr: "BIOCOMP"
semester: 5
week: 2
date: "2026-08-27"
tags: ["biomedical-computing", "bioelectric-signals", "ecg", "eeg", "emg"]
type: "LectureNote"
---

# Sinyal Bioelektrik (EKG, EEG, EMG)

Sinyal bioelektrik merupakan perubahan potensial listrik yang dihasilkan oleh aktivitas elektrokimia pada membran sel biologis, khususnya sel yang dapat terangsang (*excitable cells*) seperti sel otot (*myocytes*) dan sel saraf (*neurons*). Dalam disiplin [[Komputasi Biomedis]], perekaman dan analisis sinyal bioelektrik—meliputi Elektrokardiografi (EKG), Elektroensefalografi (EEG), dan Elektromiografi (EMG)—menjadi fondasi utama instrumen diagnostik non-invasif modern.

---

## 1. Elektrokardiogram (EKG / ECG)

Elektrokardiogram adalah modalitas rekaman biopotensial yang mengukur grafik tegangan terhadap waktu dari aktivitas kelistrikan jantung. Sinyal EKG ditangkap melalui elektroda sadapan (*leads*) yang dipasang pada permukaan kulit dada dan ekstremitas.

### 1.1 Fisiologi Elektrik, Prosedur & Akuisisi Sinyal
Kelistrikan jantung diinisiasi secara spontan oleh **Nodus Sinoatrial (SA Node)** sebagai *pacemaker* alami. Depolarisasi merambat melalui atrium menuju **Nodus Atrioventrikular (AV Node)**, mengalami penundaan singkat untuk pengisian ventrikel, kemudian diteruskan melalui **Berkas His**, **Cabang Berkas (Bundle Branches)**, dan **Serabut Purkinje** untuk memicu kontraksi ventrikel.

> [!NOTE]
> **Prosedur & Persiapan Pasien EKG**:
> - Pasien diminta berbaring rileks, melepaskan baju bagian atas, dan melepaskan seluruh perhiasan/benda logam yang dikenakan (mencegah *metal interference*).
> - Elektroda ditempelkan di dada (V1-V6) serta ekstremitas lengan dan tungkai.
> - Pasien **dilarang banyak bergerak atau berbicara** selama perekaman sinyal berlangsung karena pergerakan otot tubuh/dada memicu artefak sinyal (*EMG noise artifact*) yang dapat mengdistorsi bentuk gelombang EKG.

Perekaman EKG dipetakan dalam koordinat Cartesian:
- **Sumbu Y (Amplitudo):** Mengukur tegangan listrik dalam milivolt ($\text{mV}$). Kalibrasi standar adalah $1\text{ mV} = 10\text{ mm}$ (dua kotak besar vertikal).
- **Sumbu X (Waktu):** Mengukur durasi waktu dalam detik ($\text{s}$). Pada kecepatan kertas $25\text{ mm/s}$:
  - $1\text{ kotak kecil } (1\text{ mm}) = 0.04\text{ s}$
  - $1\text{ kotak besar } (5\text{ mm}) = 0.20\text{ s}$

![[diagram_college_biocomp_ecg_waveform_anatomy.webp]]

### 1.2 Anatomi Gelombang & Segmen Sinyal EKG

| Komponen / Parameter | Definisi Elektrofisiologis | Nilai Normal & Karakteristik |
| :--- | :--- | :--- |
| **Gelombang P (*P Wave*)** | Depolarisasi sekuensial atrium kanan dan kiri (*atrial depolarisation*). | Durasi: $< 0.12\text{ s}$, Amplitudo: $< 0.25\text{ mV}$. Morphologi bundar simetris. |
| **Kompleks QRS (*QRS Complex*)** | Depolarisasi ventrikel kanan dan kiri secara simultan (*ventricular depolarisation*). Repolarisasi atrium tertutup oleh kompleks ini. | Durasi: $0.06 - 0.10\text{ s}$. Gelombang Q (defleksi negative awal), R (defleksi positif), S (defleksi negatif pasca R). |
| **Gelombang T (*T Wave*)** | Repolarisasi ventrikel (*ventricular repolarisation*). | Amplitudo asimetris dengan puncak melengkung halus. Orientasi searah dengan kompleks QRS. |
| **Segmen ST (*ST Segment*)** | Fase isoelektrik antara akhir depolarisasi ventrikel dan awal repolarisasi ventrikel (fase plato potensial aksi miokard). | Berada pada garis basis (*isoelectric line*). Penyimpangan $\ge 1\text{ mm}$ mengindikasikan patologi iskemia/infark. |
| **Gelombang U (*U Wave*)** | Depolarisasi lambat pada serabut Purkinje atau otot papilaris saat permulaan diastole. | Tampak kecil pasca gelombang T. Terlihat jelas pada kondisi hipokalemia. |
| **Interval PR (*PR Interval*)** | Waktu awal depolarisasi atrium hingga awal depolarisasi ventrikel (mencakup konduksi nodus AV). | Durasi normal: $0.12 - 0.20\text{ s}$ ($3 - 5\text{ kotak kecil}$). Pemanjangan menandakan blok AV. |
| **Durasi QRS (*QRS Duration*)** | Lebar waktu kompleks QRS (kecepatan konduksi intraventrikular). | Durasi normal: $< 0.12\text{ s}$. Durasi $> 0.12\text{ s}$ mengindikasikan *Bundle Branch Block* (BBB). |
| **Interval QT (*QT Interval*)** | Total durasi depolarisasi dan repolarisasi ventrikel (sistole elektrik ventrikel). | Dihitung dengan koreksi laju jantung (Rumus Bazett): $QT_c = \frac{QT}{\sqrt{RR}}$. Normal: $< 0.44\text{ s}$ (pria), $< 0.46\text{ s}$ (wanita). |
| **Interval PP & RR (*PP & RR Intervals*)** | Durasi satu siklus atrial lengkap (P-to-P) dan siklus ventrikel (R-to-R). | Digunakan untuk kalkulasi *Heart Rate* (HR): $HR = \frac{60}{RR\text{ (dalam detik)}}$. Regularitas RR menentukan irama sinus vs aritmia. |

### 1.3 Patologi Klinis: STEMI (ST-Elevation Myocardial Infarction)
STEMI merupakan kondisi kedaruratan medis berupa sindrom koroner akut yang ditandai oleh transmural nekrosis miokardium akibat oklusi total pembuluh darah arteri koroner secara mendadak.

- **Patofisiologi**: Ruptur plak aterosklerosis memicu pembentukan trombus yang menyumbat total aliran arteri koroner (misalnya *Left Anterior Descending* / LAD, *Right Coronary Artery* / RCA). Area miokardium pasca-sumbatan mengalami iskemia akut, penurunan potensial istirahat membran, dan kelainan gaya gerak listrik repolarisasi ventrikel.
- **Gambaran EKG**: Terjadi **ST Elevation** (peningkatan abnormal segmen ST di atas garis isoelektrik $\ge 1\text{ mm}$ pada minimal dua sadapan berdampingan/kontigu).
- **Intervensi Medis & Modalitas Penunjang**: Pasien wajib segera menjalani prosedur *Percutaneous Coronary Intervention* (PCI) berupa kateterisasi jantung dan **pemasangan ring/stent jantung**. Prosedur intervensi ini dilakukan di laboratorium kateterisasi (Cath Lab) menggunakan panduan **[[Fluoroskopi]]** secara real-time untuk membuka sumbatan arteri dan mengembalikan reperpusi darah (*blood flow restoration*).

---

## 2. Elektroensefalografi (EEG)

Elektroensefalografi adalah teknik perekaman non-invasif untuk memantau fluktuasi aktivitas kelistrikan potensial post-sinaptik dari jutaan neuron pada korteks serebri melalui pencatatan elektroda yang ditempatkan di kulit kepala (*scalp*).

### 2.1 Karakteristik Sinyal EEG
Sinyal EEG beramplitudo sangat mikro ($10 - 100\ \mu\text{V}$) dengan rentang spektrum frekuensi fisiologis $0.5 - 50\text{ Hz}$. Berdasarkan pita frekuensinya, sinyal EEG diklasifikasikan menjadi:
1. **Gelombang Delta ($\delta$, $0.5 - 4\text{ Hz}$):** Dominan pada kondisi tidur nyenyak (*deep sleep / NREM*).
2. **Gelombang Teta ($\theta$, $4 - 8\text{ Hz}$):** Terjadi pada fase mengantuk (*drowsiness*) atau meditasi.
3. **Gelombang Alfa ($\alpha$, $8 - 13\text{ Hz}$):** Tampak pada kondisi rileks dengan mata tertutup (dominan area oksipital).
4. **Gelombang Beta ($\beta$, $13 - 30\text{ Hz}$):** Tampak saat aktivitas mental aktif, konsentrasi, atau kecemasan.
5. **Gelombang Gamma ($\gamma$, $> 30\text{ Hz}$):** Terlibat dalam pemrosesan kognitif tingkat tinggi dan integrasi sensorik.

### 2.2 Deteksi Epilepsi vs Pseudoseizure
EEG merupakan modalitas standar utama (*gold standard*) dalam evaluasi gangguan neurofisiologis kejang:

- **Epilepsi (Kejang Sejati / *True Seizure*)**:
  - *Elektrofisiologi*: Disebabkan oleh pelepasan muatan listrik berlebih dan hipersinkron abnormal dari sekelompok neuron kortikal.
  - *Gambaran EEG*: Menunjukkan pola khas berupa **Spike-and-Wave Complex** (puncak gelombang tajam berdurasi $< 70\text{ ms}$ diikuti gelombang lambat), *polyspikes*, atau *paroxysmal burst*. EEG memiliki spesifisitas sangat tinggi dalam mendiagnosis epilepsi.
- **Pseudoseizure (PNES / *Psychogenic Non-Epileptic Seizure*)**:
  - *Elektrofisiologi*: Serangan menyerupai kejang yang dipicu oleh faktor psikologis (gangguan konversi atau somatisasi) tanpa disertai kelainan pelepasan muatan listrik kortikal.
  - *Gambaran EEG*: Saat serangan berlangsung, rekaman EEG menunjukkan ritme fisiologis normal atau dominansi *muscle artifact*, tanpa adanya aktivitas gelombang epileptiform.
- **Indikasi Klinis EEG Lainnya**:
  - Infeksi sistem saraf pusat (Ensefalitis, Meningitis).
  - Evaluasi pasca-stroke dan riwayat cedera otak traumatik.
  - Adanya massa atau tumor otak.
  - Gangguan kognitif dan memori (Demensia, Penyakit Alzheimer).
  - Riwayat kejang demam (*febrile seizure*) berulang atau berdurasi panjang pada anak.
  - Gangguan fungsional otak atau dampak penyakit sistemik terhadap SSP.

### 2.3 Protokol Persiapan Klinis dan Rationale Fisis

#### A. Rationale Protokol *Sleep Deprivation* (Kurang Tidur / Begadang)
Sebelum menjalani tes EEG, pasien diinstruksikan untuk membatasi waktu tidur (begadang). Rationale klinis dan fisis protokol ini meliputi:
1. **Provokasi Aktivitas Epileptiform**: Kurang tidur menurunkan ambang kejang (*seizure threshold*) pada otak. Hal ini memprovokasi kemunculan gelombang kejang (*spike-and-wave*) yang mungkin tidak muncul pada kondisi terjaga normal.
2. **Transisi Fase Tidur**: Perekaman aktivitas otak saat pasien tertidur di ruang pemeriksaan memungkinkan evaluasi transisi fase tidur NREM, di mana gelombang epileptiform interiktal paling sering teraktivasi.
3. **Minimasi Artefak Kelistrikan**: Saat pasien tertidur, artefak fisik akibat gerakan otot wajah/leher (*EMG artifact*), gerakan bola mata (*EOG artifact*), dan kedipan kelopak mata berkurang secara drastis, sehingga menghasilkan sinyal sinaps kortikal yang bersih.

#### B. Kebersihan Kulit Kepala & Rambut
Pasien diwajibkan mencuci rambut hingga bersih (keramas) tanpa menggunakan minyak rambut, kondisioner, atau *hairspray*:
- **Rationale Hantaran Sinyal**: Minyak dan zat kimia pada kulit kepala berperan sebagai isolator listrik (meningkatkan impedansi antarmuka elektroda-kulit $Z_{contact}$). Impedansi yang tinggi ($> 5\text{ k}\Omega$) menghambat transmisi sinyal biopotensial beramplitudo mikrovolt ($\mu\text{V}$) dan menginduksi *thermal/ambient noise* yang merusak integritas rekaman.

#### C. Timing dan Durasi Pemeriksaan
Pemeriksaan EEG standar berlangsung selama $20 - 30\text{ menit}$. Waktu eksekusi terbaik adalah **$< 24\text{ jam}$ pasca serangan kejang**, saat jejak fragmentasi gelombang kejang (*post-ictal epileptiform discharge*) masih berada pada fase puncak untuk terdeteksi.

---

## 3. Elektromiografi (EMG)

Elektromiografi adalah teknik pemeriksaan neurofisiologi untuk merekam dan menganalisis aktivitas kelistrikan otot rangka (*skeletal muscle*) serta sel saraf motorik yang mengontrolnya (*lower motor neurons*).

> [!IMPORTANT]
> **Pelaksanaan & Prosedur Praktis EMG**:
> - **Tanpa Puasa / Persiapan Khusus**: Pasien tidak memerlukan puasa atau diet khusus sebelum tes.
> - **Kompetensi Pelaksana**: Pemeriksaan EMG wajib dilakukan langsung oleh **Dokter Spesialis Saraf (Neurolog)** karena penentuan titik stimulasi dan penusukan jarum bersifat dinamis sesuai kondisi klinis pasien.
> - **Durasi Pemeriksaan**: Umumnya berlangsung selama $30 - 60\text{ menit}$.

### 3.1 Evaluasi Sistem Saraf Tepi & Neuromuskular
EMG mengevaluasi unit motorik yang terdiri dari satu neuron motorik alfa beserta seluruh serat otot yang dipersarafinya. Pemeriksaan ini mencakup dua komponen dasar:
1. **EMG Jarum (*Needle EMG*)**: Penusukan elektroda jarum steril langsung ke otot untuk menilai *Motor Unit Action Potential* (MUAP) saat istirahat dan kontraksi voluntar.
2. **Studi Konduksi Saraf (*Nerve Conduction Study* / NCS)**: Pemberian stimulasi listrik eksternal pada saraf tepi untuk mengukur kecepatan hantar saraf (KHS) dan amplitudo respons motorik/sensorik.

```mermaid
graph LR
    NM["🧠 Neuron Motorik Spinal"] --> AX["⚡ Saraf Tepi (Axon)"]
    AX -->|Titik Gangguan MG| NMJ["🔌 Neuromuscular Junction"]
    NMJ --> MUAP["💪 Serat Otot (MUAP)"]
```

### 3.2 Indikasi Klinis Pemeriksaan EMG
Pemeriksaan EMG diindikasikan untuk menentukan lokasi lesi (*diagnosis topis*), patologi (aksonopati vs demielinasi), serta prospek kesembuhan (*prognosis*) pada kondisi:
- **Neuropati Tepi**: Kerusakan aksonal atau penyempitan saraf periferal (contoh: *Carpal Tunnel Syndrome*, penyempitan **Saraf Ulnar / Ulnar Nerve Constriction**, neuropati diabetik).
- **Hernia Nukleus Pulposus (HNP)**: Penekanan radiks saraf spinalis (saraf terjepit) pada area servikal atau lumbal.
- **Low Back Pain (LBP)**: Nyeri punggung bawah yang disertai radikulopati.
- **Miopati & Distrofi Otot**: Kelainan struktural primer pada serat otot.
- **Myasthenia Gravis (MG)**: Gangguan autoimun pada transmisi junction neuromuskular.
- **Guillain-Barré Syndrome (GBS)**: Polineuropati inflamasi demielinasi akut yang menyerang sistem saraf tepi.

### 3.3 Aturan Prosedural: Larangan Edema / Pembengkakan
Salah satu syarat mutlak lokasi penempelan elektroda atau penusukan jarum EMG adalah **area ekstremitas tidak boleh dalam kondisi edema (bengkak)**.

- **Rationale Fisis & Bioelektrik**:
  - Penumpukan cairan interstitial pada jaringan yang bengkak meningkatkan impedansi jaringan dan memperlebar jarak dielektrik antara elektroda dengan berkas saraf/otot.
  - Edema menyebabkan **dispersi arus stimulasi Listrik** (*current dispersion*). Arus listrik terhambat dan menyebar di cairan interstitial, sehingga stimulasi supramaksimal gagal mencapai akson saraf. Hal ini menghasilkan penurunan amplitudo palsu (*false attenuation*) atau absensi gelombang aksi yang menyesatkan diagnosis.

### 3.4 Respons Sinyal EMG: Myasthenia Gravis vs Otot Normal
Pada evaluasi Myasthenia Gravis, dilakukan uji **Repetitive Nerve Stimulation (RNS)**, yaitu pemberian stimulasi listrik berulang pada saraf motorik dengan frekuensi rendah ($2 - 5\text{ Hz}$).

![[diagram_college_biocomp_emg_myasthenia_gravis_rns.webp]]

- **Respons Otot Normal (Sehat)**:
  - Amplitudo *Compound Muscle Action Potential* (CMAP) tetap **stabil dan konstan** pada setiap stimulasi berulang. Cadangan neurotransmiter Asetilkolin (ACh) pada vesikel presinaptik cukup untuk mengaktivasi reseptor pascasinaptik secara konsisten.
- **Respons Penderita Myasthenia Gravis (MG)**:
  - Menunjukkan **Penurunan Amplitudo Progresif (*Decremental Response*)** $> 10\%$ antara respons CMAP pertama dan keempat/kelima.
  - *Patofisiologi*: Autoantibodi menyerang dan merusak reseptor Asetilkolin (AChR) pada membran pascasinaptik junction neuromuskular. Stimulasi berulang menguras pasokan ACh presinaptik, dan karena jumlah AChR aktif terbatas, transmisi neuromuskular mengalami kelelahan (*neuromuscular fatigue*), menyebabkan penurunan amplitudo kontraksi otot.

### 3.5 Pola Differensial Sinyal EMG

| Parameter | Kondisi Normal | Neurogenic Disorder (Saraf Rusak) | Myopathic Disorder (Otot Rusak) |
| :--- | :--- | :--- | :--- |
| **Aktivitas Istirahat** | Hening (*Silence*). | Fibrilasi & Gelombang Positif Tumpul (*PWS*). | Hening atau Fibrilasi terbatas. |
| **Morfologi MUAP** | Biphasic / Triphasic, durasi & amplitudo normal. | Polifasik, amplitudo tinggi, durasi panjang (reinnervasi). | Polifasik, amplitudo rendah, durasi pendek. |
| **Pola Interferensi** | Penuh (*Full Interference Pattern*). | Berkurang / Kasar (*Reduced Recruitment*). | Penuh tapi beramplitudo kecil (*Early Recruitment*). |

---

## 4. Perspektif Komputasi Biomedik & Pengolahan Sinyal

Dalam kerangka [[Komputasi Biomedis]], sinyal EKG, EEG, dan EMG mentah (*raw signals*) merupakan sinyal analog kontinu yang rentan terhadap distorsi lingkungan. Pemrosesan sinyal digital (DSP) mengikuti tahapan baku:

1. **Akuisisi & Filtering Sinyal**:
   - *Bandpass Filtering*:
     - EKG: $0.05 - 100\text{ Hz}$ (eliminasi *baseline wander* dan noise otot).
     - EEG: $0.5 - 70\text{ Hz}$ (isolasi pita gelombang $\delta, \theta, \alpha, \beta, \gamma$).
     - EMG: $10 - 500\text{ Hz}$ (menangkap spektrum MUAP murni).
   - *Notch Filter*: Menghilangkan interferensi jala-jala listrik AC pada frekuensi $50\text{ Hz}$ atau $60\text{ Hz}$.
2. **Ekstraksi Fitur (*Feature Extraction*)**:
   - Domain Waktu: *Root Mean Square* (RMS), *Mean Absolute Value* (MAV), *Zero Crossing* (ZC), kalkulasi interval peak-to-peak (RR-interval).
   - Domain Frekuensi: *Fast Fourier Transform* (FFT), *Power Spectral Density* (PSD), *Mean Frequency* (MNF), *Median Frequency* (MDF).
   - Domain Waktu-Frekuensi: *Continuous/Discrete Wavelet Transform* (CWT/DWT) untuk sinyal non-stasioner.
3. **Pattern Recognition & AI Classification**:
   - Algoritma Machine Learning (SVM, Random Forest, CNN, LSTM) dilatih untuk otomatisasi pemetaan patologi, seperti identifikasi segmen ST pada EKG STEMI, klasifikasi gelombang *spike-and-wave* EEG pada epilepsi, serta pendeteksian pola dekrementil EMG pada Myasthenia Gravis.

---

## 5. Ringkasan Komparatif Modalitas Sinyal Bioelektrik

| Parameter | Elektrokardiogram (EKG) | Elektroensefalografi (EEG) | Elektromiografi (EMG) |
| :--- | :--- | :--- | :--- |
| **Sumber Organ** | Jantung (*Myocardium*). | Otak (*Cerebral Cortex Neurons*). | Otot Rangka & Saraf Tepi (*PNS*). |
| **Amplitudo Tipikal** | $0.5 - 4.0\text{ mV}$ (Sedang). | $10 - 100\ \mu\text{V}$ (Sangat Kecil). | $50\ \mu\text{V} - 20\text{ mV}$ (Variatif/Bisa Besar). |
| **Rentang Frekuensi Utama** | $0.05 - 100\text{ Hz}$ | $0.5 - 50\text{ Hz}$ | $10 - 500\text{ Hz}$ |
| **Indikasi Utama** | Infark Miokard (STEMI), Aritmia, Iskemik Jantung. | Epilepsi, Pseudoseizure, Sleep Disorders, Ensefalitis. | HNP, LBP, Myasthenia Gravis, Neuropati, GBS. |
| **Artefak Dominan** | Gerakan pasien, respirasi, *baseline wander*. | Gerakan mata (EOG), kedipan, aktivitas otot (EMG). | Noise jala-jala listrik, edema jaringan, posisi jarum. |
| **Fitur Khas Patologi** | Elevasi segmen ST, perpanjangan QT. | *Spike-and-Wave discharge*. | Respons dekrementil RNS (MG). |

---

## Referensi & Catatan Vault
- [[Biomedical Computing]]
- [[Komputasi Biomedis]]
- [[Sinyal dan Sistem Biomedis]]
- Source Note: [[biocomp-pertemuan-2]] (Sections 3, 10, 11)
