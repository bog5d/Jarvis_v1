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
from Jarvis_v1.skills.ears import transcribe_audio

logger = setup_logger("Secretary")

def get_recent_files(folders, hours=72):
    """Get files modified within the last N hours."""
    recent_files = []
    cutoff_time = datetime.now() - timedelta(hours=hours)
    
    # Supported Extensions
    TEXT_EXT = ['.md', '.txt']
    AUDIO_EXT = ['.mp3', '.wav', '.m4a']
    
    for folder in folders:
        if not folder.exists():
            continue
            
        for item in folder.iterdir():
            if item.is_file():
                ext = item.suffix.lower()
                if ext in TEXT_EXT or ext in AUDIO_EXT:
                    mtime = datetime.fromtimestamp(item.stat().st_mtime)
                    if mtime > cutoff_time:
                        recent_files.append(item)
    return recent_files

def analyze_content(content, source_name):
    """Generic function to summarize text content using AI."""
    prompt = f"""
    You are an elite secretary. Analyze this content from {source_name}.
    
    Content:
    {content[:2000]} 
    
    Task:
    1. Summarize the main point in ONE concise sentence (Chinese).
    2. Extract any clear TODOs (if any).
    
    Format output strictly as:
    Summary: [Your summary] <!-- SEPARATOR --> TODOs: [Task 1, Task 2 or 'None']
    """
    
    response = call_ai(prompt)
    if response:
        return response
    return "Summary: Failed to analyze. <!-- SEPARATOR --> TODOs: None"

def process_file_item(file_path):
    """Route file to appropriate processor (Read or Listen)."""
    ext = file_path.suffix.lower()
    
    # A. Audio Files
    if ext in ['.mp3', '.wav', '.m4a']:
        logger.info(f"👂 Listening to audio: {file_path.name}")
        transcript = transcribe_audio(file_path)
        if transcript:
            logger.info(f"📝 Transcript generated for {file_path.name}")
            return analyze_content(transcript, f"Audio Note ({file_path.name})")
        else:
            return "Summary: Audio transcription failed. <!-- SEPARATOR --> TODOs: Check Logs"

    # B. Text Files
    else:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(1500)
            return analyze_content(content, f"Note ({file_path.name})")
        except Exception as e:
            logger.error(f"Failed to read {file_path.name}: {e}")
            return None

def run_secretary():
    logger.info("👩‍💼 Secretary starting daily briefing generation...")
    
    # 1. Identify Target Folders
    target_folders = [
        DIR['INBOX'] / 'Processed' / 'Notes',
        DIR['INBOX'] / 'Processed' / 'Documents',
        DIR['INBOX'] / 'Processed' / 'Audio', # New Audio Folder
        DIR['INBOX'] # Also scan root of inbox
    ]
    
    # 2. Find Recent Files
    files_to_process = get_recent_files(target_folders)
    
    if not files_to_process:
        logger.info("📭 No new notes or recordings found in the last 72h. Skipping briefing.")
        return

    logger.info(f"Found {len(files_to_process)} recent items. Analyzing...")

    # 3. Generate Content
    today_str = datetime.now().strftime("%Y-%m-%d")
    briefing_content = f"# 📅 Daily Briefing ({today_str})\n\n## 📝 New Notes & Recordings\n"
    
    for file_path in files_to_process:
        # Skip the briefing file itself
        if "Daily_Briefing" in file_path.name:
            continue
            
        logger.info(f"Processing: {file_path.name}...")
        ai_result = process_file_item(file_path)
        
        if ai_result:
            # Parse result
            if "<!-- SEPARATOR -->" in ai_result:
                summary, todos = ai_result.split("<!-- SEPARATOR -->")
                summary = summary.replace("Summary:", "").strip()
                todos = todos.replace("TODOs:", "").strip()
            else:
                summary = ai_result
                todos = "None"
            
            # Determine Icon based on type
            icon = "🎙️" if file_path.suffix.lower() in ['.mp3', '.wav', '.m4a'] else "📄"
            
            # Append to report
            item_link = f"[[{file_path.name}]]"
            briefing_content += f"### {icon} {item_link}\n"
            briefing_content += f"> 💡 **Summary**: {summary}\n"
            if todos and todos.lower() != "none" and todos.lower() != "check logs":
                briefing_content += f"> 🔴 **Action Items**: {todos}\n"
            briefing_content += "\n"

    # 4. Save Briefing
    output_path = DIR['INBOX'] / f"Daily_Briefing_{today_str}.md"
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(briefing_content)
        logger.info(f"✅ Briefing generated: {output_path}")
    except Exception as e:
        logger.error(f"❌ Failed to save briefing: {e}")

if __name__ == "__main__":
    run_secretary()
