import evernote_backup
from evernote_backup.note_storage import SqliteStorage
from evernote_backup.note_exporter import NoteExporter

print("Successfully imported classes.")

# Inspect SqliteStorage
print("SqliteStorage init:")
# It likely takes the db path
print(SqliteStorage.__init__.__annotations__)

# Inspect NoteExporter
print("NoteExporter init:")
print(NoteExporter.__init__.__annotations__)
