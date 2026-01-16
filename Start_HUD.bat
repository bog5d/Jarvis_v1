@echo off
title Jarvis HUD
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (set "PY=.venv\Scripts\python.exe") else (set "PY=python")

echo [INFO] Launching Jarvis Interface...
"%PY%" -m streamlit run Jarvis_v1/app.py
