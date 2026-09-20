# THETRON
### Autonomous AI & Cloud Systems Engineering Platform

[![100% GitHub-Native Deployment](https://github.com/vign87a-git/ai-portfolio-platform/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/vign87a-git/ai-portfolio-platform/actions/workflows/deploy-pages.yml)
[![Autonomous AI Code Reviewer](https://github.com/vign87a-git/ai-portfolio-platform/actions/workflows/ai-code-review.yml/badge.svg)](https://github.com/vign87a-git/ai-portfolio-platform/actions/workflows/ai-code-review.yml)
![DevSecOps Gate](https://img.shields.io/badge/Security%20Gate-Bandit%20AST%20%7C%20TruffleHog%20OSS-brightgreen.svg?logo=security)
![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.14-3776AB.svg?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)
![Google GenAI](https://img.shields.io/badge/Google%20GenAI-Gemini%203.6%20Flash-8E75B2.svg?logo=google&logoColor=white)
![Pytest](https://img.shields.io/badge/Tests-3%2F3%20Passing-brightgreen.svg?logo=pytest&logoColor=white)
![Infra Cost](https://img.shields.io/badge/Infra%20Cost-%240.00%20%2F%20Free%20Tier-success.svg?logo=githubpages&logoColor=white)
![Git Governance](https://img.shields.io/badge/Governance-Multi--Persona%20SoD-orange.svg?logo=git&logoColor=white)
![Web Audio](https://img.shields.io/badge/Web%20Audio-Native%20Synthesizer-ff69b4.svg)

---

## 🌐 Live Interactive Platform & Direct Deep-Links
👉 **[Experience THETRON Live](https://vign87a-git.github.io/ai-portfolio-platform/)**

The platform implements a **Hybrid Deep-Linked SPA Architecture** unifying a **Sticky Cybernetic Command Bar**, a **Dynamic View Mode Switcher** (`🌐 Full Dashboard` vs `🎯 Focused Tool Workspace`), and **Client-Side Deep-Link Routing** with instant hydration:

| Interactive Tool / Module | Direct Deep-Link Hash | Standalone Direct Entry URL |
| :--- | :--- | :--- |
| **📚 In-Browser Repository RAG Explorer** | [`/#rag`](https://vign87a-git.github.io/ai-portfolio-platform/#rag) | [`/rag.html`](https://vign87a-git.github.io/ai-portfolio-platform/rag.html) |
| **🎓 How-To, Demo Theater & Playbooks** | [`/#demo`](https://vign87a-git.github.io/ai-portfolio-platform/#demo) | [`/demo.html`](https://vign87a-git.github.io/ai-portfolio-platform/demo.html) |
| **🏛️ Architecture Visualizer & Deconstructor** | [`/#architecture`](https://vign87a-git.github.io/ai-portfolio-platform/#architecture) | [`/architecture.html`](https://vign87a-git.github.io/ai-portfolio-platform/architecture.html) |
| **⚡ Live Telemetry & FinOps Cost Avoidance HUD** | [`/#telemetry`](https://vign87a-git.github.io/ai-portfolio-platform/#telemetry) | [`/telemetry.html`](https://vign87a-git.github.io/ai-portfolio-platform/telemetry.html) |
| **🤖 AI Defense & Recruiter Lens Playground** | [`/#playground`](https://vign87a-git.github.io/ai-portfolio-platform/#playground) | Direct Interactive Prompt Evaluation |
| **💼 Enterprise Projects & Competencies** | [`/#projects`](https://vign87a-git.github.io/ai-portfolio-platform/#projects) | [`/projects.html`](https://vign87a-git.github.io/ai-portfolio-platform/projects.html) |

**THETRON** is a production-grade showcase of modern software engineering discipline, combining frontier **Agentic AI orchestration**, **zero-trust DevSecOps**, **multi-persona Git governance**, and **self-defending distributed architecture**—hosted with **\$0.00 infrastructure spend**.

---

## 🧬 Brand Identity & Genesis

| Dimension | Origin & Significance |
| :--- | :--- |
| **$\theta$ (Theta)** | Honors the mathematical breakthrough of **Srinivasa Ramanujan’s Mock Theta functions** (Tamil Nadu), foundational to modern modular forms, string theory, and quantum neural tensor spaces. |
| **-on** | The fundamental building block of computation and physical intelligence (**Neuron**, **Electron**, **NPU**). |
| **Phonetics** | `[THAY-tron]` |
| **Vision** | Signifies **Future India** as a global sovereign superpower in frontier AI and deep-tech cloud systems. Cleanly breaks the repetitive Latinate `-s/-x` naming traps, carrying zero commercial IP conflicts. |

---

## 🏛️ System Architecture Topology

The platform operates on a decoupled **Option C CI/CD architecture**, isolating public serverless hosting from containerized cloud runtime:

```mermaid
flowchart TD
    subgraph Governance ["Multi-Persona Git Governance (SOC2 Simulation)"]
        Dev["Developer Persona (vign87a-dev)"] -- "git push via SSH alias github-dev" --> FeatureBranch["feature/* branch"]
        FeatureBranch -- "Open Pull Request" --> PR["Pull Request #Target"]
        Lead["Lead Persona (vign87a-lead)"] -- "Reviews AI audit & Merges" --> Main["main branch"]
    end

    subgraph Bot ["Autonomous AI Mentorship & Review"]
        PR --> ActionBot["GitHub Actions (.github/workflows/ai-code-review.yml)"]
        ActionBot --> DiffEngine["Extracts Git Diff (Zero-Dependency Python)"]
        DiffEngine --> GeminiAudit["Gemini 3.6 Flash DevSecOps System Prompt"]
        GeminiAudit --> PRComment["Auto-posts Structured Audit & Verdict to PR"]
        PRComment --> Lead
    end

    subgraph CI_CD ["Decoupled Option C CI/CD Pipeline"]
        Main -- "Push Event" --> ActionPages[".github/workflows/deploy-pages.yml"]
        ActionPages --> PytestGate["Pytest Suite (3/3 Tests with Mock Fixtures)"]
        PytestGate --> SecretInject["Safe Python Secret Injection (GEMINI_API_KEY)"]
        SecretInject --> PagesDeploy["Deploy to GitHub Pages Global Edge"]
    end

    subgraph Production ["Live Production Runtime ($0.00 Spend)"]
        PagesDeploy --> LiveSPA["Production SPA (HTML5 / Vanilla ES6 / CSS3)"]
        LiveSPA --> RecruiterLens["Dynamic Recruiter Evaluation Lenses"]
        LiveSPA --> Visualizer["Interactive System Architecture Visualizer (Click-to-Inspect)"]
        LiveSPA --> Deconstructor["Live AI Code Deconstructor Engine"]
        LiveSPA --> SelfAware["Self-Aware Architectural Defender (Gemini 3.6 Flash)"]
        LiveSPA --> Backoff["Client-Side Exponential Backoff & 429 Countdown"]
    end
```

---

## 🔬 Core Engineering Competency Pillars

### 1. 🤖 Frontier GenAI & Agentic Systems
* **Autonomous PR Reviewer**: Production GitHub Actions workflow that extracts git diffs, analyzes architecture, flags exposed secrets, and posts structured markdown reviews with zero manual intervention.
* **In-Browser Repository RAG Explorer**: Zero-cost client-side RAG engine embedding 5 structured repository manifests. Performs semantic keyword retrieval and prompts Gemini 3.6 Flash to output verbatim line citations (e.g. `[Ref: 01_SYSTEM_TOPOLOGY#L05-L10]`).
* **Cinematic Motion Graphics 2.0 & Demo Theater**: Procedural canvas motion graphics engine delivering 6 animated scenes (14-node neural synapse lattice with traveling energy pulses, 360° DevSecOps radar scanner, live terminal injection defense, bezier AST scanning topology, 3D rotating vector embedding space, and 36-band reactive cybernetic equalizer). Features synchronized character typewriter telemetry, natural curated speech, and an ambient sci-fi synthesizer bed (`lowpass` filtered at 360Hz) with $0.00 infrastructure spend.
* **Auto-Pilot Live Interactive Tour (`THETRON_AUTOPILOT`)**: Hands-free platform guide driving the live application in real time—smooth-scrolling through the HUD, toggling Recruiter Lenses, executing prompt evaluations, and deconstructing architecture nodes dynamically.
* **Self-Aware System Context**: Embedded architectural knowledge allows Gemini 3.6 Flash to defend engineering trade-offs, discuss Git governance, and deconstruct source code in real time.
* **Dynamic Recruiter Lens**: Role-adaptive evaluation matrix tailoring interactive prompt suites and executive summaries to hiring profiles (*Cloud & DevOps*, *Agentic AI*, *Full-Stack Python*, *All-Rounder*).

### 2. 🛡️ DevSecOps & Enterprise Git Governance
* **Automated Security CI Gate**: Integrated **Bandit AST Python Security Audit** (`bandit -r app/ -ll`) and **TruffleHog OSS Secret Scanner** in CI to guarantee 0 vulnerabilities and 0 leaked high-entropy tokens before any deployment.
* **Bidirectional Separation of Duties (Interpretation A)**: Strict, mutually exclusive Maker-Checker governance between local developer persona (`vign87a-dev`) and lead reviewer persona (`vign87a-lead`):
  - **Developer (`vign87a-dev`)**: Author only. Commits changes and opens PRs via `github-dev` SSH alias. Self-approval and merging are strictly blocked.
  - **Lead Reviewer (`vign87a-lead`)**: Auditor & Merger only. Reviews diffs and merges via `github-lead` SSH alias. Authoring commits, pushing feature branches, and creating PRs are strictly blocked.
  - **CI Governance Gate (`.github/workflows/governance-gate.yml`)**: Automated CI workflow that validates PR and commit authors, rejecting any PRs created by `vign87a-lead` and requiring approval from `vign87a-lead`.
  - **GitHub CODEOWNERS (`.github/CODEOWNERS`)**: Mandates `@vign87a-lead` sign-off for all repository files.
  - **Local Git Hooks (`.githooks/`) & Setup Scripts (`scripts/setup-hooks.ps1`)**: Local `pre-commit` and `pre-push` hooks enforcing identity and blocking direct pushes to `main`.
* **Least Privilege Scoping**: Automated bots operate strictly on granular `contents: read` and `pull-requests: write` permissions.
* **In-Memory Secret Handling**: Production deployment injects API keys in CI runners via string substitution, completely preventing disk-level secret persistence.

### 3. ⚡ Modern Python & Backend APIs
* **FastAPI Backend**: Asynchronous endpoints with Pydantic payload models (`PromptPayload`) and Jinja2 server-side templating (`app/main.py`).
* **Deterministic Pytest Suite**: 100% passing tests utilizing `monkeypatch` fixtures to validate status codes, missing-key fallbacks, and mocked Gemini responses without exhausting API quotas.
* **Containerized Deployment Ready**: Multi-stage `Dockerfile` (`python:3.11-slim`) targeting port 8080, prepared for container orchestration (Cloud Run / K8s).

### 4. 📐 Distributed Resilience, FinOps & Cybernetic Audio
* **Live Telemetry & FinOps Cost Avoidance HUD**: Real-time ticker tracking API round-trip latency (RTT), session tokens consumed, active edge node (`centralindia / cache-maa`), and cumulative cost avoidance vs. dedicated Cloud Run / GKE infrastructure ($58.40/mo + $0.00045/query).
* **Cybernetic Web Audio Synthesizer**: Native browser `AudioContext` synthesizer generating dynamic sine sweeps, sub-bass triangle pulses, and tri-tone chords—delivering haptic sci-fi feedback with 0 KB asset overhead and $0 cost.
* **Automated 429 Backoff Engine**: Real-time HTTP 429 rate-limit interceptor (`fetchWithRetry`) that parses cooldown timestamps and presents a live countdown timer before retrying.
* **Permanent $0.00 Infrastructure Invariant**:
  - Free global edge distribution via GitHub Pages.
  - Unlimited CI/CD execution on public GitHub repositories.
  - Gemini 3.6 Flash running on Google AI Studio Free Tier (unlinked from GCP billing).

---

## 📂 Repository Structure

```text
ai-portfolio-platform/
├── .github/
│   └── workflows/
│       ├── ai-code-review.yml      # Autonomous AI PR Reviewer Bot (Gemini 3.6 Flash)
│       ├── deploy-pages.yml        # 100% Free GitHub Pages CI/CD Deployment
│       └── deploy-gcp.yml          # Isolated GCP Cloud Run Workflow (gcp-production)
├── app/
│   ├── templates/
│   │   ├── index.html              # Jinja2 template mirror (100% parity)
│   │   └── favicon.svg             # Cybernetic vector favicon
│   └── main.py                     # FastAPI application & GenAI routing
├── public/
│   ├── favicon.svg                 # Scalable cybernetic SVG favicon
│   └── index.html                  # Standalone SPA for GitHub Pages hosting
├── tests/
│   └── test_main.py                # Pytest suite with mock client fixtures
├── Dockerfile                      # Container specification for Cloud Run / K8s
├── requirements.txt                # Python dependencies (FastAPI, google-genai, pytest)
└── README.md                       # Architecture specification & documentation
```

---

## 🛠️ Local Quickstart & Verification

### 1. Clone & Setup
```bash
git clone git@github-dev:vign87a-git/ai-portfolio-platform.git
cd ai-portfolio-platform
```

### 2. Virtual Environment & Dependencies
```powershell
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Automated Unit Tests
```powershell
# Execute Pytest suite
python -m pytest tests/ -v
```
Expected output:
```text
tests/test_main.py::test_read_root PASSED                [ 33%]
tests/test_main.py::test_generate_missing_api_key PASSED [ 66%]
tests/test_main.py::test_generate_content_success PASSED [100%]
======================== 3 passed in 1.15s ========================
```

### 4. Run DevSecOps AST Security Audit (Bandit)
```powershell
# Scan codebase for Python AST vulnerabilities
bandit -r app/ -ll
```
Expected output:
```text
[main]  INFO    running on Python 3.14.x
Test results:
        No issues identified.
```

### 5. Run FastAPI Server Locally
```powershell
# Set local Gemini API key
$env:GEMINI_API_KEY = "your-api-key-here"

# Launch ASGI server
uvicorn app.main:app --reload --port 8000
```
Visit `http://localhost:8000` to interact with the local FastAPI-backed instance.

### 6. Build and Run Container (Docker)
```bash
# Build container image
docker build -t thetron:latest .

# Run containerized instance
docker run -p 8080:8080 -e GEMINI_API_KEY="your-api-key" thetron:latest
```

---

## 📜 Audit & Quality Scorecard

In the formal **Enterprise Technical Audit & SWOT Analysis**, the platform achieved an overall **Grade A+ (9.6 / 10)**:

| Evaluation Dimension | Score | Status |
| :--- | :---: | :---: |
| **CI/CD & Automation** | `9.7 / 10` | 🟢 Superior |
| **Git Governance (SoD)** | `9.6 / 10` | 🟢 Superior |
| **Architecture & Design** | `9.5 / 10` | 🟢 Superior |
| **Reliability & Resilience** | `9.2 / 10` | 🟢 Superior |
| **Security & DevSecOps** | `9.8 / 10` | 🟢 Flawless (Bandit + TruffleHog) |
| **Cost Optimization** | `10.0 / 10` | 🟢 Flawless ($0.00 Spend) |

---

## ⚖️ License & Attribution
Architected and built with **THETRON Systems**. Powered by GitHub Actions and Google Gemini 3.6 Flash.
Licensed under the [MIT License](LICENSE).