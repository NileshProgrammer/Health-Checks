#!/usr/bin/env python3
import os
import sys

# Check Reboot function
def check_reboot():
    """ Return True if the computer has pending reboot."""
    return os.path.exists("/run/reboot-requires")


def main():
    if check_reboot():
        print("Pending Reboot")
        sys.exit(1)
    print("Everything is OK...")
    sys.exit(0)


main()
