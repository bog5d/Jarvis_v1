# -*- coding: utf-8 -*-
import sys
import os
import json
import random
from pathlib import Path
from datetime import datetime, timedelta

# Add project root to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config.system_config import DIR
from Jarvis_v1.utils.ai_brain import call_ai
from Jarvis_v1.utils.logger import setup_logger

logger = setup_logger("Gardener")

MEMORY_FILE = DIR['SYSTEM_ROOT'] / "memory.json"
INDEX_LIMIT_CHARS = 1000 

def build_index():
    """Builds a lightweight JSON index of the Knowledge Base."""
    logger.info("🧠 Building Memory Index...")
    
    # Scan multiple candidate locations (20_Knowledge_Base and Jarvis_Vault)
    kb_paths = []
    primary = DIR.get('KNOWLEDGE_BASE')
    if primary:
        kb_paths.append(primary)
    # Add a common vault folder at workspace root if exists
    vault_candidate = project_root / 'Jarvis_Vault'
    if vault_candidate.exists():
        kb_paths.append(vault_candidate)

    if not kb_paths:
        logger.warning("⚠️ No knowledge base paths configured/found.")
        return {}

    index = {}
    count = 0
    for kb_path in kb_paths:
        logger.info(f"🔍 Scanning: {kb_path}")
        if not kb_path.exists():
            logger.warning(f"⚠️ Path not found: {kb_path}")
            continue
        for file_path in kb_path.rglob("*.md"):
            try:
                stat = file_path.stat()
                mtime = datetime.fromtimestamp(stat.st_mtime)

                # Read snippet
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(INDEX_LIMIT_CHARS)

                index[str(file_path)] = {
                    "name": file_path.name,
                    "path": str(file_path),
                    "mtime": mtime.isoformat(),
                    "snippet": content.replace("\n", " ")[:500]
                }
                count += 1
            except Exception as e:
                logger.warning(f"Failed to index {file_path.name}: {e}")

    try:
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False, indent=2)
        logger.info(f"✅ Indexed {count} memories.")
    except Exception as e:
        logger.error(f"❌ Failed to save memory: {e}")
        
    return index

def get_briefing_file():
    """Finds today's briefing file."""
    today_str = datetime.now().strftime("%Y-%m-%d")
    briefing_filename = f"Daily_Briefing_{today_str}.md"
    
    # Check Inbox first (default location)
    briefing_path = DIR['INBOX'] / briefing_filename
    if briefing_path.exists():
        return briefing_path
    return None

def generate_review_summary(note_data):
    """Generates a nostalgic summary for an old note."""
    prompt = f"""
    You are 'The Gardener', a knowledge management AI. 
    You found this old note from the user's archive.
    
    Note: {note_data['name']}
    Date: {note_data['mtime']}
    Snippet: {note_data['snippet']}...
    
    Task:
    Write a 1-sentence "Memory Recall" teaser. 
    Why might this be interesting to look at again? 
    Start with "Do you remember..." or "On this day..." or similar nostalgic phrasing.
    Keep it under 30 words. Chinese.
    """
    return call_ai(prompt)

def daily_review():
    """The Gardener's daily routine."""
    logger.info("👨‍🌾 The Gardener is entering the garden...")
    
    # 1. Update Index
    memory_index = build_index()
    if not memory_index:
        return

    # 2. Find Target Briefing
    briefing_path = get_briefing_file()
    if not briefing_path:
        logger.info("📭 No Daily Briefing found to append to. (Secretary must run first)")
        return

    # 3. Random Recall
    items = list(memory_index.values())
    
    # Filter for older items (> 7 days)
    old_items = []
    now = datetime.now()
    cutoff = now - timedelta(days=7)
    
    for item in items:
        try:
            item_date = datetime.fromisoformat(item['mtime'])
            if item_date < cutoff:
                old_items.append(item)
        except:
            continue
            
    if not old_items:
        logger.info("🌱 Knowledge Base is too young for nostalgia (no notes > 7 days).")
        return

    # Pick up to 3 random notes
    sample_size = min(3, len(old_items))
    selected_items = random.sample(old_items, sample_size)
    
    logger.info(f"🏺 Recalling {len(selected_items)} old memories...")

    recall_section = "\n\n## 🏺 Rediscovered Knowledge (The Gardener)\n"
    recall_section += "> *Old notes surfaced to keep your memory fresh.*\n\n"

    for item in selected_items:
        summary = generate_review_summary(item)
        if not summary or "Error" in summary:
            summary = "Old note available for review."
            
        recall_section += f"* **[[{item['name']}]]** ({item['mtime'][:10]})\n"
        recall_section += f"  > *{summary.strip()}*\n"

    # 4. Append to Briefing
    try:
        with open(briefing_path, 'a', encoding='utf-8') as f:
            f.write(recall_section)
        logger.info(f"✅ Scaled the garden wall: Appended to {briefing_path.name}")
    except Exception as e:
        logger.error(f"❌ Failed to append review: {e}")

if __name__ == "__main__":
    daily_review()
