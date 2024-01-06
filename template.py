import os
from pathlib import Path
import logging

# loggin configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name= "textSummarizer"

# list of files required, helpful for ci/cd deployement

list_of_files= {
    ".github/workflow/.gitkeep", # automatically take code from github into deployemnt after commit
    f"src/{project_name}/__init__.py", # init is the constructor file nneded or local packets installion
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
    "research/trials.ipynb"
    
} 

# configure path to windows path, handle path issues

for filepath in list_of_files:
    filepath= Path(filepath) #,handle path issues
    filedir, filename= os.path.split(filepath) # separate folders and files
    
    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory: {filedir} for the  {filename} ")
        
    if( not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")