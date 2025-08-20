import shutil
import os
from functionality.pathchecker import pathIsValidTextfile
import variables

#shutil.copyfile(src, dst)

def startCopying(paths, conventions):
    # Datei Zeile für Zeile
    with open(paths[variables.GlobalVariables.NAMEPATH], 'r') as file:
        for line in file:
            #print(line.strip()) # TODO: Prüfung einbauen, ob die eingelesenen Werte die richtige Form haben (je Zeile ein Wert und so)

            infix = line.strip()
            path = buildFinalPath(paths, infix, conventions)

            if not pathIsValidTextfile(path):
                return None
            
            print (infix)

def buildFinalPath(paths, infix, conventions):
    # PATH                     /   PREFIX  INFIX  POSTFIX
    # /Users/Matthes/Desktop   /   _MB06   231    .ARW           ### BEISPIEL ###
    print (paths[0] + "/" + conventions[0] + infix + conventions[1])
