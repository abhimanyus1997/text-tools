import os
from pathlib import Path
import logging

# Author: Abhimanyu Singh
# GitHub: https://github.com/abhimanyus1997
# LinkedIn: www.linkedin.com/in/abhimanyus1997

# Configure logging for the project
logging.basicConfig(level=logging.INFO, format="[%(asctime)s - %(name)s]: %(message)s:")

project_name = "text-tools"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/tests.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name

    # Create directory if it doesn't exist
    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created Directory: {filedir}")

    # Create empty file if it doesn't exist or is empty
    if not filepath.exists() or os.path.getsize(filepath) == 0:
        with open(filepath, 'w'):
            pass
        logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
