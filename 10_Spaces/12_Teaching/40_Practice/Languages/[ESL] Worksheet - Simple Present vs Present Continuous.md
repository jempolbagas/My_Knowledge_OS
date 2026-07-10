---
title: "[ESL] Worksheet: Simple Present vs Present Continuous"
course: English as a Second Language
tags: ["esl", "grammar", "simple-present", "present-continuous", "worksheet"]
aliases: ["[ESL] Worksheet: Simple Present vs Present Continuous"]
created: "2026-05-07"
type: Worksheet
topic: "Grammar - Tenses Practice"
grade: 7
status: 🌿 incubating
---

# [ESL] Worksheet: Simple Present vs Present Continuous

## Daftar Isi
- [[#1. Pengantar: Memilih Mode Eksekusi yang Tepat]]
- [[#2. Sesi Pemanasan: Identifikasi Pattern]]
- [[#3. Debugging Code: Perbaiki Error Syntax]]
- [[#4. Build the Sentence: Eksekusi Fungsi Sesuai Parameter]]
- [[#5. Edge Cases: Stative Verbs (Si "Mager")]]
- [[#6. Summary — Key Concepts at a Glance]]
- [[#7. Active Recall & Self-Test]]

---

## 1. Pengantar: Memilih Mode Eksekusi yang Tepat

Halo *engineers* bahasa! Di materi sebelumnya, kita sudah membedah *engine* di balik [[[ESL] Simple Present Tense]] dan [[[ESL] Present Continuous Tense]]. Sekarang waktunya *hands-on practice*.

Ibarat mengelola sebuah *server*, kamu harus tahu kapan menjalankan fungsi secara *background routine* (rutinitas) dan kapan harus memantau proses yang *live* detik ini juga. 
- **Simple Present** = *Scheduled tasks / Cron jobs*. Rutinitas, fakta, *default state*.
- **Present Continuous** = *Live stream / Active process*. Sedang dieksekusi detik ini, *temporary state*.

Kerjakan *worksheet* di bawah ini untuk memvalidasi *logic* bahasamu!

---

## 2. Sesi Pemanasan: Identifikasi Pattern

*Task*: Baca *log* (kalimat) di bawah ini. Tentukan apakah sistem harus mengeksekusi *Simple Present* (SP) atau *Present Continuous* (PC). Berikan alasannya berdasarkan *time tracker* atau konteks kalimatnya.

1. "Look! The monkey (eat) a banana on the roof."
   - **Tense yang tepat:** _______________________
   - **Alasan:** ___________________________________

2. "My brother usually (play) video games after school."
   - **Tense yang tepat:** _______________________
   - **Alasan:** ___________________________________

3. "Water (boil) at 100 degrees Celsius."
   - **Tense yang tepat:** _______________________
   - **Alasan:** ___________________________________

4. "Shh! The students (take) an exam right now."
   - **Tense yang tepat:** _______________________
   - **Alasan:** ___________________________________

5. "She (not/like) spicy food. It hurts her stomach."
   - **Tense yang tepat:** _______________________
   - **Alasan:** ___________________________________

---

## 3. Debugging Code: Perbaiki Error Syntax

*Task*: Temukan *syntax error* pada rentetan *code* (kalimat) di bawah ini. Coret kata yang salah, lalu tulis perbaikannya (seperti melakukan *pull request* untuk mem-fix *bug*). Ingat kembali *S/ES rule* dan penggunaan *helper verb*!

1. ❌ I am reading a book every night before bed.
   - ✅ *Fix*: __________________________________________________

2. ❌ The train is depart at 8 AM tomorrow morning.
   - ✅ *Fix*: __________________________________________________

3. ❌ Listen! Somebody sing in the shower.
   - ✅ *Fix*: __________________________________________________

4. ❌ He doesn't likes playing football.
   - ✅ *Fix*: __________________________________________________

5. ❌ What do you doing under the table?
   - ✅ *Fix*: __________________________________________________

---

## 4. Build the Sentence: Eksekusi Fungsi Sesuai Parameter

*Task*: Kamu diberikan *array* kata acak. Susun menjadi kalimat yang *valid* (*compile* tanpa *error*). Perhatikan bentuk tenses yang diminta di dalam kurung [ ].

1. (you / watch / TV / now / ?) -> **[Present Continuous]**
   - ______________________________________________________________

2. (my dad / not / work / on Sundays / .) -> **[Simple Present]**
   - ______________________________________________________________

3. (they / play / basketball / in the park / at the moment / .) -> **[Present Continuous]**
   - ______________________________________________________________

4. (how often / she / go / to the library / ?) -> **[Simple Present]**
   - ______________________________________________________________

---

## 5. Edge Cases: Stative Verbs (Si "Mager")

*Task*: Awas ada *stative verbs*! Kata-kata ini sifatnya "mager" alias menolak dieksekusi dalam mode *Continuous* (-ing). Tentukan bentuk kata kerja yang tepat.

1. I (am needing / need) your help with this math homework right now.
   - Jawaban: _______________________

2. That soup (smells / is smelling) delicious!
   - Jawaban: _______________________

3. I (am not understanding / don't understand) this instruction.
   - Jawaban: _______________________

4. Who (owns / is owning) this red car?
   - Jawaban: _______________________

---

## 6. Summary — Key Concepts at a Glance

| Concept | Simple Present | Present Continuous |
| :--- | :--- | :--- |
| **Fungsi Utama** | *Routine tasks, hardcoded facts, schedules*. | *Live processes, temporary actions happening right now*. |
| **Formula / Sintaks Dasar** | S + V1 (tambah s/es untuk He/She/It) | S + am/is/are + V-ing |
| **Helper Verbs (Negatif/Tanya)**| Do / Does | Am / Is / Are |
| **Time Trackers** | *always, usually, every day, often* | *now, right now, at the moment, currently* |
| **Stative Verbs Compatibility**| ✅ 100% *Supported* (misal: *I know*) | ❌ *Error/Unsupported* (jangan pakai: *I am knowing*) |

---

## 7. Active Recall & Self-Test

> [!question]- 1. Mengapa kalimat "I am going to school every day" dianggap sebagai *logic error*?
> Karena kata *every day* adalah *time tracker* yang menandakan sebuah rutinitas (loop yang terus berulang). Rutinitas seharusnya di-*handle* oleh *Simple Present Tense*, bukan *Present Continuous* yang didesain untuk *live process* (sedang terjadi detik ini). Syntax perbaikannya adalah: "I go to school every day."

> [!question]- 2. Apa fungsi dari *helper verb* "Does" dan mengapa ia membebaskan verb utama dari beban s/es?
> *Does* bertindak seperti *API gateway* yang meng-*handle request* negatif dan interogatif untuk subjek tunggal (He/She/It). Karena *load* penanda orang ketiga sudah diambil alih oleh *Does*, verb utama ("play", "eat") kembali ke bentuk murni (*base form*) tanpa imbuhan apa pun. Menggunakan *doesn't plays* adalah *double error*.

> [!question]- 3. Tentukan letak kesalahan kalimat ini: "He is having a new smartphone."
> Kesalahannya ada pada *stative verb* "have" (dalam arti memiliki). Kata kerja kepemilikan tidak mendukung format *continuous* (-ing). Bentuk yang benar secara sintaks adalah: "He has a new smartphone."

> [!question]- 4. Apa *output* yang benar jika kita menggabungkan subjek "The sun" dan verb "shine" dalam kondisi detik ini juga?
> "The sun is shining." (Menggunakan *Present Continuous* karena sedang terjadi sekarang, dan perhatikan *spelling rule*: huruf 'e' pada *shine* di-*drop* sebelum ditambah -ing).
