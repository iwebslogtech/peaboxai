# Providers

PeaBox AI Workbench supports local, self-hosted, and cloud AI providers through a unified interface.

The goal is simple:

> Use any AI model from a single workspace without vendor lock-in.

---

# Provider Categories

PeaBox supports three provider categories:

## Local Models

Models running on your own machine.

Examples:

- Ollama
- LM Studio
- Local OpenAI-compatible APIs

### Benefits

✅ Maximum privacy

✅ No cloud dependency

✅ No per-message costs

✅ Works offline

---

## Self-Hosted Models

Models running on company infrastructure or private cloud environments.

Examples:

- Ollama on AWS
- Ollama on Azure
- Ollama on Oracle Cloud
- LiteLLM Gateway
- Open WebUI

### Benefits

✅ Full control

✅ Enterprise-friendly

✅ Data sovereignty

✅ Custom deployment models

---

## Cloud AI Providers

Models hosted by third-party providers.

Examples:

- OpenAI
- Anthropic Claude
- Google Gemini
- OpenRouter
- Groq

### Benefits

✅ Large model selection

✅ No infrastructure required

✅ Easy onboarding

✅ Scalable

---

# Ollama

Ollama enables local and self-hosted execution of open-source language models.

## Supported Models

Examples:

- Qwen
- Gemma
- Llama
- DeepSeek
- Phi
- Mistral

---

## Connection Modes

### Direct Ollama

```text
Provider → Direct Ollama
```

Example URL:

```text
http://localhost:11434
```

or

```text
http://192.168.1.20:11434
```

---

### SSH Ollama

```text
Provider → SSH Ollama
```

Configuration:

```text
Host
User
Port
Private Key
```

Example:

```text
Host: 193.xx.xx.xx
User: opc
Port: 22
```

---

## Features

✅ Model Discovery

✅ Document Analysis

✅ Chat Memory

✅ Thinking Controls

✅ Vision Models (when available)

✅ Self Hosting

---

# LiteLLM

LiteLLM provides a unified gateway for multiple AI providers.

## Example Architecture

```text
PeaBox
   ↓
LiteLLM
   ↓
OpenAI
Claude
Gemini
Bedrock
Azure OpenAI
```

---

## Configuration

Provider:

```text
LiteLLM
```

Base URL:

```text
http://server:4000/v1
```

API Key:

```text
Optional depending on deployment
```

---

## Benefits

✅ Single endpoint

✅ Multi-model routing

✅ Cost management

✅ Enterprise friendly

✅ Provider abstraction

---

# Open WebUI

Open WebUI can act as a model gateway.

## Connection

Provider:

```text
Open WebUI
```

Base URL:

```text
http://server:3000/api
```

---

## Benefits

✅ Existing Open WebUI users

✅ Shared model catalog

✅ Works with Ollama

✅ Integration flexibility

---

# OpenAI

OpenAI provides hosted commercial language models.

## Configuration

Provider:

```text
OpenAI
```

Required:

```text
OpenAI API Key
```

---

## Example Models

- GPT-5
- GPT-5 Mini

---

## Best For

✅ Coding

✅ Analysis

✅ Structured Outputs

✅ General Productivity

---

# Anthropic Claude

Anthropic provides Claude family models.

## Configuration

Provider:

```text
Anthropic
```

Required:

```text
Anthropic API Key
```

---

## Example Models

- Claude Sonnet
- Claude Opus

---

## Best For

✅ Writing

✅ Research

✅ Summarization

✅ Long Documents

✅ Enterprise Use Cases

---

# Google Gemini

Google's Gemini family of models.

## Configuration

Provider:

```text
Google Gemini
```

Required:

```text
Gemini API Key
```

---

## Example Models

- Gemini Flash
- Gemini Pro

---

## Best For

✅ Fast Responses

✅ Large Context Windows

✅ Document Analysis

✅ Multimodal Use Cases

---

# OpenRouter

OpenRouter provides unified access to many model providers.

## Configuration

Provider:

```text
OpenRouter
```

Required:

```text
OpenRouter API Key
```

---

## Example Models

Examples may include:

- Claude
- Gemini
- DeepSeek
- Qwen
- Mistral
- Llama

---

## Benefits

✅ Large model catalog

✅ Single API key

✅ Easy experimentation

✅ Provider flexibility

---

# Groq

Groq provides ultra-fast inference for supported open models.

## Configuration

Provider:

```text
Groq
```

Required:

```text
Groq API Key
```

---

## Example Models

- Llama
- Gemma
- Qwen

---

## Best For

✅ Low latency

✅ Rapid prototyping

✅ Quick chat applications

✅ Lightweight workloads

---

# Custom OpenAI-Compatible APIs

PeaBox supports custom providers implementing the OpenAI API standard.

## Configuration

Provider:

```text
Custom OpenAI-Compatible
```

Required:

```text
Base URL
API Key (optional)
```

---

## Examples

- Internal company gateways
- Private AI infrastructure
- Custom LiteLLM deployments
- API management platforms

---

# Model Discovery

Supported providers automatically discover models whenever possible.

Click:

```text
Discover Models
```

PeaBox retrieves:

- Available models
- Capabilities
- Parameter information
- Context limits
- Metadata

---

# Reasoning Support

Some providers support advanced reasoning controls.

Options may include:

```text
Default
Off
Low
Medium
High
```

Availability depends on the selected model.

---

# Vision Support

Vision-capable models can analyze:

- PNG
- JPG
- JPEG
- WEBP

Examples:

```text
Screenshots
Charts
Diagrams
Photos
Reports
```

Vision support depends on the provider and model.

---

# Choosing the Right Provider

## Maximum Privacy

Choose:

```text
SSH Ollama
Direct Ollama
```

Best for:

- Private documents
- Enterprise environments
- Sensitive information

---

## Lowest Cost

Choose:

```text
Ollama
Groq
```

Best for:

- Personal projects
- Learning
- Experiments

---

## Highest Flexibility

Choose:

```text
OpenRouter
LiteLLM
```

Best for:

- Model comparisons
- Multi-provider strategies
- Rapid experimentation

---

## Enterprise Adoption

Choose:

```text
LiteLLM
SSH Ollama
OpenAI
Claude
Gemini
```

Best for:

- Corporate environments
- Governance
- Scalability
- Managed deployments

---

# Provider Comparison

| Provider | Self Hosted | Cloud | Model Discovery | Vision | Reasoning |
|-----------|------------|--------|----------------|---------|-----------|
| Ollama | ✅ | ❌ | ✅ | ✅* | ✅* |
| SSH Ollama | ✅ | ❌ | ✅ | ✅* | ✅* |
| LiteLLM | ✅ | ✅ | ✅ | Depends | Depends |
| Open WebUI | ✅ | ✅ | ✅ | Depends | Depends |
| OpenAI | ❌ | ✅ | ✅ | ✅ | ✅ |
| Claude
