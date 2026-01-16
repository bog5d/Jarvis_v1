import sqlite3
import re
from pathlib import Path

DB_PATH = Path(r"C:\Users\王波\en_backup.db")
OUTPUT_DIR = Path(r"C:\Users\王波\OneDrive - Personal\my_system\Inbox\Enex_Export")

def sanitize_filename(name):
    unsafe = r'[\\/:*?"<>|]'
    safe = re.sub(unsafe, '_', name)
    return safe.strip()

def verify():
    if not DB_PATH.exists():
        print("DB not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM notebooks")
    notebooks = sorted([row[0] for row in cur.fetchall()])
    conn.close()

    print(f"Total Notebooks in DB: {len(notebooks)}")
    
    missing = []
    found = []
    
    # Get actual files map (name -> size)
    files_map = {}
    if OUTPUT_DIR.exists():
        for f in OUTPUT_DIR.glob("*.enex"):
            files_map[f.name] = f.stat().st_size

    print(f"Total Files in Dir: {len(files_map)}")

    for nb in notebooks:
        safe_name = sanitize_filename(nb)
        fname = f"{safe_name}.enex"
        
        # Fuzzy match attempt because sanitization might vary
        # If verify logic in script was: expected_file = OUTPUT_DIR / f"{safe_name}.enex"
        
        if fname in files_map:
            found.append(nb)
        else:
            missing.append(nb)
            # print(f"Missing: {nb} (Expected: {fname})")

    print(f"Verified Found: {len(found)}")
    print(f"Pending/Missing: {len(missing)}")
    
    if missing:
        print("\n--- First 10 Missing ---")
        for m in missing[:10]:
            print(f"- {m}")

if __name__ == "__main__":
    verify()
