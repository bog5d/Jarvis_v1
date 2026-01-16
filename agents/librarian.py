import os
import shutil
import sys
from pathlib import Path
from datetime import datetime

# Add project root to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config.system_config import DIR, ACCEPTED_TYPES
from Jarvis_v1.utils.logger import setup_logger

logger = setup_logger("Librarian")

def get_file_category(extension):
    """Determine category based on extension."""
    ext = extension.lower()
    for category, extensions in ACCEPTED_TYPES.items():
        if ext in extensions:
            return category.capitalize() # e.g. "Images"
    return "Others"

def run_librarian():
    inbox_path = DIR["INBOX"]
    
    logger.info(f"📚 Librarian starting work in: {inbox_path}")
    
    if not inbox_path.exists():
        logger.error(f"Inbox directory not found: {inbox_path}")
        return

    # Create Processed folder structure root
    processed_base = inbox_path / "Processed"
    processed_base.mkdir(exist_ok=True)

    moved_count = 0
    
    # Iterate over files in Inbox
    for item in inbox_path.iterdir():
        if item.is_dir():
            continue
            
        if item.name == ".DS_Store" or item.name == "desktop.ini":
            continue

        # Categorize
        category = get_file_category(item.suffix)
        
        # Prepare destination folder: Inbox/Processed/{Category}
        dest_folder = processed_base / category
        dest_folder.mkdir(parents=True, exist_ok=True)
        
        dest_path = dest_folder / item.name
        
        # Handle Duplicates
        if dest_path.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_name = f"{item.stem}_{timestamp}{item.suffix}"
            dest_path = dest_folder / new_name

        try:
            shutil.move(str(item), str(dest_path))
            logger.info(f"✅ Moved: {item.name} -> Processed/{category}/{dest_path.name}")
            moved_count += 1
        except Exception as e:
            logger.error(f"❌ Failed to move {item.name}: {e}")

    logger.info(f"🏁 Librarian finished. Processed {moved_count} files.")

if __name__ == "__main__":
    run_librarian()
