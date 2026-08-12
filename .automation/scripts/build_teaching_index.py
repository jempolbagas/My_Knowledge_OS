#!/usr/bin/env python3
import os
import re
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
TEACHING_DIR = VAULT_ROOT / "10_Spaces" / "12_Teaching"
SOURCES_DIR = TEACHING_DIR / "30_Sources"
PRACTICE_DIR = TEACHING_DIR / "40_Practice"
INDEX_FILE = TEACHING_DIR / "00_Atlas" / "index_teaching.md"

LEVELS = ["SMP", "SMA"]

LEVEL_HEADERS = {
    "SMP": "# 🏫 SMP (Junior High School)",
    "SMA": "# 🎓 SMA (Senior High School)"
}

SUBJECT_METADATA = {
    "Biology": {"title": "🧬 Biology & Science (IPA)", "order": 1},
    "Mathematics": {"title": "📐 Mathematics", "order": 2},
    "Languages": {"title": "🗣️ Languages (English / ESL)", "order": 3},
    "Physics": {"title": "⚛️ Physics", "order": 4},
    "Economics": {"title": "📈 Economics", "order": 5},
    "Social_Studies": {"title": "🌍 Social Studies (IPS / Geografi)", "order": 6},
}

def extract_file_info(file_path: Path):
    """
    Extract stem, title/desc, and level (SMP or SMA) from file.
    """
    stem = file_path.stem
    if not file_path.exists():
        return stem, "", "SMP" if "_SMP" in stem else "SMA"
    
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return stem, "", "SMP" if "_SMP" in stem else "SMA"

    title = ""
    level = ""

    # Check YAML frontmatter
    fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        
        lvl_m = re.search(r'^level:\s*["\']?(.*?)["\']?$', fm, re.MULTILINE)
        if lvl_m:
            level = lvl_m.group(1).strip().upper()

        title_m = re.search(r'^title:\s*["\']?(.*?)["\']?$', fm, re.MULTILINE)
        if title_m:
            title = title_m.group(1).strip()
            title = re.sub(r'^(Materi Ajar|Materi Ajar Santai):\s*', '', title, flags=re.IGNORECASE)

    if not level:
        if "_SMP" in stem or "SMP" in content[:300]:
            level = "SMP"
        else:
            level = "SMA"

    if not title:
        h1_m = re.search(r'^#\s+(.*?)$', content, re.MULTILINE)
        if h1_m:
            title = h1_m.group(1).strip()

    if not title:
        title = stem.replace("_SMP", "").replace("_SMA", "").replace("_", " ")

    return stem, title, level

def generate_index():
    md_lines = [
        "---",
        'title: "🍎 Teaching Resources Hub"',
        'course: ""',
        "tags: [teaching, index, dashboard]",
        'aliases: ["🍎 Teaching Resources Hub"]',
        'created: "2026-05-01"',
        "---",
        "",
        "# 🍎 Teaching Resources Hub",
        "",
        "Selamat datang di Teaching Resources Hub! Halaman ini mengorganisir seluruh materi ajar (sources) dan lembar kerja siswa (practice) yang terbagi dengan rapi berdasarkan jenjang pendidikan **SMP** dan **SMA**.",
        "",
        "---",
        ""
    ]

    for level in LEVELS:
        md_lines.append(LEVEL_HEADERS[level])
        md_lines.append("")

        # Gather subjects that have files for this level
        subjects_found = set()
        if SOURCES_DIR.exists():
            subjects_found.update([d.name for d in SOURCES_DIR.iterdir() if d.is_dir()])
        if PRACTICE_DIR.exists():
            subjects_found.update([d.name for d in PRACTICE_DIR.iterdir() if d.is_dir()])

        def sort_key(s):
            return (SUBJECT_METADATA.get(s, {}).get("order", 99), s)

        sorted_subjects = sorted(list(subjects_found), key=sort_key)

        for subj in sorted_subjects:
            subj_meta = SUBJECT_METADATA.get(subj, {
                "title": f"📚 {subj.replace('_', ' ')}",
                "order": 99
            })
            header_title = subj_meta["title"]

            # 1. Sources / Materi Ajar for this level
            subj_sources_dir = SOURCES_DIR / subj
            sources_entries = []

            if subj_sources_dir.exists():
                for item in sorted(subj_sources_dir.iterdir(), key=lambda p: p.name):
                    if item.is_file() and item.suffix == ".md":
                        stem, desc, file_level = extract_file_info(item)
                        if file_level == level:
                            if desc and desc != stem:
                                sources_entries.append(f"- [[{stem}]] — {desc}")
                            else:
                                sources_entries.append(f"- [[{stem}]]")
                    elif item.is_dir():
                        # Modular topic folder
                        topic_files = sorted([f for f in item.iterdir() if f.is_file() and f.suffix == ".md"], key=lambda p: p.name)
                        
                        master_file = None
                        sub_files = []

                        for tf in topic_files:
                            stem, desc, file_level = extract_file_info(tf)
                            if file_level == level:
                                if stem in [item.name, f"{item.name}_{level}"]:
                                    master_file = tf
                                else:
                                    sub_files.append(tf)

                        if master_file:
                            stem, desc, _ = extract_file_info(master_file)
                            sources_entries.append(f"- 🏠 [[{stem}]] — {desc}")
                            for sf in sub_files:
                                s_stem, s_desc, _ = extract_file_info(sf)
                                if s_desc and s_desc != s_stem:
                                    sources_entries.append(f"  - 📄 [[{s_stem}]] — {s_desc}")
                                else:
                                    sources_entries.append(f"  - 📄 [[{s_stem}]]")
                        elif sub_files:
                            for idx, tf in enumerate(sub_files):
                                s_stem, s_desc, _ = extract_file_info(tf)
                                prefix = "🏠 " if idx == 0 else "  - 📄 "
                                indent = "- " if idx == 0 else ""
                                if s_desc and s_desc != s_stem:
                                    sources_entries.append(f"{indent}{prefix}[[{s_stem}]] — {s_desc}")
                                else:
                                    sources_entries.append(f"{indent}{prefix}[[{s_stem}]]")

            # 2. Practice / Lembar Kerja for this level
            subj_practice_dir = PRACTICE_DIR / subj
            practice_entries = []

            if subj_practice_dir.exists():
                for item in sorted(subj_practice_dir.iterdir(), key=lambda p: p.name):
                    if item.is_file() and item.suffix == ".md":
                        stem, desc, file_level = extract_file_info(item)
                        if file_level == level:
                            practice_entries.append(f"- [[{stem}]]")

            # Only render subject section if it has entries for this level
            if sources_entries or practice_entries:
                md_lines.append(f"## {header_title}")
                md_lines.append("")

                if sources_entries:
                    md_lines.append("### 📚 Materi Ajar (Sources)")
                    md_lines.extend(sources_entries)
                    md_lines.append("")

                if practice_entries:
                    md_lines.append("### 📝 Lembar Kerja (Practice)")
                    md_lines.extend(practice_entries)
                    md_lines.append("")

                md_lines.append("---")
                md_lines.append("")

    # Remove final duplicate trailing separator if present
    if md_lines and md_lines[-1] == "":
        md_lines.pop()
    if md_lines and md_lines[-1] == "---":
        md_lines.pop()

    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    INDEX_FILE.write_text("\n".join(md_lines).strip() + "\n", encoding="utf-8")
    print(f"Successfully generated teaching index: {INDEX_FILE}")

if __name__ == "__main__":
    generate_index()
