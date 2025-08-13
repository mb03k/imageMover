import shutil
from functionality.pathchecker import pathIsFile

#shutil.copyfile(src, dst)

def startCopying(paths, conventions):
    # Datei Zeile für Zeile
    with open('testdatei.txt', 'r') as file: # TODO: Dateinamen in zentrale Datei verschieben
        for line in file:
            #print(line.strip()) # TODO: Prüfung einbauen, ob die eingelesenen Werte die richtige Form haben (je Zeile ein Wert und so)

            infix = line.strip()
            path = buildFinalPath(paths, infix, conventions)

            if pathIsFile(""):
                None

def buildFinalPath(paths, infix, conventions):
    # PATH                     /   PREFIX  INFIX  POSTFIX
    # /Users/Matthes/Desktop   /   _MB06   231    .ARW           ### BEISPIEL ###
    print (paths[0] + "/" + conventions[0] + infix + conventions[1])
