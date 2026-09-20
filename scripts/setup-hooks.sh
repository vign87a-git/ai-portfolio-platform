#!/usr/bin/env bash
# ==============================================================================
# THETRON DevSecOps: Install Git Hooks (Bash)
# Configures core.hooksPath to point to .githooks/
# ==============================================================================

echo "Configuring Git hooks path to .githooks/..."
chmod +x .githooks/*
git config core.hooksPath .githooks

if [ $? -eq 0 ]; then
    echo "✅ Git hooks successfully configured to .githooks/!"
    echo "   - pre-commit: Prevents vign87a-lead from authoring commits"
    echo "   - pre-push:   Prevents direct pushes to main & lead branch pushes"
else
    echo "❌ Failed to configure Git hooks."
fi
