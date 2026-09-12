from __future__ import annotations
import json
import subprocess
from dataclasses import dataclass, field
import requests
from openai import OpenAI
from anthropic import Anthropic

@dataclass
class ModelInfo:
    id: str
    capabilities: set[str] = field(default_factory=set)
    parameters: dict = field(default_factory=dict)
    details: dict = field(default_factory=dict)

PROVIDER_PRESETS = {
    "SSH Ollama": {"kind": "ssh_ollama"},
    "Direct Ollama": {"kind": "direct_ollama", "base_url": "http://localhost:11434"},
    "LiteLLM": {"kind": "openai_compatible", "base_url": "http://localhost:4000/v1"},
    "Open WebUI": {"kind": "openai_compatible", "base_url": "http://localhost:3000/api"},
    "OpenAI": {"kind": "openai_compatible", "base_url": "https://api.openai.com/v1"},
    "Anthropic": {"kind": "anthropic", "base_url": "https://api.anthropic.com"},
    "Google Gemini": {"kind": "openai_compatible", "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/"},
    "OpenRouter": {"kind": "openai_compatible", "base_url": "https://openrouter.ai/api/v1"},
    "Groq": {"kind": "openai_compatible", "base_url": "https://api.groq.com/openai/v1"},
    "Custom OpenAI-compatible": {"kind": "openai_compatible", "base_url": ""},
}


def _parse_parameters(text):
    result = {}
    for line in (text or "").splitlines():
        parts = line.strip().split(None, 1)
        if len(parts) == 2 and parts[0] not in result:
            result[parts[0]] = parts[1].strip().strip('"')
    return result


def _ssh_base(settings):
    key = settings.get("key_path", "")
    host = settings.get("host", "")
    user = settings.get("user", "opc")
    port = str(settings.get("port", 22))
    if not key or not host:
        raise ValueError("Configure the SSH host and private-key path.")
    return ["ssh", "-i", key, "-p", port, "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", f"{user}@{host}"]


def _ssh_json(settings, endpoint, payload=None, timeout=120):
    remote = f"curl -sS --fail-with-body http://127.0.0.1:11434{endpoint}"
    if payload is not None:
        remote += " -H 'Content-Type: application/json' --data-binary @-"
    proc = subprocess.run(_ssh_base(settings) + [remote], input=json.dumps(payload) if payload is not None else None, capture_output=True, text=True, timeout=timeout)
    if proc.returncode:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "SSH request failed")
    return json.loads(proc.stdout)


def _http_json(base_url, endpoint, payload=None, api_key="", timeout=120):
    url = base_url.rstrip("/") + endpoint
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    response = requests.get(url, headers=headers, timeout=timeout) if payload is None else requests.post(url, headers=headers, json=payload, timeout=timeout)
    response.raise_for_status()
    return response.json()


def discover_models(provider, settings, api_key=""):
    kind = PROVIDER_PRESETS[provider]["kind"]
    if kind in {"ssh_ollama", "direct_ollama"}:
        call = (lambda e, p=None: _ssh_json(settings, e, p)) if kind == "ssh_ollama" else (lambda e, p=None: _http_json(settings["base_url"], e, p, api_key))
        tags = call("/api/tags")
        output = []
        for item in tags.get("models", []):
            name = item.get("name") or item.get("model")
            detail = call("/api/show", {"model": name})
            output.append(ModelInfo(name, set(detail.get("capabilities", [])), _parse_parameters(detail.get("parameters", "")), detail.get("details", {})))
        return output
    if kind == "anthropic":
        client = Anthropic(api_key=api_key)
        return [ModelInfo(x.id, infer_cloud_capabilities(provider, x.id)) for x in client.models.list(limit=100).data]
    client = OpenAI(api_key=api_key or "not-required", base_url=settings["base_url"])
    return [ModelInfo(x.id, infer_cloud_capabilities(provider, x.id)) for x in client.models.list().data]


def infer_cloud_capabilities(provider, model):
    value = model.lower()
    caps = {"chat", "attachments_text"}
    if any(token in value for token in ("gpt-4o", "gpt-5", "claude", "gemini", "vision", "vl")):
        caps.add("vision")
    if any(token in value for token in ("o1", "o3", "o4", "gpt-5", "claude", "gemini-2.5", "gemini-3", "reason", "deepseek-r1")):
        caps.add("thinking")
    return caps


def _ollama_payload(model, messages, images, settings):
    outgoing = [dict(m) for m in messages]
    if images:
        outgoing[-1]["images"] = [x["base64"] for x in images]
    payload = {"model": model, "messages": outgoing, "stream": False}
    reasoning = settings.get("reasoning", "Default")
    if reasoning != "Default":
        payload["think"] = False if reasoning == "Off" else reasoning.lower() if reasoning in {"Low", "Medium", "High", "Max"} else True
    if not settings.get("use_defaults", True):
        payload["options"] = {
            "temperature": settings["temperature"], "top_p": settings["top_p"], "top_k": settings["top_k"],
            "repeat_penalty": settings["repeat_penalty"], "num_ctx": settings["num_ctx"]
        }
    return payload


def chat(provider, model, messages, images, settings, api_key=""):
    kind = PROVIDER_PRESETS[provider]["kind"]
    if kind in {"ssh_ollama", "direct_ollama"}:
        payload = _ollama_payload(model, messages, images, settings)
        data = _ssh_json(settings, "/api/chat", payload, 1800) if kind == "ssh_ollama" else _http_json(settings["base_url"], "/api/chat", payload, api_key, 1800)
        msg = data.get("message", {})
        return msg.get("content", ""), msg.get("thinking", "")
    if kind == "anthropic":
        converted = []
        for m in messages:
            if m["role"] == "system":
                continue
            converted.append({"role": m["role"], "content": m["content"]})
        if images:
            converted[-1]["content"] = [{"type": "text", "text": messages[-1]["content"]}] + [
                {"type": "image", "source": {"type": "base64", "media_type": image["media_type"], "data": image["base64"]}} for image in images
            ]
        kwargs = {"model": model, "messages": converted, "max_tokens": settings.get("max_tokens", 4096)}
        if not settings.get("use_defaults", True):
            kwargs.update({"temperature": settings["temperature"], "top_p": settings["top_p"]})
        response = Anthropic(api_key=api_key).messages.create(**kwargs)
        return "\n".join(block.text for block in response.content if getattr(block, "type", "") == "text"), ""
    converted = [dict(m) for m in messages]
    if images:
        converted[-1]["content"] = [{"type": "text", "text": messages[-1]["content"]}] + [
            {"type": "image_url", "image_url": {"url": f"data:{image['media_type']};base64,{image['base64']}"}} for image in images
        ]
    kwargs = {"model": model, "messages": converted}
    if not settings.get("use_defaults", True):
        kwargs.update({"temperature": settings["temperature"], "top_p": settings["top_p"], "max_tokens": settings.get("max_tokens", 4096)})
    reasoning = settings.get("reasoning", "Default")
    if reasoning in {"Low", "Medium", "High"}:
        kwargs["reasoning_effort"] = reasoning.lower()
    response = OpenAI(api_key=api_key or "not-required", base_url=settings["base_url"]).chat.completions.create(**kwargs)
    return response.choices[0].message.content or "", ""
