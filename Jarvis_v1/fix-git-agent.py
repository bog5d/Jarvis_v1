import autogen
import subprocess
import os
import shutil
import re
import time

# ============================================================
# 1. 强化的原子工具箱 (Enhanced Tools)
# ============================================================

def run_cmd_safe(command: str) -> str:
    """执行命令，带超时和截断，防崩溃"""
    print(f"\n[AI 动作] 执行命令: {command}")
    try:
        # 增加超时到 600秒，防止大文件上传中断
        result = subprocess.run(
            command, shell=True, capture_output=True, text=False, timeout=600
        )
        try:
            stdout = result.stdout.decode('gbk', errors='ignore')
            stderr = result.stderr.decode('gbk', errors='ignore')
        except:
            stdout = str(result.stdout)
            stderr = str(result.stderr)

        full_output = f"{stdout}\n{stderr}"
        
        # 智能截断：保留头部错误信息和尾部进度信息
        if len(full_output) > 2000:
            preview = full_output[:1000] + "\n...[中间省略]...\n" + full_output[-500:]
            return f"RESULT (TRUNCATED):\n{preview}"
        
        if result.returncode != 0:
            return f"EXECUTION FAILED (Code {result.returncode}):\n{full_output}"
        return f"SUCCESS:\n{full_output}"

    except subprocess.TimeoutExpired:
        return "ERROR: Command timed out (600s). Network might be too slow."
    except Exception as e:
        return f"EXCEPTION: {str(e)}"

def fix_network_issues() -> str:
    """
    [新增] 专门解决 'schannel' 和 'handshake' 错误的特效药。
    1. 切换 SSL 后端为 OpenSSL (更稳)
    2. 盲试常用代理端口 (Clash/v2ray)
    """
    print("\n[AI 动作] 正在执行网络急救 (Network Rescue)...")
    log = []
    
    # 1. 切换后端
    subprocess.run("git config --global http.sslBackend openssl", shell=True)
    subprocess.run("git config --global http.sslVerify false", shell=True) # 临时关闭验证以确保连通
    log.append("✅ 已切换 Git SSL 后端为 OpenSSL 并临时允许非安全连接。")
    
    # 2. 盲试设置代理 (针对 netstat 查不到的情况)
    # 这里我们直接尝试最常见的端口，即使不知道哪个是开着的，试了再说
    # 注意：通常 Clash 是 7890，v2ray 是 10808。我们先试 7890。
    subprocess.run("git config --global http.proxy http://127.0.0.1:7890", shell=True)
    log.append("✅ 已强制设置代理为 127.0.0.1:7890 (常见 Clash 端口)。")
    
    return "\n".join(log) + "\n建议：如果依然失败，请尝试让用户手动检查代理软件端口。"

def scan_and_nuke_secrets() -> str:
    """[安全] 扫描密钥并自动加入黑名单"""
    print("\n[AI 动作] 扫描敏感文件...")
    found_secrets = []
    ignore_dirs = {'.git', '.venv', '__pycache__', 'autogen_workspace'}
    
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            path = os.path.join(root, file)
            if os.path.getsize(path) > 2 * 1024 * 1024: continue # 跳过大文件
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if "sk-" in content and len(re.findall(r'sk-[a-zA-Z0-9]{20,}', content)) > 0:
                        if "example" not in file and "agent" not in file:
                            found_secrets.append(path)
            except: pass
    
    if not found_secrets:
        return "SECURE: 未发现新密钥。"
    
    # 写入 gitignore
    with open(".gitignore", "a", encoding="utf-8") as f:
        f.write("\n# [AUTO-BLOCK] Secret Files\n")
        for p in found_secrets:
            rel = p.replace(".\\", "").replace("\\", "/")
            f.write(f"{rel}\n")
    
    return f"WARNING: 发现 {len(found_secrets)} 个密钥文件，已加入 .gitignore。"

def cleanup_environment() -> str:
    """[清理] 移除嵌套 Git 和大文件目录"""
    print("\n[AI 动作] 清理环境...")
    # 1. 移除嵌套 Git
    for root, dirs, files in os.walk("."):
        if root != "." and ".git" in dirs:
            shutil.rmtree(os.path.join(root, ".git"), ignore_errors=True)
    
    # 2. 确保 .gitignore 包含核心目录
    rules = """
99_Archives/
Manual_Backups/
.venv/
__pycache__/
*.log
deepseek_config.json
"""
    if not os.path.exists(".gitignore"):
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write(rules)
    else:
        with open(".gitignore", "r+", encoding="utf-8") as f:
            content = f.read()
            if "99_Archives" not in content:
                f.write(rules)
                
    return "CLEANUP: 嵌套 Git 已移除，黑名单已更新。"

# ============================================================
# 2. 塑造“全能专家”大脑 (The Brain)
# ============================================================

llm_config = {
    "config_list": [{"model": "deepseek-coder", "api_key": "sk-da9d300dd6814aaba1dc112e60dc8202", "base_url": "https://api.deepseek.com"}],
    "temperature": 0.1,
}

SYSTEM_PROMPT = """
你是一个 **全自动 Git 修复与备份专家**。
目标：将代码推送到 `https://github.com/bog5d/Jarvis_v1`。

**核心逻辑 (Loop)：**
遇到任何错误，不要恐慌，根据错误类型选择工具：

1. **错误类型 A: 网络握手失败 (schannel, handshake, unable to access, 443, timed out)**
   - **原因**：没有代理或 SSL 后端不兼容。
   - **对策**：立即调用 `fix_network_issues`。
   - **然后**：再次尝试 `git push`。

2. **错误类型 B: 拒绝推送 (GH013, Secret detected)**
   - **原因**：文件包含 Key。
   - **对策**：调用 `scan_and_nuke_secrets`。
   - **关键步骤**：必须执行 `run_cmd_safe("git rm -r --cached .")` 清理缓存。
   - **然后**：重新 add -> commit -> push。

3. **错误类型 C: 嵌套仓库警告 (embedded git repository)**
   - **对策**：调用 `cleanup_environment`。
   - **然后**：清理缓存并重新 add。

4. **错误类型 D: 远程冲突 (rejected, non-fast-forward)**
   - **对策**：不要试图 pull 或 rebase (太复杂且容易卡死)。
   - **直接方案**：使用 `git push -u origin main --force`。

**标准流程：**
1. 先调用 `cleanup_environment` 确保环境干净。
2. 调用 `scan_and_nuke_secrets` 确保安全。
3. 执行 `git status` 看一眼。
4. 执行 `git add .` -> `git commit -m "Auto Fix"`。
5. 尝试 `git push`。如果失败，根据报错调用对应工具修复，**直到成功**。

**终止条件：**
看到 "Everything up-to-date" 或 "master -> master" / "main -> main" 推送成功信息后，回复 "TERMINATE"。
"""

# ============================================================
# 3. 启动系统
# ============================================================

user_proxy = autogen.UserProxyAgent(
    name="Executor",
    human_input_mode="NEVER",
    code_execution_config=False, 
)

expert = autogen.AssistantAgent(
    name="Jarvis_Expert",
    llm_config=llm_config,
    system_message=SYSTEM_PROMPT
)

# 注册所有工具
autogen.register_function(run_cmd_safe, caller=expert, executor=user_proxy, name="run_cmd_safe", description="执行命令")
autogen.register_function(fix_network_issues, caller=expert, executor=user_proxy, name="fix_network_issues", description="修复 SSL 和 代理问题")
autogen.register_function(scan_and_nuke_secrets, caller=expert, executor=user_proxy, name="scan_and_nuke_secrets", description="扫描并屏蔽密钥文件")
autogen.register_function(cleanup_environment, caller=expert, executor=user_proxy, name="cleanup_environment", description="清理嵌套 Git 和配置 gitignore")

print("🤖 Jarvis 全能专家上线。正在接管网络与文件系统...")
user_proxy.initiate_chat(
    expert,
    message="上次推送失败了（SSL handshake failed）。请你根据最新的情况，自动调整网络设置、清理垃圾文件，并强制推送到 GitHub。"
)