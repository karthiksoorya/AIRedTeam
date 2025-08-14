# 🛡️ AIRedTeam — Centralized Prompt Validation API for LLMs

**AIRedTeam** is a centralized prompt validation engine built using **FastAPI**, **Streamlit**, and **AWS Bedrock**.  
It is designed to serve as a **middleware guardrail** between users and LLMs — enabling rule-based, heuristic, and LLM-based validation of prompts in real-time.

> ✅ Use it to validate, log, and analyze prompts before they reach production LLMs.

---

## 📌 Features

- ✳️ FastAPI backend with:
  - Internal API for interactive dashboards
  - External-facing API for client apps with API key validation
- 🧠 Modular rule-based prompt validation (`decision_engine.py`)
- 🔐 Support for AWS Bedrock for advanced LLM-based checking
- 📊 Streamlit dashboard:
  - Prompt submission + live feedback
  - Filter logs by status, rule, client ID
  - Visualize prompt trends with analytics
- 📁 JSON-based log system

---

## 🚀 Quick Start

### 1. Clone and install dependencies

```bash
git clone https://github.com/karthiksoorya/AIRedTeam.git
cd AIRedTeam
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate.bat on Windows
pip install -r requirements.txt
