import streamlit as st
import time
import yaml
import sys
import os
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))

# Import core modules
from src.chat_engine import JarvisChat
from src.handlers.audio_handler import AudioHandler

# --- Page Configuration ---
st.set_page_config(
    page_title="Jarvis Mobile",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS Styles ---
st.markdown("""
<style>
    /* Tags Styling */
    .tag-container {
        background-color: #f8f9fa;
        padding: 12px;
        border-radius: 8px;
        border-left: 4px solid #ff4b4b;
        font-size: 0.9em;
        margin-top: 12px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    .tag-header {
        font-weight: 600;
        color: #ff4b4b;
        margin-bottom: 4px;
        display: block;
    }
    
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        border-bottom: 1px solid #eee;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        font-size: 16px;
        font-weight: 500;
        color: #666;
    }
    .stTabs [aria-selected="true"] {
        color: #ff4b4b !important;
        border-bottom: 2px solid #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# --- Initialization ---
if "jarvis" not in st.session_state:
    config_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        st.error(f"Failed to load config: {e}")
        st.stop()
    st.session_state.jarvis = JarvisChat(str(config_path))
    st.session_state.jarvis.initialize_context()
    st.session_state.audio_handler = AudioHandler(output_dir=config['paths']['output_dir'], api_key=config['aliyun']['api_key'])

# --- Helper: Render Message ---
def render_message(role, content):
    with st.chat_message(role):
        if "**Tags**" in content:
            main_text, tags_part = content.split("**Tags**", 1)
            st.markdown(main_text.strip())
            st.markdown(f"""
            <div class="tag-container">
                <span class="tag-header">🏷️ Atomic Tags:</span>
                {tags_part.strip()}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(content)

# --- Layout: Tabs ---
tab_chat, tab_voice, tab_monitor = st.tabs(["💬 指挥中心 (Chat)", "🎙️ 语音控制 (Voice)", "📊 每周洞察 (Insights)"])

# === Tab 1: Chat ===
with tab_chat:
    current_history = st.session_state.jarvis.messages
    for msg in current_history:
        if msg["role"] != "system":
            render_message(msg["role"], msg["content"])

    if prompt := st.chat_input("What's on your mind?"):
        render_message("user", prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.jarvis.chat(prompt)
                render_message("assistant", response)

# === Tab 2: Voice ===
with tab_voice:
    st.title("🎙️ Voice Command")
    audio_value = st.audio_input("Record Voice Note")
    if audio_value:
        audio_id = hash(audio_value.getvalue())
        if "last_audio_id" not in st.session_state or st.session_state.last_audio_id != audio_id:
            st.session_state.last_audio_id = audio_id
            temp_path = Path("temp_voice.wav")
            with open(temp_path, "wb") as f: f.write(audio_value.getvalue())
            text = st.session_state.audio_handler.transcribe_audio(str(temp_path))
            if text:
                st.info(f"📝 {text}")
                if st.button("Send to Chat"):
                    st.session_state.jarvis.chat(text)
                    st.success("Sent!")

# === Tab 3: Monitor / Insights ===
with tab_monitor:
    st.title("📊 Weekly Knowledge Garden")
    
    # Load Report
    report_dir = Path("D:/My_System/Jarvis_v1/reports")
    if report_dir.exists():
        reports = list(report_dir.glob("Weekly_Report_*.md"))
        if reports:
            # Sort by modification time
            latest_report = max(reports, key=os.path.getmtime)
            content = latest_report.read_text(encoding='utf-8')
            
            st.markdown(f"### 📅 Report: {latest_report.name}")
            st.markdown(content)
            
            if st.button("🔄 Refresh Report"):
                # Call gardener manually? Or just rerun?
                # For now just rerun visuals
                st.rerun()
        else:
            st.info("No reports found. Run gardener.py manually.")
    else:
        st.warning("Report directory not created yet.")
        
    st.divider()
    
    # File Monitor
    st.subheader("📂 System Files")
    col1, col2 = st.columns(2)
    drafts_dir = Path("D:/My_System/01_Drafts")
    if drafts_dir.exists():
        with col1:
            st.caption("Recent Drafts")
            for f in sorted(drafts_dir.glob("*.md"), key=os.path.getmtime, reverse=True)[:5]:
                st.text(f"📄 {f.name}")

