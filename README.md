# INET4031 Add Users Script and User List

## Program Description
The `create-users.py` script is a Python-based automation tool designed to streamline the process of managing user accounts on an Ubuntu system. In a professional environment, manually adding dozens or hundreds of users is inefficient and prone to human error. This program replaces the manual repetition of the `sudo adduser` and `sudo usermod` commands by reading user data from a structured input file.

Under the hood, the script utilizes the same standard Linux commands you would use at the CLI:
* **`adduser`**: To create the user, set their password, and build their home directory.
* **`usermod`**: To assign the user to specific groups.
* **`chown/chmod`**: To ensure proper directory permissions.

By wrapping these commands in a Python loop, the script ensures every user is created with consistent settings in a fraction of the time.

## Program User Operation
To use this program, the administrator must provide an input file containing the user details and then execute the Python script via the terminal. The script parses the input, validates the data, and interfaces with the system's user management utilities.

### Input File Format
The script reads from a file (typically `create-users.input`) where each line represents a single user. The fields are comma-delimited in the following order:
`username, password, group1, group2, ...`

* **Skipping Lines**: If a line begins with a `#` character, the script treats it as a comment and skips it.
* **No Groups**: If you do not want a user added to any secondary groups, simply leave the fields after the password blank (e.g., `user01, password123`).

### Command Execution
Before running the script, ensure the file has execution permissions. You can set this using:
`chmod +x create-users.py`

To run the script and feed it the input file, use the following redirection command:
`sudo ./create-users.py < create-users.input`

*Note: Administrative (sudo) privileges are required because the script modifies system files like `/etc/passwd` and `/etc/group`.*

### "Dry Run"
The script includes a "Dry Run" feature for safety. When enabled (usually by a toggle variable inside the code or a command-line flag), the script will print the commands it **intends** to run to the screen without actually executing them. This allows the administrator to verify the input file logic before making permanent changes to the system.
