import time
import json
import dashscope
from dashscope import Generation
from pathlib import Path
from datetime import datetime
from dashscope.audio.asr import Transcription
from src.utils.logger import setup_logger

logger = setup_logger("AudioHandler")

class AudioHandler:
    def __init__(self, output_dir: str, api_key: str = None):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if api_key:
            dashscope.api_key = api_key
        else:
            logger.error("未提供 Aliyun API Key，音频转录将无法进行。")

    def handle(self, file_path: str) -> None:
        """
        处理音频文件：上传 -> 转录 -> 保存
        """
        try:
            if not dashscope.api_key:
                logger.error("跳过处理：缺少 API Key")
                return

            logger.info(f"🎤 正在处理音频文件: {file_path}...")
            input_path = Path(file_path)
            
            # 1. 上传文件到 DashScope 临时存储
            logger.info("📤 正在上传文件到云端...")
            try:
                from dashscope.file import File
                file_url = File.upload(str(input_path))
                logger.info(f"✅ 上传成功: {file_url}")
            except ImportError:
                logger.error("❌ dashscope 版本过低，不支持文件上传。请运行 pip install dashscope --upgrade")
                return
            except Exception as e:
                logger.error(f"❌ 文件上传失败: {e}")
                raise

            # 2. 提交转录任务
            logger.info("🚀 提交转录任务...")
            task = Transcription.async_call(
                model='paraformer-v1',
                file_urls=[file_url],
                language_hints=['zh', 'en'] 
            )
            
            task_id = task.output.task_id
            logger.info(f"⏳ 任务 ID: {task_id}，等待转录完成...")

            # 3. 轮询等待结果
            status = Transcription.wait(task=task_id)
            
            if status.status_code == 200:
                if status.output['task_status'] == 'SUCCEEDED':
                    logger.info("✅ 转录成功！")
                    transcription_results = status.output['results']
                    
                    # 提取全文
                    full_text = ""
                    try:
                        for result in transcription_results:
                            if 'subtask_status' in result and result['subtask_status'] == 'SUCCEEDED':
                                 if 'sentences' in result:
                                     for sentence in result['sentences']:
                                         full_text += sentence['text'] + " "
                    except Exception:
                        pass
                    
                    # 调用总结
                    ai_summary = ""
                    if full_text:
                        logger.info("🧠 正在调用 Qwen 模型进行总结...")
                        try:
                            prompt = """你是一个专业的秘书。请阅读以下会议/录音转录内容，并按以下格式输出：
1. 提取 3-5 个关键标签 (Tags)
2. 生成一句话的精炼总结 (Summary)
3. 列出具体的待办事项 (Action Items)
4. 总结核心观点

请确保你的回答包含以上所有部分。"""
                            messages = [{'role': 'system', 'content': prompt}, {'role': 'user', 'content': full_text[:30000]}]
                            response = Generation.call(model='qwen-plus', messages=messages, result_format='message')
                            if response.status_code == 200:
                                ai_summary = response.output.choices[0].message.content
                        except Exception as e:
                            logger.error(f"总结失败: {e}")

                    self._save_result(input_path, full_text, ai_summary)
                else:
                    logger.error(f"❌ 转录失败: {status.output}")
            else:
                logger.error(f"❌ API 调用失败: {status.code} - {status.message}")

        except Exception as e:
            logger.error(f"❌ 处理音频文件时出错: {file_path}, 错误: {e}")

    def _save_result(self, input_path: Path, full_text: str, ai_summary: str):
        """保存转录结果到 Markdown (带 YAML Frontmatter)"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        created_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        output_filename = f"{input_path.stem}_transcribed_{timestamp}.md"
        output_path = self.output_dir / output_filename

        markdown_content = f"""---
created: "{created_time}"
source_file: "{input_path.name}"
type: "audio"
tags: [AI转录, 语音]
status: inbox
---

# 音频转录与总结

## AI 总结与待办

{ai_summary}

## 转录全文

{full_text}

---
*由 Jarvis_v1 (Aliyun Paraformer + Qwen) 自动生成*
"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            logger.info(f"💾 结果已保存: {output_path}")
        except Exception as e:
            logger.error(f"❌ 保存文件失败: {e}")
