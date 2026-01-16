@echo off
chcp 65001 >nul
title AutoHotkey 安装脚本

echo ============================================
echo   AutoHotkey 安装脚本
echo ============================================
echo.

REM 检查是否已安装 AutoHotkey
where ahk >nul 2>nul
if %errorlevel% equ 0 (
    echo [✓] AutoHotkey 已安装
    echo.
    goto :CHECK_INSTALL
)

echo [✗] AutoHotkey 未安装
echo.

:DOWNLOAD
echo [1/3] 正在下载 AutoHotkey 安装程序...
echo.

REM 下载 AutoHotkey 安装程序
powershell -Command "$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri 'https://www.autohotkey.com/download/ahk-install.exe' -OutFile '%TEMP%\ahk-install.exe'"

if not exist "%TEMP%\ahk-install.exe" (
    echo [✗] 下载失败
    echo 请检查网络连接后重试
    pause
    exit /b 1
)

echo [✓] 下载完成: %TEMP%\ahk-install.exe
echo.

:INSTALL
echo [2/3] 正在安装 AutoHotkey...
echo 注意：安装过程可能需要几分钟，请耐心等待...
echo.

REM 安装 AutoHotkey（静默安装到当前用户目录）
start /wait "" "%TEMP%\ahk-install.exe" /S /D=%LOCALAPPDATA%\AutoHotkey

echo [✓] 安装完成
echo.

:CHECK_INSTALL
echo [3/3] 验证安装...
echo.

REM 等待系统更新
timeout /t 3 /nobreak >nul

REM 刷新 PATH
set PATH=%PATH%;%LOCALAPPDATA%\AutoHotkey

REM 检查是否安装成功
where ahk >nul 2>nul
if %errorlevel% equ 0 (
    echo [✓] AutoHotkey 安装成功！
    ahk /version
) else (
    echo [!] 在 PATH 中未找到 AutoHotkey
    echo 尝试手动查找...
    
    if exist "%LOCALAPPDATA%\AutoHotkey\AutoHotkey.exe" (
        echo [✓] 找到 AutoHotkey: %LOCALAPPDATA%\AutoHotkey\AutoHotkey.exe
        set AHK_PATH=%LOCALAPPDATA%\AutoHotkey
    ) else if exist "%APPDATA%\AutoHotkey\AutoHotkey.exe" (
        echo [✓] 找到 AutoHotkey: %APPDATA%\AutoHotkey\AutoHotkey.exe
        set AHK_PATH=%APPDATA%\AutoHotkey
    ) else (
        echo [✗] 未找到 AutoHotkey，请手动安装
        echo 访问: https://www.autohotkey.com/
        pause
        exit /b 1
    )
)

echo.
echo ============================================
echo   安装完成！
echo ============================================
echo.
echo 下一步操作：
echo 1. 运行自动点击器: D:\My_system\Scripts\start_auto_clicker.bat
echo 2. 或创建桌面快捷方式（可选）
echo.
echo 是否创建桌面快捷方式？ (Y/N)
choice /c YN /n /m "请选择: "

if errorlevel 2 goto :NO_SHORTCUT

echo.
echo 正在创建桌面快捷方式...
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\启动自动点击器.lnk'); $Shortcut.TargetPath = 'D:\My_system\Scripts\start_auto_clicker.bat'; $Shortcut.WorkingDirectory = 'D:\My_system\Scripts'; $Shortcut.Description = '自动点击器 - 远程桌面辅助工具'; $Shortcut.Save()"

if exist "%USERPROFILE%\Desktop\启动自动点击器.lnk" (
    echo [✓] 桌面快捷方式已创建
) else (
    echo [!] 无法创建快捷方式
)

:NO_SHORTCUT
echo.
echo ============================================
echo   自动点击器说明
echo ============================================
echo.
echo 功能：监控常见弹窗并自动点击 Yes/Allow 按钮
echo 适用：通过 Tailscale 远程连接时，避免在手机小屏幕上点击困难
echo.
echo 使用方法：
echo 1. 双击运行 D:\My_system\Scripts\start_auto_clicker.bat
echo 2. 脚本会在后台运行，监控弹窗
echo 3. 按 F12 可退出脚本
echo.
echo 支持的弹窗：
echo   - VS Code 信任作者弹窗
echo   - 浏览器下载允许弹窗
echo   - Windows 安全警告
echo   - 用户账户控制(UAC)
echo.
echo 按任意键退出...
pause >nul