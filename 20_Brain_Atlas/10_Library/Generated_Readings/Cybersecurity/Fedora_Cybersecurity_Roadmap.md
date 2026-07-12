---
type: generated_reading
title: Fedora Cybersecurity Roadmap
topic: "Starting Cybersecurity with Fedora Linux"
requested_on: "2026-07-13"
prompt: "Start learning cybersecurity using Fedora Linux on a laptop"
status: done
tags: [cybersecurity, linux, fedora, roadmap]
promoted_to: []
---

## The reading

### 1. Introduction: Fedora as a Cybersecurity Lab
Fedora Linux is an outstanding distribution for learning cybersecurity. Unlike distributions designed specifically for offensive security (such as Kali Linux or Parrot OS), which are configured out-of-the-box for running exploits and come with hundreds of pre-installed hacking tools, Fedora is a standard, secure-by-default, and bleeding-edge Linux OS. This characteristics make Fedora a superior learning platform: it forces you to understand **how Linux works** under the hood, how defensive security (like SELinux) is implemented, and how to safely install and isolate offensive security tools using modern containerization rather than cluttering your base operating system.

When learning cybersecurity, a strong grasp of Linux system administration, service configuration, and security controls is essential before diving into hacking or vulnerability exploitation. Fedora provides the perfect playground for this.

---

### 2. Core Pillars of Cybersecurity
To build a sustainable learning journey, a beginner should focus on four foundational pillars:

| Pillar                                | Focus Area                                                                               | Why It Matters                                                                     | Fedora Practice                                                                           |
| :------------------------------------ | :--------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **Linux Foundations**                 | User permissions, systemd services, SSH, logs (`journalctl`), file structures.           | Hacking is often about manipulating OS files and processes.                        | Managing firewalls (`firewalld`), customizing `sudoers`, examining auth logs.             |
| **Networking Basics**                 | TCP/IP model, routing, DNS, HTTP/HTTPS, ICMP, DHCP, Wireshark packet capture.            | Exploiting or securing systems requires understanding how they talk to each other. | Using `ss -tulpn` to check open ports; capturing traffic with `tshark`/`wireshark`.       |
| **Cryptography**                      | Hashing (MD5, SHA-256), symmetric/asymmetric encryption, SSL/TLS, certificates, OpenSSL. | Crucial for understanding data confidentiality, integrity, and authentication.     | Generating SSH keypairs, hashing files, checking web certificates via `openssl s_client`. |
| **SELinux (Security-Enhanced Linux)** | Mandatory Access Control (MAC) vs Discretionary Access Control (DAC), policies.          | Fedora enables SELinux by default. It restricts what applications can do.          | Managing SELinux contexts with `semanage` and debugging blocks via `sealert`.             |

---

### 3. Practical Fedora Lab Setup
A critical skill in security is maintaining a clean, isolated environment. Installing pentesting tools directly on your main host is generally discouraged because many of them have weak security or complex dependencies. 

Instead, you can leverage Fedora's native support for **Podman** (a daemonless, rootless container engine that acts as a drop-in replacement for Docker):

1. **Setting up Podman:**
   ```bash
   sudo dnf install -y podman
   ```
2. **Spinning up a Kali Linux shell in a container:**
   ```bash
   podman run --rm -it docker.io/kalilinux/kali-rolling /bin/bash
   ```
   This gives you a fully isolated container environment where you can install any offensive tools (like `nmap`, `metasploit-framework`, `sqlmap`) via `apt-get` without modifying or endangering your host OS files.

3. **Installing Network Tools on Fedora Host:**
   Some safe, essential networking tools should be installed on your host system:
   ```bash
   sudo dnf install -y nmap wireshark tcpdump
   ```
   *Note:* Add your user to the `wireshark` group to capture packets without running the UI as root:
   ```bash
   sudo usermod -aG wireshark $USER
   ```
   *(Re-login or run `newgrp wireshark` to apply).*

---

### 4. Recommended First Steps & Exercises
If you are starting from scratch, avoid jump-starting straight into complex exploits. Build up your muscle memory step-by-step:

*   **Linux Command Line Mastery:** Play [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/). It is a text-based wargame designed for beginners that teaches SSH, finding files, decoding data, and basic scripting.
*   **Active Recall & Networking:** Before exploring exploits, learn what "normal" looks like. Capture your own browser traffic using `Wireshark` and try to identify the TLS handshake, DNS requests, and TCP segments.
*   **Web Application Security:** Register at the [PortSwigger Web Security Academy](https://portswigger.net/web-security). It offers free, high-quality, hands-on labs starting from fundamental web vulnerabilities like SQL Injection, Cross-Site Scripting (XSS), and Broken Authentication.
*   **General Security Concepts:** Use [TryHackMe](https://tryhackme.com/) for gamified, guided paths. It is highly recommended for beginners because it provides clear text descriptions before asking questions or assigning practical targets.

---

### 5. Leveraging Existing Vault Resources
You do not have to start from an empty slate. Your vault already contains structured lecture guides and notes on networking and security concepts:
*   [[Cybersecurity_Roadmap]] — A generic, time-independent, dependency-based skill tree to guide your progression.
*   [[(Week 14) Network Security Complete Guide]] — A reference sheet detailing security threats, vulnerabilities, malware categorization, and mitigations.
*   [[(CN-14) Keamanan Jaringan Lecture Notes]] — The local language lecture logs mapping technology vs policy vulnerabilities, AAA security models, and basic firewall rules.

## Concepts to extract
- [ ] [[SELinux (Security-Enhanced Linux)]]
- [ ] [[Containerized Security Lab]]
- [ ] [[Linux Privilege Escalation]]
- [ ] [[Cybersecurity_Roadmap]]

