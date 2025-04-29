#!/usr/bin/env python3
# hello.py — Your First Python Script for DevOps

# Print a welcome message
print("🚀 Hello, DevOps World!")

# Use a variable
name = "DevOps Engineer"
print("Welcome,", name)

# Show basic system information (using built-in platform module)
import platform
import datetime

print("\n🔧 System Information:")
print("Operating System:", platform.system())
print("Python Version  :", platform.python_version())
print("Current Time    :", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# End message
print("\n✅ Script executed successfully.")
