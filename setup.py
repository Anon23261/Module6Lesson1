# This script sets up a Python virtual environment and installs the necessary packages.

import os
import subprocess

# Step 1: Create a virtual environment
def create_virtual_environment(env_name='venv'):
    subprocess.run(['python', '-m', 'venv', env_name])

# Step 2: Activate the virtual environment
# Note: Activation is usually done manually in the terminal.

# Step 3: Install required packages
def install_packages():
    subprocess.run(['venv/Scripts/pip', 'install', 'requests'])

if __name__ == '__main__':
    create_virtual_environment()
    install_packages()
