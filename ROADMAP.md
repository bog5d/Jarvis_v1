# Jarvis_v1 项目路线图 (Roadmap) & 架构说明

> **致 AI 助手 (To AI Assistant)**: 
> 如果你接手此项目，请务必先阅读本文件。本项目采用模块化架构，修改功能时请遵循“配置分离”和“单一职责”原则。

## 1. 项目现状 (Current Status)
- **核心架构**: `Watchdog` 监控 -> `EventHandler` 分发 -> `Handlers` 处理。
- **已实现功能**:
  - ✅ 基础文件监控 (`src/core/watcher.py`)
  - ✅ 阿里云语音转写 (`src/handlers/audio_handler.py` - Paraformer)
  - ✅ 文本智能总结 (`src/handlers/text_handler.py` - Qwen-Plus)
  - ✅ 隐私保护 (API Key 分离)
  - ✅ Git 存档

## 2. 待优化方向 (Optimization Backlog)

### 优先级 P0 (近期目标)
- [ ] **PDF 支持**: 新增 `src/handlers/pdf_handler.py`，使用 `pdfplumber` 提取文本并总结。
- [ ] **错误重试机制**: 当前 API 调用失败仅记录日志，需要增加 `retrying` 装饰器进行自动重试。
- [ ] **长文本处理**: 针对超过 Token 限制的长文，实现“分段总结 + 汇总”逻辑。

### 优先级 P1 (中期目标)
- [ ] **本地日志文件**: 将日志输出到 `logs/jarvis.log`，并按天轮转，方便排查问题。
- [ ] **图片 OCR**: 支持上传图片，调用阿里云 OCR 或多模态大模型识别文字。
- [ ] **Docker 化**: 编写 `Dockerfile`，方便在 NAS 或服务器上一键部署。

### 优先级 P2 (远期愿景)
- [ ] **Web 界面**: 提供一个简单的网页查看处理历史和结果。
- [ ] **知识库入库**: 将处理后的 Markdown 自动存入 Notion 或 Obsidian 库。

## 3. 架构导航 (Architecture Map)

- **入口**: `main.py` (负责加载配置、初始化日志、启动 Watcher)
- **配置**: `config/settings.yaml` (所有路径、Key、Prompt 都在这里，**严禁硬编码**)
- **核心**: `src/core/watcher.py` (只负责监控和分发，不写具体业务逻辑)
- **业务**: `src/handlers/` (所有的实际处理逻辑都在这里，新增功能请在此处新建文件)

## 4. 开发规范 (Guidelines)
1. **修改配置**: 如果需要新增参数，先在 `config/settings.yaml` 添加，再在代码中读取。
2. **依赖管理**: 引入新库后，必须更新 `requirements.txt`。
3. **日志**: 所有输出必须使用 `logger.info` 或 `logger.error`，禁止使用 `print`。
