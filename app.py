from __future__ import annotations
import keyring
import streamlit as st
from attachments import build_user_content
from providers import PROVIDER_PRESETS, ModelInfo, chat, discover_models
from storage import add_message, delete_conversation, init_db, list_conversations, load_config, load_messages, new_conversation, save_config, update_conversation

st.set_page_config(page_title="PeaBox AI Workbench", page_icon="🟣", layout="wide")
init_db()

if "config" not in st.session_state:
    st.session_state.config = load_config()
if "conversation_id" not in st.session_state:
    conversations = list_conversations()
    st.session_state.conversation_id = conversations[0]["id"] if conversations else new_conversation()
if "models" not in st.session_state:
    st.session_state.models = {}


def provider_key(provider):
    return keyring.get_password("PeaBoxStreamlitLLM", provider) or ""


def save_provider_key(provider, value):
    if value:
        keyring.set_password("PeaBoxStreamlitLLM", provider, value)


def current_messages():
    return load_messages(st.session_state.conversation_id)


with st.sidebar:
    st.title("PeaBox AI")
    if st.button("＋ New chat", use_container_width=True):
        st.session_state.conversation_id = new_conversation()
        st.rerun()
    st.subheader("Conversations")
    conversations = list_conversations()
    labels = {f"{c['title']}  ·  {c['id']}": c["id"] for c in conversations}
    current_label = next((k for k, v in labels.items() if v == st.session_state.conversation_id), None)
    selected = st.selectbox("Open chat", list(labels), index=list(labels).index(current_label) if current_label in labels else 0, label_visibility="collapsed") if labels else None
    if selected and labels[selected] != st.session_state.conversation_id:
        st.session_state.conversation_id = labels[selected]
        st.rerun()
    if st.button("Delete current chat", use_container_width=True):
        delete_conversation(st.session_state.conversation_id)
        remaining = list_conversations()
        st.session_state.conversation_id = remaining[0]["id"] if remaining else new_conversation()
        st.rerun()

    st.divider()
    provider = st.selectbox("Provider", list(PROVIDER_PRESETS), key="provider")
    preset = PROVIDER_PRESETS[provider]
    provider_cfg = st.session_state.config.setdefault("providers", {}).setdefault(provider, {})

    with st.expander("Connection settings", expanded=not bool(provider_cfg)):
        if provider == "SSH Ollama":
            provider_cfg["host"] = st.text_input("VM host / IP", provider_cfg.get("host", ""))
            provider_cfg["user"] = st.text_input("SSH user", provider_cfg.get("user", "opc"))
            provider_cfg["port"] = st.number_input("SSH port", 1, 65535, int(provider_cfg.get("port", 22)))
            provider_cfg["key_path"] = st.text_input("Private-key path", provider_cfg.get("key_path", ""), help=r"Example: C:\Keys\oracle.key")
        else:
            default_url = preset.get("base_url", "")
            provider_cfg["base_url"] = st.text_input("Base URL", provider_cfg.get("base_url", default_url))
            if provider not in {"Direct Ollama"}:
                new_key = st.text_input("API key", type="password", placeholder="Stored in Windows Credential Manager")
                if new_key:
                    save_provider_key(provider, new_key)
        if st.button("Save connection", use_container_width=True):
            save_config(st.session_state.config)
            st.success("Connection saved")

    if st.button("Discover models", type="primary", use_container_width=True):
        try:
            with st.spinner("Discovering models..."):
                discovered = discover_models(provider, provider_cfg, provider_key(provider))
            st.session_state.models[provider] = {m.id: m for m in discovered}
            st.success(f"Found {len(discovered)} models")
        except Exception as exc:
            st.error(str(exc))

    model_map = st.session_state.models.get(provider, {})
    model_name = st.selectbox("Model", list(model_map), disabled=not bool(model_map)) if model_map else ""
    model_info = model_map.get(model_name, ModelInfo(model_name))
    capabilities = model_info.capabilities
    if model_name:
        details = model_info.details
        st.caption("Capabilities: " + (", ".join(sorted(capabilities)) or "not reported"))
        if details:
            st.caption(f"Size: {details.get('parameter_size', '?')} · Quantization: {details.get('quantization_level', '?')}")

    st.subheader("Generation")
    use_defaults = st.toggle("Use model defaults", value=True)
    reasoning_options = ["Default", "Off", "Low", "Medium", "High", "Max"] if "thinking" in capabilities else ["Default"]
    reasoning = st.selectbox("Reasoning / thinking", reasoning_options, disabled=len(reasoning_options) == 1)
    with st.expander("Advanced parameters", expanded=not use_defaults):
        defaults = model_info.parameters
        temperature = st.slider("Temperature", 0.0, 2.0, float(defaults.get("temperature", 0.6)), 0.05, disabled=use_defaults)
        top_p = st.slider("Top P", 0.0, 1.0, float(defaults.get("top_p", 0.95)), 0.01, disabled=use_defaults)
        top_k = st.number_input("Top K", 0, 500, int(float(defaults.get("top_k", 20))), disabled=use_defaults)
        repeat_penalty = st.number_input("Repeat penalty", 0.0, 2.0, float(defaults.get("repeat_penalty", 1.0)), 0.05, disabled=use_defaults)
        num_ctx = st.number_input("Context tokens", 1024, 262144, int(float(defaults.get("num_ctx", 8192))), 1024, disabled=use_defaults)
        max_tokens = st.number_input("Maximum output tokens", 256, 32768, 4096, 256, disabled=use_defaults)

    uploaded = st.file_uploader("Attachments", accept_multiple_files=True, type=["txt","md","csv","json","xml","html","py","ps1","js","ts","yaml","yml","log","pdf","docx","xlsx","xlsm","pptx","png","jpg","jpeg","webp"])
    st.caption("Documents are extracted locally. Images require a model detected as vision-capable.")

st.title("PeaBox AI Workbench")
st.caption("Self-hosted Ollama over SSH or direct URL, plus OpenAI-compatible and Anthropic cloud providers.")

messages = current_messages()
for item in messages:
    with st.chat_message(item["role"]):
        st.markdown(item["content"])
        if item.get("thinking"):
            with st.expander("Thinking trace"):
                st.text(item["thinking"])

prompt = st.chat_input("Ask a question or analyze uploaded files", disabled=not bool(model_name))
if prompt:
    try:
        supports_vision = "vision" in capabilities
        combined, images = build_user_content(prompt, uploaded, supports_vision)
        prior = [{"role": m["role"], "content": m["content"]} for m in messages]
        outgoing = prior + [{"role": "user", "content": combined}]
        settings = dict(provider_cfg)
        settings.update({
            "use_defaults": use_defaults, "reasoning": reasoning, "temperature": temperature,
            "top_p": top_p, "top_k": int(top_k), "repeat_penalty": repeat_penalty,
            "num_ctx": int(num_ctx), "max_tokens": int(max_tokens)
        })
        add_message(st.session_state.conversation_id, "user", prompt)
        if len(messages) == 0:
            update_conversation(st.session_state.conversation_id, title=prompt[:60].replace("\n", " "), provider=provider, model=model_name)
        with st.chat_message("assistant"):
            with st.spinner(f"Running {model_name}..."):
                answer, thinking = chat(provider, model_name, outgoing, images, settings, provider_key(provider))
            st.markdown(answer)
            if thinking:
                with st.expander("Thinking trace"):
                    st.text(thinking)
        add_message(st.session_state.conversation_id, "assistant", answer, thinking)
        st.rerun()
    except Exception as exc:
        st.error(f"Request failed: {exc}")

with st.expander("Privacy and operating notes"):
    st.markdown("""
- SSH Ollama keeps port 11434 private and sends requests through the SSH tunnel-like command path.
- Direct Ollama, LiteLLM, Open WebUI, and custom endpoints must be reachable from this computer.
- Cloud-provider prompts and attachments leave your computer and may incur charges.
- Conversation history is stored locally in SQLite and resent with every new turn for context.
- Start a new chat when changing topics because long histories consume context and cloud tokens.
""")
