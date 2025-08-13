import time
import functionality.pathcatcher as pathcatcher
import functionality.nameconvention as nameconvention
import moveImage as mover
from variables import GlobalVariables as GV
from config import MESSAGES
import config as c

# TODO: 
# Ordner für ablageort der Bilder auf Wunsch erstellen (falls er nicht gefunden wurde)

def main():
    svar = GV("", "", "") # TODO: language abfragen

    print(MESSAGES["welcome_message"])

    time.sleep(0.5)
    
    paths = pathcatcher.getValidPaths() # gibt array zurüc
    svar.setPaths(paths)
    print (svar.paths)
    # conventions=[prefix, postfix]
    # conventions = nameconvention.getConventions()

    # mover.startCopying(paths, conventions)

    # p1 = GV("/bin", "/output", "de")
    # print (p1.paths," " ,p1.selected_language)

    # jetzt prüfen welche bilder man haben will
    # meine werden als _MB06210.ARW gespeichert
    # -> präfix & postfix sind (hoffentlich) immer statisc -> _MB06 -> .ARW
    # zahlen in Liste eingeben, welche dann nacheinander herausgesucht und kopiert werden

main()