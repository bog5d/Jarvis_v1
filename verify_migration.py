import os
from pathlib import Path

# 新绝对路径
ROOT_DIR = Path(r"C:\Users\王波\OneDrive - Personal\my_system")

def verify_and_create():
    print(f"Checking Migration Status for Root: {ROOT_DIR}")
    
    # Required Folders
    required_folders = [
        "Inbox",
        "20_Knowledge_Base"
    ]
    
    all_good = True
    
    # Also check if the Jarvis_v1 folder itself is reachable under this if expected
    # But user specifically asked for Inbox and 20_Knowledge_Base
    
    for folder_name in required_folders:
        folder_path = ROOT_DIR / folder_name
        if folder_path.exists():
            print(f"[OK] Found: {folder_path}")
        else:
            print(f"[MISSING] {folder_path} not found. Attempting to create...")
            try:
                folder_path.mkdir(parents=True, exist_ok=True)
                print(f"[CREATED] Successfully created {folder_path}")
            except Exception as e:
                print(f"[ERROR] Failed to create {folder_path}: {e}")
                all_good = False

    if all_good:
        print("Migration Success: Core folders found.")
    else:
        print("Migration Partial: Some folders were missing or could not be created.")

if __name__ == "__main__":
    verify_and_create()
