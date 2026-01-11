@echo off
cd /d "%~dp0"
echo 🔧 AGGRESSIVE REPO FIX...
git config user.name "Jarvis System"
git config user.email "jarvis@localhost"

:: Reset local branch to match remote origin/main (drops bad local commits)
:: This keeps your file changes in the workspace ("Mixed" reset)
git fetch origin
git reset --mixed origin/main

echo 🧹 Enforcing .gitignore...
git rm -r --cached node_modules 2>nul

echo 📦 Staging clean files (Code Only)...
git add .

echo 💾 Committing...
git commit -m "Jarvis System Update: Agents & Scripts"

echo 🚀 Pushing...
git push origin main

echo Done.
pause
