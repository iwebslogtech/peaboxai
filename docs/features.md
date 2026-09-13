# Features

PeaBox AI Workbench provides a unified workspace for working with local, self-hosted, and cloud AI models from a single interface.

---

## Multi-Provider AI Access

Connect to multiple AI providers without switching applications.

Supported providers include:

- Ollama
- SSH Ollama
- Direct Ollama
- LiteLLM
- Open WebUI
- OpenAI
- Anthropic Claude
- Google Gemini
- OpenRouter
- Groq
- Custom OpenAI-Compatible APIs

### Benefits

✅ Avoid vendor lock-in

✅ Compare models side-by-side

✅ Use the best model for each task

✅ Switch providers in seconds

---

## Self-Hosted AI

Run AI models on your own infrastructure.

Examples:

- Qwen
- Llama
- Gemma
- DeepSeek
- Mistral
- Phi

### Deployment Options

- Local machine
- Home server
- NAS
- Private cloud
- Oracle Cloud
- AWS
- Azure
- On-premises infrastructure

### Benefits

✅ Full data ownership

✅ Enhanced privacy

✅ Offline capability

✅ No per-message costs

---

## SSH Ollama Integration

Securely connect to remote Ollama instances without exposing model APIs to the internet.

### Architecture

```text
PeaBox
   ↓
 SSH
   ↓
 Remote VM
   ↓
 Ollama
```

### Benefits

✅ No public Ollama endpoint required

✅ SSH key authentication

✅ Encrypted communication

✅ Enterprise-friendly architecture

---

## Direct Ollama Support

Connect directly to:

```text
localhost
LAN servers
VPN servers
Private gateways
```

Examples:

```text
http://localhost:11434

http://192.168.1.20:11434

https://ollama.company.com
```

### Benefits

✅ Simple setup

✅ Fast local access

✅ Automatic model discovery

---

## Automatic Model Discovery

Workbench automatically discovers available models.

Examples:

```text
qwen3:8b
qwen2.5:1.5b
gemma3
llama
deepseek
```

### Retrieved Information

- Model name
- Parameter size
- Quantization level
- Context size
- Capabilities
- Default parameters

### Benefits

✅ No manual model configuration

✅ Easier onboarding

✅ Reduced setup errors

---

## Capability Detection

Workbench automatically determines model capabilities.

Detected capabilities may include:

```text
Chat
Reasoning
Vision
Function Calling
Tools
```

### Benefits

✅ Dynamic UI behavior

✅ Only relevant options are displayed

✅ Less user confusion

---

## Chat History

Conversations are stored locally.

History survives:

- Restarts
- Upgrades
- System reboots

### Benefits

✅ Long-term context

✅ Easier research

✅ Better productivity

---

## Conversation Memory

Previous messages are automatically supplied to the model.

### Examples

```text
Summarize the discussion.
```

```text
Expand the second recommendation.
```

```text
Create an action plan from what we discussed.
```

### Benefits

✅ Natural conversations

✅ Reduced repetition

✅ Better context retention

---

## Document Analysis

Upload business documents and ask questions.

Supported formats:

- PDF
- DOCX
- XLSX
- CSV
- PPTX
- TXT
- JSON
- XML

### Example Use Cases

- Policy review
- Project planning
- Requirements analysis
- Business analysis
- Audit preparation
- Process documentation

---

## Image Analysis

Supported formats:

- PNG
- JPG
- JPEG
- WEBP

Available for vision-capable models.

### Example Use Cases

- Screenshots
- UI reviews
- Report images
- Diagrams
- Charts

---

## Thinking and Reasoning Controls

Supported reasoning models can expose configurable reasoning levels.

Options:

```text
Default
Off
Low
Medium
High
```

### Benefits

✅ Faster responses when needed

✅ Deeper analysis when required

✅ Better control over model behavior

---

## Model Parameters

Use model defaults or customize generation settings.

Supported controls:

- Temperature
- Top P
- Top K
- Repeat Penalty
- Context Window
- Max Output Tokens

### Benefits

✅ Fine-tuned responses

✅ Better control for advanced users

✅ Optimization for specific workloads

---

## Workspace-Oriented Design

Organize work by project.

Example workspaces:

```text
HR Transformation

D365 Implementation

Oracle HCM

Project Management

Consulting

Investments
```

### Benefits

✅ Better organization

✅ Cleaner conversations

✅ Easier document management

---

## OpenAI Compatible APIs

Connect any provider supporting the OpenAI API standard.

Examples:

- OpenAI
- LiteLLM
- OpenRouter
- Groq
- Custom Gateways

### Benefits

✅ Future-proof architecture

✅ Simplified integration

✅ Broad ecosystem compatibility

---

## Enterprise Readiness

Built with enterprise adoption in mind.

Features supporting enterprise use:

- Self-hosting
- SSH integration
- Local AI models
- Flexible provider architecture
- Open-source transparency

### Future Enhancements

Planned:

- SSO
- Role-Based Access
- Team Workspaces
- Audit Logs
- SharePoint Integration
- Microsoft Teams Integration

---

## Open Source

PeaBox AI Workbench is released under:

```text
Apache License 2.0
```

Users can:

✅ Use

✅ Modify

✅ Fork

✅ Self-host

✅ Commercially deploy

subject to license terms.

---

## Key Benefits Summary

### For Individuals

- One AI workspace
- Multiple providers
- Private local models
- Lower AI costs

### For Consultants

- Project analysis
- Requirements review
- Faster documentation
- Better client support

### For Enterprises

- Data control
- Flexible deployment
- Vendor independence
- AI platform standardization

---

## Vision

PeaBox AI Workbench is designed to become the universal workspace for interacting with artificial intelligence, regardless of where models run or who provides them.

**One Workspace. Any AI Model. Your Data. Your Choice.**
