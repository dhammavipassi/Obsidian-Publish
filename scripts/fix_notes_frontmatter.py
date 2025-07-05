#!/usr/bin/env python3

import os
import re
from pathlib import Path

def fix_note_frontmatter(file_path):
    """Fix frontmatter for Jekyll notes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
        except UnicodeDecodeError:
            print(f"Warning: Could not read {file_path} due to encoding issues")
            return False
    
    # Extract title from filename
    title = file_path.stem
    
    # Check if already has proper frontmatter
    if content.startswith('---') and '---' in content[3:]:
        parts = content.split('---', 2)
        if len(parts) >= 3:
            # Already has frontmatter, check if it has title
            frontmatter = parts[1]
            if 'title:' not in frontmatter:
                # Add title to existing frontmatter
                new_frontmatter = frontmatter.strip() + f'\ntitle: "{title}"'
                new_content = f"---\n{new_frontmatter}\n---{parts[2]}"
            else:
                return False  # Already has proper frontmatter
        else:
            # Malformed frontmatter, recreate
            new_content = f"""---
title: "{title}"
layout: note
---

{content}"""
    else:
        # No frontmatter, add it
        new_content = f"""---
title: "{title}"
layout: note
---

{content}"""
    
    # Write back the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Fixed: {file_path.name}")
    return True

def main():
    """Fix all notes in _notes directory"""
    notes_dir = Path('_notes')
    
    if not notes_dir.exists():
        print("Error: _notes directory not found")
        return
    
    fixed_count = 0
    for file_path in notes_dir.glob('*.md'):
        if fix_note_frontmatter(file_path):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} notes")

if __name__ == '__main__':
    main()