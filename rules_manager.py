import os

def select_rules():
    print("\nRule sources:")
    print("1) Emerging Threats Open")
    print("2) Local rules")
    choice = input("Select ruleset [1]: ").strip() or "1"

    if choice == "1":
        os.system("suricata-update")
        print("[+] Emerging Threats rules updated.")
    else:
        print("[*] Using local rules (make sure they're configured).")
