# AgentZERO / OpenZero AIOS

<div align="center">
  <img src="https://github.com/ResearchForumOnline/AgentZERO/raw/main/Screenshot_21.png" width="800" alt="OpenZero control panel screenshot">
</div>

<p align="center">
  <a href="https://openzero.talktoai.org/">OpenZero AIOS</a> |
  <a href="https://talktoai.org/">TalkToAI</a> |
  <a href="https://research.talktoai.org/">Research</a> |
  <a href="https://github.com/ResearchForumOnline/ZEROtalktoai">Project Hub</a>
</p>

<p align="center">
  <img alt="Local AI" src="https://img.shields.io/badge/focus-local%20AI-111827">
  <img alt="Server agents" src="https://img.shields.io/badge/focus-server%20agents-0ea5e9">
  <img alt="Security boundary" src="https://img.shields.io/badge/security-reviewed%20public%20docs-16a34a">
</p>

AgentZERO is the public OpenZero AIOS repository for local AI agent work, server-based assistant workflows, vector memory experiments, browser/terminal automation research, and ZeroMint-style AI workstations.

It is designed as a practical AI systems project: run locally where possible, keep sensitive data under owner control, document the deployment path clearly, and separate public demos from private server operations.

## What This Repository Covers

- OpenZero AIOS public project material.
- AgentZERO local/server deployment notes.
- Vector memory and retrieval experiments.
- Browser and terminal automation research.
- ZeroMint AIOS screenshots, release notes, and public install direction.
- Links into TalkToAI, ZERO, ZeroThink, and ZSEC.

## Public Links

| Area | Link |
| --- | --- |
| OpenZero AIOS | https://openzero.talktoai.org/ |
| TalkToAI | https://talktoai.org/ |
| ZeroThink | https://zerothink.talktoai.org/ |
| Research | https://research.talktoai.org/ |
| ZSEC Auto Updates | https://github.com/ResearchForumOnline/ZSEC |
| Public project hub | https://github.com/ResearchForumOnline/ZEROtalktoai |

## Quick Install

For existing Linux machines, review the installer before running it:

```bash
curl -fsSL https://openzero.talktoai.org/install.sh -o openzero-install.sh
less openzero-install.sh
bash openzero-install.sh
```

For unattended testing on a machine you control:

```bash
curl -fsSL https://openzero.talktoai.org/install.sh | bash
```

Use a clean test machine or VM first. Keep API keys, SSH keys, model paths, and server credentials in local environment files that are never committed to GitHub.

## Recommended Environment

A practical OpenZero workstation or VPS should have:

- Linux Mint, Ubuntu, Debian, or a compatible server Linux.
- 16 GB RAM minimum for lighter local AI work; more RAM for larger local models.
- 30 GB disk minimum for the application stack; more for local model files.
- SSH access protected by keys, firewall rules, and lockout-safe admin access.
- Optional XRDP or desktop access for visual workflows.

## Running On A Remote Desktop Server

For a graphical AI workstation, install XRDP only on a server you control and protect it with firewall rules. Do not expose default credentials or weak passwords to the public internet.

Example setup:

```bash
sudo apt update
sudo apt install xrdp -y
sudo systemctl enable xrdp
sudo systemctl start xrdp
sudo ufw allow 3389/tcp
sudo ufw reload
```

For stronger hardening, restrict RDP to your home IP, use SSH tunnelling, or place the desktop behind a VPN.

## Process Management

OpenZero deployments commonly use PM2 for long-running services:

```bash
pm2 status
pm2 restart all
pm2 logs
```

Keep service names and local paths documented on the server, but do not publish secrets or production-only notes in this repository.

## Screenshots

<div align="center">
  <img src="https://github.com/ResearchForumOnline/AgentZERO/raw/main/Screenshot_18.png" width="400" alt="OpenZero interface screenshot 1">
  <img src="https://github.com/ResearchForumOnline/AgentZERO/raw/main/Screenshot_20.png" width="400" alt="OpenZero interface screenshot 2">
  <img src="https://github.com/ResearchForumOnline/AgentZERO/raw/main/Screenshot_22.png" width="400" alt="OpenZero interface screenshot 3">
  <img src="https://github.com/ResearchForumOnline/AgentZERO/raw/main/Screenshot_23.png" width="400" alt="OpenZero interface screenshot 4">
  <img src="https://github.com/ResearchForumOnline/AgentZERO/raw/main/Screenshot_6.png" width="804" alt="OpenZero terminal logs">
</div>

## Security Notes

AgentZERO can connect to local files, model runtimes, browsers, and terminals depending on configuration. Treat it as a powerful local/server automation project, not a toy chatbot.

Important rules:

- Do not publish default passwords, SSH private keys, API keys, or live server credentials.
- Change any initial ISO, VM, or test credentials before network exposure.
- Keep RDP, SSH, panel ports, and model APIs restricted to trusted IPs where possible.
- Use ZSEC Auto Updates for security-only update automation and hardening direction.
- Review scripts before running them on production servers.

## Development Direction

Next public improvements should focus on:

1. A clearer demo path for new users.
2. Safer local model setup guidance.
3. Screenshots or short videos showing working OpenZero flows.
4. ZSEC-linked server hardening notes.
5. Separation between public docs and private deployment operations.

## Repository Boundary

This repository can include public source, screenshots, docs, demos, and release notes. It must not include private server notes, customer data, SSH keys, API tokens, unpublished production code, or secrets.

## Related Projects

- ZERO: https://github.com/ResearchForumOnline/ZERO
- ZT: https://github.com/ResearchForumOnline/ZT
- ZSEC Auto Updates: https://github.com/ResearchForumOnline/ZSEC
- FreeWebPanel: https://github.com/ResearchForumOnline/FreeWebPanel
