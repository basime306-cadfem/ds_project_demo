import os
from pathlib import Path
import logging

project_name = "ds_demo"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "DockerFile.dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"


]

for file_path in list_of_files:
    path = Path(file_path)
    folder_dir, file_name = os.path.split(path)

    if folder_dir!="":
        os.makedirs(folder_dir, exist_ok=True)
        logging.info(f"Creating directroy {folder_dir} for the file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"The file for {file_name} created at {file_path}")
    else:
        logging.info(f"File {file_name} already exists")

    
