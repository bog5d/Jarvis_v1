@echo off
title Jarvis Watchdog - Always On 🐕
color 0B
echo.
echo ========================================================
echo    J A R V I S   A U T O - P I L O T   (Watchdog)
echo ========================================================
echo.
echo [INFO] Monitoring Inbox for new files...
echo [INFO] DO NOT CLOSE THIS WINDOW (Minimize it)
echo.

:: Setup Python Environment
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (set "PY=.venv\Scripts\python.exe") else (set "PY=python")

:: Launch the Service
"%PY%" "Jarvis_v1/utils/watchdog_service.py"

pause
