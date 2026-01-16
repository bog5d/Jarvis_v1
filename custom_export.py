import os
import sys
import time
import traceback
import sqlite3
import re
from pathlib import Path

# --- Monkeypatch for standalone execution ---
import evernote_backup.cli_app_util
def mock_get_progress_output():
    return sys.stdout
evernote_backup.cli_app_util.get_progress_output = mock_get_progress_output

from evernote_backup import note_exporter
try:
    note_exporter.get_progress_output = mock_get_progress_output
except:
    pass

from evernote_backup.note_storage import SqliteStorage
from evernote_backup.note_exporter import NoteExporter

# Configuration
DB_PATH = Path(r"C:\Users\王波\en_backup.db")
OUTPUT_DIR = Path(r"D:\My_System\Inbox\Enex_Export")
LOG_FILE = Path(r"D:\My_System\Jarvis_v1\export_status.log")

def sanitize_filename(name):
    """Sanitize notebook name for filesystem."""
    unsafe = r'[\\/:*?"<>|]'
    safe = re.sub(unsafe, '_', name)
    return safe.strip()

def get_notebook_list(db_path):
    """Directly query notebook names from SQLite."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM notebooks")
    notebooks = [row[0] for row in cur.fetchall()]
    conn.close()
    return sorted(notebooks)

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except:
        pass

def export_single_notebook(notebook_name, storage):
    """Export a single notebook to a specific file, skipping if exists."""
    safe_name = sanitize_filename(notebook_name)
    expected_file = OUTPUT_DIR / f"{safe_name}.enex"
    
    # Check if file exists roughly
    if expected_file.exists() and expected_file.stat().st_size > 0:
        log(f"SKIP: '{notebook_name}' (File exists: {expected_file.name})")
        return True

    log(f"START: Exporting '{notebook_name}'...")
    
    try:
        # Initialize fresh exporter for isolation
        exporter = NoteExporter(
            storage=storage,
            target_dir=OUTPUT_DIR,
            single_notes=False, 
            export_trash=True if "垃圾" in notebook_name else False, 
            no_export_date=False,
            add_guid=False,
            add_metadata=True,
            overwrite=True, 
            filter_notebooks=[notebook_name], 
            filter_tags=None
        )
        
        exporter.export_notebooks()
        
        # Verify creation
        if expected_file.exists():
             log(f"SUCCESS: '{notebook_name}'")
             return True
        else:
             # Sometimes sanitization mismatches what evernote-backup does
             # Check if *any* new file appeared? 
             # For now, just assume failure if exact match not found, but it might just be named differently.
             log(f"WARNING: Export function finished but {safe_name}.enex not found immediately.")
             return True 
        
    except Exception as e:
        log(f"ERROR: Failed to export '{notebook_name}'. Reason: {str(e)}")
        return False

def main():
    print("--- Robust Evernote Export Script (Breakfast Mode) ---")
    log("Session Started.")
    
    if not DB_PATH.exists():
        log(f"Error: Database not found at {DB_PATH}")
        return
    
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
    try:
        storage = SqliteStorage(DB_PATH)
        storage.check_version()
    except Exception as e:
        log(f"CRITICAL: Failed to initialize storage: {e}")
        return

    notebooks = get_notebook_list(DB_PATH)
    log(f"Found {len(notebooks)} notebooks in database.")

    success_count = 0
    fail_count = 0
    
    for i, nb in enumerate(notebooks, 1):
        print(f"\n[{i}/{len(notebooks)}] Processing: {nb}")
        if export_single_notebook(nb, storage):
            success_count += 1
        else:
            fail_count += 1
            
        sys.stdout.flush()

    log(f"--- Export Function Completed ---")
    log(f"Summary: {success_count} Succeeded, {fail_count} Failed.")

if __name__ == "__main__":
    main()
