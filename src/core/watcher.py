import time
import os
from pathlib import Path
# from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import FileSystemEventHandler
from src.utils.logger import setup_logger
from src.handlers.audio_handler import AudioHandler
from src.handlers.text_handler import TextHandler
from src.handlers.pdf_handler import PDFHandler
from src.services.cabinet_secretary import CabinetSecretary

logger = setup_logger("Watcher")

import shutil

class JarvisEventHandler(FileSystemEventHandler):
    def __init__(self, config):
        self.config = config
        self.processed_files = set()

        # 初始化 Handlers
        output_dir = config['paths']['output_dir']
        self.archive_dir = Path(config['paths'].get('archive_dir', 'D:\\My_System\\99_Archive'))
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        
        api_key = config.get('aliyun', {}).get('api_key')
        
        if not api_key:
            logger.warning("⚠️ 未检测到 Aliyun API Key，相关功能可能无法正常工作。请检查 config/settings.yaml")

        briefing_dir = config['paths'].get('briefing_dir', output_dir)
        
        self.audio_handler = AudioHandler(output_dir, api_key)
        self.text_handler = TextHandler(output_dir, api_key)
        self.pdf_handler = PDFHandler(output_dir, api_key)
        self.cabinet_secretary = CabinetSecretary(output_dir, briefing_dir, api_key)
        
        # 加载配置规则
        self.audio_exts = set(config['file_types']['audio'])
        self.text_exts = set(config['file_types']['text'])
        self.pdf_exts = set(config['file_types'].get('pdf', []))
        self.ignore_exts = set(config['ignore']['extensions'])
        self.ignore_folders = set(config['ignore']['folders'])
        self.ignore_prefixes = tuple(config['ignore']['prefixes'])

    def _should_ignore(self, file_path: str) -> bool:
        path = Path(file_path)
        filename = path.name

        # 检查文件夹
        for part in path.parts:
            if part in self.ignore_folders:
                return True
        
        # 检查前缀
        if filename.startswith(self.ignore_prefixes):
            return True
            
        # 检查扩展名
        if path.suffix.lower() in self.ignore_exts:
            return True
            
        return False

    def _is_file_ready(self, file_path: str, wait_time: float = 1.0) -> bool:
        """简单检查文件是否写入完成"""
        try:
            if not os.path.exists(file_path): return False
            size1 = os.path.getsize(file_path)
            time.sleep(wait_time)
            if not os.path.exists(file_path): return False
            size2 = os.path.getsize(file_path)
            return size1 == size2 and size2 > 0
        except Exception:
            return False

    def on_created(self, event):
        logger.debug(f"Raw event created: {event.src_path}")
        if event.is_directory: return
        self._process_event(event.src_path)

    def on_modified(self, event):
        logger.debug(f"Raw event modified: {event.src_path}")
        if event.is_directory: return
        self._process_event(event.src_path)

    def _process_event(self, file_path: str):
        if self._should_ignore(file_path):
            return

        # 简单的去重机制
        try:
            file_size = os.path.getsize(file_path)
        except OSError:
            return # 文件可能已被删除
            
        file_key = f"{file_path}_{file_size}"
        if file_key in self.processed_files:
            return

        logger.info(f"检测到文件变动: {file_path}")
        
        if not self._is_file_ready(file_path):
            return

        self.processed_files.add(file_key)
        
        # 检查是否为“早朝”触发指令
        filename_lower = Path(file_path).name.lower()
        if any(kw in filename_lower for kw in ["早朝", "briefing", "report"]):
            logger.info("🔔 收到【内阁晨报】召唤指令！")
            try:
                self.cabinet_secretary.generate_briefing()
                # 删除触发文件
                os.remove(file_path)
                logger.info("🗑️ 触发指令已销毁")
            except Exception as e:
                logger.error(f"❌ 生成晨报失败: {e}")
            return

        # lf.processed_files.add(file_key)
        
        # 清理缓存
        if len(self.processed_files) > 1000:
            self.processed_files.clear()

        # 分发处理
        ext = Path(file_path).suffix.lower()
        try:
            processed = False
            if ext in self.audio_exts:
                self.audio_handler.handle(file_path)
                processed = True
            elif ext in self.text_exts:
                self.text_handler.handle(file_path)
                processed = True
            elif ext in self.pdf_exts:
                self.pdf_handler.handle(file_path)
                processed = True
            else:
                logger.debug(f"跳过不支持的文件类型: {file_path}")
            
            # 自动归档
            if processed:
                self._archive_file(file_path)
                
        except Exception as e:
            logger.error(f"处理失败: {e}")

    def _archive_file(self, file_path: str):
        """将处理完的文件移动到归档目录"""
        try:
            path = Path(file_path)
            # 按日期归档 (可选，这里先简单归档到根目录)
            # target_dir = self.archive_dir / time.strftime("%Y-%m")
            # target_dir.mkdir(exist_ok=True)
            
            target_path = self.archive_dir / path.name
            
            # 如果目标文件存在，添加时间戳避免覆盖
            if target_path.exists():
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                target_path = self.archive_dir / f"{path.stem}_{timestamp}{path.suffix}"
            
            shutil.move(file_path, target_path)
            logger.info(f"📦 文件已归档: {path.name} -> {target_path}")
        except Exception as e:
            logger.error(f"归档失败: {e}")

class FileWatcher:
    def __init__(self, config):
        self.config = config
        self.observer = Observer()
        self.handler = JarvisEventHandler(config)

    def start(self):
        input_dir = self.config['paths']['input_dir']
        Path(input_dir).mkdir(parents=True, exist_ok=True)
        
        # 开机自检：检查今日晨报
        logger.info("🔍 正在进行开机自检...")
        try:
            today_str = time.strftime("%Y-%m-%d")
            briefing_dir = self.config['paths'].get('briefing_dir', self.config['paths']['output_dir'])
            briefing_path = Path(briefing_dir) / f"📅_每日内阁晨报_{today_str}.md"
            if not briefing_path.exists():
                logger.info("📭 今日晨报尚未生成，正在补课...")
                self.handler.cabinet_secretary.generate_briefing()
            else:
                logger.info("✅ 今日晨报已存在")
        except Exception as e:
            logger.error(f"❌ 开机自检失败: {e}")

        self.observer.schedule(self.handler, input_dir, recursive=True)
        self.observer.start()
        logger.info(f"🚀 Jarvis Watcher 已启动，正在监控: {input_dir}")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        logger.info("正在停止监控...")
        self.observer.stop()
        self.observer.join()
        logger.info("监控已停止")
