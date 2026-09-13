# SSH Ollama Guide

SSH Ollama allows secure access to remote models without exposing Ollama publicly.

## Architecture

```text
Workbench
    ↓
SSH
    ↓
Remote VM
    ↓
localhost:11434
```

## Configure SSH

Provider:

```text
SSH Ollama
```

Fill:

```text
Host
User
Port
Private Key Path
```

Example:

```text
Host: 193.xx.xx.xx
User: opc
Port: 22
```

## Test SSH

Run:

```bash
ssh -i mykey.key opc@HOST
```

If login succeeds:

```bash
ollama list
```

should work.

## Security Benefits

- No public Ollama port
- SSH encryption
- Key-based authentication

## Troubleshooting

Permission denied:

```bash
chmod 600 mykey.key
```

SSH timeout:

- Verify firewall rules
- Verify VM availability
