import sqlite3
import lzma
import binascii

DB_PATH = r"C:\Users\王波\en_backup.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("SELECT title, raw_note FROM notes LIMIT 1")
title, raw_data = cur.fetchone()

print(f"Title: {title}")
print(f"Raw hex: {binascii.hexlify(raw_data[:10])}")

try:
    # Try generic decompression
    content = lzma.decompress(raw_data)
    print("Decompressed successfully!")
    print(f"Content preview: {content[:200]}")
except Exception as e:
    print(f"Decompression failed: {e}")
    # Try without header?
    
conn.close()
