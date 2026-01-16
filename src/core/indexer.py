import os
import re
import json
import yaml
from pathlib import Path
from datetime import datetime

class Indexer:
    """
    The Historian.
    Scans static markdown files, extracts metdata (Tags, Links), 
    and builds a lightweight JSON index.
    """
    
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.index = {
            "last_updated": None,
            "tags": {},     # "tag_name": ["file_path_1", "file_path_2"]
            "file_map": {}  # "file_path": {"title": "...", "mtime": ...}
        }
        
    def extract_metadata(self, content):
        """
        Extracts tags from Frontmatter and Inline content.
        Returns a set of tags.
        """
        tags = set()
        
        # 1. Frontmatter Parsing (YAML style between ---)
        frontmatter_match = re.search(r'^---\s+(.*?)\s+---', content, re.DOTALL)
        if frontmatter_match:
            try:
                fm_data = yaml.safe_load(frontmatter_match.group(1))
                if fm_data and 'tags' in fm_data:
                    if isinstance(fm_data['tags'], list):
                        tags.update(fm_data['tags'])
                    elif isinstance(fm_data['tags'], str):
                        # Handle comma separated strings
                        tags.update([t.strip() for t in fm_data['tags'].split(',')])
            except Exception as e:
                print(f"  [Warn] Failed to parse frontmatter: {e}")

        # 2. Inline Tag Parsing (#Tag)
        # Regex looks for #tag but avoids markdown headers (##), hex colors (#FFFFFF), or links
        # Simple implementation: #word characters
        inline_tags = re.findall(r'(?<!#)#([a-zA-Z0-9_\u4e00-\u9fa5]+)', content)
        tags.update(inline_tags)
        
        return list(tags)

    def scan(self):
        """
        Walks the directory and parses valid .md files.
        """
        print(f"[*] Scanning: {self.root_dir} ...")
        count = 0
        
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith(".md"):
                    file_path = Path(root) / file
                    rel_path = str(file_path.relative_to(self.root_dir)) # Store relative paths
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            
                        found_tags = self.extract_metadata(content)
                        
                        # Add to Index
                        self.index["file_map"][rel_path] = {
                            "mtime": os.path.getmtime(file_path),
                            "tags": found_tags
                        }
                        
                        for tag in found_tags:
                            if tag not in self.index["tags"]:
                                self.index["tags"][tag] = []
                            self.index["tags"][tag].append(rel_path)
                            
                        count += 1
                        
                    except Exception as e:
                        print(f"  [Error] reading {rel_path}: {e}")
        
        self.index["last_updated"] = datetime.now().isoformat()
        print(f"[+] Index built. Processed {count} files. Found {len(self.index['tags'])} unique tags.")
        return self.index

    def save(self, output_path="index.json"):
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, indent=2, ensure_ascii=False)
        print(f"[+] Index saved to: {output_path}")

if __name__ == "__main__":
    # Test run
    # Assuming 'data/simulated_archive' exists for testing
    indexer = Indexer("data/simulated_archive")
    indexer.scan()
    indexer.save("data/knowledge_index.json")
