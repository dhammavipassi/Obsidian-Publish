#!/usr/bin/env python3

import os
import json
import re
from pathlib import Path

def extract_title_and_links(file_path):
    """Extract title and wikilinks from markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
        except UnicodeDecodeError:
            print(f"Warning: Could not read {file_path} due to encoding issues")
            return None, []
    
    # Extract title (first H1 or filename)
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()
    else:
        title = file_path.stem
    
    # Extract wikilinks [[link]] or [[link|text]]
    wikilinks = re.findall(r'\[\[([^\|\]]+)(?:\|[^\]]+)?\]\]', content)
    wikilinks = [link.strip() for link in wikilinks]
    
    return title, wikilinks

def generate_notes_graph():
    """Generate notes graph data"""
    notes_dir = Path('_notes')
    
    if not notes_dir.exists():
        print("Warning: _notes directory not found")
        # Create empty graph
        graph_data = {'nodes': [], 'links': []}
    else:
        notes = {}
        links = []
        
        # Process all markdown files
        for file_path in notes_dir.glob('*.md'):
            note_id = file_path.stem
            title, wikilinks = extract_title_and_links(file_path)
            
            if title is None:
                continue
                
            notes[note_id] = {
                'id': note_id,
                'title': title,
                'url': f'/{note_id}'
            }
            
            # Create links
            for link in wikilinks:
                # Try to find target note
                if f"{link}.md" in [f.name for f in notes_dir.glob('*.md')]:
                    links.append({
                        'source': note_id,
                        'target': link
                    })
        
        graph_data = {
            'nodes': list(notes.values()),
            'links': links
        }
        
        print(f"Generated graph with {len(notes)} notes and {len(links)} links")
    
    # Ensure output directory exists
    includes_dir = Path('_includes')
    includes_dir.mkdir(exist_ok=True)
    
    # Write JSON file
    output_file = includes_dir / 'notes_graph.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
    
    print(f"Graph data written to {output_file}")

if __name__ == '__main__':
    generate_notes_graph()