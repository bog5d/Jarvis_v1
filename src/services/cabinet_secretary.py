import os
import time
import dashscope
from dashscope import Generation
from pathlib import Path
from datetime import datetime, timedelta
from src.utils.logger import setup_logger

logger = setup_logger("CabinetSecretary")

# Try importing OpenAI for DeepSeek
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

class CabinetSecretary:
    def __init__(self, drafts_dir: str, briefing_dir: str, api_key: str = None, deepseek_config: dict = None, prompt_path: str = None):
        self.drafts_dir = Path(drafts_dir)
        self.briefing_dir = Path(briefing_dir)
        self.briefing_dir.mkdir(parents=True, exist_ok=True)
        
        # Aliyun Config (Fallback)
        if api_key:
            dashscope.api_key = api_key
        else:
            logger.warning("⚠️ 未提供 Aliyun API Key，Qwen 降级模式不可用。")

        # DeepSeek Config
        self.deepseek_client = None
        self.deepseek_model = "deepseek-chat" 
        if deepseek_config and deepseek_config.get('api_key'):
            if OpenAI:
                try:
                    self.deepseek_client = OpenAI(
                        api_key=deepseek_config['api_key'],
                        base_url=deepseek_config.get('base_url', "https://api.deepseek.com")
                    )
                    logger.info("🧠 DeepSeek 引擎已加载 (内阁首辅模式)")
                except Exception as e:
                    logger.error(f"❌ DeepSeek 初始化失败: {e}")
            else:
                logger.warning("⚠️ 未安装 openai 库，无法使用 DeepSeek。请运行 pip install openai")

        # Prompt Config
        self.prompt_path = prompt_path
        self.system_prompt = self._load_prompt()

    def _load_prompt(self) -> str:
        default_prompt = """你不仅是 AI 助手，更是用户的“内阁首辅”。请根据以下过去 24 小时的文件摘要，撰写一份《每日施政要略》。"""
        if self.prompt_path and os.path.exists(self.prompt_path):
            try:
                logger.info(f"📜 加载 Prompt: {self.prompt_path}")
                return Path(self.prompt_path).read_text(encoding='utf-8')
            except Exception as e:
                logger.error(f"❌ 读取 Prompt 文件失败: {e}")
        return default_prompt

    def generate_briefing(self):
        """生成每日内阁晨报"""
        logger.info("👑 内阁首辅正在整理每日晨报...")
        
        # 1. 扫描自上次晨报以来的文件
        recent_files = self._scan_recent_files()
        if not recent_files:
            logger.info("📭 自上次晨报以来无新奏折，无需上朝。")
            return

        # 2. 提取关键信息
        briefing_context = self._extract_context(recent_files)
        
        # 3. 调用 AI 生成晨报
        briefing_content = self._call_ai_briefing(briefing_context)
        
        if briefing_content:
            self._save_briefing(briefing_content)

    def _get_last_briefing_time(self) -> float:
        """获取上一份晨报的生成时间"""
        if not self.briefing_dir.exists():
            return 0.0
        
        # 查找所有晨报文件
        briefings = list(self.briefing_dir.glob("📅_每日内阁晨报_*.md"))
        if not briefings:
            return 0.0
            
        # 按修改时间排序，找最新的
        try:
            latest_briefing = max(briefings, key=lambda p: p.stat().st_mtime)
            return latest_briefing.stat().st_mtime
        except Exception:
            return 0.0

    def _scan_recent_files(self) -> list[Path]:
        """扫描 01_Drafts 下自上次晨报以来修改过的 .md 文件 (排除晨报本身)"""
        recent_files = []
        
        last_briefing_time = self._get_last_briefing_time()
        
        if last_briefing_time == 0.0:
            # 如果从未生成过，默认回溯 24 小时
            last_briefing_time = time.time() - 24 * 3600
            logger.info("🔍 未找到历史晨报，默认扫描过去 24 小时...")
        else:
            last_date = datetime.fromtimestamp(last_briefing_time).strftime("%Y-%m-%d %H:%M")
            logger.info(f"🔍 上次晨报时间: {last_date}，正在扫描此后更新的奏折...")
        
        if not self.drafts_dir.exists():
            return []

        for file_path in self.drafts_dir.glob("*.md"):
            if "每日内阁晨报" in file_path.name:
                continue
                
            # 只要文件的修改时间晚于上次晨报时间
            if file_path.stat().st_mtime > last_briefing_time:
                recent_files.append(file_path)
        
        logger.info(f"📄 找到 {len(recent_files)} 份新奏折")
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
                # 增加上下文长度以支持深度萃取 (V2.0)
                context += f"\n[内容摘要]\n{body[:5000]}...\n\n"
                
            except Exception as e:
                logger.error(f"读取文件失败 {file_path}: {e}")
        
        return context

    def _call_ai_briefing(self, context: str) -> str:
        """调用 AI 生成晨报 (优先 DeepSeek, 降级 Qwen)"""
        
        # 1. Try DeepSeek
        if self.deepseek_client:
            logger.info("🧠 正在起草内阁晨报 (DeepSeek)...")
            try:
                response = self.deepseek_client.chat.completions.create(
                    model=self.deepseek_model,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": context},
                    ],
                    stream=False
                )
                return response.choices[0].message.content
            except Exception as e:
                logger.error(f"❌ DeepSeek 调用失败: {e}, 尝试切换回 Aliyun...")
        
        # 2. Fallback to Aliyun
        logger.info("🧠 正在起草内阁晨报 (Qwen-Max)...")
        try:
            messages = [
                {'role': 'system', 'content': self.system_prompt},
                {'role': 'user', 'content': context}
            ]
            
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