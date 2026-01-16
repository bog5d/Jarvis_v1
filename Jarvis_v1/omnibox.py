# -*- coding: utf-8 -*-
import sys
import os
import threading
import time
import customtkinter as ctk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Tk
from datetime import datetime
from pathlib import Path
from plyer import notification
import queue
import shutil

# Add project root to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config.system_config import DIR
from Jarvis_v1.utils.ai_brain import call_ai, retrieve_context, build_context_text
from Jarvis_v1.utils.logger import setup_logger

logger = setup_logger("OmniBoxV2")

# --- Helper: Save Note to Inbox ---
def save_note(content):
    if not content.strip():
        return False
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Note_{timestamp}.md"
    filepath = DIR['INBOX'] / filename
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filename
    except Exception as e:
        logger.error(f"Failed to save note: {e}")
        return False

# --- Helper: Save File to Inbox ---
def save_file_to_inbox(src_path):
    try:
        src = Path(src_path)
        if not src.exists():
            return False, "File does not exist."
        dest = DIR['INBOX'] / src.name
        shutil.copy2(src, dest)
        return True, src.name
    except Exception as e:
        logger.error(f"Failed to save file: {e}")
        return False, str(e)

# --- Main App ---
class OmniBoxV2(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Jarvis Omni-Box v2.0")
        self.geometry("600x420")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.hide_window)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Center window
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - 300
        y = (self.winfo_screenheight() // 2) - 210
        self.geometry(f"600x420+{x}+{y}")

        # Chat history (read-only, scrollable)
        self.chat_history = ctk.CTkTextbox(self, width=580, height=280, font=("Consolas", 13))
        self.chat_history.grid(row=0, column=0, padx=10, pady=(10, 5))
        self.chat_history.configure(state="disabled")

        # Multi-line input
        self.input_box = ctk.CTkTextbox(self, width=580, height=80, font=("Consolas", 14))
        self.input_box.grid(row=1, column=0, padx=10, pady=(0, 10))
        self.input_box.bind("<Return>", self.on_enter)
        self.input_box.bind("<Shift-Return>", self.on_shift_enter)
        self.input_box.bind("<Control-v>", self.on_paste)
        self.input_box.bind("<Control-V>", self.on_paste)
        self.input_box.focus_set()

        # Session memory
        self.chat_history_list = []
        self.queue = queue.Queue()

        # Hotkey registration (Ctrl+Alt+J)
        self.after(100, self.register_hotkey)

        # Hide on start
        self.withdraw()
        self.is_visible = False

        # Poll for AI responses
        self.after(200, self.process_queue)

    def register_hotkey(self):
        try:
            import keyboard
            keyboard.add_hotkey('ctrl+alt+j', self.toggle_window)
        except Exception as e:
            logger.error(f"Failed to register hotkey: {e}")

    def toggle_window(self):
        if self.is_visible:
            self.hide_window()
        else:
            self.show_window()

    def show_window(self):
        self.deiconify()
        self.input_box.focus_set()
        self.is_visible = True

    def hide_window(self, event=None):
        self.withdraw()
        self.is_visible = False

    def on_enter(self, event=None):
        # Only send if not Shift+Enter
        if event and (event.state & 0x0001):  # Shift pressed
            return
        user_text = self.input_box.get("1.0", "end-1c").strip()
        if not user_text:
            return "break"
        self.append_chat(f"🧑 You: {user_text}")
        filename = save_note(user_text)
        if filename:
            self.append_chat(f"✅ 系统消息：已存入 Inbox（{filename}）")
        else:
            self.append_chat(f"❌ 系统消息：存储失败")
        self.input_box.delete("1.0", "end")
        # Call AI in thread
        threading.Thread(target=self.call_ai_and_display, args=(user_text,), daemon=True).start()
        return "break"

    def on_shift_enter(self, event=None):
        self.input_box.insert("insert", "\n")
        return "break"

    def on_paste(self, event=None):
        try:
            self.after(50, self.handle_clipboard)
        except Exception as e:
            self.append_chat(f"❌ 粘贴失败: {e}")
        return "break"

    def handle_clipboard(self):
        # Robust clipboard handling using win32clipboard with safe open/close
        try:
            import win32clipboard
            import win32con
        except Exception as e:
            self.append_chat(f"❌ 粘贴失败: missing pywin32: {e}")
            return

        try:
            win32clipboard.OpenClipboard()
            try:
                # Files (CF_HDROP)
                if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
                    files = win32clipboard.GetClipboardData(win32con.CF_HDROP)
                    for file_path in files:
                        ok, msg = save_file_to_inbox(file_path)
                        if ok:
                            self.append_chat(f"📂 File captured: {msg}")
                        else:
                            self.append_chat(f"❌ File error: {msg}")
                    return

                # Text (Unicode)
                if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
                    try:
                        text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
                    except Exception:
                        text = None
                    if text:
                        text = text.strip()
                        # If text is a path to an existing file, copy it
                        if os.path.exists(text):
                            ok, msg = save_file_to_inbox(text)
                            if ok:
                                self.append_chat(f"📂 File captured: {msg}")
                            else:
                                self.append_chat(f"❌ File error: {msg}")
                            return
                        # Otherwise, paste text into input box
                        self.input_box.insert('end', text)
                        return

                # No supported format
                self.append_chat("❌ 粘贴失败: 剪贴板内无可识别的文件或文本")
            finally:
                try:
                    win32clipboard.CloseClipboard()
                except Exception:
                    pass
        except Exception as e:
            self.append_chat(f"❌ 粘贴失败: {e}")

    def append_chat(self, msg):
        self.chat_history.configure(state="normal")
        self.chat_history.insert("end", msg + "\n")
        self.chat_history.see("end")
        self.chat_history.configure(state="disabled")
        self.chat_history_list.append(msg)

    def call_ai_and_display(self, user_text):
        # Retrieve local context (RAG) and call AI
        self.append_chat("🤖 Jarvis: 正在思考...")
        try:
            ctxt_items = retrieve_context(user_text)
            ctxt = build_context_text(ctxt_items)
            if ctxt:
                prompt = f"以下是来自本地记忆的相关片段，请以中文、简洁并结合这些片段回答：\n{ctxt}\n\n用户问题：{user_text}"
            else:
                prompt = f"请用中文回答，简洁扼要：\n{user_text}"
        except Exception:
            prompt = f"请用中文回答，简洁扼要：\n{user_text}"
        response = call_ai(prompt)
        if response:
            self.queue.put(f"🤖 Jarvis: {response}")
        else:
            self.queue.put("🤖 Jarvis: [AI 无法响应]")

    def process_queue(self):
        try:
            while not self.queue.empty():
                msg = self.queue.get_nowait()
                self.append_chat(msg)
        except Exception:
            pass
        self.after(200, self.process_queue)

if __name__ == "__main__":
    app = OmniBoxV2()
    app.mainloop()
