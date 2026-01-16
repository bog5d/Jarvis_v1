# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path

# Setup path to recognize Jarvis_v1 as a package
# We are in d:\My_system\Jarvis_v1
# Root is d:\My_system
current_file = Path(__file__).resolve()
jarvis_root = current_file.parent
project_root = jarvis_root.parent

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

try:
    from Jarvis_v1.config import system_config
    from Jarvis_v1.utils import file_utils
except ImportError as e:
    print(f"CRITICAL ERROR: Import failed - {e}")
    # Fallback to local import if package structure is invalid
    sys.path.append(str(jarvis_root))
    try:
        from config import system_config
        from utils import file_utils
        print("Recovered via local import.")
    except Exception as e2:
        print(f"Fatal Import Error: {e2}")
        sys.exit(1)

def run_checks():
    print("\n========================================")
    print("   JARVIS SYSTEM HEALTH CHECK PROTOCOL")
    print("========================================")
    
    logger = file_utils.setup_logger("HealthCheck")
    logger.info("Starting System Health Check sequence...")
    
    # -------------------------------------------------
    # 1. Directory Structure Verification
    # -------------------------------------------------
    print("\n[1. Directory Tree Verification]")
    dirs_to_check = [
        ("ROOT", system_config.PROJECT_ROOT),
        ("INBOX", system_config.INBOX_DIR),
        ("DASHBOARD", system_config.DASHBOARD_DIR),
        ("KNOWLEDGE", system_config.KNOWLEDGE_BASE_DIR),
        ("ARCHIVES", system_config.ARCHIVE_DIR),
        ("LOGS", system_config.LOG_DIR),
        ("CONFIG", system_config.CONFIG_DIR),
        ("UTILS", system_config.UTILS_DIR)
    ]
    
    missing_dirs = []
    for name, path in dirs_to_check:
        exists = path.exists()
        symbol = "✅" if exists else "❌"
        print(f" {symbol} {name:<12}: {path}")
        if not exists:
            missing_dirs.append(name)
            
    if missing_dirs:
        logger.error(f"Missing directories: {missing_dirs}")
        print("\nWARNING: Some directories are missing!")
    else:
        logger.info("Directory structure valid.")
        
    # -------------------------------------------------
    # 2. File I/O Test (OneDrive/Disk Latency)
    # -------------------------------------------------
    print("\n[2. Input/Output Latency Test]")
    test_file = system_config.INBOX_DIR / "health_check_probe.txt"
    test_content = "System Probe: Active"
    
    try:
        # Write
        print(f" -> Writing probe file to Inbox...")
        file_utils.safe_write(test_file, test_content)
        
        # Read
        print(f" -> Reading probe file...")
        content = file_utils.safe_read(test_file)
        
        # Verify
        if content == test_content:
            print(" -> Content Match: YES")
        else:
            print(f" -> Content Match: NO (Got '{content}')")
            logger.warning("I/O verification mismatch.")

        # Cleanup
        print(f" -> Deleting probe file...")
        try:
            os.remove(test_file)
            print(" ✅ I/O Subsystem: OPERATIONAL")
            logger.info("I/O Subsystem Operational")
        except Exception as e:
            print(f" ⚠️ Warning: Could not delete probe file ({e})")
            
    except Exception as e:
        print(f" ❌ I/O FAILURE: {e}")
        logger.critical(f"I/O Failure: {e}")

    # -------------------------------------------------
    # 3. Environment Summary
    # -------------------------------------------------
    print("\n[3. Environment Summary]")
    print(f" Python: {sys.version.split()[0]}")
    print(f" Root:   {system_config.PROJECT_ROOT}")
    print("========================================")
    print("SYSTEM INITIALIZATION COMPLETE")
    print("========================================")

if __name__ == "__main__":
    run_checks()
