import os
import time
import sys

def system_type(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def initialize_scan():
    os.system('clear' if os.name == 'posix' else 'cls')
    system_type("Checking system integrity...")
    time.sleep(0.5)
    system_type("Accessing kernel-level data...")
    time.sleep(0.8)
    system_type("Bypassing user ignorance... Done.")
    print("-" * 40)

def detect_distro():
    if os.name != 'posix':
        system_type("FATAL ERROR: This is not a Linux environment.")
        system_type("Why are you running this on a toy OS? 💀")
        return

    try:
        with open("/etc/os-release") as f:
            data = {}
            for line in f:
                if "=" in line:
                    key, val = line.rstrip().split("=", 1)
                    data[key] = val.replace('"', '')
            
            distro_name = data.get("PRETTY_NAME", "Unknown Entity")
            
            system_type(f"SENSORS DETECTED: {distro_name}")
            
            # Sok-sokan ngasih komentar berdasarkan distro
            if "arch" in distro_name.lower():
                system_type("STATUS: User thinks they are superior. Typical. 😹")
            elif "ubuntu" in distro_name.lower():
                system_type("STATUS: Basic user detected. Safe but boring.")
            else:
                system_type("STATUS: Interesting choice. Proceed with caution.")
                
    except Exception:
        system_type("CRITICAL FAILURE: System identity is corrupted or hidden.")

if __name__ == "__main__":
    initialize_scan()
    detect_distro()
    print("-" * 40)
    system_type("Scan complete. Don't break anything, human.")
