# 项目变更日志 (Changelog)

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 规范。
所有对本项目的重大更改都将记录在此文件中。

## [0.5.0] - 2026-01-10
### Changed
- **System Migration**: 核心存储库从物理磁盘 `D:\My_System` 迁移至 OneDrive 云同步目录 `C:\Users\王波\OneDrive - Personal\my_system`。
- **Core Configuration**: 更新了所有的硬编码路径，确保系统在新的环境路径下可以正常运行。
- **Migration Verification**: 新增 `verify_migration.py` 用于自动监测和修复路径迁移后的文件夹完整性。

## [0.4.0] - 2026-01-07
### Added
- **Historian (Indexer)**: 新增 `src/core/indexer.py`，实现“三级火箭”策略的第二级。能够扫描静态 Markdown 档案，提取 Frontmatter 和内联标签 (#Tag)，构建轻量级 JSON 索引。
- **Librarian (Retriever)**: 新增 `src/core/retriever.py`，实现“零成本”上下文检索。能够根据用户对话中的关键词，自动查找并提取相关历史笔记。
- **RAG Capability**: 升级 `chat_engine.py`，集成检索器。实现了“标签触发式 RAG”，只在需要时（匹配到标签）才读取历史文件，极大降低 Token 消耗。

## [0.3.0] - 2026-01-07
### Added
- **DeepSeek V3 接入**: 全面替换阿里云 Qwen 模型，成为新的“内阁首辅”大脑 (`llm_engine`)。
- **Streamlit 移动指挥所**:
  - 重构 `src/dashboard.py`，采用 **Tabs (分页)** 架构：
    - **Tab 1 Chat**: DeepSeek 聊天窗口，支持流式对话。
    - **Tab 2 Voice**: 集成语音转文字功能。
    - **Tab 3 Files**: 文件监控与手动上传。
  - 增加 **Atomic Tags (原子标签)** 可视化显示，实现内容与元数据的视觉分离。
- **系统级 Prompt**: 新增 `prompts/system_prompt.md`，定义“双轨制标签”输出规范 (Category + Keywords)。
- **Tailscale 适配**: 优化 Dashboard 网络配置，支持局域网/Tailscale 远程访问。

### Changed
- **Config**: `settings.yaml` 新增 `deepseek` 配置节 (API Key, Temperature, Caching)。
- **Doc**: 更新 `project_context.md` 重新定义系统身份为 "Executive Decision Support System" 并固化原子化笔记方法论。

## [0.2.0] - 2026-01-04
### Added
- **PDF 支持**: 新增 `src/handlers/pdf_handler.py`，使用 `pdfplumber` 提取文本并调用 Qwen-Plus 进行总结。
- **配置更新**: `settings.yaml` 新增 `.pdf` 文件类型支持。

## [0.1.0] - 2026-01-04
### Added
- **项目初始化**: 建立 `Jarvis_v1` 核心架构。
- **核心模块**:
  - `src/core/watcher.py`: 基于 `watchdog` 的文件监控系统。
  - `src/handlers/audio_handler.py`: 集成阿里云 DashScope (Paraformer) 实现语音转文字。
  - `src/handlers/text_handler.py`: 集成阿里云 DashScope (Qwen-Plus) 实现文本智能总结。
- **配置管理**:
  - `config/settings.yaml`: 实现路径、文件类型、API Key 的配置分离。
  - `config/settings.example.yaml`: 提供配置模板，保护隐私。
- **文档**:
  - `README.md`: 项目说明书。
  - `ROADMAP.md`: 项目规划与架构说明（AI 交接文档）。
- **工程化**:
  - `.gitignore`: 配置隐私保护规则。
  - `requirements.txt`: 依赖管理。
  - Git 仓库初始化并推送到 GitHub。

### Changed
- **隐私安全**: 将硬编码的 API Key 移至配置文件，并从 Git 追踪中移除。
- **代码重构**: 从单文件脚本重构为模块化架构 (`core`, `handlers`, `utils`)。

### Fixed
- 修复了 `AudioHandler` 和 `TextHandler` 初始化时参数不匹配导致的 `TypeError`。
- 解决了 Git 推送时的网络连接重置问题（配置本地代理）。

## [0.3.0] - 2026-01-04
### Fixed
- **Startup**: Fixed issue where Dashboard browser would not launch automatically on system startup by enforcing \--server.headless false\.
- **Documentation**: Updated project context and changelog for better AI handover.


## [0.4.0] - 2026-01-05
### Added
- **Remote Access**: Added comprehensive guides (MOBILE_GUIDE.md, REMOTE_ACCESS_GUIDE.md) for LAN and Tailscale access.
- **Server Mode**: Configured system power settings to support 'Lid Closed' operation (Clamshell Mode).
- **Mobile Voice**: Implemented st.audio_input in Dashboard for direct voice interaction from mobile devices.

### Fixed
- **Dashboard**: Resolved 502 Bad Gateway error by disabling headless mode and manually handling browser launch.
- **Config**: Fixed KeyError in dashboard.py regarding output directory path.

