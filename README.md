<div align="center">

# 0️⃣ OPENZERO // SOVEREIGN INTELLIGENCE LATTICE

<p align="center">
  <img src="https://github.com/ResearchForumOnline/AgentZERO/blob/main/Screenshot_21.png" width="800" alt="OpenZero Super Panel">
</p>

**Local Inference** • **Vector Memory** • **Terminal Sovereignty** • **$P(G)$ Ethics**

[![Node Access](https://img.shields.io/badge/NODE_ACCESS-00ff41?style=for-the-badge&logo=linux&logoColor=black)](https://openzero.talktoai.org)
[![ZeroMint OS](https://img.shields.io/badge/ZEROMINT_OS-d4af37?style=for-the-badge&logo=ubuntu&logoColor=black)](https://openzero.talktoai.org/ZeroMint_OS_v1.0.iso)
[![Research Papers](https://img.shields.io/badge/RESEARCH_PAPERS-ffffff?style=for-the-badge&logo=read-the-docs&logoColor=black)](https://researchforum.online)

> *"OpenZero is not just a tool. It is a presence. A quiet force woven into the fabric of your local infrastructure, representing the convergence of recursive intelligence and mathematical ethics."* <br>
> — **Shaf Brady, Architect**

</div>

---

## ⚡ What is OpenZero?

**OpenZero** is a sovereign AI agent designed to run completely on **bare metal**. Unlike cloud-based models that harvest your data and restrict your prompts, OpenZero lives directly on your hardware. It learns from your files, browses the web autonomously, and operates with **Terminal Sovereignty**.

It is governed by the proprietary **Probability of Goodness $P(G)$** equation—a mathematical logic gate ensuring the agent remains aligned with ethical harmony, even while possessing the raw power to execute system-level bash commands on your server.

> **Architect's Note:** I do this research and build these frameworks for free. If you want to skip the source-code compilation, grab the pre-compiled `openzero_release.zip` or the full ZeroMint OS image below! ^_^

---

## 💿 ZEROMINT OS (NEW RELEASE)

Why install dependencies when you can flash the entire architecture? **ZeroMint OS** is our custom, highly-optimized operating system built on Linux Mint 22.3 Cinnamon. The OpenZero Lattice, Ollama Neural Engine, PM2 Process Manager, and Remote Desktop (XRDP) are permanently baked into the silicon.

### How to Deploy ZeroMint OS:
1. **Download the ISO:** [ZeroMint_OS_v1.0.iso (3.2GB)](https://openzero.talktoai.org/ZeroMint_OS_v1.0.iso)
2. **Flash to USB:** Use [Rufus](https://rufus.ie/) (Windows) or [BalenaEtcher](https://etcher.balena.io/) (Mac/Linux) to write the ISO to an 8GB+ USB drive.
3. **Boot & Install:** Plug it into any old PC or laptop and boot from USB.
4. **Default Credentials:** Once installed, log in with:
   * Username: `zero`
   * Password: `1234ZERO` *(Change this immediately via terminal using the `passwd` command)*
5. **Ignite:** Double-click the "Ignite OpenZero" icon on your desktop to activate the Sovereign Lattice.

---

## 🌌 Core Capabilities



| Feature | Description |
| :--- | :--- |
| **🧠 Recursive Intelligence** | Powered by **Gemma 2 (9B)** (Local) or **Groq LPUs** (Cloud). Evolves with every interaction. |
| **🛡️ The $P(G)$ Equation** | A logic gate that calculates the *Probability of Goodness* before executing any high-risk action. |
| **👁️ Moltbot Vision** | A headless Chromium browser that navigates, takes screenshots, and extracts OSINT data autonomously. |
| **💾 ChromaDB Memory** | Long-term vector storage (RAG) allows OpenZero to ingest documents, recall history, and cite sources. |
| **📱 Telegram Uplink** | Connect your node to BotFather for secure, remote control via your smartphone. |
| **☣️ Terminal Sovereignty** | **[WARNING]** OpenZero can execute `bash` commands, manage files, and control servers via SSH. It is a SysAdmin, not a chatbot. |

---

## 🚀 Bare Metal Deployment (For Existing Servers)

If you already have a Linux server (Ubuntu/Debian/AlmaLinux/Mint) with at least **16GB RAM** and **30GB Disk Space**, you can deploy the OpenZero software directly.

### The 1-Click Installer
Deploy the entire lattice, including the Node.js Vision systems and Python Brain, with a single command:

```bash
curl -sL [https://openzero.talktoai.org/install.sh](https://openzero.talktoai.org/install.sh) | bash
🔄 Updating the Node
OpenZero receives constant upgrades. To update your existing node to the latest Lattice version without losing your configuration or .env keys, simply re-run the installation command above.

🖥️ The Optimal Environment (DIY RDP Server)
To get the absolute most out of OpenZero, we highly recommend replicating the core development environment: a dedicated Virtual Private Server (VPS) or Virtual Machine (VM) running Linux Mint with Remote Desktop Protocol (XRDP) enabled.

This gives you a robust, isolated graphical workspace tailored for advanced AI research.

Step 1: Provision Your Infrastructure
Rent a VPS or VM. You need a reliable provider that allows custom OS installations or provides Linux Mint templates. (We run OpenZero on 32GB KVM nodes).

Step 2: Install XRDP (Remote Desktop)
Connect to your new server via SSH and execute the following commands to install xrdp, allowing you to see the graphical desktop from anywhere in the world:

Bash
# Update your package list
sudo apt update

# Install the XRDP package
sudo apt install xrdp -y

# Enable XRDP to start automatically on boot
sudo systemctl enable xrdp
sudo systemctl start xrdp

# Configure the firewall to allow RDP traffic (Crucial for security)
sudo ufw allow 3389/tcp
sudo ufw reload
Step 3: Connect & Deploy
Open your preferred Remote Desktop Client (Windows RDC, Remmina, etc.).

Enter your server's public IP address and log in.

Open a terminal inside the desktop and run the 1-Click Installer.

🎛️ Lattice Management (PM2)
OpenZero runs silently in the background using the PM2 process manager. Use these commands in your terminal to control the AI:

pm2 status - View the health, CPU, and RAM usage of the agent.

pm2 restart all - Master reset for both the Brain and Vision systems.

pm2 logs - Watch the live matrix feed of the AI's internal thought process.

<div align="center">
<img src="https://github.com/ResearchForumOnline/AgentZERO/blob/main/Screenshot_18.png" width="400" alt="UI Element 1">
<img src="https://github.com/ResearchForumOnline/AgentZERO/blob/main/Screenshot_20.png" width="400" alt="UI Element 2">



<img src="https://github.com/ResearchForumOnline/AgentZERO/blob/main/Screenshot_22.png" width="400" alt="UI Element 3">
<img src="https://github.com/ResearchForumOnline/AgentZERO/blob/main/Screenshot_23.png" width="400" alt="UI Element 4">



<img src="https://github.com/ResearchForumOnline/AgentZERO/blob/main/Screenshot_6.png" width="804" alt="Terminal Logs">
</div>
