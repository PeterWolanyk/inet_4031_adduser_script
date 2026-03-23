#!/usr/bin/python3

# INET4031
# Peter Wolanyk
# 03/22/2026
# 03/22/2026

import os
import re
import sys

def main():
    # --- INTERACTIVE MODE SELECTION ---
    # We open /dev/tty (the terminal) specifically to ask the Y/N question.
    # This prevents the script from accidentally reading the answer from the 
    # redirected input file (stdin).
    try:
        with open('/dev/tty', 'r') as tty:
            print("Would you like to run in dry-run mode? (Y/N): ", end='', flush=True)
            choice = tty.readline().strip().upper()
    except:
        choice = 'Y'  # Default to dry-run for safety if TTY is unavailable

    # Set a boolean 'flag' to act as a master switch for execution logic.
    is_dry_run = (choice == 'Y')

    for line in sys.stdin:
        match = re.match("^#", line)
        fields = line.strip().split(':')

        # --- DATA VALIDATION & SKIP LOGIC ---
        if match or len(fields) != 5:
            # Per Step 7 requirements: Only print skip/error messages during a dry-run.
            if is_dry_run:
                if match:
                    print(f"DEBUG: Skipping commented line: {line.strip()}")
                else:
                    print(f"ERROR: Line ignored (invalid field count): {line.strip()}")
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # Define the commands for user creation and password setting
        cmd_user = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        cmd_pw = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # --- EXECUTION LOGIC ---
        # If in dry-run mode, we display the commands without executing them.
        # If in normal mode, we hide the raw commands and execute using os.system.
        if is_dry_run:
            print(f"DRY-RUN: {cmd_user}")
            print(f"DRY-RUN: {cmd_pw}")
        else:
            print("==> Creating account for %s..." % (username))
            os.system(cmd_user)
            print("==> Setting the password for %s..." % (username))
            os.system(cmd_pw)

        for group in groups:
            if group != '-':
                cmd_group = "/usr/sbin/adduser %s %s" % (username, group)
                
                if is_dry_run:
                    print(f"DRY-RUN: {cmd_group}")
                else:
                    print("==> Assigning %s to the %s group..." % (username, group))
                    os.system(cmd_group)

if __name__ == '__main__':
    main()
