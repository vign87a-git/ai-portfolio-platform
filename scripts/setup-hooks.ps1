# ==============================================================================
# THETRON DevSecOps: Install Git Hooks (PowerShell)
# Configures core.hooksPath to point to .githooks/
# ==============================================================================

Write-Host "Configuring Git hooks path to .githooks/..." -ForegroundColor Cyan
git config core.hooksPath .githooks

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Git hooks successfully configured to .githooks/!" -ForegroundColor Green
    Write-Host "   - pre-commit: Prevents vign87a-lead from authoring commits" -ForegroundColor Gray
    Write-Host "   - pre-push:   Prevents direct pushes to main & lead branch pushes" -ForegroundColor Gray
} else {
    Write-Host "❌ Failed to configure Git hooks." -ForegroundColor Red
}
