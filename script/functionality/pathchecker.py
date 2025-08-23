
import os 
from pathlib import Path

def pathIsValid(path):
    return os.path.exists(path) 

def pathIsFile(path):
    return Path(path).is_file()

def pathIsValidTextfile(path):
    endung = os.path.splitext(path)
    print ("Pfad: ",path)
    print("split: ",endung)
    return Path(path).is_file()