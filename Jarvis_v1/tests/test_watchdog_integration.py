# -*- coding: utf-8 -*-
import sys
import os
import threading
import time
import shutil
from pathlib import Path
from datetime import datetime

# Setup Paths
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config.system_config import DIR
from Jarvis_v1.utils.watchdog_service import start_watchdog
from Jarvis_v1.utils.logger import setup_logger

logger = setup_logger("Test_Watchdog")

def run_integration_test():
    print("🧪 Starting Watchdog Integration Self-Test...")
    
    # 0. Cleanup from previous runs
    test_file_name = "_AUTOTEST_NOTE.md"
    # Librarian moves to Inbox/Processed/Notes/
    src_file = DIR['INBOX'] / test_file_name
    processed_file = DIR['INBOX'] / "Processed" / "Notes" / test_file_name
    
    if src_file.exists(): 
        try: os.remove(src_file)
        except: pass
    if processed_file.exists(): 
        try: os.remove(processed_file)
        except: pass
    
    # 1. Start Watchdog in Background Thread
    # We define a wrapper to catch system exit if any
    def service_wrapper():
        try:
            start_watchdog()
        except SystemExit:
            pass

    watchdog_thread = threading.Thread(target=service_wrapper, daemon=True)
    watchdog_thread.start()
    print("⏳ Watchdog Service Launched (Background)...")
    time.sleep(5) # Let it initialize
    
    # 2. Inject Test File
    print("💉 Injecting Test Data...")
    try:
        with open(src_file, 'w', encoding='utf-8') as f:
            f.write("# Self Test\nThis is a generated test file for Watchdog verification.\nKeyword: AUTOTEST_KEY")
        print(f"📄 Created: {src_file}")
    except Exception as e:
        print(f"❌ Failed to create test file: {e}")
        return False
    
    # 3. Wait for Pipeline (Librarian -> Secretary -> etc)
    # Pipeline is triggered via subprocess, might take 5-10s
    wait_time = 25
    print(f"⏳ Waiting for pipeline execution ({wait_time}s)...")
    time.sleep(wait_time) 
    
    # 4. Validation
    errors = []
    
    # Check 1: File Moved?
    if processed_file.exists():
        print("✅ PASS: File successfully moved by Librarian.")
    else:
        print(f"❌ FAIL: File not found in {processed_file}")
        errors.append("Librarian failed to move file")
        if src_file.exists(): 
            print("   (File still in Inbox)")
        else:
            print("   (File disappeared completely)")
        
    # Check 2: Briefing Updated?
    today_str = datetime.now().strftime("%Y-%m-%d")
    briefing_file = DIR['INBOX'] / f"Daily_Briefing_{today_str}.md"
    
    if briefing_file.exists():
        try:
            with open(briefing_file, 'r', encoding='utf-8') as f:
                content = f.read()
            if test_file_name in content:
                print("✅ PASS: Briefing contains test file reference.")
            else:
                 print("⚠️ WARN: Briefing exists but missing specific file ref (Secretary lag?).")
        except:
             print("⚠️ WARN: Could not read briefing.")
    else:
        print("❌ FAIL: Daily Briefing not generated.")
        errors.append("Secretary failed to generate briefing")

    # 5. Cleanup
    try:
        if src_file.exists(): os.remove(src_file)
        if processed_file.exists(): os.remove(processed_file)
        # We don't delete Briefing as it might contain real user data too
    except:
        pass

    # 6. Final Report
    print("\n" + "="*30)
    if not errors:
        print("🎉 INTEGRATION TEST PASSED")
        return True
    else:
        print(f"💥 TEST FAILED: {', '.join(errors)}")
        return False

if __name__ == "__main__":
    success = run_integration_test()
    if not success:
        sys.exit(1)
