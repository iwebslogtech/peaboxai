# Installation Guide

This guide walks you through installing and running PeaBox AI Workbench.

## Prerequisites

- Python 3.11+
- Git
- Internet connection
- Windows, Linux, or macOS

## Clone Repository

```bash
git clone https://github.com/iwebslogtech/peaboxai.git

cd peabox-ai-workbench
```

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch Workbench

```bash
streamlit run app.py
```

Default URL:

```text
http://localhost:8501
```

## First Startup

1. Open Workbench.
2. Configure provider.
3. Discover models.
4. Start chatting.

## Upgrade

```bash
git pull

pip install -r requirements.txt --upgrade
```

## Uninstall

Delete:

```text
.venv
.peabox_streamlit_llm
```

and remove the project folder.
