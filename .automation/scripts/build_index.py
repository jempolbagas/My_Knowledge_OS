import os
import re
import sqlite3
import frontmatter

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
DB_PATH = os.path.join(VAULT_ROOT, '.automation/db/vault_index.db')

# Regex for wikilinks: [[Note Name]] or [[Note Name|Alias]]
WIKILINK_RE = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')

# Matches markdown headings (# ... ######)
HEADING_RE = re.compile(r'^#{1,6}\s+', re.MULTILINE)

# Matches frontmatter-style callouts and blank lines
CALLOUT_RE = re.compile(r'^>\s*\[!', re.MULTILINE)

def get_relative_path(abs_path):
    return os.path.relpath(abs_path, VAULT_ROOT)

def extract_summary(content: str, max_chars: int = 280) -> str:
    """Return the first meaningful non-heading paragraph from a note body.
    Falls back to the first 280 characters of stripped content.
    """
    lines = content.splitlines()
    buffer = []
    for line in lines:
        stripped = line.strip()
        # Skip blank lines, headings, callout openers, and horizontal rules
        if not stripped or HEADING_RE.match(stripped) or CALLOUT_RE.match(stripped) or stripped.startswith('---'):
            if buffer:          # We had a paragraph building — stop here
                break
            continue
        buffer.append(stripped)
        if sum(len(l) for l in buffer) >= max_chars:
            break

    text = ' '.join(buffer).strip()
    if not text:
        text = content.strip()[:max_chars]
    return text[:max_chars]


def init_db(conn):
    cursor = conn.cursor()
    # Drop and recreate tables so schema changes (new columns) are always applied.
    # This is safe: the index is always a full rebuild from source files.
    cursor.execute('DROP TABLE IF EXISTS edges')
    cursor.execute('DROP TABLE IF EXISTS nodes')
    cursor.execute('''
        CREATE TABLE nodes (
            path TEXT PRIMARY KEY,
            title TEXT,
            type TEXT,
            status TEXT,
            notes_by TEXT,
            source_hash TEXT,
            summary TEXT,
            last_modified REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE edges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_path TEXT,
            target_name TEXT,
            target_path TEXT,
            link_type TEXT,
            FOREIGN KEY(source_path) REFERENCES nodes(path)
        )
    ''')
    conn.commit()

def scan_vault():
    md_files = {}
    title_to_path = {}
    
    # We scan 10_Spaces, 20_Brain_Atlas, and 00_Inbox
    for dir_name in ['10_Spaces', '20_Brain_Atlas', '00_Inbox']:
        dir_path = os.path.join(VAULT_ROOT, dir_name)
        if not os.path.exists(dir_path):
            continue
        for root, dirs, files in os.walk(dir_path):
            # Skip hidden dirs
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file.endswith('.md'):
                    abs_path = os.path.join(root, file)
                    rel_path = get_relative_path(abs_path)
                    title = os.path.splitext(file)[0]
                    md_files[rel_path] = abs_path
                    title_to_path[title] = rel_path
                    
    return md_files, title_to_path

def extract_links_from_string(text):
    if not isinstance(text, str):
        return []
    return [match.strip() for match in WIKILINK_RE.findall(text)]

def parse_frontmatter_links(fm, field_name):
    val = fm.get(field_name, '')
    if not val:
        return []
    links = []
    if isinstance(val, list):
        for item in val:
            links.extend(extract_links_from_string(item))
    elif isinstance(val, str):
        links.extend(extract_links_from_string(val))
    return links

def build_index():
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    cursor = conn.cursor()
    
    md_files, title_to_path = scan_vault()
    
    # First insert all nodes
    parsed_files = {}
    for rel_path, abs_path in md_files.items():
        try:
            with open(abs_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                
            metadata = post.metadata
            title = os.path.splitext(os.path.basename(abs_path))[0]
            mtime = os.path.getmtime(abs_path)
            
            summary = extract_summary(post.content)
            cursor.execute('''
                INSERT INTO nodes (path, title, type, status, notes_by, source_hash, summary, last_modified)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                rel_path,
                title,
                metadata.get('type'),
                metadata.get('status'),
                metadata.get('notes_by'),
                metadata.get('source_hash'),
                summary,
                mtime
            ))
            parsed_files[rel_path] = post
        except Exception as e:
            print(f"Error parsing {rel_path}: {e}")
            
    # Then insert all edges
    for rel_path, post in parsed_files.items():
        # Parse inline wikilinks
        inline_targets = WIKILINK_RE.findall(post.content)
        
        # Parse frontmatter links
        source_targets = parse_frontmatter_links(post.metadata, 'source')
        promoted_targets = parse_frontmatter_links(post.metadata, 'promoted_to')
        
        # Combine and record edges
        # We record target_path by matching title_to_path
        all_edges = []
        for target in inline_targets:
            all_edges.append((target.strip(), 'wikilink'))
        for target in source_targets:
            all_edges.append((target.strip(), 'frontmatter_source'))
        for target in promoted_targets:
            all_edges.append((target.strip(), 'frontmatter_promoted_to'))
            
        for target_name, link_type in all_edges:
            target_path = title_to_path.get(target_name, None)
            cursor.execute('''
                INSERT INTO edges (source_path, target_name, target_path, link_type)
                VALUES (?, ?, ?, ?)
            ''', (rel_path, target_name, target_path, link_type))
            
    conn.commit()
    conn.close()
    print("Database index successfully built!")

if __name__ == '__main__':
    build_index()
