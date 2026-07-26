---
title: "Semester 5 Dashboard (Fall 2026)"
type: Dashboard
semester: 5
academic_year: "2026/2027"
tags: ["college", "semester-5", "dashboard"]
created: "2026-07-27"
---

# 🎓 Semester 5 Hub & Operations (Fall 2026)

> [!info] **Semester Status:** Active Preparation / KRS & RPS Pending
> Central command dashboard for all 7 planned courses in Semester 5 (including 2 retake courses from Semester 3).

---

## 🎯 Academic Goals & Milestones
- **Target GPA / IPK:** 3.80+Late
- **Focus Areas:** Systems, Security, Data Analysis & Grade Improvement (Retakes).
- **Key Calendar Dates:**
  - **KRS & Registration:** Pending (Early-Mid August 2026)
  - **Midterm Exams (UTS):** October 2026
  - **Final Exams (UAS):** December 2026 / January 2027

---

## 📚 Planned Course Directory (Semester 5)

| Code / Abbr | Course Name | Status / Notes | Course Hub | Syllabus (RPS) |
| :--- | :--- | :--- | :--- | :--- |
| **DS** | Distributed Systems | Main (Smt 5) | [[Distributed Systems Overview]] | [[DS Syllabus]] |
| **IP** | Image Processing | Main (Smt 5) | [[Image Processing Overview]] | [[IP Syllabus]] |
| **DM** | Data Mining | Main (Smt 5) | [[Data Mining Overview]] | [[DM Syllabus]] |
| **HCI** | Human & Computer Interaction | Main (Smt 5) | [[HCI Overview]] | [[HCI Syllabus]] |
| **CRYPTO** | Cryptography | Main (Smt 5) | [[Cryptography Overview]] | [[Crypto Syllabus]] |
| **NM** | Numerical Methods | ⚠️ Retake (Smt 3) | [[Numerical Methods Overview]] | [[NM Syllabus]] |
| **OS** | Operating Systems | ⚠️ Retake (Smt 3) | [[Operating Systems Overview]] | [[OS Syllabus]] |

---

## 📝 Recent Semester 5 Lecture Notes
```dataview
TABLE course, week, date, tags
FROM "10_Spaces/11_College"
WHERE semester = 5 AND type = "LectureNote"
SORT date DESC
LIMIT 10
```

---

## 📌 Active Assignments & Tasks
```dataview
TASK
FROM "10_Spaces/11_College"
WHERE !completed AND semester = 5
SORT due ASC
```

---

## 🗂️ Syllabi Tracker (RPS Status)
```dataview
TABLE course, tags
FROM "10_Spaces/11_College/Syllabi"
WHERE semester = 5
```

---

## 🛠️ Quick Actions & Note Filing Rules
1. **New Lecture Note:** Use the `College_Lecture_Note` template in `99_Configs/Templates/` and file under `10_Spaces/11_College/<Course_Folder>/`.
2. **Uploading RPS / Syllabi:** Store in `10_Spaces/11_College/Syllabi/` using [Syllabus_Template.md](file:///mnt/data/life-hub/10_Knowledge_OS/10_Spaces/11_College/Syllabi/Syllabus_Template.md).
3. **Concept Extraction:** Extract core algorithms or security principles into atomic Concept notes in `20_Brain_Atlas/20_Concepts/<Subject>/`.
