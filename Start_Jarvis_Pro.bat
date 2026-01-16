@echo off
title Jarvis Omni-Box (Background)
color 0B

echo [INFO] Starting Jarvis Engine...
echo [INFO] Watchdog Service: Starting...
echo [INFO] GUI System: Starting...
echo.
echo ===================================================
echo    Jarvis is now running in the System Tray
echo    Press [Ctrl + Alt + J] to summon input box
echo ===================================================

cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (set "PY=.venv\Scripts\python.exe") else (set "PY=python")

:: Launch OmniBox
"%PY%" "Jarvis_v1/omnibox.py"
pause
