import dashscope
import pdfplumber
from dashscope import Generation
from pathlib import Path
from datetime import datetime
from src.utils.logger import setup_logger

logger = setup_logger("PDFHandler")

class PDFHandler:
    def __init__(self, output_dir: str, api_key: str = None):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if api_key:
            dashscope.api_key = api_key
        else:
            logger.error("未提供 Aliyun API Key，PDF 处理将无法进行。")

    def handle(self, file_path: str) -> None:
        """
        处理 PDF 文件：提取文本 -> 总结 -> 保存
        """
        try:
            if not dashscope.api_key:
                logger.error("跳过处理：缺少 API Key")
                return

            logger.info(f"📑 正在处理 PDF 文件: {file_path}...")
            input_path = Path(file_path)
            
            # 1. 提取 PDF 文本
            content = self._extract_text_from_pdf(file_path)
            
            if not content.strip():
                logger.warning("⚠️ PDF 内容为空或无法提取文本 (可能是扫描件)，跳过处理")
                return

            logger.info(f"✅ 文本提取成功，长度: {len(content)} 字符")

            # 2. 调用 LLM 进行总结
            logger.info("🧠 正在调用 Qwen 模型进行总结...")
            
            # 针对长文档的简单截断 (Qwen-Plus 支持 30k token，约 4-5万中文字符，这里做个安全截断)
            # TODO: 后续优化为分段总结
            max_chars = 30000
            if len(content) > max_chars:
                logger.warning(f"⚠️ 文本过长 ({len(content)} 字符)，将截取前 {max_chars} 字符进行总结")
                content_to_process = content[:max_chars] + "\n...(已截断)"
            else:
                content_to_process = content

            prompt = """你是一个专业的秘书。请阅读以下 PDF 文档内容，并按以下格式输出：
1. 提取 3-5 个关键标签 (Tags)
2. 生成一句话的精炼总结 (Summary)
3. 列出具体的待办事项 (Action Items)
4. 总结核心观点

请确保你的回答包含以上所有部分。"""
            
            messages = [
                {'role': 'system', 'content': prompt},
                {'role': 'user', 'content': content_to_process}
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
            logger.error(f"❌ 处理 PDF 文件时出错: {file_path}, 错误: {e}")

    def _extract_text_from_pdf(self, file_path: str) -> str:
        """使用 pdfplumber 提取文本"""
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            logger.error(f"PDF 解析失败: {e}")
        return text

    def _save_result(self, input_path: Path, original_content: str, ai_content: str):
        """保存总结结果到 Markdown (带 YAML Frontmatter)"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        created_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        output_filename = f"{input_path.stem}_pdf_summary_{timestamp}.md"
        output_path = self.output_dir / output_filename

        markdown_content = f"""---
created: "{created_time}"
source_file: "{input_path.name}"
type: "pdf"
tags: [AI处理, PDF]
status: inbox
---

# PDF 智能总结

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
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            logger.info(f"💾 结果已保存: {output_path}")
        except Exception as e:
            logger.error(f"❌ 保存文件失败: {e}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        logger.info(f"💾 结果已保存: {output_path}")
