# Security

Security is a core design principle of PeaBox AI Workbench.

## Local Storage

Stored locally:

- Chat history
- Configuration
- Preferences

## Secrets

API keys are stored using:

```text
Windows Credential Manager
```

or platform equivalent.

## SSH Keys

Never commit:

```text
.pem
.key
.ppk
```

to source control.

## Recommended Deployment

### Best

```text
Workbench
  ↓
SSH
  ↓
Remote Ollama
```

### Good

```text
Workbench
  ↓
VPN
  ↓
Ollama
```

### Avoid

```text
Public Internet
   ↓
Unsecured Ollama
```

## Reporting Vulnerabilities

See:

```text
SECURITY.md
```

in repository root.
