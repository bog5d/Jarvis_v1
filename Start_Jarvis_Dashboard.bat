@echo off
chcp 65001
echo Starting Jarvis Dashboard (Streamlit)...
echo Access via browser: http://localhost:8501
set PYTHONPATH=%~dp0
python -m streamlit run "%~dp0src\dashboard.py" --server.headless false
if %errorlevel% neq 0 (
    echo Error occurred!
    pause
)
pause
