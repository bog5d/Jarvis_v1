import streamlit as st
import time
import yaml
from pathlib import Path
from datetime import datetime
import sys

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))
from src.chat_engine import JarvisChat
from src.handlers.audio_handler import AudioHandler

st.set_page_config(
    page_title="Jarvis Command Center",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Styles ---
st.markdown("""
<style>
    /* 移除顶部多余空白，让布局更紧凑 */
    .block-container {
        padding-top: 2rem;
    }
    
    /* Tabs 容器 - 更加清爽的底部线条 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 30px;
        border-bottom: 1px solid #f0f2f6;
        padding-bottom: 5px;
    }

    /* 单个 Tab - 移除黑色背景，改为透明，极简风格 */
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 0px;
        gap: 5px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: #666; /* 柔和的灰色 */
        font-weight: 500;
        font-size: 16px;
        border: none;
        transition: all 0.3s ease;
    }

    /* 选中状态 - 只有底部高亮，文字变黑 */
    .stTabs [aria-selected="true"] {
        background-color: transparent;
        color: #000;
        font-weight: 600;
        border-bottom: 3px solid #FF4B4B; /* 使用醒目的红色线条 */
    }
    
    /* 悬停状态 */
    .stTabs [data-baseweb="tab"]:hover {
        color: #FF4B4B;
        background-color: transparent;
    }

    /* 优化 Metric 显示，增加轻微卡片感，适配白色背景 */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08); /* 轻微阴影 */
        border: 1px solid #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

# --- Init Jarvis ---
if "jarvis" not in st.session_state:
    config_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    
    # Load Config
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        
    st.session_state.jarvis = JarvisChat(str(config_path))
    st.session_state.jarvis.initialize_context()
    
    # Init AudioHandler for Voice Chat
    st.session_state.audio_handler = AudioHandler(
        output_dir=config['paths']['output_dir'],
        api_key=config['aliyun']['api_key']
    )

if "last_check_time" not in st.session_state:
    st.session_state.last_check_time = time.time()

def check_for_new_drafts():
    """检查是否有新处理完成的奏折 (Drafts)"""
    drafts_dir = Path("D:/My_System/01_Drafts")
    if not drafts_dir.exists(): return

    # 查找自上次检查以来新修改/生成的文件
    new_files = []
    for f in drafts_dir.glob("*.md"):
        if "每日内阁晨报" in f.name: continue
        if f.stat().st_mtime > st.session_state.last_check_time:
            new_files.append(f)
    
    if new_files:
        for f in new_files:
            try:
                content = f.read_text(encoding='utf-8')
                # 构造通知消息
                msg = f"✅ **【系统通知】后台已完成文件处理**\n\n📄 **文件**: `{f.name}`\n\n**摘要内容**:\n{content[:500]}...\n\n(已存入记忆库，您现在可以就此提问)"
                st.session_state.jarvis.messages.append({"role": "assistant", "content": msg})
            except Exception:
                pass
        # 更新检查时间
        st.session_state.last_check_time = time.time()

# 每次页面刷新/交互时，都检查一次
check_for_new_drafts()

# --- Sidebar: Auto-Refresh ---
with st.sidebar:
    st.title("⚙️ 控制台设置")
    auto_refresh = st.toggle("🔴 实时监控模式", value=False, help="开启后每 5 秒自动刷新页面，以便即时接收后台处理完成的通知。注意：打字时建议关闭，以免打断输入。")
    
    if st.button("🔄 手动刷新"):
        st.rerun()

if auto_refresh:
    time.sleep(5)
    st.rerun()

# --- Tabs ---
tab1, tab2 = st.tabs(["📊 监控大屏 (Monitor)", "💬 顾问对话 (Chat)"])

# === Tab 1: Monitor ===
with tab1:
    st.title("📊 Jarvis System Monitor")
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    
    drafts_dir = Path("D:/My_System/01_Drafts")
    briefing_dir = Path("D:/My_System/02_Briefings")
    
    # Count today's drafts
    today_drafts = 0
    one_day_ago = time.time() - 24 * 3600
    if drafts_dir.exists():
        today_drafts = sum(1 for f in drafts_dir.glob("*.md") if f.stat().st_mtime > one_day_ago and "每日内阁晨报" not in f.name)
    
    # Last briefing time
    last_briefing = "无"
    if briefing_dir.exists():
        briefings = list(briefing_dir.glob("📅_每日内阁晨报_*.md"))
        if briefings:
            latest = max(briefings, key=lambda p: p.stat().st_mtime)
            last_briefing = latest.name.replace("📅_每日内阁晨报_", "").replace(".md", "")
            briefing_content = latest.read_text(encoding='utf-8')
        else:
            briefing_content = "暂无今日晨报"
    else:
        briefing_content = "目录不存在"

    with col1:
        st.metric("今日奏折 (24h)", f"{today_drafts} 份")
    with col2:
        st.metric("最新晨报日期", last_briefing)
    with col3:
        st.metric("系统状态", "🟢 Online")

    st.divider()
    
    st.subheader("📅 最新内阁晨报")
    st.markdown(briefing_content)

# === Tab 2: Chat ===
with tab2:
    st.title("💬 内阁首辅 (DeepSeek)")

    # --- File Uploader ---
    with st.expander("📎 上传奏折 (PDF/Audio/Text)", expanded=False):
        uploaded_file = st.file_uploader("选择文件上传至 Inbox", type=['pdf', 'txt', 'md', 'mp3', 'wav', 'm4a'])
        if uploaded_file is not None:
            inbox_dir = Path("D:/My_System/Inbox")
            inbox_dir.mkdir(parents=True, exist_ok=True)
            save_path = inbox_dir / uploaded_file.name
            
            try:
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"✅ 已呈递奏折: {uploaded_file.name}，内阁正在处理中...")
                
                # --- 关键修改：立即读取文件内容并注入对话上下文 ---
                file_content = ""
                if uploaded_file.type == "text/plain" or uploaded_file.name.endswith(".md") or uploaded_file.name.endswith(".txt"):
                    # 文本文件直接读取
                    uploaded_file.seek(0)
                    file_content = uploaded_file.read().decode("utf-8")
                elif uploaded_file.type == "application/pdf":
                    # PDF 简单提取 (需要安装 pypdf，这里做个简单的提示，或者尝试读取)
                    # 为了稳定性，暂时只提示用户文件已上传，等待后台处理
                    file_content = "(PDF文件已上传，后台正在转录中... 请稍后询问)"
                else:
                    file_content = "(音频/二进制文件已上传，后台正在转录中...)"

                if file_content and len(file_content) < 50000: # 限制长度防止爆Token
                     st.session_state.jarvis.messages.append({
                        "role": "system", 
                        "content": f"【系统通知】用户刚刚上传了一份文件《{uploaded_file.name}》。\n如果这是文本，内容如下：\n{file_content}\n\n如果是其他格式，请告知用户后台正在处理。"
                    })
                
            except Exception as e:
                st.error(f"❌ 上传失败: {e}")

    # Display chat history
    # Filter out system prompts for display
    for msg in st.session_state.jarvis.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # --- Input Area ---
    # 1. Audio Input
    audio_value = st.audio_input("🎤 语音输入 (Voice Input)")
    
    # 2. Text Input
    text_prompt = st.chat_input("请下达指令或询问...")
    
    final_prompt = None
    
    # Handle Text Input
    if text_prompt:
        final_prompt = text_prompt
        
    # Handle Audio Input
    elif audio_value:
        # Use hash to prevent re-processing the same audio on rerun
        audio_id = hash(audio_value.getvalue())
        if "last_audio_id" not in st.session_state or st.session_state.last_audio_id != audio_id:
            st.session_state.last_audio_id = audio_id
            
            # Save and Transcribe
            temp_audio_path = Path("temp_voice_input.wav")
            with open(temp_audio_path, "wb") as f:
                f.write(audio_value.getvalue())
            
            with st.spinner("👂 正在听取您的指令..."):
                transcribed_text = st.session_state.audio_handler.transcribe_audio(str(temp_audio_path))
            
            if transcribed_text:
                final_prompt = transcribed_text
                st.toast(f"🗣️ 识别内容: {final_prompt}")
            else:
                st.warning("未能识别到语音内容")
            
            # Cleanup
            try:
                temp_audio_path.unlink()
            except:
                pass

    # Process Message
    if final_prompt:
        # User message
        with st.chat_message("user"):
            st.markdown(final_prompt)
        
        # AI Response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")
            
            # Call Jarvis
            response = st.session_state.jarvis.chat(final_prompt)
            
            message_placeholder.markdown(response)

