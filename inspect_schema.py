import sqlite3

db_path = r"C:\Users\王波\en_backup.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def get_columns(table_name):
    try:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [row[1] for row in cursor.fetchall()]
        print(f"Columns in '{table_name}': {columns}")
    except Exception as e:
        print(f"Error accessing '{table_name}': {e}")

get_columns("notebooks")
get_columns("notes")
get_columns("resources") # Attachments often stored here

conn.close()
