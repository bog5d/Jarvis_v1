import os
import shutil
import re

SOURCE_DIR = r"D:\My_System\Inbox\Enex_Export"
DEST_DIR = r"D:\My_System\Inbox\Enex_Ready"

def sanitize_filename(filename):
    # Remove extension for processing
    name, ext = os.path.splitext(filename)
    
    # Replace common problematic characters
    name = name.replace(" ", "_")
    name = name.replace("=", "-")
    name = name.replace("「", "")
    name = name.replace("」", "")
    name = name.replace("(", "")
    name = name.replace(")", "")
    
    # Remove any other non-standard characters if needed, but keep Chinese
    # Just ensure no weird shell characters
    return name + ext

def main():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        print(f"Created directory: {DEST_DIR}")
    else:
        print(f"Directory exists: {DEST_DIR}")

    count = 0
    skipped = 0
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.lower().endswith(".enex"):
                src_path = os.path.join(root, file)
                
                # Create rudimentary safe name
                safe_name = sanitize_filename(file)
                dest_path = os.path.join(DEST_DIR, safe_name)
                
                # Handle Collisions
                if os.path.exists(dest_path):
                    # Check if it's the same file (size)
                    if os.path.getsize(src_path) == os.path.getsize(dest_path):
                        print(f"Skipping duplicate (size match): {safe_name}")
                        skipped += 1
                        continue
                    else:
                        # Rename with counter
                        base, ext = os.path.splitext(safe_name)
                        counter = 1
                        while os.path.exists(dest_path):
                            dest_path = os.path.join(DEST_DIR, f"{base}_{counter}{ext}")
                            counter += 1
                
                try:
                    shutil.copy2(src_path, dest_path)
                    print(f"Copied: {file} -> {os.path.basename(dest_path)}")
                    count += 1
                except Exception as e:
                    print(f"Error copying {file}: {e}")

    print("-" * 30)
    print(f"Total files processed: {count}")
    print(f"Total files skipped: {skipped}")
    print(f"Total .enex files in Ready folder: {len(os.listdir(DEST_DIR))}")

if __name__ == "__main__":
    main()
