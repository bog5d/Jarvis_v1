@echo off
echo ==========================================
echo      JARVIS DATA MIGRATION PROTOCOL
echo ==========================================
echo.
echo [Step 1] Running Robust Export (Python)...
python "C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\custom_export.py"

echo.
echo [Step 2] Running Yarle Conversion...
echo Note: This step requires Node.js installed.
cd /d "C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1"
call npx -y yarle-evernote-to-md --configFile "C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\config\yarle_config.json"

echo.
echo ==========================================
echo          ALL TASKS COMPLETED
echo ==========================================
pause
