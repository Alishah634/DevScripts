import os
import subprocess
import sys

def install_python_packages(requirements_file='requirements.txt'):
    if not os.path.exists(requirements_file):
        print(f"Requirements file '{requirements_file}' not found.")
        return
    
    try:
        print(f"Installing packages from '{requirements_file}'...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])  # Upgrade pip
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
        print("All packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")

if __name__ == "__main__":
    install_python_packages()
