import sqlite3
import os

DB_PATH = r"C:\Users\王波\en_backup.db"
OUTPUT_DIR = r"D:\My_System\Inbox\Enex_Export_Script"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Get notebooks
cur.execute("SELECT guid, name FROM notebooks")
notebooks = cur.fetchall()

print(f"Found {len(notebooks)} notebooks.")

for guid, name in notebooks:
    # Sanitize filename
    safe_name = "".join([c for c in name if c.isalpha() or c.isdigit() or c==' ' or c=='_']).strip()
    if not safe_name:
        safe_name = "Untitled_Notebook"
    
    print(f"Exporting notebook: {name}...")
    
    # Use evernote-backup command via os.system for each notebook
    # Try singular notebook export if the bulk export fails
    cmd = f'python -m evernote_backup.cli export "{OUTPUT_DIR}" --database "{DB_PATH}"'
    # It seems the previous command failed silently. 
    # Let's try to export just this notebook? 
    # evernote-backup doesn't seem to have a flag for single notebook export in the CLI help I saw implicitly.
    # But wait, looking at documentation (or assuming), maybe the database state is "synced but not ready for export"?
    
    # Actually, let's look at the database content more closely.
    # The `evernote-backup` tool stores raw data. 
    # If `export` produces nothing, it might be because the notes are not marked as downloaded fully?
    pass

# Direct approach: Since evernote-backup is failing silently, let's try to debug WHY.
# Maybe the output directory permission? Or key error?
# Let's run a script that captures stderr.
