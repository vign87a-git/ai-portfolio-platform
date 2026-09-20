# ==============================================================================
# THETRON Local Quality & Governance Gate (PowerShell)
# ==============================================================================
# Executes all quality, security, naming, and end-to-end audit checks locally.
# Fails immediately if any check fails, preventing regressions.
# ==============================================================================

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir

Write-Host "`n=======================================================" -ForegroundColor Cyan
Write-Host "THETRON UNIFIED LOCAL QUALITY GATE" -ForegroundColor Cyan
Write-Host "Repository Root: $RepoRoot" -ForegroundColor Gray
Write-Host "=======================================================`n" -ForegroundColor Cyan

# Detect Python executable (prefer local venv if present)
$PythonExe = "python"
if (Test-Path "$RepoRoot\venv\Scripts\python.exe") {
    $PythonExe = "$RepoRoot\venv\Scripts\python.exe"
}

# 1. Pytest Unit Tests
Write-Host ">>> [1/5] Running Pytest Unit Test Suite using $PythonExe..." -ForegroundColor Yellow
& $PythonExe -m pytest "$RepoRoot\tests\" -v
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ [FAIL] Pytest unit tests failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ [PASS] Pytest unit tests passed.`n" -ForegroundColor Green

# 2. Bandit AST Security Scan
Write-Host ">>> [2/5] Running Bandit AST Security Scan (High/Medium severity)..." -ForegroundColor Yellow
& $PythonExe -m bandit -r "$RepoRoot\app" -ll
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ [FAIL] Bandit security vulnerabilities detected!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ [PASS] Bandit security scan passed (0 vulnerabilities).`n" -ForegroundColor Green

# 3. Nano-Level DOM & Template Validator
Write-Host ">>> [3/5] Running Nano-Level DOM & Template Validator..." -ForegroundColor Yellow
& $PythonExe "$RepoRoot\scripts\nano_validator.py"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ [FAIL] Nano-level template validation failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ [PASS] Nano-level validation passed.`n" -ForegroundColor Green

# 4. Naming Standards & Jargon Audit
Write-Host ">>> [4/5] Running Naming Standards & Terminology Auditor..." -ForegroundColor Yellow
& $PythonExe "$RepoRoot\scripts\audit_naming_standards.py"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ [FAIL] Naming standards audit failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ [PASS] Naming standards audit passed.`n" -ForegroundColor Green

# 5. 91-Gate End-to-End Audit Suite
Write-Host ">>> [5/5] Running 91-Gate End-to-End Platform Audit..." -ForegroundColor Yellow
& $PythonExe "$RepoRoot\scripts\e2e_audit.py"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ [FAIL] End-to-end audit suite failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ [PASS] 91-gate audit suite passed.`n" -ForegroundColor Green

Write-Host "=======================================================" -ForegroundColor Green
Write-Host "🎉 ALL QUALITY & GOVERNANCE GATES PASSED (100% READY)" -ForegroundColor Green
Write-Host "=======================================================`n" -ForegroundColor Green
exit 0
