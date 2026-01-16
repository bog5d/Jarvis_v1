@echo off
chcp 65001 >nul
title Jarvis System - Active Processing...
color 0A

:: 1. Setup Environment
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (set "PY=.venv\Scripts\python.exe") else (set "PY=python")

echo ========================================================
echo       J A R V I S   S Y S T E M   (v1.0)
echo ========================================================

:: Step 1: Organize
echo [1/5] 🧹 Librarian: Organizing Inbox...
"%PY%" "Jarvis_v1/agents/librarian.py"

:: Step 2: Analyze
echo [2/5] 👩‍💼 Secretary: Generating Daily Briefing...
"%PY%" "Jarvis_v1/agents/secretary.py"

:: Step 3: Visualize
echo [3/5] 🎨 Cartographer: Drawing Diagrams...
"%PY%" "Jarvis_v1/agents/cartographer.py"

:: Step 4: Recall (New)
echo [4/5] 🏺 Gardener: Rediscovering Knowledge...
"%PY%" "Jarvis_v1/agents/gardener.py"

:: Step 5: Report
echo [5/5] 📊 Reporter: Updating Dashboard...
"%PY%" "Jarvis_v1/agents/reporter.py"

echo.
echo ========================================================
echo ✅ Mission Accomplished. Phase 3 Complete.
echo 📂 Check Inbox for: Daily_Briefing.md (with History)
echo ========================================================
timeout /t 5
