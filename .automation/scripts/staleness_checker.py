import os
import sqlite3
import json
import hashlib
import re
import frontmatter

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
DB_PATH = os.path.join(VAULT_ROOT, '.automation/db/vault_index.db')
REPORT_JSON = os.path.join(VAULT_ROOT, '.automation/reports/stale_concepts.json')
REPORT_MD = os.path.join(VAULT_ROOT, '.automation/reports/stale_concepts.md')

WIKILINK_RE = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')

def get_md5(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error hashing {file_path}: {e}")
        return None

def check_staleness():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    stale_list = []
    
    # Query all concept nodes
    cursor.execute('''
        SELECT path, title, source_hash 
        FROM nodes 
        WHERE type = 'concept' OR path LIKE '%20_Concepts%'
    ''')
    concepts = cursor.fetchall()
    
    for concept_path, concept_title, stored_hash in concepts:
        abs_concept_path = os.path.join(VAULT_ROOT, concept_path)
        if not os.path.exists(abs_concept_path):
            continue
            
        try:
            post = frontmatter.load(abs_concept_path)
            meta = post.metadata
            source_raw = meta.get('source', '')
            
            if not source_raw:
                continue
                
            # Extract first wikilink target from the source field
            matches = WIKILINK_RE.findall(source_raw)
            if not matches:
                continue
            source_name = matches[0].strip()
            
            # Skip if the source is explicitly a PDF
            if source_name.lower().endswith('.pdf'):
                continue
                
            # Resolve the source note path
            cursor.execute('SELECT path FROM nodes WHERE title = ?', (source_name,))
            row = cursor.fetchone()
            if not row:
                continue
                
            source_rel_path = row[0]
            if source_rel_path.lower().endswith('.pdf'):
                continue
                
            abs_source_path = os.path.join(VAULT_ROOT, source_rel_path)
            if not os.path.exists(abs_source_path):
                continue
                
            current_hash = get_md5(abs_source_path)
            if not current_hash:
                continue
                
            # Check for missing or mismatching hash snapshot
            concept_stored_hash = meta.get('source_hash', '')
            if not concept_stored_hash or concept_stored_hash != current_hash:
                stale_list.append({
                    "concept_file": concept_path,
                    "concept_title": concept_title,
                    "source_file": source_rel_path,
                    "source_title": source_name,
                    "stored_hash": concept_stored_hash,
                    "current_hash": current_hash,
                    "status": "missing_hash" if not concept_stored_hash else "outdated"
                })
        except Exception as e:
            print(f"Error checking staleness for {concept_path}: {e}")
            
    # Write JSON report
    with open(REPORT_JSON, 'w', encoding='utf-8') as f:
        json.dump(stale_list, f, indent=2)
        
    # Write MD report
    with open(REPORT_MD, 'w', encoding='utf-8') as f:
        f.write("# Knowledge OS Staleness Checker Report\n\n")
        f.write("Detected when a source file has changed since the Concept wiki page was generated from it.\n\n")
        
        if stale_list:
            f.write("| Concept Note | Source Note | Status | Action Required |\n")
            f.write("| --- | --- | --- | --- |\n")
            for item in stale_list:
                status_lbl = "⚠️ Outdated" if item["status"] == "outdated" else "❓ No Snapshot Hash"
                f.write(f"| [[{item['concept_title']}]] | [[{item['source_title']}]] | {status_lbl} | Run LLM review to update concept and update `source_hash: \"{item['current_hash']}\"` |\n")
        else:
            f.write("All concept notes are fresh and up-to-date with their sources! 🎉\n")
            
    conn.close()
    print("Staleness checker report generated successfully!")

if __name__ == '__main__':
    check_staleness()
