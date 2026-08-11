#!/usr/bin/env python3
import os
import sys
import re
import argparse
import subprocess
import urllib.parse
from pathlib import Path
from PIL import Image

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
EXCLUDE_DIRS = {'.git', '.obsidian', '.automation', '.trash', 'node_modules', 'Archived_Assets'}

def parse_args():
    parser = argparse.ArgumentParser(description="Vault Asset Converter & Wikilink Refactor Tool")
    parser.add_argument("--assets-dir", default="30_Assets", help="Relative or absolute path to assets directory")
    parser.add_argument("--from-ext", default="jpg,jpeg,png", help="Comma-separated extensions to convert")
    parser.add_argument("--to-ext", default="webp", help="Target extension")
    parser.add_argument("--quality", type=int, default=82, help="WebP compression quality (1-100)")
    parser.add_argument("--dry-run", action="store_true", help="Preview conversion and refactoring without making changes")
    parser.add_argument("--keep-source", action="store_true", help="Do not delete original source image files after conversion")
    parser.add_argument("--no-sync", action="store_true", help="Skip running build_index.py after conversion")
    return parser.parse_args()

def get_vault_markdown_files(vault_root):
    md_files = []
    for root, dirs, files in os.walk(vault_root):
        rel_path = os.path.relpath(root, vault_root)
        if any(part in EXCLUDE_DIRS for part in Path(rel_path).parts):
            dirs.clear()
            continue
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def convert_image(src_path, target_ext, quality, dry_run=False):
    src_path = Path(src_path)
    dst_path = src_path.with_suffix('.' + target_ext.lstrip('.'))
    
    if src_path == dst_path:
        return None, 0, 0
    
    src_size = src_path.stat().st_size
    
    if dry_run:
        return dst_path, src_size, 0
        
    with Image.open(src_path) as img:
        if target_ext.lower() == 'webp':
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                img = img.convert('RGBA')
            else:
                img = img.convert('RGB')
            img.save(dst_path, 'WEBP', quality=quality, optimize=True)
        else:
            img.save(dst_path, quality=quality)
            
    dst_size = dst_path.stat().st_size
    return dst_path, src_size, dst_size

def refactor_links_in_notes(md_files, conversion_map, dry_run=False):
    expanded_map = {}
    for old_name, new_name in conversion_map.items():
        expanded_map[old_name] = new_name
        old_quoted = urllib.parse.quote(old_name)
        new_quoted = urllib.parse.quote(new_name)
        if old_quoted != old_name:
            expanded_map[old_quoted] = new_quoted
            
    updated_files_count = 0
    total_replacements = 0
    
    for md_path in md_files:
        try:
            with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {md_path}: {e}")
            continue
            
        new_content = content
        file_replacements = 0
        
        for old_name, new_name in expanded_map.items():
            if old_name not in new_content:
                continue
                
            # 1. Replace in Wikilinks [[...old_name...]] or ![[...old_name...]]
            wiki_pattern = re.compile(
                r'(\!?(?:\[\[))([^\]]*?)(' + re.escape(old_name) + r')([^\]]*?)(?:\]\])'
            )
            
            def replace_wiki(match):
                nonlocal file_replacements
                file_replacements += 1
                return f"{match.group(1)}{match.group(2)}{new_name}{match.group(4)}]]"
                
            new_content = wiki_pattern.sub(replace_wiki, new_content)
            
            # 2. Replace in Markdown links ![alt](path/old_name) where path is not http(s)
            md_pattern = re.compile(
                r'(\!?(?:\[[^\]]*?\]\()(?!https?://))([^\)]*?)(' + re.escape(old_name) + r')([^\)]*?\))'
            )
            
            def replace_md(match):
                nonlocal file_replacements
                file_replacements += 1
                return f"{match.group(1)}{match.group(2)}{new_name}{match.group(4)}"
                
            new_content = md_pattern.sub(replace_md, new_content)
            
        if file_replacements > 0:
            updated_files_count += 1
            total_replacements += file_replacements
            rel_note = os.path.relpath(md_path, VAULT_ROOT)
            print(f"  [Refactor] {rel_note} ({file_replacements} link(s) updated)")
            if not dry_run:
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
    return updated_files_count, total_replacements

def main():
    args = parse_args()
    
    # Resolve assets dir
    if os.path.isabs(args.assets_dir):
        assets_dir = Path(args.assets_dir)
    else:
        assets_dir = Path(VAULT_ROOT) / args.assets_dir
        
    if not assets_dir.exists():
        print(f"Error: Assets directory '{assets_dir}' does not exist.")
        sys.exit(1)
        
    from_exts = set(ext.strip().lower().lstrip('.') for ext in args.from_ext.split(','))
    to_ext = args.to_ext.strip().lower().lstrip('.')
    
    print(f"=== Knowledge OS Asset Converter & Link Refactor ===")
    print(f"Target Directory : {assets_dir}")
    print(f"Convert Formats  : {', '.join('.' + e for e in from_exts)} -> .{to_ext}")
    print(f"Mode             : {'DRY RUN (Preview)' if args.dry_run else 'LIVE EXECUTION'}")
    print("====================================================\n")
    
    # 1. Find images to convert
    images_to_convert = []
    for root, _, files in os.walk(assets_dir):
        for file in files:
            ext = Path(file).suffix.lower().lstrip('.')
            if ext in from_exts and ext != to_ext:
                images_to_convert.append(Path(root) / file)
                
    if not images_to_convert:
        print("No matching image assets found for conversion.")
        sys.exit(0)
        
    print(f"Found {len(images_to_convert)} image(s) to convert.\n")
    
    conversion_map = {} # {old_filename: new_filename}
    total_src_bytes = 0
    total_dst_bytes = 0
    converted_count = 0
    
    for img_path in images_to_convert:
        old_filename = img_path.name
        new_filename = img_path.with_suffix('.' + to_ext).name
        
        print(f"• Processing: {old_filename} -> {new_filename}")
        dst_path, src_size, dst_size = convert_image(img_path, to_ext, args.quality, dry_run=args.dry_run)
        
        if dst_path:
            conversion_map[old_filename] = new_filename
            total_src_bytes += src_size
            total_dst_bytes += dst_size
            converted_count += 1
            if not args.dry_run and not args.keep_source:
                try:
                    img_path.unlink()
                except Exception as e:
                    print(f"  Warning: Failed to remove original file {img_path}: {e}")
                    
    print("\n--- Refactoring Notes Tying to Assets ---")
    md_files = get_vault_markdown_files(VAULT_ROOT)
    updated_files_count, total_replacements = refactor_links_in_notes(md_files, conversion_map, dry_run=args.dry_run)
    
    print("\n=== Conversion Summary ===")
    print(f"Images Converted : {converted_count} file(s)")
    if not args.dry_run and total_src_bytes > 0:
        saved_bytes = total_src_bytes - total_dst_bytes
        saved_pct = (saved_bytes / total_src_bytes) * 100 if total_src_bytes > 0 else 0
        print(f"Original Size    : {total_src_bytes / 1024:.2f} KB")
        print(f"New Size         : {total_dst_bytes / 1024:.2f} KB")
        print(f"Storage Saved    : {saved_bytes / 1024:.2f} KB ({saved_pct:.1f}%)")
    print(f"Notes Updated    : {updated_files_count} note(s)")
    print(f"Links Refactored : {total_replacements} link(s)")
    
    # Trigger index build if not dry-run and not disabled
    if not args.dry_run and not args.no_sync:
        build_index_script = Path(VAULT_ROOT) / ".automation/scripts/build_index.py"
        if build_index_script.exists():
            print("\nRebuilding vault index...")
            subprocess.run([sys.executable, str(build_index_script)], check=False)
            
    print("\nOperation completed successfully.")

if __name__ == "__main__":
    main()
