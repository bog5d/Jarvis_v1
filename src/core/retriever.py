import json
import os
from pathlib import Path

class Retriever:
    """
    The Librarian.
    Consults the 'knowledge_index.json' to find relevant documents 
    based on keywords/tags in the user query.
    """
    
    def __init__(self, index_path, root_dir):
        self.index_path = Path(index_path)
        self.root_dir = Path(root_dir)
        self.index = self._load_index()
        
    def _load_index(self):
        if not self.index_path.exists():
            print(f"[Warn] Index not found at {self.index_path}")
            return {"tags": {}, "file_map": {}}
        
        with open(self.index_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def find_relevant_files(self, query):
        """
        Simple keyword matching against indexed Tags.
        Returns a set of file paths (relative).
        """
        query_words = set(query.lower().split())
        found_files = set()
        
        # We look for exact matches between query words and Tags (case-insensitive)
        available_tags = self.index.get("tags", {})
        
        print(f"[*] Searching index for tags in: '{query}'")
        
        for tag, files in available_tags.items():
            if tag.lower() in query_words:
                print(f"  -> Found match on tag: #{tag}")
                found_files.update(files)
                
        return list(found_files)

    def get_context(self, file_paths):
        """
        Reads the actual content of the files.
        Returns a formatted context string.
        """
        context_parts = []
        for rel_path in file_paths:
            full_path = self.root_dir / rel_path
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    context_parts.append(f"--- DOCUMENT: {rel_path} ---\n{content}\n")
            except Exception as e:
                print(f"[Error] reading {rel_path}: {e}")
                
        return "\n".join(context_parts)

if __name__ == "__main__":
    # Test Run
    # Adjust paths to match workspace structure
    base_path = Path("D:/My_system/Jarvis_v1")
    retriever = Retriever(
        index_path=base_path / "data/knowledge_index.json",
        root_dir=base_path / "data/simulated_archive"
    )
    
    # Simulate a query
    q = "tell me about the Project Architecture and python"
    hits = retriever.find_relevant_files(q)
    print(f"Found {len(hits)} documents.")
    
    if hits:
        print(retriever.get_context(hits))
