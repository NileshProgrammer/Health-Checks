#!/usr/bin/env python3
import os
import sys
import shutil
import psutil
from network import *

# Check Reboot function
def check_reboot():
    """ Return True if the computer has pending reboot."""
    return os.path.exists("/run/reboot-requires")


def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

#Check spu usage 
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75


# Main Function
def main():
    if check_reboot():
        print("Pending Reboot and it need to be restarted.....")
        sys.exit(1)
    print("Everything is OK...")
    sys.exit(0)

    if not check_disk_usage("/") or not check_cpu_usage():
        print("ERROR!")
    elif check_localhost() and check_connectivity():
        print("Everything ok.")
    else:
        print("Network Check failed.")


main()
