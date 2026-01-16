@echo off
chcp 65001
echo Starting Jarvis Chat Mode...
set PYTHONPATH=%~dp0
python "%~dp0src\chat_engine.py"
pause