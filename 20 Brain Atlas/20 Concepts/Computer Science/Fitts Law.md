---
type: concept
subject: Computer_Science
source: "HCI_Week_1_Overview"
source_hash: "a1b2c3d4e5f67890123456789abcdef0"
date_created: 2026-08-18
status: atomic
tags:
  - hci
  - ux
  - concept
---

# Fitts's Law

**Fitts's Law** adalah hukum psikomotorik yang memprediksi waktu yang dibutuhkan seseorang untuk berpindah ke target berdasarkan jarak menuju target ($D$) dan lebar target ($W$).

## Persamaan Matematika
$$T = a + b \log_2 \left( \frac{2D}{W} \right)$$

Di mana:
- $T$ = Movement time (waktu pergerakan)
- $D$ = Distance (jarak ke target)
- $W$ = Width (lebar/ukuran target)

## Implikasi dalam UX/UI
1. **Ukuran Tombol:** Tombol aksi utama (*Call to Action*) harus dibuat lebih besar agar lebih cepat dan mudah diklik.
2. **Jarak Target:** Elemen interaktif yang sering digunakan diletakkan mendekati posisi kursor atau jangkauan jempol (*thumb zone*).
3. **Magic Corners:** Sudut dan tepi layar memiliki ukuran efektif tak hingga ($W = \infty$) karena kursor tidak bisa melewatinya, menjadikannya lokasi ideal untuk menu utama atau tombol keluar.
