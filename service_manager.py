import subprocess

CONFIG_FILE = "/etc/suricata/suricata.yaml"

def validate_config():
    print("[*] Validating Suricata config...")
    result = subprocess.run(
        ["suricata", "-T", "-c", CONFIG_FILE],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("[-] Config validation failed:\n", result.stderr)
        return False
    print("[+] Config validation successful.")
    return True

def restart_suricata():
    restart = input("Restart Suricata service now? (y/n) [y]: ").strip().lower() or "y"
    if restart == "y":
        if validate_config():
            subprocess.run(["systemctl", "restart", "suricata"])
            print("[+] Suricata restarted.")
        else:
            print("[-] Not restarting Suricata because config is invalid. Backup is available.")
