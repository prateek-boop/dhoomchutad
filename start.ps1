# EduEagle - Student Success & Intervention Orchestration Platform
# Startup script for Windows PowerShell

$ErrorActionPreference = "Stop"

# Detect available Python runtime dynamically
$pythonPath = ""
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonPath = (Get-Command python).Source
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonPath = (Get-Command py).Source
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonPath = (Get-Command python3).Source
} elseif (Test-Path "C:\msys64\ucrt64\bin\python.exe") {
    $pythonPath = "C:\msys64\ucrt64\bin\python.exe"
} else {
    Write-Error "Python executable not found. Please ensure Python 3 is installed and added to PATH."
    exit 1
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "       EduEagle: Student Success & Intervention Engine    " -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "Using Python runtime at: $pythonPath" -ForegroundColor DarkGray

# Check database
if (-not (Test-Path "edueagle.db")) {
    Write-Host "Initializing database & seeding realistic university cohort data..." -ForegroundColor Yellow
    & $pythonPath database.py
}

Write-Host "`nLaunching web server on http://localhost:8000 ..." -ForegroundColor Cyan
Write-Host "Press Ctrl+C to terminate the server anytime.`n" -ForegroundColor DarkYellow

& $pythonPath server.py

