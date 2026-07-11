import os
import re
import sqlite3
import frontmatter

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
DB_PATH = os.path.join(VAULT_ROOT, '.automation/db/vault_index.db')

# Regex for wikilinks: [[Note Name]] or [[Note Name|Alias]]
WIKILINK_RE = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')

# Splits a raw wikilink target into (note_name, anchor).
# Handles: "Note Name", "Note Name#Heading", "Note Name#^blockid", "#Heading" (same-note anchor)
# Anchor split is on the FIRST unescaped '#' only — headings can legitimately contain
# further '#' characters in edge cases, and we never want to over-split.
ANCHOR_SPLIT_RE = re.compile(r'^([^#]*)(#.*)?$')

def split_wikilink_target(raw_target: str):
    raw_target = raw_target.strip()
    m = ANCHOR_SPLIT_RE.match(raw_target)
    note_name = m.group(1).strip()
    anchor = m.group(2)  # includes leading '#', or None
    return note_name, anchor

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
    """Returns list of (note_name, anchor) tuples. note_name == '' means
    a same-note heading/block anchor like [[#Some Heading]]."""
    if not isinstance(text, str):
        return []
    raw_targets = WIKILINK_RE.findall(text)
    return [split_wikilink_target(t) for t in raw_targets]

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
        inline_targets = extract_links_from_string(post.content)

        # Parse frontmatter links
        source_targets = parse_frontmatter_links(post.metadata, 'source')
        promoted_targets = parse_frontmatter_links(post.metadata, 'promoted_to')

        all_edges = []
        for note_name, anchor in inline_targets:
            all_edges.append((note_name, anchor, 'wikilink'))
        for note_name, anchor in source_targets:
            all_edges.append((note_name, anchor, 'frontmatter_source'))
        for note_name, anchor in promoted_targets:
            all_edges.append((note_name, anchor, 'frontmatter_promoted_to'))

        for note_name, anchor, link_type in all_edges:
            if note_name == '':
                # Same-note anchor, e.g. [[#Some Heading]] — resolves to this file itself.
                target_path = rel_path
                target_name = rel_path  # store resolved name, not blank
            else:
                target_path = title_to_path.get(note_name, None)
                target_name = note_name

            cursor.execute('''
                INSERT INTO edges (source_path, target_name, target_path, link_type)
                VALUES (?, ?, ?, ?)
            ''', (rel_path, target_name, target_path, link_type))
            
    conn.commit()
    conn.close()
    print("Database index successfully built!")

if __name__ == '__main__':
    build_index()
