import os
import json
import glob
import subprocess
import time
import shutil
from pathlib import Path
from datetime import datetime

# ================= Configuration =================
SOURCE_DIR = r"D:\My_System\Inbox\Enex_Export"
BASE_CONFIG_PATH = r"D:\My_System\Jarvis_v1\config\yarle_config.json"
OUTPUT_DIR = r"D:\Yarle_Out"
TEMP_CONFIG = r"D:\My_System\Jarvis_v1\config\temp_yarle_config.json"
LOG_FILE = r"D:\My_System\Jarvis_v1\conversion_report.log"

# Stability Settings
NODE_MEM_LIMIT = 12288      # 12GB (Pushing limits for the big file)
TIMEOUT_SECONDS = 3600      # 60 Minutes per notebook max
MIN_DISK_SPACE_GB = 2.0     # Stop if free space < 2GB

# =================================================

def log(message):
    """Writes to both console and log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{timestamp}] {message}"
    print(msg)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(msg + "\n")

def check_disk_space(path):
    """Returns True if space is sufficient"""
    total, used, free = shutil.disk_usage(path)
    free_gb = free // (2**30)
    if free_gb < MIN_DISK_SPACE_GB:
        log(f"⚠️ CRITICAL: Disk space low! Only {free_gb}GB remaining.")
        return False
    return True

def load_base_config():
    with open(BASE_CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    log("🚀 Starting Robust Batch Conversion V2.0")
    
    # Ensure output dir exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Environment Check
    if not check_disk_space(OUTPUT_DIR):
        log("❌ Aborting: Not enough disk space to start.")
        return

    # 2. Find files
    source_path = Path(SOURCE_DIR)
    enex_files = sorted(list(source_path.rglob("*.enex")), key=lambda x: x.stat().st_size)
    # Sort by size: Small files first (Quick wins), Big files last (Risk management)
    
    total = len(enex_files)
    log(f"[*] Found {total} .enex files. Sorted by size (Small -> Large).")

    base_config = load_base_config()
    
    # Force Flat Structure for stability
    base_config["outputDir"] = OUTPUT_DIR
    base_config["skipEnexFileNameFromOutputPath"] = True 
    
    success_count = 0
    fail_count = 0
    skipped_count = 0

    for idx, enex_path in enumerate(enex_files, 1):
        filename = enex_path.name
        filesize_mb = enex_path.stat().st_size / (1024 * 1024)
        
        log(f"---------------------------------------------------")
        log(f"[{idx}/{total}] Processing: {filename} ({filesize_mb:.1f} MB)")
        
        # Pre-flight Check
        if not check_disk_space(OUTPUT_DIR):
            log("❌ Disk full during process. Pausing/Stopping to prevent corruption.")
            break

        # Config Setup
        current_config = base_config.copy()
        current_config["enexSources"] = [str(enex_path)]
        
        # Write Config
        try:
            with open(TEMP_CONFIG, 'w', encoding='utf-8') as f:
                json.dump(current_config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            log(f"❌ Failed to write config: {e}")
            fail_count += 1
            continue
        
        # Prepare Command
        cmd = f'npx -y yarle-evernote-to-md --configFile "{TEMP_CONFIG}"'
        env = os.environ.copy()
        env["NODE_OPTIONS"] = f"--max-old-space-size={NODE_MEM_LIMIT}"
        
        # Execute with Timeout
        start_time = time.time()
        try:
            # We use subprocess.run with timeout
            result = subprocess.run(
                cmd, 
                shell=True, 
                env=env, 
                check=True, 
                capture_output=True, 
                text=True, 
                encoding='utf-8', 
                errors='replace',
                timeout=TIMEOUT_SECONDS
            )
            
            elapsed = time.time() - start_time
            log(f"✔️ Success in {elapsed:.1f}s")
            success_count += 1
            
        except subprocess.TimeoutExpired:
            log(f"⏳ TIMEOUT: File took longer than {TIMEOUT_SECONDS}s. Skipped.")
            fail_count += 1
        except subprocess.CalledProcessError as e:
            fail_count += 1
            log(f"❌ Failed (Exit Code {e.returncode})")
            err_msg = e.stderr if e.stderr else (e.stdout if e.stdout else "No error details")
            log(f"  Error Snippet: {err_msg[:500]}...") 
        except Exception as e:
            fail_count += 1
            log(f"❌ Unexpected Error: {e}")

    log("=" * 30)
    log(f"Batch Complete. Success: {success_count}, Failed: {fail_count}")

if __name__ == "__main__":
    main()
