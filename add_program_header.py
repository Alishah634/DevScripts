import os
import argparse
import datetime

# Define the function to add the comment block
def add_comment_block_to_file(file_path, author_name, version):
    file_path = os.path.abspath(file_path)
    print(file_path)
    # Get current date for the comment block
    creation_date = datetime.datetime.now().strftime("%m/%d/%y")
    last_edited_date = creation_date

    # Create the comment block template dynamically
    comment_block_template = f"""
#############################################################################################################################
# Author: {author_name}
# Date (MM/DD/YY): {creation_date}
#
# History of file:
# Last edited on {last_edited_date}
# Version: {version}
#
# Description:
# This script [briefly describe the purpose of the script, what it does, and any relevant details].
# 
# Usage:
# - [Include any important instructions, such as how to run the script, prerequisites, or dependencies].
#
# Dependencies:
# - [List any dependencies or libraries that the script requires, e.g., numpy, requests, etc.].
#
# Additional Notes:
# - [Any extra details that might be helpful, such as environment assumptions (e.g., Ubuntu 22.04), 
#   special configurations, or things to keep in mind while using the script].
#
#############################################################################################################################
"""
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file and read its current content
        with open(file_path, 'r') as file:
            content = file.read()

        # Prepend the comment block template to the content
        new_content = comment_block_template + "\n" + content

        # Write the new content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)

        print(f"Comment block added to {file_path}.")

    else:
        print(f"Error: The file {file_path} does not exist.")


# Set up argparse to handle command-line arguments
def main():
    # Default author name
    default_author = "Ali A. Shah"

    # Setting up the command-line arguments
    parser = argparse.ArgumentParser(description="Automatically add a comment block to a Python file, header for start of new file")
    
    # Adding arguments for the script
    parser.add_argument('--file_path', '-f', type=str, required=True, help='The path to the Python file')
    parser.add_argument('--author_name', type=str, default=default_author, help='The author of the script (default: Ali A. Shah)')
    parser.add_argument('--version', '-v', type=str, help='The version or description of the changes made')

    # Parse arguments
    args = parser.parse_args()
    if args.version is None:
        args.version = "1.0 - Initial version of utility functions such as"
    
    # Call the function to add the comment block with provided arguments
    add_comment_block_to_file(args.file_path, args.author_name, args.version)


if __name__ == '__main__':
    main()

