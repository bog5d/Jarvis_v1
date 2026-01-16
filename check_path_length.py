import os

def check_long_paths(root_dir=r'D:\My_System\Inbox\Yarle_Output_Fixed', limit=250):
    long_paths = []

    if not os.path.exists(root_dir):
        print(f"Directory not found: {root_dir}")
        return

    print(f"Scanning directory: {root_dir} for paths longer than {limit} chars...")
    
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            file_path = os.path.abspath(os.path.join(root, name))
            if len(file_path) > limit:
                long_paths.append((len(file_path), file_path))
    
    # Sort by length descending
    long_paths.sort(key=lambda x: x[0], reverse=True)

    if long_paths:
        print(f"\n[WARNING] Found {len(long_paths)} files with absolute paths longer than {limit} characters!")
        print(f"Top 5 longest paths:")
        for length, path in long_paths[:5]:
            print(f"[{length}] {path}")
    else:
        print(f"\n[OK] No paths exceeding {limit} characters found.")

if __name__ == "__main__":
    check_long_paths()