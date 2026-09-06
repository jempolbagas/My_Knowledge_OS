import os
import re
import sqlite3
import json
import frontmatter

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
DB_PATH = os.path.join(VAULT_ROOT, '.automation/db/vault_index.db')
REPORT_JSON = os.path.join(VAULT_ROOT, '.automation/reports/linter_report.json')
REPORT_MD = os.path.join(VAULT_ROOT, '.automation/reports/linter_report.md')

def check_integrity():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    errors = {
        "broken_links": [],
        "orphans": [],
        "missing_frontmatter": [],
        "malformed_math_blocks": []
    }
    
    # 1. Detect Broken Links
    cursor.execute('''
        SELECT source_path, target_name, link_type 
        FROM edges 
        WHERE target_path IS NULL
    ''')
    for row in cursor.fetchall():
        source_path, target_name, link_type = row
        # Skip web URLs or media references in wikilinks
        if target_name.startswith('http://') or target_name.startswith('https://'):
            continue
        if any(target_name.lower().endswith(ext) for ext in ['.pdf', '.png', '.jpg', '.jpeg', '.gif', '.mp3', '.mp4', '.zip']):
            continue
        errors["broken_links"].append({
            "file": source_path,
            "broken_link": target_name,
            "context": link_type
        })
        
    # 2. Detect Orphans (in Brain Atlas or Spaces)
    # A node is an orphan if it has no incoming links AND no outgoing links
    cursor.execute('''
        SELECT path, title 
        FROM nodes 
        WHERE path NOT LIKE '%Dashboard%' 
          AND path NOT LIKE '%Templates%' 
          AND path NOT IN (
              SELECT DISTINCT target_path FROM edges WHERE target_path IS NOT NULL
          )
          AND path NOT IN (
              SELECT DISTINCT source_path FROM edges
          )
    ''')
    for row in cursor.fetchall():
        path, title = row
        errors["orphans"].append({
            "file": path,
            "title": title
        })
        
    # 3. Check Frontmatter Fields
    cursor.execute('SELECT path, type FROM nodes')
    for row in cursor.fetchall():
        rel_path, note_type = row
        abs_path = os.path.join(VAULT_ROOT, rel_path)
        if not os.path.exists(abs_path):
            continue
            
        try:
            post = frontmatter.load(abs_path)
            meta = post.metadata
            missing = []
            
            # Determine expectations based on file location
            if '20 Notes' in rel_path:
                if meta.get('type') != 'note':
                    missing.append("type (should be 'note')")
                for field in ['title', 'created']:
                    if field not in meta:
                        missing.append(field)
            
            if missing:
                errors["missing_frontmatter"].append({
                    "file": rel_path,
                    "missing_fields": missing
                })
        except Exception as e:
            errors["missing_frontmatter"].append({
                "file": rel_path,
                "error": str(e)
            })
            
    # 4. Check Math Blocks (Quartz/KaTeX Display Math Compliance)
    open_math_re = re.compile(r"^(\s*(?:>\s*)*)\$\$(?!\$)(.+)$")
    close_math_re = re.compile(r"^(\s*(?:>\s*)*)(.*\S.*)\$\$\s*$")
    standalone_fence_re = re.compile(r"^\s*(?:>\s*)*\$\$\s*$")

    cursor.execute('SELECT path FROM nodes')
    for row in cursor.fetchall():
        rel_path = row[0]
        abs_path = os.path.join(VAULT_ROOT, rel_path)
        if not os.path.exists(abs_path) or not abs_path.endswith('.md'):
            continue
            
        try:
            with open(abs_path, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
                
            in_code = False
            in_math = False
            math_start_line = -1
            
            for idx, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith("```"):
                    in_code = not in_code
                    continue
                if in_code:
                    continue
                
                clean = re.sub(r"`[^`]+`", "", line)
                if not in_math:
                    m_open = open_math_re.match(clean)
                    if m_open:
                        if "$$" not in m_open.group(2):
                            in_math = True
                            math_start_line = idx + 1
                            errors["malformed_math_blocks"].append({
                                "file": rel_path,
                                "line": idx + 1,
                                "type": "Opening line contains formula text",
                                "snippet": line.strip()
                            })
                    elif standalone_fence_re.match(clean):
                        in_math = True
                        math_start_line = idx + 1
                else:
                    if standalone_fence_re.match(clean):
                        in_math = False
                    else:
                        m_close = close_math_re.match(clean)
                        if m_close and "$$" not in m_close.group(2).strip():
                            in_math = False
                            errors["malformed_math_blocks"].append({
                                "file": rel_path,
                                "line": idx + 1,
                                "type": "Closing line contains formula text",
                                "snippet": line.strip()
                            })
                            
            if in_math:
                errors["malformed_math_blocks"].append({
                    "file": rel_path,
                    "line": math_start_line,
                    "type": "Unclosed math block",
                    "snippet": lines[math_start_line - 1].strip() if 0 <= math_start_line - 1 < len(lines) else ""
                })
        except Exception:
            pass

    # Write JSON report
    with open(REPORT_JSON, 'w', encoding='utf-8') as f:
        json.dump(errors, f, indent=2)
        
    # Write MD report
    with open(REPORT_MD, 'w', encoding='utf-8') as f:
        f.write("# Knowledge OS Structural Linter Report\n\n")
        
        # Broken links
        f.write("## 🔗 Broken Links\n")
        if errors["broken_links"]:
            f.write("| File | Broken Link Target | Context |\n")
            f.write("| --- | --- | --- |\n")
            for item in errors["broken_links"]:
                f.write(f"| [[{os.path.splitext(os.path.basename(item['file']))[0]}]] | `{item['broken_link']}` | `{item['context']}` |\n")
        else:
            f.write("No broken links found! 🎉\n")
        f.write("\n")
        
        # Orphans
        f.write("## 🕳️ Orphan Pages (Disconnected Nodes)\n")
        if errors["orphans"]:
            f.write("These files have no incoming or outgoing links:\n")
            for item in errors["orphans"]:
                f.write(f"- [[{item['title']}]] (`{item['file']}`)\n")
        else:
            f.write("No orphan pages found! 🎉\n")
        f.write("\n")
        
        # Frontmatter
        f.write("## 📄 Missing/Invalid Frontmatter Properties\n")
        if errors["missing_frontmatter"]:
            f.write("| File | Missing/Invalid Fields |\n")
            f.write("| --- | --- |\n")
            for item in errors["missing_frontmatter"]:
                fields_str = ", ".join(item.get("missing_fields", [])) if "missing_fields" in item else f"Error: {item.get('error')}"
                f.write(f"| [[{os.path.splitext(os.path.basename(item['file']))[0]}]] | `{fields_str}` |\n")
        else:
            f.write("All frontmatter schemas are valid! 🎉\n")
        f.write("\n")

        # Math Blocks
        f.write("## 📐 Math Blocks (Quartz/KaTeX Compliance)\n")
        if errors["malformed_math_blocks"]:
            f.write("Multiline math blocks must have opening `$$` and closing `$$` on their own lines:\n\n")
            f.write("| File | Line | Issue | Snippet |\n")
            f.write("| --- | --- | --- | --- |\n")
            for item in errors["malformed_math_blocks"]:
                note_name = os.path.splitext(os.path.basename(item['file']))[0]
                f.write(f"| [[{note_name}]] | `{item['line']}` | {item['type']} | `{item['snippet']}` |\n")
        else:
            f.write("All math blocks are properly formatted! 🎉\n")
        f.write("\n")
            
    conn.close()
    print("Structural linter report generated successfully!")

if __name__ == '__main__':
    check_integrity()
