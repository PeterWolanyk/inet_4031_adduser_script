#!/usr/bin/python3

# INET4031
# Peter Wolanyk
# 03/22/2026

# Import os for system execution, re for regex, and sys for reading stdin
import os
import re
import sys

def main():
    # Process the user data redirected into the script from stdin
    for line in sys.stdin:

        # Identify lines starting with '#' to allow for comments in the data file
        match = re.match("^#", line)

        # Remove trailing spaces and split the line into a list using colons as the delimiter
        fields = line.strip().split(':')

        # Skip current line if it is a comment or doesn't have exactly 5 fields
        # This prevents the script from crashing on empty lines or malformed data
        if match or len(fields) != 5:
            continue

        # Map data fields to variables for easier readability
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2]) # Standard /etc/passwd Full Name format

        # Split the group field by commas to handle multiple secondary group assignments
        groups = fields[4].split(',')

        # Execute the adduser command with a disabled password and pre-filled GECOS info
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)

        # Set the user password by piping the password string into the passwd utility
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)

        # Loop through each group and add the user to it
        for group in groups:
            # Check for a hyphen, which indicates no group assignment is needed
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()
