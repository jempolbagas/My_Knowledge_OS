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

## Konvensi Wajib

**1. Gunakan Wikilinks untuk referensi internal**
Tulis `[[Index]]` bukan path lengkap atau link biasa.

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

## Git Workflow

- Branch: diskusikan dulu dengan tim (main langsung atau feature branch?)
- Commit message: `[KTI] deskripsi singkat apa yang diubah`
- Contoh: `[KTI] tambah catatan riset topik X`

## Mulai dari Sini

→ Buka [[Index_Gemastik]] untuk overview lengkap tim dan status KTI.

---

## Setup Automasi (Wajib setelah Clone)

Vault ini punya sistem automasi yang menjaga index vault, deteksi broken links, dan staleness check. Tanpa ini, agen AI tidak bisa membaca vault dengan efisien.

### Prasyarat Sistem

```bash
# Cek apakah sudah terinstall
python3 --version   # butuh Python 3.8+
inotifywait --version  # bagian dari inotify-tools (untuk watcher)
```

Kalau `inotifywait` belum ada:
```bash
# Ubuntu/Debian
sudo apt install inotify-tools

# Arch
sudo pacman -S inotify-tools
```

### Setup Pertama Kali (satu kali saja)

```bash
# 1. Masuk ke direktori vault
cd /path/ke/vault  # sesuaikan dengan lokasi clone kamu

# 2. Buat virtual environment Python
python3 -m venv .automation/venv

# 3. Install dependencies
.automation/venv/bin/pip install -r .automation/requirements.txt

# 4. Build index awal (generate semua reports)
.automation/venv/bin/python3 .automation/scripts/build_index.py
.automation/venv/bin/python3 .automation/scripts/linter.py
.automation/venv/bin/python3 .automation/scripts/staleness_checker.py
.automation/venv/bin/python3 .automation/scripts/generate_summary.py
```

### Jalankan Watcher (setiap sesi kerja)

Watcher otomatis rebuild index setiap kali ada perubahan file di vault.

```bash
bash .automation/scripts/watcher.sh
```

Jalankan ini di terminal terpisah, biarkan berjalan di background selama kamu kerja di vault. Tekan `Ctrl+C` untuk stop.

### Sync ke Git

Untuk push perubahan ke remote (semua anggota bisa pakai ini):

```bash
bash .automation/scripts/git_sync.sh
```

Script ini otomatis `git add -A`, commit dengan timestamp, lalu push ke `main`.

> [!warning] Sebelum push, pastikan kamu sudah `git pull` terlebih dahulu untuk menghindari konflik.

### Reports yang Dihasilkan

Setelah watcher/script berjalan, cek folder `.automation/reports/`:

| File | Isi |
|------|-----|
| `vault_summary.json` | Peta lengkap vault, dibaca agen AI setiap sesi |
| `linter_report.md` | Broken links dan orphan pages |
| `stale_concepts.md` | Concept notes yang mungkin sudah outdated |
