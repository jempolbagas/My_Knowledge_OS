import os
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
        "missing_frontmatter": []
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
            if '20_Concepts' in rel_path:
                if meta.get('type') != 'concept':
                    missing.append("type (should be 'concept')")
                for field in ['title', 'subject', 'date_created', 'source']:
                    if field not in meta:
                        missing.append(field)
            elif '10_Library' in rel_path:
                t = meta.get('type')
                if t == 'generated_reading':
                    for field in ['title', 'topic', 'requested_on', 'prompt', 'status', 'tags', 'promoted_to']:
                        if field not in meta:
                            missing.append(field)
                elif t in ['repo', 'paper', 'article', 'book', 'talk']:
                    for field in ['title', 'source_url', 'author', 'date_added', 'status', 'notes_by', 'tags', 'promoted_to']:
                        if field not in meta:
                            missing.append(field)
                else:
                    missing.append("type (should be repo/paper/article/book/talk/generated_reading)")
            
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
            
    conn.close()
    print("Structural linter report generated successfully!")

if __name__ == '__main__':
    check_integrity()
