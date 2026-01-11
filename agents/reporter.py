import sys
from pathlib import Path
from datetime import datetime

# Add project root to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config.system_config import DIR

def run_reporter():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 📊 Reporter initialized...")
    
    # 1. Data Collection
    # Inbox Count (Top level files only, excluding folders)
    inbox_path = DIR['INBOX']
    if inbox_path.exists():
        inbox_count = sum(1 for item in inbox_path.iterdir() if item.is_file() and item.name not in [".DS_Store", "desktop.ini"])
        inbox_status = "Pending" if inbox_count > 0 else "Clean"
    else:
        inbox_count = 0
        inbox_status = "Missing"

    # Knowledge Base Count (Recursive count of .md files)
    kb_path = DIR['KNOWLEDGE_BASE']
    if kb_path.exists():
        kb_count = sum(1 for item in kb_path.rglob("*.md"))
    else:
        kb_count = 0

    # Read Logs (Last 10 lines)
    log_file = DIR['LOGS'] / 'jarvis.log'
    log_lines = ""
    if log_file.exists():
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                log_lines = "".join(lines[-10:])
        except Exception as e:
            log_lines = f"Error reading logs: {e}"
    else:
        log_lines = "No logs found."

    # 2. Generate Dashboard Content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""# 🎛️ Jarvis Control Center
> **Last Sync**: {timestamp}

## 📊 System Vital Signs
| Module | Status | Count |
| :--- | :--- | :--- |
| 📥 **Inbox** | {inbox_status} | **{inbox_count}** files |
| 🧠 **Knowledge** | Active | **{kb_count}** notes |

## 📋 Recent Neural Activity
```text
{log_lines}
```

## 🔗 Quick Actions
* [[01_Inbox/Index|📂 Open Inbox]]
* [[20_Knowledge_Base/Index|🧠 Open Brain]]
"""

    # 3. Write to Dashboard
    dashboard_path = DIR['DASHBOARD']
    if not dashboard_path.exists():
        dashboard_path.mkdir(parents=True, exist_ok=True)
        
    target_file = dashboard_path / 'Home.md'
    
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Dashboard updated: {target_file}")
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Failed to update dashboard: {e}")

if __name__ == "__main__":
    run_reporter()
