#!/usr/bin/env python3
import os
import sys
import shutil
import psutil
import socket

# Check Reboot function
def check_reboot():
    """ Return True if the computer has pending reboot."""
    return os.path.exists("/run/reboot-requires")


# check disk usage
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


# check cpu usage
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75


def check_root_full():
    """
    Return True if the root partition is full, false otherwise.
    """
    return check_disk_usage("/")


def check_no_network():
    """
    Return True if its resolve Google URL
    """
    try:
        socket.gethostbyname("wwww.google.com")
        return False
    except:
        return True


# Main Function
def main():

    if check_reboot() or check_root_full() or check_no_network():
        print("Pending Reboot and it need to be restarted.....")
        sys.exit(1)
    print("Everything is OK...")

    if not check_disk_usage("/") or not check_cpu_usage():
        print("ERROR!")
    sys.exit(0)


main()
