@echo off
chcp 65001
cd /d "%~dp0"

echo ========================================================
echo 🧠 正在启动“数字方舟”备份程序...
echo ========================================================

:: 检查是否关联了远程仓库
git remote -v >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 尚未关联 GitHub 仓库！
    echo 请先运行以下命令（替换为您自己的仓库地址）：
    echo git remote add origin https://github.com/您的用户名/仓库名.git
    pause
    exit /b
)

echo 1. 正在扫描新知识...
git add .

echo 2. 正在记录变更...
git commit -m "Brain Backup: %date% %time%"

echo 3. 正在推送到云端保险箱...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ 备份成功！您的知识已安全存储在 GitHub。
) else (
    echo.
    echo ❌ 备份失败，请检查网络或 GitHub 连接。
)

pause