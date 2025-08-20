
class GlobalVariables:
    paths = ["", "", ""]
    selected_language = "de"
    INPUTPATH = 0
    OUTPUTPATH = 1
    NAMEPATH = 2

    def __init__(self, imageInputPath, imageOutputPath, imageNamePath, selectedLanguage):
        self.paths = [imageInputPath, imageOutputPath, imageNamePath]
        self.selected_language = selectedLanguage

    def setSelectedLanguage(self, selectedLanguage):
        self.selected_language = selectedLanguage

    def setPaths(self, paths):
        self.paths = paths
