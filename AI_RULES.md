# 🤖 AI Agent Protocols (The Prime Directive)

## SCP v3.8｜集团工程原则（仅引用）

现行唯一上位规范：https://github.com/bog5d/grill-to-spec/blob/main/SCP-v3.8.md 。中大型软件、跨模块与AI Agent任务先读中央 README、START_HERE、SCP-v3.8、HARNESS，按 GCCSEG 对齐终局目标及独立验收。L0 小任务按安全/复用/回归简化，不自建Harness。
文件/录音等资料真正被正确处理、归档、可检索并可恢复才算用户效果；监听心跳、Dashboard正常或日志增长不能替代有效完成。持久化执行必须保留合法授权边界。

工程进度不等于用户效果达成率；真实证据、当前生效配置、硬门槛和 UNKNOWN/FAIL 规则按中央 v3.8 执行。不改变既有数据隐私、历史状态或业务授权。

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
