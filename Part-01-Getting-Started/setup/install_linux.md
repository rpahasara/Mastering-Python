# 🐧 Python Setup for Linux

## ✅ Step 1: Check if Python is Preinstalled

Most Linux distros come with Python preinstalled. Check with:

```bash
python3 --version
```

If it's not installed, proceed to install it.

## ✅ Step 2: Install Python via Package Manager

For Debian/Ubuntu-based distros:

```bash 
sudo apt update
sudo apt install python3 python3-pip
```

For RHEL/CentOS/Fedora:

```bash
sudo dnf install python3 python3-pip
```

>🛠️ You might need sudo privileges for installation.

## ✅ Step 3: Verify Installation

```bash
python3 --version
pip3 --version
```
Expected output (version numbers may vary):

```bash
Python 3.11.6
pip 23.2.1
```
You’re now all set to write and run Python scripts on Linux! 🧑‍💻
