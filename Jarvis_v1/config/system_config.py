# -*- coding: utf-8 -*-
import sys
from pathlib import Path

# ==============================================================================
# 🏗️ Jarvis System Configuration (Single Source of Truth)
# ==============================================================================

# --- 1. 动态环境感知 (Context Awareness) ---
# 获取当前文件 (system_config.py) 的父级的父级 -> Jarvis_v1 的父级 -> Root
# Layout: /my_system/Jarvis_v1/config/system_config.py
_CURRENT_FILE = Path(__file__).resolve()
ROOT_DIR = _CURRENT_FILE.parent.parent.parent

# --- 2. 核心目录映射 (Directory Mapping) ---
# 确保所有 Agent 只能通过这些变量访问路径，禁止硬编码字符串
DIR = {
    "ROOT": ROOT_DIR,
    "INBOX": ROOT_DIR / "01_Inbox",
    "KNOWLEDGE_BASE": ROOT_DIR / "20_Knowledge_Base",
    "ARCHIVES": ROOT_DIR / "99_Archives",
    "DASHBOARD": ROOT_DIR / "00_Dashboard",
    # System Internal
    "SYSTEM_ROOT": ROOT_DIR / "Jarvis_v1",
    "LOGS": ROOT_DIR / "Jarvis_v1" / "logs",
    "UTILS": ROOT_DIR / "Jarvis_v1" / "utils",
}

# --- 3. 系统常量 (System Constants) ---
SYSTEM_NAME = "Jarvis"
VERSION = "1.0.0"
GITHUB_REPO = "https://github.com/bog5d/Jarvis_v1"

# 支持的文件类型 (用于 Librarian 分类)
ACCEPTED_TYPES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "documents": {".pdf", ".docx", ".pptx", ".xlsx", ".txt"},
    "audio": {".mp3", ".wav", ".m4a", ".ogg", ".webm"},
    "notes": {".md", ".canvas"}
}

# --- 4. 验证与自检 (Validation) ---
def validate_environment():
    """
    检查核心目录是否存在，不存在则报警。
    用于 Agent 启动前的自检。
    """
    # 强制修正：如果 01_Inbox 不存在但 Inbox 存在，自动识别
    if not DIR["INBOX"].exists() and (ROOT_DIR / "Inbox").exists():
        DIR["INBOX"] = ROOT_DIR / "Inbox"

    missing = []
    for key, path in DIR.items():
        if not path.exists():
            # 尝试自动创建日志和工具目录
            if key in ["LOGS", "UTILS"]:
                try:
                    path.mkdir(parents=True, exist_ok=True)
                except:
                    missing.append(f"{key}: {path}")
            else:
                missing.append(f"{key}: {path}")
    
    if missing:
        return False, f"❌ Critical Directories Missing: {missing}"
    return True, f"✅ Environment OK. Root: {ROOT_DIR}"

# 当作为主脚本运行时，打印环境信息
if __name__ == "__main__":
    is_ok, msg = validate_environment()
    # Handle potential encoding issues in Windows console
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode('utf-8'))
        
    print("-" * 20)
    print(f"📂 Inbox Path: {DIR['INBOX']}")
    print(f"🪵 Log Path:   {DIR['LOGS']}")

# ==============================================================================
# 🧠 AI Brain & Ears (Secrets) - TO BE FILLED BY USER LATER
# ==============================================================================
# DeepSeek / OpenAI Config
LLM_API_BASE = "https://api.deepseek.com"
LLM_API_KEY = "sk-da9d300dd6814aaba1dc112e60dc8202" 
LLM_MODEL = "deepseek-chat"

# Aliyun Voice Config (DashScope / NLS)
ALIYUN_API_KEY = "sk-9302ea779fb14227afe2fd5d15dda68b"
ALIYUN_APPKEY = "YOUR_APPKEY_HERE" # Legacy NLS
ALIYUN_TOKEN = "YOUR_TOKEN_HERE"   # Legacy NLS
