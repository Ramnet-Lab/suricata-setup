#!/usr/bin/env bash

set -e

echo "[*] Cleaning up old Suricata installs..."
# Stop Suricata if running
if systemctl is-active --quiet suricata; then
    sudo systemctl stop suricata
fi

# Disable service if enabled
if systemctl is-enabled --quiet suricata; then
    sudo systemctl disable suricata
fi

# Remove old packages
sudo apt purge -y suricata suricata-update || true
sudo apt autoremove -y
sudo apt clean

# Optionally back up old config (if exists)
if [ -f "/etc/suricata/suricata.yaml" ]; then
    TS=$(date +%Y%m%d_%H%M%S)
    echo "[*] Backing up old config to /etc/suricata/suricata.yaml.backup.$TS"
    sudo cp /etc/suricata/suricata.yaml /etc/suricata/suricata.yaml.backup.$TS
    sudo rm -f /etc/suricata/suricata.yaml
fi

echo "[*] Updating system..."
sudo apt update && sudo apt upgrade -y

echo "[*] Installing dependencies..."
sudo apt install -y software-properties-common \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev \
    wget curl llvm libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
    git python3 python3-pip python3-venv

echo "[*] Installing Suricata (from Ubuntu repository)..."
sudo apt install -y suricata suricata-update

echo "[*] Enabling and starting Suricata service..."
sudo systemctl enable suricata
sudo systemctl start suricata

echo "[*] Installing Emerging Threats Open rules..."
sudo suricata-update update-sources
sudo suricata-update enable-source et/open
sudo suricata-update

echo "[*] Checking Suricata version..."
suricata --build-info | head -n 10

echo "[+] Suricata installation complete!"
echo "[*] Config file: /etc/suricata/suricata.yaml"
echo "[*] Logs: /var/log/suricata/"
echo "[*] Rules installed from Emerging Threats Open"
echo "[*] Validate config: sudo suricata -T -c /etc/suricata/suricata.yaml -v"

echo ""
echo "[*] Launching interactive Suricata setup..."
echo ""

# Run the interactive setup tool
if [ -f "./suricata-setup.py" ]; then
    chmod +x ./suricata-setup.py
    ./suricata-setup.py
else
    echo "[-] suricata-setup.py not found in current directory."
    echo "    Please clone/copy the setup utility here before running install.sh"
fi
