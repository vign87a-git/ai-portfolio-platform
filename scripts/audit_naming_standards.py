#!/usr/bin/env python3
"""
==============================================================================
THETRON NAMING STANDARDS & TERMINOLOGY AUDITOR
==============================================================================
Enforces strict platform naming conventions and eliminates internal
development jargon:
- Prohibits deprecated 'Option C' / 'Option A' / 'Option B' jargon
- Verifies canonical module titles across index.html & templates
- Verifies 'Serverless Edge Decoupling' architecture naming
==============================================================================
"""

import os
import re
import sys
from pathlib import Path

# Ensure UTF-8 output encoding
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent

print("=" * 80)
print("THETRON NAMING STANDARDS & TERMINOLOGY AUDITOR")
print(f"Repository Root: {REPO_ROOT}")
print("=" * 80)

violations = []

# 1. Prohibited Jargon Scan
FORBIDDEN_PATTERNS = [
    (r'\bOption\s+C\b', "Forbidden internal jargon 'Option C' found"),
    (r'\bOption\s+A\b', "Forbidden internal jargon 'Option A' found"),
    (r'\bOption\s+B\b', "Forbidden internal jargon 'Option B' found")
]

SCAN_EXTENSIONS = {'.html', '.py', '.md', '.yml', '.yaml'}
SCAN_DIRS = ['public', 'app', '.github', 'scripts']

print("\n--- 1. SCANNING FOR DEPRECATED INTERNAL JARGON ---")
for scan_dir in SCAN_DIRS:
    dir_path = REPO_ROOT / scan_dir
    if not dir_path.exists():
        continue
    for fpath in dir_path.rglob('*'):
        if fpath.is_file() and fpath.suffix in SCAN_EXTENSIONS:
            rel_path = fpath.relative_to(REPO_ROOT)
            content = fpath.read_text(encoding='utf-8', errors='ignore')
            for line_no, line in enumerate(content.splitlines(), 1):
                for pattern, msg in FORBIDDEN_PATTERNS:
                    if re.search(pattern, line, re.IGNORECASE):
                        # Filter out git commit history messages or comments in audit scripts
                        if "scripts/audit_naming_standards.py" in str(rel_path).replace('\\', '/'):
                            continue
                        violation = f"{rel_path}:{line_no}: {msg} -> '{line.strip()}'"
                        violations.append(violation)
                        print(f"  ❌ {violation}")

if not any("Option" in v for v in violations):
    print("  [PASS] 0 deprecated 'Option A/B/C' references found across codebase")

# 2. Canonical Module Titles Audit
print("\n--- 2. VERIFYING CANONICAL MODULE TITLES IN INDEX.HTML ---")
CANONICAL_MODULE_PATTERNS = [
    (r'Overview', "Executive Overview & Platform Directory"),
    (r'Telemetry\s+(&amp;|&)\s+FinOps\s+HUD', "Telemetry & FinOps HUD"),
    (r'AI\s+Defense\s+Playground', "AI Defense Playground"),
    (r'Architecture\s+Visualizer', "Architecture Visualizer"),
    (r'In-Browser\s+RAG\s+Explorer', "In-Browser RAG Explorer"),
    (r'How-To\s+(&amp;|&)\s+Demo\s+Theater', "How-To & Demo Theater"),
    (r'(Core\s+Technical\s+Competencies|Featured\s+Enterprise\s+Projects)', "Enterprise Projects & Competencies")
]

index_path = REPO_ROOT / 'public' / 'index.html'
index_content = index_path.read_text(encoding='utf-8')

for pattern, mod_name in CANONICAL_MODULE_PATTERNS:
    if re.search(pattern, index_content, re.IGNORECASE):
        print(f"  [PASS] Canonical module present: '{mod_name}'")
    else:
        v = f"Missing canonical module in public/index.html: '{mod_name}' (pattern: {pattern})"
        violations.append(v)
        print(f"  ❌ {v}")

# 3. Standard Architecture Naming
print("\n--- 3. VERIFYING ARCHITECTURE LABELS ---")
if "Serverless Edge Decoupling" in index_content:
    print("  [PASS] Canonical label 'Serverless Edge Decoupling' verified in Architecture Visualizer")
else:
    v = "Missing canonical label 'Serverless Edge Decoupling' in public/index.html"
    violations.append(v)
    print(f"  ❌ {v}")

print("\n" + "=" * 80)
print("NAMING STANDARDS SUMMARY")
print("=" * 80)
print(f"Total Violations: {len(violations)}")

if len(violations) == 0:
    print(">>> OVERALL VERDICT: ALL NAMING STANDARDS ENFORCED (100% CLEAN) <<<")
    sys.exit(0)
else:
    print(">>> OVERALL VERDICT: NAMING STANDARDS AUDIT FAILED <<<")
    for v in violations:
        print(f"  - {v}")
    sys.exit(1)
