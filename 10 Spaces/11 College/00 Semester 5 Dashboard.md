---
title: "Semester 5 Dashboard (Gasal 2026/2027)"
type: Dashboard
semester: 5
academic_year: "2026/2027"
tags: ["college", "semester-5", "dashboard"]
created: "2026-07-27"
updated: "2026-08-13"
---

# 🎓 Semester 5 Hub & Operations (Gasal 2026/2027)

> [!success] **Semester Status:** Official KRS Approved & Active (22 SKS / 33.00 ECTS)
> Central command dashboard for all 8 official courses in Semester 5 Gasal 2026/2027.
> 📄 **Official KRS Record:** [[Official KRS Semester 5|Kartu Rencana Studi (KRS) Smt 5]]
> 📋 **Preparation Guide:** [[Semester 5 Prep|Semester 5 Preparation Guide]]

---

## 🎯 Academic Goals & Milestones
- **Target GPA / IPK:** 3.80+
- **Focus Areas:** Distributed Systems, Computer Vision, Digital Signal Processing, Biomedical Computing, & Technopreneurship.
- **Key Calendar Dates:**
  - **KRS Approval:** ✅ Completed (`2026-08-13`) — 22 SKS Approved
  - **Midterm Exams (UTS):** October 2026
  - **Final Exams (UAS):** December 2026 / January 2027

---

## 📚 Official KRS Course Directory (Semester 5)

| MK Code | Abbr | Course Name | Sec | SKS | ECTS | Course Hub | Syllabus (RPS) |
| :---: | :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| `12013130344` | **BIOCOMP** | Komputasi Biomedik | A | 3 | 4.50 | [[Biomedical Computing Overview]] | [[BioComp Syllabus]] |
| `12013120332` | **IMPROC** | Pengolahan Citra Digital | B | 3 | 4.50 | [[Image Processing Overview]] | [[Improc Syllabus]] |
| `12013120333` | **DISTSYS** | Sistem Terdistribusi | B | 3 | 4.50 | [[Distributed Systems Overview]] | [[DistSys Syllabus]] |
| `12013120231` | **HCI** | Interaksi Manusia & Komputer | B | 2 | 3.00 | [[HCI Overview]] | [[HCI Syllabus]] |
| `12013140310` | **COMVIS** | Computer Vision | A | 3 | 4.50 | [[Computer Vision Overview]] | [[ComVis Syllabus]] |
| `12013140302` | **SIGPRO** | Pengolahan Sinyal Digital | A | 3 | 4.50 | [[Digital Signal Processing Overview]] | [[SigPro Syllabus]] |
| `12013220330` | **DATMIN** | Data Mining | C | 3 | 4.50 | [[Data Mining Overview]] | [[DatMin Syllabus]] |
| `12013120203` | **ENTRE** | Kewirausahaan | A2 | 2 | 3.00 | [[Entrepreneurship Overview]] | [[Entre Syllabus]] |
| **TOTAL** | | **8 Mata Kuliah** | | **22** | **33.00** | | |

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
1. **New Lecture Note:** Follow `college-study-pack` skill guidelines under `10_Spaces/11_College/<Course_Folder>/Week_<XX>_<Topic_Snake_Case>/`.
2. **Uploading RPS / Syllabi:** Store in `10_Spaces/11_College/Syllabi/` using [Syllabus_Template.md](file:///mnt/data/life-hub/10_Knowledge_OS/10_Spaces/11_College/Syllabi/Syllabus_Template.md).
3. **Concept Extraction:** Extract core algorithms into atomic Concept notes in `20_Brain_Atlas/20_Concepts/<Subject>/`.
