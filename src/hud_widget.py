import tkinter as tk
from tkinter import font
import os
import time
import re
from pathlib import Path
from datetime import datetime
import itertools

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
LOG_FILE = PROJECT_ROOT / "logs" / "jarvis.log"
DRAFTS_DIR = Path("D:/My_System/01_Drafts")
BRIEFING_DIR = Path("D:/My_System/02_Briefings")
REFRESH_RATE = 1000  # ms (Data refresh)

# Rotation Settings
IDLE_INTERVAL = 25 * 60 * 1000  # 25 minutes (Idle)
ACTIVE_INTERVAL = 3000          # 3 seconds (Hover)

# Window Size
WIDTH = 320
COMPACT_HEIGHT = 110
EXPANDED_HEIGHT = 220

class JarvisHUD:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jarvis HUD")
        
        # Window Setup
        self.root.overrideredirect(True)  # Frameless
        self.root.attributes('-topmost', True)  # Always on top
        self.root.attributes('-alpha', 0.8)  # Transparency
        self.root.configure(bg='#1e1e1e')
        
        # Positioning (Top Right)
        screen_width = self.root.winfo_screenwidth()
        self.x_pos = screen_width - WIDTH - 20
        self.y_pos = 50
        self.root.geometry(f"{WIDTH}x{COMPACT_HEIGHT}+{self.x_pos}+{self.y_pos}")

        # Fonts
        self.font_status = font.Font(family="Segoe UI", size=11, weight="bold")
        self.font_info = font.Font(family="Microsoft YaHei UI", size=10) # Better for Chinese
        self.font_log = font.Font(family="Consolas", size=8)

        # UI Elements
        self.frame = tk.Frame(self.root, bg='#1e1e1e', padx=12, pady=8)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # 1. Status Indicator
        self.lbl_status = tk.Label(
            self.frame, 
            text="🟢 JARVIS ACTIVE", 
            fg='#00ff00', 
            bg='#1e1e1e', 
            font=self.font_status,
            anchor='w'
        )
        self.lbl_status.pack(fill=tk.X, pady=(0, 5))

        # 2. Info Carousel (The "Screen")
        self.lbl_info = tk.Label(
            self.frame, 
            text="📊 初始化数据...", 
            fg='#ffffff', 
            bg='#1e1e1e', 
            font=self.font_info,
            anchor='w',
            justify=tk.LEFT,
            wraplength=300
        )
        self.lbl_info.pack(fill=tk.X, expand=True)

        # 3. Last Log
        self.lbl_log = tk.Label(
            self.frame, 
            text="Waiting for logs...", 
            fg='#666666', 
            bg='#1e1e1e', 
            font=self.font_log,
            anchor='w',
            justify=tk.LEFT
        )
        self.lbl_log.pack(fill=tk.X, pady=(5, 0))

        # Data Storage
        self.info_items = []
        self.info_cycle = itertools.cycle([])
        self.is_hovered = False
        self.rotate_job = None
        
        # Interaction
        self.root.bind('<Button-1>', self.start_move)
        self.root.bind('<B1-Motion>', self.do_move)
        self.root.bind('<Enter>', self.on_enter)
        self.root.bind('<Leave>', self.on_leave)
        
        # Menu
        self.menu = tk.Menu(self.root, tearoff=0, bg='#2d2d2d', fg='#ffffff')
        self.menu.add_command(label="Exit Jarvis HUD", command=self.root.quit)
        self.root.bind("<Button-3>", self.show_menu)

        # Start Loops
        self.update_data()     # Fetch data (every 1s)
        self.rotate_info()     # Start rotation loop
        self.root.mainloop()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
        # Update stored position so resize works correctly
        self.x_pos = x
        self.y_pos = y

    def on_enter(self, event):
        self.is_hovered = True
        self.root.attributes('-alpha', 1.0)
        self.root.configure(bg='#252526')
        self.frame.configure(bg='#252526')
        for widget in self.frame.winfo_children():
            widget.configure(bg='#252526')
        
        # Expand Window
        self.root.geometry(f"{WIDTH}x{EXPANDED_HEIGHT}+{self.x_pos}+{self.y_pos}")
        
        # Trigger immediate rotation update
        if self.rotate_job:
            self.root.after_cancel(self.rotate_job)
        self.rotate_info()

    def on_leave(self, event):
        self.is_hovered = False
        self.root.attributes('-alpha', 0.8)
        self.root.configure(bg='#1e1e1e')
        self.frame.configure(bg='#1e1e1e')
        for widget in self.frame.winfo_children():
            widget.configure(bg='#1e1e1e')
        
        # Shrink Window
        self.root.geometry(f"{WIDTH}x{COMPACT_HEIGHT}+{self.x_pos}+{self.y_pos}")
        
        # Reset to Summary View immediately
        count = self.get_today_intel_count()
        self.lbl_info.config(text=f"📊 今日战绩: 已处理 {count} 份奏折")
        
        # Reset rotation timer to long interval
        if self.rotate_job:
            self.root.after_cancel(self.rotate_job)
        self.rotate_job = self.root.after(IDLE_INTERVAL, self.rotate_info)

    def show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

    # --- Data Fetching Logic ---

    def get_today_intel_count(self):
        try:
            if not DRAFTS_DIR.exists(): return 0
            today_str = datetime.now().strftime("%Y%m%d")
            today_str_dash = datetime.now().strftime("%Y-%m-%d")
            count = 0
            for f in DRAFTS_DIR.glob("*"):
                if f.is_file() and (today_str in f.name or today_str_dash in f.name):
                    count += 1
            return count
        except: return 0

    def get_briefing_highlights(self):
        """Extract 'Decisions Needed' from today's briefing"""
        highlights = []
        try:
            today_str = datetime.now().strftime("%Y-%m-%d")
            briefing_file = BRIEFING_DIR / f"📅_每日内阁晨报_{today_str}.md"
            
            if briefing_file.exists():
                content = briefing_file.read_text(encoding='utf-8')
                # Find the "Decisions Needed" section
                match = re.search(r'## .*?需圣裁.*?$(.*?)(?=##|\Z)', content, re.DOTALL | re.MULTILINE)
                if match:
                    section_text = match.group(1)
                    # Extract bullet points
                    lines = [line.strip() for line in section_text.split('\n') if line.strip()]
                    for line in lines:
                        # Clean up markdown bullets
                        clean_line = re.sub(r'^[\-\*\d\.]+\s*', '', line)
                        # Keep short meaningful lines
                        if 4 < len(clean_line) < 30: 
                            highlights.append(f"⚖️ 待办: {clean_line}")
                        elif len(clean_line) >= 30:
                            highlights.append(f"⚖️ 待办: {clean_line[:28]}...")
        except Exception as e:
            pass
        return highlights[:3] # Return top 3 items

    def get_latest_file(self):
        try:
            files = list(DRAFTS_DIR.glob("*.md"))
            if not files: return None
            latest_file = max(files, key=os.path.getmtime)
            name = latest_file.name.replace("_pdf_summary", "").replace("_summary", "")
            # Truncate
            if len(name) > 20: name = name[:18] + "..."
            return f"📄 最新: {name}"
        except: return None

    def update_data(self):
        # 1. Update Log (Fast refresh)
        log_text = self.get_last_log()
        if " - " in log_text:
            parts = log_text.split(" - ", 2)
            if len(parts) >= 3: log_text = parts[-1]
        self.lbl_log.config(text=f"📝 {log_text}")

        # 2. Prepare Info Items
        new_items = []
        
        # Item A: Stats
        count = self.get_today_intel_count()
        new_items.append(f"📊 今日战绩: 已处理 {count} 份奏折")
        
        # Item B: Latest File
        latest = self.get_latest_file()
        if latest: new_items.append(latest)
        
        # Item C: Briefing Highlights
        highlights = self.get_briefing_highlights()
        new_items.extend(highlights)
        
        # Update cycle if list changed significantly
        if len(new_items) != len(self.info_items) or (new_items and new_items[0] != self.info_items[0]):
            self.info_items = new_items
            self.info_cycle = itertools.cycle(self.info_items)

        self.root.after(REFRESH_RATE, self.update_data)

    def rotate_info(self):
        # Determine interval based on state
        interval = ACTIVE_INTERVAL if self.is_hovered else IDLE_INTERVAL

        if self.info_items:
            try:
                # If hovered, rotate through everything
                # If idle, we might just want to stay on the first item (Stats) or rotate very slowly
                text = next(self.info_cycle)
                self.lbl_info.config(text=text)
            except StopIteration:
                self.info_cycle = itertools.cycle(self.info_items)
        
        self.rotate_job = self.root.after(interval, self.rotate_info)

    def get_last_log(self):
        try:
            if not LOG_FILE.exists(): return "Waiting for logs..."
            with open(LOG_FILE, 'rb') as f:
                try: f.seek(-200, os.SEEK_END)
                except: f.seek(0)
                lines = f.readlines()
                if lines:
                    last = lines[-1].decode('utf-8', errors='ignore').strip()
                    return last[:45] + "..." if len(last) > 48 else last
                return "Log empty"
        except: return "Log error"

if __name__ == "__main__":
    JarvisHUD()
