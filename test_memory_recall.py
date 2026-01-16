import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from chat_engine import JarvisChat

def test_memory_recall():
    print("🚀 Starting Phase 3.5 Verification: Memory Recall")
    
    try:
        # Initialize
        config_path = Path("config/settings.yaml")
        jarvis = JarvisChat(str(config_path))
        
        # Test Chat with Keywords present in Index (Architecture, Security)
        # We expect the 'simulated_archive/old_project_notes.md' to be retrieved.
        user_msg = "Please review the Project Architecture. Is Python 3.12 feasible?"
        print(f"\nUser > {user_msg}\n")
        
        response = jarvis.chat(user_msg)
        
        print(f"\nJarvis > {response}\n")
        
        if "old_project_notes.md" in str(jarvis.messages):  
             # Note: we can't easily check internal messages from here unless we inspect jarvis.messages
            print("✅ Test Passed: Context appears to have been injected (Check logs for '检索到').")
        else:
             print("⚠️ Test Warning: Check if context was actually retrieved.")
             
        # Inspect internal messages to prove injection
        for m in jarvis.messages:
            if m['role'] == 'user' and '【Jarvis 历史档案库】' in m['content']:
                print("\n[Proof of Injection]:")
                print(m['content'][:200] + "...")
                
    except Exception as e:
        print(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    test_memory_recall()
