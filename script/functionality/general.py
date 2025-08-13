
import functionality.pathchecker as pathchecker
from config import MESSAGES

def getValidPaths():
    """ iteriert so lange bis die eingegebenen Pfade stimmen und geht dann zurück """
    CORRECT_PATHS = False

    while not CORRECT_PATHS:
        print(MESSAGES["welcome_image_input"])
        imageInputPath = input()

        if pathchecker.pathIsValid(imageInputPath):
            CORRECT_PATHS = True

        else:
            print(MESSAGES["error_invalid_path"])


    CORRECT_PATHS = False

    while not CORRECT_PATHS:
        print(MESSAGES["welcome_image_output"])
        imageOutputPath = input()

        if pathchecker.pathIsValid(imageOutputPath):
            CORRECT_PATHS = True

        else:
            print(MESSAGES["error_invalid_path"])

    return [imageInputPath, imageOutputPath]