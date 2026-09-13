# Troubleshooting

## No Models Found

### Cause

Incorrect provider configuration.

### Fix

Verify:

```text
Provider
URL
API Key
```

and click:

```text
Discover Models
```

---

## Ollama Not Reachable

Verify:

```bash
ollama list
```

and:

```bash
curl http://localhost:11434/api/tags
```

---

## SSH Failure

Verify:

```bash
ssh -i mykey.key opc@HOST
```

works outside Workbench.

---

## OpenAI Authentication Error

Verify:

```text
API Key
```

is correct.

---

## Gemini Authentication Error

Verify:

```text
Google AI Studio API Key
```

has been entered.

---

## Uploaded Files Not Working

Verify file type is supported.

Supported:

```text
PDF
DOCX
XLSX
PPTX
CSV
TXT
```

---

## Chat History Missing

Verify:

```text
.peabox_streamlit_llm
```

was not deleted.

---

## Application Won't Start

Check:

```bash
pip install -r requirements.txt
```

and:

```bash
streamlit run app.py
```

for errors.
