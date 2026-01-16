@echo off
echo Stopping any existing Streamlit instances...
taskkill /F /IM streamlit.exe >nul 2>&1
taskkill /F /FI "WINDOWTITLE eq Jarvis Dashboard" >nul 2>&1

echo Configuring Firewall...
netsh advfirewall firewall delete rule name="Jarvis Mobile" >nul 2>&1
netsh advfirewall firewall add rule name="Jarvis Mobile" dir=in action=allow protocol=TCP localport=8501 profile=any

echo Starting Jarvis Dashboard...
title Jarvis Dashboard
"C:/Users/王波/AppData/Local/Microsoft/WindowsApps/python3.13.exe" -m streamlit run "C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\src\dashboard.py" --server.address=0.0.0.0 --server.port=8501
pause