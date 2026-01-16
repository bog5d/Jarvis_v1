# -*- coding: utf-8 -*-

import time
import logging
import os
import sys
from pathlib import Path
from typing import Union

# Add project root to sys.path to ensure absolute imports work
current_dir = Path(__file__).resolve()
jarvis_root = current_dir.parent.parent
project_root = jarvis_root.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

try:
    from Jarvis_v1.config import system_config
except ImportError:
    # Fallback or development mode
    try:
        from config import system_config # type: ignore
    except ImportError:
         print("Warning: Could not import system_config")

MAX_RETRIES = 5
RETRY_DELAY = 1.0 # seconds

def safe_read(filepath: Union[str, Path], mode='r', encoding='utf-8') -> Union[str, bytes]:
    """
    Read file with retry mechanism for cloud sync locks (OneDrive/Dropbox).
    """
    filepath = Path(filepath)
    last_error = None
    
    for attempt in range(MAX_RETRIES):
        try:
            use_encoding = encoding if 'b' not in mode else None
            with open(filepath, mode, encoding=use_encoding) as f:
                return f.read()
        except (PermissionError, OSError) as e:
            last_error = e
            # print(f"File locked, retrying ({attempt+1}/{MAX_RETRIES}): {filepath}")
            time.sleep(RETRY_DELAY)
            
    raise last_error

def safe_write(filepath: Union[str, Path], content: Union[str, bytes], mode='w', encoding='utf-8') -> bool:
    """
    Write file with retry mechanism. Automaticaly creates parent directories.
    """
    filepath = Path(filepath)
    # Ensure directory exists
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory {filepath.parent}: {e}")
        
    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            use_encoding = encoding if 'b' not in mode else None
            with open(filepath, mode, encoding=use_encoding) as f:
                f.write(content)
            return True
        except (PermissionError, OSError) as e:
            last_error = e
            print(f"File locked, retrying write ({attempt+1}/{MAX_RETRIES}): {filepath}")
            time.sleep(RETRY_DELAY)
            
    print(f"Failed to write {filepath}: {last_error}")
    raise last_error

def setup_logger(name: str) -> logging.Logger:
    """
    Configure a standard logger outputting to both file and console.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Check if handlers already exist to avoid duplicates
    if logger.handlers:
        return logger
        
    formatter = logging.Formatter(system_config.LOG_FORMAT, datefmt=system_config.LOG_DATE_FORMAT)
    
    # 1. File Handler (Rotates logs ideally, but standard Append for now)
    try:
        log_file = system_config.DEFAULT_LOG_FILE
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except Exception as e:
        print(f"Failed to setup file logging: {e}")
    
    # 2. Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger
