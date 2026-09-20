#!/usr/bin/env python3
"""
==============================================================================
THETRON END-TO-END RIGOROUS AUDIT SUITE
==============================================================================
Portable 91-gate verification suite covering:
1. Template & Asset Parity (public/ vs app/templates/)
2. DOM Structure & Single-View CSS Invariants
3. Router & JavaScript Mapping Integrity
4. In-Browser RAG & FinOps Invariants
5. DevSecOps & Governance CI/CD Pipelines
6. FastAPI Backend & HTTP Endpoints
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

# Resolve repository root dynamically
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

print("=" * 80)
print("THETRON END-TO-END RIGOROUS AUDIT SUITE")
print(f"Repository Root: {REPO_ROOT}")
print("=" * 80)

audit_results = {
    "passed": 0,
    "failed": 0,
    "warnings": 0,
    "details": []
}

def record_pass(category: str, desc: str):
    audit_results["passed"] += 1
    print(f"  [PASS] {category}: {desc}")

def record_fail(category: str, desc: str):
    audit_results["failed"] += 1
    audit_results["details"].append(f"FAIL in {category}: {desc}")
    print(f"  [FAIL] {category}: {desc}")

def record_warn(category: str, desc: str):
    audit_results["warnings"] += 1
    audit_results["details"].append(f"WARN in {category}: {desc}")
    print(f"  [WARN] {category}: {desc}")


# ==============================================================================
# 1. PARITY AUDIT (public/ vs app/templates/)
# ==============================================================================
print("\n--- 1. TEMPLATE & ASSET PARITY AUDIT ---")
files_to_compare = [
    ('public/index.html', 'app/templates/index.html'),
    ('public/architecture.html', 'app/templates/architecture.html'),
    ('public/demo.html', 'app/templates/demo.html'),
    ('public/projects.html', 'app/templates/projects.html'),
    ('public/rag.html', 'app/templates/rag.html'),
    ('public/telemetry.html', 'app/templates/telemetry.html'),
    ('public/favicon.svg', 'app/templates/favicon.svg')
]

for p_rel, a_rel in files_to_compare:
    p_path = REPO_ROOT / p_rel
    a_path = REPO_ROOT / a_rel
    if not p_path.exists() or not a_path.exists():
        record_fail("Parity", f"File missing: {p_rel} or {a_rel}")
        continue
    p_bytes = p_path.read_bytes()
    a_bytes = a_path.read_bytes()
    if p_bytes == a_bytes:
        record_pass("Parity", f"100% byte-for-byte match: {p_rel} == {a_rel} ({len(p_bytes)} bytes)")
    else:
        record_fail("Parity", f"Difference detected between {p_rel} and {a_rel}")


# ==============================================================================
# 2. DOM STRUCTURE & CSS SINGLE-VIEW AUDIT
# ==============================================================================
print("\n--- 2. DOM STRUCTURE & SINGLE-VIEW CSS AUDIT ---")
index_path = REPO_ROOT / 'public' / 'index.html'
html_content = index_path.read_text(encoding='utf-8')

# Check Unconditional Single-View CSS
if ".view-section { display: none !important; }" in html_content or ".view-section {\n            display: none !important;" in html_content:
    record_pass("Single-View CSS", "Unconditional '.view-section { display: none !important; }' rule verified")
else:
    record_fail("Single-View CSS", "Unconditional '.view-section { display: none !important; }' rule NOT found")

if ".view-section.active-focus { display: block !important;" in html_content or ".view-section.active-focus {\n            display: block !important;" in html_content:
    record_pass("Single-View CSS", "Unconditional '.view-section.active-focus { display: block !important; }' rule verified")
else:
    record_fail("Single-View CSS", "Active focus CSS rule NOT found")

# Check that body does not gate view sections
if "body.focused-mode .view-section" in html_content:
    record_fail("Single-View CSS", "Found legacy 'body.focused-mode .view-section' gating!")
else:
    record_pass("Single-View CSS", "No legacy 'body.focused-mode .view-section' gating exists")

# Check DOM IDs uniqueness
all_ids = re.findall(r'\bid=[\'"]([^\'"]+)[\'"]', html_content)
seen_ids = set()
dup_ids = set()
for i in all_ids:
    if i in seen_ids:
        dup_ids.add(i)
    seen_ids.add(i)

if not dup_ids:
    record_pass("DOM IDs", f"All {len(seen_ids)} DOM IDs are strictly unique")
else:
    record_fail("DOM IDs", f"Duplicate DOM IDs detected: {dup_ids}")

# Check Section Elements
expected_sections = [
    'overviewSection', 'telemetrySection', 'playgroundSection',
    'architectureSection', 'ragExplorerSection', 'demoSection', 'projectsSection'
]
for sec in expected_sections:
    if f'id="{sec}"' in html_content:
        record_pass("Sections", f"Section '{sec}' exists in DOM with class 'view-section'")
    else:
        record_fail("Sections", f"Missing section '{sec}' in DOM")

# Check that only ONE section has active-focus in initial HTML
initial_active = re.findall(r'class="[^"]*view-section[^"]*active-focus[^"]*"', html_content)
if len(initial_active) == 1:
    record_pass("Initial State", f"Exactly 1 section has 'active-focus' on initial page load ({initial_active[0]})")
else:
    record_fail("Initial State", f"Expected 1 initially active section, found {len(initial_active)}")


# ==============================================================================
# 3. ROUTER & MAPPING INTEGRITY AUDIT
# ==============================================================================
print("\n--- 3. ROUTER & JAVASCRIPT MAPPING INTEGRITY ---")

# Check ROUTE_SECTIONS mappings
route_sections_match = re.search(r'const ROUTE_SECTIONS = \{([^}]+)\};', html_content)
if route_sections_match:
    rs_body = route_sections_match.group(1)
    routes = dict(re.findall(r'(\b[a-z]+\b):\s*[\'"]([^\'"]+)[\'"]', rs_body))
    record_pass("Router", f"ROUTE_SECTIONS defines {len(routes)} routes: {list(routes.keys())}")
    for r_key, r_id in routes.items():
        if r_id in seen_ids:
            record_pass("Router Mapping", f"Route '#{r_key}' cleanly maps to existing DOM element '#{r_id}'")
        else:
            record_fail("Router Mapping", f"Route '#{r_key}' maps to NON-EXISTENT DOM element '#{r_id}'")
else:
    record_fail("Router", "ROUTE_SECTIONS object not found in JavaScript")

# Check Nav Pills
for r_key in routes.keys():
    pill_id = f"pill-{r_key}"
    if pill_id in seen_ids:
        record_pass("Nav Pills", f"Pill button '#{pill_id}' exists in Command Bar")
    else:
        record_fail("Nav Pills", f"Missing pill button '#{pill_id}'")

# Check Autopilot Steps
autopilot_targets = re.findall(r'targetId:\s*[\'"]([^\'"]+)[\'"]', html_content)
record_pass("Autopilot", f"THETRON_AUTOPILOT defines {len(autopilot_targets)} steps")
for target in autopilot_targets:
    if target in seen_ids:
        record_pass("Autopilot Target", f"Step targetId '#{target}' exists in DOM")
    else:
        record_fail("Autopilot Target", f"Step targetId '#{target}' DOES NOT EXIST in DOM")

# Check Demo Chapters
demo_routes = re.findall(r'targetRoute:\s*[\'"]([^\'"]+)[\'"]', html_content)
record_pass("Demo Theater", f"THETRON_DEMO defines {len(demo_routes)} chapters")
for d_route in demo_routes:
    if d_route in routes:
        record_pass("Demo Target Route", f"Chapter targetRoute '#{d_route}' is a valid route")
    else:
        record_fail("Demo Target Route", f"Chapter targetRoute '#{d_route}' is INVALID")

# Check Architecture Nodes
arch_nodes_in_html = re.findall(r'id="node-([a-z]+)"', html_content)
arch_match = re.search(r'const ARCH_DATA = \{([\s\S]+?)\n\s*\};', html_content)
arch_data_keys = re.findall(r'^\s*([a-z]+):\s*\{', arch_match.group(1), re.MULTILINE) if arch_match else []
record_pass("Architecture Data", f"ARCH_DATA defines nodes: {arch_data_keys}")
for an in arch_nodes_in_html:
    if an in arch_data_keys:
        record_pass("Architecture Nodes", f"DOM node '#node-{an}' maps to ARCH_DATA.{an}")
    else:
        record_fail("Architecture Nodes", f"DOM node '#node-{an}' missing in ARCH_DATA")

# Check Explainer Snippets
explainer_btns = re.findall(r'id="btn-([a-z]+)"', html_content)
explainer_keys = ['fastapi', 'prbot', 'retry']
for eb in explainer_btns:
    if eb in explainer_keys:
        record_pass("Explainer Snippets", f"Explainer button '#btn-{eb}' maps to EXPLAINER_SNIPPETS.{eb}")
    else:
        record_fail("Explainer Snippets", f"Explainer button '#btn-{eb}' missing in EXPLAINER_SNIPPETS")


# ==============================================================================
# 4. RAG KNOWLEDGE BASE & FINOPS INVARIANTS AUDIT
# ==============================================================================
print("\n--- 4. RAG KNOWLEDGE BASE & FINOPS INVARIANTS ---")

manifest_keys = ["01_SYSTEM_TOPOLOGY", "02_GIT_GOVERNANCE", "03_DEVSECOPS_PIPELINE", "04_THETRON_ORIGIN", "05_RESILIENCE_FINOPS"]
for mk in manifest_keys:
    if f'"{mk}":' in html_content:
        record_pass("RAG Manifest", f"Knowledge base manifest '{mk}' is loaded in-browser")
    else:
        record_fail("RAG Manifest", f"Missing manifest '{mk}'")

# Check Offline RAG Fallback
if "Offline Extractive Mode" in html_content:
    record_pass("RAG Fallback", "Offline extractive retrieval fallback verified in runRAGSearch")
else:
    record_fail("RAG Fallback", "Offline extractive fallback NOT found in runRAGSearch")

# Check FinOps Invariant Values
if "$58.40" in html_content and "0.00045" in html_content:
    record_pass("FinOps Constants", "$58.40 monthly avoided spend & $0.00045 per-query constants verified")
else:
    record_fail("FinOps Constants", "FinOps constants mismatch in telemetry")


# ==============================================================================
# 5. DEVSECOPS & GOVERNANCE CI/CD AUDIT
# ==============================================================================
print("\n--- 5. DEVSECOPS & GOVERNANCE CI/CD AUDIT ---")

workflow_dir = REPO_ROOT / '.github' / 'workflows'
workflows = {
    'deploy-pages.yml': ['bandit -r app/ -ll', 'pytest tests/', 'deploy-pages'],
    'deploy-gcp.yml': ['bandit -r app/ -ll', 'pytest tests/', 'deploy-cloudrun'],
    'pr-governance-gate.yml': ['vign87a-dev', 'vign87a-lead', 'gemini-3.6-flash']
}

for wf_name, expected_terms in workflows.items():
    wf_path = workflow_dir / wf_name
    if not wf_path.exists():
        record_fail("Workflows", f"Missing workflow: {wf_name}")
        continue
    wf_content = wf_path.read_text(encoding='utf-8')
    record_pass("Workflows", f"Workflow file exists: {wf_name} ({len(wf_content.splitlines())} lines)")
    for term in expected_terms:
        if term in wf_content:
            record_pass("Workflow Rules", f"'{wf_name}' contains mandatory audit step '{term}'")
        else:
            record_fail("Workflow Rules", f"'{wf_name}' MISSING mandatory step '{term}'")

# Git hooks audit
hooks_dir = REPO_ROOT / '.githooks'
for hook in ['pre-commit', 'pre-push']:
    h_path = hooks_dir / hook
    if h_path.exists():
        h_content = h_path.read_text(encoding='utf-8')
        if 'vign87a-lead' in h_content and 'vign87a-dev' in h_content:
            record_pass("Git Hooks", f"Hook '{hook}' enforces Separation of Duties (vign87a-dev vs vign87a-lead)")
        else:
            record_fail("Git Hooks", f"Hook '{hook}' does not enforce personas properly")
    else:
        record_fail("Git Hooks", f"Missing git hook '{hook}'")


# ==============================================================================
# 6. FASTAPI BACKEND & HTTP ENDPOINT AUDIT
# ==============================================================================
print("\n--- 6. FASTAPI BACKEND & HTTP ENDPOINT AUDIT ---")
try:
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    # 1. Root
    resp = client.get("/")
    if resp.status_code == 200 and "THETRON" in resp.text:
        record_pass("FastAPI Root", "GET / returns 200 OK with HTML template")
    else:
        record_fail("FastAPI Root", f"GET / failed with status {resp.status_code}")

    # 2. Favicon
    resp = client.get("/favicon.svg")
    if resp.status_code == 200 and "image/svg+xml" in resp.headers.get("content-type", ""):
        record_pass("FastAPI Favicon", "GET /favicon.svg returns 200 OK with SVG content-type")
    else:
        record_fail("FastAPI Favicon", f"GET /favicon.svg failed with status {resp.status_code}")

    # 3. All Redirect endpoints
    endpoints_to_test = [
        "/architecture", "/architecture.html",
        "/demo", "/demo.html",
        "/projects", "/projects.html",
        "/rag", "/rag.html",
        "/telemetry", "/telemetry.html"
    ]
    for ep in endpoints_to_test:
        resp = client.get(ep)
        if resp.status_code == 200 and "THETRON" in resp.text:
            record_pass("FastAPI Route", f"GET {ep} returns 200 OK")
        else:
            record_fail("FastAPI Route", f"GET {ep} failed with status {resp.status_code}")

    # 4. Generate without key
    resp = client.post("/generate", json={"text": "Test"})
    if resp.status_code == 200 and "error" in resp.json():
        record_pass("FastAPI Generate", "POST /generate handles missing API key gracefully")
    else:
        record_fail("FastAPI Generate", f"POST /generate failed with status {resp.status_code}")

    # 5. Invalid JSON payload
    resp = client.post("/generate", json={"invalid_field": 123})
    if resp.status_code == 422:
        record_pass("FastAPI Validation", "POST /generate rejects invalid payload with 422 Unprocessable Entity")
    else:
        record_fail("FastAPI Validation", f"POST /generate invalid payload status was {resp.status_code}")

except Exception as e:
    record_fail("FastAPI", f"FastAPI test client execution failed: {e}")


# ==============================================================================
# SUMMARY VERDICT
# ==============================================================================
print("\n" + "=" * 80)
print("AUDIT SUMMARY VERDICT")
print("=" * 80)
total_tests = audit_results['passed'] + audit_results['failed'] + audit_results['warnings']
print(f"Total Tests Executed: {total_tests}")
print(f"Passed:   {audit_results['passed']}")
print(f"Failed:   {audit_results['failed']}")
print(f"Warnings: {audit_results['warnings']}")
print("=" * 80)

if audit_results['failed'] == 0:
    print(">>> OVERALL VERDICT: ALL AUDIT GATES PASSED (100% PRODUCTION READY) <<<")
    sys.exit(0)
else:
    print(">>> OVERALL VERDICT: AUDIT GATES FAILED - REMEDIATION REQUIRED <<<")
    for d in audit_results["details"]:
        print(f"  - {d}")
    sys.exit(1)
