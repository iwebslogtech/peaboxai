# Security Policy

## Supported Versions

Security updates are provided for the latest stable release.

| Version | Supported |
|---|---|
| Latest stable release | Yes |
| Earlier releases | Best effort |
| Development branches | No guarantee |

## Reporting a Vulnerability

Please do not report security vulnerabilities through public GitHub issues.

Report vulnerabilities privately through GitHub's private vulnerability reporting feature.

Include:

- A description of the vulnerability
- Steps to reproduce it
- The affected version
- The potential impact
- A suggested remediation, if available

## Secret Handling

PeaBox AI Workbench is designed to store supported API credentials through the operating system's credential manager.

Users must not:

- Commit API keys
- Commit SSH private keys
- Commit `.env` files
- Expose Ollama publicly without protection
- Store production credentials in source code

## Responsible Disclosure

Please allow reasonable time for investigation and remediation before publicly disclosing a vulnerability.
