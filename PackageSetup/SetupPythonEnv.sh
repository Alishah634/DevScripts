#!/bin/bash

REQUIREMENTS_FILE="requirements.txt"

if [[ ! -f "$REQUIREMENTS_FILE" ]]; then
    echo "Requirements file '$REQUIREMENTS_FILE' not found."
    exit 1
fi

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing pipdeptree for dependency checking..."
python -m pip install pipdeptree

echo "Installing packages from '$REQUIREMENTS_FILE'..."
if ! python -m pip install -r "$REQUIREMENTS_FILE"; then
    echo "An error occurred while installing packages. Generating dependency tree..."
    python -m pipdeptree > dependencies.txt
    echo "Dependency tree generated in 'dependencies.txt'. Please check for conflicts."
    exit 1
fi

echo "All packages installed successfully."
