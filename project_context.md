# 🧠 Jarvis System Context (AI Memory)

> **Note to AI Agents**: This file contains the architectural blueprint and current state of the Jarvis system. Read this first to understand the project context.

## 1. System Identity: "The Cabinet Secretary" (内阁首辅)
Jarvis has evolved from a simple file automation script into an **Executive Decision Support System**.
*   **Old Role**: File Converter (Audio -> Text, PDF -> Summary).
*   **New Role**: Cabinet Secretary. It reviews all "Drafts" (奏折) submitted throughout the day and compiles a "Daily Briefing" (每日内阁晨报) for the user (The Emperor/Executive).

## 2. Architecture Overview

### 📂 Folder Structure (The "Palace" Layout)
*   **`D:\My_System\Inbox` (The Box)**:
    *   Entry point for all raw files (Audio, PDF, Text).
    *   *Action*: Watcher monitors this.
*   **`D:\My_System\01_Drafts` (奏折库)**:
    *   Stores individual processed files (Summaries, Transcripts).
    *   *Sync*: Synced to mobile for "Micro-level" lookup.
*   **`D:\My_System\02_Briefings` (御书房)**:
    *   Stores the **Daily Cabinet Briefing** (`📅_每日内阁晨报_YYYY-MM-DD.md`).
    *   *Sync*: Synced to mobile for "Macro-level" decision making.
*   **`D:\My_System\99_Archive` (Royal Archives)**:
    *   Storage for original raw files after processing.
*   **`D:\My_System\20_Knowledge_Base\Chat_Logs` (起居注)**:
    *   Stores chat history with Jarvis for long-term memory context.
*   **`D:\My_System\Jarvis_v1\prompts` (圣旨库)**:
    *   Stores modular system prompts (`secretary_briefing.md`, `audio_summary.md`).

### 🧩 Core Components
1.  **Watcher (`src/core/watcher.py`)**:
    *   Real-time file monitoring.
    *   **Scheduler**: Checks daily at 8:00 AM. If no briefing exists for today, triggers `CabinetSecretary`.
2.  **Handlers (`src/handlers/`)**:
    *   `PDFHandler`, `AudioHandler`, `TextHandler`.
    *   **AI Engine**: Now uses **DeepSeek-V3** for high-level summarization and logic extraction (Aliyun Paraformer still used for ASR).
    *   **Standard**: All outputs now include **YAML Frontmatter** (Metadata).
3.  **Cabinet Secretary (`src/services/cabinet_secretary.py`)**:
    *   **Logic**: Scans `01_Drafts` for files modified **since the last briefing** (Smart Lookback).
    *   **AI**: Calls **DeepSeek-V3** to aggregate, analyze, and highlight "Decisions Needed" (需圣裁事项).
    *   **Output**: Generates the Daily Briefing Markdown with interactive checkboxes.
4.  **Chat Engine (`src/chat_engine.py`)**:
    *   **Role**: Interactive "Chief of Staff" chat interface.
    *   **Memory**: Auto-loads recent chat logs from `20_Knowledge_Base` to maintain context across sessions.
    *   **Archiving**: Real-time saving of conversations to Markdown.
5.  **HUD Widget (`src/hud_widget.py`)**:
    *   **Tech**: Python `tkinter` (No external UI deps).
    *   **Features**: Zen Mode / Active Mode (Hover).

## 3. Workflow (The "Loop")
1.  **Input**: User drops file into `Inbox` (PC or Mobile Sync).
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
*   [Feat] **Remote Access**: Integrated Tailscale for secure, anywhere-access to Jarvis Dashboard.
*   [Feat] **Server Mode**: Configured power settings to allow laptop operation with lid closed (Clamshell Mode).
*   [Feat] **Mobile Voice**: Added native voice input support in Dashboard for mobile browsers.
*   [Fix] **Dashboard Startup**: Fixed 502 Bad Gateway errors by disabling headless mode and manually launching browser.
*   [Docs] **Guides**: Added `MOBILE_GUIDE.md` and `REMOTE_ACCESS_GUIDE.md`.

## 6. Remote Access & Server Mode (The "Throne Room")
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
