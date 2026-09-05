---
title: "Teaching Space Dashboard"
type: "dashboard"
course: "Teaching"
tags:
  - "teaching"
  - "dashboard"
aliases:
  - "Dashboard"
  - "Teaching Dashboard"
created: 2026-05-01
---
# 🍎 Teaching Dashboard

> 🔗 **Quick Link:** [[index_teaching|🍎 Buka Teaching Resources Hub (Index)]]

## 🚀 Recently Edited Resources
> [!info]- 
> Menampilkan 10 berkas bahan ajar dan lembar kerja yang paling baru diperbarui.

```dataview
TABLE file.mtime AS "Last Modified", type AS "Type", subject AS "Subject", level AS "Level"
FROM "10 Spaces/12 Teaching"
WHERE file.name != "Dashboard" AND file.name != "index_teaching"
SORT file.mtime desc
LIMIT 10
```

---

## 🔬 Curriculum Development Backlog
> [!info]-
> Modul materi sumber (*30 Sources*) yang masih perlu disusun atau disempurnakan.

### STEM & Science
- [x] [[Trigonometri_SMA]] — Master Dashboard & 5 Submodul Lengkap
- [x] [[Konsep_dan_Kesamaan_Polinomial_SMA]] — Polinomial & Horner

### Languages
- [ ] Perfect Tenses (SMA) — Master Dashboard & Submodul (*Present, Past, Future, Continuous*)
- [ ] Present Continuous Tense (SMP) Source Material

---

## 📝 Practice Material Backlog
> [!info]-
> Lembar Kerja (LKPD) & Paket Soal Evaluasi (*40 Practice*) yang perlu dilengkapi.

### Paket Soal Evaluasi
- [ ] Soal Evaluasi: Parts of Speech (SMP)
- [ ] Soal Evaluasi: Text Types (Descriptive, Narrative, Functional) (SMP)
- [ ] Soal Evaluasi: Persamaan Kuadrat (SMP)
- [ ] Soal Evaluasi: Matriks (SMA)
- [ ] Soal Evaluasi: Peluang & Kombinatorika (SMA)
- [ ] Soal Evaluasi: Pendapatan Nasional (SMA)
- [ ] Soal Evaluasi: IPS SMP (Tenaga Eksogen, Endogen, Keanekaragaman Hayati, Pertambangan)
- [ ] Soal Evaluasi: Litosfer Tenaga Endogen dan Eksogen (SMA)

### Lembar Kerja Peserta Didik (LKPD)
- [ ] LKPD: Konsep Dasar Ekonomi (SMA)

