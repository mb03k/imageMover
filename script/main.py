import time
import functionality.pathcatcher as pathcatcher
import functionality.nameconvention as nameconvention
import functionality.mover.moveImage as mover
from variables import GlobalVariables as GV
from config import MESSAGES
import config as conf
from color import Color 

# TODO: 
# Ordner für ablageort der Bilder auf Wunsch erstellen (falls er nicht gefunden wurde)

def main():
    svar = GV("", "", "", "") # TODO: language abfragen

    print(MESSAGES["welcome_message"])

    time.sleep(0.5)
    
    paths = pathcatcher.getValidPaths() # gibt array zurück
    svar.setPaths(paths)

    #conventions=[prefix, postfix]
    conventions = nameconvention.getConventions()

    mover.startCopying(paths, conventions)

    # jetzt prüfen welche bilder man haben will
    # meine werden als _MB06210.ARW gespeichert
    # -> präfix & postfix sind (hoffentlich) immer statisc -> _MB06 -> .ARW
    # zahlen in Liste eingeben, welche dann nacheinander herausgesucht und kopiert werden

main()