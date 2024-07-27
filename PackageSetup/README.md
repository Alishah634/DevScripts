# Development Environment Setup Scripts

## Overview

This repository contains scripts to quickly set up a Python development environment by installing all necessary packages listed in a requirements file. These scripts aim to simplify the initial setup process for any Python project, ensuring that all required packages are installed efficiently without multiple pip install commands. Additionally, example dependency and requirements files are provided to demonstrate usage.

## Files Included

### 1. SetupPythonEnv.sh

A Bash script that installs all the Python packages listed in `requirements_example.txt`. This script allows users to start a project quickly without needing to run multiple pip install commands.

### 2. SetupPythonEnv.py

A Python script that performs the same function as `SetupPythonEnv.sh`, installing all the Python packages listed in `requirements_example.txt`. This script is useful for users who prefer using Python for their setup tasks.

### 3. dependency_example.txt

An example file demonstrating the output of the scripts, providing users with information about their dependency tree. This file serves as a guide to understanding the dependencies involved in their project.

### 4. requirements_example.txt

An example requirements file containing a large number of commonly used Python packages. This file is necessary for the installation scripts to work. Users can replace this file with their own `requirements.txt` to suit their specific project needs.

## Purpose

The primary purpose of this repository is to provide a quick and efficient way to set up a Python development environment by installing all necessary packages listed in a requirements file. This ensures that users can start working on their projects without the hassle of manually installing each package.

## Usage

Remember for both scripts it is necessary to have your packages in `requirements.txt` not `requirements_example.txt` that is only for demonstration purpose, to use that file rename it `requirements.txt`. You can also just edit the scripts, to use `requirements_example.txt` rather than `requirements.txt` this is completely upto you. 

### Running the Bash Script

1. Ensure that `SetupPythonEnv.sh` is executable. If not, run:

```sh {"id":"01J3SWMN466X75EKY7NYHX6GC4"}
chmod +x SetupPythonEnv.sh
```

2. Execute the script:

```sh {"id":"01J3SWMN466X75EKY7P1Y5594Y"}
./SetupPythonEnv.sh
This will install all packages listed in `requirements.txt`.

## Running the Python Script
Ensure that Python is installed on your system.

Execute the script:
```sh
python SetupPythonEnv.py
This will install all packages listed in requirements.txt.


```

## Customizing Requirements
Replace `requirements_example.txt` with your own `requirements.txt` to install specific packages for your project. Ensure that the file is in the same directory as the scripts.

## System Requirements
- Python 3.x
- pip (Python package installer)
- Bash (for running the Bash script)

## Potential Issues
- **Permission Denied Error:** If you encounter a permission denied error while running the Bash script, ensure that the script has executable permissions by running `chmod +x SetupPythonEnv.sh`.
- **Missing pip:** If pip is not installed, the scripts will fail. Install pip by following the instructions at [pip installation guide](https://pip.pypa.io/en/stable/installation/).
- **Package Conflicts:** If there are conflicts between packages in the `requirements_example.txt`, resolve them by updating the requirements file with compatible versions.
- Using the `requirements_example.txt` as your projects' `requirements.txt` may take a while to install as it is a very large file with many packages, meant to be used if setting up python packages on a new device or for the first time.

## Example Files
The `.txt` files provided are examples. The `requirements_example.txt` is designed to allow any user who installs the packages on that list to start any project with little need to pip install additional packages. Users are encouraged to replace these example files with their own specific requirements and dependencies.

## Contributions
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

Hope this helps, and thank you for using our setup scripts!
