import sqlite3
import os
from pathlib import Path

DB_PATH = r"C:\Users\王波\en_backup.db"
OUTPUT_DIR = Path(r"D:\My_System\Inbox\Enex_Export")

def get_db_notebooks():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM notebooks")
    notebooks = [row[0] for row in cur.fetchall()]
    conn.close()
    return notebooks

def get_exported_notebooks():
    # .enex files can be in subdirectories (stacks) or root
    files = list(OUTPUT_DIR.rglob("*.enex"))
    # Filename is "NotebookName.enex"
    exported_names = [f.stem for f in files]
    return exported_names

all_nbs = get_db_notebooks()
done_nbs = get_exported_notebooks()

missing = []
for nb in all_nbs:
    # Check if nb is in done_nbs (sanitized name might differ slightly)
    # Evernote backup usually keeps the name safe.
    # Let's simple check for now.
    if nb not in done_nbs:
        # Try checking sanitized version if simple match fails
        # But for now assume exact match or close enough
        missing.append(nb)

print(f"Total Notebooks: {len(all_nbs)}")
print(f"Exported: {len(done_nbs)}")
print(f"Missing: {len(missing)}")

if missing:
    print("Next 5 to export:")
    for m in missing[:5]:
        print(f" - {m}")

# Generate a list for the export script
with open("missing_notebooks.txt", "w", encoding="utf-8") as f:
    for m in missing:
        f.write(m + "\n")
