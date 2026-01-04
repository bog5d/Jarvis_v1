import time
import json
import dashscope
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
                    self._save_result(input_path, transcription_results)
                else:
                    logger.error(f"❌ 转录失败: {status.output}")
            else:
                logger.error(f"❌ API 调用失败: {status.code} - {status.message}")

        except Exception as e:
            logger.error(f"❌ 处理音频文件时出错: {file_path}, 错误: {e}")

    def _save_result(self, input_path: Path, results: list):
        """保存转录结果到 Markdown"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{input_path.stem}_transcribed_{timestamp}.md"
        output_path = self.output_dir / output_filename

        # 提取文本内容
        full_text = ""
        try:
            for result in results:
                if 'subtask_status' in result and result['subtask_status'] == 'SUCCEEDED':
                     if 'sentences' in result:
                         for sentence in result['sentences']:
                             full_text += sentence['text'] + " "
        except Exception as e:
            logger.warning(f"解析结果结构时遇到问题: {e}，尝试直接 dump JSON")
            full_text = json.dumps(results, ensure_ascii=False, indent=2)

        markdown_content = f"""# 音频转录结果

## 源文件信息
- **文件名**: {input_path.name}
- **处理时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **文件类型**: 音频文件

## 转录内容

{full_text}

---
*由 Jarvis_v1 (Aliyun Paraformer) 自动生成*
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        logger.info(f"💾 结果已保存: {output_path}")
