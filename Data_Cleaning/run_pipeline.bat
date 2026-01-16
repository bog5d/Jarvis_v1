@echo off
chcp 65001
echo ==========================================
echo      Jarvis Data Cleaning Pipeline
echo ==========================================

echo [Step 1] Exporting Evernote DB to ENEX...
:: 使用用户指定的数据库路径
set DB_PATH="C:\Users\王波\en_backup.db"
set EXPORT_DIR="D:\My_System\Inbox\Enex_Export"

if not exist %DB_PATH% (
    echo ❌ Error: Database not found at %DB_PATH%
    pause
    exit /b
)

if not exist %EXPORT_DIR% mkdir %EXPORT_DIR%

echo 正在从 %DB_PATH% 导出笔记...
python -m evernote_backup.cli export %EXPORT_DIR% --database %DB_PATH%

echo.
echo [Step 2] Converting ENEX to Markdown (Yarle)...
:: 检查 Yarle 是否安装
call npx -v >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Node.js/npx is not installed.
    pause
    exit /b
)

echo 正在运行 Yarle 转换...
call npx -p yarle-evernote-to-md yarle "D:\My_System\Inbox\Enex_Export" --configFile "D:\My_System\Jarvis_v1\config\yarle_config.json"

echo.
echo [Step 3] Running Three-Stage Rocket Cleaning...
python "D:\My_System\Jarvis_v1\Data_Cleaning\clean_notes.py"

echo.
echo ==========================================
echo      All Done! Go to sleep now. zzz...
echo ==========================================
pause