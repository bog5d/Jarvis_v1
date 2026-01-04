import dashscope
from dashscope import Generation
from pathlib import Path
from datetime import datetime
from src.utils.logger import setup_logger

logger = setup_logger("TextHandler")

class TextHandler:
    def __init__(self, output_dir: str, api_key: str = None):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if api_key:
            dashscope.api_key = api_key
        else:
            logger.error("未提供 Aliyun API Key，文本处理将无法进行。")

    def handle(self, file_path: str) -> None:
        """
        处理文本文件：读取 -> 总结 -> 保存
        """
        try:
            if not dashscope.api_key:
                logger.error("跳过处理：缺少 API Key")
                return

            logger.info(f"📝 正在处理文本文件: {file_path}...")
            input_path = Path(file_path)
            
            # 1. 读取文件内容
            content = ""
            try:
                with open(input_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(input_path, 'r', encoding='gbk') as f:
                        content = f.read()
                except Exception:
                    logger.error(f"❌ 无法读取文件编码: {file_path}")
                    return

            if not content.strip():
                logger.warning("⚠️ 文件内容为空，跳过处理")
                return

            # 2. 调用 LLM 进行总结
            logger.info("🧠 正在调用 Qwen 模型进行总结...")
            
            prompt = "你是一个专业的秘书。请阅读以下内容，总结核心观点（3-5点），并列出所有具体的待办事项(Action Items)。"
            
            messages = [
                {'role': 'system', 'content': prompt},
                {'role': 'user', 'content': content}
            ]

            response = Generation.call(
                model='qwen-plus',
                messages=messages,
                result_format='message',
            )

            if response.status_code == 200:
                logger.info("✅ AI 响应成功")
                ai_content = response.output.choices[0].message.content
                self._save_result(input_path, content, ai_content)
            else:
                logger.error(f"❌ API 调用失败: {response.code} - {response.message}")

        except Exception as e:
            logger.error(f"❌ 处理文本文件时出错: {file_path}, 错误: {e}")

    def _save_result(self, input_path: Path, original_content: str, ai_content: str):
        """保存总结结果到 Markdown"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{input_path.stem}_summary_{timestamp}.md"
        output_path = self.output_dir / output_filename

        markdown_content = f"""# 文本智能总结

## 源文件信息
- **文件名**: {input_path.name}
- **处理时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **模型**: Qwen-Plus

## AI 总结与待办

{ai_content}

## 原始内容 (存档)

<details>
<summary>点击展开查看原文</summary>

```text
{original_content[:2000]}{'...(内容过长已截断)' if len(original_content) > 2000 else ''}
```
</details>

---
*由 Jarvis_v1 (Aliyun Qwen) 自动生成*
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        logger.info(f"💾 结果已保存: {output_path}")
