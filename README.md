INET4031 Add Users Script and User List

Program Description
The create-users.py script is a Python-based automation tool designed to streamline user account management on Ubuntu. Manually adding dozens of users is inefficient and error-prone; this program automates the process by wrapping standard Linux commands like adduser and passwd into a robust Python loop.

By reading from a structured input file, the script ensures every user is created with consistent settings, home directories, and group memberships in a fraction of the time.

Program Operation
The administrator provides a structured input file and executes the script via the terminal. The script parses the input, validates the data fields, and interfaces with system utilities.

Input File Format
The script reads from a file (typically create-users.input) where each line represents a single user. Fields must be colon-delimited (:) in the following order:
username:password:lastname:firstname:group1,group2

Skipping Lines: Lines beginning with a # are treated as comments and skipped.

Group Handling: Secondary groups are comma-separated. If a user requires no secondary groups, use a - in the group field.

Validation: Lines missing any of the 5 required fields are automatically ignored to prevent system errors.

Command Execution
Before running, ensure the script has execution permissions:
chmod +x create-users.py

To execute the script and redirect the input file, use:
sudo ./create-users.py < create-users.input

Note: sudo privileges are required as the script modifies /etc/passwd and /etc/group.

"Dry Run" Safety
For safety, the script can be run in "Dry Run" mode by commenting out the os.system calls and enabling the print statements. This allows the administrator to verify exactly which commands will be executed before making permanent changes to the server.
