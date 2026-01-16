# 🧠 Jarvis System Context (AI Blueprint v1.0)

> **⚠️ NOTE TO AI AGENTS**: EXPERT LEVEL CONTEXT. 
> This file is the **Absolute Truth** of the system architecture. Read this first.

## 1. System Identity: "Jarvis v1.0"
**Owner**: `bog5d`
**Repository**: `https://github.com/bog5d/Jarvis_v1`
A local, privacy-focused "LifeOS" that automates the flow of information from capture to knowledge.
*   **Core Core**: Python 3.12+ (Windows)
*   **Brain**: DeepSeek-V3 (via `openai` compatible API).
*   **Ears**: Aliyun NLS (ASR).
*   **Eyes**: Watchdog (File System Events).
*   **Face**: CustomTkinter (OmniBox) & Streamlit (HUD).

## 2. The "Pentagon" Architecture (5 Agents)

The system is driven by 5 distinct Agents, executed sequentially or triggered by events.

| Agent | File Path | Role | Capabilities |
| :--- | :--- | :--- | :--- |
| **1. Librarian** | `agents/librarian.py` | **Sort & Organize** | Scans `Inbox`, identifies file types (img, doc, audio, note), moves them to `Inbox/Processed/Category`. Handles duplicates. |
| **2. Secretary** | `agents/secretary.py` | **Hear & Read** | Transcribes Audio (.mp3) using Aliyun. Summarizes Text (.md) using DeepSeek. Generates `Daily_Briefing_{date}.md`. |
| **3. Cartographer** | `agents/cartographer.py` | **Visualize** | Scans notes for processes/logic. Appends Mermaid.js diagrams (Flowcharts, Mindmaps) to the bottom of notes. |
| **4. Gardener** | `agents/gardener.py` | **Remember (RAG)** | Maintains `memory.json` index of `20_Knowledge_Base`. Surfaces "Rediscovered Knowledge" (old notes) into the Daily Briefing. |
| **5. Reporter** | `agents/reporter.py` | **Report** | Updates `00_Dashboard/Home.md` with system stats (Files processed, Knowledge count, Storage). |

## 3. The "Nervous System" (Automation)

### 🐕 Watchdog (`utils/watchdog_service.py`)
*   **Role**: The "Always-On" Event Listener.
*   **Trigger**: Detects creation/move events in `01_Inbox`.
*   **Action**: Debounces (2s) -> Triggers the full 5-Step Pipeline (Librarian -> ... -> Reporter).
*   **Launcher**: `Start_Watchdog.bat`.

### 🔮 Omni-Box (`omnibox.py`)
*   **Role**: The Native Desktop Interface (GUI).
*   **Features**:
    *   **System Tray**: Persistent background icon.
    *   **HotKey**: `Ctrl+Alt+J` toggles the input window.
    *   **Quick Input**: Saves text directly to `Inbox/QuickInput_{time}.md`.
*   **Launcher**: `Start_Jarvis_Pro.bat`.

### 📊 HUD (`app.py`)
*   **Framework**: Streamlit.
*   **Role**: Advanced Dashboard (Logs, Manual Chat, Stats).
*   **Launcher**: `Start_HUD.bat`.

## 4. Directory Map

```text
my_system/
├── 01_Inbox/                  <-- The Input Funnel (Monitored)
├── 20_Knowledge_Base/         <-- Long-term Storage (Indexed by Gardener)
├── 00_Dashboard/              <-- System Status Reports
├── Jarvis_v1/                 <-- The Engine Room (This Repo)
│   ├── agents/                <-- The 5 Agents
│   ├── utils/                 <-- AI Brain, Logger, Watchdog
│   ├── config/                <-- `system_config.py` (Paths & Constants)
│   ├── logs/                  <-- Runtime Logs
│   ├── requirements.txt       <-- Dependencies
│   └── omnibox.py             <-- Desktop App Entry
├── Start_Watchdog.bat         <-- Server Mode
├── Start_HUD.bat              <-- Web UI Mode
└── Start_Jarvis_Pro.bat       <-- Desktop App Mode
```

## 5. Development Protocols
1.  **Path Safety**: ALWAYS use `DIR['KEY']` from `config.system_config`. NEVER hardcode paths.
2.  **Log First**: Use `logger` for everything. No `print()`.
3.  **Atomic Edits**: When editing agents, ensure `Run_Jarvis.bat` logic isn't broken.
