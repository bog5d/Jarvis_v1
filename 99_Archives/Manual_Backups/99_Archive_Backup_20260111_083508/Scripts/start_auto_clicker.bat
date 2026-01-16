@echo off
chcp 65001 >nul
title 自动点击器启动脚本

echo ============================================
echo   自动点击器启动脚本
echo ============================================
echo.
echo 功能：启动自动点击器，监控常见弹窗并自动点击
echo 适用：通过Tailscale远程连接时，避免在手机小屏幕上点击困难
echo.

REM 检查AutoHotkey是否安装
where ahk >nul 2>nul
if %errorlevel% equ 0 (
    echo [✓] AutoHotkey 已安装
    goto :RUN_SCRIPT
) else (
    echo [✗] AutoHotkey 未安装
    echo.
    echo 请安装 AutoHotkey 以运行自动点击器：
    echo 1. 访问 https://www.autohotkey.com/
    echo 2. 下载并安装 AutoHotkey
    echo 3. 安装完成后重新运行此脚本
    echo.
    echo 或者，您可以选择：
    echo    A) 我已完成安装，继续运行
    echo    B) 退出脚本
    echo.
    choice /c AB /n /m "请选择 (A/B): "
    
    if errorlevel 2 (
        echo 退出脚本
        pause
        exit /b 1
    )
    
    where ahk >nul 2>nul
    if %errorlevel% neq 0 (
        echo 仍然未找到 AutoHotkey，请确保已正确安装
        pause
        exit /b 1
    )
)

:RUN_SCRIPT
echo.
echo 正在启动自动点击器...
echo 脚本位置: %~dp0auto_clicker.ahk
echo.

REM 检查脚本文件是否存在
if not exist "%~dp0auto_clicker.ahk" (
    echo [错误] 未找到 auto_clicker.ahk 脚本文件
    pause
    exit /b 1
)

REM 运行AutoHotkey脚本
echo 按 Ctrl+C 停止脚本
echo.

REM 设置AutoHotkey路径
set AHK_PATH=C:\Users\王波\AppData\Local\AutoHotkey\AutoHotkey.exe

REM 检查AutoHotkey是否存在
if not exist "%AHK_PATH%" (
    echo [错误] 未找到 AutoHotkey: %AHK_PATH%
    echo 请运行 install_autohotkey_simple.bat 安装 AutoHotkey
    pause
    exit /b 1
)

echo 使用 AutoHotkey: %AHK_PATH%
echo.

"%AHK_PATH%" "%~dp0auto_clicker.ahk"

if %errorlevel% neq 0 (
    echo.
    echo [错误] 运行脚本时出错
    echo 可能的原因：
    echo 1. AutoHotkey 安装不完整
    echo 2. 脚本文件损坏
    echo 3. 权限不足
    echo.
    pause
    exit /b 1
)

echo.
echo 脚本已正常退出
pause