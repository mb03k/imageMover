import time
import functionality.general as general
from config import MESSAGES

selected_language = "de"
paths = ["", ""]

def main():
    print(MESSAGES["welcome_message"])

    time.sleep(1)
    
    paths = general.getValidPaths()

main()