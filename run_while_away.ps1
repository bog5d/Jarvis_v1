$ErrorActionPreference = "Continue"

$ExportScript = "D:\My_System\Jarvis_v1\custom_export.py"
$YarleConfig = "D:\My_System\Jarvis_v1\config\yarle_config.json"

Write-Host ">>> STARTING AUTOMATED MIGRATION SEQUENCE <<<" -ForegroundColor Green

# Step 1: Export
Write-Host "--- Step 1: Exporting from Database (Robust Mode) ---" -ForegroundColor Yellow
python $ExportScript

# Note: Python script handles its own errors and continues, so we proceed even if exit code is non-zero
Write-Host "Export phase finished. Logs above show skipped/failed items." -ForegroundColor Gray

# Step 2: Convert
Write-Host "--- Step 2: Converting to Markdown (Yarle) ---" -ForegroundColor Yellow
Write-Host "Target Configuration: $YarleConfig"

# Using npx with -y to auto-accept install if needed
# Command syntax depends on package version, but usually 'yarle' bin is exposed
cmd /c "npx -y -p yarle-evernote-to-md yarle --configFile `"$YarleConfig`""

Write-Host ">>> SEQUENCE FINISHED. CHECK D:\My_System\01_Drafts\Yarle_Output (or configured output dir) <<<" -ForegroundColor Cyan
Pause
