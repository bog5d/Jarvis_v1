@echo off
chcp 65001
echo ========================================================
echo  Jarvis Dashboard is Starting...
echo ========================================================
echo.
echo [Access Guide]
echo 1. Local (This PC): http://localhost:8501
echo 2. Mobile (LAN):    http://10.217.27.190:8501
echo 3. Remote (VPN):    http://100.101.227.116:8501
echo.
echo Launching browser automatically...
start http://localhost:8501
set PYTHONPATH=%~dp0
python -m streamlit run "%~dp0src\dashboard.py" --server.headless true --server.address 0.0.0.0 --server.port 8501
if %errorlevel% neq 0 (
    echo Error occurred!
    pause
)
pause
