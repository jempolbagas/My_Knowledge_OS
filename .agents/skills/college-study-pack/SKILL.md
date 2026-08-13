---
name: college-study-pack
description: Specialized workflow for university-level coursework, lecture digests, exam prep cheatsheets, and practice drills in 10_Spaces/11_College/.
---

# College Study Pack Skill

Skill ini digunakan ketika pengguna meminta untuk merangkum materi kuliah (PPT/PDF/RPS), menyusun paket belajar mingguan, membuat *cheatsheet* persiapan UTS/UAS, atau membuat *problem set & active recall drills* untuk mata kuliah di `10_Spaces/11_College/`.

---

## 📐 Aturan Struktur & Penamaan Berkas

### 1. Pengelompokan Berkas per Minggu / Topik (Sub-folder per Topik)
Seluruh materi per topik mingguan disimpan di dalam subfolder terdedikasi di bawah direktori mata kuliah yang bersangkutan:
- **Lokasi Direktori:** `10_Spaces/11_College/<Course_Folder>/Week_<XX>_<Topic_Snake_Case>/`
  - Contoh: `10_Spaces/11_College/Computer_Vision/Week_03_CNN_Inverse_Halftoning/`
  - Contoh: `10_Spaces/11_College/Distributed_Systems/Week_04_Raft_Consensus/`

### 2. Paket Berkas Utama per Minggu (Weekly File Suite)
Di dalam folder topik tersebut, buat berkas-berkas berikut sesuai kebutuhan pengguna:
1. **Master Lecture Note:** `Week_<XX>_<Topic_Snake_Case>_Notes.md`
   - Berisi rangkuman mendalam, penjelasan teknis/matematis, dan pseudo-code.
2. **Practice & Active Recall Drills:** `Week_<XX>_<Topic_Snake_Case>_Drills.md`
   - Berisi latihan soal berstandar ujian universitas dengan jawaban tersembunyi (`<details><summary>Jawaban & Pembahasan</summary></details>`).
3. **Formula & Key Algorithm Cheatsheet:** `Week_<XX>_<Topic_Snake_Case>_Cheatsheet.md`
   - Reference card ringkas berisi teorema, formula LaTeX, dan matriks kompleksitas time/space.

### 3. Paket Ujian Semester (UTS / UAS)
Untuk ringkasan ujian tengah/akhir semester, simpan langsung di root folder mata kuliah:
- `10_Spaces/11_College/<Course_Folder>/Exam_Prep_UTS_<Course>.md`
- `10_Spaces/11_College/<Course_Folder>/Exam_Prep_UAS_<Course>.md`

---

## 📝 Format Seragam (Fixed Uniform Template)

Setiap catatan kuliah mingguan (`Week_<XX>_<Topic_Snake_Case>_Notes.md`) **wajib** mengikuti hirarki 4 tahap fixed di bawah ini:

```markdown
---
title: "Week <XX>: <Judul Topik>"
course: "<Nama Mata Kuliah>"
course_abbr: "<Singkatan, misal: CV, DS, DM, DSP>"
semester: 5
week: <XX>
date: "<YYYY-MM-DD>"
tags: ["college", "lecture-note", "<course-tag>", "semester-5"]
type: LectureNote
---

# 🎓 Week <XX>: <Judul Topik> — <Subtitle Hook>

> [!info] **Course Overview:** [[<Course_Overview_Note>]] | **Syllabus:** [[<Course_Syllabus_Note>]]
> **Topics Covered:** <Sub-bahasan 1>, <Sub-bahasan 2>, <Sub-bahasan 3>

---

## 📌 1. Overview & Core Context
- **Latar Belakang & Motivasi:** Mengapa topik ini penting dalam konteks <Nama Mata Kuliah>.
- **High-Level Takeaway:** 3-5 poin taksonomi utama yang wajib dikuasai untuk ujian.

---

## 📖 2. Detailed Lecture Notes & Technical Deep-Dive

### 2.1 <Sub-topik Utama 1>
- Penjelasan akademis berstandar mahasiswa.
- Penggunaan LaTeX math untuk formula: inline `\( ... \)` atau block `\[ ... \]`.
- Blok kode (Python/C++/Mermaid) jika mencakup algoritma atau struktur data.

### 2.2 <Sub-topik Utama 2>
...

---

## ⚡ 3. Formulas, Key Theorems, & Algorithms

| Nama Konsep / Algoritma | Teorema / Formula Kunci | Kompleksitas / Catatan Kunci |
| :--- | :--- | :--- |
| **<Nama Algoritma>** | `\( <Formula> \)` | `\( O(N \log N) \)` — <Catatan Singkat> |

---

## 🧠 4. Active Recall & Practice Drills

### Q1: <Pertanyaan Derivasi / Konseptual HOTS>
<details>
<summary>💡 Lihat Jawaban & Step-by-Step Pembahasan</summary>

**Pembahasan:**
1. Langkah 1: ...
2. Langkah 2: ...
</details>

---

## 🔗 Vault Linkage & Brain Atlas Promotion

> [!tip] **Promotable Concepts for Permanent Vault (`20_Brain_Atlas/`)**
> Catatan ini mereferensikan konsep-konsep fundamental yang layak dipromosikan ke `20_Brain_Atlas/20_Concepts/`:
> - `[[<Nama_Konsep_1>]]`: <Alasan singkat mengapa konsep ini bersifat abadi/timeless>
> - `[[<Nama_Konsep_2>]]`
```

---

## 🎨 Kebijakan Visual & Diagram (`30_Assets/`)

1. **AI Visual Asset Generation:**
   - Gunakan tool `generate_image` untuk membuat diagram arsitektur sistem, alur *pipeline*, atau peta konsep visual yang kompleks.
   - Simpan gambar ke direktori vault terpusat `30_Assets/` dengan format penamaan:
     `30_Assets/diagram_college_<course_abbr>_<topic_snake_case>.png`
   - Sematkan dalam catatan menggunakan sintaks Obsidian: `![[diagram_college_<course_abbr>_<topic_snake_case>.png]]`.
2. **Native Mermaid & LaTeX:**
   - Gunakan Mermaid code block (` ```mermaid `) untuk *flowchart* proses sederhana, *sequence diagram*, atau *state machine*.
   - Gunakan LaTeX math (`$$ ... $$`) untuk derivasi rumus matematika dan matriks.

---

## 🔄 Integrasi Dataview & Vault Architecture

1. **Otomatisasi Dashboard:** Setiap dokumen yang dibuat dengan `type: LectureNote` dan `semester: 5` akan otomatis terdeteksi di [[00_Semester_5_Dashboard|Semester 5 Dashboard]].
2. **Soft Linkage:** Tautkan istilah penting dengan `[[Wikilinks]]` ke catatan yang ada di `20_Brain_Atlas/`.
