# Jarvis v1.0 🤖

![Status](https://img.shields.io/badge/Status-Operational-green.svg) ![AI](https://img.shields.io/badge/AI-DeepSeek-blue.svg)

A fully automated "LifeOS" that captures, organizes, analyzes, visualizes, and remembers your digital life.

## 🚀 Quick Start

| Mode | Launcher | Description |
| :--- | :--- | :--- |
| **🟢 Desktop** | `Start_Jarvis_Pro.bat` | Hidden System Tray App. Press `Ctrl+Alt+J` to capture ideas. |
| **🟠 Web HUD** | `Start_HUD.bat` | Visual Dashboard (Streamlit). View Logs & Chat. |
| **🔵 Server** | `Start_Watchdog.bat` | Background Service Only. Auto-processing on file arrival. |

## 🏗️ Architecture

1.  **Librarian**: Sorts incoming files.
2.  **Secretary**: Summarizes text & transcribes audio.
3.  **Cartographer**: Draws Mermaid diagrams from notes.
4.  **Gardener**: Recalls old memories (RAG).
5.  **Reporter**: Updates the dashboard.

## 🛠️ Installation

```bash
# 1. Install Dependencies
pip install -r requirements.txt

# 2. Configure Keys
# Edit config/system_config.py with your API Keys
```

---
*For AI Agents: Please read `project_context.md` for architectural rules.*
