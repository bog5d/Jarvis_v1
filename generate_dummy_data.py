
import os
from pathlib import Path
from datetime import datetime

def generate_logs():
    base_dir = Path("D:/My_System/20_Knowledge_Base/Chat_Logs")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = base_dir / f"{today}_Chat.md"
    
    content = """
### 10:00 - User
DeepSeek 的 API 价格是多少？ #AI成本 #预算

---

### 10:01 - Jarvis
DeepSeek-V3 的 API 价格非常亲民...
**Tags**
* **Category**: Resource
* **Keywords**: #AI成本 #DeepSeek #预算 #API

---

### 11:00 - User
帮我列一下 RWA 项目的合规风险。 #Web3 #RWA #合规

---

### 11:01 - Jarvis
RWA (Real World Assets) 项目面临的主要合规风险包括...
**Tags**
* **Category**: Insight
* **Keywords**: #Web3 #RWA #合规 #金融监管 #风险管理

---

### 14:00 - User
明天去上海出差的行程安排。 #差旅 #上海

---

### 14:01 - Jarvis
为您规划的上海行程如下...
**Tags**
* **Category**: Project
* **Keywords**: #差旅 #上海 #行程规划 #效率

---

### 15:00 - User
我觉得原子化笔记这个概念很好，能不能展开讲讲？

---

### 15:02 - Jarvis
原子化笔记的核心在于去语境化...
**Tags**
* **Category**: Insight
* **Keywords**: #原子化笔记 #知识管理 #卢曼 #卡片盒

---
"""
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Dummy logs generated at {log_file}")

if __name__ == "__main__":
    generate_logs()
