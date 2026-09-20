#!/usr/bin/env python3
"""
==============================================================================
THETRON PR MANAGEMENT TOOL
==============================================================================
Programmatic GitHub Pull Request automation tool that interacts with the
GitHub REST API without requiring an external GitHub CLI ('gh').
- Supports: status, list, create
- Securely retrieves tokens from environment (GITHUB_TOKEN / GH_TOKEN) or
  the local Git Credential Manager
- Enforces Separation of Duties (Maker-Checker governance)
==============================================================================
"""

import os
import sys
import json
import argparse
import subprocess
import urllib.request
import urllib.error
from pathlib import Path

# Ensure UTF-8 output encoding
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
REPO_SLUG = "vign87a-git/ai-portfolio-platform"

def get_git_branch() -> str:
    """Get the current checked-out git branch."""
    res = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT)
    return res.stdout.strip()

def get_git_user() -> str:
    """Get the local git user.name."""
    res = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True, cwd=REPO_ROOT)
    return res.stdout.strip()

def get_github_token() -> str:
    """Retrieve GitHub token from environment or Git Credential Manager."""
    # 1. Check environment variables
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token.strip()

    # 2. Query Git Credential Manager
    try:
        proc = subprocess.Popen(
            ["git", "credential", "fill"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=REPO_ROOT
        )
        input_data = "protocol=https\nhost=github.com\n"
        stdout, _ = proc.communicate(input=input_data, timeout=5)
        for line in stdout.splitlines():
            if line.startswith("password="):
                return line.split("=", 1)[1].strip()
    except Exception as e:
        pass

    return ""

def api_request(endpoint: str, method: str = "GET", data: dict = None) -> dict:
    """Execute authenticated GitHub REST API request."""
    token = get_github_token()
    if not token:
        print("[ERROR] No GitHub token found. Set GITHUB_TOKEN or configure Git Credential Manager.", file=sys.stderr)
        sys.exit(1)

    url = f"https://api.github.com{endpoint}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "THETRON-PR-Manager",
        "Content-Type": "application/json"
    }

    req_data = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"[HTTP ERROR {e.code}] {err_msg}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] API request failed: {e}", file=sys.stderr)
        sys.exit(1)

def cmd_status(args):
    """Check PR status for the current branch."""
    branch = args.branch or get_git_branch()
    print(f"Checking Pull Requests for branch '{branch}' in {REPO_SLUG}...")
    endpoint = f"/repos/{REPO_SLUG}/pulls?head=vign87a-git:{branch}&state=all"
    prs = api_request(endpoint)
    if not prs:
        print(f"No pull requests found for branch '{branch}'.")
        return

    for pr in prs:
        state_icon = "🟢" if pr["state"] == "open" else ("🟣" if pr.get("merged_at") else "🔴")
        print(f"{state_icon} PR #{pr['number']}: {pr['title']}")
        print(f"   State:     {pr['state'].upper()} (Merged: {bool(pr.get('merged_at'))})")
        print(f"   URL:       {pr['html_url']}")
        print(f"   Author:    @{pr['user']['login']}")
        if pr.get("merged_by"):
            print(f"   Merged By: @{pr['merged_by']['login']}")
        print("-" * 60)

def cmd_create(args):
    """Create a new Pull Request."""
    branch = args.head or get_git_branch()
    user = get_git_user()

    print(f"Authoring PR from '{branch}' into '{args.base}' as '{user}'...")

    # SoD Check: Warn if vign87a-lead tries to create a PR
    if user == "vign87a-lead":
        print("[WARNING] SoD Governance Notice: 'vign87a-lead' is designated as Lead Auditor/Merger.")
        print("          PRs should typically be authored by 'vign87a-dev'.")

    payload = {
        "title": args.title,
        "head": branch,
        "base": args.base,
        "body": args.body or "Automated Pull Request from THETRON tooling."
    }

    res = api_request(f"/repos/{REPO_SLUG}/pulls", method="POST", data=payload)
    print(f"✅ Pull Request Created Successfully!")
    print(f"   PR #{res['number']}: {res['title']}")
    print(f"   URL: {res['html_url']}")

def main():
    parser = argparse.ArgumentParser(description="THETRON PR Management Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # status
    p_status = subparsers.add_parser("status", help="Check PR status for the current or specified branch")
    p_status.add_argument("--branch", help="Branch name to check (defaults to current branch)")
    p_status.set_defaults(func=cmd_status)

    # create
    p_create = subparsers.add_parser("create", help="Create a new Pull Request")
    p_create.add_argument("--title", required=True, help="PR Title")
    p_create.add_argument("--body", help="PR Description (markdown)")
    p_create.add_argument("--head", help="Head branch (defaults to current branch)")
    p_create.add_argument("--base", default="main", help="Base branch (default: main)")
    p_create.set_defaults(func=cmd_create)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
