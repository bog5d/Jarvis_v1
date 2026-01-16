# Jarvis Automated Deployment Script
# Version: 1.0
# Author: Jarvis AI

param (
    [string]$TargetRoot = "D:\My_System"
)

$ErrorActionPreference = "Stop"
$ScriptPath = $PSScriptRoot
$SourcePath = Split-Path -Parent $ScriptPath # Parent of 'deployment' is 'Jarvis_v1'

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "      Jarvis System Deployment Wizard     " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Check Administrator Privileges
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warning "Please run this script as Administrator to ensure all dependencies can be installed."
    # We continue, but some winget installs might fail or prompt.
}

# 2. Confirm Target Directory
$InputPath = Read-Host "Enter installation root directory (Default: $TargetRoot)"
if (-not [string]::IsNullOrWhiteSpace($InputPath)) {
    $TargetRoot = $InputPath
}
Write-Host "Target Root: $TargetRoot" -ForegroundColor Green

# 3. Create Directory Structure
$Folders = @(
    "$TargetRoot",
    "$TargetRoot\Inbox",
    "$TargetRoot\01_Drafts",
    "$TargetRoot\02_Briefings",
    "$TargetRoot\99_Archive",
    "$TargetRoot\Jarvis_v1"
)

foreach ($folder in $Folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
        Write-Host "Created: $folder" -ForegroundColor Gray
    }
}

# 4. Copy System Files
Write-Host "`n[1/5] Copying System Files..." -ForegroundColor Yellow
Copy-Item -Path "$SourcePath\*" -Destination "$TargetRoot\Jarvis_v1" -Recurse -Force -Exclude ".git", "venv", "__pycache__", "deployment"
# We exclude deployment folder itself to keep the installed version clean, but maybe user wants it? Let's exclude .git and venv mainly.

# 5. Configure Settings
Write-Host "[2/5] Configuring Paths..." -ForegroundColor Yellow
$SettingsFile = "$TargetRoot\Jarvis_v1\config\settings.yaml"
if (Test-Path $SettingsFile) {
    $Content = Get-Content $SettingsFile -Raw
    # Escape backslashes for regex
    $EscapedRoot = $TargetRoot -replace "\\", "\\"
    # Replace D:\My_System with new root. We assume the original file has D:\My_System or D:\\My_System
    # We'll use a generic regex to replace the standard paths
    $Content = $Content -replace "D:\\My_System", $EscapedRoot
    $Content = $Content -replace "D:\\My_System", $EscapedRoot # Handle double backslash if present in regex logic
    Set-Content -Path $SettingsFile -Value $Content
    Write-Host "Updated settings.yaml with new paths." -ForegroundColor Green
} else {
    Write-Warning "settings.yaml not found!"
}

# 6. Python Environment Setup
Write-Host "`n[3/5] Setting up Python Environment..." -ForegroundColor Yellow
if (-not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Host "Python not found. Attempting to install via Winget..." -ForegroundColor Magenta
    winget install Python.Python.3.13 -e --source winget --accept-package-agreements --accept-source-agreements
    # Refresh env vars
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

$PythonPath = "$TargetRoot\Jarvis_v1"
Set-Location $PythonPath

if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

Write-Host "Installing dependencies..."
.\venv\Scripts\python -m pip install --upgrade pip
.\venv\Scripts\pip install -r requirements.txt

# 7. Create Desktop Shortcut
Write-Host "`n[4/5] Creating Shortcuts..." -ForegroundColor Yellow
$WshShell = New-Object -comObject WScript.Shell
$DesktopPath = [System.Environment]::GetFolderPath('Desktop')
$Shortcut = $WshShell.CreateShortcut("$DesktopPath\Jarvis HUD.lnk")
$Shortcut.TargetPath = "$TargetRoot\Jarvis_v1\Start_Jarvis_HUD.bat"
$Shortcut.WorkingDirectory = "$TargetRoot\Jarvis_v1"
$Shortcut.IconLocation = "shell32.dll,3" # Folder icon, or maybe a custom one if we had it
$Shortcut.Save()
Write-Host "Shortcut created on Desktop." -ForegroundColor Green

# 8. Optional Software
Write-Host "`n[5/5] Checking External Tools..." -ForegroundColor Yellow
$InstallObsidian = Read-Host "Do you want to install Obsidian (Note Taking App)? (Y/N)"
if ($InstallObsidian -eq 'Y') {
    winget install Obsidian.Obsidian -e --source winget
}

Write-Host "`n==========================================" -ForegroundColor Cyan
Write-Host "      Deployment Complete!                " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Next Steps:"
Write-Host "1. Install VerySync (http://www.verysync.com/) manually if not installed."
Write-Host "2. Set up sync folder to: $TargetRoot\Inbox"
Write-Host "3. Double click 'Jarvis HUD' on your desktop to start."
Write-Host "4. Read '$ScriptPath\MIGRATION_GUIDE.md' for details."
Pause
