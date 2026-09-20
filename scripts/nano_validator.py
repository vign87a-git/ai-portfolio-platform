#!/usr/bin/env python3
"""
==============================================================================
THETRON NANO-VALIDATOR: Static DOM, HTML & Resource Integrity Gate
==============================================================================
Performs static AST and regex validation across all HTML templates in public/
and app/templates/ to catch:
- Unbalanced HTML tags
- Duplicate DOM IDs
- Missing local image / link assets
- Undefined onclick handlers
- Broken hash links (#target)
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
print("THETRON NANO-LEVEL STATIC VALIDATOR")
print(f"Repository Root: {REPO_ROOT}")
print("=" * 80)

total_errors = 0
total_warnings = 0

STANDARD_ROUTES = {'overview', 'telemetry', 'playground', 'architecture', 'rag', 'demo', 'projects'}

def validate_html_file(filepath: Path):
    global total_errors, total_warnings
    rel_path = filepath.relative_to(REPO_ROOT)
    print(f"\n[SCAN] Validating: {rel_path}")

    content = filepath.read_text(encoding='utf-8')
    file_errors = []
    file_warnings = []

    # 1. Check all href="#..." targets
    hash_links = re.findall(r'href=[\'"]#([a-zA-Z0-9_-]+)[\'"]', content)
    defined_ids = set(re.findall(r'\bid=[\'"]([^\'"]+)[\'"]', content))
    for hl in hash_links:
        if hl not in defined_ids and hl not in STANDARD_ROUTES:
            file_warnings.append(f"Hash link href='#{hl}' does not match any defined ID or standard route")

    # 2. Check all onclick functions
    onclicks = re.findall(r'onclick=[\'"]([^\'"]+)[\'"]', content)
    for oc in onclicks:
        match = re.match(r'([a-zA-Z0-9_.]+)\(', oc.strip())
        if match:
            fn = match.group(1)
            base_obj = fn.split('.')[0]
            if base_obj not in ['event', 'window', 'document', 'history', 'console', 'navigator']:
                pattern = rf'\b(function\s+{base_obj}|const\s+{base_obj}|let\s+{base_obj}|var\s+{base_obj})\b'
                if not re.search(pattern, content):
                    file_errors.append(f"onclick handler calls undefined object/function: '{fn}' in '{oc}'")

    # 3. Check for broken SVG / img src
    img_srcs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', content)
    for src in img_srcs:
        if not src.startswith(('http://', 'https://', 'data:')):
            local_path = filepath.parent / src
            if not local_path.exists():
                file_errors.append(f"Image src does not exist locally: '{src}'")

    # 4. Check for dead script / link references
    links = re.findall(r'<link[^>]+href=[\'"]([^\'"]+)[\'"]', content)
    for link in links:
        if not link.startswith(('http://', 'https://', 'data:')):
            local_path = filepath.parent / link
            if not local_path.exists():
                file_errors.append(f"Link href does not exist locally: '{link}'")

    # 5. Check for unbalanced HTML tags of major containers
    for tag in ['div', 'section', 'main', 'header', 'footer', 'script', 'style']:
        opens = len(re.findall(rf'<{tag}\b', content, re.IGNORECASE))
        closes = len(re.findall(rf'</{tag}>', content, re.IGNORECASE))
        if opens != closes:
            file_errors.append(f"Unbalanced <{tag}> tags: {opens} opened vs {closes} closed")

    # 6. Check for duplicate IDs in the same file
    all_ids = re.findall(r'\bid=[\'"]([^\'"]+)[\'"]', content)
    seen = set()
    duplicates = set()
    for i in all_ids:
        if i in seen:
            duplicates.add(i)
        seen.add(i)
    if duplicates:
        file_errors.append(f"Duplicate DOM IDs found: {duplicates}")

    if file_errors:
        print(f"  FAILED: {len(file_errors)} error(s)")
        for err in file_errors:
            print(f"    ❌ {err}")
    else:
        print(f"  PASSED: 0 errors (DOM structure & assets valid)")

    if file_warnings:
        print(f"  WARNINGS: {len(file_warnings)} warning(s)")
        for warn in file_warnings:
            print(f"    ⚠️  {warn}")

    total_errors += len(file_errors)
    total_warnings += len(file_warnings)

# Run across all templates in public/ and app/templates/
target_dirs = [REPO_ROOT / 'public', REPO_ROOT / 'app' / 'templates']
for target_dir in target_dirs:
    for html_file in sorted(target_dir.glob('*.html')):
        validate_html_file(html_file)

print("\n" + "=" * 80)
print(f"NANO-VALIDATION SUMMARY: {total_errors} Errors, {total_warnings} Warnings")
print("=" * 80)

if total_errors == 0:
    print(">>> OVERALL VERDICT: ALL TEMPLATES VALID (0 ERRORS) <<<")
    sys.exit(0)
else:
    print(">>> OVERALL VERDICT: VALIDATION FAILED <<<")
    sys.exit(1)
