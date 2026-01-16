import os
import json
import subprocess
import glob

# Test Config
ENEX_FILE = r"D:\My_System\Inbox\Enex_Flat\01_每日收集组__EverMemo.enex"
OUTPUT_DIR = r"D:\My_System\Inbox\Yarle_Debug_Output"
TEMPLATE_PATH = r"D:\My_System\Jarvis_v1\config\debug_template.md"

CONFIG = {
    "enexSources": [ENEX_FILE],
    "outputDir": OUTPUT_DIR,
    "templateFile": TEMPLATE_PATH,
    "isMetadataNeeded": True,
    "isNotebookNameNeeded": True,
    "isZettelkastenNeeded": False,
    "useHashTags": True,
    "outputFormat": "ObsidianMD",
    "skipWebClips": False,
    "isSmallestImageSizeNeeded": True,
    "trimTitle": True,
    "replaceSpacesInTags": True,
    "dateFormat": "YYYY-MM-DD"
}

def run_debug():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    config_path = r"D:\My_System\Jarvis_v1\config\yarle_debug_conf.json"
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(CONFIG, f, indent=2)
        
    cmd = f'npx -y yarle-evernote-to-md --configFile "{config_path}"'
    print(f"Running debug conversion...")
    subprocess.run(cmd, shell=True, check=True)
    
    # Read Result
    md_files = glob.glob(os.path.join(OUTPUT_DIR, "**", "*.md"), recursive=True)
    if md_files:
        print(f"\nCreated file: {md_files[0]}")
        with open(md_files[0], 'r', encoding='utf-8') as f:
            print(f.read(500))
    else:
        print("No MD file created.")

if __name__ == "__main__":
    run_debug()
