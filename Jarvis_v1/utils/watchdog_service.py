# -*- coding: utf-8 -*-
import sys
import os
import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import socket

# Add project root to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config.system_config import DIR
from Jarvis_v1.utils.logger import setup_logger

logger = setup_logger("Watchdog")

class JarvisHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.process_event(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            # If moved INTO the folder, dest_path is the one we want
            if str(DIR['INBOX']) in str(event.dest_path):
                self.process_event(event.dest_path)

    def process_event(self, file_path):
        filename = Path(file_path).name
        
        # Filter temp files
        if filename.startswith(".") or filename.endswith(".tmp") or filename.endswith(".crdownload"):
            return
            
        # Avoid recursion loops (e.g. if we write logs or briefing to Inbox)
        if "Daily_Briefing" in filename or "jarvis.log" in filename:
            return

        # Double check existence (sometimes temp files disappear fast)
        if not Path(file_path).exists():
            return

        logger.info(f"👀 Detected new file: {filename}")
        
        # Debounce/Wait for file copy completion
        time.sleep(2)
        
        # Trigger Pipeline
        self.run_pipeline()

    def run_pipeline(self):
        logger.info("🚀 Triggering Jarvis Pipeline...")
        
        # We need to run the agents in order.
        agents = [
            "Jarvis_v1/agents/librarian.py",
            "Jarvis_v1/agents/secretary.py",
            "Jarvis_v1/agents/cartographer.py",
            "Jarvis_v1/agents/gardener.py",
            "Jarvis_v1/agents/reporter.py"
        ]
        
        env = os.environ.copy()
        python_exe = sys.executable

        for agent in agents:
            script_path = DIR['ROOT'] / agent
            if not script_path.exists():
                logger.error(f"❌ Agent not found: {script_path}")
                continue
                
            try:
                # Run sync
                logger.info(f"▶️ Running {script_path.name}...")
                subprocess.run([python_exe, str(script_path)], check=True, env=env)
            except subprocess.CalledProcessError as e:
                logger.error(f"❌ {script_path.name} failed: {e}")
            except Exception as e:
                logger.error(f"❌ Error running {script_path.name}: {e}")

        logger.info("✅ Pipeline Complete.")

def start_watchdog():
    path_to_watch = DIR['INBOX']
    if not path_to_watch.exists():
        logger.error(f"❌ Inbox not found: {path_to_watch}")
        return

    # Single-instance lock using a localhost port bind. If bind fails, another watchdog is running.
    lock_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lock_port = getattr(DIR['SYSTEM_ROOT'], 'watchdog_lock_port', 51927)
    try:
        lock_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lock_sock.bind(('127.0.0.1', lock_port))
        lock_sock.listen(1)
    except Exception as e:
        logger.warning(f"🐾 Watchdog already running (failed to bind lock port {lock_port}): {e}")
        try:
            lock_sock.close()
        except:
            pass
        return

    event_handler = JarvisHandler()
    observer = Observer()
    observer.schedule(event_handler, str(path_to_watch), recursive=False)
    observer.start()
    logger.info(f"🐕 Jarvis Watchdog started. Monitoring: {path_to_watch}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    try:
        lock_sock.close()
    except:
        pass

if __name__ == "__main__":
    start_watchdog()
