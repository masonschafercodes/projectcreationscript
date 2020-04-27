import os
from os import path

def create_dir():
    FOLDER_PATH = "C:/Users/mason/OneDrive/Development/'20/Personal"

    fname = input("What should I name the folder: ")


    try:
        if path.exists(f"{FOLDER_PATH + '/' + fname}"):
            print("Directory Already Exists")
            return
        else:
            os.mkdir(f"{FOLDER_PATH + '/' + fname}")
    except OSError:
        print(f"Creation of directory {FOLDER_PATH + '/' + fname} failed")
    else:
        print(f"Creation of directory {FOLDER_PATH + '/' + fname} successful")
        
def remove_dir():
    FOLDER_PATH = "C:/Users/mason/OneDrive/Development/'20/Personal"

    fname = input("What directory should I remove: ")


    try:
        if not path.exists(f"{FOLDER_PATH + '/' + fname}"):
            print("Directory Does Not Exist")
            return
        else:
            os.rmdir(f"{FOLDER_PATH + '/' + fname}")
    except OSError:
        print(f"Deletion of directory {FOLDER_PATH + '/' + fname} failed")
    else:
        print(f"Deletion of directory {FOLDER_PATH + '/' + fname} successful")
        

def create_readme(path):
    os.chdir()
        
create_dir()
remove_dir()