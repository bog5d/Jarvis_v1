# 项目变更日志 (Changelog)

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 规范。
所有对本项目的重大更改都将记录在此文件中。

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

