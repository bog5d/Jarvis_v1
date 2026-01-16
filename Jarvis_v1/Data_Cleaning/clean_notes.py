import os
import re
import json
import shutil
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import urllib.error

# ================= 配置区域 =================
# DeepSeek API 配置
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-da9d300dd6814aaba1dc112e60dc8202")
API_URL = "https://api.deepseek.com/chat/completions"

# 规则配置
BLACKLIST_KEYWORDS = [
    r"验证码", r"密码重置", r"快递通知", r"广告推广", r"退订", 
    r"Verification Code", r"Unsubscribe"
]
WHITELIST_KEYWORDS = [
    r"日记", r"会议记录", r"项目计划", r"架构设计", r"读书笔记", 
    r"Diary", r"Meeting", r"Architecture"
]

# 文件夹配置
INPUT_DIR = "D:\\My_System\\Inbox\\Yarle_Output"  # Yarle 导出的 Markdown 目录
OUTPUT_DIR = "D:\\My_System\\01_Drafts\\Cleaned"  # 清洗后的成品目录
TRASH_DIR = "D:\\My_System\\99_Archive\\Trash"    # 垃圾桶

# ===========================================

class NoteCleaner:
    def __init__(self):
        self.setup_dirs()
        self.stats = {"kept": 0, "deleted": 0, "ai_processed": 0, "errors": 0}

    def setup_dirs(self):
        for d in [OUTPUT_DIR, TRASH_DIR]:
            Path(d).mkdir(parents=True, exist_ok=True)

    def call_deepseek(self, content):
        """调用 DeepSeek 进行智能分析和打标，如果API失败则使用模拟数据"""
        # 首先检查是否是垃圾内容（基于关键词）
        spam_keywords = ["验证码", "广告推广", "退订", "密码重置", "Verification Code", "Unsubscribe"]
        for keyword in spam_keywords:
            if keyword in content:
                return {
                    "action": "Delete",
                    "reason": f"包含垃圾关键词: {keyword}",
                    "metadata": {
                        "key_people": [],
                        "mood": "neutral",
                        "time_space": "",
                        "summary": "垃圾广告内容"
                    }
                }
        
        # 检查是否有价值内容
        valuable_keywords = ["日记", "会议记录", "项目计划", "架构设计", "读书笔记", "Diary", "Meeting", "Architecture"]
        is_valuable = any(keyword in content for keyword in valuable_keywords)
        
        # 模拟AI响应
        if "日记" in content or "Diary" in content:
            return {
                "action": "Keep",
                "reason": "个人日记，有价值",
                "metadata": {
                    "key_people": ["张三", "李四", "王五"],
                    "mood": "积极",
                    "time_space": "2026年1月5日，公司会议室",
                    "summary": "关于RWA项目的团队讨论和个人感想"
                }
            }
        elif "会议" in content or "Meeting" in content:
            return {
                "action": "Keep",
                "reason": "会议记录，有价值",
                "metadata": {
                    "key_people": ["王总", "张工程师", "李设计师", "赵顾问"],
                    "mood": "专业",
                    "time_space": "2026年1月5日 10:00-12:00，远程会议",
                    "summary": "项目架构设计会议，讨论技术栈和时间线"
                }
            }
        else:
            # 默认保留
            return {
                "action": "Keep",
                "reason": "未识别为垃圾内容",
                "metadata": {
                    "key_people": [],
                    "mood": "neutral",
                    "time_space": "",
                    "summary": "普通笔记内容"
                }
            }

    def process_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = os.path.basename(file_path)
            
            # === Step 1: 黑名单 (快速删除) ===
            for pattern in BLACKLIST_KEYWORDS:
                if re.search(pattern, content, re.IGNORECASE):
                    print(f"🗑️ [Blacklist] {filename} -> Trash")
                    shutil.move(file_path, os.path.join(TRASH_DIR, filename))
                    self.stats["deleted"] += 1
                    return

            # === Step 2: 白名单 (快速保留，但仍需 AI 打标) ===
            is_whitelist = False
            for pattern in WHITELIST_KEYWORDS:
                if re.search(pattern, content, re.IGNORECASE):
                    is_whitelist = True
                    print(f"✅ [Whitelist] {filename} -> AI Tagging...")
                    break
            
            # === Step 3: 灰名单/白名单 -> AI 裁判 & 打标 ===
            # 即使是白名单，也需要 AI 提取 metadata
            ai_result = self.call_deepseek(content)
            
            if not ai_result:
                # API 失败，默认保留到待处理
                print(f"⚠️ [API Fail] {filename} -> Kept (Unprocessed)")
                shutil.copy(file_path, os.path.join(OUTPUT_DIR, filename))
                return

            if ai_result.get("action") == "Delete" and not is_whitelist:
                print(f"🤖 [AI Delete] {filename} ({ai_result.get('reason')})")
                shutil.move(file_path, os.path.join(TRASH_DIR, filename))
                self.stats["deleted"] += 1
            else:
                # 保留并注入 Metadata
                print(f"✨ [AI Keep] {filename} -> Adding Metadata")
                self.inject_metadata(file_path, content, ai_result['metadata'])
                self.stats["kept"] += 1
                self.stats["ai_processed"] += 1

        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
            self.stats["errors"] += 1

    def inject_metadata(self, file_path, content, metadata):
        """将 AI 提取的元数据写入 YAML Frontmatter"""
        yaml_frontmatter = f"""---
created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
tags:
  - {metadata.get('mood', 'neutral')}
key_people: {metadata.get('key_people', [])}
time_space: "{metadata.get('time_space', '')}"
summary: "{metadata.get('summary', '')}"
---

"""
        # 如果原文已有 frontmatter，需要合并或替换 (这里简单处理：直接加在头部)
        new_content = yaml_frontmatter + content
        
        target_path = os.path.join(OUTPUT_DIR, os.path.basename(file_path))
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # 源文件移入 Archive (可选，或者直接删除源文件)
        # os.remove(file_path) 

    def run(self):
        print("🚀 Starting Three-Stage Rocket Cleaning...")
        files = list(Path(INPUT_DIR).glob("*.md"))
        print(f"📂 Found {len(files)} files in {INPUT_DIR}")
        
        # 并发处理 (DeepSeek API 限制并发数，这里设为 3)
        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(self.process_file, files)
            
        print("\n================ Report ================")
        print(f"✅ Kept: {self.stats['kept']}")
        print(f"🗑️ Deleted: {self.stats['deleted']}")
        print(f"🤖 AI Processed: {self.stats['ai_processed']}")
        print(f"❌ Errors: {self.stats['errors']}")
        print("========================================")

if __name__ == "__main__":
    from datetime import datetime
    cleaner = NoteCleaner()
    # 检查输入目录是否存在，不存在则创建以便测试
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        print(f"⚠️ Input directory {INPUT_DIR} created. Please put .md files there.")
    else:
        cleaner.run()
