
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from chat_engine import JarvisChat

def test_connection():
    print("🚀 Starting Phase 1 Verification: DeepSeek Connection & Prompt Injection")
    
    try:
        # Initialize
        config_path = Path("config/settings.yaml")
        jarvis = JarvisChat(str(config_path))
        
        # Test Chat
        user_msg = "你好，Jarvis。请简要介绍你自己，并演示一下原子化笔记的输出格式。"
        print(f"\nUser > {user_msg}\n")
        
        response = jarvis.chat(user_msg)
        
        print(f"\nJarvis > {response}\n")
        
        # Check for tags
        if "**Tags**" in response and "Category" in response:
            print("\n✅ Verification Success: DeepSeek is connected AND responding with Dual-Track Tags.")
        else:
            print("\n⚠️ Verification Warning: DeepSeek connected, but Tag format missing or incorrect.")
            
    except Exception as e:
        print(f"\n❌ Verification Failed: {e}")

if __name__ == "__main__":
    test_connection()
