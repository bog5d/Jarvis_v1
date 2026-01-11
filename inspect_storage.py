from evernote_backup.note_storage import SqliteStorage
import inspect

methods = inspect.getmembers(SqliteStorage, predicate=inspect.isfunction)
for name, func in methods:
    print(name)
