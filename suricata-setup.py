#!/usr/bin/env python3
import os
import sys
from config_manager import load_config, save_config
from interface_manager import choose_interface
from rules_manager import select_rules
from service_manager import restart_suricata

# Relaunch with sudo if not root
if os.geteuid() != 0:
    print("[*] Relaunching with sudo using:", sys.executable)
    os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

def main():
    print("=== Suricata Interactive Setup ===\n")

    try:
        config = load_config()
    except FileNotFoundError:
        print("[-] Suricata config not found at /etc/suricata/suricata.yaml")
        return

    # Choose network interface
    iface = choose_interface()
    config["af-packet"] = [{"interface": iface}]

    # IDS or IPS mode
    mode = input("Run mode (ids/ips) [ids]: ").strip().lower() or "ids"
    if mode == "ips":
        config["af-packet"][0]["cluster-type"] = "cluster_flow"
        config["af-packet"][0]["copy-mode"] = "ips"
        config["af-packet"][0]["defrag"] = "yes"

    # Log directory
    log_dir = input("Log directory [/var/log/suricata]: ").strip() or "/var/log/suricata"
    config["default-log-dir"] = log_dir

    # Rules
    select_rules()

    # Save updated config
    save_config(config)

    # Restart service safely
    restart_suricata()

if __name__ == "__main__":
    main()
