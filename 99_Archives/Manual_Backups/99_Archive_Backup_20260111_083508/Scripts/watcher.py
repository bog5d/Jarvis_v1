# -*- coding: utf-8 -*-
"""
Jarvis_v1 - 个人知识库自动化系统
文件监控脚本 (watcher.py)

功能：监控 Inbox 文件夹，自动处理录音和文本文件
作者：Jarvis System
"""

import os
import time
import logging
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ==================== 核心路径配置 ====================
INPUT_DIR = r"D:\My_System\Inbox"
OUTPUT_DIR = r"D:\My_System\01_Drafts"

# ==================== 文件类型配置 ====================
AUDIO_EXTENSIONS = {'.mp3', '.wav', '.m4a'}
TEXT_EXTENSIONS = {'.txt', '.md'}
ALLOWED_EXTENSIONS = AUDIO_EXTENSIONS | TEXT_EXTENSIONS

# ==================== 忽略规则配置 ====================
IGNORE_EXTENSIONS = {'.tmp', '.crdownload', '.partial', '.downloading'}
IGNORE_FOLDERS = {'.verysync', '.sync', '.stversions', 'Thumbs.db'}
IGNORE_PREFIXES = ('~', '.')  # 忽略以这些字符开头的文件

# ==================== 日志配置 ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


# ==================== 占位处理函数 (Mock 阶段) ====================

def transcribe_audio(file_path: str) -> None:
    """
    模拟音频转录处理
    
    Args:
        file_path: 音频文件的完整路径
    
    TODO: 后续接入真实的语音转文字 API (如 Whisper, Azure Speech 等)
    """
    try:
        print(f"正在模拟处理文件: {file_path}...")
        
        # 生成输出文件名
        input_filename = Path(file_path).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{input_filename}_transcribed_{timestamp}.md"
        output_path = Path(OUTPUT_DIR) / output_filename
        
        # 生成测试 Markdown 文件
        markdown_content = f"""# 音频转录结果

## 源文件信息
- **文件名**: {Path(file_path).name}
- **处理时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **文件类型**: 音频文件

## 转录内容 (Mock)

> 这是一个模拟的转录结果。
> 
> 实际部署时，这里将显示音频的真实转录文本。

---
*由 Jarvis_v1 自动处理生成*
"""
        
        # 确保输出目录存在
        Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        logger.info(f"✅ 音频处理完成，输出文件: {output_path}")
        
    except Exception as e:
        logger.error(f"❌ 处理音频文件时出错: {file_path}, 错误: {e}")
        raise


def process_text(file_path: str) -> None:
    """
    模拟文本处理
    
    Args:
        file_path: 文本文件的完整路径
    
    TODO: 后续接入 LLM API 进行文本总结、分类等处理
    """
    try:
        print(f"正在模拟处理文件: {file_path}...")
        
        # 读取原始文本内容
        original_content = ""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='gbk') as f:
                original_content = f.read()
        
        # 生成输出文件名
        input_filename = Path(file_path).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{input_filename}_processed_{timestamp}.md"
        output_path = Path(OUTPUT_DIR) / output_filename
        
        # 生成测试 Markdown 文件
        markdown_content = f"""# 文本处理结果

## 源文件信息
- **文件名**: {Path(file_path).name}
- **处理时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **文件类型**: 文本文件
- **原文长度**: {len(original_content)} 字符

## 原始内容

```
{original_content[:500]}{'...(已截断)' if len(original_content) > 500 else ''}
```

## AI 处理结果 (Mock)

> 这是一个模拟的处理结果。
> 
> 实际部署时，这里将显示 AI 对文本的总结、分类或其他处理结果。

---
*由 Jarvis_v1 自动处理生成*
"""
        
        # 确保输出目录存在
        Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        logger.info(f"✅ 文本处理完成，输出文件: {output_path}")
        
    except Exception as e:
        logger.error(f"❌ 处理文本文件时出错: {file_path}, 错误: {e}")
        raise


# ==================== 文件过滤逻辑 ====================

def should_ignore_file(file_path: str) -> bool:
    """
    判断是否应该忽略该文件
    
    Args:
        file_path: 文件完整路径
    
    Returns:
        True 表示应该忽略，False 表示需要处理
    """
    path = Path(file_path)
    filename = path.name
    
    # 1. 检查是否在忽略的文件夹中
    for part in path.parts:
        if part in IGNORE_FOLDERS:
            logger.debug(f"忽略文件（在忽略文件夹中）: {file_path}")
            return True
    
    # 2. 检查文件名前缀
    if filename.startswith(IGNORE_PREFIXES):
        logger.debug(f"忽略文件（前缀匹配）: {file_path}")
        return True
    
    # 3. 检查是否是临时文件扩展名
    if path.suffix.lower() in IGNORE_EXTENSIONS:
        logger.debug(f"忽略文件（临时文件）: {file_path}")
        return True
    
    # 4. 检查是否是允许的文件类型
    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        logger.debug(f"忽略文件（不支持的类型）: {file_path}")
        return True
    
    return False


def is_file_ready(file_path: str, wait_time: float = 2.0) -> bool:
    """
    检查文件是否已完成写入（通过检查文件大小是否稳定）
    
    Args:
        file_path: 文件路径
        wait_time: 等待时间（秒）
    
    Returns:
        True 表示文件已准备好，False 表示文件仍在写入
    """
    try:
        if not os.path.exists(file_path):
            return False
        
        initial_size = os.path.getsize(file_path)
        time.sleep(wait_time)
        
        if not os.path.exists(file_path):
            return False
        
        final_size = os.path.getsize(file_path)
        
        return initial_size == final_size and final_size > 0
        
    except Exception as e:
        logger.warning(f"检查文件状态时出错: {e}")
        return False


# ==================== 文件系统事件处理器 ====================

class InboxEventHandler(FileSystemEventHandler):
    """
    处理 Inbox 文件夹中的文件系统事件
    """
    
    def __init__(self):
        super().__init__()
        self.processed_files = set()  # 避免重复处理
    
    def on_created(self, event):
        """当新文件创建时触发"""
        if event.is_directory:
            return
        
        self._handle_file(event.src_path)
    
    def on_modified(self, event):
        """当文件修改时触发（某些同步软件可能先创建空文件再写入）"""
        if event.is_directory:
            return
        
        self._handle_file(event.src_path)
    
    def _handle_file(self, file_path: str):
        """
        处理文件的核心逻辑
        
        Args:
            file_path: 文件完整路径
        """
        try:
            # 1. 检查是否应该忽略
            if should_ignore_file(file_path):
                return
            
            # 2. 使用文件路径+大小作为唯一标识，避免重复处理
            file_key = f"{file_path}_{os.path.getsize(file_path) if os.path.exists(file_path) else 0}"
            if file_key in self.processed_files:
                return
            
            # 3. 等待文件写入完成
            logger.info(f"📁 检测到新文件: {file_path}")
            logger.info("⏳ 等待文件写入完成...")
            
            if not is_file_ready(file_path):
                logger.warning(f"⚠️ 文件可能未完成写入或已被删除: {file_path}")
                return
            
            # 4. 标记为已处理
            self.processed_files.add(file_key)
            
            # 5. 根据文件类型分发处理
            ext = Path(file_path).suffix.lower()
            
            if ext in AUDIO_EXTENSIONS:
                logger.info(f"🎤 开始处理音频文件: {Path(file_path).name}")
                transcribe_audio(file_path)
                
            elif ext in TEXT_EXTENSIONS:
                logger.info(f"📝 开始处理文本文件: {Path(file_path).name}")
                process_text(file_path)
            
            # 6. 清理过旧的处理记录（防止内存泄漏）
            if len(self.processed_files) > 1000:
                self.processed_files.clear()
                logger.info("🧹 已清理处理记录缓存")
                
        except Exception as e:
            logger.error(f"❌ 处理文件时发生错误: {file_path}")
            logger.error(f"   错误详情: {e}")
            # 不重新抛出异常，确保监控继续运行


# ==================== 主程序 ====================

def main():
    """主程序入口"""
    
    # 打印启动信息
    print("=" * 60)
    print("  Jarvis_v1 - 个人知识库自动化系统")
    print("  文件监控服务启动中...")
    print("=" * 60)
    print()
    
    # 确保目录存在
    Path(INPUT_DIR).mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    logger.info(f"📂 监控目录: {INPUT_DIR}")
    logger.info(f"📂 输出目录: {OUTPUT_DIR}")
    logger.info(f"📋 支持的音频格式: {', '.join(AUDIO_EXTENSIONS)}")
    logger.info(f"📋 支持的文本格式: {', '.join(TEXT_EXTENSIONS)}")
    print()
    
    # 创建事件处理器和观察者
    event_handler = InboxEventHandler()
    observer = Observer()
    observer.schedule(event_handler, INPUT_DIR, recursive=True)
    
    # 启动监控
    observer.start()
    logger.info("✅ 文件监控服务已启动，按 Ctrl+C 停止...")
    print()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        logger.info("⏹️ 正在停止监控服务...")
        observer.stop()
    
    observer.join()
    logger.info("👋 监控服务已停止，再见！")


if __name__ == "__main__":
    main()
