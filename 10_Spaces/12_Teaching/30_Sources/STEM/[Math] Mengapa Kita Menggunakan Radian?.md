---
title: "[Math] Mengapa Kita Menggunakan Radian?"
course: ""
tags: []
aliases: ["[Math] Mengapa Kita Menggunakan Radian?"]
created: "2026-05-12"
---
# Mengapa Kita Menggunakan Radian?

Pernahkah kamu bertanya-tanya, kenapa dalam matematika lanjutan dan fisika kita tiba-tiba berhenti menggunakan *derajat* (seperti 90°, 180°, 360°) dan beralih menggunakan *radian* (yang penuh dengan huruf Yunani $\pi$)?

Mari kita bedah alasannya, mulai dari sejarah hingga alasan logis matematikanya.

---

## 1. Derajat itu "Buatan Manusia" (Arbitrer)

Angka 360 derajat untuk satu lingkaran penuh sebenarnya adalah sesuatu yang **dibuat-buat** oleh manusia, bukan hukum alam. 

Ada beberapa teori mengapa angka 360 yang dipilih oleh peradaban kuno (seperti Babilonia):
- **Kalender Kuno:** Satu tahun diperkirakan memiliki sekitar 360 hari. Jadi, matahari bergerak sekitar 1/360 bagian dari lintasannya setiap hari.
- **Sistem Basis 60:** Bangsa Babilonia menggunakan sistem bilangan basis 60 (sama seperti kita mengukur jam dan menit). Angka 360 sangat mudah dibagi oleh banyak angka (2, 3, 4, 5, 6, 8, 9, 10, 12, dst), membuatnya sangat praktis untuk perhitungan pecahan pada zaman sebelum ada kalkulator.

Bayangkan jika alien datang ke bumi. Mereka mungkin punya kalender dengan 400 hari setahun dan jari yang jumlahnya 8. Bagi mereka, satu lingkaran penuh mungkin bernilai 400 derajat, atau angka lainnya. Derajat **tidak universal**.

---

## 2. Radian itu "Alami" (Hukum Alam Semesta)

Berbeda dengan derajat, radian adalah cara mengukur sudut yang murni didasarkan pada sifat **geometri lingkaran itu sendiri**. Jika alien mengukur lingkaran, mereka pasti akan menemukan radian yang sama dengan kita.

**Definisi Radian:**
Satu radian adalah besar sudut yang dibentuk ketika **panjang busur lingkaran (garis lengkungnya) sama persis dengan panjang jari-jarinya (r)**.

Bayangkan kamu memiliki seutas tali yang panjangnya sama dengan jari-jari lingkaran. Lalu kamu tempelkan tali itu melengkung mengikuti tepi lingkaran. Sudut yang terbentuk dari pusat lingkaran ke ujung-ujung tali tersebut adalah **tepat 1 radian**.

---

## 3. Dari Mana Asal $2\pi$ Radian = 360 Derajat?

Sekarang kita tahu bahwa 1 radian = sudut saat panjang busur = jari-jari ($r$).

Pertanyaannya: **Butuh berapa banyak tali (sepanjang $r$) untuk bisa mengelilingi seluruh tepi lingkaran penuh?**

Mari kita ingat kembali rumus keliling lingkaran yang sudah kita pelajari sejak SD:
$$Keliling = 2 \cdot \pi \cdot r$$

Rumus ini secara harfiah memberitahu kita bahwa panjang seluruh tepi lingkaran adalah **$2\pi$ kali dari jari-jarinya**. 
Karena $\pi$ (Pi) bernilai sekitar 3.14159..., maka $2\pi$ adalah sekitar 6.28. 
Artinya, butuh sekitar 6.28 potong tali untuk mengelilingi satu lingkaran penuh.

Karena:
- 1 jari-jari di tepi lingkaran = 1 radian
- 1 lingkaran penuh = $2\pi$ kali jari-jari

Maka:
**1 lingkaran penuh (360°) = $2\pi$ radian**

Dari sini kita bisa menurunkan semuanya:
- $360^\circ = 2\pi \text{ radian}$
- $180^\circ = \pi \text{ radian}$ (Setengah lingkaran)
- $90^\circ = \frac{\pi}{2} \text{ radian}$ (Seperempat lingkaran)

---

## 4. Kenapa Harus Repot Menggunakan Radian?

Saat belajar trigonometri dasar, derajat memang terasa lebih mudah dibayangkan. Tapi ketika masuk ke Kalkulus dan Fisika, radian menjadi pahlawan.

Karena radian secara langsung menghubungkan sudut dengan panjang (melalui jari-jari), banyak rumus matematika menjadi sangat sederhana tanpa perlu konstanta yang rumit.

**Contoh: Panjang Busur (s)**
- Jika pakai radian: $s = r \cdot \theta$ (sangat simpel)
- Jika pakai derajat: $s = r \cdot \theta \cdot (\frac{\pi}{180})$ (ada angka "konstanta buatan" 180 yang mengganggu)

**Contoh dalam Kalkulus (Turunan dari sin x):**
- Jika x dalam radian: Turunan dari $\sin(x)$ adalah $\cos(x)$
- Jika x dalam derajat: Turunan dari $\sin(x)$ adalah $\frac{\pi}{180} \cdot \cos(x)$

Dalam matematika lanjutan, kita ingin rumus yang "bersih" dan mencerminkan kebenaran alam, bukan angka 360 yang kebetulan dipilih manusia ribuan tahun yang lalu. Itulah sebabnya **radian adalah bahasa asli matematika untuk sudut.**