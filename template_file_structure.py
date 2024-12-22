import os

def create_project_structure(base_dir: str):
    """
    Creates the directory structure for the project.

    Args:
        base_dir (str): The base directory for the project.
    """
    # Define the folder structure for the folders in the project directory
    # Replace the folders and their subfolders accordingly for your project
    folders = {
        "backend": [
            "routes",
            "models",
            "controllers",
            "utils"
        ],
        "frontend": [
            "components",
            "pages",
            "assets/css",
            "assets/js"
        ],
        "database": [],
        "game_engine": [
            "threejs_scripts",
            "assets/textures",
            "assets/models"
        ],
        "logs": []
    }

    # Create the directories
    for root, subdirs in folders.items():
        root_path = os.path.join(base_dir, root)
        os.makedirs(root_path, exist_ok=True)
        for subdir in subdirs:
            os.makedirs(os.path.join(root_path, subdir), exist_ok=True)

    # Print the structure
    print(f"Project structure created at: {base_dir}")
    for root, subdirs in folders.items():
        print(f"- {root}")
        for subdir in subdirs:
            print(f"  - {subdir}")

if __name__ == "__main__":
    # Set the base directory for the project
    project_folder_name = None # Replace with the desired project folder name
    assert project_folder_name != None, f"The project_folder_name is the root directory where the project folders reside, it should NOT be none!!!"
    base_dir = os.path.abspath(project_folder_name)
    
    # Create the project structure
    create_project_structure(base_dir)
