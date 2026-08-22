# README — Gemastik KTI Space

Panduan singkat untuk anggota tim yang baru join vault ini.

## Struktur Direktori

```
13_Gemastik_KTI/
├── 00_Koordinasi/   → task list, pembagian tugas, catatan rapat
├── 10_Riset/        → catatan riset dan brainstorming
├── 20_Draf/         → draf KTI (satu file per versi, jangan overwrite)
└── 30_Referensi/    → panduan format Gemastik, template resmi
```

## Arsip Topik Sebelumnya

Materi topik awal (Resilient Edge) disimpan di `90_Archive/Gemastik_KTI_Topik_1_Resilient_Edge/`.

## Konvensi Wajib

**1. Gunakan Wikilinks untuk referensi internal**
Tulis `[[Index Gemastik]]` atau `[[Riset Index]]` bukan path lengkap atau link biasa.

**2. Sumber eksternal masuk Brain Atlas, bukan sini**
Kalau kamu baca paper atau artikel untuk riset KTI:
- Buat Library note di `20_Brain_Atlas/10_Library/`
- Lalu link dari `10_Riset/Riset Index.md`

Ini supaya sumber bisa reusable dan tidak terduplikasi.

**3. Draf — jangan overwrite**
Setiap iterasi besar = file baru. Format: `Draf_v[n]_[YYYY-MM-DD].md`

**4. Frontmatter minimal**
Setiap note baru harus punya:
```yaml
---
type: [note/index/coordination/draft]
space: Gemastik_KTI
tags: [gemastik, ...]
created: YYYY-MM-DD
---
```

## Mulai dari Sini

→ Buka [[Index Gemastik]] untuk overview lengkap tim dan status KTI.
