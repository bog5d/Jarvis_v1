import evernote_backup
import inspect
from evernote_backup import cli as cli_module

print("ver:", evernote_backup.__version__)

# Try to find the storage and export classes
# Usually in note_storage and note_exporter
try:
    from evernote_backup.note_storage import SqliteStorage
    print("Found SqliteStorage")
except ImportError:
    print("SqliteStorage not found in note_storage")

try:
    from evernote_backup.note_exporter import NoteExporter
    print("Found NoteExporter")
except ImportError:
    print("NoteExporter not found in note_exporter")
    
# Let's look at the parameters for NoteExporter
if 'NoteExporter' in locals():
    print(inspect.signature(NoteExporter.__init__))
