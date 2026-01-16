import sqlite3
import pandas as pd # Assuming pandas is installed, otherwise standard sqlite3
import sys

# Standard sqlite3 fallback if pandas not present
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

db_path = r"C:\Users\王波\en_backup.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("--- Tables ---")
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print(tables)

print("\n--- Notes Status ---")
cur.execute("SELECT is_active, count(*) FROM notes GROUP BY is_active")
stats = cur.fetchall()
print(stats)

print("\n--- Sample Raw Note ---")
cur.execute("SELECT title, raw_note FROM notes LIMIT 1")
row = cur.fetchone()
if row:
    title, raw_data = row
    print(f"Title: {title}")
    print(f"Type: {type(raw_data)}")
    if isinstance(raw_data, bytes):
        print(f"Hex start: {raw_data[:20].hex()}")
        try:
            print(f"Decoded (utf-8): {raw_data[:100].decode('utf-8')}")
        except:
            print("Not valid UTF-8 text")
    else:
        print(f"Preview: {raw_data[:100]}")
else:
    print("No notes found.")

conn.close()
