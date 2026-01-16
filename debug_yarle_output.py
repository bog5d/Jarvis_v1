import os

output_dir = r"D:\My_System\Inbox\Yarle_Output"

print(f"Scanning {output_dir} for .md files...")

md_files = []
for root, dirs, files in os.walk(output_dir):
    for f in files:
        if f.endswith(".md"):
            full_path = os.path.join(root, f)
            size = os.path.getsize(full_path)
            md_files.append((full_path, size))

print(f"Found {len(md_files)} md files.")

if md_files:
    # Pick the largest one
    md_files.sort(key=lambda x: x[1], reverse=True)
    largest = md_files[0]
    print(f"Largest file: {largest[0]} ({largest[1]} bytes)")
    
    print("-" * 20)
    try:
        with open(largest[0], "r", encoding="utf-8") as f:
            print(f.read()[:500]) # First 500 chars
    except Exception as e:
        print(f"Error reading file: {e}")
else:
    print("No Markdown files found. Yarle failed completely.")
