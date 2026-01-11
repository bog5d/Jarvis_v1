from evernote_backup.note_exporter import NoteExporter
import inspect

methods = inspect.getmembers(NoteExporter, predicate=inspect.isfunction)
for name, func in methods:
    print(name)
