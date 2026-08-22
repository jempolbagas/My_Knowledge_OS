---
name: college-study-pack
description: Specialized workflow for university-level coursework in 10 Spaces/11 College/ and permanent self-study packs in 20 Brain Atlas/40 Self Study Packs/.
---

# College Study Pack Skill

Skill ini digunakan ketika pengguna meminta untuk merangkum materi kuliah, menyusun paket belajar, membuat *cheatsheet*, atau membuat *problem set & active recall drills* untuk mata kuliah di `10 Spaces/11 College/` ataupun proyek *self-study* fundamental di `20 Brain Atlas/40 Self Study Packs/`.

---

## 📐 Aturan Struktur & Penamaan Berkas

### 1. Pengelompokan Berkas per Minggu / Topik (Sub-folder per Topik)
Seluruh materi per topik mingguan/sprint disimpan di dalam subfolder terdedikasi:
- **Lokasi Direktori Kuliah:** `10 Spaces/11 College/<Course_Folder>/Week_<XX>_<Topic_Snake_Case>/`
- **Lokasi Direktori Self-Study:** `20 Brain Atlas/40 Self Study Packs/<Topic_Folder>/`
  - Contoh: `10 Spaces/11 College/Computer_Vision/Week_03_CNN_Inverse_Halftoning/`
  - Contoh: `20 Brain Atlas/40 Self Study Packs/System_Design_Fundamentals/`

### 2. Paket Berkas Utama per Minggu (Weekly File Suite)
Di dalam folder topik tersebut, buat berkas-berkas berikut sesuai kebutuhan pengguna:
1. **Master Lecture Note:** `Week_<XX>_<Topic_Snake_Case>_Notes.md`
   - Berisi rangkuman mendalam, penjelasan teknis/matematis, dan pseudo-code.
2. **Practice & Active Recall Drills:** `Week_<XX>_<Topic_Snake_Case>_Drills.md`
   - Berisi latihan soal berstandar ujian universitas, dengan kunci jawaban diletakkan di bagian paling bawah dokumen (bukan *reveal mechanism*).
3. **Formula & Key Algorithm Cheatsheet:** `Week_<XX>_<Topic_Snake_Case>_Cheatsheet.md`
   - Reference card ringkas berisi teorema, formula LaTeX, dan matriks kompleksitas time/space.

### 3. Paket Ujian Semester (UTS / UAS)
Untuk ringkasan ujian tengah/akhir semester, simpan langsung di root folder mata kuliah:
- `10 Spaces/11 College/<Course_Folder>/Exam_Prep_UTS_<Course>.md`
- `10 Spaces/11 College/<Course_Folder>/Exam_Prep_UAS_<Course>.md`

---

## 📝 Format Seragam (Fixed Uniform Template)

Setiap catatan kuliah mingguan (`Week_<XX>_<Topic_Snake_Case>_Notes.md`) **wajib** mengikuti hirarki 4 tahap fixed di bawah ini:

```markdown
---
title: "<Judul Topik>"
course: "<Nama Mata Kuliah / Topik Self-Study>"
course_abbr: "<Singkatan, misal: CV, DS, DM, DSP>"
semester: <XX / Kosongkan jika Self-Study>
week: <XX / Kosongkan jika Self-Study>
date: "<YYYY-MM-DD>"
tags: ["lecture-note", "<course-tag>"]
type: <LectureNote / SelfStudyNote>
---

# 🎓 <Judul Topik> — <Subtitle Hook>

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
*(Jawaban di bagian bawah file)*

---

## 🔑 Kunci Jawaban & Pembahasan

**Jawaban Q1:**
1. Langkah 1: ...
2. Langkah 2: ...

---

## 🔗 Vault Linkage & Brain Atlas Promotion

> [!tip] **Promotable Concepts for Permanent Vault (`20 Brain Atlas/`)**
> Catatan ini mereferensikan konsep-konsep fundamental yang layak dipromosikan ke `20 Brain Atlas/20 Concepts/`:
> - `[[<Nama_Konsep_1>]]`: <Alasan singkat mengapa konsep ini bersifat abadi/timeless>
> - `[[<Nama_Konsep_2>]]`
```

---

## 🎨 Kebijakan Visual & Diagram (`30 Assets/`)

1. **AI Visual Asset Generation:**
   - Gunakan tool `generate_image` untuk membuat diagram arsitektur sistem, alur *pipeline*, atau peta konsep visual yang kompleks.
   - Simpan gambar ke direktori vault terpusat `30 Assets/` dengan format penamaan:
     `30 Assets/diagram_college_<course_abbr>_<topic_snake_case>.png`
   - Sematkan dalam catatan menggunakan sintaks Obsidian: `![[diagram_college_<course_abbr>_<topic_snake_case>.png]]`.
2. **Native Mermaid & LaTeX:**
   - Gunakan Mermaid code block (` ```mermaid `) untuk *flowchart* proses sederhana, *sequence diagram*, atau *state machine*.
   - Gunakan LaTeX math (`$$ ... $$`) untuk derivasi rumus matematika dan matriks.

---

## 🔄 Integrasi Dataview & Vault Architecture

1. **Otomatisasi Dashboard:** Setiap dokumen yang dibuat dengan `type: LectureNote` dan `semester: 5` akan otomatis terdeteksi di [[00_Semester_5_Dashboard|Semester 5 Dashboard]].
2. **Soft Linkage:** Tautkan istilah penting dengan `[[Wikilinks]]` ke catatan yang ada di `20 Brain Atlas/`.
