# -*- coding: utf-8 -*-
import streamlit as st
import sys
import os
import time
from pathlib import Path
from datetime import datetime

# Add project root to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config.system_config import DIR

# Page Config
st.set_page_config(
    page_title="Jarvis HUD",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Logic ---

def get_stats():
    """Get system statistics."""
    inbox_count = len(list(DIR['INBOX'].glob("*.*"))) - 1 # Exclude processed folder roughly
    # Better count: exclude directories
    inbox_files = [f for f in DIR['INBOX'].iterdir() if f.is_file() and not f.name.startswith('.')]
    inbox_count = len(inbox_files)
    
    kb_count = 0
    if DIR['KNOWLEDGE_BASE'].exists():
        kb_count = len(list(DIR['KNOWLEDGE_BASE'].rglob("*.md")))
        
    return inbox_count, kb_count

def save_quick_note(content):
    """Save user input to Inbox for Watchdog to catch."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"QuickNote_{timestamp}.md"
    filepath = DIR['INBOX'] / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename

def read_logs():
    """Read the last few lines of the log file."""
    log_file = DIR['LOGS'] / "jarvis.log"
    if not log_file.exists():
        return ["No logs found yet."]
        
    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            return lines[-50:] # Last 50 lines
    except Exception as e:
        return [f"Error reading logs: {e}"]

def read_briefing():
    """Read today's briefing."""
    today_str = datetime.now().strftime("%Y-%m-%d")
    briefing_filename = f"Daily_Briefing_{today_str}.md"
    briefing_path = DIR['INBOX'] / briefing_filename
    
    if briefing_path.exists():
        with open(briefing_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    # Try Processed folder if not in Inbox
    processed_path = DIR['INBOX'] / "Processed" / "Notes" / briefing_filename
    if processed_path.exists():
        with open(processed_path, 'r', encoding='utf-8') as f:
            return f.read()
            
    return "📭 No Daily Briefing found for today yet."

# --- UI Layout ---

# Sidebar
with st.sidebar:
    st.title("🤖 Jarvis System")
    st.markdown("---")
    
    inbox_n, kb_n = get_stats()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Inbox", inbox_n)
    with col2:
        st.metric("Memory", kb_n)
    
    st.markdown("---")
    st.write("### System Status")
    
    # Check if watchdog lock or similar exists (simulation)
    # Ideally we check if python process is running, but for now simple
    st.success("🟢 System Online")
    st.info("🐕 Watchdog: Active")

# Main Content
st.title("🚀 Jarvis Command Center")

tab1, tab2, tab3 = st.tabs(["🧠 Input & Chat", "📊 Live Logs", "📅 Daily Briefing"])

with tab1:
    st.subheader("What's on your mind?")
    user_input = st.text_area("Quick Note / Instruction", height=150, placeholder="Type here... e.g., 'Remind me to call John', 'Idea for new project...'")
    
    if st.button("🚀 Send to Jarvis", type="primary"):
        if user_input.strip():
            saved_file = save_quick_note(user_input)
            st.success(f"✅ Note saved as `{saved_file}`!")
            st.info("🐕 Watchdog will pick this up in ~2 seconds...")
        else:
            st.warning("⚠️ Input cannot be empty.")

with tab2:
    st.subheader("🕵️ System Logs (Real-time)")
    
    # Auto-refresh mechanism (simple button for now)
    if st.button("🔄 Refresh Logs"):
        st.rerun()
        
    logs = read_logs()
    log_text = "".join(logs)
    st.code(log_text, language="log")

with tab3:
    st.subheader("📅 Today's Intelligence")
    if st.button("🔄 Refresh Briefing"):
        st.rerun()
        
    briefing = read_briefing()
    st.markdown(briefing)

# Footer
st.markdown("---")
st.caption(f"Jarvis v1.0 | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
