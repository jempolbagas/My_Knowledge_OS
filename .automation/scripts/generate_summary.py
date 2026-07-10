import os
import re
import sqlite3
import json
from datetime import datetime, timezone

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
DB_PATH    = os.path.join(VAULT_ROOT, '.automation/db/vault_index.db')
OUT_JSON   = os.path.join(VAULT_ROOT, '.automation/reports/vault_summary.json')

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

SPACE_LABELS = {
    '11_College' : 'College',
    '12_Teaching': 'Teaching',
    '13_Olympiad': 'Olympiad',
}

SUBJECT_DIRS = [
    'Artificial_Intelligence', 'Computer_Science', 'Cybersecurity',
    'Mathematics', 'Software_Engineering', 'Web_Development',
]

def _infer_space(path: str) -> str | None:
    for key in SPACE_LABELS:
        if key in path:
            return key
    return None

def _infer_subject(path: str) -> str | None:
    for s in SUBJECT_DIRS:
        if s in path:
            return s
    return None

def _infer_topic(path: str) -> str:
    """Return a human-readable topic label from the folder segment below the space."""
    parts = path.replace('\\', '/').split('/')
    # e.g. 10_Spaces/11_College/Sem_4_Spring_2026/<TOPIC>/...
    # or   10_Spaces/12_Teaching/30_Sources/<TOPIC>/...
    # We want the first meaningful segment after the space identifier.
    idx = next((i for i, p in enumerate(parts)
                if any(k in p for k in SPACE_LABELS)), None)
    if idx is not None and idx + 2 < len(parts):
        raw = parts[idx + 2]          # e.g. "Discrete_Mathematics_I"
        return raw.replace('_', ' ')  # → "Discrete Mathematics I"
    return 'General'

# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build_summary():
    conn   = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ── Global stats ──────────────────────────────────────────────────────
    cursor.execute('SELECT COUNT(*) FROM nodes')
    total_notes = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM edges')
    total_edges = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM edges WHERE target_path IS NULL')
    broken_links = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM nodes WHERE type IS NULL")
    untyped_notes = cursor.fetchone()[0]

    # ── 10_Spaces breakdown ───────────────────────────────────────────────
    # Structure: { space_label: { topic: [note_title, ...] } }
    spaces_out: dict[str, dict[str, list[str]]] = {}

    cursor.execute("SELECT path, title FROM nodes WHERE path LIKE '10_Spaces%'")
    for path, title in cursor.fetchall():
        space_key = _infer_space(path)
        if space_key is None:
            continue
        label = SPACE_LABELS[space_key]
        topic = _infer_topic(path)
        # Skip if the inferred "topic" is actually a raw filename (shallow file)
        if topic.endswith('.md'):
            continue
        spaces_out.setdefault(label, {}).setdefault(topic, []).append(title)

    # ── 20_Brain_Atlas breakdown ──────────────────────────────────────────
    atlas_out: dict[str, dict] = {
        'library': {
            'Papers'           : [],
            'Repos'            : [],
            'Articles_Talks'   : [],
            'Books'            : [],
            'Generated_Readings': {},   # { subject: [titles] }
        },
        'concepts': {},   # { subject: [titles] }
        'reference_lib': [],
    }

    cursor.execute("SELECT path, title, type, status FROM nodes WHERE path LIKE '20_Brain_Atlas%'")
    for path, title, ntype, status in cursor.fetchall():
        p = path.replace('\\', '/')

        if '10_Library/Generated_Readings' in p:
            subj = _infer_subject(p) or 'General'
            atlas_out['library']['Generated_Readings'].setdefault(subj, []).append(title)

        elif '10_Library/Papers' in p:
            atlas_out['library']['Papers'].append({'title': title, 'status': status})

        elif '10_Library/Repos' in p:
            atlas_out['library']['Repos'].append({'title': title, 'status': status})

        elif '10_Library/Articles_Talks' in p:
            atlas_out['library']['Articles_Talks'].append({'title': title, 'status': status})

        elif '10_Library/Books' in p:
            atlas_out['library']['Books'].append({'title': title, 'status': status})

        elif '20_Concepts' in p:
            subj = _infer_subject(p) or 'General'
            atlas_out['concepts'].setdefault(subj, []).append(title)

        elif '30_Reference_Lib' in p:
            atlas_out['reference_lib'].append(title)

    # ── 00_Inbox ──────────────────────────────────────────────────────────
    cursor.execute("SELECT title FROM nodes WHERE path LIKE '00_Inbox%'")
    inbox_notes = [row[0] for row in cursor.fetchall()]

    # ── Orphan summary (titles only, not full paths) ──────────────────────
    cursor.execute('''
        SELECT title
        FROM nodes
        WHERE path NOT LIKE '%Dashboard%'
          AND path NOT LIKE '%Templates%'
          AND path NOT IN (
              SELECT DISTINCT target_path FROM edges WHERE target_path IS NOT NULL
          )
          AND path NOT IN (
              SELECT DISTINCT source_path FROM edges
          )
        LIMIT 30
    ''')
    orphan_titles = [row[0] for row in cursor.fetchall()]

    # ── Notes with missing `type` frontmatter ─────────────────────────────
    cursor.execute("SELECT title, path FROM nodes WHERE type IS NULL LIMIT 20")
    untyped_sample = [{'title': r[0], 'path': r[1]} for r in cursor.fetchall()]

    conn.close()

    # ── Assemble final document ───────────────────────────────────────────
    summary = {
        '_meta': {
            'description': (
                'Pre-computed vault digest for token-efficient agent queries. '
                'Read this file FIRST. Only open specific vault notes when the '
                'topic is confirmed to exist here.'
            ),
            'agent_protocol': [
                '1. Read vault_summary.json → identify which 1-3 notes are relevant.',
                '2. Open only those specific notes by their path.',
                '3. Prefer 20_Brain_Atlas/20_Concepts/ notes for explanations (smallest, most distilled).',
                '4. Never scan directories or open more than 3 full notes without user approval.',
                '5. If answering creates or updates a concept, compute its source MD5 and '
                   'save it as source_hash in the concept frontmatter.',
            ],
            'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        },
        'stats': {
            'total_notes'  : total_notes,
            'total_edges'  : total_edges,
            'broken_links' : broken_links,
            'untyped_notes': untyped_notes,
            'health_score' : round(
                100 * (1 - broken_links / max(total_edges, 1)) *
                      (1 - untyped_notes / max(total_notes, 1)),
                1
            ),
        },
        'inbox': inbox_notes,
        'spaces': spaces_out,
        'brain_atlas': atlas_out,
        'maintenance': {
            'orphan_pages_sample': orphan_titles,
            'untyped_notes_sample': untyped_sample,
        },
    }

    with open(OUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    note_count  = total_notes
    size_kb     = round(os.path.getsize(OUT_JSON) / 1024, 1)
    print(f"vault_summary.json generated — {note_count} notes summarised, {size_kb} KB")


if __name__ == '__main__':
    build_summary()
