from config import MESSAGES

def getConventions():
    print ("______________________")
    print(MESSAGES["name_convention_prefix"])
    prefix = input()

    print ("______________________")
    print(MESSAGES["name_convention_postfix"])
    postfix = input()

    return [prefix, postfix]