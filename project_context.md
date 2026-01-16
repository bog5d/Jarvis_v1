# 🧠 Jarvis System Context (AI Memory)

> **Note to AI Agents**: This file contains the architectural blueprint and current state of the Jarvis system. Read this first to understand the project context.

## 1. System Identity: "The Cabinet Secretary" (内阁首辅)
Jarvis has evolved into a DeepSeek-powered **Executive Decision Support System**.
*   **Core Brain**: **DeepSeek-V3** (High reasoning capability).
*   **Mission**: Not just automation, but **Knowledge Emergence**. It transforms raw ideas into "Atomic Notes" (原子笔记) suitable for future autobiography or publication.
*   **Personality**: Professional, insightful, proactive. Uses the "Dual-Track Tagging" system for every output.

## 2. Architecture Overview

### 📂 Folder Structure (The "Palace" Layout)
*   **`C:\Users\王波\OneDrive - Personal\my_system\Inbox` (The Box)**:
    *   Entry point for all raw files (Audio, PDF, Text).
    *   *Action*: Watcher monitors this.
*   **`C:\Users\王波\OneDrive - Personal\my_system\01_Drafts` (奏折库)**:
    *   Stores individual processed files (Summaries, Transcripts).
*   **`C:\Users\王波\OneDrive - Personal\my_system\02_Briefings` (御书房)**:
    *   Stores output from `CabinetSecretary` (Daily Briefings).
*   **`C:\Users\王波\OneDrive - Personal\my_system\20_Knowledge_Base/Chat_Logs` (起居注)**:
    *   Long-term conversation history with DeepSeek.
*   **`C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\prompts` (圣旨库)**:
    *   **`system_prompt.md`**: The Constitution. Defines "Dual-Track Tagging" & "Atomic Thinking".

### 🧩 Core Components
1.  **Dashboard (The "Mobile Command Center")**:
    *   **File**: `src/dashboard.py` (Streamlit).
    *   **Access**: Accessible via Mobile (Tailscale/LAN).
    *   **Features**:
        *   **Tab 1 (Chat)**: DeepSeek Interface with separated "Atomic Tags" card.
        *   **Tab 2 (Voice)**: Audio recording & transcription.
        *   **Tab 3 (Monitor)**: File status & System health.
    
2.  **Handlers (`src/handlers/`)**:
    *   `PDFHandler`, `AudioHandler`, `TextHandler`.
    *   **AI Engine**: **DeepSeek-V3** for analysis.
    
3.  **Cabinet Secretary (`src/services/cabinet_secretary.py`)**:
    *   Scans `01_Drafts` -> Calls DeepSeek -> Generates Daily Briefing.

4.  **Chat Engine (`src/chat_engine.py`)**:
    *   **Role**: Backend logic for the Chat Interface.
    *   **Logic**: Loads Context -> Injects System Prompt (Tags) -> Calls DeepSeek -> Saves Log.

## 3. Workflow (The "Loop")
1.  **Input**: User talks to Mobile/Dash or drops file.
2.  **Process**: 
    *   If Chat: DeepSeek responds with **Tags** (Category: Project/Insight...).
    *   If File: Handlers transcribe/summarize -> Save to `01_Drafts`.
3.  **Review**: User checks Dashboard.
4.  **Emergence (Phase 3)**: (Planned) Gardener scans Tags -> Suggests "Emergence" (Book Chapters/Insights).

## 4. Key Protocols (The "Constitution")
1.  **Atomic Thinking**: De-contextualize stories into abstract concepts.
2.  **Dual-Track Tagging**: Every AI output MUST include a `**Tags**` section.
3.  **Local First**: Priorities local files and local network (Tailscale).

```
2.  **Process**: Jarvis processes it -> Moves original to `Archive` -> Saves Summary to `01_Drafts`.
3.  **Notify**: HUD Widget counter increments.
4.  **Briefing**:
    *   *Trigger*: Auto-runs at 8:00 AM or on startup if missed.
    *   *Result*: Generates/Updates the Daily Briefing in `02_Briefings`.
5.  **Review**: User checks `02_Briefings` on mobile, ticks checkboxes.
6.  **Chat**: User discusses details with Jarvis via `Start_Jarvis_Chat.bat`.

## 4. Configuration
*   **Config File**: `config/settings.yaml`
*   **Models**: 
    *   **DeepSeek-V3** (Logic, Summarization, Chat) - *Primary Brain*
    *   **Aliyun Paraformer** (ASR) - *Ears*
    *   **Aliyun Qwen** (Fallback Brain)
*   **Prompts**: Managed externally in `prompts/` folder.

## 5. Recent Changelog (2026-01-05)
*   [Feat] **Web UI Refactor**: Rebuilt the frontend (`src/web_ui/index.html`) to mimic Google Gemini's aesthetic (Material Design 3).
*   [Feat] **Split-Screen Mode**: Implemented a "Canvas" style layout where reports open in a side panel while chatting.
*   [Feat] **Backend API**: Created a lightweight Python backend (`src/web_ui/server.py`) to bridge the frontend with DeepSeek API.
*   [Feat] **Real-time Chat**: Connected the Web UI to DeepSeek-V3 for live, interactive dialogue.
*   [Feat] **Remote Access**: Integrated Tailscale for secure, anywhere-access to Jarvis Dashboard.
*   [Feat] **Server Mode**: Configured power settings to allow laptop operation with lid closed (Clamshell Mode).
*   [Feat] **Mobile Voice**: Added native voice input support in Dashboard for mobile browsers.
*   [Fix] **Dashboard Startup**: Fixed 502 Bad Gateway errors by disabling headless mode and manually launching browser.
*   [Docs] **Guides**: Added `MOBILE_GUIDE.md` and `REMOTE_ACCESS_GUIDE.md`.

## 6. Web UI Architecture (The "Gemini" Interface)
*   **Frontend**: Single-file HTML (`src/web_ui/index.html`) using Tailwind CSS (CDN) and Marked.js.
*   **Backend**: `src/web_ui/server.py` (Python `http.server` + `urllib`).
*   **API**: Direct integration with DeepSeek API (`deepseek-chat`).
*   **Features**:
    *   **Chat**: Real-time conversation with "Thinking" state.
    *   **Briefing Panel**: Markdown rendering of daily reports in a collapsible side panel.
    *   **Responsive**: Mobile-friendly sidebar and layout.

## 7. Remote Access & Server Mode (The "Throne Room")
*   **Server Mode**: Laptop configured to stay awake with lid closed (PowerCfg).
*   **Remote Access**: Tailscale VPN integration for secure anywhere-access.
*   **Mobile Guide**: See `MOBILE_GUIDE.md` and `REMOTE_ACCESS_GUIDE.md`.

## 7. Deployment & Migration (The "Colonization" Protocol)
*   **Strategy**: "One-Click" Deployment via deployment/setup.bat.
*   **Capabilities**:
    *   Auto-installs Python environment.
    *   Replicates folder structure (Inbox, Drafts, etc.).
    *   Configures paths in settings.yaml dynamically.
    *   Creates Desktop Shortcuts.
*   **Documentation**: See deployment/MIGRATION_GUIDE.md for detailed user instructions (including Mobile Sync setup).
