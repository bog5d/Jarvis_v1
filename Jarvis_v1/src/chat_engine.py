import os
import sys
import yaml
import glob
from datetime import datetime
from pathlib import Path

# Add src to path for module imports
sys.path.append(str(Path(__file__).parent.parent))
try:
    from src.core.retriever import Retriever
except ImportError:
    # Attempt local import if running directly from src
    from core.retriever import Retriever
    
# Try importing OpenAI
try:
    from openai import OpenAI
except ImportError:
    print("❌ 缺少 openai 库。请运行: pip install openai")
    sys.exit(1)

class JarvisChat:
    def __init__(self, config_path="config/settings.yaml"):
        self.base_dir = Path("D:/My_System")
        self.memory_dir = self.base_dir / "20_Knowledge_Base" / "Chat_Logs"
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        
        self.config = self._load_config(config_path)
        self.client = self._init_client()
        self.messages = []

        # Initialize Retriever (The Librarian)
        self.jarvis_root = self.base_dir / "Jarvis_v1"
        self.retriever = Retriever(
            index_path=self.jarvis_root / "data/knowledge_index.json",
            root_dir=self.jarvis_root / "data/simulated_archive"
        )
        
    def _load_config(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"⚠️ 无法加载配置文件: {e}")
            return {}

    def _init_client(self):
        # 优先从配置文件读取
        api_key = self.config.get('deepseek', {}).get('api_key')
        base_url = self.config.get('deepseek', {}).get('base_url', "https://api.deepseek.com")
        
        if not api_key or "YOUR_DEEPSEEK_API_KEY" in api_key:
            # 尝试从环境变量读取
            api_key = os.getenv("DEEPSEEK_API_KEY")
            
        if not api_key:
            print("❌ 未找到 DeepSeek API Key。请在 config/settings.yaml 中配置或设置 DEEPSEEK_API_KEY 环境变量。")
            sys.exit(1)
            
        return OpenAI(api_key=api_key, base_url=base_url)

    def _load_memory(self, limit=3):
        """加载最近几天的聊天记录作为长期记忆"""
        print("🧠 正在检索长期记忆 (Hippocampus)...")
        
        # 获取所有 .md 文件并按修改时间排序
        files = sorted(self.memory_dir.glob("*.md"), key=os.path.getmtime, reverse=True)
        recent_files = files[:limit]
        
        # 按时间正序排列，以便阅读
        recent_files.reverse()
        
        context = ""
        for f in recent_files:
            try:
                content = f.read_text(encoding='utf-8')
                context += f"\n--- 记忆来源: {f.name} ---\n{content}\n"
            except Exception as e:
                print(f"⚠️ 读取记忆文件失败 {f}: {e}")
                
        return context

    def _load_project_context(self):
        """加载项目背景信息 (System Context)"""
        context_path = self.base_dir / "Jarvis_v1" / "project_context.md"
        if context_path.exists():
            try:
                return context_path.read_text(encoding='utf-8')
            except Exception:
                return ""
        return ""

    def _load_latest_briefing(self):
        """加载最新晨报 (Current State)"""
        briefing_dir = self.base_dir / "02_Briefings"
        if briefing_dir.exists():
            files = list(briefing_dir.glob("*.md"))
            if files:
                latest = max(files, key=lambda p: p.stat().st_mtime)
                try:
                    return f"--- 最新内阁晨报 ({latest.name}) ---\n{latest.read_text(encoding='utf-8')}\n"
                except:
                    return ""
        return ""

    def _save_log(self, role, content):
        """实时存档"""
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"{today}_Chat.md"
        file_path = self.memory_dir / filename
        
        timestamp = datetime.now().strftime("%H:%M")
        
        log_entry = f"\n### {timestamp} - {role}\n{content}\n\n---\n"
        
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"❌ 存档失败: {e}")

    def _load_system_prompt(self):
        """加载系统级 Prompt"""
        prompt_path = self.base_dir / "Jarvis_v1" / "prompts" / "system_prompt.md"
        if prompt_path.exists():
            try:
                return prompt_path.read_text(encoding='utf-8')
            except Exception:
                pass
        return "你不仅是 AI 助手，更是用户的 Jarvis 内阁首辅。"

    def _load_context_from_tags(self, query):
        """[Phase 3] 基于标签检索记忆"""
        try:
            hits = self.retriever.find_relevant_files(query)
            if hits:
                print(f"📖 检索到 {len(hits)} 份相关文档...")
                return self.retriever.get_context(hits)
        except Exception as e:
            print(f"⚠️ 检索失败: {e}")
        return ""

    def initialize_context(self):
        """初始化上下文（加载记忆 + 背景 + 晨报），如果尚未加载"""
        if not self.messages:
            print("📚 正在加载项目背景与最新晨报...")
            project_context = self._load_project_context()
            latest_briefing = self._load_latest_briefing()
            past_chat_history = self._load_memory()
            core_system_prompt = self._load_system_prompt()
            
            system_prompt = f"""{core_system_prompt}

【系统背景】
{project_context}

【当前局势 (最新晨报)】
{latest_briefing}

【沟通历史 (长期记忆)】
以下是我们最近几天的沟通历史，请基于此背景继续为我服务，不要重复废话。
=== 历史记忆开始 ===
{past_chat_history}
=== 历史记忆结束 ===

你的回答应专业、简洁、有洞察力，并严格遵循双轨标签输出格式。
"""
            self.messages.append({"role": "system", "content": system_prompt})

    def chat(self, user_input: str) -> str:
        """供外部调用的对话接口"""
        self.initialize_context()
        
        # 1. 尝试检索历史背景
        additional_context = self._load_context_from_tags(user_input)
        
        # 2. 构造最终输入
        if additional_context:
            final_user_content = f"{user_input}\n\n【Jarvis 历史档案库】\n{additional_context}\n(请根据上述档案补充回答细节)"
        else:
            final_user_content = user_input

        # 记录用户输入
        self.messages.append({"role": "user", "content": final_user_content})
        self._save_log("User", final_user_content)
        
        # 获取配置
        model_name = self.config.get('deepseek', {}).get('model', "deepseek-chat")
        temperature = self.config.get('deepseek', {}).get('temperature', 1.3)

        try:
            response = self.client.chat.completions.create(
                model=model_name,
                messages=self.messages,
                temperature=temperature,
                stream=False
            )
            ai_content = response.choices[0].message.content
            
            # 记录 AI 回复
            self.messages.append({"role": "assistant", "content": ai_content})
            self._save_log("Jarvis", ai_content)
            
            return ai_content
        except Exception as e:
            return f"❌ 发生错误: {e}"

    def start(self):
        # 1. 构建 System Prompt
        self.initialize_context()
        
        print("\n" + "="*50)
        print("🤖 Jarvis Chat Mode (DeepSeek Edition) 已启动")
        print(f"📂 记忆库: {self.memory_dir}")
        print("="*50 + "\n")

        # 2. 对话循环
        while True:
            try:
                user_input = input("User > ").strip()
                if not user_input: continue
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("Jarvis > 再见，陛下。")
                    break
                
                print("Jarvis (Thinking)...", end="\r")
                ai_content = self.chat(user_input)
                print(f"\rJarvis > {ai_content}\n")
                
            except KeyboardInterrupt:
                print("\nJarvis > 暂停服务。")
                break
            except Exception as e:
                print(f"\n❌ 发生错误: {e}")

if __name__ == "__main__":
    # 确保在项目根目录下运行，或者调整 config 路径
    # 假设脚本在 src/chat_engine.py，config 在 ../config/settings.yaml
    
    # 获取当前脚本所在目录的父目录 (Jarvis_v1)
    current_dir = Path(__file__).parent.parent
    config_path = current_dir / "config" / "settings.yaml"
    
    jarvis = JarvisChat(config_path)
    jarvis.start()
