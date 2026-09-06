#!/usr/bin/env python3
"""
fix_math_blocks.py — Ensures multiline LaTeX display math blocks ($$) are Quartz & KaTeX compliant.
Quartz (remark-math / micromark-extension-math) requires that multiline math block delimiters ($$)
must each be placed on their own separate line without text attached to them.
"""

import os
import re
import sys
import argparse

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

OPEN_MATH_RE = re.compile(r"^(\s*(?:>\s*)*)\$\$(?!\$)(.+)$")
CLOSE_MATH_RE = re.compile(r"^(\s*(?:>\s*)*)(.*\S.*)\$\$\s*$")
STANDALONE_FENCE_RE = re.compile(r"^\s*(?:>\s*)*\$\$\s*$")


def fix_content(content: str) -> tuple[str, int]:
    """
    Normalizes multiline display math blocks so opening $$ and closing $$
    are on their own separate lines.
    Returns (fixed_content, num_fixes).
    """
    lines = content.split("\n")
    new_lines = []
    in_block = False
    fixes_count = 0

    for line in lines:
        clean = re.sub(r"`[^`]+`", "", line)

        m_open = OPEN_MATH_RE.match(line)
        m_close = CLOSE_MATH_RE.match(line)

        if not in_block:
            if m_open and "$$" not in m_open.group(2):
                in_block = True
                fixes_count += 1
                prefix = m_open.group(1)
                formula_start = m_open.group(2)
                new_lines.append(f"{prefix}$$")
                new_lines.append(f"{prefix}{formula_start}")
            elif STANDALONE_FENCE_RE.match(clean):
                in_block = True
                new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            if STANDALONE_FENCE_RE.match(clean):
                in_block = False
                new_lines.append(line)
            elif m_close and "$$" not in m_close.group(2).strip():
                in_block = False
                fixes_count += 1
                prefix = m_close.group(1)
                formula_end = m_close.group(2).rstrip()
                new_lines.append(f"{prefix}{formula_end}")
                new_lines.append(f"{prefix}$$")
            else:
                new_lines.append(line)

    return "\n".join(new_lines), fixes_count


def scan_and_fix(files: list[str], check_only: bool = False, verbose: bool = True) -> int:
    issues_found = 0
    files_fixed = 0

    for path in files:
        if not os.path.exists(path) or not path.endswith('.md'):
            continue

        with open(path, "r", encoding="utf-8", errors="replace") as f:
            orig = f.read()

        fixed, num_fixes = fix_content(orig)
        if num_fixes > 0:
            issues_found += num_fixes
            rel = os.path.relpath(path, VAULT_ROOT)
            if check_only:
                if verbose:
                    print(f"[FAIL] {rel}: {num_fixes} malformed delimiter(s)")
            else:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(fixed)
                files_fixed += 1
                if verbose:
                    print(f"[FIXED] {rel} ({num_fixes} delimiter(s) normalized)")

    if verbose:
        if check_only:
            if issues_found == 0:
                print("All math blocks are compliant! 🎉")
            else:
                print(f"Total malformed delimiter(s) detected: {issues_found}")
        else:
            if files_fixed == 0:
                print("All math blocks are compliant. No fixes needed. 🎉")
            else:
                print(f"Successfully fixed {files_fixed} file(s) ({issues_found} delimiter(s)).")

    return 1 if (check_only and issues_found > 0) else 0


def collect_vault_files(include_archive: bool = False) -> list[str]:
    dirs = ['10 Spaces', '20 Brain Atlas', '00 Inbox']
    if include_archive:
        dirs.append('90 Archive')

    collected = []
    for d in dirs:
        dpath = os.path.join(VAULT_ROOT, d)
        if not os.path.exists(dpath):
            continue
        for root, _, fnames in os.walk(dpath):
            for fn in fnames:
                if fn.endswith('.md'):
                    collected.append(os.path.join(root, fn))
    return sorted(collected)


def main():
    parser = argparse.ArgumentParser(description="Auto-fix or check Quartz/KaTeX multiline math block formatting.")
    parser.add_argument("--check", action="store_true", help="Dry-run check only; returns non-zero if defects are found.")
    parser.add_argument("--all", action="store_true", help="Include 90 Archive in scan.")
    parser.add_argument("--files", nargs="*", help="Specific files to check/fix.")
    parser.add_argument("--quiet", action="store_true", help="Suppress output except errors.")
    args = parser.parse_args()

    if args.files:
        target_files = [os.path.abspath(f) for f in args.files]
    else:
        target_files = collect_vault_files(include_archive=args.all)

    exit_code = scan_and_fix(target_files, check_only=args.check, verbose=not args.quiet)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
