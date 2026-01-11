import os
import json
import subprocess
import glob
from pathlib import Path
import shutil

# Configuration
SOURCE_DIR = r"C:\Users\王波\OneDrive - Personal\my_system\Inbox\Enex_Export"
TEST_OUTPUT_DIR = r"C:\Users\王波\OneDrive - Personal\my_system\Inbox\Yarle_Test_Output"
BASE_CONFIG_PATH = r"C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\config\yarle_config.json"
TEMP_TEST_CONFIG = r"C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\config\temp_test_config.json"

def main():
    print("🚀 Starting Smoke Test...")

    # 1. Clean previous test output
    if os.path.exists(TEST_OUTPUT_DIR):
        print(f"[*] Cleaning old test output: {TEST_OUTPUT_DIR}")
        shutil.rmtree(TEST_OUTPUT_DIR)
    os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

    # 2. Find a small .enex file
    print(f"[*] Searching for a test candidate in {SOURCE_DIR}...")
    enex_files = list(Path(SOURCE_DIR).rglob("*.enex"))
    
    if not enex_files:
        print("❌ No .enex files found!")
        return

    # Sort by size to pick a small one (fastest test)
    enex_files.sort(key=lambda x: x.stat().st_size)
    target_file = enex_files[0]
    
    print(f"[*] Selected test file: {target_file.name} ({target_file.stat().st_size} bytes)")

    # 3. Create Test Config
    print("[*] Configuring Yarle...")
    with open(BASE_CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    config["enexSources"] = [str(target_file)]
    config["outputDir"] = TEST_OUTPUT_DIR
    config["skipEnexFileNameFromOutputPath"] = True
    # Ensure template is using the corrected file
    config["templateFile"] = r"C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\config\yarle_template.md"

    with open(TEMP_TEST_CONFIG, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    # 4. Run Yarle
    print("[*] Running conversion...")
    cmd = f'npx -y yarle-evernote-to-md --configFile "{TEMP_TEST_CONFIG}"'
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("✔️ Yarle process finished.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Yarle failed with exit code {e.returncode}")
        return

    # 5. Verify Output
    print("-" * 40)
    print("📝 Verifying Result:")
    
    md_files = list(Path(TEST_OUTPUT_DIR).rglob("*.md"))
    if not md_files:
        print("❌ No Markdown files generated!")
    else:
        sample_md = md_files[0]
        print(f"[*] Generated file: {sample_md.name}")
        print("-" * 20 + " CONTENT PREVIEW " + "-" * 20)
        try:
            content = sample_md.read_text(encoding='utf-8')
            print(content[:1000]) # Print first 1000 chars
            print("-" * 20 + " END PREVIEW " + "-" * 20)
            
            if len(content.strip()) < 50:
                 print("⚠️ WARNING: content seems suspiciously short. Check template!")
            else:
                 print("✅ SUCCESS: Content generated properly.")
        except Exception as e:
            print(f"❌ Failed to read generated file: {e}")

if __name__ == "__main__":
    main()
