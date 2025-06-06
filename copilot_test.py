import os
import time

def get_uptime():
    # For Linux systems
    if os.name == "posix":
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_str = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
            print(f"System Uptime: {uptime_str} (HH:MM:SS)")
    else:
        print("This script currently supports Linux systems only.")

if __name__ == "__main__":
    get_uptime()
