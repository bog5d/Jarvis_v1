import os
import time
import dashscope
from dashscope import Generation
from pathlib import Path
from datetime import datetime, timedelta
from src.utils.logger import setup_logger

logger = setup_logger("CabinetSecretary")

class CabinetSecretary:
    def __init__(self, drafts_dir: str, briefing_dir: str, api_key: str = None):
        self.drafts_dir = Path(drafts_dir)
        self.briefing_dir = Path(briefing_dir)
        self.briefing_dir.mkdir(parents=True, exist_ok=True)
        if api_key:
            dashscope.api_key = api_key
        else:
            logger.error("未提供 Aliyun API Key，内阁秘书无法工作。")

    def generate_briefing(self):
        """生成每日内阁晨报"""
        logger.info("👑 内阁首辅正在整理每日晨报...")
        
        # 1. 扫描过去 24 小时的文件
        recent_files = self._scan_recent_files()
        if not recent_files:
            logger.info("📭 过去 24 小时无新奏折，无需上朝。")
            return

        # 2. 提取关键信息
        briefing_context = self._extract_context(recent_files)
        
        # 3. 调用 AI 生成晨报
        briefing_content = self._call_ai_briefing(briefing_context)
        
        if briefing_content:
            self._save_briefing(briefing_content)

    def _scan_recent_files(self) -> list[Path]:
        """扫描 01_Drafts 下过去 24 小时修改过的 .md 文件 (排除晨报本身)"""
        recent_files = []
        now = time.time()
        one_day_ago = now - 24 * 3600
        
        if not self.drafts_dir.exists():
            return []

        for file_path in self.drafts_dir.glob("*.md"):
            if "每日内阁晨报" in file_path.name:
                continue
                
            if file_path.stat().st_mtime > one_day_ago:
                recent_files.append(file_path)
        
        logger.info(f"📄 找到 {len(recent_files)} 份近期奏折")
        return recent_files

    def _extract_context(self, files: list[Path]) -> str:
        """提取文件摘要和待办"""
        context = "以下是过去 24 小时处理的文件摘要：\n\n"
        
        for file_path in files:
            try:
                content = file_path.read_text(encoding='utf-8')
                # 简单提取 YAML (如果存在) 和正文前 500 字
                context += f"--- 文件名: {file_path.name} ---\n"
                
                # 尝试提取 YAML
                if content.startswith("---"):
                    end_yaml = content.find("---", 3)
                    if end_yaml != -1:
                        yaml_part = content[3:end_yaml].strip()
                        context += f"[元数据]\n{yaml_part}\n"
                        body = content[end_yaml+3:].strip()
                    else:
                        body = content
                else:
                    body = content
                
                # 提取待办事项
                todos = [line for line in body.split('\n') if "- [ ]" in line or "- [x]" in line]
                if todos:
                    context += "[待办事项]\n" + "\n".join(todos) + "\n"
                
                # 提取 AI 总结部分 (假设在 "## AI" 标题下)
                # 简单起见，截取前 800 字
                context += f"\n[内容摘要]\n{body[:800]}...\n\n"
                
            except Exception as e:
                logger.error(f"读取文件失败 {file_path}: {e}")
        
        return context

    def _call_ai_briefing(self, context: str) -> str:
        """调用 Qwen-Max 生成晨报"""
        logger.info("🧠 正在起草内阁晨报 (Qwen-Max)...")
        
        prompt = """你不仅是 AI 助手，更是用户的“内阁首辅”。请根据以下过去 24 小时的文件摘要，撰写一份《每日施政要略》。

要求：
1. **核心情报 (Executive Summary)**: 宏观概述昨日处理了哪些关键议题，发现什么关联或冲突。
2. **需圣裁事项 (Decisions Required)**: 从待办事项或风险中，提炼出需要用户亲自决策或关注的高优先级事项。
3. **风险与机遇 (Risks & Opportunities)**: 洞察潜在的风险点或新的机会。
4. **语气**: 专业、干练、不仅是陈述事实，要有洞察力 (Insight)。

格式参考：
# 📅 每日内阁晨报 (YYYY-MM-DD)

## 👑 核心情报
...

## ⚡ 需圣裁事项
...

## 🛡️ 风险与机遇
...
"""
        
        try:
            messages = [
                {'role': 'system', 'content': prompt},
                {'role': 'user', 'content': context}
            ]
            
            # 使用 qwen-max 以获得更好的逻辑分析能力
            response = Generation.call(
                model='qwen-max', 
                messages=messages,
                result_format='message',
            )

            if response.status_code == 200:
                return response.output.choices[0].message.content
            else:
                logger.error(f"❌ 生成晨报失败: {response.code} - {response.message}")
                return None
        except Exception as e:
            logger.error(f"❌ 调用 AI 失败: {e}")
            return None

    def _save_briefing(self, content: str):
        """保存晨报"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"📅_每日内阁晨报_{date_str}.md"
        output_path = self.briefing_dir / filename
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"✅ 晨报已呈递: {output_path}")
        except Exception as e:
            logger.error(f"❌ 保存晨报失败: {e}")