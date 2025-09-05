# Suricata Interactive Setup Tool

This project provides a modular, interactive command-line utility for configuring and managing Suricata on Ubuntu systems. It simplifies Suricata setup, ensures safe configuration updates, and validates changes before restarting the service.

---

## ✨ Features

* Interactive setup via prompts (choose interface, IDS/IPS mode, log directory, ruleset)
* Automatic backup of `/etc/suricata/suricata.yaml` before changes
* Ensures Suricata YAML headers (`%YAML 1.1` + `---`) are preserved
* Config validation with `suricata -T` before restarting service
* Safe service restart only on valid configs
* Modular design for easy extension
* Self-elevating script (automatically runs with `sudo`)

---

## 📂 Repository Structure

```
suricata-setup/
├── suricata-setup.py       # Main entrypoint script
├── config_manager.py       # Handles Suricata YAML load/save + backups
├── interface_manager.py    # Detects and selects network interface
├── rules_manager.py        # Handles rule source selection (ET Open, local)
├── service_manager.py      # Validates config and manages Suricata service
```

---

## 🚀 Installation

### 1. Clone Repo

```bash
git clone https://github.com/<your-repo>/suricata-setup.git
cd suricata-setup
```

### 2. Python Environment

It is recommended to use **pyenv** or a virtual environment.

Example with `venv`:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pyyaml psutil
```

### 3. Make Script Executable

```bash
chmod +x suricata-setup.py
```

---

## 🛠 Usage

Run the interactive setup:

```bash
./suricata-setup.py
```

The script will:

1. Relaunch with `sudo` if not root
2. Detect network interfaces and prompt selection
3. Ask for IDS or IPS mode
4. Ask for log directory
5. Let you choose rule source (ET Open or local)
6. Backup and update `/etc/suricata/suricata.yaml`
7. Validate config (`suricata -T`)
8. Restart Suricata service if config is valid

---

## 🔒 Safety Features

* **Backup**: Saves `.bak` file before each change
* **Validation**: Uses `suricata -T` before restart
* **Fail-Safe**: Will not restart Suricata if config is invalid

---

## 📝 Example Walkthrough

```
=== Suricata Interactive Setup ===

Available interfaces:
1) eth0
2) lo
Select interface to monitor: 1
Run mode (ids/ips) [ids]: ips
Log directory [/var/log/suricata]: /var/log/suricata

Rule sources:
1) Emerging Threats Open
2) Local rules
Select ruleset [1]: 1

[+] Backup saved: /etc/suricata/suricata.yaml.bak
[+] Config updated: /etc/suricata/suricata.yaml
[*] Validating Suricata config...
[+] Config validation successful.
Restart Suricata service now? (y/n) [y]: y
[+] Suricata restarted.
```

---

## 📌 Requirements

* Ubuntu (20.04+ recommended)
* Suricata installed (`sudo apt install suricata`)
* Python 3.8+
* Packages: `pyyaml`, `psutil`

---

## 📖 References

* [Suricata Documentation](https://suricata.io/documentation/)
* [PyYAML](https://pyyaml.org/)
* [psutil](https://github.com/giampaolo/psutil)

---

## 🔮 Future Enhancements

* Auto-restore last known good config if validation fails
* Support for advanced rule management (categories, enable/disable)
* Integration with ELK/Graylog for log monitoring
* TUI (text-based UI) for improved interaction
