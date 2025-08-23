
import functionality.pathchecker as pathchecker
from config import MESSAGES
from color import Color

def getValidPaths():
    """ iteriert so lange bis die eingegebenen Pfade stimmen und geht dann zurück """
    CORRET_PATH = False

    while not CORRET_PATH:
        print(Color.BOLD + MESSAGES["welcome_image_input"] + Color.END)
        imageInputPath = input()

        if pathchecker.pathIsValid(imageInputPath):
            CORRET_PATH = True
        else:
            print ("______________________")
            print(MESSAGES["error_invalid_path"])

    print ("______________________")
    CORRET_PATH = False

    while not CORRET_PATH:
        print(MESSAGES["welcome_image_output"])
        imageOutputPath = input()

        if pathchecker.pathIsValid(imageOutputPath):
            CORRET_PATH = True

        else:
            print(MESSAGES["error_invalid_path"])

    print ("______________________")
    CORRET_PATH = False

    while not CORRET_PATH:
        print(MESSAGES["welcome_image_names_file"])
        imageNamePath = input()

        if pathchecker.pathIsValid(imageNamePath):
            CORRET_PATH = True

        else:
            print ("______________________")
            print(MESSAGES["error_invalid_path"])

    return [imageInputPath, imageOutputPath, imageNamePath]