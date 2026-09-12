# peaboxai
Open-source AI workspace for cloud models like Ollama, OpenAI, Claude, Gemini, LiteLLM, Open WebUI, OpenRouter and self-hosted local LLMs. Supports chat, files, memory, reasoning controls, parameter controls and multiple providers.

# PeaBox AI Workbench

> **One Workspace. Any AI Model. Your Data. Your Choice.**

PeaBox AI Workbench is an open-source AI workspace that connects local, self-hosted, and cloud AI models through a single interface.

Use Ollama, OpenAI, Claude, Gemini, LiteLLM, Open WebUI, OpenRouter, Groq, and other OpenAI-compatible providers without being locked into a single ecosystem.

---

## 🚀 Why PeaBox AI Workbench?

Most AI applications are tied to a single provider.

PeaBox AI Workbench gives you the freedom to:

✅ Run local AI models

✅ Connect cloud AI services

✅ Switch models instantly

✅ Upload and analyze documents

✅ Maintain persistent chat history

✅ Control where your data goes

✅ Use reasoning/thinking models

✅ Work with private or enterprise knowledge bases

---

# ✨ Features

## Multi-Provider AI Access

Connect:

- Ollama
- OpenAI
- Anthropic Claude
- Google Gemini
- LiteLLM
- Open WebUI
- OpenRouter
- Groq
- Custom OpenAI-compatible APIs

---

## Self-Hosted AI

Run local AI models using:

- Ollama
- LM Studio
- LiteLLM
- Private Infrastructure

Supported models include:

- Qwen
- Gemma
- Llama
- DeepSeek
- Mistral
- Phi

---

## Document Analysis

Upload and analyze:

- PDF
- DOCX
- XLSX
- CSV
- PPTX
- TXT
- JSON

Examples:

- Summarize policies
- Create implementation plans
- Extract action items
- Generate test cases
- Create executive summaries

---

## Chat Memory

Conversation history is stored locally.

The workbench automatically provides previous chat context to the selected model.

---

## Thinking / Reasoning Models

Control model reasoning:

- Default
- Off
- Low
- Medium
- High

Supported where available.

---

## SSH-Based Secure Access

Connect to remote Ollama servers via SSH keys without exposing Ollama publicly.

Architecture:

```text
PeaBox Workbench
        ↓
       SSH
        ↓
    Remote VM
        ↓
     Ollama
```

---

## Direct AI Access

Connect directly to:

```text
http://localhost:11434
```

or

```text
http://server:11434
```

for local and network-based deployments.

---

# 🏗️ Architecture

```text
                     ┌──────────────────┐
                     │ PeaBox AI        │
                     │ Workbench        │
                     └────────┬─────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼

    Local Models        Self-Hosted         Cloud Models
      Ollama             LiteLLM

      Qwen             Open WebUI          OpenAI
      Gemma            Custom APIs         Claude
      Llama                                Gemini
      DeepSeek                             OpenRouter
                                           Groq
```

---

# 🔌 Supported Providers

| Provider | Status |
|----------|---------|
| Ollama | ✅ |
| SSH Ollama | ✅ |
| LiteLLM | ✅ |
| Open WebUI | ✅ |
| OpenAI | ✅ |
| Claude | ✅ |
| Gemini | ✅ |
| OpenRouter | ✅ |
| Groq | ✅ |
| Custom OpenAI APIs | ✅ |

---

# 📦 Installation

## Windows

Clone repository:

```bash
git clone https://github.com/iwebslogtech/peabox-ai-workbench.git
```

Navigate:

```bash
cd peabox-ai-workbench
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

---

# ⚙️ Provider Setup

## Ollama

Install model:

```bash
ollama pull qwen3:8b
```

In Workbench:

```text
Provider → Direct Ollama
URL      → http://localhost:11434
```

---

## SSH Ollama

Configure:

```text
Host
User
Port
Private Key
```

Example:

```text
Host: 192.168.1.50
User: opc
Port: 22
```

Click:

```text
Discover Models
```

---

## OpenAI

```text
Provider → OpenAI
```

Add API key and discover available models.

---

## Claude

```text
Provider → Anthropic
```

Add API key and discover Claude models.

---

## Gemini

```text
Provider → Google Gemini
```

Add Gemini API key and discover available models.

---

# 📸 Screenshots

> Coming Soon

### Dashboard

screenshots/dashboard.png

### Chat

screenshots/chat.png

### Settings

screenshots/settings.png

---

# 🗺️ Roadmap

## Version 1.0

- ✅ Multi-provider support
- ✅ Ollama integration
- ✅ Chat history
- ✅ File uploads
- ✅ Model discovery

---

## Version 2.0

- 🚧 Knowledge Base (RAG)
- 🚧 Vector Search
- 🚧 Document Indexing
- 🚧 Workspaces

---

## Version 3.0

- 📋 Multi-user support
- 📋 Role-based access
- 📋 SharePoint integration
- 📋 Microsoft Teams integration

---

## Version 4.0

- 📋 AI Agents
- 📋 MCP support
- 📋 Workflow Builder
- 📋 Marketplace

---

# 🏢 Enterprise Use Cases

## HR & HRIS

- Policy Assistant
- HR Knowledge Base
- Compensation Assistant
- Oracle HCM Assistant
- Dynamics 365 Assistant

---

## Consulting

- BRD Generator
- User Story Generator
- RAID Log Generator
- Executive Summaries
- Proposal Creation

---

## Project Management

- Risk Analysis
- Status Reporting
- Project Planning
- Meeting Summaries
- Action Tracking

---

# 🤝 Contributing

Contributions are welcome.

Please read:

```text
CONTRIBUTING.md
```

before creating pull requests.

---

# 🔒 Security

For responsible disclosure of security vulnerabilities, please contact:

```text
security@peabox.ai
```

Please do not submit vulnerabilities through public issues.

---

# 📄 License

PeaBox AI Workbench is licensed under the:

```text
Apache License 2.0
```

You may:

- Use
- Modify
- Fork
- Distribute
- Commercially deploy

the software under the terms of the license.

The PeaBox name, logos, and trademarks are not granted under the Apache License.

See:

```text
LICENSE
NOTICE
TRADEMARKS.md
```

for details.

---

# 🌍 Vision

PeaBox AI Workbench exists to give users complete freedom over:

- Where AI runs
- Which models they use
- How their data is processed

**Local when you need privacy. Cloud when you need scale. One workspace for everything.**

---

## ⭐ Support the Project

If you find the project useful:

- Star the repository
- Share it with your network
- Submit feature requests
- Contribute code
- Report issues

Your support helps make AI more open, flexible, and accessible for everyone.
