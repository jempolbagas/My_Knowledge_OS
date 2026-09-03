---
name: college-study-pack
description: Workflow for university-level coursework in 10 Spaces/11 College/ and permanent self-study notes in 20 Brain Atlas/20 Notes/.
---

# College Study Pack Skill

Skill ini digunakan ketika pengguna meminta untuk merangkum materi kuliah, membuat catatan belajar, atau menyusun materi untuk mata kuliah di `10 Spaces/11 College/` ataupun self-study di `20 Brain Atlas/20 Notes/`.

---

## 📐 Output Format: Fluid Notes

Semua output menggunakan format **Fluid Note** — satu file per topik, tanpa template tetap. Struktur mengikuti konten, bukan sebaliknya.

### 1. Lokasi Berkas
- **Kuliah:** `10 Spaces/11 College/<Course_Folder>/<Topic_Name>.md`
- **Self-Study:** `20 Brain Atlas/20 Notes/<Subject>/<Topic_Name>.md`

### 2. Frontmatter

**Kuliah:**
```yaml
---
type: note
title: "Judul Topik"
course: "Nama Mata Kuliah"
semester: 5
week: 3
created: YYYY-MM-DD
prerequisites: []
tags: [college]
---
```

**Self-Study:**
```yaml
---
type: note
title: "Judul Topik"
subject: "Subject Area"
created: YYYY-MM-DD
prerequisites: []
tags: []
---
```

### 3. Struktur Konten (Adaptif)

**Tidak ada template fixed.** Agent memilih content blocks yang dibutuhkan berdasarkan topik:

- **Lead:** 2-4 kalimat pembuka — apa ini dan kenapa penting. Selalu ada.
- **Core:** Penjelasan utama dengan subheading deskriptif (bukan bernomor). Contoh dan worked examples langsung di-weave ke dalam penjelasan, bukan dipisah.
- **Quick Ref:** Callout `> [!abstract]- Quick Reference` berisi formula, teorema, command reference. Hanya jika topik memerlukan lookup cepat.
- **Drills:** Callout `> [!question]- Practice` berisi soal latihan + jawaban dalam nested `> [!check]- Answer`. Hanya jika latihan diperlukan.
- **Going Deeper:** Callout `> [!info]- Going Deeper` untuk materi lanjutan atau rabbit holes.

### 4. Aturan Generasi

1. **Satu file per topik** — jangan pisah ke Notes/Drills/Cheatsheet terpisah.
2. **Tidak ada emoji di heading** — gunakan heading deskriptif plain text.
3. **Tidak ada numbered sections** (❌ `## 1. Overview`, ❌ `### 2.1 Sub-topik`) — gunakan heading yang mendeskripsikan isinya.
4. **Tidak ada "Vault Linkage & Brain Atlas Promotion" footer** — cukup wikilink secara natural di dalam teks.
5. **LaTeX:** Gunakan `$` untuk inline dan `$$` untuk block. Jangan gunakan `\(` atau `\[`.
6. **Tone:** Conversational tapi akurat — seperti menjelaskan ke peer yang pintar, bukan menulis textbook.

---

## 📝 Contoh Struktur Output

```markdown
---
type: note
title: "Inverse Halftoning via CNN"
course: "Computer Vision"
semester: 5
week: 3
created: 2026-09-01
prerequisites: ["[[Convolutional Neural Networks]]"]
tags: [college]
---

# Inverse Halftoning via CNN

Inverse halftoning mengubah gambar biner halftone kembali ke continuous-tone.
Pendekatan klasik (filtering, lookup tables) gagal menangkap detail tekstur.
CNN bisa belajar mapping non-linear dari halftone → grayscale langsung dari data.

## Kenapa Halftone Perlu Di-reverse

(penjelasan motivasi + contoh visual ...)

## Arsitektur CNN untuk Inverse Halftoning

(penjelasan arsitektur + worked example forward pass ...)

## Loss Function: MSE vs Perceptual Loss

(perbandingan + kapan pakai yang mana ...)

> [!abstract]- Quick Reference
> **Input:** Binary halftone image (1-bit)
> **Output:** Continuous-tone grayscale (8-bit)
> **Common architectures:** U-Net, DnCNN, ResNet variants
> **Loss:** MSE for pixel accuracy, perceptual loss for texture

> [!question]- Practice
>
> **Q1.** Jelaskan mengapa MSE loss cenderung menghasilkan output yang blurry.
>
> > [!check]- Answer
> > MSE meminimalkan rata-rata error per pixel, yang berarti ...
```

---

## 🎨 Kebijakan Visual & Diagram

1. **AI Visual Asset Generation:**
   - Gunakan tool `generate_image` untuk diagram arsitektur atau peta konsep visual.
   - Simpan ke `30 Assets/` dengan format: `30 Assets/diagram_<topic_snake_case>.png`
   - Sematkan: `![[diagram_<topic_snake_case>.png]]`
2. **Native Mermaid & LaTeX:**
   - Mermaid code block untuk flowchart, sequence diagram, state machine.
   - LaTeX `$$ ... $$` untuk derivasi dan matriks.
