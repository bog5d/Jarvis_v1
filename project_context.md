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

### 🧩 Core Components
1.  **Watcher (`src/core/watcher.py`)**:
    *   Real-time file monitoring.
    *   **Startup Check**: Automatically triggers `CabinetSecretary` if today's briefing is missing.
2.  **Handlers (`src/handlers/`)**:
    *   `PDFHandler`, `AudioHandler`, `TextHandler`.
    *   **Standard**: All outputs now include **YAML Frontmatter** (Metadata) for easier parsing.
3.  **Cabinet Secretary (`src/services/cabinet_secretary.py`)**:
    *   **Logic**: Scans `01_Drafts` for files modified in the last 24h.
    *   **AI**: Calls `qwen-max` to aggregate, analyze, and highlight "Decisions Needed" (需圣裁事项).
    *   **Output**: Generates the Daily Briefing Markdown.
4.  **HUD Widget (`src/hud_widget.py`)**:
    *   **Tech**: Python `tkinter` (No external UI deps).
    *   **Features**:
        *   **Zen Mode**: Compact, shows daily file count.
        *   **Active Mode (Hover)**: Expands to show "Latest File" and "Pending Decisions" (scraped from Briefing).
        *   **Cyberpunk UI**: Transparent, frameless, always-on-top.

## 3. Workflow (The "Loop")
1.  **Input**: User drops file into `Inbox` (PC or Mobile Sync).
2.  **Process**: Jarvis processes it -> Moves original to `Archive` -> Saves Summary to `01_Drafts`.
3.  **Notify**: HUD Widget counter increments.
4.  **Briefing**:
    *   *Trigger*: Auto-runs on startup OR manually triggered.
    *   *Result*: Generates/Updates the Daily Briefing in `02_Briefings`.
5.  **Review**: User checks `02_Briefings` on mobile for high-level overview.

## 4. Configuration
*   **Config File**: `config/settings.yaml`
*   **Model**: `qwen-max` (Briefing), `qwen-plus` (Summaries).
*   **API**: Aliyun DashScope.

## 5. Recent Changelog (2026-01-04)
*   [Feat] Implemented `CabinetSecretary` service.
*   [Feat] Created `02_Briefings` dedicated folder.
*   [Feat] Added `Start_Jarvis_HUD.bat` for one-click silent startup.
*   [Feat] Developed **HUD Widget 3.0** with Zen/Active modes and Briefing integration.
*   [Refactor] Updated all Handlers to use YAML Frontmatter.

## 4. Deployment & Migration (The "Colonization" Protocol)
*   **Strategy**: "One-Click" Deployment via deployment/setup.bat.
*   **Capabilities**:
    *   Auto-installs Python environment.
    *   Replicates folder structure (Inbox, Drafts, etc.).
    *   Configures paths in settings.yaml dynamically.
    *   Creates Desktop Shortcuts.
*   **Documentation**: See deployment/MIGRATION_GUIDE.md for detailed user instructions (including Mobile Sync setup).
