import sys
import os
import shutil
from pathlib import Path
import time
from datetime import datetime

# Add project root to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config.system_config import DIR
from Jarvis_v1.agents.librarian import run_librarian
from Jarvis_v1.agents.secretary import run_secretary

def setup_dummies():
    print("[TEST] Setting up dummy files...")
    inbox = DIR['INBOX']
    if not inbox.exists():
        inbox.mkdir(parents=True)

    # Dummy Audio
    audio_file = inbox / "test_audio_sim.mp3"
    with open(audio_file, 'wb') as f:
        f.write(b'FAKE_AUDIO_CONTENT') # Just needs to exist
    
    # Dummy Note
    note_file = inbox / "test_note.md"
    with open(note_file, 'w', encoding='utf-8') as f:
        f.write("# Project Jarvis\nWe are moving to Phase 3. The Hearing module is crucial.")

    print(f"Created: {audio_file}")
    print(f"Created: {note_file}")
    
    # Hack: Reset file mtime to NOW to ensure Secretary picks them up
    # (Sometimes file creation might be slightly behind if clock sync issues)
    now = time.time()
    os.utime(audio_file, (now, now))
    os.utime(note_file, (now, now))

def verify_results():
    print("[TEST] Verifying results...")
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    briefing_file = DIR['INBOX'] / f"Daily_Briefing_{today_str}.md"
    
    if not briefing_file.exists():
        print("❌ FAIL: No Briefing Generated.")
        return False, "Briefing Missing"
    
    content = ""
    with open(briefing_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    print(f"[TEST] Briefing Content Preview:\n{content[:500]}...")

    audio_check = "test_audio_sim.mp3" in content
    # Note check might look for the filename or the AI summary content. 
    # Since AI summary is variable, looking for filename is safer for "Process" verification.
    note_check = "test_note.md" in content
    
    # Check if mock transcript appeared (or its translated summary)
    mock_check = "MOCK" in content or "Artificial Intelligence" in content or "人工智能" in content
    
    results = {
        "Audio_File_Found": audio_check,
        "Note_File_Found": note_check,
        "Mock_Transcript_Used": mock_check
    }
    
    if all(results.values()):
        return True, results
    else:
        return False, results

def cleanup():
    print("[TEST] Cleaning up dummies...")
    # Be careful not to delete user stuff. We only delete specific test files.
    # Note: Librarian moves them, so we need to find them in Processed to delete.
    
    # Delete from Processed/Audio
    processed_audio = DIR['INBOX'] / 'Processed' / 'Audio' / "test_audio_sim.mp3"
    if processed_audio.exists():
        os.remove(processed_audio)
        
    # Delete from Processed/Notes
    processed_note = DIR['INBOX'] / 'Processed' / 'Notes' / "test_note.md"
    if processed_note.exists():
        os.remove(processed_note)

    print("Cleanup done.")

def run_test():
    print("="*40)
    print("🤖 Jarvis Autonomous Self-Test Protocol")
    print("="*40)
    
    try:
        setup_dummies()
        
        print("\n--- Step 1: Librarian ---")
        run_librarian()
        
        print("\n--- Step 2: Secretary ---")
        run_secretary()
        
        print("\n--- Step 3: Verification ---")
        success, details = verify_results()
        
        print("\n" + "="*40)
        if success:
            print("✅ TEST PASSED: Full Chain Operational")
        else:
            print(f"❌ TEST FAILED: {details}")
        print("="*40)
        
        # Cleanup
        cleanup()
        
        return success
    except Exception as e:
        print(f"❌ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    run_test()
