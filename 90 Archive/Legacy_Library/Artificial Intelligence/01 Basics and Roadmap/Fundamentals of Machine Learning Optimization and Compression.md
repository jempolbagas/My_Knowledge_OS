---
type: generated_reading
title: "Fundamentals of Machine Learning Optimization and Compression: Overview Map"
topic: "Artificial_Intelligence"
requested_on: "2026-08-20"
updated_on: "2026-08-21"
status: done
tags: [artificial-intelligence, optimization, math, pruning, quantization, distillation, svd, lora]
---

# Fundamentals of Machine Learning Optimization and Compression: Overview Map

Dokumen ini berfungsi sebagai **peta taksonomi dan navigasi utama** untuk empat pilar fundamental kompresi dan optimasi jaringan saraf (*Deep Learning Model Compression*). Setiap pilar telah diurai secara mendalam ke dalam catatan bacaan terfokus (*dedicated reading notes*):

```mermaid
graph TD
    Root["Model Optimization & Compression"] --> P["1. Network Pruning & Sparsity"]
    Root --> Q["2. Model Quantization"]
    Root --> KD["3. Knowledge Distillation"]
    Root --> LR["4. Low-Rank Factorization & LoRA"]

    P -. Read Note .-> P_Note["[[Network Pruning and Sparsity Analysis]]"]
    Q -. Read Note .-> Q_Note["[[Post Training Quantization End to End Guide]]"]
    KD -. Read Note .-> KD_Note["[[Knowledge Distillation and Teacher Student Optimization]]"]
    LR -. Read Note .-> LR_Note["[[Low Rank Factorization and LoRA Mechanics]]"]
```

---

## 1. Network Pruning & Sparsity Analysis
* **Fokus:** Menghapus parameter berlebih berdasarkan analisis *saliency*orde dua (ekspansi Taylor & *Optimal Brain Damage*) untuk meminimalkan kenaikan *loss* empiris.
* **Master Reading:** [[Network Pruning and Sparsity Analysis]]

---

## 2. Model Quantization
* **Fokus:** Mengonversi representasi *floating-point* ($32$-bit `FP32`) ke *integer* presisi rendah ($8$-bit `INT8`) menggunakan pemetaan afin (faktor skala $S$, titik nol $Z$) serta algoritma kalibrasi (MinMax, MSE, KL-Divergence).
* **Master Reading:** [[Post Training Quantization End to End Guide]]

---

## 3. Knowledge Distillation (Teacher-Student)
* **Fokus:** Mentransfer *"Dark Knowledge"* dari model besar (*Teacher*) ke model kecil (*Student*) melalui manipulasi distribusi *softmax* dengan *Temperature Scaling* ($T > 1$) dan peminimalan *KL Divergence*.
* **Master Reading:** [[Knowledge Distillation and Teacher Student Optimization]]

---

## 4. Low-Rank Factorization & LoRA
* **Fokus:** Memanfaatkan *low intrinsic rank* pada matriks bobot jaringan saraf menggunakan dekomposisi nilai singular (*SVD*) dan *Low-Rank Adaptation* ($W = W_0 + BA$) untuk pelatihan parameter yang efisien.
* **Master Reading:** [[Low Rank Factorization and LoRA Mechanics]]
