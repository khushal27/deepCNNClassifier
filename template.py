import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s] : %(message)s : ')

package_name = "deepClassifier"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constant/__init__.py",
    "test/__init__.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requiements.txt",
    "requiements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"                 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating folder: [ {filedir} ] for the file : [ {filename} ]")
    else:
        logging.info(f"folder: [ {filedir} ] already exists!!!")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass # help to create empty file
        logging.info(f"Creating empty file : [ {filepath} ]")
    else:
        logging.info(f"file : [ {filepath} ] already exists !!!")