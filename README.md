# Jarvis_v1

## SCP v3.8｜集团工程原则（仅引用）

现行唯一上位规范：https://github.com/bog5d/grill-to-spec/blob/main/SCP-v3.8.md 。中大型软件、跨模块与AI Agent任务先读中央 README、START_HERE、SCP-v3.8、HARNESS，按 GCCSEG 对齐终局目标及独立验收。L0 小任务按安全/复用/回归简化，不自建Harness。
文件/录音等资料真正被正确处理、归档、可检索并可恢复才算用户效果；监听心跳、Dashboard正常或日志增长不能替代有效完成。持久化执行必须保留合法授权边界。

工程进度不等于用户效果达成率；真实证据、当前生效配置、硬门槛和 UNKNOWN/FAIL 规则按中央 v3.8 执行。不改变既有数据隐私、历史状态或业务授权。

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
