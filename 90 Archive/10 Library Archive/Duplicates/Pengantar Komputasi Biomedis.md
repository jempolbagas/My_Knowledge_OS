---
type: generated_reading
title: Pengantar Komputasi Biomedis
topic: Biomedical Computing
requested_on: 2026-08-20
prompt: "Bikin aku bacaan untuk semacam brief overview ke komputasi biomedis dong. Jadinya kayak semacam pengantar lah ke course ini."
status: archived
archived_reason: "Duplicate reading of English master note 'Introduction to Biomedical Computing.md'"
tags:
  - biomedical-computing
  - overview
  - computer-science
  - medicine
promoted_to:
  - "[[Komputasi Biomedis]]"
source_hash: "77fb188333f73b389b106c94738cca3f"
---
## The reading

[[Komputasi Biomedis]] (Biomedical Computing) adalah disiplin ilmu interdisipliner yang menggabungkan informatika, matematika terapan, pemrosesan sinyal, dan pembelajaran mesin untuk memodelkan, menganalisis, serta menyelesaikan permasalahan kompleks dalam domain biologi dan kedokteran. Bidang ini menjembatani data biologis berskala mikroskopis (seperti sekuens DNA dan struktur protein) hingga fenotipe makroskopis (seperti pencitraan organ, sinyal elektrofisiologis, dan rekaman medis pasien). Tujuan utamanya adalah meningkatkan pemahaman mekanistik terhadap penyakit, mempercepat penemuan obat, serta mendukung pengambilan keputusan klinis secara presisi dan terukur.

### 1. Fondasi Interdisipliner dan Hirarki Data Biomedis

Komputasi biomedis beroperasi di persimpangan antara sains data computational dan sains hayati. Kompleksitas domain ini bersumber dari karakteristik data biomedis yang multiskala (*multiscale data*) dan bervariasi tinggi (*heterogeneous data*).

Hirarki analisis dalam komputasi biomedis terbagi ke dalam empat tingkatan utama:
1. **Tingkat Molekuler & Genomik:** Berfokus pada sekuens asam nukleat (DNA/RNA), ekspresi gen, dan lipatan struktur protein ($3\text{D}$).
2. **Tingkat Seluler & Jaringan:** Memodelkan interaksi antar-sel, jalur metabolisme, dan dinamika jaringan biologis.
3. **Tingkat Organ & Sistem Fisiologis:** Mengolah sinyal bioelektrik dan dinamika fluida tubuh (seperti aliran darah sistem kardiovaskular).
4. **Tingkat Individu & Populasi:** Memproses data klinis makro, Rekam Medis Elektronik (EHR), dan studi epidemiologi.

### 2. Pilar-Pilar Utama Komputasi Biomedis

Mata kuliah Komputasi Biomedis umumnya terbagi menjadi lima sub-disiplin inti:

#### A. Pemrosesan Sinyal Biomedis (Biomedical Signal Processing)
Menganalisis sinyal waktu kontinu dan diskrit yang dihasilkan oleh aktivitas fisiologis tubuh.
- **Contoh Sinyal:** Elektrokardiogram (ECG/EKG untuk jantung), Elektroensefalogram (EEG untuk otak), dan Elektromiogram (EMG untuk otot).
- **Metode Kunci:** Ekstraksi fitur domain waktu dan frekuensi melalui Transformasi Fourier diskrit ($DFT$), Transformasi Wavelet untuk sinyal non-stasioner, serta tapis digital (IIR/FIR filter) untuk mereduksi *noise* artefak gerak atau interferensi listrik.

#### B. Pencitraan Biomedis & Analisis Citra (Biomedical Image Analysis)
Mengolah dan menginterpretasikan data visual medis 2D, 3D, dan 4D.
- **Modalitas Pencitraan:** *Computed Tomography* (CT), *Magnetic Resonance Imaging* (MRI), *Ultrasound* (USG), dan *Positron Emission Tomography* (PET).
- **Metode Kunci:** Rekonstruksi citra (seperti algoritma *Filtered Back-Projection* berdasarkan Transformasi Radon), segmentasi organ/tumor, registrasi citra (penyelarasan citra medis dari waktu atau modalitas berbeda), serta ekstraksi fitur visual berbasis *Convolutional Neural Networks* (CNN).

#### C. Bioinformatika & Genomika Komputasional (Bioinformatics)
Memproses dan menganalisis data molekuler berskala masif dari teknik *Next-Generation Sequencing* (NGS).
- **Fokus Utama:** Penyelarasan sekuens (*sequence alignment*) menggunakan algoritma pemograman dinamis (Needleman-Wunsch dan Smith-Waterman), estimasi pohon filogenetik, pemodelan struktur protein $3\text{D}$ (seperti AlphaFold), serta analisis variasi genetik (SNP).

#### D. Pemodelan & Simulasi Fisiologis (Physiome & Multiscale Modeling)
Konstruksi model matematika prediktif untuk meniru fungsi mekanis dan kimiawi organ tubuh.
- **Fokus Utama:** Pemodelan elektrofisiologi sel jantung menggunakan persamaan diferensial non-linear (seperti model Hodgkin-Huxley), serta simulasi dinamika fluida komputasional (*Computational Fluid Dynamics* / CFD) untuk menganalisis aneurisma atau aliran darah pada arteri koroner.

#### E. Informatika Klinis & AI Kedokteran (Clinical Informatics & Healthcare AI)
Penerapan sistem cerdas pada data kesehatan klinis untuk *Clinical Decision Support Systems* (CDSS).
- **Fokus Utama:** Pemrosesan bahasa alami (*Natural Language Processing* / NLP) pada catatan klinis tak terstruktur, prediksi risiko penyakit berbasis *Machine Learning*, ontologi medis (SNOMED-CT, ICD-10), serta *Federated Learning* untuk menjaga privasi data pasien sesuai regulasi kesehatan.

### 3. Formulasi Matematika Dasar dan Representasi Komputasi

Analisis biomedis bergantung pada formulasi matematika yang kuat untuk mentransformasikan fenomena biologi menjadi persamaan yang dapat diselesaikan oleh komputer.

#### Transformasi Sinyal (Domain Frekuensi)
Untuk menganalisis komponen frekuensi sinyal bioelektrik $x(t)$, digunakan Transformasi Fourier Waktu-Kontinu:
$$X(f) = \int_{-\infty}^{\infty} x(t) e^{-j 2\pi f t} \, dt$$

#### Segmentasi CitraMedis berbasis Variasi Energetik
Banyak metode segmentasi batas organ memanfaatkan fungsi energi kurva (*Active Contours / Snakes*):
$$E_{\text{snake}} = \int_{0}^{1} \left( E_{\text{internal}}(v(s)) + E_{\text{image}}(v(s)) + E_{\text{con}}(v(s)) \right) ds$$

#### Model Persamaan Diferensial Elektrofisiologi
Perubahan potensial membran sel $V$ terhadap waktu $t$ diformulasikan berdasarkan arus ionik $I_{i}$:
$$C_m \frac{dV}{dt} + \sum I_i(V, t) = I_{\text{app}}$$
di mana $C_m$ adalah kapasitansi membran dan $I_{\text{app}}$ adalah arus stimulasi luar.

### 4. Tantangan Komputasi dan Arah Masa Depan

1. **Dimensionalitas Tinggi & *Data Sparsity*:** Data biomedis sering kali memiliki ribuan fitur (misalnya ekspresi gen) namun sampel pasien terbatas ($p \gg n$).
2. **Kebutuhan *Explainable AI* (XAI):** Model *black-box* tidak dapat langsung diterapkan dalam keputusan medis tanpa transparansi rasionalitas klinis.
3. **Kedokteran Presisi (*Precision Medicine*):** Pergeseran dari pengobatan umum ke terapi terpersonalisasi berdasarkan profil genomik dan fisiologis spesifik pasien.
4. **Organ Digital (*Digital Twins*):** Pembuatan replika komputasional real-time dari organ pasien untuk menguji respons pengobatan secara simulatif sebelum intervensi fisik.

---

## Concepts to extract
- [ ] [[Komputasi Biomedis]]
- [ ] [[Sinyal Biomedis]]
- [ ] [[Pencitraan Biomedis]]
- [ ] [[Bioinformatika]]
- [ ] [[Pemodelan Fisiologis]]
- [ ] [[Kedokteran Presisi]]
