# 🤖 AI Agent Protocols (The Prime Directive)

> **Warning to AI Agents**: 
> Before writing any code or answering architecture questions, you MUST read `project_context.md` first.
> This file defines the "Constitution" of the Jarvis System.

## 1. Context Awareness Rule
*   **Rule**: Always check `CHANGELOG.md` to see the latest state.
*   **Reason**: The system evolves fast (e.g., Qwen -> DeepSeek, Tkinter -> Streamlit). Don't rely on assumptions.

## 2. Tech Stack Constraints
*   **LLM Provider**: DeepSeek V3 (via `openai` client). Do NOT suggest other providers.
*   **Dashboard**: Streamlit (`src/dashboard.py`). Do NOT update `src/web_ui/`.
*   **Network**: Tailscale is the primary remote access method.

## 3. Output Format Protocols
*   **Dual-Track Tagging**: 
    *   All AI interactions (Chat or Summary) MUST generate Tags.
    *   Format: `**Tags**\n* **Category**: ...\n* **Keywords**: ...`
*   **Atomic Notes**:
    *   When processing user input, try to extract abstract concepts rather than just recording events.

## 4. Operational Boundaries
*   **Editing**: When editing `dashboard.py`, ALWAYS preserve the "Tabs" structure (Chat/Voice/Files).
*   **Secrets**: API Keys must be loaded from `config/settings.yaml` or Environment Variables.
