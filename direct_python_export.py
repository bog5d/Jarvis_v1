import sqlite3
import lzma
import pickle
import re
import os
import gc
from pathlib import Path
from datetime import datetime

# Import Evernote types
try:
    from evernote.edam.type.ttypes import Note
except ImportError:
    # Try finding it in site-packages if strictly needed, 
    # but likely it is available if evernote-backup is installed.
    import sys
    # sys.path... 
    pass

from evernote_backup.note_formatter import NoteFormatter

# Config
DB_PATH = r"C:\Users\王波\en_backup.db"
OUTPUT_DIR = r"D:\My_System\Inbox\Enex_Export"

def sanitize(name):
    clean = re.sub(r'[\\/*?:"<>|]', "_", name).strip()
    return clean if clean else "Untitled_Notebook"

def get_now_str():
    return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def main():
    print("--- Direct Python SQL -> ENEX Exporter ---")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Get Notebooks
    cur.execute("SELECT guid, name FROM notebooks")
    notebooks = cur.fetchall()
    
    print(f"Found {len(notebooks)} notebooks in database.")
    
    formatter = NoteFormatter()
    
    for idx, (nb_guid, nb_name) in enumerate(notebooks, 1):
        safe_name = sanitize(nb_name)
        out_path = os.path.join(OUTPUT_DIR, f"{safe_name}.enex")
        
        # Skip if exists and > 1KB (header size is small)
        if os.path.exists(out_path) and os.path.getsize(out_path) > 500:
             print(f"[{idx}/{len(notebooks)}] SKIPPING {nb_name} (File exists)")
             continue
             
        print(f"[{idx}/{len(notebooks)}] Exporting {nb_name} -> {safe_name}.enex")
        
        # Get Notes for this notebook
        # Note: 'notes' table has 'notebook_guid'
        cur.execute("SELECT raw_note FROM notes WHERE notebook_guid=? AND is_active=1", (nb_guid,))
        rows = cur.fetchall()
        note_count = len(rows)
        print(f"  > Found {note_count} notes.")
        
        try:
             with open(out_path, "w", encoding="utf-8") as f:
                 f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                 f.write('<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export4.dtd">\n')
                 f.write(f'<en-export export-date="{get_now_str()}" application="DirectExport" version="1.0">\n')
                 
                 for row in rows:
                     try:
                         raw = row[0]
                         decompressed = lzma.decompress(raw)
                         note = pickle.loads(decompressed)
                         
                         # Format note using library formatter
                         # format_note args: note, notebook_name, tasks
                         # We pass empty list for tasks as we didn't fetch them (tables: tasks, note_tasks?)
                         snippet = formatter.format_note(note, nb_name, []) 
                         f.write(snippet)
                         f.write("\n")
                         
                     except Exception as ne:
                         print(f"  [Warn] Error processing note: {ne}")
                 
                 f.write('</en-export>')
                 
        except Exception as e:
            print(f"  [ERROR] Failed to write notebook {nb_name}: {e}")
            # Try to delete partial file
            try:
                os.remove(out_path)
            except:
                pass
            
        # GC per notebook
        gc.collect()
            
    conn.close()
    print("--- Export Complete ---")

if __name__ == "__main__":
    main()
