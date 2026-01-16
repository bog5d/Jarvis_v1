import yaml
import sys
from pathlib import Path
from src.core.watcher import FileWatcher
from src.utils.logger import setup_logger

def load_config(config_path: str) -> dict:
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"无法加载配置文件: {e}")
        sys.exit(1)

def main():
    # 设置项目根目录
    root_dir = Path(__file__).parent
    config_path = root_dir / "config" / "settings.yaml"
    
    # 加载配置
    config = load_config(str(config_path))
    
    # 初始化日志
    logger = setup_logger()
    logger.info("Jarvis_v1 系统初始化...")
    
    # 启动监控
    watcher = FileWatcher(config)
    watcher.start()

if __name__ == "__main__":
    main()
