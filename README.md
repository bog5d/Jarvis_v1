# Jarvis_v1

> **🤖 To AI Assistant (AI 助手必读)**
> 
> 1. **Context**: Before starting any task, **PLEASE READ** `ROADMAP.md` (for architecture & plans) and `CHANGELOG.md` (for history).
> 2. **Protocol**: 
>    - Follow the modular architecture: `Watcher` -> `Handlers`.
>    - Keep configuration separated in `config/settings.yaml`.
>    - **Update `CHANGELOG.md`** after every significant change.
> 3. **Current Goal**: Check `ROADMAP.md` for the latest P0 tasks.

---

个人知识库自动化系统。监控指定目录，自动处理录音（转录）和文本文件（处理/归档）。

## 目录结构

- `config/`: 配置文件
- `src/core/`: 核心逻辑 (Watcher)
- `src/handlers/`: 业务处理模块 (Audio, Text)
- `src/utils/`: 工具函数


## 部署与同步 (Deployment & Sync)

为了实现“从灵感到影响力”的闭环，建议配合 **微力同步 (VerySync)** 使用：

1.  **手机端回环 (Mobile Feedback Loop)**:
    *   在电脑端安装微力同步。
    *   将输出目录 `D:\My_System\01_Drafts` 添加为同步文件夹。
    *   将同步密钥发送至手机端微力同步。
    *   **效果**: 手机端可实时查看 Jarvis 生成的 AI 总结和笔记。

## 快速开始

1. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```

2. 修改配置 (可选):
   编辑 `config/settings.yaml` 设置监控路径。

3. 运行:
   ```bash
   python main.py
   ```
