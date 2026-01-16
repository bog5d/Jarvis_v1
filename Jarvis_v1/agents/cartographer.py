import sys
import os
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

logger = setup_logger("Cartographer")

def get_recent_notes(folder, hours=24):
    """Get markdown notes modified within the last N hours."""
    recent_notes = []
    cutoff_time = datetime.now() - timedelta(hours=hours)
    
    if not folder.exists():
        return []
        
    for item in folder.iterdir():
        if item.is_file() and item.suffix.lower() == '.md':
            # Skip Briefings to avoid self-loop
            if "Daily_Briefing" in item.name:
                continue
                
            mtime = datetime.fromtimestamp(item.stat().st_mtime)
            if mtime > cutoff_time:
                recent_notes.append(item)
    return recent_notes

def generate_diagram(file_path):
    """Ask AI to generate Mermaid diagram based on note content."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(2000) # Read first 2000 chars
            
        # Check if already has mermaid (simple check)
        if "```mermaid" in content:
            logger.info(f"Skipping {file_path.name}: Mermaid diagram already exists.")
            return None
            
        prompt = f"""
        You are an expert Data Visualizer. Analyze this note content.
        
        Content:
        {content}
        
        Task:
        Determine if this content describes a Process (Flowchart), Hierarchy (Mindmap), or Timeline.
        
        If YES:
        Result strictly a valid Mermaid.js code block. Use 'graph TD' for processes, 'mindmap' for hierarchies.
        Wrap it in standard markdown code block: ```mermaid ... ```.
        
        If NO (implied simple text):
        Return exactly: SKIP
        """
        
        response = call_ai(prompt)
        
        if response and "```mermaid" in response:
            return response
        elif "SKIP" in response:
            return None
        return None
        
    except Exception as e:
        logger.error(f"Failed to analyze {file_path.name}: {e}")
        return None

def append_diagram(file_path, diagram_code):
    """Append the diagram to the file."""
    try:
        # Check if we need a newline
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            last_char = lines[-1][-1] if lines and lines[-1] else '\n'
            
        prefix = "\n" if last_char == '\n' else "\n\n"
        
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"{prefix}## 🧠 Auto-Visualized Structure\n")
            f.write(diagram_code)
            f.write("\n")
            
        logger.info(f"📊 Diagram appended to: {file_path.name}")
        return True
    except Exception as e:
        logger.error(f"Failed to write to {file_path.name}: {e}")
        return False

def run_cartographer():
    logger.info("🎨 Cartographer starting visualization scan...")
    
    # 1. Target Folder
    notes_folder = DIR['INBOX'] / 'Processed' / 'Notes'
    
    # 2. Find Recent Notes
    # Expanded lookback to 72h to match Secretary logic for demo purposes
    files_to_process = get_recent_notes(notes_folder, hours=72)
    
    if not files_to_process:
        logger.info("📭 No new notes found to visualize.")
        return

    logger.info(f"Scanning {len(files_to_process)} notes for visualization candidates...")

    count = 0
    for file_path in files_to_process:
        diagram = generate_diagram(file_path)
        
        if diagram:
            if append_diagram(file_path, diagram):
                count += 1
    
    logger.info(f"🏁 Cartographer finished. Generated {count} diagrams.")

if __name__ == "__main__":
    run_cartographer()
