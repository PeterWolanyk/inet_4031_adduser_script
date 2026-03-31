# INET4031 — Add Users Script & User List

A Python-based automation tool for bulk user account creation on Ubuntu Linux. Built for INET4031 (Spring 2026).

---

## Overview

Manually provisioning user accounts one at a time is slow and error-prone. `create-users.py` automates the entire process — reading a structured input file and executing the necessary Linux commands to create accounts, set passwords, and assign group memberships in a single pass.

> **Note:** This script manages *users only*. All groups referenced in the input file must already exist on the system before running the script. The script will fail if a group does not exist.

---

## How It Works

For each valid entry in the input file, the script executes three system-level operations:

1. **Creates the user** — Runs `adduser` with the provided username, first name, and last name
2. **Sets the password** — Pipes the password via `echo` into `/usr/bin/passwd` for the target user
3. **Assigns group membership** — Runs `adduser` again to add the user to each specified group

---

## Input File Format

The script reads from `create-users.input`. Each line represents one user account using colon-delimited fields:
```
username:password:lastname:firstname:group1,group2,group3
```

| Field | Description |
|---|---|
| `username` | Login name for the new account |
| `password` | Initial password |
| `lastname` | User's last name |
| `firstname` | User's first name |
| `groups` | Comma-separated list of existing groups, or `-` for none |

### Examples

**Single group:**
```
user01:pass01:Last01:First01:sudo
```

**Multiple groups:**
```
user02:pass02:Last02:First02:sudo,developers
```

**No groups:**
```
user03:pass03:Last03:First03:-
```

**Skipped line (comment):**
```
#user04:pass04:Last04:First04:sudo
```

### Validation Rules

- Lines beginning with `#` are treated as comments and skipped
- Lines missing any of the 5 required fields are silently ignored
- Users that already exist on the system are skipped without notification

---

## Running the Script

### 1. Set execution permissions (first time only)
```bash
chmod +x create-users.py
```

### 2. Execute with input file
```bash
sudo ./create-users.py < create-users.input
```

> `sudo` is required — the script writes to `/etc/passwd` and `/etc/group`.

---

## Dry Run Mode

Before making permanent changes, you can verify exactly which commands will be executed without running them. In `create-users.py`, comment out the `os.system(...)` calls and uncomment the corresponding `print(...)` statements. Re-run the script normally — it will output the planned commands to the terminal instead of executing them.

---

## Verifying Results

After running the script, confirm that users and groups were created correctly:

**Check user account:**
```bash
grep <username> /etc/passwd
```

**Check group membership:**
```bash
grep <username> /etc/group
```
