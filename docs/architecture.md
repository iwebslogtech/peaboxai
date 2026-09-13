# Architecture

PeaBox AI Workbench separates the user interface from AI providers.

## High-Level Architecture

```text
            PeaBox AI Workbench
                     │
     ┌───────────────┼────────────────┐
     │               │                │

 Local Models    Self Hosted      Cloud Models
    Ollama         LiteLLM

    Qwen         Open WebUI       OpenAI
    Gemma        Custom APIs      Claude
    Llama                         Gemini
```

## Core Components

### Streamlit UI

Responsible for:

- Chat UI
- File uploads
- History
- Provider configuration

### Provider Layer

Responsible for:

- Model discovery
- API communication
- Authentication
- Reasoning controls

### Storage Layer

Stores:

- Chat history
- Preferences
- Workspace settings

### Attachments Layer

Processes:

- PDFs
- Office documents
- Images
- Text files

before sending content to models.

## Design Principles

- Provider agnostic
- Local-first
- Open source
- Extensible
- Privacy aware
