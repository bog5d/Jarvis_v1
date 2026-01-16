# AutoHotkey 安装脚本
# 自动下载并安装 AutoHotkey

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "   AutoHotkey 安装脚本" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# 检查是否以管理员身份运行
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "警告: 建议以管理员身份运行此脚本以安装到所有用户" -ForegroundColor Yellow
    Write-Host "可以继续安装到当前用户，但某些功能可能受限" -ForegroundColor Yellow
    Write-Host ""
}

# 检查是否已安装 AutoHotkey
$ahkPath = Get-Command autohotkey -ErrorAction SilentlyContinue
if ($ahkPath) {
    Write-Host "[✓] AutoHotkey 已安装: $($ahkPath.Source)" -ForegroundColor Green
    Write-Host ""
    Write-Host "是否重新安装? (Y/N)" -ForegroundColor Yellow
    $reinstall = Read-Host
    if ($reinstall -notmatch '^[Yy]') {
        Write-Host "安装取消" -ForegroundColor Yellow
        exit 0
    }
}

# AutoHotkey 下载信息
$downloadUrl = "https://www.autohotkey.com/download/ahk-install.exe"
$installerPath = "$env:TEMP\ahk-install.exe"

Write-Host "[1/4] 正在下载 AutoHotkey 安装程序..." -ForegroundColor Cyan
try {
    # 使用 Invoke-WebRequest 下载
    $ProgressPreference = 'SilentlyContinue'
    Invoke-WebRequest -Uri $downloadUrl -OutFile $installerPath
    $ProgressPreference = 'Continue'
    
    if (Test-Path $installerPath) {
        Write-Host "[✓] 下载完成: $installerPath" -ForegroundColor Green
    } else {
        Write-Host "[✗] 下载失败" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "[✗] 下载失败: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[2/4] 正在安装 AutoHotkey..." -ForegroundColor Cyan

# 安装参数
# /S 静默安装
# /D=C:\Program Files\AutoHotkey 指定安装目录
$installArgs = "/S"
if ($isAdmin) {
    $installArgs += " /D=C:\Program Files\AutoHotkey"
} else {
    $installArgs += " /D=$env:LOCALAPPDATA\AutoHotkey"
}

try {
    $process = Start-Process -FilePath $installerPath -ArgumentList $installArgs -Wait -PassThru
    
    if ($process.ExitCode -eq 0) {
        Write-Host "[✓] 安装完成" -ForegroundColor Green
    } else {
        Write-Host "[✗] 安装失败，退出代码: $($process.ExitCode)" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "[✗] 安装失败: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[3/4] 验证安装..." -ForegroundColor Cyan

# 等待系统更新 PATH
Start-Sleep -Seconds 2

# 刷新 PATH 环境变量
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# 再次检查是否安装成功
$ahkPath = Get-Command autohotkey -ErrorAction SilentlyContinue
if ($ahkPath) {
    Write-Host "[✓] AutoHotkey 安装成功: $($ahkPath.Source)" -ForegroundColor Green
} else {
    Write-Host "[!] 在 PATH 中未找到 AutoHotkey，尝试手动查找..." -ForegroundColor Yellow
    
    # 尝试常见安装路径
    $possiblePaths = @(
        "C:\Program Files\AutoHotkey\AutoHotkey.exe",
        "C:\Program Files (x86)\AutoHotkey\AutoHotkey.exe",
        "$env:LOCALAPPDATA\AutoHotkey\AutoHotkey.exe",
        "$env:APPDATA\AutoHotkey\AutoHotkey.exe"
    )
    
    $found = $false
    foreach ($path in $possiblePaths) {
        if (Test-Path $path) {
            Write-Host "[✓] 找到 AutoHotkey: $path" -ForegroundColor Green
            $found = $true
            break
        }
    }
    
    if (-not $found) {
        Write-Host "[✗] 未找到 AutoHotkey，请手动安装" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "[4/4] 创建快捷方式..." -ForegroundColor Cyan

# 创建桌面快捷方式
$desktopPath = [Environment]::GetFolderPath("Desktop")
$shortcutPath = Join-Path $desktopPath "启动自动点击器.lnk"

try {
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($shortcutPath)
    $Shortcut.TargetPath = "D:\My_system\Scripts\start_auto_clicker.bat"
    $Shortcut.WorkingDirectory = "D:\My_system\Scripts"
    $Shortcut.Description = "启动自动点击器 - 远程桌面辅助工具"
    $Shortcut.Save()
    
    Write-Host "[✓] 桌面快捷方式已创建: $shortcutPath" -ForegroundColor Green
} catch {
    Write-Host "[!] 无法创建快捷方式: $_" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  安装完成！" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "下一步操作：" -ForegroundColor Yellow
Write-Host "1. 双击桌面上的 '启动自动点击器' 快捷方式" -ForegroundColor White
Write-Host "2. 或运行: D:\My_system\Scripts\start_auto_clicker.bat" -ForegroundColor White
Write-Host ""
Write-Host "脚本功能：" -ForegroundColor Yellow
Write-Host "- 监控常见弹窗并自动点击 Yes/Allow 按钮" -ForegroundColor White
Write-Host "- 特别适用于 Tailscale 远程桌面场景" -ForegroundColor White
Write-Host "- 解决手机小屏幕上点击困难的问题" -ForegroundColor White
Write-Host ""
Write-Host "按任意键退出..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")