@echo off
cd /d "C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1"

:: 1. 启动主引擎 (后台静默模式)
start pythonw main.py

:: 2. 启动悬浮挂件 (后台静默模式)
start pythonw src/hud_widget.py

exit

