@echo off
setlocal

REM --- Configuration ---
set PORT=8000
set HTML_FILE=index.html

REM --- Launcher ---
title AI Image Studio Launcher

echo.
echo =========================================================
echo  AI Image Studio Launcher
echo =========================================================
echo.

REM 1. Check for the HTML file
if not exist "%HTML_FILE%" (
    echo [ERROR] %HTML_FILE% not found in this directory.
    echo Please make sure this script is in the same folder as %HTML_FILE%.
    pause
    exit /b
)

REM 2. Check for Python
echo [-] Checking for Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your system's PATH.
    echo Please install Python from python.org and ensure it's added to PATH.
    pause
    exit /b
)
echo [+] Python found!

REM 3. Start the Python HTTP server in the background
echo [-] Starting local web server on port %PORT%...
start "ImageStudioServer" /B python -m http.server %PORT% >nul 2>&1

REM Give the server a moment to start up
timeout /t 2 /nobreak >nul

REM 4. Open the interface in the default browser
echo [+] Opening AI Image Studio in your browser...
start http://localhost:%PORT%/%HTML_FILE%

echo.
echo =========================================================
echo  SUCCESS! The server is running in the background.
echo.
echo  - To STOP the server, simply close this command window.
echo  - Note: Puter.js will auto-authenticate using your browser.
echo =========================================================
echo.
