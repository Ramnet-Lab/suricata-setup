import psutil

def list_interfaces():
    return list(psutil.net_if_addrs().keys())

def choose_interface():
    interfaces = list_interfaces()
    if not interfaces:
        raise RuntimeError("No network interfaces found!")

    print("Available interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i+1}) {iface}")

    while True:
        try:
            choice = int(input("Select interface to monitor: ")) - 1
            return interfaces[choice]
        except (ValueError, IndexError):
            print("[-] Invalid choice, try again.")
