import yaml
import shutil

CONFIG_FILE = "/etc/suricata/suricata.yaml"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

def save_config(config):
    # Make a backup before writing
    backup = CONFIG_FILE + ".bak"
    shutil.copy(CONFIG_FILE, backup)
    print(f"[+] Backup saved: {backup}")

    with open(CONFIG_FILE, "w") as f:
        # Suricata requires YAML header
        f.write("%YAML 1.1\n---\n")
        yaml.dump(config, f, default_flow_style=False)

    print(f"[+] Config updated: {CONFIG_FILE}")
