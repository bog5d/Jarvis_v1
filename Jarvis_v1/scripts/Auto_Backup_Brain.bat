@echo off
chcp 65001
cd /d "D:\My_System"

echo [%date% %time%] 正在启动备份流程... >> backup_log.txt

:: --- 智能联网检测 (等待 60 秒) ---
timeout /t 60 /nobreak >nul

:: 1. 添加更改
git add .

:: 2. 提交更改
git commit -m "Auto Backup: %date% %time%" >> backup_log.txt 2>&1

:: 3. 推送
git push origin main >> backup_log.txt 2>&1

if %errorlevel% equ 0 (
    echo [%date% %time%] ✅ 备份成功 >> backup_log.txt
) else (
    echo [%date% %time%] ❌ 备份失败 (可能是网络仍不稳定) >> backup_log.txt
)

echo ---------------------------------------- >> backup_log.txt
