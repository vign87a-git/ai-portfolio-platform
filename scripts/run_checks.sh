#!/usr/bin/env bash
# ==============================================================================
# THETRON Local Quality & Governance Gate (Bash)
# ==============================================================================
# Executes all quality, security, naming, and end-to-end audit checks locally.
# Fails immediately if any check fails, preventing regressions.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo ""
echo "======================================================="
echo "THETRON UNIFIED LOCAL QUALITY GATE (BASH)"
echo "Repository Root: $REPO_ROOT"
echo "======================================================="
echo ""

# Detect Python executable (prefer local venv if present)
PYTHON_EXE="python3"
if [ -f "$REPO_ROOT/venv/bin/python" ]; then
    PYTHON_EXE="$REPO_ROOT/venv/bin/python"
elif [ -f "$REPO_ROOT/venv/Scripts/python.exe" ]; then
    PYTHON_EXE="$REPO_ROOT/venv/Scripts/python.exe"
fi

# 1. Pytest Unit Tests
echo ">>> [1/5] Running Pytest Unit Test Suite using $PYTHON_EXE..."
$PYTHON_EXE -m pytest "$REPO_ROOT/tests/" -v
echo "✅ [PASS] Pytest unit tests passed."
echo ""

# 2. Bandit AST Security Scan
echo ">>> [2/5] Running Bandit AST Security Scan (High/Medium severity)..."
$PYTHON_EXE -m bandit -r "$REPO_ROOT/app" -ll
echo "✅ [PASS] Bandit security scan passed (0 vulnerabilities)."
echo ""

# 3. Nano-Level DOM & Template Validator
echo ">>> [3/5] Running Nano-Level DOM & Template Validator..."
$PYTHON_EXE "$REPO_ROOT/scripts/nano_validator.py"
echo "✅ [PASS] Nano-level validation passed."
echo ""

# 4. Naming Standards & Jargon Audit
echo ">>> [4/5] Running Naming Standards & Terminology Auditor..."
$PYTHON_EXE "$REPO_ROOT/scripts/audit_naming_standards.py"
echo "✅ [PASS] Naming standards audit passed."
echo ""

# 5. 91-Gate End-to-End Audit Suite
echo ">>> [5/5] Running 91-Gate End-to-End Platform Audit..."
$PYTHON_EXE "$REPO_ROOT/scripts/e2e_audit.py"
echo "✅ [PASS] 91-gate audit suite passed."
echo ""

echo "======================================================="
echo "🎉 ALL QUALITY & GOVERNANCE GATES PASSED (100% READY)"
echo "======================================================="
echo ""
exit 0
