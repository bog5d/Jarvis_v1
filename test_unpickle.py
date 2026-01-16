import sqlite3
import lzma
import pickle
import sys

# Try to import the Note class so pickle knows it
try:
    from evernote.edam.type.ttypes import Note
except ImportError:
    # It might be vendorized in evernote_backup or installed as evernote3
    # Let's try to find where it is.
    try:
        from evernote_backup.vendor.evernote.edam.type.ttypes import Note
    except ImportError:
        print("Could not import Note class. Pickle might fail.")

DB_PATH = r"C:\Users\王波\en_backup.db"
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT raw_note FROM notes LIMIT 1")
raw = cur.fetchone()[0]
conn.close()

decompressed = lzma.decompress(raw)
try:
    note = pickle.loads(decompressed)
    print(f"Success!")
    print(f"Note Title: {note.title}")
    # print(f"Content: {note.content[:50]}")
except Exception as e:
    print(f"Pickle error: {e}")
    # Inspect what module it wants
    import pickletools
    try:
        pickletools.dis(decompressed[:100])
    except:
        pass
